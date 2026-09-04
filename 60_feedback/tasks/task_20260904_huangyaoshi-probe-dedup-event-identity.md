---
id: task_20260904_huangyaoshi-probe-dedup-event-identity
title: "#635 返工：conveyor 陈旧事件去重键改按事件身份（行文本被划销改写后匹配失效，15:17 复发实证）"
seq: 636
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: "#635 PASS A- 后复发实证：08-27 陈旧 liveness 事件 14:47/15:17 继续重登记——王语嫣值守拍触发退回"
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-04T07:47:07.121628+00:00'
---

# #636 探针去重键修根（黄药师，#635 返工）

## 背景

#635 的去重加的是「段内全文匹配已划销行」——但王语嫣划销动作会改写行文本（加 ~~ 和处置后缀），原行不复存在，匹配永远落空。实证：08-27 陈旧 liveness 事件在 #635 终审后 14:47/15:17 继续重登记。

## 任务

conveyor_probe 去重键改为**事件身份**（源类型+原始时间戳+主体），与行文本无关：已划销行里含同一事件身份（行内嵌的原始时间戳可提取）即跳过。

## 验证

手工构造：把一条已划销行的事件再触发一次登记路径，确认不再上段。

## 交付

- diff + 复发阻断实证 + 执行报告
- claim/complete 走 queue_transition（complete 636）
