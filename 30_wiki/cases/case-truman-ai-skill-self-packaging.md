---
id: case-truman-ai-skill-self-packaging
title: AI 自复盘自封装：Truman 的 design case 技能是如何让 AI 自己包装出来的
type: case
source_refs:
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
status: reviewed
confidence: 0.85
domain: ai-collaboration
created_at: '2026-06-14'
author: 黄药师（基于 Truman 口述提取），老顽童 2026-08-22 回填补强
reviewed_by: 欧阳锋
review_notes: 历史遗留，写审分离规则确立前的早期卡片。有效性由月度抽检覆盖。2026-08-22 #408 回填空洞清零 + 8-15 口述增量（YI partner 复用链）。
review_date: 2026-08-22
trust_level: high
discoverable_by:
  - AI 自复盘自封装：Truman 的 design case
  - 自复盘自封装
  - 技能是如何让
  - 自己包装出来的
related:
- '[[case-truman-ai-skill-engineering-guide]]'
- '[[tool-skill-packaging-eight-steps]]'
- '[[dk-three-context-formula]]'
- '[[case-strategy-practice-11-third-place]]'
- '[[case-private-domain-ecommerce-formula]]'
- '[[case-strategy-failure-06-phone-n]]'
- '[[case-strategy-m-brand-profit-model]]'
- '[[tool-Truman-提示词优化底层方法]]'
- '[[case-five-step-growth-first-lever]]'
- '[[yt-product-kernel-shampoo-case]]'
- '[[case-demand-pharma-bigdata]]'
- '[[dk-modeling-case-explosion-confidence]]'
- '[[tool-Truman-AI能力分层学习路径]]'
- '[[case-doris-outbound-travel-community]]'
- '[[case-strategy-failure-04-appliance]]'
- '[[case-hr-saas-feature-usage-trap]]'
- '[[case-strategy-retailer-activity-scope]]'
- '[[case-truman-poker-deck-roi]]'
- case-child-drawing-rhyme
- case-truman-personal-growth-map-creation
- '[[ai-methodology-tools]]'
- '[[tool-ai-skill-engineering-guide]]'
- '[[tool-ai-skill-engineering-method]]'
- '[[tool-yitang-18-strategy-tool-mapping]]'
tags:
- audience:general
- scene:reference
- skill-level:intermediate
- ai-collaboration
- ai-self-packaging
- case-truman
diagnostic_signals:
- framework_lens: AI自复盘——让AI总结这次经验变下次基础
  follow_up_question: 你最后一次项目结束时，有没有让AI扫描你全程的纠偏记录、自动生成一个skill？
- framework_lens: 让AI跨工具扫描+合并同类项+封装
  follow_up_question: 你用过哪些AI工具？它们的对话/反馈记录是明文存储的吗？如果是，可以直接让另一个AI去读。
- framework_lens: 缺少可复用的审美底盘和硬性坑清单
  follow_up_question: 你是否有一个"做过就忘不掉"的skill文件，能在每次同类任务开始时自动加载审美标准和禁止项？
source_context: 单一 source 为完整长文档，内容充分支撑 high trust；2026-08-22 #408 已补第二来源（8-15 口述 L1056-1072）并回填全部空洞，trust 从 medium 升回 high
updated_at: '2026-08-22'
aliases:
- 建模能力培训
- AI知识库
- 楚门-AI知识管理探索营-口述
- AI 自复盘自封装
- design case
- AI 自封装
---
# AI 自复盘自封装：Truman 怎么让 AI 把自己包装成一个技能

> 本卡属于 AI 协作域的 AI 自封装案例卡：展示"项目结束 → AI 扫描纠偏记录 → 合并同类项 → 封装 skill → 下次自动加载"的完整自复盘闭环，与 `case-truman-ai-skill-engineering-guide`（人工造 Skill 工程指南）同源互补、分工不同——本卡讲 AI 怎么自己把经验封装成 skill，那张卡讲人怎么造出高质量 Skill 指南并审计。方法论配套见 `tool-skill-packaging-eight-steps`（Skill 八步封装）。

> **Burn line**: 不是人写 skill——是 AI 扫描你所有的纠偏记录，自己把自己的经验封装成 skill。

---

## Background

