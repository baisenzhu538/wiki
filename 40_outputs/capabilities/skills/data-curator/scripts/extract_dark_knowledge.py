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

# --- Scoring (v1.3: 4-dimension weighted) ---

def score_candidate(segment: str, dk_type: str) -> float:
    """Score a candidate segment for card-worthiness (0.0-1.0).

    Four dimensions, weighted:
      - specificity (0.30): concrete details — tools, numbers, names
      - uniqueness  (0.25): not generic, not public knowledge
      - independence(0.25): readable without surrounding context
      - actionability(0.20): can someone act on this?

    The weights differ by dk_type — insight cares more about uniqueness,
    tool_usage cares more about specificity.
    """
    weights = {
        "tool_usage": (0.30, 0.20, 0.25, 0.25),
        "failure":    (0.25, 0.30, 0.20, 0.25),
        "insight":    (0.15, 0.40, 0.30, 0.15),
        "workflow":   (0.30, 0.15, 0.25, 0.30),
    }
    w_sp, w_un, w_in, w_ac = weights.get(dk_type, (0.25, 0.25, 0.25, 0.25))

    specificity = _score_specificity(segment)
    uniqueness = _score_uniqueness(segment, dk_type)
    independence = _score_independence(segment, dk_type)
    actionability = _score_actionability(segment, dk_type)

    return w_sp * specificity + w_un * uniqueness + w_in * independence + w_ac * actionability


def _score_specificity(text: str) -> float:
    """Concrete details = higher score."""
    s = 0.0
    if any(t.lower() in text.lower() for t in KNOWN_TOOLS):
        s += 0.30
    if re.search(r"\d+", text):
        s += 0.15
    if any(name in text for name in ["月白", "Truman", "一堂", "大眉毛", "徐建", "阿蕊", "花总"]):
        s += 0.20
    if 40 < len(text) < 300:
        s += 0.15
    # Penalty: too many generic adjectives without substance
    generic = ["非常", "特别", "很", "挺", "比较"]
    if sum(1 for w in generic if w in text) >= 4:
        s -= 0.15
    return min(1.0, max(0.0, s))


def _score_uniqueness(text: str, dk_type: str) -> float:
    """Is this knowledge NOT in public AI training data?"""
    u = 0.3  # base — oral transcripts are inherently somewhat unique

    # Insight-specific: gold nugget detector
    if dk_type == "insight":
        u += _gold_nugget_score(text)

    # Tool-specific: named tool + specific trick
    if dk_type == "tool_usage":
        if any(re.search(rf"{t}.*?(?:可以|能|会|用来|用来做)", text) for t in KNOWN_TOOLS):
            u += 0.25
        if re.search(r"(?:免费|不用钱|省(?:了|下)|不花钱|白嫖)", text):
            u += 0.10

    # Failure: contains root cause analysis
    if dk_type == "failure":
        if re.search(r"(?:根因|是因为|之所以|原因.*?是|归根结底|本质上)", text):
            u += 0.30

    # Workflow: specific sequence, not generic advice
    if dk_type == "workflow":
        if len(re.findall(r"(?:先|再|然后|接着|最后|第一步|第二步)", text)) >= 3:
            u += 0.20

    # Penalty: sounds like public knowledge
    public_sounding = [
        r"(?:大家.*?知道|众所周知|一般来说|通常.*?会|很多人.*?都)",
        r"(?:重要.*?是|关键.*?是|核心.*?是|基础.*?是)\s*(?:要|需要|应该)",
    ]
    if any(re.search(p, text) for p in public_sounding):
        u -= 0.20

    return min(1.0, max(0.0, u))


