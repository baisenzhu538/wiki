"""Gold Standard comparison — with card-level context hints."""
import json, re, sys
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
sys.path.insert(0, r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")
from kdo.commands.label import load_tag_registry, flatten_dimensions, llm_label_chunk
from kdo.llm import LLMConfig
from kdo.workspace import safe_read

CORE = ["chunk_type", "method_family", "audience", "perspective"]

CARD_HINTS = {
    "master-decision-hygiene.md": "决策卫生（认知思维工具卡，讨论偏差/噪声/判断分解等认知概念）",
    "yt-decision-y-model.md": "Y模型决策框架（决策工具卡，讨论ROI/宽度深度高度/决策矩阵）",
    "master-cognitive-bias-checklist.md": "认知偏误自检清单（评估工具卡，12条逐项自检清单）",
    "ai时代判断力口述-3.md": "AI时代判断力口述（知识工程/IPO模型，面向开发者）",
}

def parse_gold(path):
    text = safe_read(path)
    chunks = []
    sections = re.split(r'\n## Chunk (\d+)', text)
    for i in range(1, len(sections), 2):
        cid = int(sections[i])
        body = sections[i+1] if i+1 < len(sections) else ""
        src_m = re.search(r'\*\*来源卡片\*\*\s*\|\s*`(.+?)`', body)
        src = src_m.group(1) if src_m else "?"
        cm = re.search(r'\*\*chunk 内容\*\*\s*\|\s*(.+?)(?=\n\|\s*\n\||\n\n)', body, re.DOTALL)
        txt = cm.group(1).strip().strip('"').strip("'") if cm else ""
        labels = {}
        table_start = body.find("| 维度 | 标签值 | 理由 |")
        if table_start >= 0:
            table_text = body[table_start:]
            nh = re.search(r'\n##\s', table_text)
            if nh: table_text = table_text[:nh.start()]
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

    tm = 0; tx = 0; t0 = 0; tg = 0
    dm = {d: 0 for d in CORE}; dt = {d: 0 for d in CORE}

    for chunk in chunks:
        card_name = chunk["source"].split("/")[-1]
        hint = CARD_HINTS.get(card_name, card_name)
        print("--- Chunk {} ({} | {}) ---".format(chunk["id"], card_name[:35], hint[:40]))
        if not chunk["text"]: print("  SKIP\n"); continue
        decisions = llm_label_chunk(chunk["text"], core_dims, config=cfg, card_hint=hint)
        auto = {}
        if decisions:
            for d in decisions: auto[d["dimension"]] = d["value"]
        else:
            print("    EMPTY")
        m = 0; gc = 0
        for dim in CORE:
            gv = chunk["gold"].get(dim)
            if not gv: continue
            gc += 1; tg += 1; dt[dim] += 1
            av = auto.get(dim)
            if av and av == str(gv):
                m += 1; tm += 1; dm[dim] += 1
                print("  OK {}: {}".format(dim, gv))
            elif av:
                tx += 1; print("  XX {}: gold={} auto={}".format(dim, gv, av))
            else:
                t0 += 1; print("  -- {}: gold={}".format(dim, gv))
        acc = m/gc if gc else 0
        print("  -> {}/{} ({:.0%})\n".format(m, gc, acc))

    ov = tm/tg if tg else 0
    print("=" * 60)
    print("OVERALL: {}/{} = {:.1%}  (OK:{} XX:{} --:{})".format(tm, tg, ov, tm, tx, t0))
    for dim in CORE:
        if dt[dim]: print("  {}: {}/{} = {:.0%}".format(dim, dm[dim], dt[dim], dm[dim]/dt[dim]))
    print("\nTarget: >= 85%  Result: {}".format("PASS" if ov >= 0.85 else "FAIL"))

if __name__ == "__main__":
    main()
