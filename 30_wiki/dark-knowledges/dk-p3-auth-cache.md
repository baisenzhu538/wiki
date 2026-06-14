---
id: "dk-p3-auth-cache"
title: "P-3：Hermes 换 API Key 后仍然 401 — auth.json 缓存覆盖 .env"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: draft
domain:
  - "master"
source_person: "system"
source_context: "pitfalls.md P-3"
source_refs:
  - ".agent/pitfalls.md#P-3"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - "dk-p1-model-switch-env"
  - "dk-p5-cc-connect-config"
contradicts:
  - "master-systems-thinking"
  - "master-first-principles"
tags:
  - #domain/knowledge-management
  - #method/evaluation-method
  - #scene/ai-collaboration
  - #scene/knowledge-management/tagging
  - #scene/learning-methodology
pipeline:
  - #source_type/error
  - confidence-draft
  - confidence-source-cited
author: legacy
reviewed_by: pending
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
> **对策**：API Key 换新时三处同步更新：`~/.hermes/.env` + `~/.hermes/auth.json` credential_pool + `~/.hermes/profiles/*/config.yaml` provider 名。改完后清掉 auth.json 里的 `last_status/exhausted` 和 `last_error_code/401`。

## 使用场景

- 你更换了 LLM API Key（如 Kimi、DeepSeek、OpenAI），但服务仍然报 401 Unauthorized
- 你排查"为什么改了 Key 还是旧的"——看起来系统"顽固"地用旧 Key
- 你管理多个 Hermes profile，发现 profile 下的 `.env` 修改不生效
- 你运维长期运行的 Agent 服务（如 Hermes gateway），需要轮换 API Key

## 操作方法

1. **确认正确的 .env 位置**：
   - Hermes 读的是 `~/.hermes/.env`（全局），不是 `~/.hermes/profiles/<name>/.env`
   - 改全局 .env，不要改 profile 下的（除非确认代码逻辑确实读 profile 下的）

2. **清理 auth.json 缓存**：
   - 打开 `~/.hermes/auth.json`
   - 找到 `credential_pool.kimi-coding[]`（或对应 provider）
   - 删除旧的 `access_token` 或整个缓存条目
   - 清除 `last_status: exhausted` 和 `last_error_code: 401`——否则 Hermes 认为 Key 已死会跳过

3. **核对 provider 名**：
   - 检查 `config.yaml` 中的 provider 名称（如 `kimi-coding` vs `kimi-for-coding`）
   - 确保 auth.json 的 credential_pool 键名与 config.yaml 一致

4. **重启并验证**：
   - `systemctl --user restart hermes-gateway-*`
   - `journalctl --user -u hermes-gateway-* --no-pager -n 30 | grep -i "401\|auth"` 确认无认证错误

5. **建立 Key 轮换 SOP**：
   - 换新 Key 时三处同步：全局 .env + auth.json 缓存 + config.yaml provider
   - 不要只改一处就宣布完成

## 适用边界

- 适用于所有使用 Hermes 或类似 auth.json 缓存机制的 Agent 框架
- 不适用于直接使用 API（如 curl 调 OpenAI API）——那些没有 auth.json 缓存层
- **与 P-1 的区别**：P-1 是 Claude Code 的"全局设置覆盖环境变量"，P-3 是 Hermes 的"auth.json 缓存覆盖 .env"。两者是同一模式在不同工具上的复现
- 如果 auth.json 不存在（首次安装），P-3 不触发——此时 .env 修改直接生效
- Provider 名问题看似低级，但在频繁切换 provider 时极易踩坑

## 为什么值钱

- 这是**缓存层 vs 配置层**的三层嵌套陷阱：.env → auth.json → provider 名，任何一层不一致都导致 401
- 极具挫败感：用户和欧阳锋"多轮尝试换新 Key 无效"——因为每层都看似正确，但组合起来就是不通
- 揭示了"状态分散"问题：配置不应该分散在三处独立维护的文件中，但现实如此
- **AI 训练语料中不会有这条**：没有任何 Hermes 文档会写"auth.json 缓存会覆盖 .env"——这是运维踩坑后的暗知识

## 与其他知识的关联

- dk-p1-model-switch-env — P-1 和 P-3 是同一模式在不同工具上的复现：都是"配置改了但不生效，因为有更高优先级的缓存层"。Claude Code 用全局设置覆盖 .env，Hermes 用 auth.json 覆盖 .env
- dk-p5-cc-connect-config — P-5 的 systemd drop-in 是 cc-connect 的"全局设置"，与 P-3 的 auth.json 缓存是同一模式的不同表现
- `90_control/failure-modes.md` → F-KDO-003（state.json 覆盖写竞态）— 同样是"状态文件与配置不一致导致的问题"
- `.agent/pitfalls.md` → P-3（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
