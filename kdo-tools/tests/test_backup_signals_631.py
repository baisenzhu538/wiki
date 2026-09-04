"""#631 回归：孤儿 backup 触发源配套探针信号——非节拍 commit 检测 + 守卫 SKIPPED 认跳拍。

背景：01:38 非节拍 backup commit（obsidian-git 10min 自备份，commitMessage 模板与
vault_git_backup.py 同文）收走 #628 在制品。三件套：触发源锁定（obsidian-git）+
第十二信号（非节拍 commit 检测）+ 第十信号 SKIPPED 口径细化（认跳拍不报停拍）。

运行：python -m pytest kdo-tools/tests/test_backup_signals_631.py -q
沙盒：tmp git 仓 + monkeypatch probe.ROOT，commit 时间戳用 GIT_COMMITTER_DATE 控制。
"""
import importlib.util
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)


def _git(repo: Path, *args: str, env_extra: dict | None = None):
    env = dict(os.environ)
    if env_extra:
        env.update(env_extra)
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True, timeout=30, env=env)


def _repo(tmp_path: Path, monkeypatch) -> Path:
    repo = tmp_path / "wiki"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "t")
    (repo / "logs").mkdir()
    monkeypatch.setattr(probe, "ROOT", repo)
    return repo


def _backup_commit_at(repo: Path, ts: datetime):
    """以指定 committer 时间落一条 'vault backup: <ts>' commit（与真实写手同消息格式）。"""
    (repo / "f.txt").write_text(str(ts.timestamp()), encoding="utf-8")
    _git(repo, "add", "f.txt")
    epoch = int(ts.timestamp())
    _git(repo, "commit", "-m", f"vault backup: {ts:%Y-%m-%d %H:%M:%S}",
         env_extra={"GIT_COMMITTER_DATE": f"@{epoch} +0800"})


def _prev_grid_ts(minute_shift: int = 0) -> datetime:
    """最近一个已过节拍点（:20/:50 格），可再平移分钟。"""
    now = datetime.now().replace(second=0, microsecond=0)
    candidates = [now.replace(minute=g) for g in probe._OFFBEAT_GRID_MINUTES]
    candidates += [(now - timedelta(hours=1)).replace(minute=g) for g in probe._OFFBEAT_GRID_MINUTES]
    past = max(c for c in candidates if c <= now - timedelta(minutes=1))
    return past + timedelta(minutes=minute_shift)


def test_offbeat_commit_alarmed_once(tmp_path, monkeypatch):
    """非节拍 commit（格点+15min）→ 告警一次（沿触发幂等，重报=噪声）。"""
    repo = _repo(tmp_path, monkeypatch)
    _backup_commit_at(repo, _prev_grid_ts(minute_shift=15))
    state: dict = {}
    alerts = probe._scan_offbeat_backup(state)
    assert len(alerts) == 1 and "非节拍" in alerts[0] and "孤儿写手" in alerts[0]
    assert probe._scan_offbeat_backup(state) == []  # 幂等不重复报


def test_onbeat_commit_no_alarm(tmp_path, monkeypatch):
    """格点上（:20/:50 ±10min 内）→ 不告警（schtasks 正常拍）。"""
    repo = _repo(tmp_path, monkeypatch)
    _backup_commit_at(repo, _prev_grid_ts(minute_shift=5))  # 格点+5min 容差内
    assert probe._scan_offbeat_backup({}) == []


def test_offbeat_window_expiry_rearm(tmp_path, monkeypatch):
    """脏→窗口过期全干净 → 重新武装（state 落回 False，可再报）。
    用独立旧仓模拟窗口过期（commit 落在 3h 窗外），不靠微窗口竞速。"""
    repo = _repo(tmp_path, monkeypatch)
    _backup_commit_at(repo, _prev_grid_ts(minute_shift=15))
    state: dict = {}
    assert probe._scan_offbeat_backup(state) != []
    assert state["offbeat_backup"] is True
    # 窗口过期：另一个仓只有 4h 前的非节拍 commit（滑出默认 3h 窗）→ 干净 → 重新武装
    repo2 = tmp_path / "wiki2"
    repo2.mkdir()
    _git(repo2, "init")
    _git(repo2, "config", "user.email", "t@t")
    _git(repo2, "config", "user.name", "t")
    monkeypatch.setattr(probe, "ROOT", repo2)
    _backup_commit_at(repo2, datetime.now() - timedelta(hours=4))
    assert probe._scan_offbeat_backup(state) == []
    assert state["offbeat_backup"] is False


def test_stall_with_recent_skip_not_alarmed(tmp_path, monkeypatch):
    """任务3：commit 停拍超阈但守卫 SKIPPED 行在窗内 = 主动跳拍（健康）→ 不报停拍。"""
    repo = _repo(tmp_path, monkeypatch)
    _backup_commit_at(repo, datetime.now() - timedelta(hours=30))  # 停拍 30h
    recent = datetime.now() - timedelta(hours=1)
    (repo / "logs" / "vault-git-backup.log").write_text(
        f"vault backup: {recent:%Y-%m-%d %H:%M:%S} SKIPPED（#628 活动会话 1：huangyaoshi(cli)）\n",
        encoding="utf-8")
    state: dict = {}
    assert probe._scan_backup_stall(state, max_age_h=24) == []
    assert state["backup_stall"] is False  # 认跳拍且重新武装


def test_stall_with_stale_skip_still_alarmed(tmp_path, monkeypatch):
    """SKIPPED 行也超窗（守卫本身停了）→ 停拍告警照报（守卫不能成停拍遮羞布）。"""
    repo = _repo(tmp_path, monkeypatch)
    _backup_commit_at(repo, datetime.now() - timedelta(hours=30))
    old = datetime.now() - timedelta(hours=26)
    (repo / "logs" / "vault-git-backup.log").write_text(
        f"vault backup: {old:%Y-%m-%d %H:%M:%S} SKIPPED（#628 活动会话 1：huangyaoshi(cli)）\n",
        encoding="utf-8")
    alerts = probe._scan_backup_stall({}, max_age_h=24)
    assert len(alerts) == 1 and "停拍" in alerts[0]


def test_stall_no_commit_no_skip_alarmed(tmp_path, monkeypatch):
    """原始场景不回归：无 commit 无 SKIPPED → 停拍告警（第十信号原语义保留）。"""
    repo = _repo(tmp_path, monkeypatch)
    _git(repo, "commit", "--allow-empty", "-m", "init",
         env_extra={"GIT_COMMITTER_DATE": f"@{int((datetime.now()-timedelta(hours=30)).timestamp())} +0800"})
    alerts = probe._scan_backup_stall({}, max_age_h=24)
    assert len(alerts) == 1
