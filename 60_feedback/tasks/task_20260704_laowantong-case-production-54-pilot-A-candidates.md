---
id: task_20260704_laowantong-case-production-54-pilot-A-candidates
title: '#54 试点 A 级候选投产：7 张 companion case 卡'
type: task
status: in_progress
priority: P2
assignee: kimi
reviewer: 欧阳锋
reviewed_by: pending
created_at: 2026-07-04
updated_at: '2026-07-03T19:56:03.925511+00:00'
expected_outputs:
- '7 张标准 case 卡，对应 #54 诊断报告中欧阳锋圈定的 A 级候选'
- 每张 case 卡包含：背景、决策/行动、结果、可迁移洞察、来源引用
- 反向更新 ≥7 张锚定概念/工具/framework 卡的 related 字段
- kdo pre-submit 全部 PASS，lint 0 新增 ERROR
dependencies:
- '#54 已 reviewed（已满足）'
source_refs:
- 60_feedback/diagnosis/diag_20260704_retroactive-case-scan-pilot.md
---

# #54 试点 A 级候选投产：7 张 companion case 卡

## 背景

#54「已消化素材案例卡补扫试点」已 reviewed（pass with reservations）。欧阳锋在终审报告中圈定 7 条应立即投产的 A 级候选，作为从「候选清单」到「完整 case 卡」的试点。

本任务只处理这 7 条，不扩展到其余 13 条 A 级候选或 B/C 级候选。目的是验证 #54 扫描流程产出的候选确实能转化为高质量 case 卡。

## 目标 A 级候选

| 编号 | 域 | 主题 | 建议锚定卡（任务单编制时参考，老顽童生产前需复核） |
|:---|:---|:---|:---|
| 科学决策-004 | 科学决策 | 全员涨薪 20% ROI 测算 | framework-decision-quality-checklist、yt-decision-y-model、tool-泛产品落地-ROI分析 |
| 科学决策-009 | 科学决策 | Top City 负收益消减与自动排名 | framework-decision-quality-checklist、tool-区分获客渠道计算单元roi |
| 科学决策-011 | 科学决策 | 把 2 小时休息压缩为 1 小时 | framework-yitang-five-step-to-time-management、dk-time-management-common-mistakes |
| 泛产品设计-001 | 泛产品设计 | 一淘项目背景与三大难题 | yt-unit-model、framework-yitang-five-step-to-time-management |
| 泛产品设计-002 | 泛产品设计 | top 1/top 3/top 5 筛选打磨 | yt-unit-model、tool-ai-deliverable-polish-loop |
| 战略-013 | 战略 | 撤退型布局 1：出售 | framework-strategy-exit-timing、yt-decision-y-model |
| 战略-006 | 战略 | 撤退型布局 2：去除 | framework-strategy-exit-timing、yt-decision-y-model |

> 老顽童生产前必须重新 Read `diag_20260704_retroactive-case-scan-pilot.md` 中对应条目，确认段落原文、来源文件、可锚定卡；任务单中的锚定卡仅为起点。

## 卡片规格

每张 case 卡需满足 KDO case 卡 v1.5 标准：

- `type: case`
- 标题格式：`case-<domain>-<short-slug>.md`
- 4 个标准 section：背景 / 决策与行动 / 结果 / 可迁移洞察
- Critique：内部局限 + 外部攻击者
- Synthesis：链接到 ≥2 张已有卡
- source_refs：指向 `00_inbox/` 原始素材文件
- related：反向链接到锚定卡，并确保锚定卡回链

## 验收标准

1. 7 张 case 卡全部 `kdo pre-submit` PASS。
2. `kdo lint` 0 新增 ERROR；WARNING 不增加或仅增加历史共通的机械类 WARNING。
3. 每张卡都有明确的「可迁移洞察」，不是简单复述故事。
4. 锚定卡 related 双向链接完整。
5. 不新建 concept/tool/framework 卡；如现有卡无法锚定，标记为 gap 交王语嫣判断。

## 边界

- 不处理 #54 报告中其余 A/B/C 级候选。
- 不扩展为新的域诊断。
- 如发现候选本身无法支撑完整 case 卡，老顽童应记录原因并退回王语嫣，而非硬凑。

## 依赖

- #54 reviewed ✅
