id: case-truman-ai-skill-self-packaging
title: AI 自复盘自封装：Truman 的 design case 技能是如何让 AI 自己包装出来的
type: case
source_refs:
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
status: enriched
confidence: 0.7
domain:
- src_unknown
- src_unknown
created_at: '2026-06-14'
author: 黄药师（基于 Truman 口述提取）
reviewed_by: 老顽童
review_notes: 历史遗留，写审分离规则确立前的早期卡片。有效性由月度抽检覆盖。
review_date: '2026-06-16'
trust_level: medium
related:
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
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- framework_lens: AI自复盘——让AI总结这次经验变下次基础
  follow_up_question: 你最后一次项目结束时，有没有让AI扫描你全程的纠偏记录、自动生成一个skill？
- framework_lens: 让AI跨工具扫描+合并同类项+封装
  follow_up_question: 你用过哪些AI工具？它们的对话/反馈记录是明文存储的吗？如果是，可以直接让另一个AI去读。
- framework_lens: 缺少可复用的审美底盘和硬性坑清单
  follow_up_question: 你是否有一个"做过就忘不掉"的skill文件，能在每次同类任务开始时自动加载审美标准和禁止项？
source_context: （单一 source 为完整长文档，内容充分支撑 high trust） （单一 source，P1 收尾时从 high 降为 medium，待补充第二来源或充分验证后再升回
  high）
updated_at: '2026-06-29'
# AI 自复盘自封装：Truman 怎么让 AI 把自己包装成一个技能

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

- src_unknown
- src_unknown
- src_unknown

> "告诉我把我的建议合并同类项给我做一个拆分例子。"

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

- src_unknown
- src_unknown
- src_unknown

### 执行步骤

1. **圈定扫描范围**
   - src_unknown
   - src_unknown
   - src_unknown

2. **运行封装提示词**

   ```markdown
   请扫描以下范围内的所有 AI 协作记录：
   - src_unknown
   - src_unknown
   - src_unknown

   请完成：
   1. 合并同类项：把重复出现的纠偏点归类
   2. 输出一个名为 "______" 的 skill，包含：
      - src_unknown
      - src_unknown
      - src_unknown
      - src_unknown
      - src_unknown
      - src_unknown
   3. 每条规则标注来源：来自哪一次具体纠偏
   ```

3. **人工终审**
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

4. **下次任务加载使用**
   - src_unknown
   - src_unknown
   - src_unknown

---

## 互链与关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

---

## 关键证据

- src_unknown
- src_unknown
- src_unknown

---

## 教训

- src_unknown
- src_unknown
- src_unknown

## Sources

- src_unknown

---

*黄药师（基于 Truman 口述提取）· 2026-06-14 · 精修于 2026-06-16*
