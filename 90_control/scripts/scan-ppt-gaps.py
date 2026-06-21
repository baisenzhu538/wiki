#!/usr/bin/env python3
"""
PPT 内容覆盖度扫描器 v2
读取 VLM 描述 → 提取方法论概念密度 → 按优先级输出补缺清单

用法：
    python 90_control/scripts/scan-ppt-gaps.py
    python 90_control/scripts/scan-ppt-gaps.py --json
"""

import argparse, json, re, sys
from pathlib import Path
from collections import Counter

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
PPT_DIR = VAULT_ROOT / "00_inbox" / "战略专题" / "冉鹏PPT截图"

METHOD_CONCEPTS = {
    "业务设计": ["业务设计", "Business Design"],
    "客户选择": ["目标客群", "客户选择", "Customer Selection"],
    "价值主张": ["价值主张", "Value Proposition", "差异化价值"],
    "价值获取": ["价值获取", "Value Capture", "盈利模式", "收入来源"],
    "活动范围": ["活动范围", "Scope of Activities", "自建", "外包", "价值链"],
    "战略控制点": ["战略控制点", "Strategic Control", "护城河", "壁垒"],
    "风险管理": ["风险管理", "Risk Management", "风险识别"],
    "SWOT": ["SWOT", "优势", "劣势", "机会", "威胁"],
    "波特五力": ["波特五力", "Porter", "五力", "竞争结构"],
    "蓝海战略": ["蓝海", "ERRC", "价值曲线"],
    "五看三定": ["五看", "三定", "看行业", "看市场"],
    "差距分析": ["差距分析", "Gap Analysis", "业绩差距", "机会差距"],
    "鱼骨图": ["鱼骨图", "Fishbone"],
    "帕雷托": ["帕雷托", "Pareto", "80/20"],
    "三地平线": ["三地平线", "Three Horizons"],
    "BCG矩阵": ["BCG", "波士顿"],
    "麦肯锡7S": ["7S", "麦肯锡"],
    "PESTLE": ["PESTLE", "宏观环境"],
    "战略执行": ["战略执行", "关键任务", "实施路线"],
    "变革管理": ["变革管理", "转型", "Change Management"],
    "组织能力": ["组织能力", "核心能力", "能力评估"],
    "竞争优势": ["竞争优势", "Competitive Advantage"],
    "竞对分析": ["竞对分析", "Competitor Analysis"],
    "商业模式": ["商业模式", "Business Model"],
    "平台战略": ["平台", "Platform", "双边"],
    "生态系统": ["生态系统", "Ecosystem"],
    "创新战略": ["创新", "Innovation", "颠覆"],
    "数字化转型": ["数字化", "Digital", "AI", "人工智能"],
    "用户画像": ["用户画像", "Persona"],
    "战略共识": ["战略共识", "共识", "Alignment"],
    "战略复盘": ["战略复盘", "复盘", "Review"],
    # 🆕 自攻击补全（Attacker B 发现词典覆盖不足）
    "战略定价": ["定价策略", "定价", "Price", "价格"],
    "渠道策略": ["渠道", "Channel", "分销", "经销商"],
    "组织设计": ["组织设计", "组织结构", "组织架构", "Org Design"],
    "人才管理": ["人才", "Talent", "招聘", "培养", "梯队"],
    "KPI体系": ["KPI", "指标", "绩效", "考核"],
    "企业文化": ["文化", "Culture", "价值观"],
    "并购整合": ["并购", "M&A", "收购", "整合"],
    "国际化": ["国际化", "出海", "海外", "Global"],
    "财务战略": ["财务", "Finance", "现金流", "资本"],
    "品牌战略": ["品牌", "Brand", "定位"],
    "技术战略": ["技术", "Technology", "R&D", "研发"],
    "供应链": ["供应链", "Supply Chain", "采购", "物流"],
}


def scan():
    slides = {}
    concepts = Counter()
    for fp in sorted(PPT_DIR.glob("*_vlm_desc.md")):
        sid = fp.stem.replace("_vlm_desc", "")
        vlm = fp.read_text(encoding="utf-8")
        found = Counter()
        for concept, keywords in METHOD_CONCEPTS.items():
            for kw in keywords:
                if kw.lower() in vlm.lower():
                    found[concept] += 1; break
        if found:
            title = ""
            m = re.search(r"标题[：:]\s*(.+?)(?:\n|$)", vlm)
            if m and m.group(1).strip() not in ("", "未识别"): title = m.group(1).strip()
            conf = 0
            m = re.search(r"置信度[：:]\s*([\d.]+)", vlm); conf = float(m.group(1)) if m else 0
            slides[sid] = {"concepts": dict(found), "title": title, "conf": conf}
            concepts.update(found)
    return slides, concepts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    slides, concepts = scan()
    ranked = sorted(slides.items(), key=lambda x: len(x[1]["concepts"]), reverse=True)

    if args.json:
        print(json.dumps({"total": len(slides), "concepts": len(concepts),
                          "top_slides": [{"id": s, "title": i["title"], "concepts": len(i["concepts"])}
                                         for s, i in ranked[:20]]}, ensure_ascii=False, indent=2))
        return

    print("# PPT 内容覆盖度扫描 v2")
    print(f"**幻灯片**: {len(slides)} 张含方法论内容")
    print(f"**识别概念**: {len(concepts)} 个")
    print()
    print("## 补缺优先级——概念密度排序")
    print("| # | 幻灯片 | 标题 | 概念数 | 含概念 |")
    print("|---|---|---|---|---|")
    for i, (sid, info) in enumerate(ranked[:40], 1):
        if len(info["concepts"]) < 3: break
        title = info["title"][:40] if info["title"] else "-"
        cs = ", ".join(info["concepts"].keys())[:80]
        print(f"| {i} | `{sid}` | {title} | {len(info['concepts'])} | {cs} |")

    print()
    print("## 概念频次分布")
    for c, n in concepts.most_common(15):
        bar = "█" * (n // 5)
        print(f"| {c} | {n} | {bar} |")

    print()
    print("> 用法：王语嫣标记完成后，老顽童按此优先级逐张提取。每张高密度幻灯片 ≈ 1 张 tool 卡。")

if __name__ == "__main__":
    main()
