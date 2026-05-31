---
id: dk-p1-model-switch-env-var
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
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p5-cc-connect-config-cascade
  - master-systems-thinking
---

# P-1：切模型改环境变量无效——Claude Code 走全局设置

## 原始表述

> **症状**：在 WSL `.bashrc` / `.profile` 里 `export ANTHROPIC_*` 设为 Kimi，但 `claude.exe` 始终读不到，一直连 DeepSeek。改 Windows 注册表 + `wsl --shutdown` 也无效。
>
> **根因**：Claude Code 的模型/API 配置有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 侧等价路径），优先级高于环境变量。单独改 env var 或注册表都不生效——全局设置覆盖一切。
>
> **对策**：不要逐项改环境变量——直接改 Claude Code 的全局设置文件。全局设置的模型/API endpoint/Key 一处修改即生效，无需注销重登。
>
> **2026-05-16 补充**：P-1 的初始诊断不完全准确。真正的覆盖源对飞书黄药师而言是 cc-connect 的 systemd `env.conf` drop-in（见 P-5），对 CLI 黄药师则可能是全局设置或注册表。两者互不影响——这就是为什么 CLI 黄药师正常工作而飞书黄药师 401。
>
> **关联**：`decisions.md` 2026-05-16 DeepSeek vs Kimi

## 使用场景

- 你准备从 DeepSeek 切换到 Kimi（或反之），修改了 `.bashrc` 中的 `ANTHROPIC_API_KEY` 但发现不生效
- 你观察到 CLI 和飞书 bot 的行为不一致（一个正常一个 401），需要排查配置层级
- 你在调试 API Key 失效问题，已经尝试了环境变量和注册表但都没有改变
- 你设计多通道 AI 系统时，需要理解 CLI 和 daemon 服务的配置是完全独立的

## 操作方法

1. **确认当前配置层级**：先用 `claude config get apiKey` 或查看 `~/.claude/settings.json` 确认当前生效的配置来源
2. **修改全局设置**：直接编辑 `~/.claude/settings.json`，设置 `apiKey` 和 `provider`
3. **区分 CLI 和 Daemon**：如果有 cc-connect 等 daemon 服务，单独修改 CLI 的配置不会影响 daemon——需要额外检查 systemd drop-in 和 `config.toml`
4. **验证改动**：修改后运行 `claude --version` 或发送一条测试消息，确认模型已切换
5. **不要重启机器或 WSL**：全局设置文件的修改不需要重启即生效，重启只是浪费时间

## 适用边界

- 适用于所有使用 Claude Code CLI 或其他有全局设置文件的工具
- 不适用于纯环境变量驱动的工具（如普通的 curl 脚本）——这些工具确实只读环境变量
- 如果同时有多个 Claude Code 实例（CLI + cc-connect），每个实例的配置是独立的，修改一个不会影响另一个
- 全局设置文件的优先级高于环境变量，但如果全局设置为空，会回退到环境变量——这个回退行为可能让问题更加迷惑
- 在 Windows + WSL 环境中，注册表和 `.bashrc` 是两条独立的链路，优先级低于全局设置文件

## 为什么值钱

- 这是配置级联的经典陷阱：多层配置（环境变量 → 注册表 → 全局设置 → systemd drop-in）中，最高优先级的那一层决定了实际行为
- **"改了环境变量但无效"是最消耗信任的失败模式**：用户会认为自己的配置修改没问题，从而开始怀疑工具本身是不是坏了
- 揭示了"配置层级"的核心原理：不是"改了就行"，而是"改了最高优免级的那一层才行"
- 任何 AI 训练语料中都不会有"Claude Code 的全局设置文件优先级高于环境变量"这条知识

## 与其他知识的关联

- [[dk-p5-cc-connect-config-cascade]] — 同一事故链的第二环。P-1 是"切模型改环境变量无效"，P-5 是"切模型后 CLI 正常但飞书 401"——两者共同构成 Config Cascade 调试技能的案例
- [[master-systems-thinking]] — 系统思维中的"级联效应"：多层配置形成了一个级联，最低层的配置调整被最高层覆盖，产生非直观的行为偏差
- `.agent/pitfalls.md` → P-1（原始记录）
- `90_control/decisions.md` → 2026-05-16 DeepSeek vs Kimi 决策（关联案例）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
