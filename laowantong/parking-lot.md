---
id: laowantong-parking-lot
title: 老顽童停车场清单
type: index
status: enriched
author: 老顽童
domain:
- strategy
- operations
- product
source_context: 老顽童待排期任务集合
source_refs:
- 00_inbox/战略专题/_strategy_cards_implementation_status.md
- 70_product/tasks/laowantong-batch-2026-06-20.md
- 60_feedback/audit/kcard-quality-gate-report-2026-06-15.md
confidence: 0.95
trust_level: high
language: zh-CN
---

# 老顽童停车场清单

> 已识别但尚未进入执行状态的任务集合。此处不承诺完成时间，仅用于防止遗漏，并在获得明确指令或迭代规划时作为输入。

## 当前停车任务

| 编号 | 任务 | 来源 | 预期产出 | 优先级 | 状态 | 备注 |
|:---:|:---|:---|:---|:---:|:---:|:---|
| LW-PL-001 | `_269` 深蓝海洋主题页卡片化 | `00_inbox/战略专题/_strategy_cards_implementation_status.md` | 1 张战略域 tool/case/framework 卡 | P2 | 待内容确认 | VLM 描述仅为背景图/主题页，未明确实质框架内容 |
| LW-PL-002 | 重启 `laowantong-batch-2026-06-20.md` waves 1-2 | `70_product/tasks/laowantong-batch-2026-06-20.md` | 完成门禁快速清理 11 张卡 + P0 返工 13 张卡 | P1 | 待用户/欧阳锋确认 | 因战略域 PPT 补强插入而暂停，未取消 |
| LW-PL-003 | 全库 lint 历史债务修复 | `60_feedback/audit/kcard-quality-gate-report-2026-06-15.md` | kdo lint errors/warnings 大幅下降 | P2 | 待另排工单 | 当前 1700+ errors / 4700+ warnings；不应与主线并发 |
| LW-PL-004 | #145 两卡 frontmatter 状态同步：`framework-一堂-关键假设` + `framework-一堂-关键假设-ABCD模型` 由 `pending_review` 改 `reviewed` | 王语嫣 ABCD 域盘点（2026-07-11）；#145 已欧阳锋终审 A- 但卡状态未同步 | 2 卡 status 与 #145 终审结论一致 | P2 | 待排期 | 1 分钟级修复；可搭任何下一个任务收尾顺手做 |
| LW-PL-005 | D 域（转化率黑客）素材暂存与立项等待 | 王语嫣 ABCD 域盘点（2026-07-11）；老朱闸门「等系统课到位再立项」 | 素材到位后：总纲 framework + 工具卡族 + 案例族 + agent-spec（按基本功域 #150 同规格，由王语嫣编排） | P1 | 待素材输入 | 现有暂存素材：`yt-management-conversion-hacking` / `yt-model-conversion-optimization` / `yt-product-kernel-key-conversion` + `tool-动力阻力分析` + 2 案例 + 2 OCR（10大浪费触点/动力曲线）+ #149 三案例 D 触点（舞蹈 C↔D、服装店 L5/L6 参数回填） |

## 已完成任务

| 编号 | 任务 | 完成时间 | 产出 | 备注 |
|:---:|:---|:---:|:---|:---|
| ✅ LW-DONE-001 | 战略域 PPT 补强 `_54` | 2026-06-22 | `case-strategy-snack-export-opportunity.md` | 已补核心洞察 |
| ✅ LW-DONE-002 | 战略域 PPT 补强 `_115` | 2026-06-22 | `tool-strategy-value-capture.md` 补强 | 王语嫣验收通过 |
| ✅ LW-DONE-003 | 战略域 PPT 补强 `_184` | 2026-06-22 | `tool-strategy-logistics-cost-planning.md` | 王语嫣验收通过 |
| ✅ LW-DONE-004 | 战略域 PPT 补强 `_249` | 2026-06-22 | `tool-strategy-market-opportunity-matrix.md` | 王语嫣验收通过 |

## 边界

- **入池标准**：已识别、与老顽童职责相关、但尚未获得明确执行指令的任务。
- **不出池标准**：未形成可描述任务项的模糊想法；已排期并进入 active 状态的任务。
- **不替代项目计划**：停车场只记录"待安排"，不分配资源、不设定 deadline。

## 失败模式

| 失败模式 | 信号 | 防御 |
|:---|:---|:---|
| 停车场变墓地 | 任务长期待排期超过 2 周 | 每周 review，超过 2 周无进展标注 stale |
| 优先级漂移 | 所有任务都是 P1 | 每次仅允许 ≤2 个 P1 并存 |
| 来源不可追溯 | 任务来源只有口头描述 | 每个任务必须关联文件路径或工单 |

---

*老顽童 · 2026-06-23 · 战略域收工后整理*
