---
id: dk-p3-auth-json-cache-override
title: "P-3：Hermes 换 API Key 后仍然 401——auth.json 缓存覆盖 .env"
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
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p1-model-switch-env-var
  - master-systems-thinking
---

# P-3：Hermes 换 API Key 后仍然 401——auth.json 缓存覆盖 .env

## 原始表述

> **症状**：更新 `~/.hermes/profiles/*/.env` 中的 `KIMI_API_KEY` 后重启服务，仍然 HTTP 401，日志显示用的还是旧 Key。用户和欧阳锋多轮尝试换新 Key 无效——"系统顽固用旧的覆盖新的"。
>
> **根因（3 层）**：
> 1. 改错了 .env — Hermes 加载 `~/.hermes/.env`（全局），不是 `~/.hermes/profiles/<name>/.env`。profile 下的 .env 根本不被读取
> 2. auth.json 缓存 — `~/.hermes/auth.json` 的 `credential_pool.kimi-coding[]` 缓存了旧 Key 的 access_token + `last_status: exhausted`，Hermes 优先用缓存而不是重读 env
> 3. Provider 名 — 之前用过 `kimi-for-coding`，正确是 `kimi-coding`
>
> **对策**：
> - API Key 换新时三处同步更新：`~/.hermes/.env` + `~/.hermes/auth.json` credential_pool + `~/.hermes/profiles/*/config.yaml` provider 名
> - 改完后清掉 auth.json 里的 `last_status/exhausted` 和 `last_error_code/401`，否则 Hermes 认为 Key 已死会跳过
> - 用 `journalctl --user -u hermes-gateway-* --no-pager -n 30 | grep -i "401\|auth"` 验证无认证错误

## 使用场景

- 你更新了 Hermes 的 API Key，但重启后仍然报 401 或认证错误
- 你在多个 profile 中使用 Hermes，不确定到底该改哪个 .env 文件
- 你发现 auth.json 中有 `last_status: exhausted` 或 `last_error_code: 401`，需要清理缓存
- 你在排查"系统顽固用旧 Key"的问题时，需要理解 Hermes 的几层配置和缓存机制

## 操作方法

1. **确认正确的 .env 文件**：Hermes 读的是 `~/.hermes/.env`（全局），而非 profile 目录下的 .env。修改前先 `cat ~/.hermes/.env` 确认当前值
2. **更新全局 .env**：将新的 `KIMI_API_KEY` 写入 `~/.hermes/.env`
3. **清理 auth.json 缓存**：编辑 `~/.hermes/auth.json`，在 `credential_pool.kimi-coding[]` 中更新为新 Key，并删除 `last_status: exhausted` 和 `last_error_code: 401`
4. **验证 provider 名称**：检查 `~/.hermes/profiles/*/config.yaml`，确认 provider 是 `kimi-coding` 而非 `kimi-for-coding`
5. **验证修复**：`systemctl --user restart hermes-gateway-*` 后，用 `journalctl` 查看最新日志，确认无 401 错误

## 适用边界

- 适用于所有使用 Hermes 并需要更换 API Key 的场景
- 不适用于不使用 Hermes 的系统（如直接用 curl 调用 API）——这些系统没有 auth.json 缓存
- 如果使用的是其他 provider（如 DeepSeek、Anthropic），缓存机制相同——auth.json 的 `credential_pool` 对所有 provider 都有缓存
- 删除 auth.json 是安全的——Hermes 会重新从 .env 加载 Key并重新认证
- 如果不想手动编辑 JSON，可以直接删除 `~/.hermes/auth.json`（Hermes 会自动重建）

## 为什么值钱

- 这是 Hermes 特有的配置层级：**3 层配置 + 1 层缓存**，每一层都可能覆盖或缓存旧值
- **"系统顽固用旧的覆盖新的"是最令人灰心的错误描述**：实际上不是"顽固"，而是"缓存机制设计如此"——但用户体验就是"明明改了为什么还是旧的"
- 暴露了缓存设计中的一个关键问题：`last_status: exhausted` 是一个"状态标记"，但这个标记不会自动清除——即使 Key 已经更新
- 任何 AI 训练语料中都不会有"Hermes 的 auth.json 缓存会覆盖 .env 中的新 API Key"这条知识

## 与其他知识的关联

- [[dk-p1-model-switch-env-var]] — 同一深层模式：多层配置下的"覆盖"问题。P-1 是"全局设置覆盖环境变量"，P-3 是"缓存覆盖配置文件"——两者都是"新配置被旧状态覆盖"
- [[master-systems-thinking]] — 系统思维中的"状态一致性"：auth.json 是一个独立的状态存储，它与 .env 文件之间没有自动同步机制——修改一处必须手动同步另一处
- `.agent/pitfalls.md` → P-3（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
