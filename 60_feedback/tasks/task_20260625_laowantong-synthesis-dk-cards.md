# 老顽童任务指令：三域跨案例合成 dk 卡生产（王语嫣）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产卡片。
> 触发来源：strategy / research / yitang 三域 case 卡数量达到阈值，自动触发跨案例合成任务。
> 王语嫣已完成三域合成报告，老顽童据此生产 9 张 dk 卡。

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务来源 | 自动触发的跨案例合成任务 |
| 合成报告 | `60_feedback/audit/synthesis_strategy.md`、`synthesis_research.md`、`synthesis_yitang.md` |
| 反馈日期 | 2026-06-25 |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | 老顽童 |
| 优先级 | P2（在 AI 2041 P0 完成后执行，或与 AI 2041 P1 并行） |

---

## 1. 必须生产的 9 张 dk 卡

### 1.1 strategy 域（3 张）

| id | 标题 | 来源洞察 | 核心要求 |
|:---|:---|:---|:---|
| `dk-strategy-stage-leverage-mismatch` | 战略阶段与杠杆错配 | strategy 合成报告 洞察 1 | 识别生命周期阶段、阶段转换信号、各阶段应追求的杠杆 |
| `dk-strategy-correlation-vs-causation-leverage` | 相关指标 vs 因果抓手 | strategy 合成报告 洞察 2 | 在业务公式中识别真正的因果杠杆，避免平均用力 |
| `dk-strategy-organization-strategy-mismatch` | 组织能力与战略方向不匹配 | strategy 合成报告 洞察 3 | 战略方向与组织承载力的同步诊断清单 |

### 1.2 research 域（3 张）

| id | 标题 | 来源洞察 | 核心要求 |
|:---|:---|:---|:---|
| `dk-research-identity-craft-for-closed-information` | 为获取封闭情报设计合法身份 | research 合成报告 洞察 1 | 身份设计 checklist、伦理边界、退出策略 |
| `dk-research-triangulation-stop-rule` | 多源交叉验证的停止规则 | research 合成报告 洞察 2 | 验证成本-置信度权衡、何时停止验证 |
| `dk-research-decision-first-mapping` | 研究活动如何服务决策 | research 合成报告 洞察 3 | 研究动作 → 决策 → 假设 → 通过标准的映射表 |

### 1.3 yitang 域（3 张）

| id | 标题 | 来源洞察 | 核心要求 |
|:---|:---|:---|:---|
| `dk-yitang-behavior-over-asking` | 调研中行为证据重于口头证据 | yitang 合成报告 洞察 1 | 观察法 + JTBD 组合 SOP、远程访谈还原现场语境 |
| `dk-yitang-business-model-risk-over-product-risk` | 商业模式错误比产品错误更致命 | yitang 合成报告 洞察 2 | 定性调研结论 → 单元模型调整的映射模板 |
| `dk-yitang-model-asset-capitalization` | 组织级模型资产的盘点、定价与迭代 | yitang 合成报告 洞察 3 | 周对周迭代、定价飞轮、AI 盘点、雷达图评选机制 |

---

## 2. dk 卡统一内容要求

每张 dk 卡必须包含：

1. **一句话定义**：用 1 句话说明这个暗知识解决什么问题。
2. **模式描述**：2-3 段，说明这是什么模式、为什么重要、在什么情况下出现。
3. **支撑案例**：3-5 个，必须带 `[[case-xxx]]` 双向链接，并简要说明每个案例如何支持该模式。
4. **与现有框架的关系**：
   - 列出 2-3 张已覆盖部分内容的 framework/tool 卡；
   - 明确说明现有框架未覆盖的缺口（这是 dk 卡存在的理由）。
5. **预警信号**：≥3 条，帮助读者识别自己是否正在陷入该模式。
6. **可迁移场景**：2-3 个，说明在哪些其他领域/情境下也适用。
7. **行动建议**：1-2 条，读者今晚就能执行的步骤。

---

## 3. Frontmatter 规范

```yaml
---
id: dk-strategy-stage-leverage-mismatch
title: 战略阶段与杠杆错配
type: dk
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.80
trust_level: medium
language: zh-CN
domain:
- strategy
source_refs:
- 60_feedback/audit/synthesis_strategy.md
related:
- "[[framework-strategy-six-stages]]"
- "[[framework-strategy-brm]]"
- "[[tool-strategy-nine-problems]]"
- "[[case-strategy-failure-02-supermarket]]"
- "[[case-lean-premature-expansion]]"
---
```

**source_refs 必须精确到合成报告文件**。

**related 必须 ≥ 5**：包含相关 framework/tool 卡和支撑 case 卡。

---

## 4. 执行顺序

建议按域分批生产，每完成一个域通知王语嫣抽样：

1. `dk-strategy-stage-leverage-mismatch`
2. `dk-strategy-correlation-vs-causation-leverage`
3. `dk-strategy-organization-strategy-mismatch`
4. `dk-research-identity-craft-for-closed-information`
5. `dk-research-triangulation-stop-rule`
6. `dk-research-decision-first-mapping`
7. `dk-yitang-behavior-over-asking`
8. `dk-yitang-business-model-risk-over-product-risk`
9. `dk-yitang-model-asset-capitalization`

---

## 5. 质量门禁

每张 dk 卡完成后必须自查：

- [ ] `id` 与文件名一致
- [ ] `status` = `enriched`
- [ ] `author` = `老顽童`
- [ ] `reviewed_by` ≠ author
- [ ] `source_refs` 指向对应合成报告
- [ ] `related ≥ 5` 个有效双向链接
- [ ] 包含支撑案例（≥3 个 `[[case-xxx]]`）
- [ ] 包含预警信号（≥3 条）
- [ ] 包含可迁移场景
- [ ] 明确说明现有框架未覆盖的缺口
- [ ] 跑 `kdo lint` 无致命错误
- [ ] YAML 解析通过

---

## 6. 验收标准

王语嫣验收时检查：
1. 9 张 dk 卡是否全部存在；
2. 每张卡是否严格基于对应合成报告；
3. 支撑案例是否 ≥3 且链接有效；
4. 是否明确说明现有框架缺口；
5. 预警信号是否可操作；
6. `related` 网络是否合理；
7. 是否出现与已有 dk 卡的重复。

---

## 7. 与现有任务的关系

| 已有任务 | 关系 |
|:---|:---|
| `task_20260624_laowantong-ai2041-cards.md` | AI 2041 P0 优先；本任务可在 AI 2041 P0 完成后或与 P1 并行 |
| `task_20260623_laowantong-lean-startup-cards.md` | 精益创业已验收完成，无冲突 |
| `task_20260623_laowantong-cross-domain-bridge-cards.md` | 跨域融合已验收完成，无冲突 |

---

*质量负责人：王语嫣 | 生成时间：2026-06-25*
