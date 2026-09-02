"""#625 任务1 第二层回归：vault_git_backup 提交链路大文件门禁（>100MB 硬拦 / >15MB WARNING）。

背景：391MB zip 经 backup 脚本 add -A 静默入仓 → GitHub 100MB 硬限断 push 3 个月（2026-09-02 实证）。
口径：>100MB 移出暂存（工作区文件保留）+ 其余照提 + 台账留痕；>15MB WARNING 照提。

运行：python -m pytest kdo-tools/tests/test_vault_git_backup_gate.py -q
沙盒：tmp git 仓 + monkeypatch ROOT/GATE_LOG，不碰真实 wiki 仓。
大文件用 truncate 造逻辑大小（NTFS 稀疏写，秒级），门禁读的是 st_size 逻辑大小。
"""
import importlib.util
import json
import subprocess
import sys
import time
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "vault_git_backup", Path(__file__).resolve().parent.parent / "vault_git_backup.py"
)
vb = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(vb)


def _git(repo: Path, *args: str):
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True, timeout=30)


def _repo(tmp_path: Path, monkeypatch) -> Path:
    repo = tmp_path / "wiki"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "t")
    (repo / "small.txt").write_text("x\n", encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "init")
    monkeypatch.setattr(vb, "ROOT", repo)
    monkeypatch.setattr(vb, "GATE_LOG", tmp_path / "large-file-gate.log")
    return repo


def _big(repo: Path, rel: str, size: int) -> Path:
    p = repo / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("wb") as f:
        f.truncate(size)
    return p


def test_over_100mb_blocked_and_unstaged(tmp_path, monkeypatch):
    """>100MB：移出暂存（工作区保留）+ blocked 列表 + 台账 BLOCKED 行。"""
    repo = _repo(tmp_path, monkeypatch)
    big = _big(repo, "huge.zip", vb.HARD_LIMIT_BYTES + 1)
    _git(repo, "add", ".")
    blocked, warned = vb.gate_staged_large_files()
    assert blocked == ["huge.zip"] and warned == []
    assert big.exists()  # 工作区文件不动
    staged = _git(repo, "diff", "--cached", "--name-only").stdout
    assert "huge.zip" not in staged
    log = vb.GATE_LOG.read_text(encoding="utf-8")
    assert "BLOCKED｜huge.zip" in log


def test_over_15mb_warned_but_staged(tmp_path, monkeypatch):
    """>15MB 且 ≤100MB：WARNING 照提（不拦）+ 台账 WARNING 行。"""
    repo = _repo(tmp_path, monkeypatch)
    _big(repo, "video.mp4", vb.WARN_LIMIT_BYTES + 1)
    _git(repo, "add", ".")
    blocked, warned = vb.gate_staged_large_files()
    assert blocked == [] and warned == ["video.mp4"]
    staged = _git(repo, "diff", "--cached", "--name-only").stdout
    assert "video.mp4" in staged
    assert "WARNING｜video.mp4" in vb.GATE_LOG.read_text(encoding="utf-8")


def test_small_file_untouched(tmp_path, monkeypatch):
    repo = _repo(tmp_path, monkeypatch)
    (repo / "ok.md").write_text("ok\n", encoding="utf-8")
    _git(repo, "add", ".")
    blocked, warned = vb.gate_staged_large_files()
    assert blocked == [] and warned == []
    assert not vb.GATE_LOG.exists()  # 无命中不落台账


def test_main_commits_rest_when_big_file_blocked(tmp_path, monkeypatch):
    """端到端：大文件被拦 + 小变更照常 commit（硬拦文件 ≠ 停摆备份）。"""
    repo = _repo(tmp_path, monkeypatch)
    _big(repo, "huge.bin", vb.HARD_LIMIT_BYTES + 1)
    (repo / "small.txt").write_text("y\n", encoding="utf-8")  # 小变更
    monkeypatch.setattr(vb, "active_sessions", lambda: [])  # #628 守卫关（测试环境无关进程不干扰）
    rc = vb.main()
    assert rc == 0
    committed = _git(repo, "show", "--name-only", "--pretty=format:", "HEAD").stdout
    assert "small.txt" in committed and "huge.bin" not in committed
    assert (repo / "huge.bin").exists()


def test_main_only_big_change_no_commit(tmp_path, monkeypatch):
    """全部暂存变更被硬拦 → 不产生空 commit，rc=1 且 stderr 有提示。"""
    repo = _repo(tmp_path, monkeypatch)
    _big(repo, "huge.bin", vb.HARD_LIMIT_BYTES + 1)
    monkeypatch.setattr(vb, "active_sessions", lambda: [])  # #628 守卫关
    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()
    rc = vb.main()
    assert rc == 1
    assert _git(repo, "rev-parse", "HEAD").stdout.strip() == head_before


