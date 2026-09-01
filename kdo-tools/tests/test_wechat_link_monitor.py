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
