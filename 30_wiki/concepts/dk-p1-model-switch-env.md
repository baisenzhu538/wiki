---
id: dk-p1-model-switch-env
title: "P-1：切模型改环境变量无效——Claude Code 走全局设置"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-1"
source_refs:
  - .agent/pitfalls.md#P-1
tags:
  - "#source_type/error"
  - "#domain/system-operations"
  - "#method/debugging"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - dk-p5-cc-connect-config-cascade
  - master-config-cascade-debug
  - dk-p2-tmux-cache
contradicts:
---

# P-1：切模型改环境变量无效——Claude Code 走全局设置

## 原始表述

> **症状**：在 WSL `.bashrc` / `.profile` 里 `export ANTHROPIC_*` 设为 Kimi，但 `claude.exe` 始终读不到，一直连 DeepSeek。改 Windows 注册表 + `wsl --shutdown` 也无效。
>
> **根因**：Claude Code 的模型/API 配置有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 侧等价路径），优先级高于环境变量。单独改 env var 或注册表都不生效——全局设置覆盖一切。
>
> **对策**：不要逐项改环境变量——直接改 Claude Code 的全局设置文件。一处修改即生效，无需注销重登。
>
> **⚠️ 补充诊断**：P-1 的初始诊断不完全准确。真正的覆盖源对飞书黄药师而言是 cc-connect 的 systemd `env.conf` drop-in（见 P-5），对 CLI 黄药师则可能是全局设置或注册表。两者互不影响——这就是 CLI 正常而飞书 401 的原因。

## 使用场景

- 你想把 Claude Code 从 DeepSeek 切到 Kimi（或反向），在 `.bashrc` 里改了 `export` 但行为没变
- 你改了 Windows 注册表里的 API Key，Claude Code 仍然用旧的
- 飞书端的 Agent 和 CLI 端的 Agent 表现不一致（一个正常一个 401）
- 你在排查"为什么配置改了却不生效"的多层配置覆盖问题

## 操作方法

1. **停止改环境变量**——`.bashrc`、`.profile`、Windows 注册表单独改都不一定能生效
2. **找到真正的配置源**：
   - CLI 黄药师：检查 `~/.claude/settings.json`（全局设置文件）
   - 飞书黄药师：检查 `~/.config/systemd/user/cc-connect.service.d/env.conf`（systemd drop-in）
   - 两者是**独立链路**，互不影响
3. **直接改优先级最高的配置层**：
   - CLI → 改 `~/.claude/settings.json` 里的 model 和 API endpoint
   - 飞书 → 改 systemd drop-in 里的 `Environment=` 行，然后 `daemon-reload && restart`
4. **验证**：改完后发一条测试消息，看 API 调用目标是否变化（查日志确认 endpoint）
5. **如果仍然不生效**：检查是否有更高优先级的覆盖层（见 P-5 配置层叠图）

## 适用边界

- 适用于 Claude Code 模型/API 切换场景，不适用于其他 CLI 工具（如 `curl` 直接调用 API）
- 如果是全新安装（无历史配置），环境变量可能直接生效——因为不存在更高优先级的覆盖
- **与 P-5 的区分**：P-1 解决"配置改了不生效"，P-5 解决"多层配置互相覆盖导致不同入口行为不一致"
- 不适用于非 Claude Code 的 systemd 服务——其他服务的配置层结构可能不同

## 为什么值钱

- 揭示了**配置层叠（Config Cascade）**的真实复杂度：不是"改了就行"，而是"改了哪一层、哪一层优先级最高"
- 典型的"症状在 A 层，根因在 B 层"——`.bashrc` 改了但 `settings.json` 没改，debug 时容易在错误层浪费时间
- 任何 AI 训练语料中都不会有"Claude Code 的全局设置文件优先级高于 WSL 环境变量"这条知识——这是特定工具链的实战经验

## 与其他知识的关联

- [[dk-p5-cc-connect-config-cascade]] — P-5 是 P-1 的深化版：P-1 发现"全局设置覆盖 env"，P-5 发现"五层配置互相独立，改了三处漏了两处"。两者共同构成配置层叠的完整认知
- [[master-config-cascade-debug]] — 系统性 debug 多层配置覆盖的方法论。P-1 是该方法论在 Claude Code 切换场景下的具体实例
- [[dk-p2-tmux-cache]] — 同样是"改了配置不生效"：P-1 是静态配置优先级问题，P-2 是动态 session 缓存问题。两者常被同时遇到
- `.agent/pitfalls.md` → P-1（原始记录）
