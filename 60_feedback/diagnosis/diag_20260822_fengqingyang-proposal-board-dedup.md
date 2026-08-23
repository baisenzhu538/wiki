---
id: diag_20260822_fengqingyang-proposal-board-dedup
title: PROPOSAL-PENDING 重复登记审计与修复建议（conveyor_probe 去重键失效）
type: proposal
author: 风清扬（观察者 / 审计者）
created_at: 2026-08-22
status: resolved
audience: 王语嫣
---

# PROPOSAL-PENDING 重复登记审计与修复建议

> 老朱指令：把 08-22 夜 PROPOSAL-PENDING 段重复登记写成建议交王语嫣。
> 定位：观察者审计建议（B2-2 ① 只交王语嫣）。只诊断与建议，不动队列/看板/探针代码（黄药师域）。

## 0. 一句话结论

conveyor_probe.py 21:38 那轮登记，把三份建议书各重复登记了一条「待王语嫣复核裁定」，其中两份已复核的（orchestration-audit / 5role-spec-workflow）被重新登记成「待复核」——等于把已了结项重新打开。根因是登记幂等的去重键两侧格式不一致，叠加复核后 frontmatter 状态不回写。

## 1. 现状证据（production-queue.md PROPOSAL-PENDING 段）

| 文件 | 手工登记行 | 探针登记行（21:38） | 判定 |
|:--|:--|:--|:--|
| diag_20260822_fengqingyang-orchestration-audit.md | 已复核裁定 ×2（划掉） | 待复核 ×1 | 重复且已复核，被重开 |
| diag_20260822_fengqingyang-5role-spec-workflow.md | 已复核裁定 ×1（划掉） | 待复核 ×1 | 重复且已复核，被重开 |
| diag_20260822_fengqingyang-coldstart-oneclick-recovery.md | 待复核 ×1（未划，全路径+长标题） | 待复核 ×1 | 重复，仍待复核 |

三份 frontmatter 均为 `audience: 王语嫣` + `status: pending_orchestration`；已复核的两份 status 未回写。

## 2. 根因（三层）

1. **去重键两侧格式不一致（直接原因）**：`_scan_proposals()` 返回裸文件名（`diag_*.md`）；`_update_proposal_board()` 以每行首个「｜」字段建 known 集合——手工行是全路径（`60_feedback/diagnosis/diag_*.md`），已复核行还带 `~~` 前缀。裸名 / 全路径 / ~~全路径 三者互不相等，首跑三份全被判「未登记」而重复写入。
2. **复核后状态不回写（生命周期缺口）**：王语嫣复核只在队列行划掉写结论，不回写文件 frontmatter `status`；`_scan_proposals()` 只读 frontmatter，已复核文件永远是 `pending_orchestration` 命中，每次扫描都当新建议书。
3. **通道切换期双轨并存（历史成因）**：手工自登（全路径格式）与探针自动登记（裸文件名格式）并存，格式不统一是重复的土壤。

## 3. 处置建议（按归属）

| # | 动作 | 归属 | 依赖 |
|:--|:--|:--|:--|
| A | 清重：删掉三份「21:38 待复核」重复行，各保留一条有效行（orchestration/5role 留已复核行；coldstart 留未划待复核行） | 王语嫣 | 无 |
| B | 修探针去重键：known 建集前把每行首字段归一为裸文件名（strip `~~` + 取 basename），再与 hits 比较 | 黄药师 | 无 |
| C | 复核状态回写：王语嫣复核划掉后同步把 frontmatter `status` 改为 `resolved`；`_scan_proposals()` 只收 `pending_orchestration`，已复核退出命中 | 王语嫣（口径）+ 黄药师（脚本） | B 后 |

> B 能止血（现账清了不再重复）；C 才是断根（已复核文件永久退出扫描面）。建议 B/C 同步做，A 清现账。

## 4. 附带说明

- 本建议书自身为 `status: pending_orchestration`，按新通道由 conveyor_probe 自动登记；我未手改队列段（遵守「勿手改」+ 观察者不改看板）。
- 若 C 采纳，本建议书复核后同样需回写 frontmatter，避免成为下一条永久命中。

---

*风清扬（观察者 / 审计者）· 2026-08-22 · 只建议、不派活*