"""#601 回归：wechat_link_monitor canonical_key URL 变体归一。

背景（风清扬 P0-B-3）：seen_links.txt 里同一链接的 `&`/`&amp;`/exportkey/chksm
等变体各占一行，查重口径不一 → 同内容重复采集。canonical_key 必须把变体归一到同一键。

运行：python -m pytest kdo-tools/tests/test_wechat_link_monitor.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "wechat_link_monitor", Path(__file__).resolve().parent.parent / "wechat_link_monitor.py"
)
wlm = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(wlm)

ck = wlm.canonical_key


def test_mp_amp_variant_same_key():
    """公众号：`&` 与 `&amp;` 变体归一到同一键。"""
    a = ck("https://mp.weixin.qq.com/s?__biz=MzAx&mid=2650545393&idx=1&sn=abc")
    b = ck("https://mp.weixin.qq.com/s?__biz=MzAx&amp;mid=2650545393&amp;idx=1&amp;sn=abc")
    assert a == b == "mp:MzAx:2650545393:1"


def test_mp_tracking_params_ignored():
    """公众号：chksm/scene/exportkey/pass_ticket 等追踪参数不影响身份。"""
    base = "https://mp.weixin.qq.com/s?__biz=MzAx&mid=2650545393&idx=1"
    v1 = ck(base + "&chksm=1111&scene=21")
    v2 = ck(base + "&exportkey=xxxx&pass_ticket=yyy")
    assert v1 == v2 == "mp:MzAx:2650545393:1"


def test_toutiao_gid_same_key():
    """头条：同 gid 的 video/group/article/追踪参数变体归一。"""
    a = ck("https://m.toutiao.com/video/7670120133340102707/?app=news_article&amp;category_new=xx")
    b = ck("https://m.toutiao.com/video/7670120133340102707/")
    assert a == b == "tt:7670120133340102707"


def test_seen_line_normalization_injection():
    """seen 读入归一化逻辑：历史 `&amp;` 变体行注入规范化键后能命中新 `&` 链接。"""
    legacy_line = "https://mp.weixin.qq.com/s?__biz=MzAx&amp;mid=2650545393&amp;idx=1&amp;sn=abc"
    new_url = "https://mp.weixin.qq.com/s?__biz=MzAx&mid=2650545393&idx=1&sn=abc"
    # 模拟 main() 的读入逻辑：每行注入 canonical_key
    seen = {legacy_line, ck(legacy_line)}
    assert ck(new_url) in seen  # 新链接的规范化键命中历史变体行


# ── #649 回归：转写动态 timeout + 失败留痕 + 3 败熔断 ──

def _seed_fails(tmp_path, key, n):
    wlm.TRANSCRIBE_FAIL_FILE = tmp_path / "transcribe_fails.txt"
    wlm.TRANSCRIBE_FAIL_FILE.write_text(
        "".join(f"{key}|1757000000|timeout 900s killed\n" for _ in range(n)), encoding="utf-8")


def test_transcribe_timeout_scales_with_duration(tmp_path, monkeypatch):
    """65min 视频（148MB 实证件）timeout 必须 >900s——固定 15min 必杀→死循环根因。"""
    video = tmp_path / "v.mp4"
    video.write_bytes(b"x")
    monkeypatch.setattr(wlm, "media_duration_seconds", lambda p: 3905.0)
    assert wlm.transcribe_timeout(video) == 3905 + 300
    monkeypatch.setattr(wlm, "media_duration_seconds", lambda p: 60.0)
    assert wlm.transcribe_timeout(video) == 900  # 短视频落下限
    monkeypatch.setattr(wlm, "media_duration_seconds", lambda p: 20000.0)
    assert wlm.transcribe_timeout(video) == 14400  # 上限 4h 防失控占拍


def test_transcribe_timeout_size_fallback_without_ffprobe(tmp_path, monkeypatch):
    """ffprobe 缺席/失败 → 按体量兜底（60s/MB），仍走 900s 下限。"""
    video = tmp_path / "v.mp4"
    video.write_bytes(b"x" * (2 * 1024 * 1024))  # 2MB → 120s → 落下限 900
    monkeypatch.setattr(wlm, "media_duration_seconds", lambda p: 0.0)
    assert wlm.transcribe_timeout(video) == 900


def test_run_transcribe_timeout_leaves_trace(tmp_path, monkeypatch):
    """超时不再静默：留痕 ledger（key+timeout 原因），返回 False。"""
    import subprocess as sp
    video, out_md = tmp_path / "v.mp4", tmp_path / "out.md"
    video.write_bytes(b"x")
    _seed_fails(tmp_path, "https://x", 0)
    calls = {}

    def boom(*a, **k):
        calls["hit"] = True
        raise sp.TimeoutExpired(cmd=a[0], timeout=k.get("timeout", 900))

    monkeypatch.setattr(wlm.subprocess, "run", boom)
    assert wlm.run_transcribe(video, out_md, "https://x") is False
    assert calls.get("hit")
    assert "timeout" in wlm.TRANSCRIBE_FAIL_FILE.read_text(encoding="utf-8")


def test_run_transcribe_failure_leaves_trace(tmp_path, monkeypatch):
    """转写失败（非超时）也留痕——原实现只 print 不落盘。"""
    import types
    video, out_md = tmp_path / "v.mp4", tmp_path / "out.md"
    video.write_bytes(b"x")
    _seed_fails(tmp_path, "file:v.mp4", 0)
    monkeypatch.setattr(wlm.subprocess, "run",
                        lambda *a, **k: types.SimpleNamespace(returncode=1, stderr=b"model missing"))
    assert wlm.run_transcribe(video, out_md, "file:v.mp4") is False
    assert "model missing" in wlm.TRANSCRIBE_FAIL_FILE.read_text(encoding="utf-8")


def test_run_transcribe_circuit_breaker_after_three_fails(tmp_path, monkeypatch):
    """同素材累计 3 败熔断：不再起 subprocess（防每拍重烧 148MB）。"""
    video, out_md = tmp_path / "v.mp4", tmp_path / "out.md"
    video.write_bytes(b"x")
    _seed_fails(tmp_path, "file:v.mp4", 3)
    monkeypatch.setattr(wlm.subprocess, "run",
                        lambda *a, **k: (_ for _ in ()).throw(AssertionError("不应起子进程")))
    assert wlm.run_transcribe(video, out_md, "file:v.mp4") is False


def test_run_transcribe_success(tmp_path, monkeypatch):
    import types
    video, out_md = tmp_path / "v.mp4", tmp_path / "out.md"
    video.write_bytes(b"x")
    out_md.write_text("# 逐字稿\n", encoding="utf-8")
    _seed_fails(tmp_path, "file:v.mp4", 0)
    monkeypatch.setattr(wlm.subprocess, "run",
                        lambda *a, **k: types.SimpleNamespace(returncode=0, stderr=b""))
    assert wlm.run_transcribe(video, out_md, "file:v.mp4") is True
