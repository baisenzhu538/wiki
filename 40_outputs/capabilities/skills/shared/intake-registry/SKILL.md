---
name: intake-registry
title: "intake-registry——采集登记面（watch_inbox 素材检出 + conveyor_probe 信号登记）"
description: |
  采集登记面：watch_inbox（00_inbox 新素材检出 → 看板待编排段登记 → 通知编排者）+ conveyor_probe（队列/建议书/门禁信号检出 → 登记 → 飞书通知）。
  单扫描器纪律：检出→登记→通知一条事件链，禁止第二套扫描器；划销必须逐行身份核验（E059），禁区间兜扫。
category: kdo-infrastructure
version: 1.0.0
related_skills:
  - queue-transition
  - oral-transcript-trio
encapsulates: kdo-tools/watch_inbox.py + kdo-tools/conveyor_probe.py
tags:
  - audience:wangyuyan
  - scene:intake-registry
  - 素材登记
  - 划销纪律
status: draft
reviewed_by: 待审
review_date:
grade:
updated_at: 2026-09-06
trigger:
  natural_language:
    - 新素材怎么被登记
    - 看板待编排段/INBOX-PENDING
    - PROPOSAL-PENDING 段怎么维护
    - 划销/误划销
    - 飞书通知谁在发
    - watch_inbox / conveyor_probe 手工跑
---

# intake-registry：采集登记面（watch_inbox + conveyor_probe）

> **一句话**：两个探针每 10 分钟自动跑一次——watch_inbox 管「新素材被看见」，conveyor_probe 管「队列/建议书/门禁信号被看见」。手工跑 = 与计划任务同一条命令，幂等。

## 何时用

- 素材投进 `00_inbox/` 后没人接：先确认登记面是否已把它登记到看板
- 编排者（王语嫣）处理待编排段/PROPOSAL-PENDING 段时的划销与核对
- 排查「为什么没人被通知」「为什么素材转了存、存了忘」
- 通道/看板异常时手工补一拍（与计划任务同频同命令）

**不要用于**：绕过质量门直接派活（登记面只登记不编排）；自己另写脚本扫 `00_inbox/`（单扫描器纪律，E021/E028 同族教训）。

## 怎么调

前置：`cd C:\Users\Administrator\Desktop\wiki`。

### watch_inbox：素材检出 → 登记看板

```bash
python kdo-tools/watch_inbox.py     # 手工一拍（与计划任务 kdo-inbox-watch 同命令，10min/拍）
```

- **扫描面**：`00_inbox` 顶层文件 + 白名单子目录 `pending-cards/ wechat-collect/ video_transcripts/ video_transcripts_small/`（#605/#619 口径）；白名单外的**顶层子目录**只登记一行「目录待编排」（#651，内件不全扫，防看板洪水）。
- **登记落点**：`70_product/tasks/production-queue.md` 的 `<!-- INBOX-PENDING-BEGIN --> … <!-- INBOX-PENDING-END -->` 段，条目格式：
  `- <路径>｜<P0/P2>｜<大小>｜检测到 <月-日 时分>｜待王语嫣编排`
- **通知落点**：`90_control/todos/wangyuyan.md` 追加一行（`📥 新素材 N 项`；无 agent 在岗时 `🔕` 静默落盘）。
- 状态文件：`.kdo/inbox_state.json`（判重键；删它=重扫全量 → 看板洪水，08-31 实证 7907 行）。
- 超 120 行自动溢出归档到 `70_product/tasks/archive/inbox-pending-overflow.md` 留指针。

⚠️ `--seed-top-dirs [--keep <目录名>]` 是**一次性部署动作**：把当前已存在的顶层子目录记为已见（只写 state 不登记）——误跑会把真新素材静默吞掉，日常节拍禁止使用。

### conveyor_probe：队列/建议书/门禁信号 → 登记 + 飞书通知

```bash
python kdo-tools/conveyor_probe.py             # 常规扫描（检出→登记→通知）
python kdo-tools/conveyor_probe.py --dry-run   # 登记照做，通知只打印不发送（验收/排障用）
python kdo-tools/conveyor_probe.py --json      # 结构化输出（stdout 纯 JSON，可 json.loads）
```

