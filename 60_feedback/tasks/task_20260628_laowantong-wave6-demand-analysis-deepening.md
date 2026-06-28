---
id: task_20260628_laowantong-wave6-demand-analysis-deepening
type: task
status: queued
assignee: 老顽童
priority: P1
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- 60_feedback/diags/diag_20260628_wangyuyan-wave6-decision-science-demand-analysis.md
- .agent/kb-evolution-direction.md
---

# Wave 6-B：需求分析域深化

## 目标

把需求分析域从"3 concept + 4 dk + 3 framework"补全为有 index、有 case、有跨域桥接的独立方法论域，强化 Agent 在需求识别、需求验证、假需求识别等核心咨询场景的能力。

## 背景

- 当前已有 10 张 reviewed 需求分析卡片，但缺少 case 卡和 domain digest/index
- 需求分析是"一堂五步法"第一环，与产品内核、渠道增长、精益创业强相关，但缺少跨域桥接卡
- 与 `.agent/kb-evolution-direction.md` 中「需求分析域 domain digest」待启动项一致

## 卡片清单（5 张）

| ID | Type | Title | 关键问题 |
|:---|:---|:---|:---|
| `domain-demand-analysis-index` | index | 需求分析域索引 | 需求分析域有哪些核心工具？适用什么场景？ |
| `case-demand-b2b-enterprise-erp` | case | ToB 企业 ERP 需求分析案例 | 复杂 B2B 需求如何分层验证？ |
| `case-demand-b2c-consumer-insight` | case | ToC 消费洞察驱动需求案例 | 用户说的和做的不一致时，如何识别真需求？ |
| `framework-demand-validation-pipeline` | framework | 需求验证流水线 | 从假设到验证的完整流程是什么？ |
| `dk-demand-signal-vs-noise` | dk | 需求信号与噪音的区分 | 哪些市场信号是真需求，哪些是噪音？ |

## 质量标准

1. 每张卡按 `laowantong-context.md` 标准跑 `kdo pre-submit`
2. index 卡必须链接到本域所有已有 reviewed 卡 + 新建卡
3. case 卡必须含 4 个标准 section（关键证据/可迁移场景/教训/失败模式）
4. framework 卡必须含 When NOT to Use + 失败模式
5. dk 卡必须含 6 个标准 section
6. 跨域桥接必须回答双向价值（需求分析 × 产品内核 / 渠道增长 / 精益创业）

## 依赖

- 黄药师负责 `domain-demand-analysis-index` 的 domain digest 基建规格
- 王语嫣先审核已有 10 张需求分析 reviewed 卡，避免重复

## 验证

- 5 张卡全部 `kdo pre-submit` 通过
- 需求分析域 reviewed 卡片数从 10 增至 15
- `kdo lint` 无新增 ERROR

## 欧阳锋审核备注

- 当前需求分析域 reviewed 卡片约 20 张（不同统计口径），但缺少 case 卡和独立 index，诊断结论成立
- 2 张 case 卡建议从一堂/精益创业素材中萃取真实案例，避免凭空编造
- `framework-demand-validation-pipeline` 应与现有 `yt-demand-analysis-hiking-map` 等框架明确区分
