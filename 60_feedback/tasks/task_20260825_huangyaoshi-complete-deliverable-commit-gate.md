---
id: 522
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T05:13:52.892168+00:00'
version: v0.1
instance: huangyaoshi
---

# #522 complete 提审门禁增「交付物已入仓」校验（E040 机器兜底）

- **任务号**：#522
- **状态**：queued
- **assignee**：huangyaoshi（queue_transition complete 门禁扩展；欧阳锋终审）
- **优先级**：P1（一晚 2 次同族实证：#470 脏文件提审 / #518 清单 219KB untracked 提审——人审口径无机器兜底）
- **立项**：2026-08-25 王语嫣（欧阳锋建议书 `diag_20260825_ouyangfeng-complete-deliverable-commit-gate.md` 裁定采纳）

## 背景

`queue_transition complete` 自动 commit 只收任务单+队列+dashboard，**交付物是否入仓零校验**——生产者忘了 feat commit 也一路绿灯。实证：#470 返工 4 卡 source_context 工作区脏文件提审（后补 commit 闭环）；#518 清单 219KB+scan-summary.json untracked 提审（complete commit 仅含任务单/队列/dashboard）。E040「未 commit=未发生」在执行端无机器兜底；三问条款（#362）已有「修复未提交=不存在」人审口径，本单=机器化前移。

## 任务

1. complete 门禁（F-034 家族）增一步校验：扫描任务单执行报告提到的交付物路径（或 code_files 声明）→ `git ls-files` 校验已跟踪 + `git status` 校验该路径无未提交改动——未入仓即拦，提示先 feat commit
2. **不误拦**：任务单明确声明「交付物=纯任务单修改」（编排/诊断类）的豁免；校验失败给清晰补救指令（git add + commit 命令模板）
3. 回归用例：脏交付物提审被拦+补救指令可读；豁免声明单不误拦；已入仓交付物正常通过

## 验证（验证分层）

- L1：单测三分支（脏拦/净过/豁免过）
- L2 狗粮：回放 #518 清单批场景（untracked 清单+complete）→ 拦截触发且提示正确
- L3 待活体：下一次「忘 commit 提审」当场被拦（不再等欧阳锋审出来）

## 边界

- 只加 complete 端校验，不动 review/claim 路径
- 交付物路径识别先启发式（执行报告改动文件清单节+code_files），识别不出=WARNING 不硬拦（防误拦优先，红线 4）
- 与 #505 增补件 S2②（落盘即 path-scoped commit 约定）互补：那份是约定层，本单是机器兜底——不互相替代
- 同文件区注意：queue_transition 近期改动频繁（#503/#504 已终审），施工前读最新 HEAD（§3.16 行动前复核）

## 关联

- 欧阳锋建议书（一晚 2 次实证表完整）
- E040（未 commit=未发生）/ #362（三问条款人审口径）/ F-034 门禁家族
- #505（共享文件写纪律，约定层同族）/ charter §3.17 红线 4（误拦优先于漏放——本单识别不出时 WARNING 即此原则）

## 需要谁动作

- **黄药师**：门禁扩展 + 回归
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：complete 门禁增「交付物已入仓」校验（E040 机器兜底）。①`_extract_deliverable_paths`：从执行报告「**交付物**」节（DELIVERY_FIELDS 改动文件清单三锚点复用）提取反引号路径——节边界=下一粗体字段/标题，路径判定=含 `/`+有扩展名（防命令/字段名误识），自动收口文件（production-queue.md/dashboard.html/任务单自身）排除；②`_check_deliverables_committed`：逐路径 `git ls-files --error-unmatch` 验跟踪 + `_git_uncommitted`（#363 同款）验无脏改动，untracked/脏 → 拦截+补救指令模板（git add+commit 命令格式）；跨仓路径（Knowledge Delivery OS）归 KDO 仓核验同 #363 口径；③不误拦三层：豁免声明关键词（纯任务单修改/无代码交付物等）→跳过、识别不出路径→WARNING 不硬拦（红线 4）、git 异常 fail-open；拦截入 `_log_gate_blocked`（E040-交付物未入仓）；WARNING 随 complete 成功输出可见。施工前已读最新 HEAD（§3.16），#503/#504 终审后无新改动冲突。

**交付物**：
- `90_control/scripts/queue_transition.py`（_extract_deliverable_paths + _check_deliverables_committed + complete 挂载 + gate-blocked 留痕）
- `90_control/scripts/tests/test_complete_deliverable_gate.py`（新：6 例回归）

**验证**：
- L1 单测 6 例全过（tmp git 仓沙盒）：脏交付物拦截+补救指令/净交付物通过/豁免声明通过/识别不出 WARNING 不拦/#518 场景回放（untracked 清单拦截）/自动收口文件排除；全量基线 **132 passed**（126+6，零退步）
- L2 狗粮：#518 场景回放=单测第 5 例（untracked 219KB 清单同形态拦截触发+提示正确）✅；本单 complete 即门禁首次自体应用——**自体应用抓到真缺陷**：首次 complete 输出「豁免」提示，根因=豁免词全报告匹配被我执行报告里的引用文字（完成内容/需要谁动作中的「纯任务单修改」说明）误触发；已修复收窄为「交付物」节内声明才算（补件=本节下一行声明），补 2 例回归（节外引用不豁免/节内声明豁免）
- **提审后补件声明**（#511 先例透明覆盖）：豁免判定收窄修复+2 例回归在提审后 10 分钟内补入（自体应用狗粮当场暴露，生产代码 1 处逻辑改动：`_extract_deliverable_section` 抽出+豁免判定收窄），补件后基线 134 passed（126+8）
- L3 待活体：下一次「忘 commit 提审」当场被拦

**边界**：只加 complete 端校验，review/claim 路径未动 ✅；识别启发式先小后大（反引号路径），识别不出 WARNING ✅；code_files 声明仍归 #363 门禁管（本单补报告交付物节盲区，两门禁互补不重叠）✅；#505 约定层不动 ✅；review 路径的负向判词门禁（#433）未动。

**需要谁动作**：欧阳锋终审本单；各生产者知悉——complete 前交付物须先 feat commit（忘 commit 会被 E040 门禁当场拦下并给补救命令）；王语嫣知悉——编排/诊断类任务在执行报告写「纯任务单修改」即走豁免通道。
