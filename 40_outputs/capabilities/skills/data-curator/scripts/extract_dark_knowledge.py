#!/usr/bin/env python3
"""Dark Knowledge Auto-Extractor from Oral Transcripts.

Scans unstructured oral transcripts and identifies dark knowledge candidates:
  - tool_usage: specific tool configurations, tricks, integration patterns
  - failure: mistakes, lessons learned, "what went wrong"
  - insight: aphorisms, professional heuristics, original judgments
  - workflow: sequential descriptions of how something is done

Outputs pre-filled 6-field templates for 老顽童 to review and refine.
Designed for non-structured transcripts (~78KB oral text).

Usage:
  python extract_dark_knowledge.py --input "00_inbox/design/AI设计-AI设计师实操培训01.txt" --dry-run
  python extract_dark_knowledge.py --input "00_inbox/design/AI设计-AI设计师实操培训01.txt" --output "60_feedback/data-quality/dk-candidates/"
"""

import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

VAULT_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
OUTPUT_DIR = VAULT_ROOT / "60_feedback" / "data-quality" / "dk-candidates"

# --- Detection Patterns ---

# Tool names to detect
KNOWN_TOOLS = [
    "Cubox", "NotebookLM", "豆包", "Midjourney", "GPT", "Claude", "PS",
    "Photoshop", "Illustrator", "Figma", "Canva", "PaddleOCR", "Obsidian",
    "飞书", "Markdown", "JSON", "Key Value", "RAG", "GraphRAG", "kdo",
    "Notion", "印象笔记", "有道云笔记", "Python", "Git", "Excel",
    "P图", "ClassCode", "Antigravity", "Yi", "元器"
]

# Action verbs indicating tool usage
TOOL_ACTION_PATTERNS = [
    r"(?:用|使用|打开|配置|推荐|试了|换|切换到|装|下载|买了)\s*(?:了|过)?\s*[" + "|".join(KNOWN_TOOLS) + r"]",
    r"(?:扔|丢|放|导入|导出|同步|保存)(?:给|到|进).*?(?:[" + "|".join(KNOWN_TOOLS) + r"]|知识库|文件夹|笔记)",
    r"[" + "|".join(KNOWN_TOOLS) + r"].*?(?:好用|不好用|好用吗|不行|可以|推荐|别用|放弃)",
]

# Failure/lesson patterns
FAILURE_PATTERNS = [
    r"(?:发现|结果|但是|然而|没想到|踩了|遇到|出现)(?:.*?)(?:问题|不行|不能用|失败|错误|bug|卡|不管用|无效)",
    r"(?:犯了|踩了|掉进).*?(?:坑|错误|误区)",
    r"(?:教训|经验.*?告诉|后来.*?才|回头.*?看|反思)",
    r"(?:很多|好多|大量).*?(?:设计师|团队|人).*?(?:习惯.*?糟糕|不会|不知道|没用过|放弃)",
    r"(?:不要|别|千万别|警惕|注意|小心).*?(?:直接|轻易|随便|盲目)",
]

# Insight/aphorism patterns
INSIGHT_PATTERNS = [
    r"(?:本质上|核心是|归根结底|说白了|其实|真正.*?是)(.{10,80})",
    r"(?:一句话|总结|金句).*?[：:]\s*(.{10,100})",
    r"(?:我.*?觉得|我认为|我.*?理解|我的体感)(.{10,80})",
    r"(?:审美|品味|范式|心智|操盘手).{5,50}(?:是|不是|在于|就是)",
]

# Workflow patterns
WORKFLOW_PATTERNS = [
    r"(?:第一步|第二步|第三步|首先|然后|接着|最后|再|之后).*?(?:再|然后|接着)",
    r"(?:流程|步骤|阶段|工序).*?[：:].{10,100}",
    r"(?:分成|分为|拆成).*?(?:三步|两步|五步|三个|两个|五个)",
]

# --- Scoring ---

def score_candidate(segment: str, dk_type: str) -> float:
    """Score a candidate segment for card-worthiness (0.0-1.0)."""
    score = 0.3  # base

    # Specificity bonus
    if any(tool.lower() in segment.lower() for tool in KNOWN_TOOLS):
        score += 0.15
    if re.search(r"\d+", segment):  # contains numbers
        score += 0.05
    if len(segment) > 40 and len(segment) < 300:
        score += 0.10

    # Uniqueness bonus
    specific_names = ["月白", "Truman", "一堂", "大眉毛", "徐建", "阿蕊", "花总"]
    if any(name in segment for name in specific_names):
        score += 0.10

    # Actionability bonus
    if dk_type in ("tool_usage", "failure") and _has_how_to(segment):
        score += 0.15
    if dk_type == "workflow" and len(segment.split("。")) >= 3:
        score += 0.15
    if dk_type == "insight" and len(segment) < 120:
        score += 0.10

    # Penalty: too generic
    generic_words = ["重要", "关键", "核心", "基础", "必要"]
    if sum(1 for w in generic_words if w in segment) >= 3 and dk_type != "insight":
        score -= 0.10

    return min(1.0, max(0.0, score))


