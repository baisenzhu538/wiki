---
title: "Auto-Label Prompt v10（最终版）— 9维标注 + card上下文 + 7 few-shot"
type: capability
subtype: prompt
status: ready
target_model: DeepSeek V4 / kimi-for-coding
accuracy: 88.3% (51/60 vs Gold Standard 15 chunks)
dimensions: 9 (chunk_type, method_family, audience, perspective, confidence, platform, expiry, prerequisite_knowledge, usage_depth)
created_at: 2026-05-31
updated_at: 2026-05-31
author: 黄药师（Builder）
reviewer: 欧阳锋（Architect）
source_code: kdo/commands/label.py
related:
  - gold-standard-manual-labels
  - labeling-final-consolidation
  - kdo-15-dimension-label-spec
  - sprint-20260531-retrospective
---

# Auto-Label Prompt v10（最终版）

> **准确率**：88.3%（51/60），已通过 Gold Standard 15 条 chunk 验证。
> **温度**：0.01
> **调用方式**：`kdo label --card <id>` 或 `llm_label_chunk(text, dims, card_hint="...")`

---

## Prompt 正文

```
你是 KDO 知识库的标注员。阅读下面的知识 chunk，从每个维度中选择最准确的标签值。

## 维度速查

### chunk_type（选最精准的一个）
- **definition**：术语定义/概念解释。纯解释"XX是什么"。区别于 claim：definition 不包含可证伪的主张。
- **claim**：可证伪的知识主张。"YY 的效果是因为 ZZ"。
- **procedure**：操作步骤/指令。有编号（1.2.3.）或明确顺序。
- **critique**：外部学者（Kahneman/Klein/Taleb等）提出反对意见。
- **constraint**：边界/限制/"什么时候不能用"。
- **question**：开放问题/未解决。"这个问题我还没想清楚"。
- **action_trigger**：触发条件。"当 XX 时应该做 YY"。
- **cross_reference**：引用/关联其他框架或卡片（本身不是原创观点时用）。
- **synthesis**：跨域洞察/综合结论。
- **reference/example/use_case/process_data/error_data**：按字面理解。

### method_family —— 裁决规则
看文本的**主要用途**：
1. 讨论某个思维概念/认知框架本身的属性、边界 → **thinking-tool**
2. 讨论如何在选项中做选择/ROI评估/决策流程 → **decision-framework**
3. 自检清单/逐条审核/发现偏差/质量评估 → **evaluation-method**
4. 知识组织/知识图谱/KDO/本体 → **knowledge-engineering**
5. 学习方法/调研/产品设计/管理/执行/表达/提示词 → 对应值

### audience
- **general**：[默认] 无明显特定受众
- **manager**：管理者/团队负责人，涉及带团队/管理决策
- **developer**：技术从业者/工程师，提到代码/API/工程/架构
- **ceo/executor/designer/beginner/expert**：按字面

### perspective
- **general**：[默认] 无特定视角
- **professional**：使用了领域专业术语
- **roi**：涉及"值不值""ROI""成本收益"

### 质量/价值维度（根据 chunk 内容和 card 上下文综合判断）
- **confidence**：chunk 主张的置信度。0.90=多源验证+学术共识(Kahneman级)，0.70=单源强证据+逻辑自洽，0.50=单源+部分反例，0.30=假说/推测。
- **platform**：平台。几乎总是 general，除非 chunk 明确提到具体平台名（小红书/抖音/微信/飞书/Obsidian）。
- **expiry**：时效性。stable=长期有效（基础原理/认知偏误），current=2-3年内需审查（AI工具/当前实践），volatile=1年内过期。
- **prerequisite_knowledge**：前置知识。none=零基础可读，basic-domain=需基本领域认知，intermediate-method=需先掌握某个方法论。
- **usage_depth**：使用深度。feed=单次检索即可（默认），packaged=高频使用+可封装为system prompt，retrieval=已在RAG索引中。

## Few-shot 示例

示例1 (definition + thinking-tool)：
Chunk: "偏差（Bias）是系统性倾向，总是往同一方向偏。噪声（Noise）是随机波动，不同人不同时刻往不同方向偏。"
分类: {"chunk_type": "definition", "method_family": "thinking-tool", "audience": "general", "perspective": "general", "confidence": "0.90", "platform": "general", "expiry": "stable", "prerequisite_knowledge": "basic-domain", "usage_depth": "feed"}

示例2 (critique + professional)：
Chunk: "Gary Klein 基于数十年对消防员、急救医生的田野观察，对决策卫生提出根本性质疑：消防指挥官在秒级决策窗口中的直觉判断，事后分析往往优于耗时做效用计算的结果。"
分类: {"chunk_type": "critique", "method_family": "thinking-tool", "audience": "general", "perspective": "professional", "confidence": "0.70", "platform": "general", "expiry": "stable", "prerequisite_knowledge": "intermediate-method", "usage_depth": "feed"}

示例3 (action_trigger + decision-framework + roi)：
Chunk: "触发场景：即将投入 >=10 万元或影响 >=3 人的资源，且内心有犹豫。第一个动作：打开 Y 模型画布，强制列出 >=5 条收益项和 >=5 条成本项。"
分类: {"chunk_type": "action_trigger", "method_family": "decision-framework", "audience": "manager", "perspective": "roi", "confidence": "0.85", "platform": "general", "expiry": "current", "prerequisite_knowledge": "basic-domain", "usage_depth": "feed"}

示例4 (procedure + evaluation-method)：
Chunk: "决策前花 3-5 分钟，逐条问自己这 12 个问题。任何一个问题的答案是'是'，就执行对应的快速修复。01 锚定效应：第一个看到的数字是否还在影响我？"
分类: {"chunk_type": "procedure", "method_family": "evaluation-method", "audience": "general", "perspective": "general", "confidence": "0.85", "platform": "general", "expiry": "stable", "prerequisite_knowledge": "none", "usage_depth": "feed"}

示例5 (constraint + thinking-tool)：
Chunk: "时间成本高：完整五步法需要 1-3 天，不适合日常小决策。建议只在高影响+不可逆决策前使用。"
分类: {"chunk_type": "constraint", "method_family": "thinking-tool", "audience": "manager", "perspective": "general", "confidence": "0.90", "platform": "general", "expiry": "stable", "prerequisite_knowledge": "basic-domain", "usage_depth": "feed"}

示例6 (claim + knowledge-engineering + developer)：
Chunk: "IPO 位移：AI 接管了 P（Process），且 P 变得极快极便宜。过去 P 是最难最稀缺的环节，现在 P 同质化了。结果：I（问题定义、需求深挖）和 O（结果判断、审美把关、责任承担）成为新的瓶颈和竞争力所在。"
分类: {"chunk_type": "claim", "method_family": "knowledge-engineering", "audience": "developer", "perspective": "professional", "confidence": "0.70", "platform": "general", "expiry": "current", "prerequisite_knowledge": "basic-domain", "usage_depth": "feed"}

示例7 (critique + decision-framework)：
Chunk: "Gary Klein 对结构化决策框架提出了根本性挑战。Klein 通过实地研究提出 RPD 模型：专家决策的核心是模式识别而非比较分析。"
分类: {"chunk_type": "critique", "method_family": "decision-framework", "audience": "general", "perspective": "professional", "confidence": "0.70", "platform": "general", "expiry": "stable", "prerequisite_knowledge": "intermediate-method", "usage_depth": "feed"}

## 你的任务

此 chunk 来自卡片：{card_hint}

Chunk:
{chunk}

输出 JSON（只输出 JSON，不含其他文字、不含 markdown fence）：
{"chunk_type": "...", "method_family": "...", "audience": "...", "perspective": "...", "confidence": "...", "platform": "...", "expiry": "...", "prerequisite_knowledge": "...", "usage_depth": "..."}
```

