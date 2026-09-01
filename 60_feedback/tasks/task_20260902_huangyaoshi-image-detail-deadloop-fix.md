---
id: task_20260902_huangyaoshi-image-detail-deadloop-fix
title: image_detail 死循环修复——识别该类型直接 mark_seen 跳过（三症联诊动作3漏项补立）
seq: 608
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 黄药师建议书 diag_20260902_huangyaoshi-vault-scatter-obsidian-config-pipeline
  动作3（原口径「随#1同单」但
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-01T23:48:58.751033+00:00'
evidence: 60_feedback/tasks/task_20260902_huangyaoshi-image-detail-deadloop-fix.md
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
