"""Gold Standard comparison v2 — bypass pre-screen, full-dimension LLM labeling."""
import json, re, sys
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import (
    load_tag_registry, flatten_dimensions, llm_label_chunk, validate_and_route,
)
from kdo.llm import LLMConfig
from kdo.workspace import safe_read

DIMS = ["chunk_type","method_family","audience","perspective","platform",
        "confidence","data_generation","value_tier","prerequisite_knowledge",
        "expiry","usage_depth","source_person","source_context_type"]

# Core dimensions to label (full value list sent to LLM)
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

def build_candidates(dims, core_only=None):
    """Build candidates from selected dimensions; if core_only, use those dims."""
    target = core_only or dims.keys()
    result = []
    for dim_name in target:
        if dim_name in dims:
            for entry in dims[dim_name]:
                result.append({
                    "dimension": dim_name, "value": entry["value"],
                    "includes": entry.get("includes",""),
                    "excludes": entry.get("excludes",""),
                })
    return result

def main():
    chunks = parse_gold(VAULT / "30_wiki/decisions/gold-standard-manual-labels.md")
    print(f"Parsed {len(chunks)} Gold Standard chunks.\n")

    cfg = LLMConfig.from_yaml()
    print(f"LLM: {cfg.model} (configured={cfg.is_configured()})\n")

    registry = load_tag_registry(VAULT)
    all_dims = flatten_dimensions(registry)

    total_match = 0; total_miss = 0; total_missing = 0; total_gold = 0
    all_results = []

    for chunk in chunks:
        print(f"--- Chunk {chunk['id']} ({chunk['source'].split('/')[-1][:35]}) ---")
        print(f"  text: {chunk['text'][:80]}...")

        # Build candidates: core dims all values + domain from card filename
        candidates = build_candidates(all_dims, core_only=CORE_DIMS)
        # Add domain from source
        domain_val = "master" if "master" in chunk["source"] else "yitang"
        candidates.append({"dimension": "domain", "value": domain_val, "includes": "", "excludes": ""})

        print(f"  candidates: {len(candidates)} (chunk_type+method_family+audience+perspective)")

        # LLM labeling
        try:
            decisions = llm_label_chunk(chunk["text"], candidates, config=cfg)
        except Exception as e:
            print(f"  LLM ERROR: {e}")
            decisions = []

        if not decisions:
            print(f"  ⚠ LLM returned empty")
            result = {"labels": [], "routing": "llm_error"}
        else:
            applied = [d for d in decisions if d.get("decision") == "APPLY"]
            print(f"  decisions: {len(decisions)} total, {len(applied)} APPLY")
            for d in applied:
                print(f"    APPLY {d['dimension']}/{d['value']} ({d.get('confidence',0):.2f})")
            result = validate_and_route(decisions)

        # Compare
        auto = {l["dimension"]: str(l["value"]) for l in result.get("labels", [])}
        matches = 0; misses = 0; gold_only = 0
        details = []
        for dim in DIMS:
            gv = chunk["gold"].get(dim)
            if not gv: continue
            total_gold += 1
            av = auto.get(dim)
            if av and av == str(gv):
                matches += 1; total_match += 1
                details.append(f"  ✅ {dim}: {gv}")
            elif av:
                misses += 1; total_miss += 1
                details.append(f"  ❌ {dim}: gold={gv} auto={av}")
            else:
                gold_only += 1; total_missing += 1
                if dim in CORE_DIMS:
                    details.append(f"  ⚠️ {dim}: gold={gv} auto=<missing>")

        acc = matches/(matches+misses+gold_only) if (matches+misses+gold_only) else 0
        print(f"  → {matches}/{matches+misses+gold_only} correct ({acc:.0%}) routing={result.get('routing','?')}")
        for d in details[:8]:
            print(d)
        print()
        all_results.append({**chunk, "comparison": {"matches":matches,"misses":misses,"missing":gold_only,"accuracy":acc,"details":details}})

    overall = total_match/total_gold if total_gold else 0
    print("=" * 60)
    print(f"OVERALL: {total_match}/{total_gold} = {overall:.1%}")
    print(f"  ✅ Match:   {total_match}")
    print(f"  ❌ Miss:    {total_miss}")
    print(f"  ⚠️ Missing:  {total_missing}")
    print(f"  Target:     ≥ 85%")

    # Save
    out_path = VAULT / "60_feedback/data-quality/label-results/gold-standard-comparison.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2, default=str)
    print(f"\nSaved: {out_path}")

if __name__ == "__main__":
    main()
