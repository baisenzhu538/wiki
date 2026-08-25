"""#522 回归：complete 门禁「交付物已入仓」校验（E040 机器兜底）。

三分支+L2 回放：
- 脏交付物（untracked/未提交改动）→ 拦截+补救指令
- 净交付物（已跟踪无脏）→ 通过
- 豁免声明（纯任务单修改）→ 通过+WARNING
- 识别不出路径 → 通过+WARNING（红线 4 不硬拦）
- #518 场景回放：untracked 清单提审 → 拦截

运行：python -m pytest 90_control/scripts/tests/test_complete_deliverable_gate.py -q
沙盒：tmp git 仓（git init+commit），不碰真实 wiki 仓。
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
    tf = tmp_path / "task_test_522.md"
    tf.write_text(
        "---\nid: 522\nstatus: in_progress\n---\n\n# 任务\n\n## 执行报告\n\n" + report_body,
        encoding="utf-8",
    )
    return tf


def test_dirty_deliverable_blocked(tmp_path):
    """未提交改动的交付物 → 拦截+补救指令可读。"""
    repo = _repo(tmp_path)
    (repo / "kdo-tools" / "tool.py").write_text("x=2\n", encoding="utf-8")  # 脏
    tf = _task(tmp_path, "**完成内容**：改工具\n\n**交付物**：\n- `kdo-tools/tool.py`\n\n**验证**：过\n")
    ok, msg, _warn = qt._check_deliverables_committed(tf, {}, wiki_root=repo)
    assert not ok
    assert "未提交改动" in msg and "git add" in msg and "git commit" in msg


def test_clean_deliverable_passes(tmp_path):
    repo = _repo(tmp_path)
    tf = _task(tmp_path, "**完成内容**：改工具\n\n**交付物**：\n- `kdo-tools/tool.py`\n\n**验证**：过\n")
    ok, _msg, warn = qt._check_deliverables_committed(tf, {}, wiki_root=repo)
    assert ok and "核验通过" in warn


def test_exempt_declaration_passes(tmp_path):
    repo = _repo(tmp_path)
    tf = _task(tmp_path, "**完成内容**：纯任务单修改（诊断类）\n\n**交付物**：本报告\n\n**验证**：过\n")
    ok, _msg, warn = qt._check_deliverables_committed(tf, {}, wiki_root=repo)
    assert ok and "豁免" in warn


def test_unrecognized_paths_warn_not_block(tmp_path):
    """红线 4：识别不出=WARNING 不硬拦。"""
    repo = _repo(tmp_path)
    tf = _task(tmp_path, "**完成内容**：x\n\n**交付物**：见上文描述（无路径）\n\n**验证**：过\n")
    ok, _msg, warn = qt._check_deliverables_committed(tf, {}, wiki_root=repo)
    assert ok and "未识别出文件路径" in warn


def test_518_replay_untracked_blocked(tmp_path):
    """L2 回放 #518：untracked 清单文件提审 → 拦截。"""
    repo = _repo(tmp_path)
    # 清单文件存在于工作区但从未 git add（#518 场景）
    (repo / "60_feedback").mkdir()
    (repo / "60_feedback" / "list.csv").write_text("a,b\n", encoding="utf-8")
    tf = _task(tmp_path, "**完成内容**：产清单\n\n**交付物**：\n- `60_feedback/list.csv`\n\n**验证**：过\n")
    ok, msg, _warn = qt._check_deliverables_committed(tf, {}, wiki_root=repo)
    assert not ok and "untracked" in msg


def test_auto_commit_files_excluded(tmp_path):
    """队列/看板/任务单自身=流转自动收口，不算交付物。"""
    paths = qt._extract_deliverable_paths(
        "**交付物**：\n- `70_product/tasks/production-queue.md`\n- `70_product/tasks/dashboard.html`\n"
        "- `task_test_522.md`（本任务单）\n- `kdo-tools/tool.py`\n\n**验证**：过\n",
        "task_test_522.md",
    )
    assert paths == ["kdo-tools/tool.py"]
