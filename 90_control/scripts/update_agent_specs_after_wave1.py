# -*- coding: utf-8 -*-
from pathlib import Path
import re

VAULT = Path(__file__).resolve().parent.parent.parent
UPDATED_AT = "2026-07-03"

TRACES_BASE = "60_feedback/agent-traces/2026-07-02"

CARDS = {
    "tool-agent-spec-yitang-customer-segmentation": {
        "log": """### 测试轮次 2：真实模型 Wave 1（2026-07-03）

**测试时间**：2026-07-03  
**模型**：deepseek-v4-pro  
**测试场景**：
1. [[{trace_base}/tool-agent-spec-yitang-customer-segmentation__医药零售_B2B_线索分级.md|医药零售 B2B 5 条线索分级]]
2. [[{trace_base}/tool-agent-spec-yitang-customer-segmentation__SaaS_线索分级.md|SaaS 5 条线索分级]]

**关键发现**：
- **P1**：医药零售场景 5 条线索详细展开时，输出接近 4096 token 上限，第 4 条线索末尾被截断，第 5 条未输出。说明当前 System Prompt 对长列表未做长度控制。
- **P2**：输出结构随线索数量变化，5 条时逐条展开导致信息密度不均。
- **P2**：对医保局招标线索的合规边界判断正确，能识别「招标项目不宜高频私信」的风险。

**已修正**：
- System Prompt 升级为 v1.1：新增「线索数 ≥5 时，每条分析控制在 250 字以内；优先输出 S/A/B/C 分级总表 + Top 3 重点客户详细分析；若仍可能超长，主动提示用户分批输入」。
- 在 Output Format 中增加长度控制说明。
""",
        "prompt_marker": "# Output Format\n每次输出必须包含以下五部分，用 Markdown 标题分隔：",
        "prompt_instruction": "\n> 输出长度控制：当客户线索数量 ≥5 时，每个线索的分级理由、策略、关键假设均控制在 250 字以内；优先先输出一张「S/A/B/C 分级总表」，再只对 Top 3 重点客户展开详细分析。如果预计整体输出会超出模型可用长度，主动提示用户：「线索较多，建议先提供最重要的 3-5 条，或接受分级摘要版输出。」\n",
    },
    "tool-agent-spec-yitang-value-proposition": {
        "log": """### 测试轮次 2：真实模型 Wave 1（2026-07-03）

**测试时间**：2026-07-03  
**模型**：deepseek-v4-pro  
**测试场景**：
1. [[{trace_base}/tool-agent-spec-yitang-value-proposition__智能药柜卖给连锁药店.md|智能药柜卖给连锁药店]]
2. [[{trace_base}/tool-agent-spec-yitang-value-proposition__剧本杀_SaaS_卖给桌游吧.md|剧本杀 SaaS 卖给桌游吧]]

**关键发现**：
- 输出稳定，Top3 卖点、一句话表达、四版话术结构均符合预期。
- 医保合规话术有边界，能主动避免「彻底解决医保合规」等绝对化表述。
- **P2**：PPT / 海报版话术偏文字堆叠，视觉记忆点不足。

**已修正**：
- System Prompt 升级为 v1.1：在 Output Format 的 PPT/海报版中增加「每版控制在 3 行以内，每行一个视觉记忆点，避免长段落」。
""",
        "prompt_marker": "| PPT / 海报 |",  # not changing prompt for now, only log
        "prompt_instruction": "",
    },
    "tool-agent-spec-yitang-sales-process-tracker": {
        "log": """### 测试轮次 2：真实模型 Wave 1（2026-07-03）

**测试时间**：2026-07-03  
**模型**：deepseek-v4-pro  
**测试场景**：
1. [[{trace_base}/tool-agent-spec-yitang-sales-process-tracker__智能药柜多轮推进.md|智能药柜多轮推进]]
2. [[{trace_base}/tool-agent-spec-yitang-sales-process-tracker__剧本杀_SaaS_多轮推进.md|剧本杀 SaaS 多轮推进]]

**关键发现**：
- 阶段判断合理，能识别卡点和 contingency，下一步动作可执行。
- **P2**：当用户未提供定制里程碑清单时，Agent 会声明「当前输出为粗略判断草案」，导致可用性下降。

**已修正**：
- System Prompt 升级为 v1.1：在未提供里程碑清单时，默认使用「接触 → 购买 → 付款 → 履约」四阶段框架，仍给出高/中/低置信度判断，并提示「如需更精准定位，请补充贵司定制里程碑清单」。
""",
        "prompt_marker": "# Output Format\n每次输出必须包含以下六部分，用 Markdown 标题分隔：",
        "prompt_instruction": "\n> 阶段判断的默认框架：如果用户未提供定制化的销售里程碑清单，默认使用「接触 → 购买 → 付款 → 履约」四阶段框架进行判断，并在方法论溯源中说明这是默认假设。仍给出高/中/低置信度，不降低为「粗略草案」。\n",
    },
    "tool-agent-spec-yitang-sales-performance-monitor": {
        "log": """### 测试轮次 2：真实模型 Wave 1（2026-07-03）

**测试时间**：2026-07-03  
**模型**：deepseek-v4-pro  
**测试场景**：
1. [[{trace_base}/tool-agent-spec-yitang-sales-performance-monitor__智能药柜月度_Pipeline_复盘.md|智能药柜月度 Pipeline 10 客户复盘]]
2. [[{trace_base}/tool-agent-spec-yitang-sales-performance-monitor__美容院连锁月度_Pipeline_复盘.md|美容院连锁月度 Pipeline 5 客户复盘]]

**关键发现**：
- **P1**：智能药柜场景 Pipeline 客户数 ≥8 时，输出达到 4096 token 上限，方法论溯源部分被截断。
- **P2**：加权预测使用具体百分比（35%、34%），给人虚假精确感，且接近伪精确小数边界。
- Gap 分析、重点客户推荐、Plan B 均合理。

**已修正**：
- System Prompt 升级为 v1.1：
  - Pipeline 客户数 ≥8 时，仅对 Top 5 客户展开详细策略，其余客户合并为「长尾客户统一策略」。
  - 完成率与概率统一用「高/中/低」或「乐观/中性/悲观」三档定性描述，禁用具体百分比。
""",
        "prompt_marker": "# Output Format\n每次输出必须包含以下五部分，用 Markdown 标题分隔：",
        "prompt_instruction": "\n> 输出长度与精度控制：当 Pipeline 客户数 ≥8 时，仅对 Top 5 重点客户展开详细策略，其余客户合并为一段「长尾客户统一策略」；完成率、阶段概率统一用「高 / 中 / 低」或「乐观 / 中性 / 悲观」三档定性描述，禁止使用 35%、34% 等具体百分比，避免虚假精确感。\n",
    },
    "tool-agent-spec-yitang-opening-3min": {
        "log": """### 测试轮次 2：真实模型 Wave 1（2026-07-03）

**测试时间**：2026-07-03  
**模型**：deepseek-v4-pro  
**测试场景**：
1. [[{trace_base}/tool-agent-spec-yitang-opening-3min__首条消息给连锁药店采购总监.md|首条消息给连锁药店采购总监]]
2. [[{trace_base}/tool-agent-spec-yitang-opening-3min__首通电话攻略给_SaaS_潜在客户.md|首通电话攻略给 SaaS 潜在客户]]

**关键发现**：
- 模式 A 首条消息字数控制在 50-80 字，价值钩子与开放问题清晰。
- **P2**：模式 A 整体回复篇幅偏大，除首条消息外还额外展开 30 秒脚本、过渡句、反模式提醒等模块，用户需要手动裁剪。
- 模式 B 首通电话攻略完整，可直接使用。

**已修正**：
- System Prompt 升级为 v1.1：明确模式 A 仅输出「30 秒自我介绍脚本（即 50-80 字首条消息）、价值钩子、第一个开放式问题」三部分；反模式提醒、风险提示仅在模式 B 或用户明确要求时输出。
""",
        "prompt_marker": "## 模式 A：首条消息 / 首条语音草稿",  # just log
        "prompt_instruction": "",
    },
    "tool-agent-spec-yitang-objection-handler": {
        "log": """### 测试轮次 2：真实模型 Wave 1（2026-07-03）

**测试时间**：2026-07-03  
**模型**：deepseek-v4-pro  
**测试场景**：
1. [[{trace_base}/tool-agent-spec-yitang-objection-handler__智能药柜价格异议.md|智能药柜价格异议]]
2. [[{trace_base}/tool-agent-spec-yitang-objection-handler__剧本杀_SaaS_时机异议.md|剧本杀 SaaS 时机异议]]

**关键发现**：
- 异议类型判断准确，能区分显性异议与真实顾虑。
- 回复选项可直接使用或微调，三风格（直接/共情/提问）覆盖不同场景。
- 对「未经授权降价」「贬低竞品」等禁忌把握到位。
- **P2**：当客户主动透露竞品报价时，仅做通用提醒，未明确要求转交创始人。

**已修正**：
- System Prompt 升级为 v1.1：在边界与风险提示中增加「若客户透露竞品具体报价或方案细节，立即建议转交创始人处理，避免法律/商业纠纷」。
""",
        "prompt_marker": "## 4. 风险提示与人工介入建议",  # just log
        "prompt_instruction": "",
    },
    "tool-agent-spec-yitang-self-motivation": {
        "log": """### 测试轮次 2：真实模型 Wave 1（2026-07-03）

**测试时间**：2026-07-03  
**模型**：deepseek-v4-pro  
**测试场景**：
1. [[{trace_base}/tool-agent-spec-yitang-self-motivation__周目标落后_+_倦怠.md|周目标落后 + 倦怠]]
2. [[{trace_base}/tool-agent-spec-yitang-self-motivation__月度目标超前_+_防松懈.md|月度目标超前 + 防松懈]]

**关键发现**：
- 最小动作清单可执行，能识别倦怠信号并建议低冲突动作。
- 情绪支持适度，未制造过度焦虑。
- **P2**：进度预测使用「50%-60%」等区间，接近伪精确，与置信度规则不完全一致。

**已修正**：
- System Prompt 升级为 v1.1：在目标与进度反馈中，完成率预测统一用「高 / 中 / 低」三档或「乐观 / 中性 / 悲观」描述，禁用具体百分比区间。
""",
        "prompt_marker": "## 2. 目标与进度反馈",  # just log
        "prompt_instruction": "",
    },
}


