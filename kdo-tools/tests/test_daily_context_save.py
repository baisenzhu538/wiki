"""#512 回归：daily-context-save 重打覆盖写 + 事件去重 + 存量清理剥层。

运行：python -m pytest kdo-tools/tests/test_daily_context_save.py -q
隔离：REVIEW_DIR/ARCHIVE_DIR/mc.A_DB 全部注入临时目录，不碰真实复盘库与事件库。
"""
import sqlite3
import sys
import tempfile
import types
from pathlib import Path

KDO_TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KDO_TOOLS))

import importlib.util
_SPEC = importlib.util.spec_from_file_location("daily_context_save", KDO_TOOLS / "daily-context-save.py")
dcs = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(dcs)
import memory_capsule as mc


def _args(**kw):
    base = dict(agent="huangyaoshi", instance="", file="", stdin=False, text="", truman=True)
    base.update(kw)
    return types.SimpleNamespace(**base)


def _sandbox(tmp_path, monkeypatch):
    monkeypatch.setattr(dcs, "REVIEW_DIR", tmp_path / "retro")
    monkeypatch.setattr(dcs, "ARCHIVE_DIR", tmp_path / "archive")
    monkeypatch.setattr(dcs, "WIKI", tmp_path)  # relative_to(WIKI) 打印路径用
    monkeypatch.setattr(dcs, "_run_review_check", lambda agent: "🟢 A")
    monkeypatch.setattr(mc, "A_DIR", tmp_path / "capsule")
    monkeypatch.setattr(mc, "A_DB", tmp_path / "capsule" / "activity_log.db")
    mc.cmd_init()
    return tmp_path / "retro" / "huangyaoshi" / "daily-context"


def _layers(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    n, in_fm = 0, False
    for ln in text.splitlines():
        if ln.strip() == "---":
            if not in_fm:
                n += 1
                in_fm = True
            else:
                in_fm = False
    return n


def test_resave_is_overwrite_single_layer(tmp_path, monkeypatch):
    """重打场景：打回后 --file 重打 → 文件仍只有一层 frontmatter（覆盖不追加）。"""
    dc_dir = _sandbox(tmp_path, monkeypatch)
    assert dcs.cmd_save(_args(text="## 差异栏\n\n初版内容。")) == 0
    fp = next(dc_dir.glob("*.md"))
    assert _layers(fp) == 1
    # 打回重打：读既有文件（含 frontmatter+标题）作为输入再 save
    assert dcs.cmd_save(_args(file=str(fp))) == 0
    assert _layers(fp) == 1, "重打后仍多层堆叠"
    text = fp.read_text(encoding="utf-8")
    assert text.count("# huangyaoshi ·") == 1  # 标题唯一
    assert "初版内容" in text  # 正文保留


def test_strip_multi_layer_keeps_body_and_truman_heading():
    """三层堆叠输入 → 剥到只剩正文；Truman 内容标题不误伤。"""
    body = (
        "---\nsession_id: x\n---\n\n# huangyaoshi · 2026-08-24\n\n"
        "---\nsession_id: y\n---\n\n# huangyaoshi · 2026-08-24\n\n"
        "# Truman 11章复盘 · 黄药师 · 2026-08-24（标题带后缀）\n\n## 差异栏\n\n真内容。\n"
    )
    out = dcs._strip_existing_layers(body)
    assert not out.startswith("---")
    assert out.startswith("# Truman 11章复盘")  # 内容标题保留
    assert "真内容" in out
    assert "session_id" not in out


def test_event_dedup_same_content(tmp_path, monkeypatch):
    """同内容重打不刷屏：两次 save 同内容 → 事件库只有 1 条 review_saved。"""
    dc_dir = _sandbox(tmp_path, monkeypatch)
    dcs.cmd_save(_args(text="## 差异栏\n\n同内容。"))
    dcs.cmd_save(_args(text="## 差异栏\n\n同内容。"))
    con = sqlite3.connect(str(mc.A_DB))
    n = con.execute(
        "SELECT COUNT(*) FROM activity_log WHERE event_type='review_saved'").fetchone()[0]
    con.close()
    assert n == 1


def test_event_not_dedup_when_content_changes(tmp_path, monkeypatch):
    """内容真实变化的重打 → 新事件正常留痕（改进版也是审计线索）。"""
    dc_dir = _sandbox(tmp_path, monkeypatch)
    dcs.cmd_save(_args(text="## 差异栏\n\n版本一。"))
    fp = next(dc_dir.glob("*.md"))
    # 修改内容后重打（模拟打回补章）
    (tmp_path / "v2.md").write_text(
        fp.read_text(encoding="utf-8") + "\n## 补充章节\n\n新增。\n", encoding="utf-8")
    dcs.cmd_save(_args(file=str(tmp_path / "v2.md")))
    con = sqlite3.connect(str(mc.A_DB))
    n = con.execute(
        "SELECT COUNT(*) FROM activity_log WHERE event_type='review_saved'").fetchone()[0]
    con.close()
    assert n == 2