- 边界**硬编码**：只通知/只登记，不领取/不裁决/不流转（代码层无 claim/review/complete 能力）——状态流转只能走 `queue-transition` skill。
- 登记落点：`production-queue.md` 的 `PROPOSAL-PENDING` 段（建议书三元组自动登记，幂等，撞 doc_id 拒绝登记=E045）。
- 顺带聚合推送：`90_control/gate-blocked.log`、`90_control/force-exceptions.log`、`pending-git-commits.log` 等门禁留痕。
- 契约成文：`90_control/conveyor-probes-contract.md`（改行为先改契约）。

## 边界与红线

1. **单扫描器纪律**：一次扫描事件驱动「检出 → 登记 → 通知」。需要新信号 → 在既有探针里加探针，禁止另起一套扫描器。
2. **划销必须逐行身份核验（E059）**：编排完把对应行划掉（或清空段），但**一行一行核对路径再划**——禁区间兜扫/按行号区间批量划。实证：09-06 01:44 区间兜扫把「启动会回放转写」行误挂假去向（#645 候选卡），靠人肉发现后撤销。
3. **登记 ≠ 编排 ≠ 生产**：登记面只让素材/信号「被看见」。裁决、写任务单、入队是编排者（王语嫣）的事；生产走 `queue-transition`。
4. 手工跑与计划任务同命令、state 判重幂等——但**不要为「刷一下看板」高频手跑**，10 分钟节拍已覆盖。
5. `production-queue.md` 两个自动段（INBOX-PENDING / PROPOSAL-PENDING）由脚本维护，段头都标「勿手改」；划销是编排者对**条目行**的操作，不是改段结构。

## 常见坑（症状 → 修复）

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| 素材投放后没人接 | 落点在白名单外顶层子目录，只登记了一行「目录待编排」（#651 口径），或整夹投放早于扫描面 | 查看板目录级登记行；需要文件级跟踪 → 让编排者把该目录加进 `SCAN_SUBDIRS` |
| 整夹投放 0 登记全盲 | 白名单外目录（#651 修的就是它） | 看板应有「目录待编排」行；没有则手工跑一拍 watch_inbox 再查 |
| 看板登记暴涨几百行 | `.kdo/inbox_state.json` 被删/重建 → 全量重扫 | 停手，恢复 state 或走 SOFT_CAP 溢出归档；不要手删登记行掩盖 |
| 飞书没收到通知 | 夜间静默 / webhook 缺失（dry-run 只打印） | 排障用 `--dry-run` 看登记是否发生；`--force-notify` 仅测试用，生产红线不变 |
| 划销后素材「消失」 | 区间兜扫误划（E059） | 撤销记录 + 逐行身份核验重划；在队列行注记撤销痕迹 |
| 手改 PROPOSAL-PENDING 段后重复登记 | 段是脚本幂等重写的 | 不要手改段结构；对条目的处置（划销）单独做 |

## 失败模式（本技能特有）

| 失败 | 可识别信号 | 修复 |
|:--|:--|:--|
| 只看通知不看登记 | 「我飞书没收到 = 没素材」 | 登记是真相源（看板段），通知只是推送；以看板为准 |
| 划销凭印象 | 批量划销不看行内容 | 逐行核对路径与去向再划（E059） |
| 把登记面当派活工具 | 在登记行里写「请 XX 直接做」 | 编排走任务单入队；登记行只描述素材/信号 |

## 相关协议与卡

- 契约：`90_control/conveyor-probes-contract.md`；调度（Windows 计划任务 `kdo-inbox-watch` / `kdo-conveyor-probe`）见各脚本头注
- 扫描面口径：脚本 `watch_inbox.py` 头注（#605/#619/#651 三轮裁定与实证）
- E059 划销纪律出处：`90_control/todos/wangyuyan.md` 09-06 值守拍（误划销撤销实证）；错误模式库 E 系
- 姊妹 skill：`queue-transition`（登记面之后的所有状态流转）
