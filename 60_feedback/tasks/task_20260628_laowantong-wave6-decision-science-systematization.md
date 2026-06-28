---
id: task_20260628_laowantong-wave6-decision-science-systematization
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

# Wave 6-A：决策科学域系统化

## 目标

把决策科学域从"散落的 case + 1 个 framework"升级为有索引、有框架、有跨域桥接的方法论域，提升 Agent 在商业判断、资源分配、机会成本场景中的咨询能力。

## 背景

- 当前已有 14 张 reviewed 决策科学卡片（多为 ROI/办公 case），但缺少 domain digest/index
- 只有 1 张 framework（`yt-decision-abcd-model`），缺少决策流程、质量评估、认知偏差等核心骨架
- 与 `.agent/kb-evolution-direction.md` 中「决策域 domain digest」待启动项一致

## 卡片清单（5 张）

| ID | Type | Title | 关键问题 | 说明 |
|:---|:---|:---|:---|:---|
| `decision-science-domain-digest` | index | 决策科学域摘要（升级） | 决策科学域包含哪些核心方法论？如何按场景选用？ | 已存在，状态 enriched，需从 src_unknown 占位升级为完整索引 |
| `framework-decision-quality-checklist` | framework | 决策质量六问检查表 | 一个决策做出前，必须回答哪六个问题？ | 新建 |
| `framework-decision-cognitive-bias-map` | framework | 商业决策常见认知偏差地图 | 哪些认知偏差最常破坏商业决策？如何对冲？ | 新建 |
| `dk-decision-when-to-defer` | dk | 何时应该推迟决策 | 什么情况下"不决策"比"快速决策"更好？ | 新建 |
| `case-decision-ai-assisted-vs-human` | case | AI 辅助决策 vs 人工决策的边界案例 | 哪些决策可以交给 AI，哪些必须保留人工判断？ | 新建，决策科学 × AI 协作桥接 |

## 质量标准

1. 每张卡按 `laowantong-context.md` 标准跑 `kdo pre-submit`
2. index 卡必须链接到本域所有已有 reviewed 卡 + 新建卡
3. framework 卡必须含 When NOT to Use + 失败模式
4. case 卡必须含 4 个标准 section（关键证据/可迁移场景/教训/失败模式）
5. dk 卡必须含 6 个标准 section
6. 桥接卡必须回答双向价值（决策科学 × AI 协作）

## 依赖

- 黄药师负责 `domain-decision-science-index` 的 domain digest 基建规格
- 王语嫣先审核已有 14 张决策科学 reviewed 卡，避免重复

## 验证

- 1 张 index 升级 + 4 张新建卡全部 `kdo pre-submit` 通过
- 决策科学域 reviewed 卡片数从 14 增至 18（index 升级后算 1 张，不新增计数）
- `kdo lint` 无新增 ERROR

## 欧阳锋审核备注

- 原建议的 `domain-decision-science-index` 与现有 `30_wiki/domains/decision-science-domain-digest.md` 重复，改为升级现有 digest
- 升级时必须清理内容区 `src_unknown` 占位，补全核心框架/关键概念/与其他域桥接
