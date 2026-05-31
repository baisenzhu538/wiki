"""Gold Standard comparison v3 — single-pass per-dimension LLM classification."""
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

CORE_DIMS = ["chunk_type", "method_family", "audience", "perspective"]

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
    print("Parsed {} Gold Standard chunks.\n".format(len(chunks)))

    cfg = LLMConfig.from_yaml()
    print("LLM: {} (configured={})\n".format(cfg.model, cfg.is_configured()))

    registry = load_tag_registry(VAULT)
    all_dims = flatten_dimensions(registry)
    core_dims = {k: v for k, v in all_dims.items() if k in CORE_DIMS}

    total_match = 0; total_miss = 0; total_missing = 0; total_gold = 0

    for chunk in chunks:
        print("--- Chunk {} ({}) ---".format(chunk["id"], chunk["source"].split("/")[-1][:35]))
        print("  text: {}...".format(chunk["text"][:70]))

        try:
            decisions = llm_label_chunk(chunk["text"], core_dims, config=cfg)
        except Exception as e:
            print("  LLM ERROR: {}".format(e))
            decisions = []

        if not decisions:
            print("  LLM returned empty")
            result = {"labels": [], "routing": "llm_error"}
        else:
            result = validate_and_route(decisions)
            print("  decisions: {} total".format(len(decisions)))
            for d in decisions:
                print("    {}={} (conf={:.2f})".format(d["dimension"], d.get("value","?"), d.get("confidence",0)))

        auto = {l["dimension"]: str(l["value"]) for l in result.get("labels", [])}
        matches = 0; misses = 0; gold_only = 0
        for dim in CORE_DIMS:
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
        print("  -> {}/{} correct ({:.0%})\n".format(matches, matches+misses+gold_only, acc))

    overall = total_match/total_gold if total_gold else 0
    print("=" * 60)
    print("OVERALL: {}/{} = {:.1%}".format(total_match, total_gold, overall))
    print("  OK Match:  {}".format(total_match))
    print("  XX Miss:   {}".format(total_miss))
    print("  -- Missing: {}".format(total_missing))
    print("  Target:    >= 85%")

if __name__ == "__main__":
    main()
