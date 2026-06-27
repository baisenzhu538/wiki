"""Final batch source_refs fix: Steps 1-5 (mechanical) + Step 6-9 samples."""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")

def fix_file(path: Path, replacements: dict[str, str]) -> int:
    """Apply string replacements to a file. Returns number of replacements made."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    n = 0
    for old, new in replacements.items():
        if old in raw:
            raw = raw.replace(old, new)
            n += 1
    if n:
        path.write_text(raw, encoding="utf-8")
    return n

# Step 1: dict URL -> src_unknown
n1 = 0
for md in (ROOT / "30_wiki").rglob("*.md"):
    if ".trash" in md.parts: continue
    n1 += fix_file(md, {
        '{\'web\': \'MCP specification (modelcontextprotocol.io)\'}': 'src_unknown',
        '{\'web\': \'Anthropic MCP documentation\'}': 'src_unknown',
        '{\'web\': \'Competitive Intelligence Alliance CI Operating Model\'}': 'src_unknown',
        '{\'web\': \'BestBootcamps CI Framework Guide 2026\'}': 'src_unknown',
        '{\'web\': \'LangGraph multi-agent patterns (LangChain docs)\'}': 'src_unknown',
        '{\'web\': \'Paiteq multi-agent architecture guide\'}': 'src_unknown',
        '{\'web\': \'Lushbinary agent architecture patterns\'}': 'src_unknown',
        '{\'web\': \'ATAM (Architecture Trade-off Analysis Method)\'}': 'src_unknown',
        '{\'web\': \'SARA (Software Architecture Review & Assessment)\'}': 'src_unknown',
        '{\'web\': \'NHS Digital Software Engineering Quality Framework\'}': 'src_unknown',
        '{\'web\': \'dycke-gurevych-2025 counterfactual evaluation framework\'}': 'src_unknown',
        '{\'web\': \'Richards Heuer & Pherson, Structured Analytic Techniques for Intelligence Analysis\'}': 'src_unknown',
        '{\'web\': \'CIA Tradecraft Primer\'}': 'src_unknown',
        '{\'web\': \'OSINT tools 2025-2026 comparison (Defcon Level, Cyble, Kali Linux Tutorials)\'}': 'src_unknown',
        '{\'web\': \'OSINT tools 2025-2026 comparison\'}': 'src_unknown',
    })
# Also catch any remaining {'web': '...'} patterns
for md in (ROOT / "30_wiki").rglob("*.md"):
    if ".trash" in md.parts: continue
    raw = md.read_text(encoding="utf-8", errors="replace")
    new_raw = re.sub(r"\{'web':\s*'[^']*'\}", "src_unknown", raw)
    if new_raw != raw:
        n1 += 1
        md.write_text(new_raw, encoding="utf-8")

# Step 2: Placeholders -> src_unknown
n2 = 0
for md in (ROOT / "30_wiki").rglob("*.md"):
    if ".trash" in md.parts: continue
    n2 += fix_file(md, {
        "source_unknown": "src_unknown",
        "system-log": "src_unknown",
        "mineru-docs": "src_unknown",
    })

# Step 3: Strategic domain OCR suffix strip
n3 = 0
for md in (ROOT / "30_wiki").rglob("*.md"):
    if ".trash" in md.parts: continue
    raw = md.read_text(encoding="utf-8", errors="replace")
    replacements = [
        (r"00_inbox/战略专题/冉鹏战略课逐字稿_ocr\.md.*?(?=\n|\r|$)",
         "00_inbox/战略专题/冉鹏战略课录屏_ocr.md"),
        (r"00_inbox/战略专题/冉鹏老师战略课程知识点_ocr\.md.*?(?=\n|\r|$)",
         "00_inbox/战略专题/冉鹏老师战略课程知识点_ocr.md"),
        (r"00_inbox/战略专题/冉鹏战略课录屏_ocr\.md\s*§?\s*\d+(-\d+)?",
         "00_inbox/战略专题/冉鹏战略课录屏_ocr.md"),
        (r"00_inbox/战略专题/冉鹏老师战略课知识库_ocr\.md\s*§?\s*\d+(-\d+)?",
         "00_inbox/战略专题/冉鹏老师战略课知识库_ocr.md"),
    ]
    for pat, repl in replacements:
        new_raw, subs = re.subn(pat, repl, raw)
        if subs:
            n3 += subs
            raw = new_raw
    if n3:
        md.write_text(raw, encoding="utf-8")

# Step 4: Anchor strip
n4 = 0
for md in (ROOT / "30_wiki").rglob("*.md"):
    if ".trash" in md.parts: continue
    n4 += fix_file(md, {
        "10_raw/sources/src_20260619_f35cd8b6_20_memory_corrections.md#C-3": "10_raw/sources/src_20260619_f35cd8b6_20_memory_corrections.md",
        "10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md#P-16": "10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md",
    })

# Step 5: Chinese memo -> src_unknown
MEMO_PATTERNS = [
    "feishu-publishing (段王爷 SKILL.md)",
    "feishu-publishing (",
    "老板老朱 2026-06-23 口述",
    "七件事集团深度调研综合报告",
    "七件事集团商业模式全解析",
    "HILTS框架（ScienceDirect, 2026）",
    "NVIDIA开源对话基准2025年",
    "KGC 2022 Taxonomy Design Tutorial",
    "Gruber知识本体原则",
    "逻辑事件集团深度调研综合报告",
    "逻辑事件集团商业模型全解析",
]
n5 = 0
for md in (ROOT / "30_wiki").rglob("*.md"):
    if ".trash" in md.parts: continue
    for pat in MEMO_PATTERNS:
        if fix_file(md, {pat: "src_unknown"}):
            n5 += 1

print(f"Step 1 (dict URL):      {n1}")
print(f"Step 2 (placeholders):  {n2}")
print(f"Step 3 (strategic OCR): {n3}")
print(f"Step 4 (anchors):       {n4}")
print(f"Step 5 (memo):          {n5}")
print(f"Total: {n1+n2+n3+n4+n5}")
