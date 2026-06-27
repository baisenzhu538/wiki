---
id: task_20260627_laowantong-deliberate-practice-cards
type: production_task
created_at: 2026-06-27
author: 王语嫣
assignee: Hermes 老顽童
priority: P1
scope: 元能力-刻意练习素材卡片化生产
related:
  - '[[diag_20260627_wangyuyan-deliberate-practice-nine-layer]]'
  - '[[diag_20260627_wangyuyan-cross-domain-bridge-supplement]]'
  - '[[framework-ai-deliberate-practice-loop]]'
---

# Hermes 老顽童生产任务：元能力-刻意练习卡片化

> 王语嫣已完成九层深挖 + 六层交叉验证，本任务基于诊断报告 `diag_20260627_wangyuyan-deliberate-practice-nine-layer` 生成。
> 本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产卡片。

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 新建卡片 |
| 素材来源 | `00_inbox/元能力-刻意练习/` 下 4 个文件 |
| 优先级 | P1 |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | Hermes 老顽童 |
| 预计产出 | 12 张卡（4 framework + 1 concept + 3 tool + 3 case/dk + 1 AI 桥接 framework） |

---

## 1. 素材清单

| # | 文件名 | 类型 | 核心内容 |
|---|:---|:---|:---|
| 1 | `truman-刻意练习-口述.txt` | 口述逐字稿 | 1+4 模型、三环模型、20 小时定律、舒适/拉伸/恐慌区、最佳实践、反馈机制 |
| 2 | `truman-刻意练习-笔记.txt` | 结构化笔记 | 同上，已提炼为摘要 |
| 3 | `盈盈-刻意练习行动营-科学成长-口述.txt` | 口述逐字稿 | 行动营设计、AI 时代练习、乔牌/蓝军/崔磊案例 |
| 4 | `盈盈-刻意练习行动营-科学成长-笔记.txt` | 结构化笔记 | 同上，已提炼为摘要 |

---

## 2. 待生产卡片清单

### P0：核心框架与工具（3 张）

#### 2.1 `framework-yitang-deliberate-practice-1plus4`

| 字段 | 要求 |
|:---|:---|
| type | framework |
| title | 刻意练习 1+4 模型：科学成长的操作系统 |
| domain | yitang, personal-growth |
| confidence | 0.85 |
| trust_level | medium-high |
| source_refs | `00_inbox/元能力-刻意练习/truman-刻意练习-口述.txt`, `truman-刻意练习-笔记.txt` |

**内容要求**：
- 一句话：刻意练习 = 长期追求（1）+ 固定套路 + 非舒适区 + 及时反馈 + 大量重复（4）
- 画一个 1+4 结构图（可用 ASCII 或 Mermaid）
- 每个要素必须有：定义、为什么重要、典型操作、缺失时的症状
- 包含「成长速度 = 五要素乘积」公式
- When NOT to Use：生理天赋主导领域、完全无参照领域、认知负荷过高新手
- 失败模式：低水平重复、套路囤积、无反馈闭环、动机不足
- Critique：行为心理学家（意志力陷阱）、Ericsson 派（过度简化心理表征）、AI 替代论者
- related ≥ 5：链回 `yt-model-deliberate-practice-growth`、`yt-note-deliberate-practice-four-elements`、`framework-yitang-nine-layer-deep-dig`、`tool-yitang-practice-20hour-starter`、`framework-yitang-three-ring-ability-focus`

#### 2.2 `tool-yitang-practice-20hour-starter`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 20 小时刻意练习入门法：快速超过 80% 的人 |
| domain | yitang, personal-growth |
| confidence | 0.75 |
| trust_level | medium |
| source_refs | `00_inbox/元能力-刻意练习/truman-刻意练习-口述.txt`（麻将案例段落 L1926-L2058） |

