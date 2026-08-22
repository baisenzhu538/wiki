---
title: 分批任务批次 TODO 闭环机制修复建议书（#411 三批实证）
type: proposal
status: pending_orchestration
domain: infrastructure
created_at: '2026-08-22'
updated_at: '2026-08-22'
author: 欧阳锋
audience: 王语嫣（编排层）
related:
- 60_feedback/tasks/task_20260822_laowantong-related-asymmetry-backfill.md
- 60_feedback/tasks/task_20260822_huangyaoshi-queue-mojibake-fix.md
---

# 分批任务批次 TODO 闭环机制修复建议书

## 来源

- 2026-08-22 #411（related-asymmetry 分批回填）第三批实证：**第二批终审的 TODO（dk-p11 脏链移除）第三批未执行未提**——批次间反馈闭环断裂
- 用户追问"这个是什么问题产生的"后根因分析完成，本建议书为修复立项依据
- 场景：**任何"可长期分批推进"的任务**（#411 型）都会踩同一机制缺口

## 问题与根因（三批实证）

| 层 | 根因 | 实证 |
|:--|:--|:--|
| **节奏层** | 批次间无验收闸——执行者连续冲批（11:56 第二批 / 11:58 第三批仅隔 2 分钟），不等上批终审 PASS 就开下批 | TODO 写于 12:1x（第二批终审），第三批 11:58 已交付——**TODO 落地时下批已完成，客观上无法被吸收** |
| **机制层** | O-3 已知 bug：queue_transition `complete` 对 queued 任务锁内 re-check 失败 → 状态卡 queued、REVIEW-PENDING 段不登记 → 欧阳锋收不到提审通知，验收进一步滞后 | #411 三批提审全部无声（第二批靠用户转达、第三批靠用户提醒才发现） |
| **结构层** | 跨批 TODO 无固定传递位——终审 TODO 写在"终审记录"节（审查者区域），执行者默认读"执行范围"节，靠"恰好读到"闭环 | 第一批 compas TODO 闭环属运气（11:53 写、11:54 处理），第二批 dk-p11 未闭环（11:58 后无人处理） |

## 建议修复项（R 系列，编号建议性，正式编号以队列为准）

### R1（结构）：分批任务单加「批次 TODO 队列」固定节

- 位置：任务单「执行范围」节之后（执行者必读区，与执行范围同层）
- 内容：`| 批次 | TODO 项 | 提出者 | 状态 |`，终审产生的跨批 TODO 由欧阳锋落此节，执行者每批开工前必读并逐项闭环（✓/✗ + 说明）
- 执行报告新增「上批 TODO 闭环」节（逐项 ✓/✗）——#411 第三批终审已将此设为硬性要求，本项为机制化

### R2（节奏）：分批任务批次间验收闸

- 规则：分批任务执行者**下一批开工前**必须：① 读任务单「批次 TODO 队列」节（R1）② 上批终审记录已存在（PASS 或 FAIL 意见均已吸收）
- 例外：用户直接下令连续冲批（如#411 当前 3 批连发）时可豁免，但执行报告须声明"未等上批终审"
- 防呆建议：QUEUED 段分批任务行备注注明"分批任务：批次间须读 TODO 节"

### R3（机制）：O-3 bug 修复——queue_transition complete 锁内 re-check 失败

- 现状：`complete --force` 对 queued 任务锁内 re-check 必失败（blocker 已挂），导致提审无声、REVIEW-PENDING 不登记
- 影响放大：分批任务每批都提审，O-3 让每批提审都无声——审查者依赖用户转达才发现，验收延迟直接放大 TODO 闭环失败概率
- 建议：黄药师修复 complete 路径锁内 re-check（或 complete 后强制登记 REVIEW-PENDING 段），修复前 REVIEW-PENDING 段登记作为 complete 的必含动作

### R4（工具，可选）：related-asymmetry 清单标注原始链方向

- full-library-rescan `--check related-asymmetry` 输出追加"原始链来源"（A→B 中 A 的 related 原文行号）——执行者/审查者快速定位疑链（脏链对称化模式已 2 次实证：compas/dk-p11）
- 与 #399 工具同仓演进，可并入 #409 同类基建批次

## 优先级与依赖（建议）

| 项 | 优先级 | 执行者 | 依赖 |
|:--|:--|:--|:--|
| R1 批次 TODO 队列节 | P1 | 王语嫣（任务单模板）+ 欧阳锋（#411 先行落地） | 无 |
| R2 批次间验收闸 | P1 | 王语嫣（编排规则写入 PROTOCOL）+ 各执行者 | R1 |
| R3 O-3 complete 修复 | P1 | 黄药师 | 无（blocker 已挂） |
| R4 工具标注原始链方向 | P2 | 黄药师 | #399 工具演进 |

## 验收标准

1. R1：#411 任务单已含「批次 TODO 队列」节，第四批执行报告含「上批 TODO 闭环」逐项 ✓/✗
2. R2：PROTOCOL/编排规则含"分批任务批次间验收闸"，新分批任务单模板引用
3. R3：complete 后 REVIEW-PENDING 段必登记（实测 3 单），O-3 blocker 关闭
4. R4：related-asymmetry 清单含原始链来源列

## 送审

- 王语嫣编排：复核 R1-R4 方向/优先级/依赖，立项入队
- 欧阳锋：R1 在 #411 先行落地；R3/R4 终审验收
