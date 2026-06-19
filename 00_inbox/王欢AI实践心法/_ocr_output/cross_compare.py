#!/usr/bin/env python3
"""
六层交叉比对脚本：
1. 口述稿、2. 笔记、3. 逐字稿、4. 图片 OCR、5. 当前业务场景、6. 现有 wiki 域
输出：交叉比对报告 markdown
"""
import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path("00_inbox/王欢AI实践心法")
OUTPUT_DIR = BASE_DIR / "_ocr_output"

# 定义关键词/框架库
FRAMEWORKS = [
    "演员", "导演", "演员思维", "导演思维",
    "五层", "五层金字塔", "五层跃迁", "问答层", "工作流层", "作品层", "产品层", "应用层", "系统层",
    "BITCOE", "BTICOE", "BTICME", "背景", "任务", "指令", "约束", "输出", "示例", "方法",
    "三层架构", "贾维斯", "MM", "哨兵", "需求拆解", "代码执行", "审查验收",
    "OODA", "观察", "定向", "决策", "行动",
    "对抗式生成", "生成器", "判别器", "评审者",
    "PACED", "痛点", "消费能力", "决策链", "期望", "决策时机", "Authority", "Capacity", "Expectation", "Decision",
    "双角色", "对练", "客户", "教练",
    "GAN", "生成器", "判别器", "合成器",
    "飞轮", "第一圈", "最小闭环",
    "harness", "驾驭",
    "AI业务档案", "关于我", "我服务谁", "风格偏好", "行业暗规则", "输出标准",
    "AI native",
    "选场景", "海报工具", "医语轻记",
    "标准的力量",
    "导演的工作方式",
    "说想做", "豆包", "TREE", "Cursor",
    "沈阳", "软件公司", "闫总", "教育机构", "销售",
]

CASES = [
    "沈阳软件公司", "软件外包公司", "闫总", "九百多个政企客户",
    "教育机构", "销售能力萃取", "PECED", "PACED", "双角色对练",
    "海报工具", "医语轻记",
]


def read_text(path: Path) -> str:
    """读取文本文件，尝试多种编码。"""
    for enc in ["utf-8", "gbk", "gb2312", "utf-16"]:
        try:
            return path.read_text(encoding=enc)
        except Exception:
            continue
    return ""


def count_keywords(text: str, keywords: list) -> dict:
    """统计关键词在文本中出现次数。"""
    result = {}
    for kw in keywords:
        # 不区分大小写
        count = len(re.findall(re.escape(kw), text, re.IGNORECASE))
        if count > 0:
            result[kw] = count
    return result


def extract_context(text: str, keyword: str, window: int = 60) -> list:
    """提取关键词上下文片段。"""
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    fragments = []
    for m in pattern.finditer(text):
        start = max(0, m.start() - window)
        end = min(len(text), m.end() + window)
        fragments.append(text[start:end].replace("\n", " "))
    return fragments


