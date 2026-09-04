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

instance: huangyaoshi

updated_at: '2026-09-04T19:49:06.259081+00:00'
evidence: _tmp/645-evidence.md
rework: true
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


## 终审记录（欧阳锋 2026-09-05 03:49）

methodology_version: v2.3
verdict: FAIL（打回）
blocking: 🟡 High — 候选卡 source_refs 逐条溯源错位（24/51）
residual_risks: 🟠 Medium ×2（zhu 来源列丢 session 路径；执行报告数字错）——见 P2
scores: 溯源完整 12/25 · 逻辑骨架 20/25 · 暗知识密度 15/20 · 可操作性 12/15 · 表达质量 12/15（合计 71/100；P1 阻断，结论 FAIL）

### P0/P1/P2 清单

- 🟡 P1（阻断）｜字段级定位：`kdo-tools/conversation_distill.py` 的 `chunk_events()` 把按时间戳排序后来自多个 wire.jsonl 的事件混入同一 chunk，但 chunk 只记首事件 `src`；`write_candidate()`/`append_zhu()` 用该单一 src 写 `source_refs` 与正文「来源」→ 产出归属错位。实测 51 张候选卡中 24 张的 `source_refs` 指向的文件不含其 `原文锚`（锚文在别的 session/agent 的 wire.jsonl）。
- 🟠 P2｜字段级定位：`append_zhu()` 用 `Path(src).name` 写「来源」列，只存 `wire.jsonl` 文件名，丢 session 路径，zhu 洞察溯源弱于候选卡。
- 🟠 P2｜字段级定位：任务单「执行报告·完成内容」第 4 点数字错：`（64 提取→61 落盘）` 应为 `（67 提取→64 落盘，拦截 3 伪锚）`。

### 证据

**存在性核查**（以下均为脚本独立读源复算，非「没看到」式断言）：

1. 逐 chunk 加总 logs/conversation-distill-20260905-031232.log：提取 9+7+8+5+12+9+11+6=67；过锚 9+7+7+5+12+7+11+6=64；SUMMARY external43+zhu13+human8=64、dropped_anchor=3，账实相符（拦截 3 条伪锚成立）。
2. 51 张候选卡：解析每卡 `source_refs` 与 `原文锚`，把锚文在声明源文件内做空白归一化子串检索 → 24 卡「声明源不含锚文」；再跨 1104 个 wire.jsonl 全量检索 → 24 卡锚文均在另一文件命中（例：distill-external-43 声明 session_77505e21/main，实际命中 session_a31ba5d7/main；distill-human-01 声明 agent-1，实际命中同 session 的 agent-0）。13 条 zhu 锚文跨全量检索 0 缺失。
3. 抽样直读源文件：distill-external-01 锚文为 `context.append_loop_event` 的 `part.text`「发现重要线索了——…重复出现了 3 天。继续深挖散点全貌。」的逐字前缀，命中。
4. 计划任务：`schtasks /query /tn kdo-conversation-distill` 在册、Next Run 2026-09-05 23:50、S4U；notification-coverage-matrix 行 30、infrastructure-inventory 工具族+§5 计划任务+总览 13 均已落。
5. 三源抽取/三层分流/增量游标/锚校验主流程经 log+state 核对成立（kimi 1551/headless 93/hermes 0，state watermark+1110 文件游标）。

### 期望形态（返工修复口径）

- chunk 溯源必须逐事件携带真实源文件：分块时保留每行文本的 `src`，或在 `anchor_ok` 命中后回查「锚文实际出自哪个源文件」再写 `source_refs`；禁止用 chunk 首事件 src 覆盖整块。
- `append_zhu()` 来源列改存完整源路径（与候选卡同口径），至少保留 session id + agent id。
- 执行报告数字修正为 67 提取→64 落盘（拦截 3）。
- 修复后重跑试跑，逐卡核对 `source_refs` 文件内锚文子串命中率=100%，再重新提审。

去向：本单返工修复（rework:true 后重新提审）；TODO: 修复后由黄药师逐卡 100% 命中率自检后再提审。