Truman 在一堂高阶建模课上分享了一个插画/PPT 协作案例：他花了约两周时间，让 AI 协助完成大量课程插图和 PPT。过程中他与 AI 反复纠偏——"颜色不对""流程不对""缺了某个东西"。

这类高频协作的痛点是：**每一次任务都像在教一个新实习生**，风格、标准、禁止项都需要从头再说一遍。Truman 想知道：能否让 AI 在项目结束时，自动把纠偏记录封装成一个可复用的 skill？

---

## What Happened

项目交付后，Truman 没有手工写总结，而是让 Cubox 扫描所有 AI 工具里的纠偏记录，自动合并同类项，输出一个名为 **"design case"** 的技能包。

整个过程分为五步：

### Step 1：标记扫描范围

让一个 AI（如 Cubox/Codex）去读其他 AI 工具的本地存储。关键前提：**这些工具的对话和反馈记录是明文存的。**

> "我说你帮我扫描12345，你帮你把别的这个工具你帮我去扫描一下它的数据库。"

### Step 2：定义输出目标

只需一句话："帮我做一个叫 design case 的技能"。

不需要定义技能格式、字段、分类——AI 自己会从纠偏记录里反推。

### Step 3：AI 自动合并同类项

AI 扫描完所有纠偏记录后，自动：

- 把所有反馈和建议**合并同类项**——"把我给他的建议合并同类项给我做一个拆分例子"（L1212）
- 提炼"出现一次我喷一次"的硬性坑为禁止项（L1218）
- 从大量沟通纠偏中抽象出可复用的规则，Truman 只需喷一段提示词（L1218）

> "告诉我把我的建议合并同类项给我做一个拆分例子。"（L1212）

### Step 4：AI 生成结构化 skill

输出包含：

| 组成部分 | 说明 |
|:--|:--|
| 使用场景 | 什么时候调用这个 skill |
| 审美底盘 | 可接受/不可接受的视觉标准 |
| 协作流程 | 先看懂参考 → 先发散再收敛 → 每轮一个主问题 |
| track list | 检查项清单，逐项打勾 |
| 评审表 | 不同类型图要考虑什么 |
| 硬性坑 | "出现一次我喷一次"→ 自动提取为禁止项 |

### Step 5：下次迭代时自吸收

下次再做图时，AI 基于这个 skill 自动执行，明显聪明很多。

> "以后下一次再做的时候，它会基于这个再去做，下一次就会明显聪明很多。"

---

## 结果

### 直接产出

1. 一个比 Truman 自己预期更完整的 **design case skill**：覆盖使用场景、审美底盘、协作流程、track list、评审表、硬性坑清单。
2. 一套 **AI 自复盘工作流**：项目结束 → 扫描纠偏记录 → 合并同类项 → 封装 skill → 下次自动加载。
3. 一次 **零人工整理** 的知识沉淀：Truman 只需喷一段提示词，AI 完成分类、抽象、结构化。

### 效果

| 指标 | 结果 |
|:--|:--|
| 沉淀时间 | 几分钟（AI 自动扫描+封装） |
| 覆盖维度 | 6 个（场景、审美、流程、track list、评审表、硬性坑） |
| 下次复用 | AI 基于 skill 自动执行，风格/标准稳定性明显提升 |
| 人的角色 | 定义扫描范围、验收 skill、继续纠偏迭代 |

---

## 可迁移场景与使用边界

| 可迁移场景 | 具体用法 | 使用边界 |
|:--|:--|:--|
| 高频重复的 AI 协作任务（插图/PPT/文案/代码） | 项目结束让 AI 扫描全部纠偏记录，生成 skill | 任务必须有可识别的重复模式；一次性创意任务不适用 |
| 把个人审美固化成 AI 可执行标准 | 把"颜色不对""流程不对"等纠偏点抽象为审美底盘+硬性坑 | 需要人能判断 AI 抽象是否准确；不能无人值守 |
| 团队新人快速复用老人经验 | 把资深成员的纠偏记录封装成团队共享 skill | 记录必须明文可读、可跨工具扫描；隐私/权限需合规 |
| KDO 卡片/内容生产的自迭代 | 让 AI 定期扫描 `60_feedback/corrections/`，自动生成新的门禁规则建议 | 反馈记录需结构化、有明确上下文；否则 AI 会过度泛化 |
| 多 Agent 协作中的经验传递 | Agent A 完成任务后自动生成 skill，Agent B 下次同类任务先加载 | 需要统一的 skill 格式和存储位置；否则各 Agent 理解不一致 |

