---
id: audit-stuck-cards-20260907
title: "存量停留卡审计：终审已过（queue=reviewed）但交付卡未转正清单"
type: audit
status: draft
author: huangyaoshi
created_at: 2026-09-07
task: task_20260906_huangyaoshi-card-status-flip
reviewed_by: 待审
source_refs:
  - 60_feedback/tasks/task_20260906_huangyaoshi-card-status-flip.md
  - 90_control/scripts/queue_transition.py
  - 60_feedback/tasks/task_20260906_laowantong-ai-kb-cards-promotion.md
---

# 存量停留卡审计（#670 附带产物，2026-09-07）

> **方法**【实证】：用 #670 新解析器 `_resolve_delivered_cards`（三层解析）反查全部
> `queue status=reviewed`（253 单）的执行报告「交付物」节 → 逐卡读 frontmatter 三态。
> 只读不写——本审计不翻转任何卡。

## 结论 1：#670 任务单点名的 8 张已收口（外部动作，非本单）

欧阳锋 09-07 02:09 手工 `review_mark` 批收口 21 张（11 张 #668 AI-KB + 10 张 #666 框架批），
commit `1ceef00d5`。任务单点名的 `framework-ai-business-cognition-system` + #666 批 7 张
全部在列，当前三态均为 `status: reviewed / reviewed_by: 欧阳锋 / review_date: 2026-09-07`
【实证：逐卡 grep，2026-09-07】。

## 结论 2：更早存量仍有 33 张 draft 类停留卡（16 个任务）

终审已过（queue=reviewed）但交付卡 `status: draft|needs-review`——同属「挖出来了但卡在
半路」的检索失明机制（检索层 `【未审 draft】` 标，KDO CLI delivery.py `_label_unreviewed`
#380）。#670 钩子上线后新增单不再产生此存量；**历史单的翻转属审查裁量，须欧阳锋核裁后
批量收口**（`reviewed_by` 归属=审查者动作，生产/基建侧不代写——E018 家族防线）。

| seq | 卡路径 | status | reviewed_by |
|:---:|:--|:--|:--|
| 451 | `30_wiki/agent-specs/agent-spec-laowantong-producer.md` | draft | 待审 |
| 570 | `30_wiki/agent-specs/agent-spec-hongqigong-multimodal.md` | draft | 待审 |
| 570 | `30_wiki/agent-specs/agent-spec-duanwangye-publisher.md` | draft | 待审 |
| 571 | `30_wiki/frameworks/framework-truman-ai-featureset.md` | draft | pending |
| 573 | `30_wiki/cases/case-wangfei-koupen-dual-track-writing.md` | draft | 待审 |
| 575 | `30_wiki/frameworks/framework-openclaw-vs-harness-selection.md` | draft | 待审 |
| 578 | `30_wiki/dk/dk-multithread-whack-a-mole.md` | draft | 待审 |
| 578 | `30_wiki/dk/dk-project-skill-agent-loop.md` | draft | 待审 |
| 578 | `30_wiki/dk/dk-roi-three-step-decision.md` | draft | 待审 |
| 578 | `30_wiki/dk/dk-jiejiaxiuzhen-ai-reestablish.md` | draft | 待审 |
| 579 | `30_wiki/frameworks/framework-strategy-conviction.md` | draft | 待审 |
| 611 | `30_wiki/concepts/concept-yihang-data-pack-ethics.md` | draft | pending |
| 633 | `30_wiki/frameworks/framework-education-protracted-war.md` | draft | 待审 |
| 633 | `30_wiki/cases/case-live261-luyu-strategy-conviction-maoxuan.md` | draft | 待审 |
| 633 | `30_wiki/cases/case-live261-jacky-ip-marketing-protracted-war.md` | draft | 待审 |
| 633 | `30_wiki/cases/case-live261-lixiuhui-compound-bow-dealer-war.md` | draft | 待审 |
| 641 | `30_wiki/cases/case-private-board-majingjing-decision-camp.md` | draft | 待审 |
| 641 | `30_wiki/dark-knowledges/dk-majingjing-chengquan-thinking.md` | draft | 待审 |
| 641 | `30_wiki/dark-knowledges/dk-majingjing-momentum-design.md` | draft | 待审 |
| 641 | `30_wiki/dark-knowledges/dk-majingjing-role-ladder.md` | draft | 待审 |
| 641 | `30_wiki/dark-knowledges/dk-listen-ear-heart-qi.md` | draft | 待审 |
| 641 | `30_wiki/dark-knowledges/dk-wangzhen-transfer-law.md` | draft | 待审 |
| 654 | `30_wiki/skills/skill-five-layer-positioning.md` | draft | pending |
| 654 | `30_wiki/agent-specs/agent-spec-kouspeng-task-decomposer.md` | draft | pending |
| 654 | `30_wiki/bridges/bridge-yitang-seek-truth-liberate-thought.md` | draft | 待审（review_date 2026-07-26 与 draft 并存，疑旧值残留） |
| 664 | `30_wiki/workflows/workflow-multi-researcher-cross.md` | draft | 待审 |
| 665 | `30_wiki/dark-knowledges/dk-modeling-untrained-first-pride-cost.md` | draft | pending |
| 665 | `30_wiki/dark-knowledges/dk-modeling-checklist-working-medium.md` | draft | pending |
| 665 | `30_wiki/dark-knowledges/dk-jiangxiang-origin-story-mental-coordinate-system.md` | draft | pending |
| 665 | `30_wiki/dark-knowledges/dk-ai-stronger-need-to-know-what-you-want.md` | draft | pending |
| 665 | `30_wiki/dark-knowledges/dk-strategy-meeting-quality-friction-signal.md` | draft | pending |
| 665 | `30_wiki/frameworks/framework-education-protracted-war.md` | draft | 待审 |
| 665 | `30_wiki/methods/method-dual-triangle-human-ai-division.md` | draft | pending |

