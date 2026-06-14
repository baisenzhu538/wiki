# -*- coding: utf-8 -*-
import os

source_dir = "C:/Users/Administrator/Desktop/wiki/10_raw/sources"
output_path = "C:/Users/Administrator/Desktop/wiki/_temp_extract_context_out.txt"

queries = [
    # (filename_contains, start_line, end_line, label)
    ("src_20260614_1be3d76f-一堂-思维模型案例分享.md", 366, 376, "准备系数5-10倍"),
    ("src_20260614_610cbfc3-一堂-新人落地必修课.md", 104, 112, "新人落地14个工具"),
    ("src_20260614_c944bda5-一堂-案例必修课.md", 108, 150, "案例课四类"),
    ("src_20260614_239c9f4e-一堂-知识萃取探索营.md", 540, 600, "知识萃取五级"),
    ("src_20260614_8f80cb0f-一堂-课程地图精华串讲.md", 135, 145, "课程地图三大地图"),
    ("src_20260614_8f80cb0f-一堂-课程地图精华串讲.md", 273, 290, "管理地图创业地图个人地图"),
    ("src_20260614_8f80cb0f-一堂-课程地图精华串讲.md", 360, 370, "无限进步大地图"),
    ("src_20260614_faa8021d-Y模型探索营-第二节课.md", 65, 75, "Y模型12345口诀"),
    ("src_20260614_842be4c9-一堂-Y模型实操探索营.md", 849, 860, "Y模型快速入门无限进步"),
    ("src_20260614_3501eb39-一堂-PCPR模型课程.md", 670, 690, "TCPR躬身入局"),
    ("src_20260614_64015d4d-AI数据第一课闲聊篇.mp4.md", 75, 85, "双三角无限进步基础"),
    ("src_20260614_64015d4d-AI数据第一课闲聊篇.mp4.md", 120, 140, "AI交互系统三级循环"),
    ("src_20260614_64015d4d-AI数据第一课闲聊篇.mp4.md", 250, 295, "龙虾循环"),
    ("src_20260614_239c9f4e-一堂-知识萃取探索营.md", 1095, 1175, "千人广场"),
    ("src_20260614_a25ca678-一堂-AI数据必修课.md", 550, 560, "数据是给AI的食材"),
    ("src_20260614_93ffa2b0-一堂-公司AI转型.md", 35, 55, "AI化必经之路"),
    ("src_20260614_70cde3fb-一堂-需求评估方法论.md", 270, 280, "需求评估三角"),
    ("src_20260614_6d9f7671-业务公式拆解培训.md", 1010, 1035, "业务公式拆解L5-L6"),
    ("src_20260614_610cbfc3-一堂-新人落地必修课.md", 230, 310, "新人落地五层框架"),
    ("src_20260614_f2578dfb-一堂-世总会0到1实践.md", 400, 545, "NPC体系"),
]

out_lines = []
for fname, start, end, label in queries:
    path = os.path.join(source_dir, fname)
    out_lines.append(f"\n=== {label}: {fname} L{start}-{end} ===")
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i in range(start-1, min(end, len(lines))):
            out_lines.append(f"L{i+1}: {lines[i].rstrip()}")
    except Exception as e:
        out_lines.append(f"ERROR: {e}")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print(f"Output written to {output_path}")
