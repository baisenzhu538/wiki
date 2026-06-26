---
id: diag_20260627_wangyuyan-skill-taxonomy-evaluation
type: diagnosis_report
created_at: 2026-06-27
author: 王语嫣
scope: 欧阳锋「只有三个真正的 skills」论断的独立评估
confidence: 0.88
trust_level: high
related:
  - '[[skill-research-behavior-over-asking]]'
  - '[[skill-research-decision-first-mapping]]'
  - '[[skill-research-triangulation-stop-rule]]'
  - '[[framework-yitang-taxonomy]]'
---

# 王语嫣独立评估：为什么只有 3 个真正的 skill？

> 用户问：欧阳锋说只有三个真正的 skills，那之前积累的 skills 去哪儿了？是不构成 skills 吗？是什么原因？
> 王语嫣基于当前 vault 实际状态给出独立客观评价。

---

## 一、当前事实状态

### 1.1 当前 `30_wiki` 中 `type: skill` 的卡片

王语嫣扫描结果：

| 路径 | 卡片 ID | 状态 |
|:---|:---|:---|
| `30_wiki/skills/skill-research-behavior-over-asking.md` | 行为证据重于口头证据 | enriched, reviewed |
| `30_wiki/skills/skill-research-decision-first-mapping.md` | 决策优先映射 | enriched, reviewed |
| `30_wiki/skills/skill-research-triangulation-stop-rule.md` | 多源交叉验证的停止规则 | enriched, reviewed |
| `30_wiki/skills/yt-demand-insight-extraction.md` | 从用户访谈中提取真实需求 | enriched, reviewed |
| `30_wiki/skills/feishu-docx-pagination-extraction.md` | 飞书 Docx API 分页安全提取 | enriched, reviewed |

**注**：欧阳锋说「只有三个真正的 skills」，大概率指前三个 `skill-research-*` 系列。后两个（需求洞察提取、飞书分页提取）虽然 `type=skill`，但可能仍处于待终审或边界状态。

### 1.2 之前的 457 张 `skill-*.md` 去哪儿了？

王语嫣在 2026-06-27 早些时候扫描到 457 张 `skill-*.md`，其中 361 张 frontmatter 已标记为 `type: tool`、2 张为 `type: concept`。在欧阳锋 taxonomy 裁决执行后，这些文件已被批量重命名：

| 原文件名 | 现文件名 | 实际类型 |
|:---|:---|:---:|
| `skill-ai-four-elements-validation.md` | `tool-ai-four-elements-validation.md` | tool |
| `skill-1视角升级思考法.md` | `tool-1视角升级思考法.md` | tool |
| `skill-Truman-AI场景探索STAR模型.md` | `tool-Truman-AI场景探索STAR模型.md` | tool |
| `skill-纪浩-Agent开工检查单制作法.md` | `tool-纪浩-Agent开工检查单制作法.md` | tool |
| `skill-纪浩-ai-collaboration-five-layer.md` | `concept-纪浩-ai-collaboration-five-layer.md` | concept |
| ... | ... | ... |

**结论**：之前的 457 张 skill 卡并没有被删除，而是根据内容本质被重新分类并更名。它们现在以 `tool-*`、`concept-*`、`framework-*`、`dk-*` 的形式存在。

---

## 二、为什么大部分 skill 卡不是真正的 skill？

### 2.1 它们实际是什么？

王语嫣抽样检查了 20+ 张原 skill 卡，发现：

| 实际内容 | 占比估算 | 正确类型 |
|:---|---:|:---|
| 操作步骤 / 检查单 / SOP | ~75% | **tool** |
| 概念定义 / 原则 / 认知框架 | ~15% | **concept** 或 **framework** |
| 跨案例提炼的暗知识 | ~8% | **dk** |
| 真正的高阶判断技能 | ~2% | **skill** |

### 2.2 典型误分类案例

#### 案例 1：`skill-ai-four-elements-validation` → `tool-ai-four-elements-validation`

- **原标**：skill
- **内容**：真需求四要素验证法，包含操作步骤、诊断信号、检查清单
- **本质**：一套可执行的需求验证 **工具/流程**
- **为什么不是 skill**：它告诉你「按哪四步验证」，而不是「在什么情境下凭直觉判断要不要验证」。

#### 案例 2：`skill-Truman-AI场景探索STAR模型` → `tool-Truman-AI场景探索STAR模型`

- **原标**：skill
- **内容**：用 STAR 模型探索 AI 应用场景
- **本质**：结构化分析 **工具**
- **为什么不是 skill**：STAR 是一个可被直接调用的方法论模板，不是需要长期修炼的判断力。

#### 案例 3：`skill-纪浩-ai-collaboration-five-layer` → `concept-纪浩-ai-collaboration-five-layer`

- **原标**：skill
- **内容**：纪浩 AI 协作五层工作空间法
- **本质**：概念框架
- **为什么不是 skill**：它描述的是一个分层模型/认知框架，而非可训练的操作技能或判断技能。

---

## 三、什么才是真正的 skill？

王语嫣基于欧阳锋的 taxonomy 和当前 3-5 张 skill 卡，归纳出 **KDO 中 skill 的判定标准**：