def _gold_nugget_score(text: str) -> float:
    """Detect genuine aphorisms vs filler '我觉得' statements.

    Gold nugget signals:
      - Short and punchy (<80 chars)
      - Contains contrast/reversal/paradox (不是X而是Y, 以前X现在Y)
      - Standalone quotable (去掉"我觉得"仍然成立)
      - Has original metaphor/analogy (像/如同/相当于/活菩萨)
      - Counter-intuitive claim (其实/本质上/恰恰/反而)

    Noise signals:
      - Long and rambling (>150 chars for an 'insight')
      - Heavy on filler words (这个/然后呢/就是说)
      - Statement of obvious preference (我喜欢/我觉得好用)
    """
    score = 0.0

    # Positive signals
    if len(text) < 80:
        score += 0.25
    elif len(text) > 150:
        score -= 0.20

    if re.search(r"(?:不是.{2,10}(?:而是|就是|是)|以前.{2,10}现在|过去.{2,10}现在)", text):
        score += 0.20  # contrast/reversal

    if re.search(r"(?:本质上|其实|恰恰|反而|说到底|归根结底)", text):
        score += 0.15  # counter-intuitive

    if re.search(r"(?:活菩萨|许愿|教材|燃料|护城河|操盘手|查字典|食材|飞轮)", text):
        score += 0.20  # original metaphor

    # Negative signals
    filler_count = len(re.findall(r"(?:这个|然后呢|就是说|好不好|对吧|是不是)", text))
    if filler_count >= 3:
        score -= 0.20

    if re.search(r"^(?:我|我们)\s*(?:觉得|感觉|认为|喜欢|爱)", text) and len(text) > 60:
        score -= 0.10  # just an opinion, not a nugget

    return score


def _score_independence(text: str, dk_type: str = "") -> float:
    """Can this text be understood without surrounding context?

    Independent: contains its own subject, verb, object — a complete thought.
    Dependent: starts with '然后' '所以' '但是' implying prior context needed.
    """
    i = 0.4  # base

    # Oral speech penalty: relaxed for tool_usage/workflow (connectors are natural in speech)
    penalty = 0.12 if dk_type in ("tool_usage", "workflow") else 0.25
    if re.match(r"^\s*(?:然后|所以|但是|而且|因为|接着|之后|后来|于是)", text):
        i -= penalty

    # Contains demonstrative without antecedent (这个/那个/它 without prior reference)
    if re.search(r"^(?:这个|那个|它|他|她|这|那)\s*\S", text):
        if not re.search(r"(?:是|叫|指|就是|指的是)", text[:30]):
            i -= 0.15  # "这个..." — what is 这个?

    # Has a clear subject-verb-object structure
    if re.search(r".{3,20}(?:是|用|做|有|能|会|可以|需要|应该).{3,50}", text):
        i += 0.20

    # Standalone judgment — could be a tweet
    if len(text) < 100 and not re.match(r"^\s*(?:然后|所以|但是)", text):
        i += 0.15

    return min(1.0, max(0.0, i))


def _score_actionability(text: str, dk_type: str) -> float:
    """Can someone act on this knowledge?"""
    a = 0.2  # base

    if dk_type in ("tool_usage", "workflow"):
        if re.search(r"\d+[\.\)、]\s*.{5,}", text):
            a += 0.30  # numbered steps
        if len(re.findall(r"(?:打开|点击|输入|选择|设置|配置|保存|导出|导入|拖拽|复制|粘贴|下载|安装)", text)) >= 2:
            a += 0.20

    if dk_type == "failure":
        if re.search(r"(?:修正|对策|解决|修复|改进).{5,30}", text):
            a += 0.25
        if re.search(r"(?:不要|别|避免|禁止|停止).{5,30}", text):
            a += 0.20

    if dk_type == "insight":
        # Insights aren't directly actionable — they inform judgment. Lower ceiling.
        if re.search(r"(?:所以|因此|于是).{5,30}(?:应该|需要|可以|值得)", text):
            a += 0.15

    return min(1.0, max(0.0, a))


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

    # Check insight — higher bar: must pass gold nugget test
    if any(re.search(p, text) for p in INSIGHT_PATTERNS):
        nugget = _gold_nugget_score(text)
        scores["insight"] = 0.5 + nugget  # need at least 0.15 nugget score to clear base threshold

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

    # Operation: DO NOT auto-extract broken steps.
    # Leave blank with annotation. 老顽童 does this from original_quote.
    if dk_type in ("tool_usage", "workflow", "failure"):
        steps = _extract_steps(segment)
        if steps and all(len(s) > 20 for s in steps[:3]) and len(steps) >= 2:
            # Only fill if we have ≥2 real steps
            template["operation"] = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps[:5]))
        else:
            template["operation"] = "[需从原始表述中提取操作步骤]"
    else:
        template["operation"] = "[不适用]"

    # Auto-fill why_valuable
    template["why_valuable"] = _prefill_why_valuable(segment, dk_type)

    # Auto-fill boundary if conditionals detected
    boundary = _extract_boundary(segment)
    if boundary:
        template["boundary"] = boundary

    # Auto-suggest cross-references from existing cards
    refs = _match_existing_cards(segment, dk_type)
    if refs:
        template["cross_reference"] = ", ".join(refs[:3])

    return template


