---
id: dk-p3-auth-json-cache
title: "P-3：Hermes 换 API Key 后仍然 401 — auth.json 缓存覆盖 .env"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-3"
source_refs:
  - .agent/pitfalls.md#P-3
tags:
  - "#source_type/error"
  - "#domain/system-operations"
  - "#method/debugging"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - dk-p1-model-switch-env
  - dk-p5-cc-connect-config-cascade
contradicts:
---

# P-3：Hermes 换 API Key 后仍然 401 — auth.json 缓存覆盖 .env

## 原始表述

> **症状**：更新 `~/.hermes/profiles/*/.env` 中的 `KIMI_API_KEY` 后重启服务，仍然 HTTP 401，日志显示用的还是旧 Key。用户和欧阳锋多轮尝试换新 Key 无效——"系统顽固用旧的覆盖新的"。
>
> **根因（3 层）**：
> 1. **改错了 .env** — Hermes 加载 `~/.hermes/.env`（全局），不是 `~/.hermes/profiles/<name>/.env`。profile 下的 .env 根本不被读取
> 2. **auth.json 缓存** — `~/.hermes/auth.json` 的 `credential_pool.kimi-coding[]` 缓存了旧 Key 的 access_token + `last_status: exhausted`，Hermes 优先用缓存而不是重读 env
> 3. **Provider 名** — 之前用过 `kimi-for-coding`，正确是 `kimi-coding`
>
> **对策**：
> - API Key 换新时三处同步更新：`~/.hermes/.env` + `~/.hermes/auth.json` credential_pool + `~/.hermes/profiles/*/config.yaml` provider 名
> - 改完后清掉 auth.json 里的 `last_status/exhausted` 和 `last_error_code/401`，否则 Hermes 认为 Key 已死会跳过
> - 用 `journalctl --user -u hermes-gateway-* --no-pager -n 30 | grep -i "401\|auth"` 验证无认证错误

## 使用场景

- 你换了 LLM API Key（如 Kimi Key 过期/泄露/额度用完），在 `.env` 里更新了但服务仍然 401
- 你和架构者多轮尝试换新 Key 都无效，感觉"系统顽固用旧的覆盖新的"
- Hermes 日志显示调用的仍是旧 Key 或旧 endpoint
- 你在排查"为什么改了配置文件服务行为没变"的缓存类问题

## 操作方法

1. **确认你改对了文件**：
   - Hermes 读取的是 `~/.hermes/.env`（全局），不是 `~/.hermes/profiles/<name>/.env`
   - 如果你只改了 profile 下的 .env → **改错了**
2. **同步更新三处**：
   - `~/.hermes/.env` → `KIMI_API_KEY=new_key`
   - `~/.hermes/auth.json` → 找到 `credential_pool.kimi-coding[]`，删除旧 token 条目，或把 `last_status` 从 `exhausted` 改为空
   - `~/.hermes/profiles/*/config.yaml` → 确认 provider 名是 `kimi-coding`（不是 `kimi-for-coding`）
3. **清理 auth.json 中的死亡标记**：
   - 删除 `last_status: exhausted` 和 `last_error_code: 401`，否则 Hermes 认为 Key 已死会跳过不试
4. **重启服务**：`systemctl --user restart hermes-gateway-*`
5. **验证**：`journalctl --user -u hermes-gateway-* --no-pager -n 30 | grep -i "401\|auth"` → 确认无认证错误

## 适用边界

- 仅适用于 Hermes 网关的 API Key 切换场景，不适用于其他服务（如 cc-connect、Claude Code CLI）
- 如果是首次配置（无历史 auth.json），改 `.env` 后直接重启即可——因为没有旧缓存需要清理
- **与 P-1 的区分**：P-1 是 Claude Code 配置优先级问题，P-3 是 Hermes  auth 缓存问题。两者症状相似（改了配置不生效）但根因和修复路径完全不同
- Provider 名变更（如 `kimi-for-coding` → `kimi-coding`）不是缓存问题，是配置错误——但会和缓存问题叠加，导致 debug 更复杂

## 为什么值钱

- 三重根因叠加：改错文件 + 缓存覆盖 + 配置名错误。任何一个单独存在都容易 debug，三者同时存在时会产生"怎么改都没用"的绝望感
- auth.json 的 `last_status: exhausted` 设计是一个隐性陷阱：系统"记住"了 Key 的失败状态，即使 Key 已经更新也不会重试——这是一种负向缓存（negative cache）
- 任何官方文档都不会写"换 Key 时记得清 auth.json 里的 last_status"——这是运行时的隐性知识

## 与其他知识的关联

- [[dk-p1-model-switch-env]] — 同样是"改了配置不生效"，但 P-1 是 Claude Code 的全局设置优先级问题，P-3 是 Hermes 的 auth 缓存问题。两者共同构成"配置变更不生效"的两种典型根因
- [[dk-p5-cc-connect-config-cascade]] — P-5 揭示了五层配置互相独立的模式，P-3 是其中一层（auth.json 作为运行时缓存层）的具体实例
- `.agent/pitfalls.md` → P-3（原始记录）
