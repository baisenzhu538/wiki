import sys, re, json
from pathlib import Path
sys.path.insert(0, 'C:/Users/Administrator/Desktop/wiki')

WIKI_DIR = Path('C:/Users/Administrator/Desktop/wiki/30_wiki')
VALID_TYPES = {"concept","skill","case","framework","dark-knowledge","tool","decision","proposal","improvement-plan","entity","analysis","system","requirement","report","index","dk"}
VALID_STATUSES = {"draft","enriched","reviewed","stable","proposed","needs-review","deprecated","superseded","active","redirect","pending","revised"}
VALID_TRUST_LEVELS = {"low","medium-low","medium","medium-high","high"}

def parse_frontmatter(text):
    if not text.startswith("---\n"): return None, text, None
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1: return None, text, None
    fm_text = text[4:end_idx]
    try:
        import yaml
        fm = yaml.safe_load(fm_text)
        if not isinstance(fm, dict): fm = {}
        return fm, text[end_idx+5:], fm_text
    except Exception as e:
        return None, text, str(e)

def count_source_refs(fm):
    refs = fm.get("source_refs")
    if not refs: return 0
    if isinstance(refs, str): return 1 if str(refs).strip() and str(refs).strip() != "None" else 0
    if isinstance(refs, list): return len([r for r in refs if str(r).strip() and str(r).strip() != "None"])
    return 0

def extract_wikilinks(text):
    return re.findall(r"\[\[([^\]]+)\]\]", text)

def check_card(file_path, all_ids):
    text = file_path.read_text(encoding="utf-8")
    result = parse_frontmatter(text)
    issues = {"p0": [], "p1": []}
    fm = None
    if result[0] is None:
        issues["p0"].append(f"YAML解析错误: {result[2]}")
        return issues, fm
    fm, body, _ = result
    card_id = str(fm.get("id","")).strip().strip('"')
    if not card_id: issues["p0"].append("缺少id")
    elif card_id != file_path.stem: issues["p0"].append(f"id不一致")
    title = fm.get("title")
    if not title or str(title).strip() in ("", "None"): issues["p0"].append("缺少title")
    card_type = str(fm.get("type","")).strip().strip('"').lower()
    if not card_type: issues["p0"].append("缺少type")
    elif card_type not in VALID_TYPES: issues["p1"].append(f"type异常:{card_type}")
    status = str(fm.get("status","") or "").strip().strip('"').lower()
    source_count = count_source_refs(fm)
    if source_count == 0:
        if status in ("enriched","reviewed","stable","active"): issues["p0"].append("source_refs为空")
        else: issues["p1"].append("source_refs为空")
    author = str(fm.get("author","") or "").strip().strip('"')
    if not author: issues["p0"].append("author为空")
    reviewed_by = str(fm.get("reviewed_by","") or "").strip().strip('"')
    if reviewed_by == "pending" and status in ("enriched","reviewed","stable"): issues["p0"].append("reviewed_by=pending")
    if status and status not in VALID_STATUSES: issues["p1"].append(f"status异常:{status}")
    confidence_raw = fm.get("confidence")
    confidence = None
    if confidence_raw is None: issues["p0"].append("缺少confidence")
    else:
        try:
            confidence = float(confidence_raw)
            if not (0.0 <= confidence <= 1.0): issues["p0"].append(f"confidence越界")
        except: issues["p0"].append(f"confidence非数字")
    trust_level = str(fm.get("trust_level","") or "").strip().strip('"').lower()
    if not trust_level: issues["p0"].append("缺少trust_level")
    elif trust_level not in VALID_TRUST_LEVELS: issues["p1"].append(f"trust_level异常:{trust_level}")
    domain = fm.get("domain")
    if not domain: issues["p0"].append("缺少domain")
    related = fm.get("related") or []
    if isinstance(related, str): related = [related]
    related_links_raw = [str(r).strip().strip('"') for r in related if r is not None and str(r).strip()]
    body_links_raw = extract_wikilinks(body)
    all_links_raw = set(related_links_raw + body_links_raw)
    dangling = []
    for link in all_links_raw:
        link_id = link.strip()
        while link_id.startswith("[[") and link_id.endswith("]]"): link_id = link_id[2:-2]
        link_id = link_id.strip().strip("'\"").strip()
        link_id = link_id.split("#")[0].strip()
        if link_id and link_id not in all_ids: dangling.append(link_id)
    if dangling: issues["p1"].append(f"dangling:{','.join(dangling[:5])}")
    if confidence is not None:
        if confidence >= 0.90 and source_count < 2: issues["p1"].append(f"confidence高但source少")
        if status == "draft" and confidence >= 0.85: issues["p1"].append("draft但confidence高")
        if trust_level in ("low","medium-low") and confidence >= 0.85: issues["p1"].append("trust低但confidence高")
        if trust_level == "high" and source_count < 2: issues["p1"].append("trust高但source少")
    if status == "reviewed" and (not reviewed_by or reviewed_by == "pending"): issues["p1"].append("reviewed但reviewed_by无效")
    try:
        sid_map = json.loads((Path(WIKI_DIR).parent / ".kdo" / "source_id_map.json").read_text(encoding="utf-8"))
    except Exception: sid_map = {}
    refs = fm.get("source_refs", []) or []
    if isinstance(refs, str): refs = [refs]
    missing_srcs = []
    for r in refs:
        r_str = str(r).strip()
        m = re.match(r'(src_\d+_\w{8})', r_str)
        if m and m.group(1) not in sid_map: missing_srcs.append(m.group(1))
    if missing_srcs: issues["p1"].append(f"src未注册:{','.join(missing_srcs[:3])}")
    if fm.get("contradicts"): issues["p1"].append("contradicts残留")
    if reviewed_by and author and reviewed_by == author and author not in ("黄药师","欧阳锋"): issues["p1"].append("自审")
    return issues, fm

files = list(WIKI_DIR.rglob("*.md"))
all_ids = {f.stem for f in files}
targets = [
'yt-decision-y-model.md',
'yt-decision-full-process.md',
'yt-decision-consensus-iceberg.md',
'yt-decision-ai-partner.md',
'yt-decision-canvas.md']
total_p0 = total_p1 = 0
for f in files:
    if f.name in targets:
        issues, fm = check_card(f, all_ids)
        total_p0 += len(issues['p0'])
        total_p1 += len(issues['p1'])
        print(f.name, 'P0:', len(issues['p0']), 'P1:', len(issues['p1']))
        if issues['p0'] or issues['p1']:
            print('  P0:', issues['p0'])
            print('  P1:', issues['p1'])
print('TARGET TOTAL P0:', total_p0, 'P1:', total_p1)