## 结论 3：7 项「非 draft」命中——多数不该翻，单列供核对

| seq | 路径 | status | 说明 |
|:---:|:--|:--|:--|
| 570/664 | `30_wiki/index.md` | stable | MOC/目录页，解析器 tier1 命中路径；不该翻 |
| 576 | `30_wiki/tools/tool-ai-agent-feature-comparison.md` | pending_review | 状态值非规范集，疑手工误写，须人工核对 |
| 624 | `30_wiki/cases/case-truman-roi-decision-spring-festival-class.md` | enriched | 旧版状态值（legacy），是否视为已审由欧阳锋定 |
| 624 | `30_wiki/tools/tool-geo-ai-search-visibility-playbook.md` | enriched | 同上 |
| 645 | `30_wiki/personal-os/zhu-conversation-insights.md` | active | 非标准知识卡（个人 OS 产物），不该翻 |
| 665 | `30_wiki/cases/case-truman-personal-growth-map-creation.md` | enriched | 补强宿主（reviewed_by 王语嫣（代欧阳锋） 2026-06-16），非新卡，不该翻 |

## 建议处置（需欧阳锋动作）

1. 按上表逐单核对终审范围是否覆盖该卡（尤其 #654 bridge 卡与宿主/补强类命中）。
2. 确认后批收口（一行循环，dry-run 先看）：
   ```bash
   python 90_control/scripts/review_mark.py <卡路径> --reviewer 欧阳锋 --dry-run
   python 90_control/scripts/review_mark.py <卡路径> --reviewer 欧阳锋
   ```
3. 或授权黄药师开一个小批处理入口（读本清单逐卡过 `mark_card`），另立项不占 #670。

## kdo query 检索记录（宪法第六条，2026-09-07）

| 检索词 | 命中 | 相关 | 备注 |
|:--|:--|:--|:--|
| 卡片 status 状态翻转 reviewed 审查后状态流转 | Top 5 | 1（queue-transition SKILL.md） | 其余不相关；库内无「状态翻转机制」既有卡 |
| review pass 卡片转正 状态流转 终审通过 | Top 5 | 1（同上） | 单一相关命中=本机制所属 skill 文档 |

> 检索目的：确认库内是否已有「终审后卡状态流转」方法论卡/机制卡，避免重复建卡（B3/B6）。
> 结论：无既有卡覆盖此机制，#670 为基建新机制（落点=脚本+SKILL 文档，非知识卡）。