def _no_ambient_procs(monkeypatch):
    """屏蔽环境进程干扰：测试机/CI 上在跑的 claude/codex 会让守卫误跳拍。"""
    monkeypatch.setattr(vb, "_agent_processes", lambda: [])


def _write_registry(tmp_path: Path, monkeypatch, age_min: float):
    """写一个 tmp role-registry（单实例，心跳 age_min 分钟前）并挂到模块常量。"""
    reg = tmp_path / "role-registry.json"
    reg.write_text(json.dumps({"tester": {"instances": [
        {"tool": "cli", "kind": "cli", "heartbeat_ts": time.time() - age_min * 60}]}}),
        encoding="utf-8")
    monkeypatch.setattr(vb, "REGISTRY_FILE", reg)


def test_registry_fresh_skips_beat(tmp_path, monkeypatch, capsys):
    """#628 互撞防护：注册表心跳新鲜（5min）→ main 跳拍 SKIPPED 留痕，零 commit。"""
    repo = _repo(tmp_path, monkeypatch)
    _no_ambient_procs(monkeypatch)
    (repo / "wip.md").write_text("wip\n", encoding="utf-8")  # 未提交在制品
    _write_registry(tmp_path, monkeypatch, age_min=5)
    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()
    rc = vb.main()
    assert rc == 0
    assert _git(repo, "rev-parse", "HEAD").stdout.strip() == head_before  # 未收走
    assert "SKIPPED" in capsys.readouterr().out
    dirty = _git(repo, "status", "--porcelain").stdout
    assert "wip.md" in dirty  # 在制品原样留在工作区


def test_registry_stale_proceeds_to_commit(tmp_path, monkeypatch):
    """注册表心跳过期（60min）→ 不拦，正常快照 commit。"""
    repo = _repo(tmp_path, monkeypatch)
    _no_ambient_procs(monkeypatch)
    (repo / "done.md").write_text("done\n", encoding="utf-8")
    _write_registry(tmp_path, monkeypatch, age_min=60)
    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()
    rc = vb.main()
    assert rc == 0
    assert _git(repo, "rev-parse", "HEAD").stdout.strip() != head_before


def test_platform_instance_never_counts(tmp_path, monkeypatch):
    """platform（hermes 网关类）心跳再新鲜也不拦——常驻平台不是会话。"""
    reg = tmp_path / "role-registry.json"
    reg.write_text(json.dumps({"wangyuyan": {"instances": [
        {"tool": "hermes", "kind": "platform", "heartbeat_ts": time.time()}]}}),
        encoding="utf-8")
    monkeypatch.setattr(vb, "REGISTRY_FILE", reg)
    assert vb._registry_actives() == []


def test_cli_path_filter_pure():
    """进程面只认 CLI 路径特征（纯函数）：claude/codex/.kimi-code 算，kimi-desktop GUI 不算。"""
    out = ("ExecutablePath=C:\\Users\\Administrator\\AppData\\Roaming\\npm\\node_modules\\"
           "@anthropic-ai\\claude-code\\bin\\claude.exe\n"
           "ExecutablePath=C:\\Users\\Administrator\\AppData\\Local\\Programs\\kimi-desktop\\Kimi.exe\n"
           "ExecutablePath=C:\\Users\\Administrator\\.kimi-code\\bin\\kimi.exe\n"
           "ExecutablePath=C:\\Users\\Administrator\\AppData\\Roaming\\npm\\node_modules\\@openai\\codex\\"
           "node_modules\\@openai\\codex-win32-x64\\vendor\\x86_64-pc-windows-msvc\\bin\\codex.exe\n")
    assert vb._filter_cli_paths(out) == ["claude.exe", "codex.exe", "kimi.exe"]


def test_active_sessions_skip_integration(tmp_path, monkeypatch, capsys):
    """端到端：#628 活动会话存在（进程面命中）→ main 跳拍，工作区不被收走。"""
    repo = _repo(tmp_path, monkeypatch)
    (repo / "wip.md").write_text("wip\n", encoding="utf-8")
    monkeypatch.setattr(vb, "REGISTRY_FILE", tmp_path / "no-registry.json")  # 无注册表
    monkeypatch.setattr(vb, "_agent_processes", lambda: ["claude.exe"])
    head_before = _git(repo, "rev-parse", "HEAD").stdout.strip()
    rc = vb.main()
    assert rc == 0
    assert _git(repo, "rev-parse", "HEAD").stdout.strip() == head_before
    assert "SKIPPED" in capsys.readouterr().out
