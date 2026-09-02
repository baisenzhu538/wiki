"""#625 任务2 回归：complete 门禁「交付物裸路径 loose-scan」（E040-loose WARNING）。

背景：#622 终审 FAIL 实证——交付物节路径未加反引号（kdo-tools/conveyor_probe.py 裸写），
反引号启发式全漏 → E040 vacuous 通过 → 哨兵代码未入仓照样提审。
loose-scan 兜底：反引号识别为空时按已知顶层目录扫裸路径，命中未入仓
→ WARNING 打印 + gate-warning 台账（不拦截，prop_20260902_ouyangfeng 口径）。

运行：python -m pytest 90_control/scripts/tests/test_complete_loose_deliverable_scan.py -q
沙盒：tmp git 仓（git init+commit），不碰真实 wiki 仓；台账走 task_9999_ 测试件分流。
"""
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_transition as qt


def _git(repo: Path, *args: str):
    subprocess.run(["git", "-C", str(repo), *args], check=True,
                   capture_output=True, timeout=30)


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "wiki"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "t")
    (repo / "kdo-tools").mkdir()
    (repo / "kdo-tools" / "tool.py").write_text("x=1\n", encoding="utf-8")
    _git(repo, "add", "kdo-tools/tool.py")
    _git(repo, "commit", "-m", "init")
    return repo


def _task(tmp_path: Path, report_body: str) -> Path:
    tf = tmp_path / "task_test_625.md"
    tf.write_text(
        "---\nid: task_9999_loose\nstatus: in_progress\n---\n\n# 任务\n\n## 执行报告\n\n" + report_body,
        encoding="utf-8",
    )
    return tf


def test_loose_dirty_warns_not_blocks(tmp_path):
    """#622 回放：裸路径（无反引号）+ 未提交改动 → 通过但 WARNING 命中未入仓清单。"""
    repo = _repo(tmp_path)
    (repo / "kdo-tools" / "tool.py").write_text("x=2\n", encoding="utf-8")  # 脏
    tf = _task(tmp_path, "**完成内容**：改工具\n\n**交付物**：kdo-tools/tool.py 加哨兵\n\n**验证**：过\n")
    ok, _msg, warn = qt._check_deliverables_committed(
        tf, {"id": "task_9999_loose"}, wiki_root=repo)
    assert ok  # WARNING 不拦截
    assert "E040-loose" in warn and "未提交改动: kdo-tools/tool.py" in warn


def test_loose_untracked_warns(tmp_path):
    """裸路径 + untracked（盘上存在未跟踪）→ WARNING。"""
    repo = _repo(tmp_path)
    (repo / "90_control").mkdir()
    (repo / "90_control" / "matrix.md").write_text("m\n", encoding="utf-8")
    tf = _task(tmp_path, "**完成内容**：登记\n\n**交付物**：90_control/matrix.md 行27\n\n**验证**：过\n")
    ok, _msg, warn = qt._check_deliverables_committed(
        tf, {"id": "task_9999_loose"}, wiki_root=repo)
    assert ok and "untracked: 90_control/matrix.md" in warn


def test_loose_clean_no_warning(tmp_path):
    """裸路径已入仓（干净）→ 回落原「未识别出」WARNING，不报错。"""
    repo = _repo(tmp_path)
    tf = _task(tmp_path, "**完成内容**：改工具\n\n**交付物**：kdo-tools/tool.py 已提交\n\n**验证**：过\n")
    ok, _msg, warn = qt._check_deliverables_committed(
        tf, {"id": "task_9999_loose"}, wiki_root=repo)
    assert ok and "未识别出文件路径" in warn and "E040-loose" not in warn


def test_loose_ghost_path_ignored(tmp_path):
    """幻觉路径（盘上不存在且未跟踪）→ 不查不告警（fail-open，防误报）。"""
    repo = _repo(tmp_path)
    tf = _task(tmp_path, "**完成内容**：x\n\n**交付物**：kdo-tools/nonexistent.py 计划中\n\n**验证**：过\n")
    ok, _msg, warn = qt._check_deliverables_committed(
        tf, {"id": "task_9999_loose"}, wiki_root=repo)
    assert ok and "未识别出文件路径" in warn


def test_loose_ledger_written_to_test_log(tmp_path):
    """WARNING 必留痕：task_9999_ 测试件 → gate-warning-test.log（#483 分流纪律）。"""
    repo = _repo(tmp_path)
    (repo / "kdo-tools" / "tool.py").write_text("x=2\n", encoding="utf-8")
    tf = _task(tmp_path, "**完成内容**：改工具\n\n**交付物**：kdo-tools/tool.py\n\n**验证**：过\n")
    qt._check_deliverables_committed(tf, {"id": "task_9999_loose"}, wiki_root=repo)
    log = qt.GATE_WARNING_TEST_LOG
    assert log.exists() and "task_9999_loose" in log.read_text(encoding="utf-8")
    # 真实台账不得被测试件污染
    real = qt.GATE_WARNING_LOG
    if real.exists():
        assert "task_9999_loose" not in real.read_text(encoding="utf-8")


def test_loose_skipped_when_backtick_paths_found(tmp_path):
    """反引号启发式有产出时 loose-scan 不启动（主路径 E040 硬拦截语义不变）。"""
    section = ("**交付物**：\n- `kdo-tools/tool.py` 和 90_control/matrix.md 裸路径\n\n**验证**：过\n")
    assert qt._extract_deliverable_paths(section, "task_test_625.md") == ["kdo-tools/tool.py"]
    # loose 版能从同一节补出裸路径（供兜底分支用）
    assert "90_control/matrix.md" in qt._extract_deliverable_paths_loose(section, "task_test_625.md")
