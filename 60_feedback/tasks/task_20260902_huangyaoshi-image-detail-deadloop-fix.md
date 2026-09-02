---
id: task_20260902_huangyaoshi-image-detail-deadloop-fix
title: image_detail 死循环修复——识别该类型直接 mark_seen 跳过（三症联诊动作3漏项补立）
seq: 608
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 黄药师建议书 diag_20260902_huangyaoshi-vault-scatter-obsidian-config-pipeline
  动作3（原口径「随#1同单」但
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T00:15:57.886222+00:00'
evidence: 60_feedback/tasks/task_20260902_huangyaoshi-image-detail-deadloop-fix.md
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A
---

# #608 image_detail 死循环修复（黄药师）

## 背景

黄药师三症联诊症状 3 实测暴露的真 bug：采集链监控对 image_detail 类型链接死循环重试（不 mark_seen，每 10 分钟空转重试）。原建议口径「随 #601 同单」，但 #601 任务单未含此项（提审后不可追加，E025），补立本单。

## 任务

采集链监控脚本中识别 image_detail 类型 → 直接 mark_seen 跳过，不进解析重试。

## 红线

- 小改单点，不碰 #601 刚终审的去重/归一化逻辑（若 #601 未终审完成需等其 reviewed 后动手，防同文件冲突）
- 改完实跑一轮监控验证：image_detail 类链接一轮 mark_seen 后不再重复出现

## 交付

- 修复 diff + 实跑验证证据（前后两轮日志对比）
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 608 附证据）

---

## 执行报告（2026-09-02 huangyaoshi-kimi）

**交付物**：`kdo-tools/wechat_link_monitor.py` 单点修复（commit `7d2e73837`）+ 两轮实跑日志 `_tmp/608-round1.log` / `_tmp/608-round2.log`。

**完成内容**：公众号分支（main 循环 L451 起）加前置识别——URL 含 `pages/image_detail` 即打印跳过理由 + `mark_seen(url)` + `continue`，不进 `fetch_mp_article` 解析重试。5 行新增，零改动 #601 去重/归一化逻辑（diff 仅公众号分支内插入段）。

**验证**（前后两轮实跑对比）：
- 修前基线：`seen_links.txt` 中 image_detail 记录 = 0（3 条 08-31 00:14 链接循环重试 ~29h，diag 实证）
- Round 1：新链接 3 个=正是那 3 条 image_detail → 全部 ⏭️ 跳过 + mark_seen（seen_links.txt image_detail 计数 0→3），exit 0
- Round 2：新链接 0 个（共扫 10）——3 条不再重复出现，死循环封死 ✓

**边界**：只动 image_detail 一类；其他失败语义（抓取失败不记 seen 下轮重试）保持不变；头条/卡片直链等既有分支零改动。

**需要谁动作**：欧阳锋——终审 #608（验收点：diff 单点、两轮日志对比在 `_tmp/608-round1.log`/`_tmp/608-round2.log`）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/608-round1.log`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
- ⚠️ 交付物节含划痕路径 `_tmp/608-round2.log`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

---

## 终审记录（2026-09-02 欧阳锋 CLI 实例）

**等级：PASS A**

**通过维度**：
- O0 溯源：`git show 7d2e73837` 逐行核——7 行纯插入，公众号分支（main 循环 L452 起）前置识别 `pages/image_detail` → mark_seen+continue，零触碰 #601 去重/归一化逻辑（diff 仅此一段）；工作区与 HEAD 一致（git diff 空）
- 独立验证（不信报告）：`seen_links.txt` 亲查 image_detail 计数=3（L28/30/32），与 round1 日志 3 条跳过命中一致；round2 日志「新链接 0 个（共扫 10）」——3 条不再重现，死循环封死实证成立
- 版本对齐三问全过：①commit `7d2e73837` 在仓（wiki 仓=真相源）；②schtasks `wechat-link-monitor` 执行体=仓内脚本绝对路径，LastRun 08:11:11 > commit 07:48:51 且 LastResult=0——生产侧已跑新码（比"下轮将生效"更强的实证）；③审查对象=HEAD 最新态
- 红线核查：#601 已 reviewed（队列行 235，commit 6923b058a 在 7d2e73837 之前）——同文件冲突前提已解除；实跑两轮验证证据在 `_tmp/608-round1.log`/`_tmp/608-round2.log`
- 五字段执行报告在位；机器预审全绿（划痕路径提示按 #515 约定豁免）

**缺陷**：无阻塞缺陷。微瑕（内容类观察，记录即可，无需动作）：交付物节将 `_tmp/` 日志列为路径——机器预审已按 #515 划痕约定豁免提示，非内容缺陷，不构成警示级条目，不另立跟进项。

**残余风险**：image_detail 判定为 URL 子串匹配，依赖微信 `t=pages/image_detail` 当前形态；微信改参数形态时退化为旧行为（抓取失败重试），有日志可见不静默。

**矩阵核查（§3.19）**：本案改动文件 `kdo-tools/wechat_link_monitor.py` 不在第七信号 INFRA_WATCH 四面（conveyor_probe/watch_inbox/queue_transition/generate-dashboard），且不新增/修改事件类型或通知通道——总账同步纪律不适用，豁免成立。

**methodology_version**: v2.3 | **verdict**: pass | **blocking**: 无 | **residual_risks**: 见上
