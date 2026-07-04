---
id: concept-yihang-ai-feature-thinking-skeleton
type: annotation
status: draft
note: 本文件是 concept-yihang-ai-feature-thinking 的卡片骨架，由王语嫣产出，供老顽童转为 30_wiki/concepts/ 正式卡
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
  - 00_inbox/AI-study/一堂-AI学习-AI工具应用AMA口述.txt
  - 10_raw/sources/src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset.md
related:
  - '[[concept-yihang-dual-triangle-core]]'
  - '[[tool-Truman-Feature特性层训练法]]'
  - '[[tool-Truman-AI能力分层学习路径]]'
  - '[[tool-ai-feature-inventory]]'
---

# 概念卡骨架：AI 基本功的 Feature 思维

> **用途**：老顽童按此骨架生产正式概念卡 `30_wiki/concepts/concept-yihang-ai-feature-thinking.md`。
> 所有 section 标题、案例、引用均已给出，可直接迁移/扩写。

---

## 一、Frontmatter（供正式卡使用）

```yaml
---
id: concept-yihang-ai-feature-thinking
title: AI 基本功的 Feature 思维
type: concept
domain:
  - ai-collaboration
  - yitang
status: draft
author: 老顽童
reviewed_by: pending
created_at: '2026-07-04'
confidence: 0.9
trust_level: high
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
  - 00_inbox/AI-study/一堂-AI学习-AI工具应用AMA口述.txt
  - 10_raw/sources/src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset.md
related:
  - '[[concept-yihang-dual-triangle-core]]'
  - '[[tool-Truman-Feature特性层训练法]]'
  - '[[tool-Truman-AI能力分层学习路径]]'
  - '[[tool-ai-feature-inventory]]'
  - '[[method-yitang-y-model-engine-cycle]]'
---
```

---

## 二、一句话定义

**Feature 思维 = 把 AI 工具拆成最小可操作技术特性，围绕特性组合而非工具名字来思考、选型、练习和决策。**

---

## 三、核心命题（卡片正文第一段）

1. **基本功 ≠ 会用工具**。今天学 ChatGPT、明天学 Coze、后天学 Cursor，是「工具迷信」。
2. **基本功 = 掌握 AI 工具的 Feature（最小可操作技术特性）**。Feature 是位于底层大模型与上层工具之间的中间层。
3. **Feature 是原子化的、可测试的、可组合的**。例如 temperature、渐进披露、长时记忆、思维链、加案例、加约束。
4. **Skill 是 Feature 的封装逻辑**。Feature 是原子，Skill 是把原子按场景打包后的可复用逻辑。
5. **Feature 思维让人不被工具带走**。新工具火不火不重要，重要的是它比现有工具多了哪几个 Feature。

---

## 四、原文依据（必须引用）

### 4.1 双三角课程中的 Feature 思维

> 「第三个我们说的基本功，说的是 AI 基本功啊，就是 AI 上的那些工具，那些特性。」（双三角口述稿，行 1210）

> 「不要老盯着工具，你去盯着每一个工具那些特有的最小的技术特性。」（双三角口述稿，行 1408）

> 「特性是原子化的最小技术单位，叫可操作的原子化的最小技术单位。它跟 skill 是两套东西，skill 就是一个封装逻辑。」（双三角口述稿，行 1426-1428）

### 4.2 AI 上手第一课 / AI 工具应用 AMA 中的 Feature 层

> 「这在基于底层的大模型和上面的工具中间呢，要抽出了一层叫做 feature 啊，就是 feature 啊的特性。它是指的一些封装啊，包括渐进披露啊，包括 data pack 等等。」（AMA 口述，行 154-156）

> 「基于这个逻辑我们构建了 Y 模型，整个 Y 模型都是在特性 feature 的基础上去构建的。」（AMA 口述，行 160）

> 「在我们这儿你如果理解了 feature 这套逻辑工具对你来说就没有那么重要。你用什么工具？其实你用的就是那些特性。」（AMA 口述，行 180-184）

> 「但核心就是这些，核心的是提炼出来 feature 这一层这是核心。」（AMA 口述，行 192）

### 4.3 Truman 自用的 AI FeatureSet

来源：`10_raw/sources/src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset.md`

该 FeatureSet 把 Feature 分为 LLM 层、提示词层、上下文控制层、数据层、协作层、效率层六层。详见本骨架第七节。

---

## 五、关键案例：temperature 参数让成本降到 1/40

| 要素 | 内容 |
|:---|:---|
| **人物** | Truman / 业务团队 / 莹莹 |
| **背景** | 用国外模型跑一轮邮件，花了几万块钱，效果还不理想 |
| **动作** | 有人想到一个过去没用过的参数——**temperature**，只调了一个参数 |
| **结果** | 用约 **1/40 的成本**，达到了跟全球最好模型差不多的水准 |
| **教训** | 不是工具不行，是不懂工具的最小技术特性；基本功不是会换工具，而是会调特性 |

原文：

> 「我们用国外的模型做跑一轮，几万封一封信花了我们几万块钱……后来只要突然间想到了一个参数……然后调了一个 temperature……跟国外模型一模一样。就一个参数。」（双三角口述稿，行 1380-1388）

> 「所以我们用了大概 40 分之 1 的成本，达到了跟全球最好的模型的水准，就靠调一个小的参数。」（双三角口述稿，行 1392）

---

## 六、概念澄清：Feature vs 工具 vs Skill

