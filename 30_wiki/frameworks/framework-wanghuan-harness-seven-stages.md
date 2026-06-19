---
id: framework-wanghuan-harness-seven-stages
title: '王欢：Harness 七阶段 AI 构建流程'
type: framework
status: enriched
author: 王语嫣
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享（2026-06-18 授课）
source_refs:
- '00_inbox/王欢AI实践心法/王欢-AI实战分享-harness的七个阶段-示意图_vlm_desc.md'
- '10_raw/sources/src_20260619_1ffb2cef_wanghuan_harness的七个阶段_示意图.md'
- '10_raw/sources/src_20260619_2b457485_wanghuan_harness的七个阶段_示意图_ocr.md'
- '10_raw/sources/src_20260619_e4b35a3a_wanghuan_task_product_system_transcript.md'
domain:
- human-ai-collaboration
- ai-collaboration
- yitang
created_at: '2026-06-19'
updated_at: '2026-06-19'
related:
- '[[framework-wanghuan-five-criteria-first-product]]'
- '[[framework-wanghuan-task-product-system]]'
- '[[framework-wanghuan-bitcoe-prompt-framework]]'
- '[[concept-wanghuan-power-of-standards]]'
- '[[concept-wanghuan-flywheel-first-loop]]'
- '[[case-wanghuan-yiyu-qingji-medical-notes]]'
- '[[tool-wanghuan-ai-dual-role-coach]]'
diagnostic_signals:
- signal: 'AI 写出的代码能跑，但连续三次返工都是因为边界没对齐或审美不一致'
  lens: '缺规划 / 缺验收门控'
  follow_up: '引入 Harness Phase 1 产品规划与 Phase 5.5 Polish Sprint，把 spec 和审美标准书面化'
- signal: '项目做到一半发现技术栈想换就换，依赖越加越多，回滚困难'
  lens: '技术栈决策缺失或延迟'
  follow_up: '在 Phase 1.5 强制锁定 tech-stack.md，未列出的顶层依赖不得引入'
- signal: '每次 AI 生成后都靠“肉眼扫一遍”判断是否可用，没有评分维度'
  lens: 'Eval 维度与标准缺失'
  follow_up: '设计 4 个 Evaluator，明确“无维度低于 3 分、加权平均 ≥4.0、零 CRITICAL”的通过条件'
- signal: '交付时 README 跑不通、版本历史丢失、无法向他人解释为什么这么改'
  lens: 'Ship Pipeline 缺失'
  follow_up: '执行 Phase 6 四步门控：审美评分 → 文档生成 → Fresh Clone Test → Audit Trail'
tags:
- 王欢
- Harness
- AI 构建
- 软件工程
- 质量门控
- 导演思维
---

# 王欢：Harness 七阶段 AI 构建流程

> **Burn line**: 把一次 AI 软件构建切成七个严格阶段，每一阶段都有明确输入、输出和质量门控，让“导演”定义标准、AI 执行、人来验收。
>
> **来源**：王欢 AI 实战分享（2026-06-18）；Harness 七阶段示意图 VLM 描述与 OCR 交叉验证。

---

## 用一句话讲清楚

Harness 是一套把 AI 软件构建从“想到哪做到哪”变成“分阶段导演式交付”的工程流程：**先规划、后选型、再 Sprint 对抗迭代、审美精修、最终通过四门门控交付**。

---

## 核心要点

1. **Phase 0 — 初始化 & 预检**
   创建 `.harness/` 工作目录，检测 CLI 工具，生成 `budget.yml`（默认 50 轮迭代、8 个 Sprint、4 小时墙时），并自动检测是否需要从 checkpoint 恢复。目标是让构建环境可复现、成本可预算。

2. **Phase 1 — Planner 产品规划（Opus 模型）**
   用最强推理模型做一次深度产品规划，且**只跑一次**以控制成本。输出 `product-spec.md`：功能优先级、审美方向、迭代计划，并显式标出所有高风险歧义，留待后续解决。

3. **Phase 1.5 — Tech Stack Selector 技术栈选型（Opus 模型）**
   Planner 结束后立即确定技术栈，输出 `tech-stack.md`：语言、框架、测试工具、构建工具、部署目标及选型理由。核心规则：**Generator 不得自行引入未列出的顶层依赖**，防止做到一半随意堆栈。

4. **Phase 2–5 — Sprint 对抗循环**
   每轮 Sprint 的标准流程：写 Sprint Contract → 启动 Workflow → Generator 构建 → 四个 Evaluator 并行评分 → 决策引擎判断继续、修复还是裁剪范围。
   - 通过条件：没有维度低于 3 分；加权平均 ≥ 4.0 分（取两名代码审查者中更严者）；零 CRITICAL 对抗发现。

