"""Gold Standard comparison v5 — clean parsing, proper tracking."""
import json, re, sys
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import load_tag_registry, flatten_dimensions, llm_label_chunk
from kdo.llm import LLMConfig
from kdo.workspace import safe_read

CORE = ["chunk_type", "method_family", "audience", "perspective"]

def parse_gold(path):
    text = safe_read(path)
    chunks = []
    sections = re.split(r'\n## Chunk (\d+)', text)
    for i in range(1, len(sections), 2):
        cid = int(sections[i])
        body = sections[i+1] if i+1 < len(sections) else ""

        # Extract source card
        src_m = re.search(r'\*\*来源卡片\*\*\s*\|\s*`(.+?)`', body)
        src = src_m.group(1) if src_m else "?"

        # Extract chunk content
        cm = re.search(r'\*\*chunk 内容\*\*\s*\|\s*(.+?)(?=\n\|\s*\n\||\n\n\|\s*\|\n)', body, re.DOTALL)
        txt = cm.group(1).strip().strip('"').strip("'") if cm else ""

        # Extract labels
        labels = {}
        table_start = body.find("| 维度 | 标签值 | 理由 |")
        if table_start >= 0:
            table_text = body[table_start:]
            for row in table_text.split("\n")[2:]:
                cells = [c.strip() for c in row.split("|") if c.strip()]
                if len(cells) >= 2 and cells[0] in CORE:
                    labels[cells[0]] = cells[1].strip("`")

        chunks.append({"id": cid, "source": src, "text": txt, "gold": labels})
    return chunks

def main():
    chunks = parse_gold(VAULT / "30_wiki/decisions/gold-standard-manual-labels.md")
    print("Parsed {} chunks\n".format(len(chunks)))

    cfg = LLMConfig.from_yaml()
    print("LLM: {}\n".format(cfg.model))

    all_dims = flatten_dimensions(load_tag_registry(VAULT))
    core_dims = {k: v for k, v in all_dims.items() if k in CORE}

    total_match = 0; total_miss = 0; total_missing = 0; total_gold = 0
    dim_match = {d: 0 for d in CORE}
    dim_total = {d: 0 for d in CORE}

    for chunk in chunks:
        print("--- Chunk {} ({}) ---".format(chunk["id"], chunk["source"].split("/")[-1][:35]))
        if not chunk["text"]:
            print("  SKIP: empty text")
            continue
        print("  text: {}...".format(chunk["text"][:80]))

        decisions = llm_label_chunk(chunk["text"], core_dims, config=cfg)
        auto = {}
        if decisions:
            for d in decisions:
                auto[d["dimension"]] = d["value"]
                print("    {}={}".format(d["dimension"], d["value"]))
        else:
            print("    LLM returned empty")

        matches = 0; gold_count = 0
        for dim in CORE:
            gv = chunk["gold"].get(dim)
            if not gv:
                continue
            gold_count += 1
            total_gold += 1
            dim_total[dim] += 1
            av = auto.get(dim)
            if av and av == str(gv):
                matches += 1
                total_match += 1
                dim_match[dim] += 1
                print("  OK {}: {}".format(dim, gv))
            elif av:
                total_miss += 1
                print("  XX {}: gold={} auto={}".format(dim, gv, av))
            else:
                total_missing += 1
                print("  -- {}: gold={} auto=<missing>".format(dim, gv))

        acc = matches/gold_count if gold_count else 0
        print("  -> {}/{} ({:.0%})\n".format(matches, gold_count, acc))

    overall = total_match/total_gold if total_gold else 0
    print("=" * 60)
    print("OVERALL: {}/{} = {:.1%}".format(total_match, total_gold, overall))
    print("  OK: {}  XX: {}  --: {}".format(total_match, total_miss, total_missing))
    print("\nPer-dimension:")
    for dim in CORE:
        if dim_total[dim]:
            print("  {}: {}/{} = {:.0%}".format(dim, dim_match[dim], dim_total[dim],
                  dim_match[dim]/dim_total[dim]))

if __name__ == "__main__":
    main()