| 概念 | 定义 | 例子 |
|:---|:---|:---|
| **Feature（特性）** | AI 工具的最小可操作技术单位 | temperature、渐进披露、长时记忆、思维链、加案例、加约束 |
| **工具** | 把多个 Feature 打包后的产品 | ChatGPT、Coze、Cursor、Claude、Kimi、Codex |
| **Skill** | 把 Feature 按特定场景封装后的可复用逻辑 | 口喷提示词、PPT 渲染工作流、论文初审 Agent |
| **基本功** | 掌握 Feature 清单，并能根据场景组合 Feature | 知道什么时候调 temperature、什么时候加浏览器、什么时候用长时记忆 |
| **工具迷信** | 被工具名字带着走，忽略底层 Feature | 因为某个工具火了就切换，结果没用到新 Feature |

---

## 七、Truman 自用 AI FeatureSet 的结构化呈现

> 来源：`src_20260609_03491271`；OCR 有误，以下已做初步校对。

| 层级 | Feature 清单 |
|:---|:---|
| **LLM 层（大模型层）** | 选模型、使用不同版本、模型参数、同时抽卡、模型组合 |
| **提示词层** | 提示词迭代、数字角色/用户角色、任务要求、背景信息、行文规则、负面限制、输出要求、风格设定、多轮对话 |
| **上下文控制层** | 更大上下文、渐进式披露、复制粘贴、分层标注、重点标注、主动摘要、使用 Skill |
| **数据层** | 给案例集、专家资料、用多模态、联网搜索、接入 API、使用 RAG、数据分层 |
| **协作层** | AI 高阶角色、反向提示、反向教学、反向采访、反向记录、使用 CoV、使用 ReACT |
| **效率层** | 拆分任务、拆解环节、分离场景、多轮确认、使用 CoT、设计工作流、分支环、使用插件、模型匹配、并行调度、效率提升 |

---

## 八、常见 Feature 示例（跨来源汇总）

| 类别 | Feature 示例 | 来源 |
|:---|:---|:---|
| 模型参数 | temperature、top_p、max_tokens、frequency_penalty | 双三角口述稿 + FeatureSet |
| 上下文工程 | 长上下文、RAG、渐进披露、长时记忆、摘要压缩 | FeatureSet + AMA |
| 推理增强 | 思维链（CoT）、自我一致性、ReACT、Tree-of-Thoughts | AMA + 双三角口述稿 |
| 外部能力 | 浏览器使用、代码执行、文件读写、API 调用 | 双三角口述稿 |
| 输入增强 | 加案例（few-shot）、加约束、加角色、加输出格式 | FeatureSet |
| 输出控制 | JSON 模式、结构化输出、Function calling | FeatureSet |
| 多模态 | 图像理解、语音输入、视频分析 | FeatureSet |
| 协作机制 | 多 Agent 并行、红蓝军对抗、迭代反馈 | FeatureSet + 双三角口述稿 |
| 数据增强 | Data Pack、案例集、专家资料、联网搜索 | AMA + FeatureSet |

---

## 九、Feature 思维的实操价值

### 9.1 对个人：不被工具带走

- 新工具出现时，只问：「它比我现在用的工具多了哪几个 Feature？」
- 如果新 Feature 不是当前任务需要的，继续用旧工具。
- 如果新 Feature 能提升结果，快速迁移。

### 9.2 对团队：统一语言

- 团队讨论不再说「用大模型还是小模型」，而是说「这个任务需要温度调节 + 长上下文 + 浏览器使用」。
- Feature 清单成为团队选型、评估、AB 测试的共同语言。

### 9.3 对 Agent 设计：原子化能力

- Agent 的能力不应该按工具划分，而应该按 Feature 划分。
- 例如：一个 Agent 可以组合「思维链 + 长时记忆 + 工具调用」三个 Feature，而不是绑定到某个具体模型。
- 这样 Agent 可以随着工具升级无缝迁移。

### 9.4 对 KDO 建设

- 应该把热门工具拆解为 Feature 清单，沉淀为 concept/method/tool 卡。
- 避免 KDO 出现「追热点工具卡」而缺少「底层 Feature 卡」。
- 双三角画布中的「基本功」格子，未来可以填入 Feature 清单而不是工具列表。

---

## 十、如何练习 Feature 思维（操作步骤）

1. **列出你当前任务需要的 Feature**，而不是工具。
2. **评估现有工具是否覆盖这些 Feature**。
3. **新工具出现时只比较 Feature 差异**。
4. **把常用 Feature 组合沉淀为 Skill**。
5. **定期用 Feature 清单复盘自己的 AI 工作流**。

---

## 十一、边界与 Critique

- **反例**：某些工具的整体 UX 就是其价值，拆成 Feature 后可能丢失体验优势。
- **边界**：Feature 思维主要适用于技术类基本功；审美、创造力等人类三角能力不能完全 Feature 化。
- **成本**：维护 Feature 清单需要持续跟进工具更新，否则清单会过时。
- **误用**：把「Feature 堆砌」当成能力提升，忽略场景和审美判断。

---

## 十二、Related 卡片（正式卡必须链接）

- `[[concept-yihang-dual-triangle-core]]`
- `[[tool-Truman-Feature特性层训练法]]`
- `[[tool-Truman-AI能力分层学习路径]]`
- `[[tool-ai-feature-inventory]]`
- `[[method-yitang-y-model-engine-cycle]]`

---

## 十三、给老顽童的生产提示

1. 按上述 12 个 section 组织正式卡。
2. 第七节 FeatureSet 表格需要结合原图做最终 OCR 校对（特别是「歌子角色→数字角色」「别离场景→分离场景」等）。
3. 第五节 temperature 案例必须保留人物/动作/数字三要素。
4. 卡片中所有 Feature 示例都要能对应到原文或 FeatureSet。
5. 生产完成后，记得反向更新 `concept-yihang-dual-triangle-core`、`method-yitang-y-model-engine-cycle` 等已有卡的 `related`。