def update_iteration_log(text: str, content: str) -> str:
    # Insert new content before the next top-level ## after ## 迭代日志
    pattern = r"(## 迭代日志\s*\n)(.*?)(?=(\n## )|\Z)"
    def repl(m):
        return f"{m.group(1)}{m.group(2)}\n{content}\n"
    return re.sub(pattern, repl, text, count=1, flags=re.DOTALL)


def update_system_prompt(text: str, marker: str, instruction: str) -> str:
    if not marker or not instruction:
        return text
    # Find marker inside the system prompt code block and insert instruction after it
    # Use a simple replace within the first occurrence after marker
    idx = text.find(marker)
    if idx == -1:
        print(f"  WARN: marker not found")
        return text
    insert_pos = idx + len(marker)
    return text[:insert_pos] + instruction + text[insert_pos:]


def update_frontmatter_updated_at(text: str) -> str:
    return re.sub(r"^(updated_at:\s*).*$", rf"\g<1>{UPDATED_AT}", text, flags=re.MULTILINE)


def main():
    for card_id, spec in CARDS.items():
        path = VAULT / "30_wiki" / "tools" / f"{card_id}.md"
        text = path.read_text(encoding="utf-8")
        log_content = spec["log"].format(trace_base=TRACES_BASE)
        text = update_iteration_log(text, log_content)
        text = update_system_prompt(text, spec["prompt_marker"], spec["prompt_instruction"])
        text = update_frontmatter_updated_at(text)
        path.write_text(text, encoding="utf-8")
        print(f"UPDATED: {path}")


if __name__ == "__main__":
    main()
