---
id: case-252-quality-gate-pilot
title: "#252 消费端协议试点：用Feature思维分析卡片质量门禁体系"
type: case
status: draft
domain:
  - ai-basic
  - kdo
author: AI基本功教练
reviewed_by: 欧阳锋
review_date: 2026-08-09
confidence: 0.9
trust_level: observed
source_refs:
  - 10_raw/sources/feature-periodic-table-v0.8.json
  - cap_hub/features.json
  - 30_wiki/bridges/bridge-dual-track-feature-system.md
  - 30_wiki/dark-knowledges/dk-c8-format-complete-mind-empty.md
related:
  - '[[bridge-dual-track-feature-system]]'
  - '[[dk-agent-access-kdo-pitfalls]]'
  - '[[dk-c8-format-complete-mind-empty]]'
  - '[[agent-spec-basic-skills-coach]]'
created_at: 2026-08-09
updated_at: 2026-08-09
tags:
  - audience:general
  - scene:reference
  - skill-level:intermediate
  - method:feature-thinking
aliases:
  - #252
  - 消费端试点
  - quality-gate-pilot
discoverable_by:
  - #252
  - 消费端试点
  - quality-gate-pilot
---

# #252 消费端协议试点：Feature思维 × 质量门禁体系

> 一句话：用周期表随机点的 5 个 Feature 作为关键假设分析 KDO 质量门禁体系，验证"Feature 不是学会的是用会的"——5 个 Feature 中 3 个有效、1 个部分有效、1 个边界无效，全部回填周期表 JSON。

## 一、点菜结果（关键假设）

| ID | Feature | 层 | 维度 | 假设用途 |
|----|---------|----|----|---------|
| F080 | 持续推Goal | L4 | D | 门禁体系是否=目标推进机制 |
| F022 | 反向教我 | L2 | A | 门禁是否含教学反馈 |
| F085 | 能力分工 | L5 | A | 双轨体系是否=能力分工 |
| F039 | CoV视觉链式思考 | L2 | D | 门禁是否需要视觉推理 |
| F081 | 主动汇报 | L4 | D | 门禁报告机制是否=主动汇报 |

## 二、分析：5 Feature × 质量门禁体系

### F085 能力分工 → ✅ 高度有效（双轨体系的本质）

- **假设**：门禁体系=按角色分配建设职责
- **验证**：`bridge-dual-track-feature-system` 明确双轨——quality-gate轨（生产者/审查者，12-13 lint）vs capability轨（AI使用者，100 Feature），**按角色分工，互不混编**
- **结论**：F085 完美命中双轨设计的灵魂——"混编=拿lint规则当解题武器"正是能力分工缺失的后果

### F080 持续推Goal → ✅ 有效（门禁=目标推进机制）

- **假设**：门禁体系是否=Agent持续朝"卡片合格"目标推进
- **验证**：CARD_CHECKLIST（提交前逐项自检）+ REVIEW_MARK（终审标记）——两把锁确保生产Agent不偏离"可合并"目标；欧阳锋审查流防虚假完成
- **结论**：门禁就是"持续推Goal"的机制化——把"我觉得齐了"替换为"脚本输出全PASS"

### F081 主动汇报 → ✅ 有效（门禁=汇报机制）

- **假设**：门禁报告机制=Agent主动汇报
- **验证**：lint 的 PASS/FAIL 报告 + REVIEW_MARK 审查结果写回卡片 + kdo pre-submit 门禁栈逐道拦截——每一步都有状态通知
- **结论**：门禁体系的"检查→报告→标记"循环即主动汇报的自动化形态

### F022 反向教我 → 🔶 部分有效（HINT_MAP 是雏形）

- **假设**：门禁是否含"AI教你用法"的反馈
- **验证**：HINT_MAP Feature（ux类）——每条lint错误追加场景化修复提示，从编译器风格升级为教练风格
- **结论**：门禁有"教学化"趋势，但仅限错误提示——未到"主动教你门禁怎么用"的完整反向教我

