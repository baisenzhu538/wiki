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
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - dk-f4-wrong-workdir
  - dk-p3-auth-cache
contradicts:
  - master-systems-thinking
  - master-first-principles
---

# P-1：切模型改环境变量无效——Claude Code 走全局设置

## 原始表述

> **症状**：在 WSL `.bashrc` / `.profile` 里 `export ANTHROPIC_*` 设为 Kimi，但 `claude.exe` 始终读不到，一直连 DeepSeek。改 Windows 注册表 + `wsl --shutdown` 也无效。
>
> **根因**：Claude Code 的模型/API 配置有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 侧等价路径），优先级高于环境变量。单独改 env var 或注册表都不生效——全局设置覆盖一切。
>
> **对策**：直接改 Claude Code 的全局设置文件，一处修改即生效，无需注销重登。
>
> **补充**：P-1 的初始诊断不完全准确。真正的覆盖源对飞书黄药师而言是 cc-connect 的 systemd `env.conf` drop-in（见 P-5），对 CLI 黄药师则可能是全局设置或注册表。两者互不影响——这就是为什么 CLI 黄药师正常工作而飞书黄药师 401。

## 使用场景

- 你需要切换 Claude Code 使用的 LLM 模型（如从 DeepSeek 切到 Kimi 或反之）
- 你更新了 API Key 但 Claude Code 仍然使用旧 Key
- 你在 WSL 里改了环境变量但 Windows 侧的 `claude.exe` 行为没变
- 你排查"为什么同一台机器，CLI 正常但飞书 Agent 401"的多链路配置差异

## 操作方法

1. **识别你的 Claude Code 启动链路**：
   - CLI 黄药师：`.bashrc` → tmux session → `claude` 命令
   - 飞书黄药师：cc-connect → systemd `env.conf` → `claude` 子进程
   - 两者互不影响，改一处只影响一处

2. **CLI 链路改配置**：
   - 检查 `~/.claude/settings.json`（全局设置，优先级最高）
   - 如果全局设置存在，直接改这里；如果不存在，改 `.bashrc` 才有效

3. **飞书链路改配置**：
   - 改 `~/.config/systemd/user/cc-connect.service.d/env.conf`
   - 改完后 `systemctl --user daemon-reload && systemctl --user restart cc-connect`
   - 验证：`systemctl --user show cc-connect | grep Environment`

4. **改完后验证**：
   - CLI：新开一个 tmux session（`tmux kill-session -t claude` 后重开）
   - 飞书：发一条测试消息，看日志里的 model 和 endpoint

5. **不要做的事**：
   - 不要逐项改环境变量 expecting 它会覆盖全局设置
   - 不要改了一处就认为"全链路都改了"
   - 不要在改配置后不验证就宣布"完成了"

## 适用边界

- 适用于所有使用 Claude Code CLI 或 cc-connect  wrapper 的场景
- 不适用于其他 LLM 客户端（如直接使用 OpenAI SDK）——那些工具的配置链路不同
- **与 P-5 的区别**：P-1 讲的是"全局设置优先级"，P-5 讲的是"两条独立配置链路"。两者有关联但独立成坑
- 如果全局设置文件不存在，环境变量确实会生效——此时 P-1 不触发
- Windows 侧和 WSL 侧的配置完全隔离，改 WSL 不影响 Windows `claude.exe`

## 为什么值钱

- 这是**配置层优先级**的实战教训：大多数开发者假设"环境变量是最高优先级"，但 Claude Code 的全局设置优先级更高。这个假设在 90% 的工具中成立，在 Claude Code 中不成立
- 揭示了"多链路部署"的隐藏复杂度：同一台机器上 CLI 和飞书 Agent 看似用同一个工具，实际走不同的配置链路，改一处不影响另一处
- **AI 训练语料中不会有这条**：没有任何官方文档会写"我们的全局设置覆盖环境变量"——这是踩坑后的实战经验

## 与其他知识的关联

- dk-f4-wrong-workdir — 配置类失败模式的双杀。P-1 是"改配置不生效"，F-KDO-004 是"在错误目录执行命令"——两者都是"配置/环境假设与实际行为不一致"
- dk-p3-auth-cache — P-1 和 P-3 是同一事故链的前两环：模型配置不对 → 401 → 换 Key → Key 被缓存覆盖。理解 P-1 才能正确诊断 P-3
- dk-p5-cc-connect-config — P-5 是 P-1 在飞书链路的精确复现：cc-connect 的 systemd drop-in 就是飞书链路的"全局设置"
- `.agent/pitfalls.md` → P-1（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
