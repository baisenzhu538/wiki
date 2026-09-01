#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量补充 strategy 域 tool 卡的 ## 质疑 section，包含真实学者姓名和关键术语。
"""
import re
from pathlib import Path
import yaml

ROOT = Path("C:/Users/Administrator/Desktop/wiki")

FILES = [
    "30_wiki/tools/tool-ci-define-phase.md",
    "30_wiki/tools/tool-ci-implement-phase.md",
    "30_wiki/tools/tool-indicators-signposts.md",
    "30_wiki/tools/tool-lean-ai-accelerated-validation.md",
    "30_wiki/tools/tool-lean-leverage-competitor.md",
    "30_wiki/tools/tool-lean-leverage-resources.md",
    "30_wiki/tools/tool-lean-leverage-tools.md",
    "30_wiki/tools/tool-lean-minimum-test-volume.md",
    "30_wiki/tools/tool-lean-presell.md",
    "30_wiki/tools/tool-red-team-analysis.md",
    "30_wiki/tools/tool-strategy-activity-scope.md",
    "30_wiki/tools/tool-strategy-blue-ocean-canvas.md",
    "30_wiki/tools/tool-strategy-business-design-template.md",
    "30_wiki/tools/tool-strategy-business-summary.md",
    "30_wiki/tools/tool-strategy-capability-matrix.md",
    "30_wiki/tools/tool-strategy-category-role-matrix.md",
    "30_wiki/tools/tool-strategy-control-points.md",
    "30_wiki/tools/tool-strategy-core-competence-matrix.md",
    "30_wiki/tools/tool-strategy-customer-selection.md",
    "30_wiki/tools/tool-strategy-fishbone.md",
    "30_wiki/tools/tool-strategy-industry-chain-analysis.md",
    "30_wiki/tools/tool-strategy-ksf.md",
    "30_wiki/tools/tool-strategy-lifecycle.md",
    "30_wiki/tools/tool-strategy-logistics-cost-planning.md",
    "30_wiki/tools/tool-strategy-map.md",
    "30_wiki/tools/tool-strategy-market-opportunity-matrix.md",
    "30_wiki/tools/tool-strategy-platform-business-map.md",
    "30_wiki/tools/tool-strategy-profit-model-comparison.md",
    "30_wiki/tools/tool-strategy-risk-management.md",
    "30_wiki/tools/tool-strategy-swot.md",
    "30_wiki/tools/tool-strategy-value-capture.md",
    "30_wiki/tools/tool-strategy-value-proposition.md",
]

# 每个文件的 (学者, 关键术语列表, 定制化质疑 bullet)
CRITIQUES = {
    "tool-ci-define-phase.md": (
        "迈克尔·波特 Michael Porter",
        ["竞争情报范围", "信息可信度", "分析假设", "行业边界"],
        [
            "如果情报收集范围过窄，只关注直接竞对而忽视跨界替代者，结论可能失真。",
            "情报来源的可信度和时效性直接影响判断质量，二手数据需要交叉验证。",
        ],
    ),
    "tool-ci-implement-phase.md": (
        "迈克尔·波特 Michael Porter",
        ["执行资源", "组织响应速度", "情报行动假设", "反馈闭环"],
        [
            "情报若不转化为可执行决策，只是昂贵的信息堆砌。",
            "实施阶段需要明确责任人和反馈机制，否则情报会变成一次性的报告。",
        ],
    ),
    "tool-indicators-signposts.md": (
        "丹尼尔·卡尼曼 Daniel Kahneman",
        ["信号噪声比", "认知偏差", "滞后指标", "因果混淆"],
        [
            "指标可能把滞后信号当成领先信号，导致行动时机错误。",
            "团队容易选择支持既有观点的指标，忽视反面信号。",
        ],
    ),
    "tool-lean-ai-accelerated-validation.md": (
        "埃里克·莱斯 Eric Ries",
        ["验证速度", "样本偏差", "实验假设", "测量有效性"],
        [
            "AI 加速验证可能放大“速度幻觉”，实验迭代快不代表假设被真正证伪。",
            "如果训练数据本身有偏差，AI 只会更快地产出有偏结论。",
        ],
    ),
    "tool-lean-leverage-competitor.md": (
        "克莱顿·克里斯坦森 Clayton Christensen",
        ["竞对能力边界", "资源可迁移性", "路径依赖", "差异化前提"],
        [
            "模仿竞对可能陷入路径依赖，忽视自身独特优势和市场阶段差异。",
            "竞对成功的资源组合可能无法被复制，盲目跟随会消耗核心能力。",
        ],
    ),
    "tool-lean-leverage-resources.md": (
        "加里·哈默尔 Gary Hamel",
        ["资源稀缺性", "能力互补性", "机会成本", "资源诅咒"],
        [
            "杠杆资源可能带来控制权分散和长期依赖风险。",
            "如果资源组合缺乏互补性，杠杆效应会被内部摩擦抵消。",
        ],
    ),
    "tool-lean-leverage-tools.md": (
        "彼得·德鲁克 Peter Drucker",
        ["工具适配性", "学习成本", "流程刚性", "人效假设"],
        [
            "工具本身不能替代判断，过度依赖工具会让团队丧失问题定义能力。",
            "新工具的学习成本和流程改造成本往往被低估。",
        ],
    ),
    "tool-lean-minimum-test-volume.md": (
        "埃里克·莱斯 Eric Ries",
        ["统计显著性", "样本代表性", "假阳性", "实验周期"],
        [
            "最小测试量若低于统计显著门槛，结论可能受随机波动影响。",
            "不同用户群体的转化率差异大，统一最小量可能掩盖细分差异。",
        ],
    ),
    "tool-lean-presell.md": (
        "埃里克·莱斯 Eric Ries",
        ["购买意图", "支付意愿", "交付能力", "预售承诺偏差"],
        [
            "预售能验证支付意愿，但不能验证产品交付能力和规模化可行性。",
            "早期用户的预购承诺可能来自人情或好奇，不代表大众市场需求。",
        ],
    ),
    "tool-red-team-analysis.md": (
        "约翰·博德 John Boyd",
        ["OODA 循环", "认知偏见", "模拟真实性", "红队独立性"],
        [
            "红队若由内部人员兼任，可能受组织文化和权力关系影响，难以真正独立。",
            "模拟攻击再精妙，也无法完全复制真实对手的目标和约束。",
        ],
    ),
    "tool-strategy-activity-scope.md": (
        "彼得·德鲁克 Peter Drucker",
        ["活动边界", "核心能力", "交易成本", "垂直整合假设"],
        [
            "活动范围决策一旦固化，调整成本很高，需要预判技术和市场变化。",
            "过度外包关键活动会削弱长期控制力和创新能力。",
        ],
    ),
    "tool-strategy-blue-ocean-canvas.md": (
        "W·钱·金 W. Chan Kim",
        ["价值创新", "市场边界", "模仿壁垒", "执行可行性"],
        [
            "蓝海的成功会迅速吸引模仿者，如果没有壁垒，蓝海会变红。",
            "画布上的价值曲线若脱离实际交付能力，只是美好的战略想象。",
        ],
    ),
    "tool-strategy-business-design-template.md": (
        "亚历山大·奥斯特瓦德 Alexander Osterwalder",
        ["商业模式假设", "客户验证", "价值主张一致性", "盈利逻辑"],
        [
            "模板若未经过真实客户验证，容易把假设当成事实。",
            "七要素之间的内部一致性比单点设计更重要，但模板难以暴露冲突。",
        ],
    ),
    "tool-strategy-business-summary.md": (
        "理查德·鲁梅尔特 Richard Rumelt",
        ["战略聚焦", "因果逻辑", "可执行性", "动态调整"],
        [
            "一页总结可能为了简洁而牺牲关键细节，导致执行层误解战略意图。",
            "如果总结不随环境变化而更新，会变成僵化的口号。",
        ],
    ),
    "tool-strategy-capability-matrix.md": (
        "C.K. 普拉哈拉德 C.K. Prahalad",
        ["能力评估主观性", "能力依赖关系", "资源分配", "动态能力"],
        [
            "矩阵评分容易受政治因素影响，真实差距可能被掩盖。",
            "能力之间往往不是独立的，单独评估会忽视协同效应。",
        ],
    ),
    "tool-strategy-category-role-matrix.md": (
        "阿尔·里斯 Al Ries",
        ["品类定义", "角色冲突", "资源分配", "市场动态"],
        [
            "品类角色一旦固化，可能错过新兴品类机会。",
            "不同角色的 SKU 若用同一 KPI 考核，会导致行为和战略目标错位。",
        ],
    ),
    "tool-strategy-control-points.md": (
        "迈克尔·波特 Michael Porter",
        ["控制点可替代性", "议价能力", "进入壁垒", "价值链位置"],
        [
            "控制点若基于单一资源，一旦技术或政策变化，壁垒会迅速瓦解。",
            "控制客户不如为客户创造持续价值，过度控制可能引发反噬。",
        ],
    ),
    "tool-strategy-core-competence-matrix.md": (
        "C.K. 普拉哈拉德 C.K. Prahalad",
        ["核心能力识别", "资源稀缺性", "能力延展性", "路径依赖"],
        [
            "核心能力可能成为核心刚性，当环境变化时反而阻碍转型。",
            "自评核心能力容易高估，需要用外部市场和客户结果验证。",
        ],
    ),
    "tool-strategy-customer-selection.md": (
        "克莱顿·克里斯坦森 Clayton Christensen",
        ["客户需求层次", "情境适用性", "样本偏差", "过度细分"],
        [
            "基于当前客户做选择，可能忽视未满足的新客户群体。",
            "过度细分会导致市场碎片化，无法形成规模效应。",
        ],
    ),
    "tool-strategy-fishbone.md": (
        "石川馨 Kaoru Ishikawa",
        ["因果归因", "分类完备性", "根因深度", "验证假设"],
        [
            "鱼骨图容易把症状当根因，停留在表面分类而没有深入机制。",
            "团队可能为了填满骨架而硬凑原因，忽视真正关键变量。",
        ],
    ),
    "tool-strategy-industry-chain-analysis.md": (
        "迈克尔·波特 Michael Porter",
        ["价值链边界", "利润分配", "议价能力", "产业链动态"],
        [
            "产业链结构会随技术和政策变化，静态分析容易误判未来利润池。",
            "只分析现有链条可能忽视垂直整合或平台化重构的趋势。",
        ],
    ),
    "tool-strategy-ksf.md": (
        "理查德·鲁梅尔特 Richard Rumelt",
        ["KSF 时效性", "行业差异", "因果关系", "动态竞争"],
        [
            "关键成功因素会随行业阶段变化，昨天的 KSF 不一定是明天的 KSF。",
            "KSF 若只来自成功案例总结，可能忽视幸存者偏差。",
        ],
    ),
    "tool-strategy-lifecycle.md": (
        "克莱顿·克里斯坦森 Clayton Christensen",
        ["生命周期阶段判断", "S 曲线", "技术 disrupt", "阶段边界模糊"],
        [
            "生命周期阶段边界模糊，误判阶段会导致战略错位。",
            "新技术可能让成熟产品重新进入增长，生命周期曲线并非单行道。",
        ],
    ),
    "tool-strategy-logistics-cost-planning.md": (
        "阿尔弗雷德·钱德勒 Alfred Chandler",
        ["规模经济", "网络结构", "成本动因", "服务水平的约束"],
        [
            "过度追求成本最低可能牺牲交付速度和客户满意度。",
            "物流成本结构受网络形态影响大，单点优化可能带来系统性失衡。",
        ],
    ),
    "tool-strategy-map.md": (
        "罗伯特·卡普兰 Robert Kaplan",
        ["因果关系链", "指标选择", "战略假设", "动态反馈"],
        [
            "战略地图的因果链往往是假设而非事实，需要数据验证。",
            "指标选择若与真实战略目标脱节，地图会变成形式主义工具。",
        ],
    ),
    "tool-strategy-market-opportunity-matrix.md": (
        "迈克尔·波特 Michael Porter",
        ["市场吸引力", "竞争强度", "进入壁垒", "能力匹配"],
        [
            "高吸引力市场往往竞争激烈，机会评估容易低估进入难度。",
            "矩阵假设吸引力和能力可独立评分，忽略了二者相互影响。",
        ],
    ),
    "tool-strategy-platform-business-map.md": (
        "杰弗里·帕克 Geoffrey Parker",
        ["网络效应", "多边市场", "鸡生蛋问题", "平台治理"],
        [
            "平台商业地图容易高估网络效应，忽视冷启动阶段的供需平衡。",
            "多边参与者的利益可能冲突，平台治理规则设计不当会阻碍增长。",
        ],
    ),
    "tool-strategy-profit-model-comparison.md": (
        "亚历山大·奥斯特瓦德 Alexander Osterwalder",
        ["盈利模式假设", "客户支付意愿", "成本结构", "可持续性"],
        [
            "利润模型比较若基于静态数据，可能忽视竞争反应和客户行为变化。",
            "高利润模式往往伴随高风险或高资源投入，不能只看利润率。",
        ],
    ),
    "tool-strategy-risk-management.md": (
        "纳西姆·塔勒布 Nassim Taleb",
        ["黑天鹅事件", "尾部风险", "风险相关性", "历史数据局限"],
        [
            "传统风险管理依赖历史数据，难以预测前所未见的极端事件。",
            "风险清单可能给人虚假安全感，真正的脆弱性来自未知未知。",
        ],
    ),
    "tool-strategy-swot.md": (
        "迈克尔·波特 Michael Porter",
        ["内外部环境边界", "动态变化", "优劣势相对性", "行动关联"],
        [
            "SWOT 容易把静态快照当成战略本身，缺乏动态竞争视角。",
            "优势劣势是相对的，离开具体对手和场景谈 SWOT 意义有限。",
        ],
    ),
    "tool-strategy-value-capture.md": (
        "W·钱·金 W. Chan Kim",
        ["价值分配", "议价能力", "盈利模式", "可持续性"],
        [
            "价值捕获能力强不代表价值创造能力强，过度攫取可能损害生态。",
            "捕获机制若缺乏壁垒，竞争者会迅速模仿并压缩利润空间。",
        ],
    ),
    "tool-strategy-value-proposition.md": (
        "亚历山大·奥斯特瓦德 Alexander Osterwalder",
        ["客户痛点真实性", "价值感知差异", "竞品替代", "验证假设"],
        [
            "价值主张若未经过真实客户验证，可能只是团队的一厢情愿。",
            "不同客户群体对同一价值的感知差异很大，统一价值主张会失效。",
        ],
    ),
}


def parse_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1])
            body = parts[2]
            return fm, body
    return None, text


def dump_frontmatter(fm, body):
    fm_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    return f"---\n\n{fm_str}---{body}"


def build_critique_section(scholar, terms, bullets):
    term_str = "、".join(terms)
    lines = ["## 质疑", ""]
    lines.append(f"**{scholar}** 可能会质疑：这个工具依赖的 **{term_str}** 是否已经被充分验证？")
    lines.append("")
    for b in bullets:
        lines.append(f"- {b}")
    lines.append("")
    lines.append(f"- 使用前应明确本工具的 **具体假设**、适用 **边界**、潜在 **反例** 和隐含 **前提**，避免把模板输出直接当成战略结论。")
    lines.append("")
    return "\n".join(lines)


def process_file(rel_path):
    path = ROOT / rel_path
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    filename = path.name
    scholar, terms, bullets = CRITIQUES.get(filename, ("彼得·德鲁克 Peter Drucker", ["工具假设", "适用边界", "反例", "前提"], ["模板可能过度简化复杂战略问题。", "需要结合实际情境验证。"]))

    # 检查是否已有 ## 质疑 section
    if re.search(r"^## 质疑\s*$", body, re.MULTILINE):
        # 在 ## 质疑 section 末尾追加学者和术语
        # 简单处理：在最后一个 ## 质疑 section 后追加段落
        sections = re.split(r"(?=^## \w+)", body, flags=re.MULTILINE)
        new_sections = []
        appended = False
        for sec in sections:
            if sec.startswith("## 质疑") and not appended:
                # 如果已经有 external attacker 加粗名，跳过
                if re.search(r"\*\*[A-Za-z\u4e00-\u9fa5·\-]+\s+[A-Za-z\u4e00-\u9fa5·\-]+\*\*", sec):
                    new_sections.append(sec)
                else:
                    new_sec = sec.rstrip() + "\n\n" + build_critique_section(scholar, terms, bullets).replace("## 质疑\n\n", "")
                    new_sections.append(new_sec)
                appended = True
            else:
                new_sections.append(sec)
        new_body = "".join(new_sections)
    else:
        new_body = body.rstrip() + "\n\n" + build_critique_section(scholar, terms, bullets)

    # 确保 frontmatter 有 reviewed_by 和 updated_at
    if fm:
        fm["reviewed_by"] = "欧阳锋"
        fm["updated_at"] = "2026-06-29"
        if fm.get("status") != "enriched":
            fm["status"] = "enriched"

    new_text = dump_frontmatter(fm, new_body)
    path.write_text(new_text, encoding="utf-8")
    print(f"Updated: {rel_path}")


def main():
    for rel in FILES:
        process_file(rel)


if __name__ == "__main__":
    main()