5. **Phase 5.5 — Polish Sprint 审美精修**
   所有 PO 功能完成后，自动插入一轮 Polish Sprint：空状态、错误状态、加载动画、字体节奏、微交互。评分权重切换——审美维度上调到 3，功能维度下调到 1，避免“功能能跑但看起来廉价”。

6. **Phase 6 — Ship Pipeline 最终交付**
   顺序执行，每步互为门控：
   1. **Aesthetic Reviewer（Opus）**：整体审美评分 ≥ 4.0 才过。
   2. **文档生成器**：写 README + CHANGELOG + KNOWN_LIMITATIONS 并提交。
   3. **Fresh Clone Tester**：从零克隆，按 README 操作，确认真的能跑。
   4. **Audit Trail**：生成从 spec 到 ship 的完整旅程记录。

7. **导演思维是底层操作系统**
   Harness 不是让 AI 替人写代码，而是让人定义目标、标准与验收，AI 负责执行与迭代。中间那段执行，人不再亲自做。

---

## 边界

| 适用 | 不适用 |
|:---|:---|
| 需要多轮迭代、多人/多 AI 协作的软件或原型构建 | 一次性、几行代码就能解决的临时脚本 |
| 交付物有明确功能、审美、文档与可运行标准 | 探索性、尚无“好/坏”标准的艺术创作初期 |
| 团队已经接受过“演员→导演”身份切换 | 仍把 AI 当“更快的自己”、不愿放手执行环节 |
| 成本/时间可预算，需要 Audit Trail 与可复现性 | 快速演示、不在乎回滚与版本追溯的草图 |
| 多模块、多依赖、需要技术栈锁定的工程 | 单文件、无外部依赖的极简工具 |

---

## 失败模式 / 常见走偏

| 走偏模式 | 表现 | 纠偏动作 |
|:---|:---|:---|
| **跳过 Phase 1 直接开写** | AI 边做边改，需求反复漂移，返工 3 倍以上 | 强制先出 `product-spec.md`，未书面化的高风险歧义不得进入 Sprint |
| **技术栈边做边换** | 第 3 个 Sprint 突然引入新框架，依赖爆炸 | 在 Phase 1.5 锁定 `tech-stack.md`，新增顶层依赖需回到规划阶段审批 |
| **只有功能 Eval，没有审美 Eval** | 功能全绿，界面却像“实习生作品” | Phase 5.5 上调审美权重，Phase 6 用 Opus 做 Aesthetic Reviewer |
| **把“能跑”当“能交付”** | README 缺失，别人 clone 后跑不起来 | 必须通过 Fresh Clone Tester：从零按 README 操作，真跑通才算过 |
| ** Evaluator 评分放水** | 所有维度 4 分以上，但用户一看就不对 | 取两名审查者中更严者，设置“无维度低于 3 分”的硬门槛 |
| **Ship 阶段才补文档** | CHANGELOG 与 KNOWN_LIMITATIONS 流于形式 | 文档生成器作为门控步骤，未提交则阻止交付 |

---

## 行动 Checklist

- [ ] 建立 `.harness/` 目录，写入 `budget.yml`：总迭代数、Sprint 数、墙时上限、checkpoint 策略。
- [ ] 用最强推理模型跑 Phase 1，输出 `product-spec.md`，列出功能优先级、审美方向、迭代计划和高风险歧义。
- [ ] 在 Phase 1.5 输出 `tech-stack.md`，明确语言、框架、测试/构建/部署工具及选型理由，并写上“Generator 不得自行引入未列出的顶层依赖”。
- [ ] 为 Phase 2–5 设计 4 个 Evaluator，定义评分维度与通过阈值（无维度 < 3、加权平均 ≥ 4.0、零 CRITICAL）。
- [ ] 跑通至少一轮完整 Sprint：Contract → Workflow → Generator → Evaluators → 决策引擎（继续/修复/裁剪）。
- [ ] 所有 PO 功能完成后进入 Phase 5.5，专门优化空状态、错误状态、加载、字体节奏与微交互。
- [ ] 执行 Phase 6 Ship Pipeline：Aesthetic Reviewer ≥ 4.0 → 文档生成 → Fresh Clone Test → Audit Trail。
- [ ] 交付后复盘：哪些标准有效？哪些 Evaluator 放水？把改进写回 `product-spec.md` 与评估规则。

---

## 相关卡 / 互链