### F039 CoV视觉链式思考 → ❌ 边界无效（门禁是确定性检查）

- **假设**：门禁是否需要视觉链式推理
- **验证**：门禁13项全是确定性 lint/cli/ux 检查——updated_at、死链、重复ID，无一需要视觉推理
- **结论**：**跨域无效**——CoV属于"图表/设计"场景（L2-D），门禁是"卡片健康度"场景（确定性检查）。这个"无效"本身就是有效发现：Feature 的场景绑定必须尊重

## 三、复盘：对照 08-09 分析

| 维度 | 08-09 分析（L0-L5归类） | 本次分析（Feature假设验证） | 增量 |
|------|------------------------|---------------------------|------|
| 门禁的 lint 层 | ≈L0/L1 机器硬规则 | F080 持续推Goal 命中 | 门禁=目标推进机制的机制化表达 |
| 欧阳锋审查流 | ≈L2/L3 人+AI流程 | F081 主动汇报 命中 | 报告循环=主动汇报自动化 |
| 双轨体系 | 提到不混编 | F085 能力分工 命中 | 双轨=能力分工的制度化 |
| 理解盲区 dk-C8 | 提到需抽检 | F022 部分命中 HINT_MAP | 教学化是门禁演进方向 |
| —（未覆盖） | — | F039 边界无效 | Feature场景绑定必须尊重 |

**复盘结论**：
1. **有效的 3 个**（F080/F081/F085）都指向同一件事：**质量门禁体系是"多角色协作朝卡片合格目标推进"的系统**——分工、推目标、汇报三要素齐备
2. **部分有效 1 个**（F022）：门禁的教学化（HINT_MAP）是真实存在但未完整的演进方向
3. **边界无效 1 个**（F039）：跨场景 Feature 不该硬套——"无效"也是验证成果
4. 08-09 的 L0-L5 归类分析与本次 Feature 假设验证**互补不冲突**：前者是结构视角，后者是功能假设视角

## 四、回填记录

- 周期表：`10_raw/sources/feature-periodic-table-v0.8.json`
- 回填 5 个 Feature：`verified=true` + `case_ref=case-252-quality-gate-pilot`
- 全局 verified 数：20/100 → **25/100**（试点贡献 +5）
- 回填字段：id/name/layer/dimension/purpose/scenario/case_ref/verified/verify_note

## 五、消费端协议 v0.1（点菜→调优→沉淀）

> 协议目的：把"Feature 不是学会的是用会的"从理念变成可复用流程——以后任何任务按此三步闭环。

### 步骤 1：点菜（假设生成）
- 命令：`python3 kdo-tools/feature_menu.py pick --n 5`
- 产出：5 个 Feature 作为关键假设（含 layer/dimension/purpose）
- 原则：**随机点菜不挑食**——让 Feature 的适用性被真实场景检验，不预筛

### 步骤 2：调优（验证执行）
- 对每个 Feature 执行：假设 → 对照真实任务 → 有效/部分/无效判定
- 产出：每 Feature 一个"验证结论 + 证据链（卡片/命令路径）"
- 原则：**无效也是结果**——跨场景无效的 Feature 标记边界，不硬套

### 步骤 3：沉淀（回填+注册）
- 回填：`verified=true` + `case_ref=<case-id>` + `verify_note` 写回周期表 JSON
- 注册：验证结论形成 case 卡（如本卡），挂相关链
- 原则：**一任务一回填**——每跑一个真实任务，周期表就多几个"被验证过的菜单项"

### 验收标准
- [x] 五步闭环有记录（本卡）
- [x] JSON ≥5 个 Feature 被真实任务回填（本次 +5）
- [ ] 协议 v0.1 欧阳锋审

## 六、试点意义

- **制度性验证**：周期表从"100 个条目"变成"被真实任务验证过的菜单"
- **协议可复用**：#252 产出 = 以后任何任务点菜→调优→沉淀
- **触发注册链**：试点通过 → cap_hub 注册 agent → 教练正式入编能力中台
