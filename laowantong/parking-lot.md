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
| LW-PL-004 | #145 两卡 frontmatter 状态同步（`pending_review`→`reviewed`）+ `framework-一堂-关键假设-ABCD模型` 补「场景→域映射」节 | 王语嫣 ABCD 域盘点（2026-07-11）；#145 已终审 A- 但卡状态未同步；老朱亲定 ABCD=四大方法论域 | 2 卡 status 对齐终审 + ABCD 卡增映射：**A↔一堂五步法 / B↔科学决策域 / C↔业务公式域 / D↔黑客转化率域**（场景是入口、域是本体，防把「增长」当泛概念误读） | P2 | 待排期 | 可搭任何任务收尾顺手做；映射修正防后来者重犯「场景标签当域本体」的误读 |
| LW-PL-005 | D 域（黑客转化率）建域 + 反向蒸馏自有 agent | 王语嫣 ABCD 域盘点（2026-07-11）；老朱 2026-07-11：D=黑客转化率；**07-12 将到「黑客转化率 YAI」素材** | 两步：① 建域深度广度（总纲+工具族+案例族，按 #150 同规格，王语嫣编排）② **反向蒸馏自有「黑客转化率 agent」**（方法：`tool-半肥猫-课程Skill化的八步工作流` + `case-ban-fei-mao-conversion-hacker-skill` 先例） | P1 | 素材目录已建待放入 | 目录 `00_inbox/Handle the business/conversion rate` 已建暂空；暂存素材：`yt-management-conversion-hacking` / `yt-model-conversion-optimization` / `yt-product-kernel-key-conversion` + `tool-动力阻力分析` + 2 案例 + 2 OCR（10大浪费触点/动力曲线）+ #149 三案例 D 触点（舞蹈 C↔D、服装店 L5/L6） |
| LW-PL-006 | C 域（业务公式）深挖重建 + 反向蒸馏自有 agent | 老朱 2026-07-11：「孔源分享只是冰山一角，主域内容还没进来」；07-12 建域收官 | 两步：① 建域深度广度——**✅ 已完成（#155-158 全 reviewed，56 卡+1 spec/803 边/孤儿 0；图谱修复 #161 reviewed、#162 待终审）** ② **反向蒸馏自有「业务公式 Skill」**——诊断已落盘存档，**老朱节奏：先 C/D 基本盘→YAI 对话记录→反向蒸馏在后，spec 暂缓起草** | P1 | **建域 ✅ 收官；蒸馏待 D 域基本盘+YAI 后启动** | 诊断：`60_feedback/diagnosis/c-domain-business-formula-2026-07-12.md` + 蒸馏诊断 `reverse-distillation-business-formula-skill-2026-07-12.md`（八步前 5 步资产全现成，新增仅 6/7/8 步；测试核心=拒绝能力）；素材索引 `_vlm_output/王语嫣_*索引.md`×2 |

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
