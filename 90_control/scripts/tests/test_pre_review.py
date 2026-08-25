"""#515 回归：pre_review 机器预审管线（四判据+幂等附单+参考层纪律）。

运行：python -m pytest 90_control/scripts/tests/test_pre_review.py -q
沙盒：tmp git 仓+合成任务单，不碰真实 vault。
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import pre_review
import queue_transition as qt


def _git(repo: Path, *args: str):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, timeout=30)


def _repo_with_file(tmp_path: Path) -> Path:
    repo = tmp_path / "wiki"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "t")
    (repo / "kdo-tools").mkdir()
    (repo / "kdo-tools" / "tool.py").write_text("x=1\n", encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "init")
    return repo


GOOD_REPORT = """**完成内容**：改了工具。

**交付物**：
- `kdo-tools/tool.py`

**验证**：pytest 全过。

**边界**：未动其他。

**需要谁动作**：欧阳锋终审。
"""


def _task(tmp_path: Path, report: str, code_files=None) -> Path:
    cf = ""
    if code_files:
        cf = "code_files:\n" + "".join(f"- {c}\n" for c in code_files)
    tf = tmp_path / "task_t_515.md"
    tf.write_text(
        f"---\nid: 515\nassignee: huangyaoshi\nstatus: in_progress\n{cf}---\n\n# 任务\n\n## 执行报告\n\n{report}",
        encoding="utf-8")
    return tf


def test_clean_report_all_pass(tmp_path):
    repo = _repo_with_file(tmp_path)
    tf = _task(tmp_path, GOOD_REPORT)
    out = pre_review.run_pre_review(tf, wiki_root=repo)
    assert "✅ 1 个声明路径全部存在" in out
    assert "F-034 五字段在位" in out
    assert "无负向断言词" in out
    assert pre_review.PRE_REVIEW_DISCLAIMER in out  # 参考层声明必在


def test_missing_deliverable_flagged(tmp_path):
    """声称-交付差集：声称但文件不存在 → 🔴（#499 漏清单判法原型）。"""
    repo = _repo_with_file(tmp_path)
    report = GOOD_REPORT.replace("`kdo-tools/tool.py`", "`kdo-tools/tool.py`\n- `kdo-tools/ghost.py`")
    out = pre_review.run_pre_review(_task(tmp_path, report), wiki_root=repo)
    assert "🔴 声称但文件不存在: `kdo-tools/ghost.py`" in out


def test_untracked_deliverable_flagged(tmp_path):
    repo = _repo_with_file(tmp_path)
    (repo / "kdo-tools" / "new.py").write_text("y=2\n", encoding="utf-8")  # 存在但 untracked
    report = GOOD_REPORT.replace("`kdo-tools/tool.py`", "`kdo-tools/tool.py`\n- `kdo-tools/new.py`")
    out = pre_review.run_pre_review(_task(tmp_path, report), wiki_root=repo)
    assert "🔴 声称但未入仓（untracked）: `kdo-tools/new.py`" in out


def test_negative_claim_without_anchor_flagged(tmp_path):
    report = GOOD_REPORT + "\n补充：该功能确认缺失。\n"
    out = pre_review.run_pre_review(_task(tmp_path, report), wiki_root=_repo_with_file(tmp_path))
    assert "🔴" in out and "负向断言" in out


def test_no_deliverable_paths_no_check_surface(tmp_path):
    report = GOOD_REPORT.replace("**交付物**：\n- `kdo-tools/tool.py`", "**交付物**：本报告（纯任务单修改）")
    out = pre_review.run_pre_review(_task(tmp_path, report), wiki_root=_repo_with_file(tmp_path))
    assert "差集无检查面" in out


def test_attach_idempotent_and_before_review_section(tmp_path):
    tf = _task(tmp_path, GOOD_REPORT)
    tf.write_text(tf.read_text(encoding="utf-8") + "\n## 终审记录\n\n- 终审：待审\n", encoding="utf-8")
    r1 = pre_review.run_pre_review(tf, wiki_root=_repo_with_file(tmp_path))
    pre_review.attach_pre_review(tf, r1)
    pre_review.attach_pre_review(tf, r1)  # 重打不堆叠
    body = tf.read_text(encoding="utf-8")
    assert body.count(pre_review.PRE_REVIEW_HEADER) == 1
    # 位置：预审报告在终审记录之前
    assert body.index(pre_review.PRE_REVIEW_HEADER) < body.index("## 终审记录")
    # 终审记录内容完整保留
    assert "终审：待审" in body


# ── #515 终审 FAIL 返工回归：attach 防吞内容 ──

def test_prose_header_mention_no_swallow(tmp_path):
    """正文 prose 行内提及「## 机器预审报告」字样 → attach 正常且四字段存活
    （FAIL 根因：裸 find 把说明文字当既有节，删至文件尾吞掉五字段）。"""
    report = GOOD_REPORT + "\n管线行为说明：attach 幂等写入「## 机器预审报告」节（prose 提及非标题）。\n"
    tf = _task(tmp_path, report)
    pre_review.attach_pre_review(tf, pre_review.run_pre_review(tf, wiki_root=_repo_with_file(tmp_path)))
    body = tf.read_text(encoding="utf-8")
    for anchor in ("**交付物**", "**验证**", "**边界**", "**需要谁动作**", "**完成内容**"):
        assert anchor in body, f"{anchor} 被吞"
    assert body.count(pre_review.PRE_REVIEW_HEADER) == 2  # prose 提及 + 真实节
    assert "管线行为说明" in body  # prose 行完整存活


def test_fake_line_start_header_raises_no_write(tmp_path):
    """执行报告中段出现行首假标题（FAIL 原型形态）→ 截断吃掉后续字段时
    写后自检抛错拒绝落盘，原文件不动。"""
    report = ("**完成内容**：x。\n\n## 机器预审报告\n\n（生产者误手写的假标题行）\n\n"
              "**交付物**：本报告（纯任务单修改）\n\n**验证**：过\n\n**边界**：无\n\n**需要谁动作**：审\n")
    tf = _task(tmp_path, report)
    before = tf.read_text(encoding="utf-8")
    import pytest
    with pytest.raises(ValueError, match="防吞内容"):
        pre_review.attach_pre_review(tf, "x")
    assert tf.read_text(encoding="utf-8") == before  # 拒绝落盘=原文件零改动
