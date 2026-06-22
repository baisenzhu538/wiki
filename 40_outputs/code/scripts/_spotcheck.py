import json, re
from pathlib import Path

target = Path(r"C:\Users\Administrator\Desktop\wiki\00_inbox\战略专题\冉鹏PPT截图")
# 老顽童 P0 需要的业务设计 VLM + 几个之前顽固的
check_nums = ["107", "110", "112", "115", "119", "121", "124", "127",  # P0
              "16", "25", "50", "111", "114"]  # 之前顽固/parse error

for f in sorted(target.glob("*_vlm_desc.md")):
    stem = f.stem
    if not any(f"_{n}_" in stem for n in check_nums):
        continue
    content = f.read_text(encoding="utf-8")
    raw = re.search(r'## 原始 JSON\s*\n\s*```json\s*\n(.*?)\n```', content, re.DOTALL)
    if not raw:
        print(f"{stem}: NO RAW JSON")
        continue
    parsed = json.loads(raw.group(1))
    title = parsed.get("title", "N/A")
    cat = parsed.get("category", "N/A")
    conf = parsed.get("confidence", "N/A")
    ke_len = len(parsed.get("key_elements") or [])
    tags_len = len(parsed.get("tags") or [])
    desc_len = len(parsed.get("description", ""))
    has_error = parsed.get("_parse_error", False)
    print(f"{stem}: [{cat}] {title[:60]:60s} conf={conf} ke={ke_len} tags={tags_len} desc={desc_len}c {'PARSE_ERR' if has_error else ''}")