**内容要求**：
- 一句话：用 20 小时把 1+4 要素凑齐，足以超过从不科学练习的大多数人
- 步骤清单（7-10 步）：选能力 → 找最佳实践 → 拆基本功 → 建口诀/SOP → 进入非舒适区 → 自我反馈 → 高频重复 → 验收
- 必须包含 Truman 打麻将案例的复盘（不要教赌博，强调方法论）
- 标注边界：20 小时是「入门/够用」，不是「成为专家」
- When NOT to Use：需要深度创造力的领域、高风险决策领域
- 失败模式：把 20 小时当成终点、跳过反馈、舒适区练习
- related ≥ 5

#### 2.3 `framework-yitang-three-ring-ability-focus`

| 字段 | 要求 |
|:---|:---|
| type | framework |
| title | 三环能力聚焦法：从 30 个能力中锁定 3 个重点 |
| domain | yitang, personal-growth |
| confidence | 0.82 |
| trust_level | medium-high |
| source_refs | `00_inbox/元能力-刻意练习/truman-刻意练习-口述.txt`（L2180-L2238） |

**内容要求**：
- 一句话：画三个圈，逼自己只选 3 个核心能力，每个再拆 3-5 子能力，最多 15 个练习点
- 三个圈：内圈人生红点能力、中圈专业能力、外圈基础能力
- 必须包含 Truman 2015 年（产品/运营/管理）和 2024 年（产品设计/商业操盘/建模）两个版本示例
- 操作步骤：列出所有能力 → 按影响前 3 年后 5 年排序 → 画三圈 → 勾出当前重点 → 贴墙可视化
- When NOT to Use：职业初期能力单一、组织强制能力要求
- related ≥ 5

---

### P1：关键概念与工具（4 张）

#### 2.4 `concept-yitang-comfort-stretch-panic-zones`

| 字段 | 要求 |
|:---|:---|
| type | concept |
| title | 练习区域分层：舒适区、拉伸区、困难区、恐慌区 |
| domain | yitang, personal-growth |
| confidence | 0.80 |
| trust_level | medium |

**内容要求**：
- 四区定义 + 每区对成长的效果
- 关键洞察：真正成长的是「暂时不会的那部分」
- Truman 习惯：用潜力做计划，常往恐慌区走一点
- 风险：恐慌区过大导致放弃
- When NOT to Use：容错率极低的场景、身心疲惫期
- related ≥ 5

#### 2.5 `tool-yitang-best-practice-as-golden-finger`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 最佳实践临摹法：早期快速提升的「金手指」 |
| domain | yitang, personal-growth |
| confidence | 0.78 |
| trust_level | medium |

**内容要求**：
- 一句话：找到领域内最好的几个案例，建模 + 临摹，第一次出手就到 60 分
- 操作步骤：找 3-5 个最佳实践 → 拆解模型 → 临摹 3 遍 → 对比差距 → 迭代
- 必须包含 Truman「一次性忘我学习法」：一晚上刷完市场最佳实践
- 边界：早期有效，后期需突破避免模仿陷阱
- related ≥ 5

#### 2.6 `tool-yitang-feedback-self-check`

| 字段 | 要求 |
|:---|:---|
| type | tool |
| title | 无导师反馈自检法：自己给自己找差距 |
| domain | yitang, personal-growth |
| confidence | 0.80 |
| trust_level | medium |

**内容要求**：
- 三种无导师反馈机制：版本对比法、最佳实践池、同伴互评
- Truman 段位图案例：把历史最好 10 张段位图放一起对比
- 操作清单：练前拍标准 → 练中录过程 → 练后做差距分析
- When NOT to Use：完全无参照标准的领域、需要安全反馈的高敏感场景
- related ≥ 5

#### 2.7 `framework-ai-deliberate-practice-loop`（跨域桥接卡）

| 字段 | 要求 |
|:---|:---|
| type | framework |
| title | AI 刻意练习闭环：把 AI 当作按需生成的练习伙伴 |
| domain | yitang, personal-growth, ai-collaboration |
| confidence | 0.78 |
| trust_level | medium |
| source_refs | `00_inbox/元能力-刻意练习/盈盈-刻意练习行动营-科学成长-口述.txt`, Ethan Mollick《The Machines of Mastery》 |

