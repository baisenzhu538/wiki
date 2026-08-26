"""#421 传送带探针测试：三元组检出 / PROPOSAL-PENDING 登记幂等 / 历史行保留 / 边界（无流转能力）/ 通知 dry-run。

运行：python -m pytest kdo-tools/tests/test_conveyor_probe.py -q
"""
import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)

TRIPLET = """---
id: diag_test-1
title: 测试建议书
type: proposal
status: pending_orchestration
audience: 王语嫣
---

测试。
"""


def _write_triplet(dir_: Path, name: str) -> Path:
    fp = dir_ / name
    fp.write_text(TRIPLET, encoding="utf-8")
    return fp


def test_scan_proposals_detects_triplet(tmp_path, monkeypatch):
    monkeypatch.setattr(probe, "DIAG_DIR", tmp_path)
    _write_triplet(tmp_path, "diag_20260822_test-a.md")
    (tmp_path / "diag_20260822_not-proposal.md").write_text(
        "---\nid: x\ntitle: y\nstatus: reviewed\n---\n", encoding="utf-8"
    )
    hits = probe._scan_proposals()
    assert hits == ["diag_20260822_test-a.md"]


def test_update_board_idempotent(tmp_path, monkeypatch):
    queue = tmp_path / "production-queue.md"
    queue.write_text(f"# 队列\n\n{probe.PROPOSAL_BEGIN}\n{probe.PROPOSAL_END}\n", encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    first = probe._update_proposal_board(["diag_20260822_test-a.md"])
    second = probe._update_proposal_board(["diag_20260822_test-a.md"])
    assert first == ["diag_20260822_test-a.md"]
    assert second == []  # 幂等：重跑不重复登记
    assert queue.read_text(encoding="utf-8").count("diag_20260822_test-a.md") == 1


def test_update_board_keeps_historical_rows(tmp_path, monkeypatch):
    """同一文件的多条历史裁定记录不得被重写删除（2026-08-22 误删实证）。"""
    queue = tmp_path / "production-queue.md"
    history = (
        f"{probe.PROPOSAL_BEGIN}\n"
        "- ~~60_feedback/diagnosis/diag_x.md｜裁定一｜风清扬 08-22~~ → 已复核\n"
        "- ~~60_feedback/diagnosis/diag_x.md｜裁定二｜风清扬 08-22~~ → 已复核\n"
        f"{probe.PROPOSAL_END}\n"
    )
    queue.write_text(history, encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    probe._update_proposal_board(["diag_x.md"])
    text = queue.read_text(encoding="utf-8")
    assert text.count("裁定一") == 1
    assert text.count("裁定二") == 1  # 历史行保留


def test_no_transition_capability():
    """边界硬编码：探针无领取/裁决/流转能力——不 import queue_transition，无 claim/complete/review 函数。"""
    src = Path(__file__).resolve().parent.parent.joinpath("conveyor_probe.py").read_text(encoding="utf-8")
    assert "import queue_transition" not in src
    assert "from queue_transition" not in src
    for fn in ("claim", "complete", "review", "release"):
        assert f"def {fn}" not in src
    import pytest
    with pytest.raises(AttributeError):
        probe.claim("x")  # 模块无此能力 = 试图领取被拒


def test_notify_dry_run_no_send(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(probe, "HOOKS_FILE", tmp_path / "none.json")  # 无配置 → 显式打印不静默失败
    probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=False, silent=False)
    out = capsys.readouterr().out
    assert "不发送" in out


# ── #421 终审 P1 修复回归（静默/dry-run 不消耗幂等配额 + pending 补发）──

def test_notify_silent_returns_empty():
    """静默 = 不发送且不消耗配额（返回空列表，调用方据此把消息留 pending）。"""
    sent = probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=False, silent=True)
    assert sent == []


def test_notify_dryrun_returns_empty():
    """dry-run = 不发送不消耗配额。"""
    sent = probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=True, silent=False)
    assert sent == []


