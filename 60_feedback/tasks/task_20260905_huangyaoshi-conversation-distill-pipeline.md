---
id: task_20260905_huangyaoshi-conversation-distill-pipeline
title: 对话蒸馏管线：会话上下文→三层分流（外部知识→知识域 / 对老朱洞察→personal-os / 对他人洞察→人域）——老朱长期机制
seq: 645
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-05
decision_source: 老朱 09-05 定方向：对话上下文长期蒸馏，知识+洞察三层分流不同领域
reviewer: 欧阳锋
---

# #645 对话蒸馏管线（黄药师）

## 背景

老朱长期机制：他与各 agent 的对话上下文里持续沉淀三类资产——①外部知识（客观世界）②对老朱的洞察 ③对他人的洞察。时间胶囊（.kdo/time-capsule.db + time_capsule.py）已有底座。

## 任务

1. **蒸馏器**：`kdo-tools/conversation_distill.py`——读会话记录（kimi sessions wire + headless logs + hermes sessions），按三层提示词蒸馏：外部知识 / 对老朱洞察（思维模型/优缺点/决策模式）/ 对他人洞察（如马晶晶案主这类进入对话的人）
2. **分流规则**（写死）：外部知识→候选卡落 00_inbox/pending-cards（过王语嫣门禁）；对老朱洞察→30_wiki/personal-os/（zhu-feedback-patterns 同族追加）；对他人洞察→人域 human-insights 候选（pending-cards 过门禁）
3. **节奏**：每日随 kdo-daily-review 批次跑（或独立 23:50），增量蒸馏（记录上次游标）
4. **红线**：蒸馏≠编造——每条产出必须带原文锚（哪段对话哪句）；隐私面：对老朱洞察只进 personal-os 不外流

## 验证

- 用 09-02~09-05 的真实对话历史试跑：产出三类各≥1 条带原文锚样本，老朱肉眼验收

## 交付

- 蒸馏器+分流实证+样本三件+执行报告
- claim/complete 走 queue_transition（complete 645）