**内容要求**：
- 一句话：AI 不是替你练，而是提供无限量、可调整难度、即时反馈的练习环境，让人把精力集中在「高阶判断」。
- 闭环图：
  ```
  设定目标 → AI 生成场景/任务 → 学习者输出 → AI 反馈/评分 → AI 调整难度 → 下一轮
  ```
- 1+4 模型映射表：

| 1+4 要素 | AI 提供的功能 | 示例 |
|:---|:---|:---|
| 长期追求 | AI 帮助拆解目标、生成路径 | 「我想半年内成为商业分析师」→ 拆阶段 |
| 固定套路 | 最佳实践池、worked examples、SOP | 提供优秀提案、谈判脚本 |
| 非舒适区 | 动态难度调节、情境升级 | 谈判对手变强硬、增加利益相关方 |
| 即时反馈 | 逐句点评、错误定位、改进建议 | 代码 review、演讲逐字稿分析 |
| 大量重复 | 无限模拟、低成本重复 | 模拟客户异议 20 次 |

- 四类 AI 练习场景：谈判/沟通、写作/表达、编程/调试、决策/建模；
- When NOT to Use：完全可自动化的低阶任务、需要真实人际信任建立的能力、AI 幻觉高风险领域；
- 失败模式：把 AI 当答案库、只看不练、过度依赖导致元认知退化、不验证 AI 反馈质量；
- Critique：AI 反馈可能包含幻觉、情境不可重复、缺乏真实情绪张力；
- related ≥ 8：`framework-yitang-deliberate-practice-1plus4`, `concept-yitang-comfort-stretch-panic-zones`, `tool-yitang-feedback-self-check`, `case-yitang-ai-painting-commercialization`, `ai-collaboration-domain-digest`, `concept-candy-ai-as-collaborator`, `tool-agent-research-swarm`, `framework-multi-agent-research-architecture`。

---

### P2：案例与暗知识（3 张）

#### 2.8 `case-yitang-poker-parameterized-practice`

| 字段 | 要求 |
|:---|:---|
| type | case |
| title | 案例：德州扑克玩家乔牌如何通过参数化训练成为大使 |
| domain | yitang, personal-growth |
| confidence | 0.75 |
| trust_level | medium |
| source_refs | `00_inbox/元能力-刻意练习/盈盈-刻意练习行动营-科学成长-口述.txt`, `笔记.txt` |

**内容要求**：
- 叙事完整度：背景 → 关键数字（4 参数 → 20 参数 → 100 参数；同时开 8 桌） → 关键决策 → 结果
- 刻意练习要素映射：固定套路（参数模型）、非舒适区（加参数）、反馈（胜率数据）、重复（大量对局）
- 失败/成功原因分析
- related ≥ 5

#### 2.9 `case-yitang-sales-routine-deconstruction`

| 字段 | 要求 |
|:---|:---|
| type | case |
| title | 案例：社恐销售蓝军如何通过拆解销冠套路半年成亚军 |
| domain | yitang, personal-growth, sales |
| confidence | 0.75 |
| trust_level | medium |

**内容要求**：
- 叙事完整度：背景（社恐） → 方法（拆解销冠话术） → 关键数字（每天 50-60 通） → 结果（半年亚军，后进腾讯）
- 刻意练习要素映射
- 迁移价值：销冠套路拆解法可复用到其他能力
- related ≥ 5

#### 2.10 `case-yitang-ai-painting-commercialization`

| 字段 | 要求 |
|:---|:---|
| type | case |
| title | 案例：崔磊如何通过 AI 绘画练习实现商业化交付 |
| domain | yitang, personal-growth, ai-collaboration |
| confidence | 0.72 |
| trust_level | medium |

**内容要求**：
- 叙事完整度：背景 → 方法（大量出图 + 最佳实践池 + 提示词积累） → 关键数字（远超 200 张） → 结果（承接设计项目）
- AI 时代刻意练习典型案例
- related ≥ 5

#### 2.11 `dk-yitang-deliberate-practice-common-traps`

