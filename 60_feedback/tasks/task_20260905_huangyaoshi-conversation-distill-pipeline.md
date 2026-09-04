---
id: task_20260905_huangyaoshi-conversation-distill-pipeline
title: 对话蒸馏管线：会话上下文→三层分流（外部知识→知识域 / 对老朱洞察→personal-os / 对他人洞察→人域）——老朱长期机制
seq: 645
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-05
decision_source: 老朱 09-05 定方向：对话上下文长期蒸馏，知识+洞察三层分流不同领域
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-04T19:26:58.596880+00:00'
evidence: _tmp/645-evidence.md
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

## 执行报告（黄药师 2026-09-05 03:22）

**交付物**：
- `kdo-tools/conversation_distill.py`（蒸馏器：kimi wire/headless/hermes 三源抽取 → 三层提示词蒸馏 → 分流落盘 → 原文锚强校验）
- `kdo-tools/kdo-conversation-distill.cmd` + `kdo-tools/kdo-conversation-distill.xml` + 计划任务 kdo-conversation-distill（每日 23:50，S4U 无窗，已注册）
- `30_wiki/personal-os/zhu-conversation-insights.md`（13 条 zhu 洞察样本，新建 personal-os 同族文件，未动王语嫣维护的 zhu-feedback-patterns）
- `90_control/notification-coverage-matrix.md` 行 30 + `90_control/infrastructure-inventory.md`（工具族行 + §5 计划任务行 + 总览计数 12→13）
- 样本候选卡 51 张落盘 00_inbox/pending-cards/（distill-external/human-20260905 系列）——**按 gitignore 铁律 00_inbox 不进 git，验收走盘上肉眼**；增量游标 .kdo/conversation_distill_state.json 为运行时状态（.kdo/* 忽略规则内），均非入仓交付物

**完成内容**：
1. 蒸馏器：三源抽取（kimi wire 事件流解析 append_message/content.part；headless 日志按文件名日期过滤+硬切块；hermes state.db Windows 侧为空镜像，实现为优雅跳过——gateway 实库在 WSL 侧）；三层提示词一次调用出 JSON；chunk 7000 字、默认上限 8 块（F-062 成本纪律）
2. 分流写死：external/human → pending-cards 候选（过王语嫣门禁）；zhu → personal-os 追加（隐私面不外流）
3. 节奏：独立 23:50 计划任务（与 daily-review 23:37 错开）；增量=per-file 字节游标+全局水位 ts
4. 红线：anchor_quote 空白归一化子串强校验，不过即弃——试跑实证拦截 3 条伪锚（64 提取→61 落盘）

**验证**：
- dry-run 09-02~05：抽取 kimi 1550 条 / headless 93 段 / hermes 0（空镜像跳过），分块 4602 个，修复了 headless 整文件 16MB 单块 bug 后复跑通过
- 正式试跑 8 块：8 次 LLM 调用 0 失败，SUMMARY {"external":43,"zhu":13,"human":8,"dropped_anchor":3,"calls":8,"failed_calls":0}；三类各 ≥1 条带原文锚样本已人工抽查（distill-external-01 / distill-human-01 / zhu-conversation-insights 13 条表格），锚文确为会话原文逐字
- 增量游标：`--max-chunks 0` 日常模式跑通，state 写入 watermark+1110 文件游标
- 计划任务：`schtasks /query /tn kdo-conversation-distill` 在册，下次运行 2026-09-05 23:50，S4U

**边界**：
- hermes 会话源未实证（Windows 侧 state.db 为 0 字节空镜像，gateway 实库在 WSL；代码路径已就绪，有库即读）
- 试跑只吃了 4602 块中的前 8 块（kimi wire 优先排序）；全量历史回扫成本未评估，默认只走每日增量
- 候选卡分类边界（如 human 层混入 agent 协作事实）由王语嫣门禁把关，蒸馏器只做粗分流
- LLM 走 `~/.kdo/config.yaml`（kimi-for-coding），与 label 管线同源配置

**需要谁动作**：
- 欧阳锋：终审本单
- 老朱：肉眼验收三类样本（pending-cards/distill-*-20260905-* 与 personal-os/zhu-conversation-insights.md）
- 王语嫣：pending-cards 蒸馏候选卡过门禁（日常量：每日新增随 inbox 行 9 通道上浮）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
