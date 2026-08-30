---
id: dk-feishu-bot-slow-session-hygiene
title: 飞书 bot 变慢的隐形杀手——会话膨胀与 hygiene 压缩卡死
type: dk
dark_knowledge_type: heuristic
status: enriched
author: 老顽童
reviewed_by: 待审
confidence: 0.85
trust_level: high
language: zh-CN
domain:
  - agent-infrastructure
  - hermes-operations
aliases:
  - 飞书bot慢
  - hygiene压缩卡死
  - 会话膨胀
  - code plan端点
source_context:
  - 08-30 五绝飞书 bot 生产排障实录（王语嫣 524s 响应排查）
source_refs:
- 08-30 五绝飞书 bot 生产排障实录（gateway.log / state.db / config.yaml 实证，老顽童）
- AppData/Local/hermes/profiles/wangyuyan/logs/gateway.log
- AppData/Local/hermes/hermes-agent/gateway/run.py
tags:
  - audience:general
  - scene:troubleshooting
  - skill-level:intermediate
  - 运维
  - Hermes
discoverable_by:
  - 飞书 bot 慢
  - 会话膨胀
  - hygiene 压缩
  - 智谱 code plan 端点
related:
- '[[framework-hermes-multi-bot-feishu-setup]]'
quality_labels:
- cited
- validated
updated_at: '2026-08-30'
created_at: '2026-08-30'
---
# 飞书 bot 变慢的隐形杀手——会话膨胀与 hygiene 压缩卡死

> **Burn line**：飞书 bot 突然从秒回变成 8 分钟才回，90% 不是模型慢，是会话膨胀到几十万 token 触发了会卡死的 hygiene 压缩。
>
> **来源**：2026-08-30 五绝飞书 bot 生产排障实录（王语嫣 524s 响应排查；config.yaml / gateway.log / state.db 实查）。

---

## 来源人与来源语境

| 字段 | 内容 |
|:---|:---|
| source_person | 老顽童（08-30 排障） |
| source_context | 五绝飞书 bot 从 DeepSeek 切到智谱 code plan 后，王语嫣响应从 8s 恶化到 524s；查日志、state.db、config.yaml 定位。 |

## 原始表述

> 「Session hygiene compression for session xxx still streaming after 240s (last progress 0.0s ago) — extending wait (ceiling 600s)」
>
> 「📦 Preflight compression: ~500,868 tokens >= 500,000 threshold」
>
> 「Session hygiene: 433 messages, ~131,550 tokens (actual) — auto-compressing (threshold: 85% of 1,000,000 = 850,000 tokens)」[conf=0.85, source=gateway.log 实证]

---

## 一句话定义

飞书 bot 变慢的直接机制：**长会话（消息数 ≥ hygiene_hard_message_limit，默认 400）触发 Session hygiene 自动压缩；压缩要消化几十万~上百万 token 的完整历史，LLM 一次处理不完 → 压缩任务永远 streaming 无进展 → gateway 干等最多 600s**，用户感知就是"慢得像蜗牛"。

## 暗知识展开

### 1. 表象与真实根因的错位

- 表象：切到智谱 glm-5.3-flash 后变慢 → 第一反应是"智谱比 DeepSeek 慢"
- 实测：智谱 coding 端点与 DeepSeek v4-flash 原始速度几乎一样（差 0.2~0.4s；TTFT 0.7~1.4s）
- 真实根因：会话 input_tokens 累积到 **105 万**（state.db 实查 `input_tokens=1,050,499, message_count=438`），触发 hygiene 压缩，压缩卡死 600s

### 2. 根因链（按排查顺序）

1. **会话膨胀**：飞书 DM 会话长期复用，几周累积几十万~百万 token。查证：`SELECT id, message_count, input_tokens FROM sessions WHERE session_key LIKE '%feishu%'`
2. **hygiene 压缩卡死**：`compression.hygiene_hard_message_limit` 默认 **400**——消息数超线即强制压缩，不看 token 数。压缩要消化整个巨型历史，LLM 一次处理不完 → 压缩任务永远 streaming 无进展 → gateway 等 600s
3. **cron deliver=feishu 喂大会话**：定时 job 每 30 分钟往飞书会话发内容 → 会话永不 idle → 永不自动重置 → 无限膨胀
4. **智谱缓存未预热**（若刚切模型）：命中率 12% → 87% → 100% 爬升，越用越快（非根因，但叠加感知）

### 3. 修复三件套

1. **重置膨胀会话（必须从 DB 终结，只删 sessions.json 会被 gateway 恢复逻辑挂回）**：
   ```bash
   cd <profile_dir> && python -c "
   import sqlite3, time
   conn = sqlite3.connect('state.db')
   conn.execute(\"UPDATE sessions SET end_reason='session_reset', archived=1, ended_at=? WHERE id='<session_id>'\", (time.time(),))
   conn.commit()"
   # 再删 sessions.json 里对应映射；重启 gateway
   ```
   重启后确认日志出现 `pruning stale sessions.json entry` 才算干净。
2. **调大 hygiene_hard_message_limit**：400 对高频飞书 agent 太激进 → `compression.hygiene_hard_message_limit: 2000`
3. **cron deliver 改 local**：编辑 `<profile>/cron/jobs.json`，`deliver: feishu` → `deliver: local`，改完重启 gateway

### 4. 智谱 code plan 端点暗坑（同批排障发现）

- code plan 额度**只认 coding 专用端点** `https://open.bigmodel.cn/api/coding/paas/v4`；普通 `api/paas/v4` 报 429「余额不足或无可用资源包」——是假象，不是没钱
- base_url 要**三处一致**，漏一处就被覆盖：config.yaml `model.base_url` + .env `GLM_BASE_URL` + auth.json credential_pool 里 zai 条目的 base_url
- 判断模型快慢的正确方法：直接 API 基准（urllib 打 chat/completions 测 total + streaming TTFT），不要凭"感觉"

## 案例佐证

| 场景 | 现象 | 根因 | 修复 |
|:---|:---|:---|:---|
| 王语嫣 19:51 飞书消息 | 524s 响应，api_calls=32 | 会话 input_tokens 105 万，hygiene 压缩卡死 | DB 终结会话 + limit 400→2000 + cron deliver 改 local |
| 王语嫣 19:25~19:34 消息 | 8~9s 响应，api_calls=1 | 会话尚小 | —（对照组，证明不是模型问题） |
| 智谱切后首次调用 | 命中率 12% | 缓存未预热 | 连续调用后 87%→100%，延迟 4.1s→2.2s |

## 反例与边界

- **不是所有慢都是会话问题**：如果 `api_calls=1` 但 latency 高，才是模型/端点问题；`api_calls` 多（如 32）且伴随 compression 日志，才是会话问题
- **hygiene_hard_message_limit 调大是缓解不是根治**：会话仍会增长，需配合 session_reset（idle 自动重置）或定期手动重置；调太大（如 5000+）会逼近 context_length 上限，压缩会更痛苦
- **cron deliver=feishu 不是绝对坏**：若 job 本就该通知用户，可保留但配合会话隔离（独立 session）或低频调度

## 行动指引

1. 飞书 bot 变慢 → 先查 gateway.log 有无 `Session hygiene compression ... still streaming`
2. 有 → 查 state.db 该会话 input_tokens / message_count
3. 超 400 条或 tokens 巨大 → DB 终结 + 清 sessions.json + 重启
4. 同时检查该 profile 的 cron jobs，deliver=feishu 的高频 job 改 local
5. 全厂预防：四个飞书 bot 的 hygiene_hard_message_limit 统一调到 2000（已做 08-30）
