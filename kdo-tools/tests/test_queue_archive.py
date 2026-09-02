"""#453 队列归档瘦身测试：状态过滤/永不归档保护/对账一致/归档文件格式。

运行：python -m pytest kdo-tools/tests/test_queue_archive.py -q
"""
import importlib.util
import sys
from datetime import datetime, timedelta
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "queue_archive", Path(__file__).resolve().parent.parent / "queue-archive.py"
)
qa = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(qa)


def _make_env(tmp: Path, monkeypatch):
    """构造临时队列 + 任务单目录 + 归档目录（隔离环境，不碰真实队列）。

    日期全部相对「当前真实日期」动态推导（#627 口径②：归档文件按月命名按任务自身
    日期，断言随 fixture 推导不写死——跨月/跨年运行不漂移）。
    """
    queue = tmp / "production-queue.md"
    SEP = "|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|"
    old = datetime.now() - timedelta(days=60)       # 应归档（reviewed 超 14 天）
    strike_old = datetime.now() - timedelta(days=90)    # 应归档（超保留期；月份必≠主表行月）
    strike_recent = datetime.now() - timedelta(days=10)  # 保留（10 天 < 14 天判据恒成立）
    queue.write_text(
        "# 队列\n\n"
        "| # | 任务 | 名称 | 状态 | 负责人 | 交付物 | 依赖 | 任务单 | 备注 |\n" + SEP + "\n"
        "| 1 | `task_old_reviewed` | 旧 reviewed | reviewed | laowantong | x | 无 | t.md | 测试 |\n"
        "| 2 | `task_active_queued` | 活跃 queued | queued | huangyaoshi | x | 无 | t.md | 测试 |\n"
        "| 3 | `task_recent_reviewed` | 新 reviewed | reviewed | laowantong | x | 无 | t.md | 测试 |\n"
        "| 4 | `task_pending` | 待审 | pending_review | wangyuyan | x | 无 | t.md | 测试 |\n"
        "\n"
        "<!-- REVIEW-PENDING-BEGIN（queue_transition 自动维护，勿手改） -->\n"
        f"- ~~#1 task_old_reviewed｜hermes｜提审 06-01 10:00｜t.md~~ → 已终审 PASS A-（{strike_old:%Y-%m-%d} 欧阳锋）\n"
        f"- ~~#5 task_recent_strike｜hermes｜提审 08-20 10:00｜t.md~~ → 已终审 PASS A（{strike_recent:%Y-%m-%d} 欧阳锋）\n"
        "<!-- REVIEW-PENDING-END -->\n",
        encoding="utf-8")
    task_dir = tmp / "tasks"
    task_dir.mkdir()
    # 任务单 updated_at：task_old_reviewed 60 天前（应归档）；task_recent_reviewed 3 天前（保留）
    recent = datetime.now() - timedelta(days=3)
    (task_dir / "task_old_reviewed.md").write_text(
        f"---\nid: 1\nstatus: reviewed\nupdated_at: '{old:%Y-%m-%d}'\n---\n", encoding="utf-8")
    (task_dir / "task_recent_reviewed.md").write_text(
        f"---\nid: 3\nstatus: reviewed\nupdated_at: '{recent:%Y-%m-%d}'\n---\n", encoding="utf-8")
    (task_dir / "task_active_queued.md").write_text(
        "---\nid: 2\nstatus: queued\nupdated_at: '2026-01-01'\n---\n", encoding="utf-8")
    (task_dir / "task_pending.md").write_text(
        "---\nid: 4\nstatus: pending_review\nupdated_at: '2026-01-01'\n---\n", encoding="utf-8")
    archive = tmp / "archive"
    monkeypatch.setattr(qa, "QUEUE_FILE", queue)
    monkeypatch.setattr(qa, "TASK_DIR", task_dir)
    monkeypatch.setattr(qa, "ARCHIVE_DIR", archive)
    return queue, archive


def test_archive_only_old_reviewed(tmp_path, monkeypatch):
    queue, archive = _make_env(tmp_path, monkeypatch)
    rc = qa.run(dry_run=False, days=14, review_days=30, max_active=150)
    assert rc == 0

    text = queue.read_text(encoding="utf-8")
    assert "task_old_reviewed" not in text          # 旧 reviewed 已归档
    assert "task_active_queued" in text             # queued 永不归档
    assert "task_recent_reviewed" in text           # 新 reviewed 保留
    assert "task_pending" in text                   # pending_review 永不归档
    assert "task_old_reviewed" not in text.split("REVIEW-PENDING-BEGIN")[1]  # 旧划掉行归档
    assert "task_recent_strike" in text             # 保留期内划掉行保留

    # 口径②（#627）：归档命名按被归档任务自身日期归月（主表行=updated_at 月，划掉行=
    # 终审日期月），断言随 fixture 动态推导——跨月/跨年运行不漂移（09-01 起红根因）
    old_month = (datetime.now() - timedelta(days=60)).strftime("%Y-%m")
    af_main = archive / f"production-queue-{old_month}.md"
    assert af_main.exists()
    a_text = af_main.read_text(encoding="utf-8")
    assert "task_old_reviewed" in a_text            # 归档文件含移出的行（追加式不删内容）

    strike_month = (datetime.now() - timedelta(days=90)).strftime("%Y-%m")
    af_review = archive / f"production-queue-{strike_month}.md"
    assert af_review.exists()
    r_text = af_review.read_text(encoding="utf-8")
    assert "已终审 PASS A-（" in r_text             # 划掉行归终审日期月文件


def test_dry_run_no_write(tmp_path, monkeypatch):
    queue, archive = _make_env(tmp_path, monkeypatch)
    before = queue.read_text(encoding="utf-8")
    rc = qa.run(dry_run=True, days=14, review_days=30, max_active=150)
    assert rc == 0
    assert queue.read_text(encoding="utf-8") == before  # 演练不改文件
    assert not archive.exists()


def test_never_archive_active_statuses(tmp_path, monkeypatch):
    """永不归档保护：queued/pending_review 即使任务单超期也不动。"""
    queue, archive = _make_env(tmp_path, monkeypatch)
    # 把 queued 任务单也改成 60 天前（模拟超期）——仍不得归档
    qa.TASK_DIR.joinpath("task_active_queued.md").write_text(
        "---\nid: 2\nstatus: queued\nupdated_at: '2026-06-01'\n---\n", encoding="utf-8")
    qa.run(dry_run=False, days=14, review_days=30, max_active=150)
    assert "task_active_queued" in queue.read_text(encoding="utf-8")
