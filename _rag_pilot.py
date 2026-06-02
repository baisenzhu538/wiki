"""RAG Domain Pilot Phase 1: auto-label RAG cards, analyze coverage."""
import json, sys
from pathlib import Path
from collections import Counter

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import (
    load_tag_registry, flatten_dimensions, llm_label_chunk,
    extract_chunks_from_card, auto_label_chunk,
)
from kdo.llm import LLMConfig
from kdo.workspace import safe_read, parse_frontmatter

CORE = ["chunk_type","method_family","audience","perspective",
        "confidence","platform","expiry","prerequisite_knowledge","usage_depth"]

# Key RAG sub-topics to check coverage
RAG_TOPICS = [
    "检索/retrieval", "索引/indexing", "分块/chunking", "排序/ranking",
    "向量/embedding", "图谱/graph", "标注/labeling", "评估/evaluation",
    "管线/pipeline", "知识管理/knowledge-mgmt"
]

def main():
    # Find RAG-related cards
    concepts = VAULT / "30_wiki" / "concepts"
    keywords = ["rag", "RAG", "GraphRAG", "embedding", "向量", "检索", "graph-rag"]
    rag_cards = []
    for f in sorted(concepts.glob("*.md")):
        text = safe_read(f)
        if any(kw.lower() in text.lower() for kw in keywords):
            rag_cards.append(f)

    print(f"Found {len(rag_cards)} RAG-related cards")

    # Pick top N by relevance (prioritize cards with "rag" in filename or high keyword density)
    primary = [c for c in rag_cards if "rag" in c.stem.lower() or "graph" in c.stem.lower()]
    secondary = [c for c in rag_cards if c not in primary]
    selected = (primary + secondary)[:10]  # Max 10 for pilot

    print(f"Labeling {len(selected)} cards...\n")

    cfg = LLMConfig.from_yaml()
    all_dims = flatten_dimensions(load_tag_registry(VAULT))
    core_dims = {k: v for k, v in all_dims.items() if k in CORE}

    results = []
    all_labels = {d: Counter() for d in CORE + ["heading_keywords"]}
    total_chunks = 0
    covered_topics = set()

    for card_path in selected:
        text = safe_read(card_path)
        fm, body = parse_frontmatter(text)
        chunks = extract_chunks_from_card(text)
        if not chunks:
            continue

        hint = f"{fm.get('title', card_path.stem)}（{fm.get('type', 'concept')}卡）"
        print(f"  {card_path.stem[:50]} ({len(chunks)} chunks)")

        for chunk in chunks:
            decisions = llm_label_chunk(chunk["text"], core_dims, config=cfg, card_hint=hint)
            if decisions:
                total_chunks += 1
                for d in decisions:
                    all_labels[d["dimension"]][d["value"]] += 1

                # Check RAG topic coverage from chunk headings + content
                heading = chunk["heading"].lower()
                text_lower = chunk["text"].lower()
                for topic in RAG_TOPICS:
                    kw = topic.split("/")[0]
                    if kw in heading or kw in text_lower:
                        covered_topics.add(topic)

    # --- Analysis ---
    print(f"\n{'='*60}")
    print(f"RAG Pilot Phase 1 Results: {len(selected)} cards, {total_chunks} chunks\n")

    print("RAG Sub-topic Coverage:")
    for topic in RAG_TOPICS:
        status = "covered" if topic in covered_topics else "MISSING"
        marker = "  " if topic in covered_topics else "XX"
        print(f"  {marker} {topic}: {status}")

    coverage = len(covered_topics) / len(RAG_TOPICS) * 100
    print(f"\nCoverage: {len(covered_topics)}/{len(RAG_TOPICS)} ({coverage:.0f}%)")
    print(f"Target: >= 5 topics covered (50%)")

    # Label distribution
    print(f"\nLabel distribution:")
    for dim in CORE[:4]:  # Core 4 dims
        top3 = all_labels[dim].most_common(3)
        print(f"  {dim}: {dict(top3)}")

    # Save
    out = VAULT / "60_feedback/data-quality/label-results/rag-pilot-results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump({
            "cards_labeled": len(selected),
            "total_chunks": total_chunks,
            "rag_topic_coverage": list(covered_topics),
            "coverage_pct": coverage,
            "label_distribution": {d: dict(all_labels[d].most_common(5)) for d in CORE[:4]},
        }, f, ensure_ascii=False, indent=2)
    print(f"\nSaved: {out}")

if __name__ == "__main__":
    main()
