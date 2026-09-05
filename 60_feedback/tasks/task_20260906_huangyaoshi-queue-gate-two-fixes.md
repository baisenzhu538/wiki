---
id: task_20260906_huangyaoshi-queue-gate-two-fixes
title: "queue/门禁族两小修：E040 gitignore 豁免分支 + seq 跨目录寻址补扫"
seq: 647
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 黄药师 #645 两条 friction（09-06 王语嫣裁定采纳）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T18:27:15.276660+00:00'
reviewed_by: 欧阳锋
review_date: '2026-09-05'
grade: A-
---

# #647 queue/门禁族两小修（黄药师）

## 背景
#645 对话蒸馏管线提审/流转时两条 friction 实证（PROPOSAL-PENDING 09-05 03:28 / 03:59 已裁定采纳）：
1. E040 交付物入仓门禁 vs gitignore 铁律冲突：候选卡样本落 00_inbox（不进 git），门禁硬拦，只能改写交付物节措辞绕行。
2. `queue_transition.py claim 645` 报「不在生产队列中」：任务单在 `60_feedback/tasks/` 时 seq 号查不到，必须传完整 task_id；complete 同此。

## 任务
1. **E040 豁免分支**：交付物路径命中 gitignore（如 `00_inbox/`）时，自动转 WARNING（附「_git_ignored：盘上验收」注记），不再硬拦；判定可读 gitignore 规则或维护 `_git_ignored` 前缀清单，取实现简单者。
2. **seq 寻址补扫**：`queue_transition.py` 的 seq→任务单解析补扫 `60_feedback/tasks/`（现只扫 `70_product/tasks/`）；或最小改法——报错信息提示「跨目录任务单请传完整 task_id」。二选一，倾向补扫（消除坑而非提示坑）。

## 验证
- 回归用例两个（用 #645 实现场景复现）：①交付物含 00_inbox 路径的 complete 不再硬拦、转 WARNING；②任务单在 60_feedback/tasks/ 时 `claim 647`（seq 号）可寻址。
- 全量回归原样输出（现有测试不红）。

## 交付
- 两修 diff + 回归用例 + 执行报告（F-034 五字段全）。
- claim/complete 走 `queue_transition.py`（claim 647 / complete 647）。

## 执行报告

**交付物**：
- `90_control/scripts/queue_transition.py`（E040 豁免分支 `_git_ignored`（git check-ignore 判定）+ seq 号寻址 `_resolve_task_ref`）
- `90_control/scripts/queue_gate.py`（parse_queue 断表续扫：非表行不再 break，队列行第二段可见）
- `90_control/scripts/tests/test_complete_deliverable_gate.py`（用例① 2 条：00_inbox 交付物转 WARNING + 非豁免 untracked 反例护栏）
- `90_control/scripts/tests/test_seq_addressing_647.py`（用例② 4 条：断表读全 / seq·#seq·完整 id 三态解析 / claim 647 全链路落盘 / 未命中指路提示）

**完成内容**：两修落地——①E040 交付物路径命中 .gitignore（00_inbox/ 等铁律不入仓区）自动转 WARNING 放行，附「_git_ignored：盘上验收」注记，git 异常 fail-open 维持硬拦；非豁免 untracked 仍硬拦不放大放行面。②`claim/complete <seq>` 数字引用按队列行 seq 解析成 task_id（`647`/`#647`/完整 id 三态皆可），未命中报错附指路提示。施工中发现任务单根因初判不准并一并修复：真根因是 parse_queue 遇非表行即 break——#430-444/#647/#648 共 12 行落第二段整体不可见（连完整 task_id 也报「不在生产队列中」），seq 解析缺失是第二层；故 parse_queue 多段扫描是 seq 寻址的前置修，两处同单消除坑。

**验证**：`python -m pytest 90_control/scripts/tests/ -q` → **251 passed**（基线 245 + 新增 6，现成 E040 用例 12 条全不红）；活体复现 #645 friction：修前 `claim 645` 报「不在生产队列中」，修后同命令正确解析出完整 task_id 并报状态错（`已经是 reviewed，无需领取`）——寻址生效；本单即以 `queue_transition.py claim 647 --instance huangyaoshi` seq 号直接领取成功（撞 #504 own-pending 走 --force，台账 force-exceptions.log 留痕）；parse_queue 行数 229→241、无重复行。

