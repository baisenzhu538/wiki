"""Pilot: label 20 diverse cards, collect 9-dim data, analyze patterns."""
import json, re, sys
from pathlib import Path, PurePath
from collections import Counter, defaultdict

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import (
    load_tag_registry, flatten_dimensions, llm_label_chunk, extract_chunks_from_card,
)
from kdo.llm import LLMConfig
from kdo.workspace import safe_read, parse_frontmatter

CORE = ["chunk_type","method_family","audience","perspective",
        "confidence","platform","expiry","prerequisite_knowledge","usage_depth"]

# --- Card hint generation ---

def build_card_hint(filename: str, fm: dict, body: str) -> str:
    """Generate card context hint from filename and frontmatter."""
    stem = Path(filename).stem
    domain = fm.get("domain", [])
    card_type = fm.get("type", "concept")
    title = fm.get("title", stem)

    # Domain → hint
    domain_hints = {
        "master": "通用方法论/认知工具",
        "yitang": "一堂课程体系/创业方法论",
        "ai-saas": "AI产品/LLM应用",
        "design": "AI设计/视觉传达",
        "healthcare": "医疗IT",
    }
    domain_str = domain_hints.get(domain[0] if isinstance(domain, list) and domain else domain, "通用")

    # Type → hint
    type_hints = {
        "concept": "概念卡",
        "tool": "工具卡",
        "framework": "框架卡",
        "decision": "决策记录",
        "improvement-plan": "改进方案",
        "system": "系统设计",
        "entity": "实体卡",
    }
    type_str = type_hints.get(card_type, "概念卡")

    # Filename prefix → extra context
    prefix_hints = {
        "master-decision": "讨论决策卫生/认知偏误/判断分解",
        "master-cognitive": "讨论认知偏误/自检清单",
        "master-systems": "讨论系统思维/知识管理",
        "yt-decision": "讨论Y模型/决策框架/ROI评估",
        "yt-entrepreneur": "讨论创业方法论/五步法",
        "yt-model": "讨论一堂知识框架/模型",
        "yt-tool": "讨论管理工具/操作流程",
        "ocr-一堂": "OCR提取的一堂课程内容",
        "design-": "AI设计方法/工具",
        "ai-native": "AI原生工作方式",
        "kdo-": "KDO自身方法论",
    }
    extra = ""
    for prefix, hint in prefix_hints.items():
        if stem.startswith(prefix):
            extra = f"，讨论{hint}"
            break

    return f"{title[:40]}（{domain_str}{type_str}{extra}）"


# --- Card selection ---

def select_pilot_cards(n=20):
    """Select diverse cards across domains, types, and content density."""
    concepts = VAULT / "30_wiki" / "concepts"
    cards = []

    for f in sorted(concepts.glob("*.md")):
        text = safe_read(f)
        fm, body = parse_frontmatter(text)
        if not fm: continue
        chunks = extract_chunks_from_card(text)
        if not chunks: continue

        domain = fm.get("domain", [])
        dom = domain[0] if isinstance(domain, list) and domain else str(domain)
        ctype = fm.get("type", "concept")
        status = fm.get("status", "draft")

        cards.append({
            "path": f, "stem": f.stem,
            "domain": dom, "type": ctype, "status": status,
            "chunks": len(chunks), "body_len": len(body),
            "fm": fm,
        })

    # Stratified selection: ensure domain + type diversity
    selected = []
    domain_counts = defaultdict(int)
    type_counts = defaultdict(int)

    # Sort by chunk count (prefer richer cards) then sample
    cards.sort(key=lambda c: -c["chunks"])

    for card in cards:
        if len(selected) >= n: break
        dom = card["domain"]
        ct = card["type"]
        # Max 5 per domain, max 8 per type
        if domain_counts[dom] >= 5: continue
        if type_counts[ct] >= 8: continue
        # Skip OCR cards if we have enough non-OCR
        if card["stem"].startswith("ocr-") and len(selected) > 15: continue
        selected.append(card)
        domain_counts[dom] += 1
        type_counts[ct] += 1

    return selected


# --- Main ---

def main():
    print("Selecting pilot cards...")
    cards = select_pilot_cards(20)
    print(f"Selected {len(cards)} cards:\n")
    for i, c in enumerate(cards, 1):
        print(f"  {i:2d}. [{c['domain']:12s}] [{c['type']:16s}] {c['stem'][:50]} ({c['chunks']} chunks)")

    cfg = LLMConfig.from_yaml()
    print(f"\nLLM: {cfg.model}\n")

    all_dims = flatten_dimensions(load_tag_registry(VAULT))
    core_dims = {k: v for k, v in all_dims.items() if k in CORE}

    results = []
    total_chunks = 0
    dim_dist = {d: Counter() for d in CORE}

    for i, card in enumerate(cards, 1):
        text = safe_read(card["path"])
        chunks = extract_chunks_from_card(text)
        hint = build_card_hint(str(card["path"]), card["fm"], text)
        total_chunks += len(chunks)

        print(f"[{i}/{len(cards)}] {card['stem'][:45]} ({len(chunks)} chunks)")
        card_result = {"card": card["stem"], "domain": card["domain"], "chunks": []}

        for chunk in chunks:
            decisions = llm_label_chunk(chunk["text"], core_dims, config=cfg, card_hint=hint)
            labels = {}
            if decisions:
                for d in decisions:
                    dim_dist[d["dimension"]][d["value"]] += 1
                    labels[d["dimension"]] = d["value"]
            card_result["chunks"].append({"heading": chunk["heading"][:60], "labels": labels})

        results.append(card_result)

    # --- Analysis ---
    print("\n" + "=" * 60)
    print(f"PILOT RESULTS: {len(cards)} cards, {total_chunks} chunks\n")

    # Per-dimension distribution
    print("Label distribution per dimension:")
    for dim in CORE:
        dist = dim_dist[dim]
        if not dist:
            print(f"  {dim}: <no data>")
            continue
        top5 = dist.most_common(5)
        total = sum(dist.values())
        print(f"  {dim} ({total} labels):")
        for val, count in top5:
            bar = "█" * int(count / total * 40)
            print(f"    {val:25s} {count:4d} ({count/total*100:5.1f}%) {bar}")

    # Card-level stats
    print(f"\nCard-level stats:")
    for r in results:
        n = len(r["chunks"])
        has_chunk_type = sum(1 for c in r["chunks"] if "chunk_type" in c["labels"])
        has_confidence = sum(1 for c in r["chunks"] if "confidence" in c["labels"])
        print(f"  {r['card'][:45]:45s} {n:2d} chunks  ct={has_chunk_type}/{n}  conf={has_confidence}/{n}")

    # Save
    out = VAULT / "60_feedback/data-quality/label-results/pilot-20-results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump({
            "cards": len(cards), "chunks": total_chunks,
            "dim_distribution": {d: dict(dim_dist[d].most_common()) for d in CORE if dim_dist[d]},
            "results": results,
        }, f, ensure_ascii=False, indent=2)
    print(f"\nSaved: {out}")

if __name__ == "__main__":
    main()