---

## 诊断信号

出现以下信号，说明你应该启动 AI 自复盘自封装：

| 信号 | 镜头 | 追问 |
|:--|:--|:--|
| 每次做 AI 项目都要重新调 prompt，做完就丢了 | AI 自复盘——让 AI 总结这次经验变下次基础 | 你最后一次项目结束时，有没有让 AI 扫描你全程的纠偏记录、自动生成一个 skill？ |
| 我的 AI 技能库都是人手工整理的，效率很低 | 让 AI 跨工具扫描+合并同类项+封装 | 你用过哪些 AI 工具？它们的对话/反馈记录是明文存储的吗？如果是，可以直接让另一个 AI 去读。 |
| 同一个任务反复做，AI 输出质量时好时坏、风格来回横跳 | 缺少可复用的审美底盘和硬性坑清单 | 你是否有一个"做过就忘不掉"的 skill 文件，能在每次同类任务开始时自动加载审美标准和禁止项？ |

---

## 失败模式 / 常见陷阱

| 失败模式 | 真实症状 | 可执行修复 |
|:--|:--|:--|
| **扫描范围不清，封装出垃圾 skill** | AI 扫进大量无关对话，skill 里混入奇奇怪怪的规则；使用时输出风格错乱 | 指定精确关键词+时间范围+工具范围；扫描前先人工抽查 3-5 条样本 |
| **AI 抽象过度，丢失关键细节** | skill 写得像通用大道理，缺少"这个颜色不能出现""这个流程必须在前"等具体禁止项 | 要求 AI 每条规则标注来源（哪一次纠偏）；人工审核 P0 级硬性坑 |
| **封装完不加载，skill 变死文档** | 下次做同类任务还是新建对话、从零开始；skill 文件在库里吃灰 | 把 skill 写成 system prompt/自定义指令；每次同类任务先加载再对话 |
| **过早封装，样本量不足** | 只做了一次就封装 skill，结果规则过度拟合单次任务，换场景就失效 | 至少积累 2-3 次同类任务的纠偏记录再封装；首次封装后连续用 3 次验证 |
| **人不审，完全交给 AI 自封装** | skill 里出现错误归因（把人的口误当成规则）；下次 AI 按错误规则执行 | 人必须做终审：检查审美底盘、硬性坑、来源标注；对 P0 规则逐条确认 |

---

## 落地模板：AI Skill 自封装 SOP

可直接复制使用的最小流程。

### 触发条件

> 依据口述：两周密集协作 + 纠偏记录可扫描（L1204-1212）

- 你最近在某个任务上跟 AI 做了密集协作（如两周内做了大量课程插图和 PPT）（L1204-1206）
- 协作过程中有大量"颜色不对/流程不对/缺东西"式纠偏（L1208）
- AI 工具的对话/反馈记录是明文存储、可被另一个 AI 扫描（L1230）

### 执行步骤

1. **圈定扫描范围**
   - 指定要扫描哪个 AI 工具（如 Cubox/Codex）的本地存储（L1210）
   - 指定关键词/时间范围（L1230）
   - 确认记录是明文存储（L1230）

2. **运行封装提示词**

   ```markdown
   请扫描以下范围内的所有 AI 协作记录：
   - 工具：Cubox / Codex 等本地存储
   - 关键词：本次项目的全部纠偏反馈
   - 时间范围：本次项目周期

   请完成：
   1. 合并同类项：把重复出现的纠偏点归类
   2. 输出一个名为 "design case" 的 skill，包含：
      - 使用场景：什么时候调用
      - 审美底盘：可接受/不可接受的视觉标准
      - 协作流程：先看懂参考 → 先发散再收敛 → 每轮一个主问题
      - track list：检查项清单
      - 评审表：不同类型图要考虑什么
      - 硬性坑：出现一次喷一次的禁止项
   3. 每条规则标注来源：来自哪一次具体纠偏
   ```