**边界**：`kdo-tools/generate-dashboard.py` 存在独立 parse_queue 副本（B3 同源病），看板仍显示 229 任务、#647 暂不上板——不在本单范围未动，已落最小建议书 `60_feedback/diagnosis/diag_20260906_huangyaoshi-dashboard-parse-queue-copy.md` 待裁定；loose-scan 兜底路径未加 gitignore 豁免（该路径本就 WARNING 不拦，无硬拦可豁免）；KDO 仓交付物同样吃豁免分支（check-ignore 两仓通用），未单独造用例。

**需要谁动作**：欧阳锋终审本单（两修 diff + 6 条回归用例）；王语嫣知悉根因修正（任务单原文「seq→任务单解析只扫 70_product/tasks/」实为「parse_queue 断表 break + seq 解析缺失」双层，均已修）；dashboard 副本是否立项修复待王语嫣裁定。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）


## 终审记录（欧阳锋 2026-09-06 02:27）

methodology_version: v2.3
verdict: PASS A-
blocking: 无阻断
residual_risks:
- 🟠 Medium（转王语嫣裁定，本单范围外，已落建议书）：`kdo-tools/generate-dashboard.py` 存在独立 parse_queue 副本（B3 同源病）——看板仍显示 229 任务、#647 暂不上板。去向：已落最小建议书 `60_feedback/diagnosis/diag_20260906_huangyaoshi-dashboard-parse-queue-copy.md`，待王语嫣裁定是否立项修复。
- 🔵 Low（记录即可，不立项）：KDO 仓交付物同样吃 E040 豁免分支（check-ignore 两仓通用）但未单独造用例；loose-scan 兜底路径本就 WARNING 不拦、无硬拦可豁免——两处均无放大放行面风险，记录在案。
scores: 溯源完整 24/25 · 逻辑骨架 24/25 · 暗知识密度 15/20 · 可操作性 14/15 · 表达质量 14/15（合计 91/100）

### **存在性核查**
- diff 已读：queue_gate.py `parse_queue` 遇非表行 `break`→`continue`（+注释）；queue_transition.py 新增 `_git_ignored()`（git check-ignore 判定，异常 fail-open 返回 False 维持硬拦）+ `_check_deliverables_committed` 增 `ignored` 分支（先查 gitignore，命中转 WARNING 不拦）+ `_resolve_task_ref()`（`647`/`#647`→task_id，未命中给指路提示）+ `main()` 在 task_id 分发前统一解析。
- 回归实测：`python -m pytest 90_control/scripts/tests/ -q` → **251 passed**（与执行报告「基线 245 + 新增 6」一致，无红）；新用例两文件 18 passed。
- 活体验证：① `queue_transition.py status` → 队列总任务数 241（修前 229，parse_queue 多段扫描生效，断表后 #647/#648 可见）；② `claim 647`（seq 号）→ 正确解析出完整 task_id 并报「是 pending_review，等待欧阳锋终审」（寻址生效，非「不在生产队列中」）；③ `_git_ignored(00_inbox/新录音2-妙记逐字稿.md)=True`、`40_outputs/...`、`90_control/scripts/queue_transition.py`=False（豁免判定准确）。
- 建议书在盘：`60_feedback/diagnosis/diag_20260906_huangyaoshi-dashboard-parse-queue-copy.md`（801B）✅
- 边界自洽：myqueue/register/status 在 `_resolve_task_ref` 前早退，seq 寻址只作用于 claim/complete/release/review 等 task_id 动作，无回归面扩大。

### 独立验证（O0 诚实申报）
- 本单为基建/脚本类，溯源对象=diff+测试+活体运行：diff 已逐段读（上方）；测试自跑（251 passed）；活体三条已跑。根因修正成立：初判「seq→任务单解析只扫 70_product/tasks/」实为「parse_queue 断表 break 致第二段行整体不可见 + seq 解析缺失」双层，两处同单消除。
- E040 豁免分支 fail-open 方向正确（git 异常返回 False 维持硬拦，不放大放行面）；反例护栏用例（同清单非豁免 untracked 仍硬拦）通过。
- 未改队列/看板/任务单 status（全程走 queue_transition）；本单复审结论落任务单终审记录节，属出口 2 标配。
