"""#647 回归：queue_transition seq 号寻址 + 多段表扫描（#645 friction 场景复现）。

用例②（任务单在 60_feedback/tasks/ 时 `claim <seq>` 可寻址）三层：
- parse_queue：表段被段间块（划销清单/PROPOSAL）打断时仍读全（#430-444/#647/#648 第二段实证）
- _resolve_task_ref：`647`/`#647` 解析成 task_id；数字未命中返回指路提示；完整 id 原样透传
- main() 全链路：`claim 647 --instance <名>` 落盘 in_progress（queue_transition 真实入口）

运行：python -m pytest 90_control/scripts/tests/test_seq_addressing_647.py -q
沙盒：monkeypatch qt/qg 模块全局 + tmp 队列/任务目录，不碰真实队列/看板。
"""
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_gate as qg
import queue_transition as qt

# 刻意复刻 production-queue.md 的断表形态：表段 → 非表行块 → 第二段表行
QUEUE_MD = (
    "| seq | task_id | 名称 | 状态 | assignee | 交付 | 依赖 | 任务单 | 备注 |\n"
    "|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|\n"
    "| 645 | `task_9999_seq_a` | 前置任务 | reviewed | huangyaoshi | x | 无 | `60_feedback/tasks/task_9999_seq_a.md` | r |\n"
    "| 647 | `task_9999_seq_probe` | queue门禁两小修 | queued | huangyaoshi | x | 无 | `60_feedback/tasks/task_9999_seq_probe.md` | r |\n"
    "\n"
    "<!-- REVIEW-PENDING-BEGIN -->\n"
    "- ~~[gate-blocked] xxx~~ → 划销（非表行中断块）\n"
    "## PROPOSAL-PENDING\n"
    "- **问题**：段间叙述行\n"
    "<!-- REVIEW-PENDING-END -->\n"
    "\n"
    "| 648 | `task_9999_seq_after_break` | 断点后行 | queued | huangyaoshi | x | 无 | `60_feedback/tasks/task_9999_seq_after_break.md` | r |\n"
)

TASK_FM = (
    "---\nid: {tid}\nseq: {seq}\nstatus: {status}\nassignee: huangyaoshi\n"
    "---\n\n# 任务\n\n## 动作\n\n修两处门禁逻辑。\n"
)


def _sandbox(tmp_path: Path, monkeypatch) -> dict:
    """tmp 队列 + tmp 任务目录 + qt/qg 全局打补丁（不动真实队列/看板/dashboard）。"""
    qdir = tmp_path / "60_feedback" / "tasks"
    qdir.mkdir(parents=True)
    (qdir / "task_9999_seq_probe.md").write_text(
        TASK_FM.format(tid="task_9999_seq_probe", seq=647, status="queued"), encoding="utf-8")
    qpath = tmp_path / "production-queue.md"
    qpath.write_text(QUEUE_MD, encoding="utf-8")

    real_parse = qg.parse_queue
    fake_parse = lambda *a, **k: real_parse(qpath)  # noqa: E731 默认参绑定绕不开，显式传沙盒路径
    monkeypatch.setattr(qg, "parse_queue", fake_parse)
    monkeypatch.setattr(qt, "parse_queue", fake_parse)
    monkeypatch.setattr(qt, "QUEUE_PATH", qpath)
    monkeypatch.setattr(qt, "TASK_DIR", qdir)
    monkeypatch.setattr(qt, "BATCH_DIR", tmp_path / "70_product" / "tasks")
    monkeypatch.setattr(qt, "_refresh_dashboard", lambda: None)  # 不覆写真实 dashboard.html
    return {"qpath": qpath, "qdir": qdir,
            "probe": qdir / "task_9999_seq_probe.md"}


def test_647_parse_queue_reads_across_table_break(tmp_path):
    """断表后行不丢：第二段表行（#648 位）必须被读出——#430-444/#647/#648 不可见实证。"""
    qpath = tmp_path / "production-queue.md"
    qpath.write_text(QUEUE_MD, encoding="utf-8")
    rows = qg.parse_queue(qpath)
    ids = [r["task_id"] for r in rows]
    assert len(rows) == 3
    assert "task_9999_seq_after_break" in ids  # break 语义下此行丢失


def test_647_resolve_task_ref_three_ways(tmp_path):
    """seq / #seq / 完整 id 三态解析；未命中给指路提示。"""
    qpath = tmp_path / "production-queue.md"
    qpath.write_text(QUEUE_MD, encoding="utf-8")
    rows = qg.parse_queue(qpath)
    assert qt._resolve_task_ref("647", rows)[0] == "task_9999_seq_probe"
    assert qt._resolve_task_ref("#647", rows)[0] == "task_9999_seq_probe"
    assert qt._resolve_task_ref("task_9999_seq_probe", rows)[0] == "task_9999_seq_probe"
    missing, hint = qt._resolve_task_ref("99999", rows)
    assert missing is None and "完整 task_id" in hint


def test_647_claim_by_seq_end_to_end(tmp_path, monkeypatch):
    """全链路：`claim 647 --instance <名>` → 任务单落盘 in_progress（60_feedback/tasks/ 单）。"""
    sb = _sandbox(tmp_path, monkeypatch)
    monkeypatch.setattr(sys, "argv",
                        ["queue_transition.py", "claim", "647", "--instance", "tester", "--no-commit"])
    assert qt.main() == 0
    body = sb["probe"].read_text(encoding="utf-8")
    assert "status: in_progress" in body
    assert "instance: tester" in body
    queue_text = sb["qpath"].read_text(encoding="utf-8")
    assert "claimed-tester" in queue_text


def test_647_claim_bad_seq_reports_hint(tmp_path, monkeypatch, capsys):
    """数字未命中 → 退出码 1 + 指路提示（消除坑失败的兜底话术）。"""
    _sandbox(tmp_path, monkeypatch)
    monkeypatch.setattr(sys, "argv",
                        ["queue_transition.py", "claim", "99999", "--instance", "tester"])
    assert qt.main() == 1
    assert "完整 task_id" in capsys.readouterr().err