| 字段 | 要求 |
|:---|:---|
| type | dk |
| title | 刻意练习常见陷阱：老学员最容易踩的 7 个坑 |
| domain | yitang, personal-growth |
| confidence | 0.80 |
| trust_level | medium-high |

**内容要求**：
- 7 个坑：低水平重复、被 1 万小时吓退、套路囤积、无反馈闭环、动机不足、非舒适区过大、带人无章法
- 每个坑：症状 → 根因 → 修复动作
- related ≥ 5

---

## 3. 生产规范

### 3.1 每张卡必须包含

```yaml
---
id: <严格匹配文件名>
type: <framework/tool/concept/case/dk>
title: <一句话标题>
status: enriched
domain:
  - yitang
  - personal-growth
confidence: <按诊断要求>
trust_level: <按诊断要求>
author: 老顽童
reviewed_by: pending
source_refs:
  - <具体文件路径>
related:
  - '[[xxx]]'
  - ...
---
```

### 3.2 内容结构要求

| type | 必须段落 |
|:---|:---|
| framework | 一句话定义、核心结构图、操作步骤、When NOT to Use、失败模式、Critique、related |
| tool | Burn line、一句话、操作步骤、典型场景、When NOT to Use、失败模式、related |
| concept | 定义、为什么重要、关键维度、边界、常见误解、related |
| case | 背景、关键数字、关键决策、结果、成功/失败原因、刻意练习要素映射、related |
| dk | 使用场景、N 条洞见、每条附症状/修复、边界、related |

### 3.3 质量标准

1. **不要直接复制笔记**：要用九层深挖后的深度结构重新组织。
2. **source_refs 必须真实存在**：指向 `00_inbox/元能力-刻意练习/` 下的具体文件。
3. **confidence 严格按诊断要求**：不要全部写 0.85。
4. **related ≥ 5**，至少 1 个跨域链接。
5. **跨域桥接卡**（2.7 `framework-ai-deliberate-practice-loop`）要求 `related ≥ 8`，必须同时链回刻意练习核心卡与 AI 协作域核心卡。
6. **必须跑 `kdo pre-submit`**，粘贴输出到汇报中。
7. **不要使用旧版四要素模型覆盖新版 1+4 模型**：旧卡可以 related，但不要合并内容。
8. **AI 协作桥接卡不是概念随笔**：必须有闭环图、1+4 映射表、场景清单、失败模式、Critique。

---

## 4. 提交与验收

### 4.1 提交格式

老顽童完成后，按以下格式汇报：

```markdown
## 刻意练习卡片生产完成汇报

### 产出清单
| 卡片 | 类型 | 状态 |
|:---|:---|:---|
| framework-yitang-deliberate-practice-1plus4 | framework | enriched |
| ... | ... | ... |

### pre-submit 输出
```text
[粘贴 kdo pre-submit 输出]
```

### 需要王语嫣重点审查的项
- ...
```

### 4.2 验收流程

1. 王语嫣跑 `kdo pre-submit` 全量复核；
2. 王语嫣按九层深挖标准抽检 3-5 张卡；
3. 问题整改后，提交欧阳锋终审 P0 卡；
4. P1/P2 卡由王语嫣终审后入库。

---

## 5. 注意事项

- 本任务不修改旧卡，只新建；
- 若发现素材中有矛盾或不清晰处，先按最合理理解生产，并在卡片中用 `[conf=X, source=...]` 标注不确定性；
- 不要在 case 卡中宣扬赌博/麻将技巧，重点在方法论；
- 20 小时定律必须标注边界，避免用户误解为「20 小时成专家」。

---

## 刻意练习卡片生产完成汇报

> 生产人：老顽童（Kimi 实例）
> 完成时间：2026-06-27
> 任务状态：pending_review

### 产出清单

