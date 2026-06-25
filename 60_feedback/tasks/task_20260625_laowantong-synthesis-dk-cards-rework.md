---
id: task_20260625_laowantong-synthesis-dk-cards-rework
type: production_task
created_at: 2026-06-25
author: 王语嫣
assignee: 老顽童
priority: P1
---

# 老顽童返工/下一批任务：补完缺失 dk 卡 + 继续 P0-A 单元模型域

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产/修补卡片。
> 前置验收报告：`60_feedback/audit/audit_20260625_wangyuyan-synthesis-dk-cards.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 返工 + 下一批生产 |
| 返工来源 | 三域跨案例合成 dk 卡验收：9 张任务缺 1 张 |
| 下一批来源 | `task_20260625_laowantong-vlm-to-cards.md` P0-A 单元模型域 |
| 优先级 | P1（返工优先，完成后立即切 P0-A） |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | 老顽童 |

---

## 1. 返工项：补产 1 张缺失 dk 卡

### 1.1 必须生产的卡片

| id | 标题 | 来源 | 核心要求 |
|:---|:---|:---|:---|
| `dk-strategy-stage-leverage-mismatch` | 战略阶段与杠杆错配 | `60_feedback/audit/synthesis_strategy.md` 洞察 1 | 识别生命周期阶段、阶段转换信号、各阶段应追求的杠杆 |

### 1.2 内容要求

必须基于 `synthesis_strategy.md` 洞察 1，不得自行发挥：

1. **一句话定义**：说明“战略失败往往不是方向错误，而是阶段与杠杆错配”这一模式。
2. **模式描述**：2-3 段，解释同一批战略动作在不同生命周期阶段（跑马圈地期 / 吃饱期 / 转型期）为何会产生不同结果。
3. **支撑案例**：≥3 个，必须带 `[[case-xxx]]` 双向链接。优先使用：
   - `[[case-strategy-failure-02-supermarket]]`
   - `[[case-lean-premature-expansion]]`
   - `[[case-strategy-practice-12-zero-loss]]`
   - `[[case-strategy-shell-oil]]`
   - `[[case-strategy-wuxi-suntech]]`
   - `[[case-strategy-revival-13-bestore]]`
   - `[[case-strategy-revival-14-gucci]]`
4. **与现有框架的关系**：
   - `[[framework-strategy-six-stages]]`：已区分阶段，但缺少“阶段转换信号 + 阶段适配动作”操作清单；
   - `[[framework-strategy-brm]]`：回答赛道/定位/模式，但不绑定生命周期阶段；
   - 经典框架（五力、价值链、BCG）多为静态分析，缺少“何时切换杠杆”的触发器。
5. **预警信号**：≥3 条，帮助读者识别自己是否陷入阶段与杠杆错配。
6. **可迁移场景**：2-3 个（产品生命周期管理、个人职业阶段选择、投资组合阶段配置等）。
7. **行动建议**：1-2 条，今晚就能执行。

### 1.3 Frontmatter 规范

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
- "[[strategy-domain-digest]]"
- "[[framework-strategy-six-stages]]"
- "[[framework-strategy-brm]]"
- "[[case-strategy-failure-02-supermarket]]"
- "[[case-lean-premature-expansion]]"
- "[[case-strategy-shell-oil]]"
- "[[case-strategy-wuxi-suntech]]"
---
```

**`related` 必须 ≥ 5**，且至少包含 1 个跨域或 digest 链接。

---

## 2. 可选优化项（不阻塞验收，但建议顺手修）

以下 3 项来自验收报告的非阻塞性建议，老顽童可在补卡时一并处理：

1. **统一 frontmatter 字段**：
   - 部分已产卡片包含任务模板未定义的 `dark_knowledge_type: heuristic`。
   - 建议移除该字段，统一只保留 `type: dk`。
   - 涉及文件：
     - `dk-strategy-correlation-vs-causation-leverage.md`
     - `dk-strategy-organization-strategy-mismatch.md`
     - `dk-research-decision-first-mapping.md`
     - `dk-research-identity-craft-for-closed-information.md`
     - `dk-research-triangulation-stop-rule.md`
     - `dk-yitang-behavior-over-asking.md`
     - `dk-yitang-business-model-risk-over-product-risk.md`
     - `dk-yitang-model-asset-capitalization.md`

2. **补全预警信号**：
   - `dk-yitang-behavior-over-asking.md` 当前预警信号为 4 条，建议补到 5 条。

3. **结构调整**：
   - `dk-yitang-model-asset-capitalization.md` 的支撑案例当前嵌入在“操作方法”表格中，建议单独设“支撑案例”节，与任务模板保持一致。

---

## 3. 下一批任务：P0-A 单元模型域（返工完成后启动）

补卡验收通过后，老顽童立即切回 `task_20260625_laowantong-vlm-to-cards.md` 的 **P0-A 单元模型域**，按该任务中的生产顺序执行：

1. `tool-单元模型-单商圈`
2. `tool-单元模型-单城市`
3. `tool-单元模型-象限分析法`
4. `framework-单元模型-外部对抗地图`
5. `tool-单元模型-壁垒预判`
6. `framework-TCPR底层网络协议`
7. `dk-单元模型-找全成本实操难点`
8. `dk-单元模型-找单元模型实操难点`
9. `dk-单元模型-找基准值实操难点`
10. `dk-单元模型-规模对抗实操难点`
11. `dk-单元模型-对抗小抄`
12. `concept-单元模型-学练用`
13. `concept-最简单元模型`
14. `case-unit-model-gashapon`（enrich）
15. `yt-unit-model-overview`（enrich 单*系列）

P0-A 要求详见原任务文件，此处不重复。

---

## 4. 提交方式

- 补完 `dk-strategy-stage-leverage-mismatch` 后，通知王语嫣做 20% 抽样复核（至少含新卡 1 张 + 已产卡 1 张）。
- 抽样通过后，方可进入 P0-A 生产。
- P0-A 每完成 5 张卡，通知王语嫣抽样一次。

---

## 5. 质量门禁（自查清单）

新卡必须满足：

- [ ] `id` 与文件名一致
- [ ] `status` = `enriched`
- [ ] `author` = `老顽童`
- [ ] `reviewed_by` = `欧阳锋`
- [ ] `source_refs` 精确到 `synthesis_strategy.md`
- [ ] `related` ≥ 5，至少 1 条 digest/跨域链接
- [ ] 支撑案例 ≥ 3 个 `[[case-xxx]]`
- [ ] 预警信号 ≥ 3 条
- [ ] 可迁移场景 ≥ 2 个
- [ ] 明确说明现有框架未覆盖的缺口
- [ ] 关键声明带 `[conf=X, source=...]`
- [ ] YAML 解析通过

---

*任务下达：王语嫣 | 日期：2026-06-25*
