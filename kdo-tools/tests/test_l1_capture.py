"""#508 回归：l1_capture 日期增量目录 + 归档复活 + 判重游标。

运行：python -m pytest kdo-tools/tests/test_l1_capture.py -q
沙盒：模块属性注入临时目录（L1_ROOT/STATE_FILE/ARCHIVE_ROOT/SOURCE_DIRS），不碰真实 D 盘。
"""
import importlib.util
import os
import sys
import time
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "l1_capture", Path(__file__).resolve().parent.parent / "l1_capture.py"
)
lc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(lc)


def _sandbox(tmp_path, monkeypatch):
    """注入沙盒路径 + 单工具假源（2 个会话文件）。返回 (src, l1root, archroot)。"""
    src = tmp_path / "src" / "claude"
    src.mkdir(parents=True)
    (src / "s1.jsonl").write_text('{"a":1}\n', encoding="utf-8")
    (src / "s2.md").write_text("# 会话\n", encoding="utf-8")
    l1root = tmp_path / "L1-full"
    archroot = tmp_path / "L1-full-archive"
    monkeypatch.setattr(lc, "L1_ROOT", l1root)
    monkeypatch.setattr(lc, "STATE_FILE", l1root / ".capture-state.json")
    monkeypatch.setattr(lc, "ARCHIVE_ROOT", archroot)
    monkeypatch.setattr(lc, "SOURCE_DIRS", {"claude": src})
    monkeypatch.setattr(lc, "SIZE_LOG", tmp_path / "l1-size.log")
    monkeypatch.setattr(lc, "GATE_BLOCKED_LOG", tmp_path / "gate-blocked.log")
    return src, l1root, archroot


def _today():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")


def test_first_capture_copies_all_to_date_dir(tmp_path, monkeypatch):
    """首跑：全部源文件进今天日期目录（三层结构热层）。"""
    src, l1root, _ = _sandbox(tmp_path, monkeypatch)
    assert lc.capture(dry_run=False) == 0
    today_dir = l1root / _today() / "claude"
    assert (today_dir / "s1.jsonl").exists()
    assert (today_dir / "s2.md").exists()
    assert (l1root / ".capture-state.json").exists()


def test_second_capture_zero_increment(tmp_path, monkeypatch):
    """连跑：第二跑零新增（日增量铁律——不整份重拷）。"""
    src, l1root, _ = _sandbox(tmp_path, monkeypatch)
    lc.capture(dry_run=False)
    # 第二跑：今天目录文件数不变
    before = list((l1root / _today()).rglob("*"))
    lc.capture(dry_run=False)
    after = list((l1root / _today()).rglob("*"))
    assert len(before) == len(after)


def test_changed_file_lands_in_today_dir(tmp_path, monkeypatch):
    """源文件变化 → 只有它进今天目录（游标判重，其余跳过）。"""
    src, l1root, _ = _sandbox(tmp_path, monkeypatch)
    lc.capture(dry_run=False)
    # 抹掉今天目录模拟"昨天已采"，再改一个文件
    import shutil
    shutil.rmtree(l1root / _today())
    time.sleep(0.02)
    (src / "s1.jsonl").write_text('{"a":2}\n', encoding="utf-8")
    os.utime(src / "s1.jsonl", (time.time() + 1, time.time() + 1))
    lc.capture(dry_run=False)
    today_dir = l1root / _today() / "claude"
    assert (today_dir / "s1.jsonl").exists()       # 变化的进来
    assert not (today_dir / "s2.md").exists()      # 未变化的不重拷
    assert (today_dir / "s1.jsonl").read_text() == '{"a":2}\n'