def main():
    sources = {
        "口述稿": BASE_DIR / "王欢-AI实战分享-从演员到导演-口述.txt",
        "笔记": BASE_DIR / "王欢-AI实战分享-从演员到导演-笔记.txt",
        "逐字稿": BASE_DIR / "王欢-AI实战分享-从任务到产品再到系统-逐字稿.md",
        "图片OCR": OUTPUT_DIR / "all_ocr_raw.md",
    }

    texts = {name: read_text(path) for name, path in sources.items()}

    # 1. 关键词覆盖度矩阵
    framework_matrix = defaultdict(dict)
    for name, text in texts.items():
        counts = count_keywords(text, FRAMEWORKS)
        for kw, count in counts.items():
            framework_matrix[kw][name] = count

    # 2. 案例覆盖度矩阵
    case_matrix = defaultdict(dict)
    for name, text in texts.items():
        counts = count_keywords(text, CASES)
        for kw, count in counts.items():
            case_matrix[kw][name] = count

    # 3. 不一致/缺失检测
    inconsistencies = []
    for kw, counts in framework_matrix.items():
        # 如果只在某一层出现，其他层缺失
        if len(counts) == 1:
            inconsistencies.append({
                "type": "仅单层出现",
                "keyword": kw,
                "source": list(counts.keys())[0],
                "count": list(counts.values())[0],
            })
        # 如果只在口述稿和笔记出现，逐字稿和 OCR 没出现
        elif set(counts.keys()) <= {"口述稿", "笔记"}:
            inconsistencies.append({
                "type": "文本稿有但正式稿无",
                "keyword": kw,
                "source": counts,
            })

    # 4. 生成报告
    report = ["# 王欢 AI 实战分享 — 六层交叉比对报告\n"]
    report.append(f"> 比对时间：2026-06-19  ")
    report.append(f"> 比对人：王语嫣  ")
    report.append(f"> 比对对象：口述稿、笔记、逐字稿、图片 OCR\n")

    # 4.1 数据源统计
    report.append("## 一、数据源统计\n")
    for name, text in texts.items():
        report.append(f"- **{name}**：{len(text)} 字符")
    report.append("\n")

    # 4.2 框架/模型覆盖度
    report.append("## 二、框架/模型覆盖度矩阵\n")
    report.append("| 框架/关键词 | 口述稿 | 笔记 | 逐字稿 | 图片OCR | 一致性 |")
    report.append("|:---|:---:|:---:|:---:|:---:|:---|")
    for kw in sorted(framework_matrix.keys(), key=lambda k: -sum(framework_matrix[k].values())):
        counts = framework_matrix[kw]
        cells = [str(counts.get(src, "-")) for src in ["口述稿", "笔记", "逐字稿", "图片OCR"]]
        covered = sum(1 for c in cells if c != "-")
        if covered >= 3:
            consistency = "✅ 高一致性"
        elif covered == 2:
            consistency = "🟡 部分一致"
        else:
            consistency = "❌ 仅单层出现"
        report.append(f"| {kw} | {' | '.join(cells)} | {consistency} |")
    report.append("\n")

    # 4.3 案例覆盖度
    report.append("## 三、案例素材覆盖度\n")
    report.append("| 案例 | 口述稿 | 笔记 | 逐字稿 | 图片OCR | 素材完整度 |")
    report.append("|:---|:---:|:---:|:---:|:---:|:---|")
    for kw in sorted(case_matrix.keys(), key=lambda k: -sum(case_matrix[k].values())):
        counts = case_matrix[kw]
        cells = [str(counts.get(src, "-")) for src in ["口述稿", "笔记", "逐字稿", "图片OCR"]]
        covered = sum(1 for c in cells if c != "-")
        if covered >= 3:
            level = "✅ 素材完整"
        elif covered == 2:
            level = "🟡 素材较完整"
        else:
            level = "❌ 素材单薄"
        report.append(f"| {kw} | {' | '.join(cells)} | {level} |")
    report.append("\n")

    # 4.4 不一致与待确认
    report.append("## 四、不一致与待确认项\n")
    if inconsistencies:
        report.append("| 类型 | 关键词 | 详情 |")
        report.append("|:---|:---|:---|")
        for item in inconsistencies:
            if item["type"] == "仅单层出现":
                report.append(f"| {item['type']} | {item['keyword']} | 仅在 {item['source']} 出现 {item['count']} 次，其他层缺失 |")
            else:
                report.append(f"| {item['type']} | {item['keyword']} | {item['source']} |")
    else:
        report.append("未发现明显不一致。\n")
    report.append("\n")

    # 4.5 命名问题专项
    report.append("## 五、命名问题专项\n")
    report.append("- 图片中框架名为 **BTICOE**（B-T-I-C-O-E）")
    report.append("- 笔记中写为 **BTICME**（B-T-I-C-M-E），M = 方法/Method")
    report.append("- 用户明确统一为 **BITCOE**（B-I-T-C-O-E）")
    report.append("- **结论**：入 wiki 时统一使用 **BITCOE**，并在卡片中说明原名差异。\n")

    # 4.6 高价值段落与案例（自动提取部分）
    report.append("## 六、高价值段落与案例素材\n")
    report.append("### 6.1 沈阳软件公司案例\n")
    for name, text in texts.items():
        if "沈阳" in text or "闫总" in text:
            frags = extract_context(text, "沈阳", 120)
            if frags:
                report.append(f"**{name}**：\n")
                for frag in frags[:2]:
                    report.append(f"> {frag}\n")
    report.append("\n")

    report.append("### 6.2 教育机构销售能力萃取案例\n")
    for name, text in texts.items():
        if "销售" in text and ("新人" in text or "流失率" in text or "PECED" in text or "PACED" in text):
            frags = extract_context(text, "销售", 120)
            if frags:
                report.append(f"**{name}**：\n")
                for frag in frags[:2]:
                    report.append(f"> {frag}\n")
    report.append("\n")

    report.append("### 6.3 导演思维核心定义\n")
    for name, text in texts.items():
        if "导演" in text and "定义" in text:
            frags = extract_context(text, "导演", 100)
            if frags:
                report.append(f"**{name}**：\n")
                for frag in frags[:1]:
                    report.append(f"> {frag}\n")
    report.append("\n")

    # 4.7 与现有 wiki 域的桥接点
    report.append("## 七、与现有 wiki 域的桥接点\n")
    report.append("### 7.1 可直接迁移到鑫港湾/医药零售场景的框架\n")
    report.append("- **PACED 框架**：可用于诊所患者沟通、药店销售话术设计、慢病管理咨询")
    report.append("- **AI 业务档案 5 字段**：可用于定义 agent 角色、药师/医生助手人设")
    report.append("- **OODA 闭环**：可用于药柜运营迭代、小程序产品迭代")
    report.append("- **BITCOE 框架**：可作为 wiki 卡片写作、agent 提示词设计的标准模板\n")

    report.append("### 7.2 可迁移到 KDO 知识工厂操作的框架\n")
    report.append("- **五层跃迁模型**：可用来评估 wiki/知识工厂当前处于哪一层，指引向系统层进化")
    report.append("- **三层架构（需求拆解/AI开发/哨兵质检）**：可映射到老顽童/王语嫣/欧阳锋的分工")
    report.append("- **对抗式生成**：可用于卡片质量提升，生成器（老顽童）+ 判别器（欧阳锋/王语嫣）")
    report.append("- **GAN 三角色架构**：可作为多 agent 协作的技术参考\n")

    report.append("### 7.3 需新建域的原创内容\n")
    report.append("- **人机协作范式：双三角模型域**（用户指定新建）")
    report.append("- 演员↔导演、任务↔产品↔系统、说↔想↔做等成对概念可构成“双三角”结构\n")

    # 保存报告
    report_path = OUTPUT_DIR / "cross_compare_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print(f"交叉比对报告已生成：{report_path}")


if __name__ == "__main__":
    main()