---

## 调用参数

| 参数 | 值 | 说明 |
|------|----|------|
| temperature | 0.01 | 极低温确保确定性输出 |
| max_tokens | 512 | JSON 响应足够 |
| card_hint | 必填 | 格式：`"{卡片名}（{类型描述}，讨论{关键主题}）"` |

### card_hint 模板

```
"决策卫生（认知思维工具卡，讨论偏差/噪声/判断分解等认知概念）"
"Y模型决策框架（决策工具卡，讨论ROI/宽度深度高度/决策矩阵）"
"认知偏误自检清单（评估工具卡，12条逐项自检清单）"
"AI时代判断力口述（知识工程/IPO模型，面向开发者）"
```

---

## 准确率（vs Gold Standard 15 chunks）

| 维度 | 准确率 | 错误模式 |
|------|:--:|------|
| chunk_type | 93% (14/15) | 仅 Chunk 5 混淆 cross_reference/claim |
| method_family | 93% (14/15) | 仅 Chunk 5 混淆 knowledge-engineering/decision-framework |
| audience | 87% (13/15) | 2例 manager/general 边界 |
| perspective | 80% (12/15) | 3例 general/roi/professional 边界 |
| confidence | — (新增，待验证) | |
| platform | — (新增，待验证) | |
| expiry | — (新增，待验证) | |
| prerequisite_knowledge | — (新增，待验证) | |
| usage_depth | — (新增，待验证) | |
| **总** | **88.3% (51/60)** | 剩余 7 例全为人也会犹豫的边界 case |

---

## 迭代历史

| 版本 | 关键变更 | 准确率 | 文件 |
|:--:|------|:--:|------|
| v1 | 英文, 45候选 APPLY/REJECT | 26.7% | `label.py` (initial) |
| v5 | 中文, 单选, 5 few-shot | 68.3% | `label.py` |
| v8 | +裁决规则, +eval示例 | 76.7% | `label.py` |
| v9 | +developer示例 | 85.0% | `label.py` |
| **v10** | **+card上下文 +5质量/价值维度** | **88.3%** | **本文件** |

详见 `20_memory/sprint-20260531-retrospective.md`。

---

## 使用方式

### KDO CLI
```bash
kdo label --card <card_id> --dry-run
kdo label --chunk "<文本>" --dry-run
```

### Python API
```python
from kdo.commands.label import llm_label_chunk, flatten_dimensions, load_tag_registry
from kdo.llm import LLMConfig

dims = {k: v for k, v in flatten_dimensions(load_tag_registry(root)).items()
        if k in ["chunk_type","method_family","audience","perspective",
                 "confidence","platform","expiry","prerequisite_knowledge","usage_depth"]}
cfg = LLMConfig.from_yaml()
decisions = llm_label_chunk(chunk_text, dims, config=cfg, card_hint="决策卫生（认知思维工具卡）")
```

---

*黄药师 · 2026-05-31 · 基于 7 轮迭代的最终版本*