### 3.1 必要条件

| 条件 | 说明 |
|:---|:---|
| **高阶判断力** | 不是「按步骤执行」，而是「在不确定情境下做出优质判断」 |
| **诊断信号** | 必须有 `diagnostic_signals`，明确「什么时候该想起这个技能」 |
| **跨案例合成** | 最好来自多个 case 的抽象，而非单门课程的Procedure |
| **与 tool/concept/dk 有清晰边界** | skill 是「知道何时、为何、用哪个 tool」的能力，而不是 tool 本身 |
| **可训练但不可完全 SOP 化** | 有练习路径，但无法被写成 100% 机械步骤 |

### 3.2 三个 true skill 为什么合格？

| 卡片 | 核心判断 | 为什么是真正的 skill |
|:---|:---|:---|
| `skill-research-behavior-over-asking` | 行为证据重于口头证据 | 不是访谈方法，而是「什么时候该怀疑用户口头表述」的判断力 |
| `skill-research-decision-first-mapping` | 决策优先映射 | 不是研究流程，而是「研究动作是否值得做」的决策判断力 |
| `skill-research-triangulation-stop-rule` | 多源交叉验证停止规则 | 不是验证技术，而是「什么时候该停止验证、转向决策」的判断力 |

三者的共性：**它们都是关于「何时停止/转向/怀疑」的元认知技能**，而不是关于「怎么做」的操作步骤。

### 3.3 另外两个 skill 是否合格？

| 卡片 | 评估 |
|:---|:---|
| `yt-demand-insight-extraction` | 偏 tool。它有明确访谈框架（拆推评算四维度），更像「用户访谈工具」而非高阶判断技能。建议降级为 tool 或拆分为 concept + tool。 |
| `feishu-docx-pagination-extraction` | 偏 tool/code-skill。它是具体的技术实现模式（分页安全提取 + 流式处理），更像「代码工具/工程模式」。建议保留为 skill 或改为 tool 均可，取决于 KDO 是否把「工程模式」纳入 skill 范畴。 |

---

## 四、独立客观评价

### 4.1 欧阳锋的论断是否正确？

**基本正确，但可以更精确表述为：当前 vault 中只有 3 张卡片真正符合 KDO 的 skill 高标准。**

理由：
1. 之前的 457 张 skill 卡绝大多数是 tool/concept 的误标；
2. 重新分类后，知识库 taxonomy 更清晰，Agent 检索精度会提高；
3. 3 张 true skill 均来自跨案例合成，且有 diagnostic_signals，符合 skill 定义。

### 4.2 这次重分类的价值

| 价值 | 说明 |
|:---|:---|
| **消除 taxonomy 噪音** | Agent 不会被误导到「skill」类型去查找一个其实是 tool 的东西 |
| **提高检索精度** | 用户问「给我个工具」时，不会返回 concept；问「给我个原则」时，不会返回 tool |
| **降低维护成本** | skill 是高门槛类型，少量精品比大量滥发更易维护 |
| **为 future skill 设定标杆** | 以后新增 skill 卡必须对标这 3 张的标准 |

### 4.3 潜在风险

| 风险 | 说明 |
|:---|:---|
| **重命名导致死链** | 大量 `[[skill-xxx]]` 链接可能失效，需黄药师批量修复 |
| **边界争议** | `yt-demand-insight-extraction` 这类卡片是否算 skill，可能仍有争议 |
| **用户/团队习惯** | 之前习惯了「skill」这个叫法，短期内需要适应 tool/concept 区分 |
| **未文档化标准** | 如果 skill 判定标准不写清楚，未来还会重复误分类 |

---

## 五、建议

### 5.1 立即做

1. **把 skill 判定标准写入 `.agent/taxonomy.md` 或 `40_outputs/capabilities/skills/shared/kdo-card-taxonomy/SKILL.md`**，明确 skill vs tool vs concept vs framework vs dk 的边界。
2. **修复重命名导致的死链**：跑全库 wikilink 扫描，把 `[[skill-xxx]]` 替换为新的 `[[tool-xxx]]` / `[[concept-xxx]]`。
3. **确认 `yt-demand-insight-extraction` 和 `feishu-docx-pagination-extraction` 的最终类型**：建议前者改为 tool，后者可保留 skill（作为工程模式 skill）或改为 tool。

### 5.2 中期做

4. 建立「skill 准入委员会」机制：新增 skill 卡必须经欧阳锋或王语嫣终审。
5. 在 `kdo scaffold` 或 `kdo pre-submit` 中加入类型推断提示：根据内容结构建议用户选择 type。

---

## 六、一句话结论

> **欧阳锋的论断是对的。之前 457 张 skill 卡里，真正配得上「skill」这个高门槛类型的只有 3 张（最多 5 张）。其余的不是被删除了，而是根据内容本质被重新分类为 tool / concept / framework / dk。这是一次必要的 taxonomy 纠偏，会让知识库更清晰，但重命名后的死链需要黄药师批量修复。**

---

*评估人：王语嫣 | 日期：2026-06-27*