def test_notify_success_returns_sent_roles(tmp_path, monkeypatch):
    import json as _json
    hooks = tmp_path / "hooks.json"
    hooks.write_text(_json.dumps({"ouyangfeng": {"url": "https://example.com/hook", "key": "k"}}), encoding="utf-8")
    monkeypatch.setattr(probe, "HOOKS_FILE", hooks)
    monkeypatch.setattr(probe, "_send_hook", lambda url, text, key=None: True)
    sent = probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=False, silent=False)
    assert sent == ["ouyangfeng"]


def test_msg_key_stable():
    k1 = probe._msg_key("ouyangfeng", "🔔 KDO 新提审 3 单：#421，请终审")
    k2 = probe._msg_key("ouyangfeng", "🔔 KDO 新提审 3 单：#421，请终审")
    assert k1 == k2
    assert k1.startswith("ouyangfeng:")


# ── #443 可领取通知按 assignee 路由回归 ──

def test_route_huangyaoshi_task():
    rows = [("task_443_x", "443", "huangyaoshi"), ("task_426_y", "426", "laowantong")]
    buckets = probe._route_queued(rows)
    assert "huangyaoshi" in buckets and [t for t, _ in buckets["huangyaoshi"]] == ["task_443_x"]
    assert "laowantong" in buckets and [t for t, _ in buckets["laowantong"]] == ["task_426_y"]


def test_route_instance_aliases():
    """hermes/kimi 实例 → laowantong 通道（E020 实例口径）。"""
    rows = [("task_a", "1", "hermes"), ("task_b", "2", "kimi")]
    buckets = probe._route_queued(rows)
    assert buckets["laowantong"] == [("task_a", "1"), ("task_b", "2")]


def test_route_unknown_falls_back():
    """未知/缺省 assignee → 回落 laowantong，不静默丢。"""
    rows = [("task_x", "9", ""), ("task_y", "10", "some-new-instance")]
    buckets = probe._route_queued(rows)
    assert len(buckets.get("laowantong", [])) == 2


def test_route_split_buckets():
    """同批多 assignee → 拆分投递（一角色一桶）。"""
    rows = [("task_1", "1", "huangyaoshi"), ("task_2", "2", "wangyuyan"), ("task_3", "3", "laowantong")]
    buckets = probe._route_queued(rows)
    assert set(buckets.keys()) == {"huangyaoshi", "wangyuyan", "laowantong"}


# ── #458 第四探针（friction 增量扫描）回归 ──

def test_friction_scan_detects_new_lines(tmp_path, monkeypatch):
    """friction 增量检测：新行被检出，重复行幂等。"""
    f = tmp_path / "friction-log.md"
    f.write_text("# friction\n\n| 时间 | 场景 | 问题 |\n|:--|:--|:--|\n\n2026-08-23 10:00｜门禁误判｜测试问题一｜建议收窄\n", encoding="utf-8")
    monkeypatch.setattr(probe, "RETRO_ROOT", tmp_path.parent)
    monkeypatch.setattr(probe, "FRICTION_ROLES", [tmp_path.name])
    monkeypatch.setattr(probe, "SHARED_FRICTION", tmp_path / "none.md")

    state = {}
    first = probe._scan_friction(state)
    assert len(first) == 1
    assert "测试问题一" in first[0]

    second = probe._scan_friction(state)
    assert second == []  # 幂等：重复扫描零新增

    # 追加新行 → 只检出新的
    f.write_text(f.read_text(encoding="utf-8") + "2026-08-23 11:00｜工具卡顿｜测试问题二\n", encoding="utf-8")
    third = probe._scan_friction(state)
    assert len(third) == 1
    assert "测试问题二" in third[0]