- [[framework-wanghuan-five-criteria-first-product]]：选题过关后，才值得用 Harness 七阶段推进到交付。
- [[framework-wanghuan-task-product-system]]：Harness 是“任务→产品→系统”跃迁在软件工程上的具体落地形态。
- [[framework-wanghuan-bitcoe-prompt-framework]]：Planner、Sprint Contract 与 Evaluator 都需要 BTICOE 消灭模糊。
- [[concept-wanghuan-power-of-standards]]：Harness 的评分阈值、技术栈锁定、Ship 门控都是“标准是乘数”的工程化体现。
- [[concept-wanghuan-flywheel-first-loop]]：Harness 的第一圈通常最慢，但每一圈的 spec、Evaluator、文档都会成为下一圈的资产。
- [[case-wanghuan-yiyu-qingji-medical-notes]]：医语轻记式的小产品若要工程化放大，可用 Harness 管理多轮迭代与交付质量。
- [[tool-wanghuan-ai-dual-role-coach]]：对练系统中的“AI 家长 + AI 教练”双 Evaluator 思想，与 Harness 的多 Evaluator 对抗循环同源。

---

## Critique

**攻击者 1：快速交付派（Move Fast & Break Things）**
> “七个阶段、四门门控，会让一个原型的交付从几小时拖到几天。AI 编程的核心价值就是快， Harness 太重，扼杀速度。”

**回应**：Harness 的“重”是为了防止“快但不可维护”的伪交付。王欢在课堂上强调：Director 的习惯是“先让它跑起来，再找问题”，但找到问题后必须留下可复现、可审计的轨迹。对于真正的 MVP，可以压缩 Sprint 数量、降低评分维度，但“规划 → 验收 → 文档 → 可运行”四门门控不能全删，否则只是重复了“演员思维”的即兴编码。

**攻击者 2：模型能力乐观派**
> “下一代模型（如更强的代码生成模型）会自动处理审美、文档和依赖管理，Harness 这种人工门控很快会过时。”

**回应**：模型能力越强，对“好标准”的依赖反而越高。没有清晰标准的强力模型，只会更快地产出平庸或偏离意图的结果。Harness 的真正资产不是门控本身，而是被书面化的产品规格、审美标准、技术栈约束与 Eval 维度；这些标准只会随模型升级而升值，不会贬值。

**攻击者 3：非技术背景执行者**
> “Harness 明显是为软件工程设计的，我一个做销售/运营/内容的人根本用不上。”

**回应**：Harness 的七阶段可以抽象为“预算 → 规划 → 规则锁定 → 对抗迭代 → 精修 → 交付门控”的通用工作流。非技术场景可以去掉代码相关的文件名和 Evaluator，但“先定标准、再让 AI 执行、最后多维度验收”的逻辑同样适用于海报生成、销售话术、课程大纲等产品的工程化。

**不要用**
- 不要把它当成“所有 AI 项目都必须走满七阶段”的刚性流程。探索性草图、一次性任务、个人临时脚本可以只取其中 1–2 个阶段。
- 不要在标准和 Evaluator 还没想清楚时，就急着把流程“自动化”。门控多了但标准模糊，只会把错误放大并流程化。
- 不要把它当作“人可以完全甩手”的借口。Harness 的每个关键决策点（继续/修复/裁剪/交付）仍需人来拍板。

---

## Synthesis

Harness 七阶段是王欢“导演思维”在软件工程上的具体蓝图。它把一次 AI 构建从“让 AI 帮我写代码”的线性执行，改造成“人定义标准、AI 执行、多 Evaluator 对抗、多门控验收”的闭环系统。核心收益不是速度，而是可复现、可审计、可迭代：Phase 0 的预算让人对成本有数，Phase 1 的 `product-spec.md` 让模糊需求显形，Phase 1.5 的 `tech-stack.md` 防止后期堆栈失控，Phase 2–5 的 Sprint 对抗循环把“我觉得还行”变成“维度评分 ≥ 4.0”，Phase 5.5 的审美精修和 Phase 6 的 Ship Pipeline 则确保交付物不仅“能跑”，而且“能看、能用、能交、能维护”。

这套流程与 [[framework-wanghuan-task-product-system]]、[[framework-wanghuan-five-criteria-first-product]]、[[concept-wanghuan-power-of-standards]] 共同构成一个从选题到交付的完整系统：先用五条标准选对第一个真实场景，再用 BTICOE 把任务固化为可复用产品，最后用 Harness 七阶段把产品稳定地推进到可交付状态。它的边界也很清楚——适用于有明确验收标准、需要多轮迭代的工程化产品，不适用于一次性任务或探索性草图。判断你是否需要 Harness 的最简单问题：这个东西下周、下个月还会被打开和迭代吗？如果答案是肯定的，那么从 Phase 0 开始建立工作目录和预算，就是值得的。

---

*基于王欢 2026-06-18 AI 实战分享整理，经欧阳锋审核。*