def _has_how_to(text: str) -> bool:
    """Check if text contains actionable how-to content."""
    how_patterns = [
        r"\d+[\.\)、].{5,}",       # numbered steps
        r"(?:打开|点击|输入|选择|设置|配置|保存|导出|导入|拖拽|复制|粘贴)",
        r"(?:先|再|然后|接着|最后)[^。]{3,30}",
    ]
    return any(re.search(p, text) for p in how_patterns)


# --- Segment Classification ---

def classify_segment(text: str) -> str | None:
    """Classify a text segment into a dark knowledge type, or None."""
    scores = {}

    # Check tool usage
    if any(re.search(p, text) for p in TOOL_ACTION_PATTERNS):
        scores["tool_usage"] = 0.7 + (0.1 if any(t.lower() in text.lower() for t in KNOWN_TOOLS) else 0)

    # Check failure
    if any(re.search(p, text) for p in FAILURE_PATTERNS):
        scores["failure"] = 0.6 + (0.1 if "修正" in text or "对策" in text or "不要" in text else 0)

    # Check insight
    if any(re.search(p, text) for p in INSIGHT_PATTERNS):
        scores["insight"] = 0.5 + (0.15 if len(text) < 120 else 0)

    # Check workflow
    if any(re.search(p, text) for p in WORKFLOW_PATTERNS):
        scores["workflow"] = 0.5 + (0.1 if len(text) > 60 else 0)

    if not scores:
        return None

    return max(scores, key=scores.get)


# --- Text Splitting ---

def split_transcript(text: str) -> list[str]:
    """Split oral transcript into candidate segments."""
    # Clean ASR artifacts
    text = re.sub(r"这个\s*", "", text)
    text = re.sub(r"然后呢\s*", "", text)
    text = re.sub(r"好不好\s*", "", text)

    # Split by sentence boundaries into larger context windows
    sentences = re.split(r"(?<=[。！？\.\!\?])\s*", text)
    segments = []
    buffer = []
    char_count = 0

    for sent in sentences:
        sent = sent.strip()
        if not sent or len(sent) < 5:
            continue
        buffer.append(sent)
        char_count += len(sent)
        # Flush when we have enough context
        if char_count >= 80 and len(buffer) >= 2:
            segments.append("".join(buffer))
            buffer = []
            char_count = 0

    # Flush remainder
    if buffer:
        segments.append("".join(buffer))

    return segments


# --- Pre-fill 6-field template ---

def prefill_template(segment: str, dk_type: str, source_path: str, score: float) -> dict:
    """Pre-fill the 6-field dark knowledge template."""
    template = {
        "title": "",
        "dark_knowledge_type": dk_type,
        "source_person": _infer_source_person(source_path),
        "source_context": f"口述稿: {Path(source_path).stem}",
        "score": round(score, 2),
        "original_quote": segment.strip()[:500],
        "use_case": "",
        "operation": "",
        "boundary": "",
        "why_valuable": "",
        "cross_reference": "",
    }

    # Auto-fill use_case based on type
    type_contexts = {
        "tool_usage": _extract_tool_context(segment),
        "failure": _extract_failure_context(segment),
        "insight": _extract_insight_context(segment),
        "workflow": _extract_workflow_context(segment),
    }
    template["use_case"] = type_contexts.get(dk_type, "")

    # Auto-fill operation if steps detected
    if dk_type in ("tool_usage", "workflow"):
        steps = _extract_steps(segment)
        if steps:
            template["operation"] = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps[:5]))

    # Auto-fill why_valuable
    template["why_valuable"] = _prefill_why_valuable(segment, dk_type)

    # Auto-fill boundary if conditionals detected
    boundary = _extract_boundary(segment)
    if boundary:
        template["boundary"] = boundary

    return template


def _infer_source_person(source_path: str) -> str:
    """Infer source person from file path."""
    path_lower = source_path.lower()
    if "设计" in path_lower and ("基础" in path_lower or "实操" in path_lower):
        return "月白"
    if "ai数据" in path_lower or "truman" in path_lower.lower():
        return "Truman"
    return "未知"


def _extract_tool_context(segment: str) -> str:
    """Extract tool usage context."""
    for tool in KNOWN_TOOLS:
        if tool.lower() in segment.lower():
            return f"在使用 {tool} 的场景中"
    return "在使用 AI 设计工具的场景中"


