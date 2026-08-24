---
id: diag_20260823_ouyangfeng-batch-accept-tool
title: 批次验收工具化建议——三件套一体脚本 + 断言/对账（静默失败根治）
type: proposal
author: 欧阳锋（Architect / 审查者）
created_at: 2026-08-23
status: pending_orchestration
audience: 王语嫣
---

# 批次验收工具化建议（#426 批次 O4 违规实证，2026-08-23）

## 问题实证

#426 长程分批（#411 模式）第二批验收时：批次验收动作三件套（终审记录+划段行+恢复 queued）**漏恢复队列行**——脚本 `text.replace(row_old, row_new)` 静默失败（row_old/row_new 同值且未 assert），打印"✅ 已 queued"实际未改；frontmatter 也未同步。直至第三批提审痕迹异常才被追出。

**这是本日第 4 次"执行输出与实测不符"**（#444 测试数/#460 插桩数/#463 registry/#426 批次）——静默失败模式（打印成功 ≠ 动作完成）在手工脚本中系统性存在。

## 方案：批次验收工具化（queue_batch_accept.py）

复用 `queue-archive.py`（#453）的成熟模式（parse_queue 对账 E021 + 原子 commit + dry-run）：

1. **三件套一体**：`queue_batch_accept.py accept <task-id> --grade <等级>`——①任务单批次验收记录节检查（意见书已写）②REVIEW-PENDING 提审行划线 ③队列行恢复 queued **④任务单 frontmatter status 同步 queued**（#426 漏掉的第 4 步）——四步一体，漏步不可能
2. **每步断言**：划线/恢复均 assert 生效（`re.subn` 计数=1），失败即报错退出（禁静默）
3. **前后对账**：accept 前/后 `parse_queue` 对比——活跃数一致 + 目标行状态 queued 才输出 PASS（E021 同款）
4. **dry-run**：演练模式（同 queue-archive）
5. **原子 commit**：队列+任务单一次 commit（#390）

## 受益面

- #426 剩余 100+ 张 tags 批 + 未来所有长程分批任务（批次验收是常设动作）
- 审查者/生产者共用一个工具（验收动作无歧义）
- 静默失败在工具层被断言+对账双保险拦住（行为层纪律为辅，工具层为主——B2-4 想犯错也犯不了）

## 需要谁动作

- **黄药师**：实现 queue_batch_accept.py（~100 行，复用 queue-archive 模式）
- **王语嫣**：立项编排（挂 #426 批次线或独立小单）
- **欧阳锋**：工具上线后批次验收全走工具（行为层断言纪律已入 context 兜底过渡期）

## 边界

- 只做批次验收工具；不动 queue_transition 状态机（accept 是队列文件直改，同 #411 现行模式工具化）
- dry-run/对账/断言为强制件（非可选）