# --- Cross-Reference Matching ---

# Lazily loaded card index
_card_index = None

def _load_card_index() -> dict[str, str]:
    """Load a lightweight index: card_slug → title + keywords."""
    global _card_index
    if _card_index is not None:
        return _card_index

    concepts_dir = VAULT_ROOT / "30_wiki" / "concepts"
    _card_index = {}
    for fp in concepts_dir.glob("*.md"):
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")[:3000]
            # Extract title from first H1 or frontmatter
            title_match = re.search(r"^#\s+(.+)", text, re.MULTILINE)
            fm_match = re.search(r"^title:\s*\"?(.+?)\"?\s*$", text, re.MULTILINE)
            title = (title_match.group(1) if title_match else
                     fm_match.group(1) if fm_match else fp.stem)
            # Extract key terms from body
            body = text[text.find("---\n", 4) + 4:] if "---\n" in text[4:] else text
            body = body[:2000]
            _card_index[fp.stem] = f"{title} {body[:500]}"
        except Exception:
            pass
    return _card_index


def _match_existing_cards(segment: str, dk_type: str) -> list[str]:
    """Suggest existing concept cards that this dark knowledge relates to."""
    card_index = _load_card_index()
    if not card_index:
        return []

    # Extract key terms from the segment (CJK bigrams + tool names)
    terms = set()
    for tool in KNOWN_TOOLS:
        if tool.lower() in segment.lower():
            terms.add(tool)

    # CJK bigrams
    cjk_chars = re.findall(r"[一-鿿]{2,4}", segment)
    # Keep only mid-frequency terms (not every stop word)
    term_counts = Counter(cjk_chars)
    for term, count in term_counts.most_common(15):
        if count >= 2 and len(term) >= 2:
            terms.add(term)

    if not terms:
        return []

    # Score each card by term overlap
    scores = {}
    for slug, content in card_index.items():
        overlap = sum(1 for t in terms if t in content)
        if overlap >= 2:
            scores[slug] = overlap

    # Return top matches
    return [slug for slug, _ in sorted(scores.items(), key=lambda x: -x[1])[:3]]


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


def _deduplicate_semantic(candidates: list[dict]) -> list[dict]:
    """Deduplicate candidates — keep highest scored, merge near-duplicates.

    Uses CJK bigram overlap: if two candidates share >60% bigrams, keep the higher-scored one.
    """
    if len(candidates) <= 1:
        return candidates

    def bigrams(text: str) -> set[str]:
        cjk = re.findall(r"[一-鿿]{2}", text)
        return set(cjk)

    sorted_cands = sorted(candidates, key=lambda x: x["score"], reverse=True)
    unique = []
    seen_sigs = []

    for c in sorted_cands:
        sig = bigrams(c["original_quote"])
        if len(sig) < 3:  # too short to meaningfully compare
            unique.append(c)
            continue

        is_dup = False
        for prev_sig in seen_sigs:
            if not prev_sig:
                continue
            overlap = len(sig & prev_sig) / min(len(sig), len(prev_sig)) if min(len(sig), len(prev_sig)) > 0 else 0
            if overlap > 0.7:
                is_dup = True
                break

        if not is_dup:
            unique.append(c)
            seen_sigs.append(sig)

    return unique


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
        if score < 0.45:  # v1.3: tighter than B+ (0.4) but not over-strict
            continue
        template = prefill_template(seg, dk_type, str(input_path), score)
        candidates.append(template)

    # Deduplicate with semantic-aware overlap detection
    unique = _deduplicate_semantic(candidates)

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
