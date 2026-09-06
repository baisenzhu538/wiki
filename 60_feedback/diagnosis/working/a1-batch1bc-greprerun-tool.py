# -*- coding: utf-8 -*-
"""#662 任务一：28 条漏挖候选 grep 存在性核查统一重跑。
复跑口径：对 30_wiki/ 全量 .md 做固定串搜索（CJK 大小写敏感；纯 ASCII 模式额外做不区分大小写）。
输出：每候选每模式 → 命中文件数 / 总命中数 / 命中文件清单（去 index/噪音）。
"""
import os, json, io, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '30_wiki')
ROOT = os.path.normpath(ROOT)

CANDIDATES = [
    # (候选id, 来源, 批1a台账条目号, 行号锚, 模式列表)
    ("A1-M-07", "建模", "1.3#7", "L3824-3832", ["骄傲感"]),
    ("A1-M-11", "建模", "1.3#11", "L574-654", ["正在睡觉请勿敲门", "脆脆鲨", "表白墙"]),
    ("A1-M-16", "建模", "1.3#16", "L1056-1064", ["传染"]),
    ("A1-M-23", "建模", "1.3#23", "L1582-1658", ["太主流", "特别喜欢这种总结", "约等于放弃思考"]),
    ("A1-M-24", "建模", "1.3#24", "L1676", ["没认怂", "不认怂"]),
    ("A1-M-25", "建模", "1.3#25", "L1680-1708", ["气儿就顺", "人生空间决定人生上限", "人生下限"]),
    ("A1-M-26", "建模", "1.3#26", "L1752-1776", ["徐大勇", "顶天立地"]),
    ("A1-M-44", "建模", "1.3#44", "L2982-2988", ["开开心心", "战略会"]),
    ("A1-M-48", "建模", "1.3#48", "L3260-3278", ["现场说话能力", "逐字稿的本质"]),
    ("A1-M-58", "建模", "1.3#58", "L3804-3806", ["拉单子", "排列组合", "清单体"]),
    ("A1-M-60", "建模", "1.3#60", "L3866-3870", ["体系不行", "没有里程碑", "循序渐进的里程碑"]),
    ("A1-M-62", "建模", "1.3#62", "L3942-3958", ["30到50层", "30-50层", "TCP-R", "TCP"]),
    ("A1-M-65", "建模", "1.3#65", "L4148-4182", ["陪跑顾问", "业务教练"]),
    ("A1-M-66", "建模", "1.3#66", "L4216-4232", ["迁移率", "重做一遍"]),
    ("A1-M-67", "建模", "1.3#67", "L4236-4258", ["龙峰", "AI 探索状态", "AI探索状态"]),
    ("A1-M-68", "建模", "1.3#68", "L4304-4380", ["家里种地", "严肃教育"]),
    ("A1-M-69", "建模", "1.3#69", "L4388-4412", ["瑞典", "常识级别"]),
    ("A1-J-21", "讲香", "2.3#21", "L1194-1224", ["边试边复盘", "196 期", "196期"]),
    ("A1-J-30", "讲香", "2.3#30", "L1590-1616", ["4000家门店", "4000 家门店", "31家连锁", "31 家连锁", "陈先敏", "陈肖青", "范明阳"]),
    ("A1-J-32", "讲香", "2.3#32", "L1644-1692", ["凤凰卫视", "一虎奇谈", "心理的坐标系"]),
    ("A1-J-40", "讲香", "2.3#40", "L1960-1984", ["火箭模型", "火箭头"]),
    ("A1-J-51", "讲香", "2.3#51", "L2656-2662+L2704", ["越强，你越需要知道", "调用什么", "越需要知道自己要什么"]),
    ("S-1", "试金石", "pilot①", "ocr L76", ["人工合并", "过一遍我脑子", "漫长的人工"]),
    ("S-2", "试金石", "pilot②", "ocr L102+L106", ["勉强相信", "幻觉是可控", "4乘4", "4乘4个"]),
    ("S-3", "试金石", "pilot③", "ocr L82", ["龙虾组织", "分了五层", "什么是龙虾"]),
    ("S-4", "试金石", "pilot④", "ocr L84+L86", ["依然健在", "没有删除任何一个", "没删除任何一个"]),
    ("S-5", "试金石", "pilot⑤", "ocr L82", ["技术限制", "辩证统一"]),
    ("S-6", "试金石", "pilot⑥", "ocr L38", ["组织行为学校", "组织行为学", "AI组织行为学", "AI 组织行为学"]),
]

NOISE_SUBSTR = ("index", "noise", "concept-card-index", "card-id")

def build_index():
    files = {}
    for dirpath, _dirs, filenames in os.walk(ROOT):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with io.open(p, "r", encoding="utf-8", errors="replace") as f:
                    files[os.path.relpath(p, ROOT)] = f.read()
            except OSError:
                pass
    return files

def is_latin(pat):
    return all(ord(c) < 128 for c in pat)

def main():
    files = build_index()
    result = {"scope": "30_wiki/**/*.md (%d files)" % len(files), "candidates": []}
    for cid, src, ledger_ref, anchor, pats in CANDIDATES:
        entry = {"id": cid, "source": src, "ledger_ref": ledger_ref, "anchor": anchor, "patterns": []}
        for pat in pats:
            hits = {}
            for rel, text in files.items():
                n = text.count(pat)
                if is_latin(pat):
                    n += text.lower().count(pat.lower()) - text.count(pat) if text.count(pat.lower()) > text.count(pat) else 0
                if n > 0:
                    hits[rel] = n
            clean = {k: v for k, v in hits.items() if not any(s in k for s in NOISE_SUBSTR)}
            entry["patterns"].append({
                "pattern": pat,
                "total_hits": sum(hits.values()),
                "file_count": len(hits),
                "clean_file_count": len(clean),
                "clean_files": clean,
            })
        result["candidates"].append(entry)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rerun_28_greps_result.json")
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    # stdout 摘要
    for entry in result["candidates"]:
        parts = []
        for p in entry["patterns"]:
            parts.append("%s:总%d/净%d文件%s" % (p["pattern"], p["total_hits"], p["clean_file_count"],
                        ("[" + ",".join(sorted(p["clean_files"])[:4]) + "]") if p["clean_files"] else ""))
        print("%s (%s %s %s) => %s" % (entry["id"], entry["source"], entry["ledger_ref"], entry["anchor"], " | ".join(parts)))
    print("JSON ->", out)

if __name__ == "__main__":
    main()