def test_friction_registration_marks_clue(tmp_path, monkeypatch):
    """friction 线索登记 PROPOSAL-PENDING：[friction] 标记 + 幂等。"""
    queue = tmp_path / "production-queue.md"
    queue.write_text(f"# 队列\n\n{probe.PROPOSAL_BEGIN}\n{probe.PROPOSAL_END}\n", encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    probe._update_proposal_board_friction(["[huangyaoshi] 2026-08-23 10:00｜门禁误判｜测试问题"])
    text = queue.read_text(encoding="utf-8")
    assert "[friction] [huangyaoshi] 2026-08-23 10:00" in text
    probe._update_proposal_board_friction(["[huangyaoshi] 2026-08-23 10:00｜门禁误判｜测试问题"])
    assert text.count("[friction]") == 1  # 幂等


# ── #460 第五探针（gate-blocked 机器自报）回归 ──

def test_gate_blocked_scan_and_registration(tmp_path, monkeypatch):
    """门禁拦截日志增量检测 + [gate-blocked] 登记幂等。"""
    gb = tmp_path / "gate-blocked.log"
    gb.write_text("2026-08-23 14:00｜task_426｜F-034-五字段｜缺执行报告｜huangyaoshi\n", encoding="utf-8")
    monkeypatch.setattr(probe, "GATE_BLOCKED_LOG", gb)

    state = {}
    first = probe._scan_gate_blocked(state)
    assert len(first) == 1
    assert "F-034-五字段" in first[0]
    assert probe._scan_gate_blocked(state) == []  # 幂等

    queue = tmp_path / "production-queue.md"
    queue.write_text(f"# 队列\n\n{probe.PROPOSAL_BEGIN}\n{probe.PROPOSAL_END}\n", encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    probe._update_proposal_board_gate(first)
    text = queue.read_text(encoding="utf-8")
    assert "[gate-blocked] task_426" in text
    probe._update_proposal_board_gate(first)
    assert text.count("[gate-blocked]") == 1  # 幂等


# ── #462 流转完成信号回归（new_reviewed→王语嫣 / new_failback→assignee）──

def test_review_done_and_failback_signals(tmp_path, monkeypatch):
    """状态对比：新增 reviewed 检出 + pending→queued 退回检出，幂等。"""
    queue = tmp_path / "production-queue.md"
    SEP = "|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|"
    def write_queue(reviewed_ids, pending_ids, queued_ids):
        rows = []
        for i, t in enumerate(reviewed_ids):
            rows.append(f"| {i+1} | `{t}` | t{i} | reviewed | laowantong | x | 无 | t.md | 测试 |")
        for i, t in enumerate(pending_ids):
            rows.append(f"| {i+10} | `{t}` | t{i} | pending_review | huangyaoshi | x | 无 | t.md | 测试 |")
        for i, t in enumerate(queued_ids):
            rows.append(f"| {i+20} | `{t}` | t{i} | queued | laowantong | x | 无 | t.md | 测试 |")
        queue.write_text("# 队列\n\n| # | 任务 | 名称 | 状态 | 负责人 | 交付物 | 依赖 | 任务单 | 备注 |\n" + SEP + "\n" + "\n".join(rows) + "\n", encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)

    # 第一次扫描：task_a pending_review（快照）
    write_queue(reviewed_ids=[], pending_ids=["task_a"], queued_ids=[])
    state = {}
    sig1 = probe._queue_signal(state)
    assert sig1["new_reviewed"] == []
    assert sig1["new_failback"] == []

    # 第二次扫描：task_a 变 reviewed（终审 PASS）→ new_reviewed 检出
    # #521 R1：reviewed 元组带 assignee（PASS 路由生产者用），解包三位
    write_queue(reviewed_ids=["task_a"], pending_ids=[], queued_ids=[])
    sig2 = probe._queue_signal(state)
    assert [t for t, _, _ in sig2["new_reviewed"]] == ["task_a"]

    # 第三次扫描：task_b pending_review → queued（退回）→ new_failback 检出（带 assignee）
    write_queue(reviewed_ids=["task_a"], pending_ids=[], queued_ids=["task_b"])
    state["last_review_pending"] = ["task_b"]  # 模拟上次快照含 task_b pending
    sig3 = probe._queue_signal(state)
    assert [t for t, _, _ in sig3["new_failback"]] == ["task_b"]

    # 幂等：重扫不重复
    sig4 = probe._queue_signal(state)
    assert sig4["new_reviewed"] == [] and sig4["new_failback"] == []


def test_reject_duplicate_doc_ids_removes_collision(tmp_path, monkeypatch):
    """#450 登记口：同 doc_id 重复的建议书被剔除（撞号拒绝登记）。"""
    import importlib.util
    _spec = importlib.util.spec_from_file_location(
        "file_flow_check", Path(__file__).resolve().parent.parent / "file-flow-check.py")
    ffc = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(ffc)
    monkeypatch.setattr(probe, "DIAG_DIR", tmp_path)
    for name in ("diag_20260823_a-dup.md", "diag_20260823_b-dup.md"):
        (tmp_path / name).write_text(
            "---\ndoc_id: D-20260823-777\nversion: v1.0\ncreated_at: '2026-08-23T10:00:00+08:00'\n"
            "updated_at: '2026-08-23T10:00:00+08:00'\naudience: 王语嫣\nstatus: pending_orchestration\n---\n正文\n",
            encoding="utf-8")
    (tmp_path / "diag_20260823_c-ok.md").write_text(
        "---\ndoc_id: D-20260823-778\nversion: v1.0\ncreated_at: '2026-08-23T10:00:00+08:00'\n"
        "updated_at: '2026-08-23T10:00:00+08:00'\naudience: 王语嫣\nstatus: pending_orchestration\n---\n正文\n",
        encoding="utf-8")
    kept = probe._reject_duplicate_doc_ids(
        ["diag_20260823_a-dup.md", "diag_20260823_b-dup.md", "diag_20260823_c-ok.md"])
    assert kept == ["diag_20260823_c-ok.md"]  # 撞号全拒，唯一 doc_id 放行


def test_reject_duplicate_doc_ids_unique_passthrough(tmp_path, monkeypatch):
    """#450 登记口：doc_id 唯一时原样返回。"""
    import importlib.util
    _spec = importlib.util.spec_from_file_location(
        "file_flow_check", Path(__file__).resolve().parent.parent / "file-flow-check.py")
    ffc = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(ffc)
    monkeypatch.setattr(probe, "DIAG_DIR", tmp_path)
    (tmp_path / "diag_20260823_a-ok.md").write_text(
        "---\ndoc_id: D-20260823-778\nversion: v1.0\ncreated_at: '2026-08-23T10:00:00+08:00'\n"
        "updated_at: '2026-08-23T10:00:00+08:00'\naudience: 王语嫣\nstatus: pending_orchestration\n---\n正文\n",
        encoding="utf-8")
    hits = ["diag_20260823_a-ok.md"]
    assert probe._reject_duplicate_doc_ids(hits) == hits


def test_append_role_todo_all_roles(tmp_path, monkeypatch):
    """#501 角色待办收件箱：任意角色落盘 todos/<role>.md。"""
    monkeypatch.setattr(probe, "TODOS_DIR", tmp_path)
    probe._append_role_todo("wangyuyan", "⚖️ 测试终审")
    probe._append_role_todo("ouyangfeng", "✍️ F-036 测试")
    assert (tmp_path / "wangyuyan.md").exists()
    assert (tmp_path / "ouyangfeng.md").exists()
    assert "测试终审" in (tmp_path / "wangyuyan.md").read_text(encoding="utf-8")


def test_append_role_todo_appends_not_overwrites(tmp_path, monkeypatch):
    """#501 追加式留痕（防覆盖）。"""
    monkeypatch.setattr(probe, "TODOS_DIR", tmp_path)
    probe._append_role_todo("wangyuyan", "第一条")
    probe._append_role_todo("wangyuyan", "第二条")
    content = (tmp_path / "wangyuyan.md").read_text(encoding="utf-8")
    assert "第一条" in content and "第二条" in content


# ── #506 建议书 near-miss 报警回归：三元组漂移当场可见（不静默 continue）──

def _nm_setup(tmp_path, monkeypatch, files: dict[str, str]):
    """注入 DIAG_DIR + 临时 gate-blocked log，返回 (state, log_path)。"""
    monkeypatch.setattr(probe, "DIAG_DIR", tmp_path)
    log = tmp_path / "gate-blocked.log"
    monkeypatch.setattr(probe, "GATE_BLOCKED_LOG", log)
    for name, content in files.items():
        (tmp_path / name).write_text(content, encoding="utf-8")
    return {}, log


def _fm(type_="proposal", status="pending", audience=None, to=None, created="2026-08-25"):
    lines = ["---", "id: x", "title: y", f"type: {type_}"]
    if status is not None:
        lines.append(f"status: {status}")
    if audience:
        lines.append(f"audience: {audience}")
    if to:
        lines.append(f"to: {to}")
    if created:
        lines.append(f"created_at: {created}")
    lines += ["---", "", "正文。", ""]
    return "\n".join(lines)


def test_near_miss_deprecated_to_field_alarmed(tmp_path, monkeypatch):
    """08-24 漂移同型：to:+status: pending+type: diagnosis → 报警+落 gate-blocked 记录。"""
    state, log = _nm_setup(tmp_path, monkeypatch, {
        "diag_20260825_drift-a.md": _fm(type_="diagnosis", status="pending", to="王语嫣"),
    })
    misses = probe._scan_proposal_near_miss(state)
    assert len(misses) == 1 and "to:" in misses[0]
    assert "near-miss-三元组" in log.read_text(encoding="utf-8")


def test_near_miss_status_pending_alarmed(tmp_path, monkeypatch):
    """audience 对但 status=pending（非 pending_orchestration）→ 报警。"""
    state, log = _nm_setup(tmp_path, monkeypatch, {
        "diag_20260825_drift-b.md": _fm(status="pending", audience="王语嫣"),
    })
    misses = probe._scan_proposal_near_miss(state)
    assert len(misses) == 1 and "pending_orchestration" in misses[0]


def test_near_miss_proposal_missing_audience_alarmed(tmp_path, monkeypatch):
    """type: proposal 缺 audience → 报警。"""
    state, _ = _nm_setup(tmp_path, monkeypatch, {
        "diag_20260825_drift-c.md": _fm(status="pending_orchestration", audience=None),
    })
    misses = probe._scan_proposal_near_miss(state)
    assert len(misses) == 1 and "缺 audience" in misses[0]


def test_normal_triplet_no_false_alarm(tmp_path, monkeypatch):
    """正常三元组 → 零报警（不误伤登记件）。"""
    state, log = _nm_setup(tmp_path, monkeypatch, {
        "diag_20260825_ok.md": TRIPLET,
    })
    misses = probe._scan_proposal_near_miss(state)
    assert misses == []
    assert not log.exists() or "near-miss" not in log.read_text(encoding="utf-8")


def test_plain_diagnosis_report_no_alarm(tmp_path, monkeypatch):
    """纯诊断报告（type: diagnosis，无 audience/to/status）→ 不报警（非建议书形态）。"""
    state, _ = _nm_setup(tmp_path, monkeypatch, {
        "diag_20260825_report.md": _fm(type_="diagnosis", status=None),
    })
    assert probe._scan_proposal_near_miss(state) == []


def test_terminal_status_no_alarm(tmp_path, monkeypatch):
    """终态件（status: resolved）→ 不报警。"""
    state, _ = _nm_setup(tmp_path, monkeypatch, {
        "diag_20260825_done.md": _fm(status="resolved", audience="王语嫣"),
    })
    assert probe._scan_proposal_near_miss(state) == []


def test_historical_files_grandfathered(tmp_path, monkeypatch):
    """向前生效：生效日前的漂移件既往不咎（53 条历史噪声洪泛根治）。"""
    state, _ = _nm_setup(tmp_path, monkeypatch, {
        "diag_20260824_old-drift.md": _fm(type_="diagnosis", status="pending", to="王语嫣",
                                          created="2026-08-24"),
    })
    assert probe._scan_proposal_near_miss(state) == []
    # 注入回放模式（effective_date 前移）→ 同件必须检出（L2 狗粮路径）
    misses = probe._scan_proposal_near_miss(state, effective_date="20260101")
    assert len(misses) == 1


def test_near_miss_idempotent_log(tmp_path, monkeypatch):
    """幂等：同一漂移件重跑不重复落 gate-blocked 记录（state 去重）。"""
    state, log = _nm_setup(tmp_path, monkeypatch, {
        "diag_20260825_drift-d.md": _fm(status="pending", audience="王语嫣"),
    })
    probe._scan_proposal_near_miss(state)
    probe._scan_proposal_near_miss(state)
    assert log.read_text(encoding="utf-8").count("drift-d") == 1


def test_undated_file_falls_back_to_created_at(tmp_path, monkeypatch):
    """无日期文件名：回落 created_at 判新旧（proposal-self-learning-cron 实证）。"""
    state, _ = _nm_setup(tmp_path, monkeypatch, {
        "proposal-old-design.md": _fm(status="pending_review", audience=None,
                                      created="2026-06-11"),
    })
    assert probe._scan_proposal_near_miss(state) == []


# ── #521 R1 回归：PASS 路由生产者（new_reviewed 带 assignee）──

def test_reviewed_carries_assignee_and_routes(tmp_path, monkeypatch):
    """new_reviewed 元组携带 assignee；按 #443 ASSIGNEE_ROLE 路由到生产者双角色。"""
    queue = tmp_path / "production-queue.md"
    SEP = "|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|"
    rows = [
        "| 1 | `task_p_h` | t1 | reviewed | huangyaoshi | x | 无 | t.md | 测试 |",
        "| 2 | `task_p_l` | t2 | reviewed | laowantong | x | 无 | t.md | 测试 |",
    ]
    queue.write_text("# 队列\n\n| # | 任务 | 名称 | 状态 | 负责人 | 交付物 | 依赖 | 任务单 | 备注 |\n"
                     + SEP + "\n" + "\n".join(rows) + "\n", encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)

    sig = probe._queue_signal({})
    assert [(t, a) for t, _s, a in sig["new_reviewed"]] == [
        ("task_p_h", "huangyaoshi"), ("task_p_l", "laowantong")]
    buckets = probe._route_queued(sig["new_reviewed"])
    assert [t for t, _ in buckets["huangyaoshi"]] == ["task_p_h"]
    assert [t for t, _ in buckets["laowantong"]] == ["task_p_l"]

    # 幂等：重扫不重复检出
    state2 = {}
    probe._queue_signal(state2)
    assert probe._queue_signal(state2)["new_reviewed"] == []


def test_override_failback_signal(tmp_path, monkeypatch):
    """#538：曾 reviewed 的单回到 queued → new_failback 检出（改判退回信号口径）。

    原型：#537 首日改判——任务终审 PASS 后改判 FAIL 回 queued，failback 原口径
    （pending 快照对比）捕不到，须靠 last_reviewed 交集。
    """
    queue = tmp_path / "production-queue.md"
    SEP = "|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|"

    def write(rows):
        queue.write_text("# 队列\n\n| # | 任务 | 名称 | 状态 | 负责人 | 交付物 | 依赖 | 任务单 | 备注 |\n"
                         + SEP + "\n" + "\n".join(rows) + "\n", encoding="utf-8")

    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    # 第一拍：task_x reviewed（快照 last_reviewed）
    write(["| 1 | `task_x` | t | reviewed | huangyaoshi | x | 无 | t.md | n |"])
    state = {}
    probe._queue_signal(state)
    assert "task_x" in state["last_reviewed"]
    # 第二拍：改判 → task_x 回 queued → failback 检出（带 assignee）
    write(["| 1 | `task_x` | t | queued | huangyaoshi | x | 无 | t.md | n |"])
    sig = probe._queue_signal(state)
    assert [t for t, _, _ in sig["new_failback"]] == ["task_x"]
    # 幂等：再扫不重复
    assert probe._queue_signal(state)["new_failback"] == []
