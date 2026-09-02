---
id: task_20260902_huangyaoshi-watch-inbox-pipeline-dirs-fix
title: watch_inbox 扫描面回补管线落点子目录（#605 裁剪误伤：wechat-collect 等管线落点出扫描面，05:47 四件静默漏登记实证）
seq: 619
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 问「偶遇→inbox→拉起工作流这条线正常吗」→ 王语嫣逐环实测发现第二环断裂
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T14:31:26.678066+00:00'
---

# #619 watch_inbox 扫描面回补（黄药师）

## 背景（实测证据）

#605 dispatch 收口时把 watch_inbox 扫描面裁成「00_inbox 顶层文件 + pending-cards/」（watch_inbox.py L81-87）——但 wechat/BV 管线的实际落点是子目录：`wechat-collect/`、`video_transcripts/`、`video_transcripts_small/`。实证：`00_inbox/wechat-collect/src_wechat_*.md` ×4（09-02 05:47 采集落盘）未出现在 INBOX-PENDING 任何一行（grep 0 命中）——静默漏登记。

裁剪的原始目的（防 863KB dispatch 巨件）仍成立：Handle/、_vlm_output/、ocr_ingest 等大目录树**继续排除**。

## 任务

`kdo-tools/watch_inbox.py` 扫描面改为：顶层文件 + 白名单子目录（`pending-cards/`、`wechat-collect/`、`video_transcripts/`、`video_transcripts_small/`），其余子目录不扫。白名单写成常量便于日后增删。

## 验证

- 改完实跑一次扫描：05:47 的 4 件 wechat-collect 应被登记进 INBOX-PENDING（补登记或验证幂等均可）
- 大目录（Handle/ 等）确认不在扫描结果里

## 交付

- diff + 实跑登记证据 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 619）
