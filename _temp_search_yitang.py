# -*- coding: utf-8 -*-
import os
import re
import glob

source_dir = "C:/Users/Administrator/Desktop/wiki/10_raw/sources"
output_path = "C:/Users/Administrator/Desktop/wiki/_temp_search_yitang_out.txt"
source_ids = [
    "6d9f7671", "a25ca678", "64015d4d", "1be3d76f", "faa8021d", "842be4c9",
    "239c9f4e", "b65be94b", "c944bda5", "8f80cb0f", "2e2a1e9c", "a3ae193a",
    "93ffa2b0", "b23e9ae3", "70cde3fb", "610cbfc3", "f2578dfb", "6b2c4f5b",
    "ea308189", "aceef535", "dcf9d023", "4ff08501", "22f103f0", "3501eb39",
    "78622699", "46bc4b82"
]

patterns = {
    "准备系数": "准备系数",
    "5-10倍素材": r"5[\-～]10",
    "14个工具": r"14\s*[个个].{0,5}工具",
    "案例课分类": r"搞砸|最佳实践|落地|开源",
    "知识萃取五级": r"个人清单|技能建模|方法论|团队知识|行业学科",
    "课程地图": r"课程地图|个人地图|管理地图|创业地图|无限进步",
    "Y模型": r"Y模型|客观规律|理论.*事实|12345",
    "TCPR": r"TCPR|T.C.P.R|躬身入局|主题阅读|迭代优化",
    "双三角": r"双三角",
    "龙虾": r"龙虾",
    "千人广场": r"千人广场",
    "AI交互系统": r"Chatbot|Agent|Obsidian|交互系统",
    "数据是给AI的食材": r"数据.*食材|给AI.*食材",
    "AI化必经之路": r"必经之路|AI化|一号位",
    "需求评估三角": r"普遍性|频次|刚性|需求评估",
    "业务公式拆解L5-L6": r"L5|L6|业务公式|GMV",
    "新人五层落地": r"五层|新人.*落地",
    "NPC体系": r"NPC",
}

files = {}
for sid in source_ids:
    matches = glob.glob(os.path.join(source_dir, f"src_20260614_{sid}*.md"))
    if matches:
        files[sid] = matches[0]
    else:
        files[sid] = None

def read_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except Exception as e:
        return []

out_lines = []
for label, pattern in patterns.items():
    out_lines.append(f"\n=== {label} ({pattern}) ===")
    for sid, path in files.items():
        if not path:
            continue
        lines = read_lines(path)
        found = []
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                found.append((i, line.strip()))
        if found:
            out_lines.append(f"  {os.path.basename(path)}:")
            for i, line in found[:15]:
                out_lines.append(f"    L{i}: {line[:160]}")
            if len(found) > 15:
                out_lines.append(f"    ... and {len(found)-15} more")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print(f"Output written to {output_path}")
