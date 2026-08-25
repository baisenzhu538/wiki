"""#514 回归：quality_metrics 四类指标口径（spec v1）。

运行：python -m pytest kdo-tools/tests/test_quality_metrics.py -q
"""
import importlib.util
from datetime import date
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "quality_metrics", Path(__file__).resolve().parent.parent / "quality_metrics.py"
)
qm = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(qm)

QUEUE_FIXTURE = """# 队列

- ~~#1 task_a｜huangyaoshi｜提审 08-23 10:00｜p.md~~ → 已终审 PASS A（2026-08-23 欧阳锋）
- ~~#2 task_b｜laowantong｜提审 08-23 11:00｜p.md~~ → 终审退回 queued（2026-08-23 欧阳锋）
- ~~#2 task_b｜laowantong｜提审 08-24 09:00｜p.md~~ → 终审退回 queued（2026-08-24 欧阳锋）
- ~~#2 task_b｜laowantong｜提审 08-24 10:00｜p.md~~ → 已终审 PASS A-（2026-08-24 欧阳锋）
- ~~#3 task_c｜huangyaoshi｜提审 08-25 08:00｜p.md~~ → 已终审 PASS（2026-08-25 欧阳锋）
- ~~旧格式行不带提审标记~~ → 已处置（不匹配不计）
"""

GB_FIXTURE = """2026-08-23 14:15:21｜task_a｜F-034-五字段｜执行报告缺字段｜huangyaoshi
2026-08-24 09:00:00｜task_b｜F-035-意见书｜意见书缺锚点｜laowantong
2026-08-24 10:00:00｜task_x｜E040-交付物未入仓｜untracked｜huangyaoshi
2026-08-25 01:00:00｜task_y｜pre-submit｜lint｜laowantong
2026-08-25 02:00:00｜task_z｜L1-归档拒删｜核验未过｜huangyaoshi
坏行没有日期不应解析
"""

FORCE_FIXTURE = """2026-08-25 02:36:39｜task=task_a｜instance=huangyaoshi｜bypass= pending_review｜reason=老朱说继续
"""


def test_parse_queue_history():
    actions = qm.parse_queue_history(QUEUE_FIXTURE)
    assert len(actions) == 5  # 旧格式行不解析
    assert actions[1]["pass"] is False and actions[1]["terminal"] == date(2026, 8, 23)
    assert actions[0]["submit"] == date(2026, 8, 23)  # 年份从终审日推


def test_parse_gate_blocked_kinds():
    gates = qm.parse_gate_blocked(GB_FIXTURE)
    assert len(gates) == 5  # 坏行跳过
    kinds = [k for _, k in gates]
    assert kinds == ["F-034 五字段", "F-035 意见书", "E040 交付物入仓", "pre-submit", "其他(机器自报)"]


def test_parse_force():
    assert qm.parse_force_exceptions(FORCE_FIXTURE) == [date(2026, 8, 25)]


def test_fail_rate_action_level_vs_bounce_rate_task_level():
    """spec v1 关键差异：一单三轮 FAIL → FAIL 率计 3、打回率计 1（动作级≠单级）。"""
    actions = qm.parse_queue_history(QUEUE_FIXTURE)
    m = qm.compute_metrics(actions, [], [], date(2026, 8, 23), date(2026, 8, 25))
    # 终审动作 5（PASS 3 / 退回 2）
    assert m["review_actions"] == 5 and m["pass"] == 3 and m["fail"] == 2
    assert abs(m["fail_rate"] - 2 / 5) < 1e-9
    # 提审单 3（task_a/b/c 去重），被打回单 1（task_b）
    assert m["submitted_tasks"] == 3 and m["bounced_tasks"] == 1
    assert abs(m["bounce_rate"] - 1 / 3) < 1e-9


def test_block_rate_and_force_proxy():
    actions = qm.parse_queue_history(QUEUE_FIXTURE)
    gates = qm.parse_gate_blocked(GB_FIXTURE)
    forces = qm.parse_force_exceptions(FORCE_FIXTURE)
    m = qm.compute_metrics(actions, gates, forces, date(2026, 8, 23), date(2026, 8, 25))
    # 流转动作 = 提审 5 + 终审 5 = 10；拦截 5 → 50%
    assert m["flow_actions"] == 10 and m["gate_blocks"] == 5
    assert abs(m["block_rate"] - 0.5) < 1e-9
    assert m["gate_by_kind"]["F-034 五字段"] == 1
    # force 1 ÷ 拦截 5 = 20%
    assert abs(m["force_rate"] - 0.2) < 1e-9


def test_empty_window_no_crash():
    m = qm.compute_metrics([], [], [], date(2026, 8, 23), date(2026, 8, 25))
    assert m["fail_rate"] is None and m["bounce_rate"] is None
    assert m["block_rate"] is None and m["force_rate"] is None
    report = qm.render_report(m, None)
    assert "样本不足" in report


def test_last_week_monday_sunday():
    # 2026-08-25 是周二 → 上周 = 08-17(周一) ~ 08-23(周日)
    start, end = qm.last_week(date(2026, 8, 25))
    assert start == date(2026, 8, 17) and end == date(2026, 8, 23)
    assert start.weekday() == 0 and end.weekday() == 6
