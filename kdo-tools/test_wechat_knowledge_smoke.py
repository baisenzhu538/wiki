#!/usr/bin/env python3
"""wechat 采集管线 smoke 测试最小护栏（#585，源自 #584 终审扣分点 2）。

只测管线判定逻辑，不测 LLM 输出质量；全部 LLM 调用 mock/桩化，零网络零 key。
样例全部落临时目录，不碰真库（00_inbox/wechat-collect/ 一字不动）。

用法:
  python kdo-tools/test_wechat_knowledge_smoke.py   # exit 0=全绿, 1=有红
  pytest kdo-tools/test_wechat_knowledge_smoke.py   # pytest 单文件亦可收集

红绿自证（测试自身的有效性核验，见 #585 验证节）：
  python -c "import wechat_knowledge as wk; wk.SKELETON_MARKERS=('<!--',); \\
             import test_wechat_knowledge_smoke as t; raise SystemExit(t.main())"
  → 必须把 SKELETON_MARKERS 精确匹配用例跑红（证明断言对泛匹配回归敏感）。
"""
import sys
import tempfile
from pathlib import Path
from unittest import mock

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))

import wechat_knowledge as wk
import wechat_promote as wp

# ---------------------------------------------------------------- 样例

TRANSCRIPT = """# 示例视频逐字稿

[00:01] 今天讲一个真实的商业案例。
[00:12] 这家工厂用三个月把交付周期砍掉一半。
"""

# 完整卡：含五段模板自带的 '<!-- 见上方 LLM 总结 -->' 注释——
# 旧版 '<!--' 泛匹配会把这种好卡误判成骨架（08-31 实测 15 次无效 LLM 调用），
# SKELETON_MARKERS 精确匹配必须判它「非骨架」。
GOOD_CARD = """---
title: "示例案例"
type: case
status: draft
domain: pending-domain
aliases: []
discoverable_by: []
source_context:
- 来源轴: wechat-video（wechat-collect 偶遇采集管线）
source_refs:
- 00_inbox/wechat-collect/src_wechat_demo01.md
created_at: 2026-09-01
updated_at: 2026-09-01
---

# 示例案例

## 事实（客观信息）

- 事实一：工厂交付周期三个月砍半。
- 事实二：案例来自真实视频逐字稿。
- 事实三：数据点均在原文出现，无推断。
- 事实四：这是一条用于撑过正文长度校验的事实。
- 事实五：正文需要超过两百字符才算非空壳，因此再补充一句完整的描述。

## 规律（可复用模式）

<!-- 见上方 LLM 总结 -->

## 洞察（底层认知）

<!-- 见上方 LLM 总结 -->
"""

SKELETON_FAIL_CARD = GOOD_CARD.replace(
    "- 事实一：工厂交付周期三个月砍半。",
    "<!-- LLM 总结失败，请重试 -->",
)
SKELETON_NOKEY_CARD = GOOD_CARD.replace(
    "- 事实一：工厂交付周期三个月砍半。",
    "<!-- TODO: 配置 DEEPSEEK_API_KEY 后运行 wechat_knowledge.py 生成三层次总结 -->",
)

FAKE_LLM_SUMMARY = "- 事实：示例总结内容。\n- 规律：示例规律。\n- 洞察：示例洞察。"


def _is_skeleton(content: str) -> bool:
    """与 wechat_knowledge.knowledge_ize 判定同源：SKELETON_MARKERS 精确匹配。"""
    return any(m in content for m in wk.SKELETON_MARKERS)


def _write(tmp: Path, name: str, content: str) -> Path:
    p = tmp / name
    p.write_text(content, encoding="utf-8")
    return p


# ---------------------------------------------------------------- 断言

def test_skeleton_marker_exact_match():
    """骨架标记精确匹配：模板自带注释不误判，两类失败占位必命中。"""
    assert not _is_skeleton(GOOD_CARD), "完整卡被误判为骨架（<!-- 泛匹配回归？）"
    assert _is_skeleton(SKELETON_FAIL_CARD), "LLM 失败占位未命中骨架标记"
    assert _is_skeleton(SKELETON_NOKEY_CARD), "无 key TODO 占位未命中骨架标记"
    assert not _is_skeleton(""), "空内容被误判为骨架"


