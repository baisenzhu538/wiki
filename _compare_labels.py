"""Compare auto_label_chunk() against Gold Standard — with debug output."""
import json, re, sys
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import (
    auto_label_chunk, load_tag_registry, flatten_dimensions,
    prescreen_chunk, llm_label_chunk, validate_and_route,
)
from kdo.llm import LLMConfig, chat
from kdo.workspace import safe_read

DIMS = ["chunk_type","method_family","audience","perspective","platform",
        "confidence","data_generation","value_tier","prerequisite_knowledge",
        "expiry","usage_depth","source_person","source_context_type"]

def parse_gold(path):
    text = safe_read(path)
    chunks = []
    for sec in re.split(r'\n(?=## Chunk \d+)', text):
        m = re.match(r'## Chunk (\d+)', sec)
        if not m: continue
        cid = int(m.group(1))
        src = re.search(r'\*\*来源卡片\*\*\s*\|\s*`(.+?)`', sec)
        src = src.group(1) if src else "?"
        cm = re.search(r'\*\*chunk 内容\*\*\s*\|\s*(.+?)(?=\n\|\s*\n\|)', sec, re.DOTALL)
        txt = cm.group(1).strip().strip('"').strip("'") if cm else ""
        labels = {}
        for row in sec.split("\n"):
            cells = [c.strip() for c in row.split("|") if c.strip()]
            if len(cells) >= 2 and cells[0] in DIMS:
                labels[cells[0]] = cells[1]
        chunks.append({"id": cid, "source": src, "text": txt, "gold": labels})
    return chunks

def main():
    chunks = parse_gold(VAULT / "30_wiki/decisions/gold-standard-manual-labels.md")
    print(f"Parsed {len(chunks)} Gold Standard chunks.\n")

    cfg = LLMConfig.from_yaml()
    print(f"LLM: {cfg.model} @ {cfg.endpoint} (configured={cfg.is_configured()})\n")

    registry = load_tag_registry(VAULT)
    dims = flatten_dimensions(registry)

    total_match = 0; total_miss = 0; total_extra = 0; total_gold = 0

    for chunk in chunks:
        print(f"--- Chunk {chunk['id']} ({chunk['source'].split('/')[-1][:35]}) ---")
        print(f"  text: {chunk['text'][:70]}...")

        # Stage 1: Pre-screen
        candidates = prescreen_chunk(chunk["text"], dims, top_k=8)
        print(f"  pre-screen: {len(candidates)} candidates")

        # Stage 2: LLM
        if candidates:
            try:
                decisions = llm_label_chunk(chunk["text"], candidates, config=cfg)
                if not decisions:
                    print(f"  LLM: returned empty — using pre-screen fallback")
                    # Fallback: use high-scoring pre-screen candidates
                    result = validate_and_route([
                        {"dimension": c["dimension"], "value": c["value"],
                         "decision": "APPLY" if c["score"] > 0.2 else "REJECT",
                         "confidence": c["score"]}
                        for c in candidates
                    ])
                else:
                    print(f"  LLM: {len(decisions)} decisions")
                    for d in decisions[:3]:
                        print(f"    {d.get('decision','?')} {d['dimension']}/{d['value']} ({d.get('confidence','?')})")
                    result = validate_and_route(decisions)
            except Exception as e:
                print(f"  LLM ERROR: {e}")
                result = {"labels": [], "routing": "error", "summary": str(e)}
        else:
            result = {"labels": [], "routing": "no_candidates"}

        # Compare
        auto = {l["dimension"]: str(l["value"]) for l in result.get("labels", [])}
        matches = 0; misses = 0; gold_only = 0
        for dim in DIMS:
            gv = chunk["gold"].get(dim)
            if not gv: continue
            total_gold += 1
            av = auto.get(dim)
            if av and av == str(gv):
                matches += 1
                total_match += 1
                print(f"  ✅ {dim}: {gv}")
            elif av:
                misses += 1
                total_miss += 1
                print(f"  ❌ {dim}: gold={gv} auto={av}")
            else:
                gold_only += 1
                total_extra += 1
                if dim not in ("source_person","source_context_type"):
                    print(f"  ⚠️ {dim}: gold={gv} auto=<missing>")

        acc = matches/(matches+misses+gold_only) if (matches+misses+gold_only) else 0
        print(f"  → {matches}/{matches+misses+gold_only} correct ({acc:.0%}) routing={result.get('routing','?')}\n")

    overall = total_match/total_gold if total_gold else 0
    print("=" * 60)
    print(f"OVERALL: {total_match}/{total_gold} = {overall:.1%}")
    print(f"  ✅ Match:  {total_match}")
    print(f"  ❌ Miss:   {total_miss}")
    print(f"  ⚠️ Missing: {total_extra}")
    print(f"  Target:    ≥ 85%")

if __name__ == "__main__":
    main()