def _extract_failure_context(segment: str) -> str:
    """Extract failure context."""
    if "批量" in segment:
        return "在执行批量操作前"
    if "enrich" in segment.lower() or "中文" in segment:
        return "在处理中文内容时"
    return "在 KDO 管线操作中"


def _extract_insight_context(segment: str) -> str:
    """Extract insight context."""
    if "设计" in segment:
        return "在做 AI 设计相关的判断时"
    if "数据" in segment:
        return "在做数据相关决策时"
    return "在做专业判断时"


def _extract_workflow_context(segment: str) -> str:
    """Extract workflow context."""
    return "在建立 AI 设计工作流时"


def _extract_steps(text: str) -> list[str]:
    """Extract step-level instructions from text."""
    steps = []
    # Look for numbered sequences
    numbered = re.findall(r"(?:\d+[\.\)、])\s*(.{10,80})", text)
    if numbered:
        return [s.strip() for s in numbered[:5]]
    # Look for sequential markers
    seq = re.findall(r"(?:先|第一步|首先|然后|接着|最后|再|之后)\s*(.{10,80})", text)
    if seq:
        return [s.strip() for s in seq[:5]]
    return steps


def _extract_boundary(text: str) -> str:
    """Extract boundary conditions from text."""
    boundaries = re.findall(r"(?:但是|然而|不过|除非|除了|如果.*?不|不适用|不适合)(.{10,60})", text)
    if boundaries:
        return "；".join(b.strip() for b in boundaries[:2])
    return ""


def _prefill_why_valuable(segment: str, dk_type: str) -> str:
    """Pre-fill the 'why valuable' field."""
    reasons = {
        "tool_usage": f"具体工具配置技巧，不在任何通用 AI 训练语料中",
        "failure": "真实踩坑记录，包含具体症状→根因→修正。互联网不存在",
        "insight": f"个人专业体悟。'{" ".join(segment[:30].split()[:6])}...' — 这是只有这个人能说出来的判断",
        "workflow": "个人摸索出的工作流。不是通用方法论，是具体操作序列",
    }
    return reasons.get(dk_type, "不在任何 AI 训练语料中的独特知识")


# --- Main ---

def extract_from_transcript(input_path: str, dry_run: bool = True) -> list[dict]:
    """Main extraction pipeline."""
    filepath = VAULT_ROOT / input_path if not os.path.isabs(input_path) else Path(input_path)
    if not filepath.exists():
        print(f"ERROR: File not found: {filepath}")
        return []

    text = filepath.read_text(encoding="utf-8", errors="replace")
    segments = split_transcript(text)
    print(f"Split into {len(segments)} segments from {filepath.name}")

    candidates = []
    for seg in segments:
        dk_type = classify_segment(seg)
        if not dk_type:
            continue
        score = score_candidate(seg, dk_type)
        if score < 0.4:  # minimum threshold
            continue
        template = prefill_template(seg, dk_type, str(input_path), score)
        candidates.append(template)

    # Deduplicate (keep highest scored)
    seen = set()
    unique = []
    for c in sorted(candidates, key=lambda x: x["score"], reverse=True):
        key = c["original_quote"][:80]
        if key not in seen:
            seen.add(key)
            unique.append(c)

    # Report
    type_counts = Counter(c["dark_knowledge_type"] for c in unique)
    print(f"\nFound {len(unique)} unique dark knowledge candidates:")
    for dk_type, count in sorted(type_counts.items()):
        avg_score = sum(c["score"] for c in unique if c["dark_knowledge_type"] == dk_type) / count
        print(f"  {dk_type}: {count} (avg score: {avg_score:.2f})")

    if dry_run:
        # Show top 5
        print("\n--- Top 5 candidates ---")
        for i, c in enumerate(unique[:5], 1):
            preview = c["original_quote"][:100].replace("\n", " ")
            print(f"\n{i}. [{c['dark_knowledge_type']}] score={c['score']}")
            print(f"   {preview}...")
    else:
        # Write to output
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        stem = filepath.stem
        output_file = OUTPUT_DIR / f"{stem}-dk-candidates.json"
        output_file.write_text(json.dumps(unique, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nCandidates written to: {output_file}")

    return unique


def main():
    input_path = None
    dry_run = True

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--input" and i + 1 < len(args):
            input_path = args[i + 1]; i += 2
        elif args[i] == "--dry-run":
            dry_run = True; i += 1
        elif args[i] == "--output":
            dry_run = False; i += 1  # --output flag triggers write mode
        else:
            i += 1

    if not input_path:
        print("Usage: extract_dark_knowledge.py --input <path> [--dry-run|--output]")
        sys.exit(1)

    extract_from_transcript(input_path, dry_run=dry_run)


if __name__ == "__main__":
    main()
