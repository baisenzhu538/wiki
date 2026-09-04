"""#637 回归之一：gate-blocked 扫描水位线（根治 500-cap 排序淘汰翻滚）。

背景：gate-blocked.log 611 条记录 > gate_seen_v2 上限 500，sorted(known)[-500:]
按哈希字母序淘汰=随机淘汰——每拍淘汰一批、下拍重现为「新记录」，陈旧事件
30min 一滴重登记（09-04 14:17~17:47 六连滴实证）。修法=append-only 水位线
（gate_seen_pos=已处理记录数），hash 集只兜尾部。

运行：python -m pytest kdo-tools/tests/test_gate_blocked_watermark_637.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)


def _log(tmp_path, monkeypatch, records):
    gb = tmp_path / "gate-blocked.log"
    gb.write_text("".join(r + "\n" for r in records), encoding="utf-8")
    monkeypatch.setattr(probe, "GATE_BLOCKED_LOG", gb)
    return gb


def _rec(i: int) -> str:
    return f"2026-08-{10 + i % 18:02d} 0{i % 10}:00:00｜role-liveness｜role{i} 全实例疑似死亡（stale: x）｜src｜src"


def test_migration_absorbs_existing_stock(tmp_path, monkeypatch):
    """老 state（gate_seen_v2 在）→ 迁移吸水位线：存量一条不报（止滴），pos 压到末尾。"""
    _log(tmp_path, monkeypatch, [_rec(i) for i in range(20)])
    state = {"gate_seen_v2": [probe._sha256(_rec(i)) for i in range(10)]}  # 老方案见过一半
    assert probe._scan_gate_blocked(state) == []  # 吸收，零重报
    assert state["gate_seen_pos"] == 20


def test_post_watermark_only_tail_emitted(tmp_path, monkeypatch):
    """迁移后：新增记录才报，且只报一次（水位线幂等）。"""
    gb = _log(tmp_path, monkeypatch, [_rec(i) for i in range(20)])
    state = {"gate_seen_v2": ["x"]}
    probe._scan_gate_blocked(state)  # 迁移吸收
    with gb.open("a", encoding="utf-8") as f:
        f.write(_rec(99) + "\n")
    new = probe._scan_gate_blocked(state)
    assert new == [_rec(99)]
    assert probe._scan_gate_blocked(state) == []  # 幂等


def test_churn_regression_evicted_records_not_reemitted(tmp_path, monkeypatch):
    """#637 场景回放：记录数超 cap 的旧记录被 hash 集淘汰后，不再被当新记录重报。"""
    _log(tmp_path, monkeypatch, [_rec(i) for i in range(20)])
    state = {"gate_seen_v2": ["only-tail-left"]}  # 模拟老方案淘汰后：旧记录全不在 seen
    assert probe._scan_gate_blocked(state) == []  # 迁移吸水位线——淘汰的旧记录不重报
    # 再拍：依然零重报（水位线不看 hash 集内容）
    assert probe._scan_gate_blocked(state) == []


def test_fresh_state_full_scan(tmp_path, monkeypatch):
    """全新安装（无任何 seen 键）→ 全扫（首跑全貌上报，原语义保留）。"""
    _log(tmp_path, monkeypatch, [_rec(1), _rec(2)])
    state = {}
    assert len(probe._scan_gate_blocked(state)) == 2
    assert probe._scan_gate_blocked(state) == []


def test_log_truncation_resets_watermark(tmp_path, monkeypatch):
    """日志截断（记录数 < 水位）→ 水位重置，hash 集兜重防重报。"""
    gb = _log(tmp_path, monkeypatch, [_rec(i) for i in range(10)])
    state = {}
    probe._scan_gate_blocked(state)  # 全扫，seen 集满
    gb.write_text(_rec(1) + "\n" + _rec(2) + "\n", encoding="utf-8")  # 截断到 2 条
    assert probe._scan_gate_blocked(state) == []  # 重置后重扫，但 hash 集兜住已知记录