| 卡片 | 类型 | 状态 | 路径 |
|:---|:---|:---|:---|
| framework-yitang-deliberate-practice-1plus4 | framework | enriched | 30_wiki/frameworks/framework-yitang-deliberate-practice-1plus4.md |
| tool-yitang-practice-20hour-starter | tool | enriched | 30_wiki/tools/tool-yitang-practice-20hour-starter.md |
| framework-yitang-three-ring-ability-focus | framework | enriched | 30_wiki/frameworks/framework-yitang-three-ring-ability-focus.md |
| concept-yitang-comfort-stretch-panic-zones | concept | enriched | 30_wiki/concepts/concept-yitang-comfort-stretch-panic-zones.md |
| tool-yitang-best-practice-as-golden-finger | tool | enriched | 30_wiki/tools/tool-yitang-best-practice-as-golden-finger.md |
| tool-yitang-feedback-self-check | tool | enriched | 30_wiki/tools/tool-yitang-feedback-self-check.md |
| framework-ai-deliberate-practice-loop | framework | enriched | 30_wiki/frameworks/framework-ai-deliberate-practice-loop.md |
| case-yitang-poker-parameterized-practice | case | enriched | 30_wiki/cases/case-yitang-poker-parameterized-practice.md |
| case-yitang-sales-routine-deconstruction | case | enriched | 30_wiki/cases/case-yitang-sales-routine-deconstruction.md |
| case-yitang-ai-painting-commercialization | case | enriched | 30_wiki/cases/case-yitang-ai-painting-commercialization.md |
| dk-yitang-deliberate-practice-common-traps | dk | enriched | 30_wiki/dk/dk-yitang-deliberate-practice-common-traps.md |

**实际产出：11 张卡**（任务单预计 12 张，因 `concept-yitang-ai-era-deliberate-practice` 已按跨域桥接补深挖诊断升级为 `framework-ai-deliberate-practice-loop`，未单独建 concept 卡）。

### pre-submit 输出

```text
====================================================================
  Pre-Submit Gate Report
====================================================================
  Files checked: 11
  Passed:        11
  Failed:        0

  All gates passed. Ready for human review.
```

### 自攻击报告

已对 4 张核心卡执行四路对抗攻击，报告位于 `60_feedback/adversarial/`：

- `atk_framework-yitang-deliberate-practice-1plus4_2026-06-27.md`
- `atk_tool-yitang-practice-20hour-starter_2026-06-27.md`
- `atk_framework-yitang-three-ring-ability-focus_2026-06-27.md`
- `atk_framework-ai-deliberate-practice-loop_2026-06-27.md`

攻击结果：无 🔴 致命问题；🟡 严重问题已修复或已通过标注/降 confidence 降低风险；全部卡片重新通过 pre-submit。

### 需要王语嫣/欧阳锋重点审查的项

1. **framework-yitang-deliberate-practice-1plus4**：
   - "长期追求"在结构图中是前提，在公式中作为乘数出现，虽已加注说明，但仍需确认表述是否清晰无歧义。
   - 学术文献（Ericsson 1993/2016、Yerkes-Dodson 1908）已加入 source_refs，请确认引用格式是否符合 KDO 规范。

2. **tool-yitang-practice-20hour-starter**：
   - "20 小时超过 80% 的人"已弱化为"20 小时达到 good enough/够用水平"，请确认是否与诊断报告要求一致。
   - 麻将案例已严格按方法论视角处理，未宣扬赌博技巧，请抽检。

3. **framework-yitang-three-ring-ability-focus**：
   - 三环圈层定义（内圈人生红点、中圈专业、外圈基础）与 Truman 原意是否完全对齐，特别是"管理属于外圈保下限"的表述。
   - 新增评分表模板是否可操作，请审。

4. **framework-ai-deliberate-practice-loop**：
   - 桥接卡 related=10，请确认是否满足"复杂桥接 ≥8"且跨域链接足够深。
   - 引用的 2024 年 AI 教育预印本（Wang et al. / Guo et al.）请确认可接受性；如不达标，需替换为更权威来源。

5. **case 卡数字标注**：
   - 乔牌、蓝军、崔磊案例中的关键数字均已按 `[conf=X, source=...]` 标注，请抽检置信度设置是否合理。

---

*任务下达：王语嫣 | 日期：2026-06-27*
*生产完成：老顽童（Kimi） | 日期：2026-06-27*
