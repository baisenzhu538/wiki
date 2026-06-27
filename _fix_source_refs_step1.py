"""Step 1: fix 20 typos + 15 source_unknown -> src_unknown."""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")

# 20 typo fixes: exact source_ref -> replacement
TYPO_FIXES = {
    # card path -> [(old, new)]
    "30_wiki/concepts/concept-纪浩-ai-collaboration-five-layer.md": [
        ("10_raw/sources/src_20260619_e18427b7_00_inbox_纪浩_AI协作方法论_口述.md - 00_inbox/纪浩-AI协作方法论-口述.md",
         "00_inbox/纪浩-AI协作方法论-口述.md"),
    ],
    "30_wiki/concepts/yt-demand-b2b-vs-b2c.md": [
        ("xujian-tob-fivestep-oral.md", "10_raw/sources/xujian-tob-fivestep-oral.md"),
    ],
    "30_wiki/frameworks/framework-科学决策三角形.md": [
        ("00_inbox/_vlm_reprocess/_batch_科学决策/一堂-科学决策-决策三角形.png",
         "00_inbox/_vlm_reprocess/_done_科学决策/一堂-科学决策-决策三角形.png"),
    ],
    "30_wiki/frameworks/yt-demand-decision-chain.md": [
        ("xujian-tob-fivestep-oral.md", "10_raw/sources/xujian-tob-fivestep-oral.md"),
    ],
    "30_wiki/tools/tool-ROI决策评估画布.md": [
        ("00_inbox/_vlm_reprocess/_batch_科学决策/一堂-科学决策-ROI决策评估画布.png",
         "00_inbox/_vlm_reprocess/_done_科学决策/一堂-科学决策-ROI决策评估画布.png"),
    ],
    "30_wiki/tools/tool-一堂-five-step-validation.md": [
        ("10_raw/sources/src_20260619_6e7c14ee_00_inbox_一堂_产品内核验证课_truman_笔记.txt - 00_inbox/一堂-产品内核验证课-Truman-口述.txt - 00_inbox/一堂-产品内核验证课-truman-笔记.txt",
         "00_inbox/一堂-产品内核验证课-truman-笔记.txt"),
    ],
    "30_wiki/tools/tool-一堂-hypothesis-validation-three-axe.md": [
        ("10_raw/sources/src_20260619_ecbf72a3_00_inbox_一堂_关键假设课_truman_笔记.txt - 00_inbox/一堂-关键假设课-truman-口述.txt - 00_inbox/一堂-关键假设课-truman-笔记.txt",
         "00_inbox/一堂-关键假设课-truman-笔记.txt"),
    ],
    "30_wiki/tools/tool-一堂-kernel-three-questions.md": [
        ("10_raw/sources/src_20260619_6e7c14ee_00_inbox_一堂_产品内核验证课_truman_笔记.txt - 00_inbox/一堂-产品内核验证课-Truman-口述.txt - 00_inbox/一堂-产品内核验证课-truman-笔记.txt",
         "00_inbox/一堂-产品内核验证课-truman-笔记.txt"),
    ],
    "30_wiki/tools/tool-一堂-product-kernel-add-subtract.md": [
        ("10_raw/sources/src_20260619_20974e4a_00_inbox_一堂_产品内核实操课_truman_笔记.txt - 00_inbox/一堂-产品内核实操课-Truman-口述.txt - 00_inbox/一堂-产品内核实操课-truman-笔记.txt",
         "00_inbox/一堂-产品内核实操课-truman-笔记.txt"),
    ],
    "30_wiki/tools/tool-一堂-product-kernel-canvas.md": [
        ("10_raw/sources/src_20260619_20974e4a_00_inbox_一堂_产品内核实操课_truman_笔记.txt - 00_inbox/一堂-产品内核迭代课-Truman-笔记.txt - 00_inbox/一堂-产品内核验证课-truman-笔记.txt - 00_inbox/一堂-产品内核实操课-truman-笔记.txt",
         "00_inbox/一堂-产品内核实操课-truman-笔记.txt"),
    ],
    "30_wiki/tools/tool-半肥猫-ai-research-validation.md": [
        ("10_raw/sources/src_20260619_6b081aec_00_inbox_AI俱乐部_AI学习落地_半肥猫_口述.txt - 00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt",
         "00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt"),
    ],
    "30_wiki/tools/tool-半肥猫-course-to-skill-workflow.md": [
        ("10_raw/sources/src_20260619_6b081aec_00_inbox_AI俱乐部_AI学习落地_半肥猫_口述.txt - 00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt",
         "00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt"),
    ],
    "30_wiki/tools/tool-半肥猫-课程Skill化的八步工作流.md": [
        ("10_raw/sources/src_20260619_08606b41_00_inbox_半肥猫_AI学习落地_口述.md - 00_inbox/半肥猫-AI学习落地-口述.md",
         "00_inbox/半肥猫-AI学习落地-口述.md"),
    ],
    "30_wiki/tools/tool-半肥猫-边学边练边沉淀的AI学习法.md": [
        ("10_raw/sources/src_20260619_08606b41_00_inbox_半肥猫_AI学习落地_口述.md - 00_inbox/半肥猫-AI学习落地-口述.md",
         "00_inbox/半肥猫-AI学习落地-口述.md"),
    ],
    "30_wiki/tools/tool-纪浩-Agent技能市场设计法.md": [
        ("10_raw/sources/src_20260619_e7b6aca7_00_inbox_AI俱乐部_人和AI协作_纪浩_参考案例_结构化.md - 00_inbox/纪浩-AI协作方法论-口述.md - 00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-结构化.md",
         "00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-结构化.md"),
    ],
    "30_wiki/tools/tool-纪浩-AI工作空间与导诊台设计法.md": [
        ("10_raw/sources/src_20260619_e7b6aca7_00_inbox_AI俱乐部_人和AI协作_纪浩_参考案例_结构化.md - 00_inbox/纪浩-AI协作方法论-口述.md - 00_inbox/AI俱乐部-人和AI协作-纪浩-五层结构-结构化.md - 00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-结构化.md",
         "00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-结构化.md"),
    ],
    "30_wiki/tools/tool-纪浩-Do-first-PDCA渐进迭代法.md": [
        ("10_raw/sources/src_20260619_e18427b7_00_inbox_纪浩_AI协作方法论_口述.md - 00_inbox/纪浩-AI协作方法论-口述.md",
         "00_inbox/纪浩-AI协作方法论-口述.md"),
    ],
    "30_wiki/tools/tool-纪浩-problem-validation-four-checks.md": [
        ("10_raw/sources/src_20260619_e18427b7_00_inbox_纪浩_AI协作方法论_口述.md - 00_inbox/纪浩-AI协作方法论-口述.md",
         "00_inbox/纪浩-AI协作方法论-口述.md"),
    ],
    "30_wiki/tools/tool-纪浩-日志驱动排查法.md": [
        ("10_raw/sources/src_20260619_71c86250_00_inbox_AI俱乐部_人和AI协作_纪浩_五层结构_结构化.md - 00_inbox/纪浩-AI协作方法论-口述.md - 00_inbox/AI俱乐部-人和AI协作-纪浩-五层结构-结构化.md",
         "00_inbox/AI俱乐部-人和AI协作-纪浩-五层结构-结构化.md"),
    ],
    "30_wiki/tools/tool-纪浩-真需求四要素验证法.md": [
        ("10_raw/sources/src_20260619_e18427b7_00_inbox_纪浩_AI协作方法论_口述.md - 00_inbox/纪浩-AI协作方法论-口述.md",
         "00_inbox/纪浩-AI协作方法论-口述.md"),
    ],
}

n_typo = 0
for card_rel, fixes in TYPO_FIXES.items():
    card_path = ROOT / card_rel
    if not card_path.exists():
        print(f"SKIP (not found): {card_rel}")
        continue
    text = card_path.read_text(encoding="utf-8", errors="replace")
    for old, new in fixes:
        if old in text:
            text = text.replace(old, new)
            n_typo += 1
    card_path.write_text(text, encoding="utf-8")
print(f"Typo fixes applied: {n_typo}")

# 15 source_unknown -> src_unknown
n_su = 0
for md in (ROOT / "30_wiki").rglob("*.md"):
    if ".trash" in md.parts:
        continue
    text = md.read_text(encoding="utf-8", errors="replace")
    new_text = text.replace("source_unknown", "src_unknown")
    if new_text != text:
        n_su += 1
        md.write_text(new_text, encoding="utf-8")
print(f"source_unknown -> src_unknown: {n_su}")
print(f"Total: {n_typo + n_su}")
