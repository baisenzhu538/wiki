---
id: task_20260902_huangyaoshi-dispatch-mechanism-converge
title: dispatch 机制收口（散点审计 R6，P1）：watch_inbox 目录树裁剪 + dispatch 停发并入口径
seq: 605
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P1
updated_at: '2026-09-02T01:25:00+08:00'
---

# #605 dispatch 机制收口

## 背景与王语嫣裁定

风清扬审计 P0-B-4/5：watch_inbox 扫描器无目录树裁剪（单份 dispatch 达 863KB/7908 行），且 dispatch 台账 17 份**零签收**（发了没人读）。

**裁定（王语嫣 09-02）**：dispatch 台账**停发**——队列/收件箱监控职能已由看门狗 v5（clock_watchdog.py，09-02 上线）覆盖，不建第二套无人消费的壳。watch_inbox **保留 pending-cards 登记职能**（INBOX-PENDING 看板段是产线入口，不能砍）。

## 范围

1. watch_inbox 加目录树裁剪：只扫 `00_inbox/pending-cards/` 与顶层新素材，`Handle`/`_vlm_output`/`ocr_ingest` 等大目录树不进扫描面（黑名单或深度限制，施工者选简单可靠的）。
2. dispatch 落盘逻辑下线（保留代码注释标注下线原因+日期，或配置开关默认关）。
3. `60_feedback/inbox-queue/` 存量 49 个 dispatch 文件：移 `90_control/.sandbox/quarantine-20260902/inbox-queue/`（不删，留查）。

## 安全栏

- 下线前先确认看门狗 v5 的告警面确实覆盖「队列三态 + gate 增量」（读 clock_watchdog.py 核实，不凭审计转述）。
- pending-cards 登记路径零改动——下线 dispatch 后实跑一次确认 INBOX-PENDING 看板段仍正常登记。

## 交付物

裁剪后扫描面说明 + dispatch 下线证据 + 存量归档 + 实跑验证留痕 + 执行报告五字段。

## 验收

欧阳锋终审：watch_inbox 实跑零 863KB 级产物 + INBOX-PENDING 登记功能实测正常 + 存量 dispatch 已归档。
