---

id: dk-p3-auth-cache
title: P-3：Hermes 换 API Key 后仍然 401 — auth.json 缓存覆盖 .env
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: pitfalls.md P-3
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
  - "[[tool-yitang-web-scraping-research]]"
  - "[[concept-feishu-api-pagination-trap]]"
  - "[[yt-product-kernel-key-conversion]]"
  - "[[yt-entrepreneur-key-hypotheses]]"
  - "[[dk-yitang-model-asset-capitalization]]"
  - "[[yt-skill-storyline-key-elements]]"
  - "[[tool-note-keyword-bolding]]"
  - "[[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]]"
  - "[[dk-p16-validate-reads-state-json]]"
  - "[[dk-f3-state-json-race-condition]]"
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown# P-3：Hermes 换 API Key 后仍然 401 — auth.json 缓存覆盖 .env

---

## 原始表述/核心洞察

> **症状**：更新 `~/.hermes/profiles/*/.env` 中的 `KIMI_API_KEY` 后重启服务，仍然 HTTP 401，日志显示用的还是旧 Key。用户和欧阳锋多轮尝试换新 Key 无效——"系统顽固用旧的覆盖新的"。
>
> **根因（3 层）**：
> 1. **改错了 .env** — Hermes 加载 `~/.hermes/.env`（全局），不是 `~/.hermes/profiles/<name>/.env`。profile 下的 .env 根本不被读取
> 2. **auth.json 缓存** — `~/.hermes/auth.json` 的 `credential_pool.kimi-coding[]` 缓存了旧 Key 的 access_token + `last_status: exhausted`，Hermes 优先用缓存而不是重读 env
> 3. **Provider 名** — 之前用过 `kimi-for-coding`，正确是 `kimi-coding`
>
> **对策**：API Key 换新时三处同步更新：`~/.hermes/.env` + `~/.hermes/auth.json` credential_pool + `~/.hermes/profiles/*/config.yaml` provider 名。改完后清掉 auth.json 里的 `last_status/exhausted` 和 `last_error_code/401`。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **确认正确的 .env 位置**：
   - src_unknown
   - src_unknown

2. **清理 auth.json 缓存**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

3. **核对 provider 名**：
   - src_unknown
   - src_unknown

4. **重启并验证**：
   - src_unknown
   - src_unknown

5. **建立 Key 轮换 SOP**：
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|
|---|---|---|
| 改错 .env 文件 | `profiles/<name>/.env` 已更新，但全局 `~/.hermes/.env` 仍是旧 Key | Hermes 只读取全局 .env，profile 下的 .env 不被加载 | 修改 `~/.hermes/.env`，并确认服务重启后读取的是该文件 |
| auth.json 缓存旧 token | auth.json 中 `credential_pool.kimi-coding[].access_token` 仍是旧值 | Hermes 优先使用缓存的 access_token，而不是重新从 .env 读取 | 删除对应 provider 下的旧 access_token 缓存条目 |
| 状态标记导致跳过 | `last_status: exhausted` 或 `last_error_code: 401` 仍存在 | Hermes 认为该 Key 已死，直接跳过不再尝试 | 清除 `last_status` 和 `last_error_code` 字段 |
| provider 名不一致 | config.yaml 用 `kimi-coding`，auth.json 键名为 `kimi-for-coding` | credential_pool 键名与 config 不匹配，导致缓存/配置无法对应 | 统一 provider 名，并同步 auth.json 的 credential_pool 键名 |
| 只改一处就验证 | 全局 .env 改了但 auth.json 没清，或反之 | 三处状态（.env / auth.json / provider 名）未同步 | 建立 Key 轮换 checklist：三处全部修改并清除状态标记后再重启验证 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown

