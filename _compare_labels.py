"""Compare auto_label_chunk() against Gold Standard manual labels.
Reads gold-standard-manual-labels.md, extracts the 15 chunks,
runs auto_label_chunk() on each, computes accuracy metrics.
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")

# Import from KDO
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import (
    auto_label_chunk, load_tag_registry, flatten_dimensions,
    prescreen_chunk, validate_and_route, llm_label_chunk,
)
from kdo.llm import LLMConfig
from kdo.workspace import safe_read

# --- Parse Gold Standard ---

def parse_gold_standard(path: Path) -> list[dict]:
    """Extract the 15 labeled chunks from gold-standard-manual-labels.md."""
    text = safe_read(path)
    chunks = []
    # Split on "## Chunk N" sections
    sections = re.split(r'\n(?=## Chunk \d+)', text)
    for sec in sections:
        m = re.match(r'## Chunk (\d+).*?\n', sec)
        if not m:
            continue
        chunk_id = int(m.group(1))
        # Extract source card
        src_m = re.search(r'\*\*来源卡片\*\*\s*\|\s*`(.+?)`', sec)
        source_card = src_m.group(1) if src_m else "unknown"

        # Extract chunk content
        content_m = re.search(r'\*\*chunk 内容\*\*\s*\|\s*(.+?)(?:\n\n\||\n\n##)', sec, re.DOTALL)
        if not content_m:
            # Try alternative: after the chunk header
            content_m = re.search(r'\*\*chunk 内容\*\*\s*\|\s*(.+?)(?=\n\|\s*\n\|)', sec, re.DOTALL)
        chunk_text = ""
        if content_m:
            chunk_text = content_m.group(1).strip().strip('"').strip("'")

        # Extract labels from the dimension table
        labels = {}
        table_section = sec.split("| 维度 | 标签值 | 理由 |")
        if len(table_section) > 1:
            rows = table_section[1].strip().split("\n")
            for row in rows:
                cells = [c.strip() for c in row.split("|") if c.strip()]
                if len(cells) >= 2:
                    dim = cells[0].strip()
                    val = cells[1].strip()
                    if dim and val and dim not in ("维度", "---", ":--"):
                        labels[dim] = val

        chunks.append({
            "id": chunk_id,
            "source_card": source_card,
            "text": chunk_text,
            "gold_labels": labels,
        })

    return chunks


# --- Compare Labels ---

DIMS_TO_COMPARE = [
    "chunk_type", "method_family", "audience", "perspective",
    "platform", "confidence", "data_generation", "value_tier",
    "prerequisite_knowledge", "expiry", "usage_depth",
]

def compare_chunk(gold_labels: dict, auto_result: dict) -> dict:
    """Compare auto labels against gold standard for one chunk."""
    auto_labels = {}
    for lbl in auto_result.get("result", {}).get("labels", []):
        auto_labels[lbl["dimension"]] = lbl["value"]

    matches = 0
    mismatches = 0
    gold_only = 0
    auto_only = 0
    details = []

    for dim in DIMS_TO_COMPARE:
        gold_val = gold_labels.get(dim)
        auto_val = auto_labels.get(dim)
        if gold_val and auto_val:
            if str(gold_val) == str(auto_val):
                matches += 1
                details.append(f"  ✅ {dim}: {gold_val}")
            else:
                mismatches += 1
                details.append(f"  ❌ {dim}: gold={gold_val} auto={auto_val}")
        elif gold_val and not auto_val:
            gold_only += 1
            details.append(f"  ⚠️ {dim}: gold={gold_val} auto=<missing>")
        elif auto_val and not gold_val:
            auto_only += 1
            details.append(f"  ➕ {dim}: gold=<none> auto={auto_val}")

    total_gold = matches + mismatches + gold_only
    accuracy = matches / total_gold if total_gold > 0 else 0

    return {
        "matches": matches, "mismatches": mismatches,
        "gold_only": gold_only, "auto_only": auto_only,
        "accuracy": round(accuracy, 3),
        "details": details,
    }


def main():
    gold_path = VAULT / "30_wiki" / "decisions" / "gold-standard-manual-labels.md"
    if not gold_path.exists():
        print(f"Gold standard file not found: {gold_path}")
        return 1

    gold_chunks = parse_gold_standard(gold_path)
    print(f"Parsed {len(gold_chunks)} Gold Standard chunks.\n")

    # Check LLM
    llm_config = LLMConfig.from_yaml()
    llm_available = llm_config.is_configured()
    print(f"LLM configured: {llm_available}")
    if not llm_available:
        print("⚠ Running pre-screen only (no LLM). Results will be noisy.\n")
    else:
        print(f"Model: {llm_config.model}\n")

    registry = load_tag_registry(VAULT)
    if not registry:
        print("ERROR: tag-registry not found")
        return 1

    total_matches = 0
    total_mismatches = 0
    total_gold_only = 0
    total_auto_only = 0
    all_results = []

    for chunk in gold_chunks:
        print(f"--- Chunk {chunk['id']} ({chunk['source_card'].split('/')[-1][:40]}) ---")
        print(f"  Gold labels: {len(chunk['gold_labels'])} dims")
        print(f"  Text: {chunk['text'][:80]}...")

        result = auto_label_chunk(
            chunk["text"],
            registry=registry,
            llm_config=llm_config,
            top_k=15,  # More candidates for better coverage
        )

        comparison = compare_chunk(chunk["gold_labels"], result)
        total_matches += comparison["matches"]
        total_mismatches += comparison["mismatches"]
        total_gold_only += comparison["gold_only"]
        total_auto_only += comparison["auto_only"]

        print(f"  Accuracy: {comparison['accuracy']:.0%} ({comparison['matches']}/{comparison['matches']+comparison['mismatches']+comparison['gold_only']})")
        for d in comparison["details"]:
            print(d)
        print()
        all_results.append({**chunk, "comparison": comparison, "auto_result": result})

    total = total_matches + total_mismatches + total_gold_only
    overall_acc = total_matches / total if total > 0 else 0
    print("=" * 60)
    print(f"OVERALL: {total_matches}/{total} correct = {overall_acc:.1%}")
    print(f"  ✅ Matches:   {total_matches}")
    print(f"  ❌ Mismatches: {total_mismatches}")
    print(f"  ⚠️ Gold-only:  {total_gold_only} (auto missed)")
    print(f"  ➕ Auto-only:  {total_auto_only} (extra labels)")
    print(f"  Target:       ≥ 85%")

    # Save detailed results
    output_path = VAULT / "60_feedback" / "data-quality" / "label-results" / "gold-standard-comparison.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2, default=str)
    print(f"\nDetailed results saved to: {output_path}")

    return 0 if overall_acc >= 0.85 else 1


if __name__ == "__main__":
    sys.exit(main())