3. **人工终审**
   - 检查 AI 抽象是否准确、是否过度泛化（L1216"比我想象中好得多"但需人把关）
   - 确认硬性坑提取正确（L1218）
   - 确认没有把无关对话混入（失败模式：扫描范围不清）

4. **下次任务加载使用**
   - 下次做同类任务时，AI 基于该 skill 自动执行（L1220）
   - "下一次就会明显聪明很多"（L1220）

---

## 互链与关联

- `case-truman-ai-skill-engineering-guide`——同源互补：本卡讲"AI 自封装流程"，那张卡讲"如何人工造出高阶 Skill 工程指南"（L1194-1218 vs 口述 L2422-2604）
- `tool-skill-packaging-eight-steps`——Skill 八步封装的方法论工具卡，与 AI 自封装流程互为补充
- `dk-three-context-formula`——三上下文公式（我是谁/项目文档/设计宪法）：本卡 AI 自封装产出的 skill 即"设计宪法"的自动生成路径
- `tool-Truman-提示词优化底层方法`——Truman 提示词优化方法论，自封装时 AI 反推格式依赖同一套底层逻辑
- `tool-Truman-AI能力分层学习路径`——AI 能力分层学习，自封装是分层学习中"经验资产化"的一环

## 8-15 口述增量补强：自封装 → 复用的闭环（YI partner）

> 来源：`00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt` L1056-1072（本次回填新增）

- **封装成 YI partner"skill 创业专家"**：把做好的 skill 封装成 YI 里的 partner，以后对那个 partner 说"我想去做一个调研的专家"（L1056-1060）
- **复用产新 skill**：对着 partner 说去知识库搜调研方法论 → 它吸收大量知识库关于调研的方法、原则、策略 → 做出一套调研 skill 文档（L1062-1066）
- **保存链路**：YAI 笔记 → Cubox → Obsidian，"全程我就是盯着那个目录在做的"，奥森的目录里就有了一套调研技能（L1068-1072）
- 这构成完整闭环：**自封装（design case）→ 沉淀为 partner → 复用产新 skill**——AI 自复盘的产出不再是一次性文档，而是可持续调用的资产

## 关键证据

- "AI 自己复盘，AI 干活，我只提供双三角模型的审美，我把活干完了，我只要喷那么一段提示词"（L1218）
- "帮我把他给我的建议合并同类项给我做一个拆分例子"（L1212）
- "比我想象中其实好的多的一个技能，包括是什么场景……包括审美的底盘，包括协作的流程……track list，他自己做了一个评审表……甚至哪些是硬性的坑"（L1216）
- "以后下一次再做的时候，它会基于这个再去做，下一次就会明显聪明很多"（L1220）
- "它善于围绕着一个主题定义好边界之后，去各个地方帮我去找我跟 AI 的协作记录，然后做一次大的拆推评算，最后变成一个更好的技能"（L1226）
- "你只要指定关键词，他都几乎都能扫的出来……他本地其实好多都是明文存的"（L1230）
- 8-15：封装成 YI partner"skill 创业专家"→ 复用产"调研专家"skill（L1056-1066）

## 教训

- **复盘 ROI 低是人的问题，不是工作的问题**："过去人做的 ROI 是很低的，因为人其实每一次的复盘成本很高"——AI 自复盘把成本压到"喷一段提示词"（L1200 / L1218）
- **及时性是第一约束**：记忆会忘、信息会随时间消失，"过了几天有些东西你真的不一定能找得回来"——项目结束当场就让 AI 扫描封装（L1224）
- **前提是明文存储**：AI 能跨工具扫描的前提是对话/反馈记录明文存在；不满足就做不了（L1230）
- **人的角色是定义边界 + 终审**：人只圈定扫描范围、验收 skill、继续纠偏；不要人肉做合并分类（L1218 / 失败模式"人不审"）
- **自封装产出要沉淀为可复用资产**：8-15 案例证明，封装成 YI partner 后能持续复用产新 skill——"经验→资产→再产经验"循环（L1056-1066）

## Sources

- `10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md`（L1194-1232 核心段落：AI 自复盘背景/design case 五步/明文存储前提）
- `00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt`（L1056-1072，8-15 新细节：YI partner 封装/复用产调研专家/保存链路）

---

*黄药师（基于 Truman 口述提取）· 2026-06-14 · 精修于 2026-06-16*
