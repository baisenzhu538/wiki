---
id: task_20260704_laowantong-ai-feature-thinking-concept
title: AI 基本功 Feature 思维概念卡
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: null
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
related:
  - '[[annotation-yihang-ai-feature-thinking]]'
  - '[[annotation-yihang-dual-triangle-master]]'
  - '[[concept-yihang-dual-triangle-core]]'
  - '[[method-yitang-y-model-engine-cycle]]'
---

# 任务 #74：AI 基本功 Feature 思维概念卡

## 任务目标

1. 产出一张 concept 卡 `concept-yihang-ai-feature-thinking`，把 Truman 的 **Feature 思维** 固化成 KDO 可调用资产。
2. **重制两张已有的低质量草稿卡**：
   - `tool-Truman-Feature特性层训练法`（当前大量 src_unknown 占位，需用真实素材重写）
   - `tool-Truman-AI能力分层学习路径`（当前大量 src_unknown 占位，需用真实素材重写）

**核心命题**：基本功不是「会用工具」，而是掌握 AI 工具的**最小可操作技术特性（Feature）**，并能用 Feature 组合来解决问题。Feature 层是 Y模型 的底层结构，位于大模型与具体工具之间。

---

## 原始素材

- `00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt` 行 1210、1380-1468
- `00_inbox/AI-study/一堂-AI学习-AI工具应用AMA口述.txt` 行 154-192、行 450-454、行 902、行 2742-2748、行 2778-2784
- `10_raw/sources/src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset.md`（Truman 自用的 AI FeatureSet 四层结构）
- 王语嫣入口标注：`60_feedback/annotations/annotation-yihang-ai-feature-thinking.md`
- **王语嫣产出的概念卡骨架**：`60_feedback/annotations/concept-yihang-ai-feature-thinking-skeleton.md`（老顽童按此骨架转正式卡）
- 王语嫣完整深读报告：`60_feedback/annotations/annotation-yihang-dual-triangle-master.md` 第 3.6 节（已更新）
- 现有草稿卡：`30_wiki/tools/tool-Truman-Feature特性层训练法.md`、`30_wiki/tools/tool-Truman-AI能力分层学习路径.md`

---

## 卡片必须包含的内容

### 1. 一句话定义

Feature 思维 = 把 AI 工具拆成最小可操作技术特性，用特性组合而非工具名字来思考和决策。

### 2. 原文故事（必须出现人物/动作/数字）

| 要素 | 内容 |
|:---|:---|
| **人物** | Truman / 业务团队 / 莹莹 |
| **背景** | 用国外模型跑一轮邮件，花了几万块钱 |
| **转折** | 有人想到一个过去没用过的参数——temperature |
| **动作** | 只调了一个 temperature 参数 |
| **结果** | 用约 1/40 的成本，达到全球最好模型的水准 |
| **教训** | 不是工具不行，是不懂工具的最小技术特性 |

### 3. 三层概念澄清

| 概念 | 定义 | 例子 |
|:---|:---|:---|
| **Feature（特性）** | AI 工具的最小可操作技术单位 | temperature、浏览器使用、长时记忆、思维链、加案例、加约束 |
| **工具** | 把多个 Feature 打包后的产品 | ChatGPT、Coze、Cursor、Claude、Kimi |
| **Skill** | 把 Feature 按特定场景封装后的可复用逻辑 | 口喷提示词、PPT 渲染工作流、论文初审 Agent |

### 4. 常见 Feature 分类（至少 8 个示例）

- 模型参数：temperature、top_p、max_tokens
- 上下文工程：长上下文、RAG、长时记忆
- 推理增强：思维链（CoT）、自我一致性
- 外部能力：浏览器使用、代码执行、API 调用
- 输入增强：few-shot、约束、角色、输出格式
- 输出控制：JSON 模式、Function calling
- 多模态：图像理解、语音输入
- 协作机制：多 Agent 并行、红蓝军对抗

### 5. 对 KDO/Agent 的启示

- Agent 能力应该按 Feature 划分，而不是按工具划分。
- 新工具出现时，只问「它比现有工具多了哪几个 Feature」。
- 双三角画布中的「基本功」格子，可以填入 Feature 清单而不是工具列表。
- KDO 应避免只追热点工具卡，而要沉淀底层 Feature 卡。

### 6. Critique

- Feature 思维是否会让初学者更难？——不会，反而降低认知负担。
- 是否所有工具都能拆成 Feature？——大多数可以，但某些整体化体验可能难以完全拆解。
- Feature 清单需要持续更新，否则容易过时。

---

## 建议产出

| 产出 | ID | 类型 | 优先级 | 说明 |
|:---|:---|:---:|:---:|:---|
| Feature 思维概念卡 | `concept-yihang-ai-feature-thinking` | concept | P0 | 新增 |
| Feature 特性层训练法 | `tool-Truman-Feature特性层训练法` | tool | P0 | **重写现有草稿卡**，清除 src_unknown 占位 |
| AI 能力分层学习路径 | `tool-Truman-AI能力分层学习路径` | tool | P0 | **重写现有草稿卡**，清除 src_unknown 占位 |
| AI 工具特性清单 | `tool-ai-feature-inventory` | tool | P1 | 可与 #75 联动 |

---

## 验收标准

- 3 张 P0 卡全部 `kdo pre-submit` 通过。
- 必须出现 temperature 参数让成本降到约 1/40 的具体案例。
- 必须区分 Feature、工具、Skill 三层概念。
- 必须引用「AI上手第一课 / AI工具应用 AMA」行 154-192 和 Truman 自用 FeatureSet 作为更早来源。
- 必须包含至少 8 个常见 Feature 示例，并说明其来源（双三角口述 / AMA / FeatureSet）。
- 必须说明对 Agent 设计和 KDO 建设的启示。
- 至少反向更新 5 张已有卡 `related`（含 `concept-yihang-dual-triangle-core`、`method-yitang-y-model-engine-cycle`、`tool-Truman-提示词优化底层方法` 等）。
- 欧阳锋终审通过。

---

## 依赖

- 无强阻塞；可与 #64/#65/#72 并行。
- 建议 #65 reviewed 后用最新 dual-triangle 理解校准本卡。

---

## 备注

本任务是对用户批评「9 层深挖漏掉 Feature 思维」的直接回应。王语嫣已更新主标注和入口标注，老顽童按本任务单产出即可。
