"""Gold Standard comparison v4 — few-shot Chinese prompt."""
import json, re, sys
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import load_tag_registry, flatten_dimensions, llm_label_chunk, validate_and_route
from kdo.llm import LLMConfig
from kdo.workspace import safe_read

DIMS = ["chunk_type","method_family","audience","perspective","platform",
        "confidence","data_generation","value_tier","prerequisite_knowledge",
        "expiry","usage_depth","source_person","source_context_type"]
CORE = ["chunk_type", "method_family", "audience", "perspective"]

def parse_gold(path):
    text = safe_read(path)
    chunks = []
    for sec in re.split(r'\n(?=## Chunk \d+)', text):
        m = re.match(r'## Chunk (\d+)', sec);
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
                labels[cells[0]] = cells[1].strip("`").strip("'").strip('"')
        chunks.append({"id": cid, "source": src, "text": txt, "gold": labels})
    return chunks

def main():
    chunks = parse_gold(VAULT / "30_wiki/decisions/gold-standard-manual-labels.md")
    print("Parsed {} chunks.\n".format(len(chunks)))

    cfg = LLMConfig.from_yaml()
    print("LLM: {} (configured={})\n".format(cfg.model, cfg.is_configured()))

    all_dims = flatten_dimensions(load_tag_registry(VAULT))
    core_dims = {k: v for k, v in all_dims.items() if k in CORE}

    results = []
    total_match = 0; total_miss = 0; total_missing = 0; total_gold = 0

    for chunk in chunks:
        print("--- Chunk {} ({}) ---".format(chunk["id"], chunk["source"].split("/")[-1][:35]))
        print("  text: {}...".format(chunk["text"][:80]))

        try:
            decisions = llm_label_chunk(chunk["text"], core_dims, config=cfg)
        except Exception as e:
            print("  LLM ERROR: {}".format(e))
            decisions = []

        result = validate_and_route(decisions) if decisions else {"labels": [], "routing": "llm_error"}
        auto = {l["dimension"]: str(l["value"]) for l in result.get("labels", [])}

        matches = 0; misses = 0; gold_only = 0
        for dim in CORE:
            gv = chunk["gold"].get(dim)
            if not gv: continue
            total_gold += 1
            av = auto.get(dim)
            if av and av == str(gv):
                matches += 1; total_match += 1
                print("  OK {}: {}".format(dim, gv))
            elif av:
                misses += 1; total_miss += 1
                print("  XX {}: gold={} auto={}".format(dim, gv, av))
            else:
                gold_only += 1; total_missing += 1
                print("  -- {}: gold={} auto=<missing>".format(dim, gv))

        acc = matches/(matches+misses+gold_only) if (matches+misses+gold_only) else 0
        print("  -> {}/{} ({:.0%})\n".format(matches, matches+misses+gold_only, acc))
        results.append({"id": chunk["id"], "acc": acc, "auto": auto})

    overall = total_match/total_gold if total_gold else 0
    print("=" * 60)
    print("OVERALL: {}/{} = {:.1%}".format(total_match, total_gold, overall))
    print("  OK: {}  XX: {}  --: {}".format(total_match, total_miss, total_missing))

    # Per-dimension breakdown
    dim_match = {d: 0 for d in CORE}
    dim_total = {d: 0 for d in CORE}
    for chunk in chunks:
        for dim in CORE:
            gv = chunk["gold"].get(dim)
            if gv:
                dim_total[dim] += 1
                av = results[-1]["auto"].get(dim) if results else None
                if av and av == str(gv):
                    dim_match[dim] += 1
    print("\nPer-dimension:")
    for dim in CORE:
        print("  {}: {}/{} = {:.0%}".format(dim, dim_match[dim], dim_total[dim],
              dim_match[dim]/dim_total[dim] if dim_total[dim] else 0))

if __name__ == "__main__":
    main()