def test_skip_complete_card_no_llm_call():
    """skip 判定前置（#584 根治回归）：完整卡直接跳过，LLM 零调用。"""
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        transcript = _write(tmp, "src_wechat_demo01.md", TRANSCRIPT)
        out = _write(tmp, "case-wechat-demo01.md", GOOD_CARD)
        before = out.read_text(encoding="utf-8")
        with mock.patch.object(wk, "llm_summarize") as m_llm:
            assert wk.knowledge_ize(transcript, out) is True
        assert m_llm.call_count == 0, f"完整卡仍调了 LLM {m_llm.call_count} 次（skip 未前置）"
        assert out.read_text(encoding="utf-8") == before, "skip 路径改动了已有文件"


def test_skeleton_card_triggers_rerun():
    """骨架卡触发重跑：LLM 被调用一次，成功后占位标记被真内容替换。"""
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        transcript = _write(tmp, "src_wechat_demo02.md", TRANSCRIPT)
        out = _write(tmp, "case-wechat-demo02.md", SKELETON_FAIL_CARD)
        with mock.patch.object(wk, "get_api_key", return_value="fake-key"), \
             mock.patch.object(wk, "llm_summarize", return_value=FAKE_LLM_SUMMARY) as m_llm:
            assert wk.knowledge_ize(transcript, out) is True
        assert m_llm.call_count == 1, f"骨架卡重跑 LLM 调用数={m_llm.call_count}（应为 1）"
        new_content = out.read_text(encoding="utf-8")
        assert not _is_skeleton(new_content), "重跑成功后骨架标记仍残留"
        assert "示例总结内容" in new_content, "LLM 真总结未写入产出"


def test_llm_failure_preserves_old_file():
    """LLM 失败且已有旧文件 → 保留旧文件不覆盖（防好卡被降级成骨架）。"""
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        transcript = _write(tmp, "src_wechat_demo03.md", TRANSCRIPT)
        out = _write(tmp, "case-wechat-demo03.md", SKELETON_FAIL_CARD)
        before = out.read_text(encoding="utf-8")
        with mock.patch.object(wk, "get_api_key", return_value="fake-key"), \
             mock.patch.object(wk, "llm_summarize", return_value=""):
            assert wk.knowledge_ize(transcript, out) is True
        assert out.read_text(encoding="utf-8") == before, "LLM 失败时旧文件被覆盖"


def test_no_api_key_generates_skeleton():
    """无 API key → 产出 TODO 骨架卡（下次重跑可被标记识别）。"""
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        transcript = _write(tmp, "src_wechat_demo04.md", TRANSCRIPT)
        out = tmp / "case-wechat-demo04.md"
        with mock.patch.object(wk, "get_api_key", return_value=""), \
             mock.patch.object(wk, "llm_summarize") as m_llm:
            assert wk.knowledge_ize(transcript, out) is True
        assert m_llm.call_count == 0, "无 key 时仍调了 LLM"
        assert _is_skeleton(out.read_text(encoding="utf-8")), "无 key 骨架卡缺 TODO 占位标记"


def test_promote_gate_intercepts_fail_placeholder():
    """#380 内容校验联动：失败占位卡被拦，完整卡放行。"""
    bad = wp._content_issues(SKELETON_FAIL_CARD)
    assert bad, "失败占位卡未被 #380 校验拦截"
    assert any("总结失败" in i for i in bad), f"拦截原因未点名失败占位: {bad}"
    good = wp._content_issues(GOOD_CARD)
    assert not good, f"完整卡被 #380 误拦: {good}"


# ----------------------------------------------------------------  runner

ALL_TESTS = [
    test_skeleton_marker_exact_match,
    test_skip_complete_card_no_llm_call,
    test_skeleton_card_triggers_rerun,
    test_llm_failure_preserves_old_file,
    test_no_api_key_generates_skeleton,
    test_promote_gate_intercepts_fail_placeholder,
]


def main() -> int:
    failed = 0
    for fn in ALL_TESTS:
        try:
            fn()
            print(f"  ✅ {fn.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  ❌ {fn.__name__}: {e}")
        except Exception as e:  # noqa: BLE001 - smoke 要报所有意外
            failed += 1
            print(f"  💥 {fn.__name__}: {type(e).__name__}: {e}")
    print(f"\nsmoke 结果: {len(ALL_TESTS) - failed}/{len(ALL_TESTS)} 通过"
          + ("——全绿" if not failed else f"——{failed} 项红"))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