def test_archive_old_days_zip_and_idempotent(tmp_path, monkeypatch):
    """归档复活实测：旧天目录 → zip + 删原目录；同内容目录重跑 → 删目录不重复 zip（幂等）。"""
    src, l1root, archroot = _sandbox(tmp_path, monkeypatch)
    old_day = l1root / "2020-01-01" / "claude"
    old_day.mkdir(parents=True)
    (old_day / "old.jsonl").write_text('{"old":1}\n', encoding="utf-8")
    assert lc._archive_old_days() == 1
    zip_path = archroot / "2020-01-01.zip"
    assert zip_path.exists()
    assert not (l1root / "2020-01-01").exists()
    import zipfile
    with zipfile.ZipFile(zip_path) as zf:
        assert "2020-01-01/claude/old.jsonl" in zf.namelist()
    # 幂等：重建同名同内容目录再跑——zip 覆盖核验通过 → 删目录不重复 zip（mtime 不变）
    old_day.mkdir(parents=True)
    (old_day / "old.jsonl").write_text('{"old":1}\n', encoding="utf-8")
    mtime_before = zip_path.stat().st_mtime
    assert lc._archive_old_days() == 1
    assert zip_path.stat().st_mtime == mtime_before
    assert not (l1root / "2020-01-01").exists()


def test_archive_refuses_delete_when_zip_not_covering(tmp_path, monkeypatch):
    """#508 事故根治回归：zip 已存在但内容未覆盖目录 → 拒绝删除+报警（不核验不删除）。

    事故原型：存量迁移把新内容放进旧日期目录，旧 zip 不含 → 旧实现直接 rmtree 删 474 文件。
    """
    src, l1root, archroot = _sandbox(tmp_path, monkeypatch)
    archroot.mkdir(parents=True)
    # 预置一个"旧" zip（只含 1 文件）
    import zipfile
    zip_path = archroot / "2020-01-01.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("2020-01-01/claude/old.jsonl", '{"old":1}\n')
    # 目录里多出 zip 未覆盖的新文件
    old_day = l1root / "2020-01-01" / "claude"
    old_day.mkdir(parents=True)
    (old_day / "old.jsonl").write_text('{"old":1}\n', encoding="utf-8")
    (old_day / "new-not-in-zip.jsonl").write_text('{"new":2}\n', encoding="utf-8")
    assert lc._archive_old_days() == 0          # 不归档不删除
    assert (old_day / "new-not-in-zip.jsonl").exists()  # 目录保留
    assert (old_day / "old.jsonl").exists()


def test_archive_refuses_delete_on_size_mismatch(tmp_path, monkeypatch):
    """同名文件但内容不同（大小不一致）→ 拒绝删除。"""
    src, l1root, archroot = _sandbox(tmp_path, monkeypatch)
    archroot.mkdir(parents=True)
    import zipfile
    zip_path = archroot / "2020-01-01.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("2020-01-01/claude/old.jsonl", '{"old":1}\n')
    old_day = l1root / "2020-01-01" / "claude"
    old_day.mkdir(parents=True)
    (old_day / "old.jsonl").write_text('{"old":99999}\n', encoding="utf-8")  # 内容变了
    assert lc._archive_old_days() == 0
    assert (old_day / "old.jsonl").exists()


def test_archive_skips_today_and_nondirs(tmp_path, monkeypatch):
    """今天目录不归档；trace-index.md/.capture-state.json 等散文件不动。"""
    src, l1root, archroot = _sandbox(tmp_path, monkeypatch)
    lc.capture(dry_run=False)
    assert lc._archive_old_days() == 0
    assert (l1root / _today()).exists()
    assert (l1root / "trace-index.md").exists()
    assert (l1root / ".capture-state.json").exists()


def test_bootstrap_state_rebuilds_cursor(tmp_path, monkeypatch):
    """--bootstrap-state：从日期目录重建游标 → 后续 capture 全跳过（迁移后零重拷）。"""
    src, l1root, _ = _sandbox(tmp_path, monkeypatch)
    lc.capture(dry_run=False)
    # 游标丢失模拟
    (l1root / ".capture-state.json").unlink()
    assert lc.bootstrap_state() == 0
    import shutil
    before = list((l1root / _today()).rglob("*"))
    lc.capture(dry_run=False)  # 重跑：游标已重建 → 零新增目录变化
    after = list((l1root / _today()).rglob("*"))
    assert len(before) == len(after)
