---
id: "dk-p5-cc-connect-config"
title: "P-5：cc-connect 切模型后 CLI 正常但飞书 401 + 找不到文件夹"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "system"
source_context: "pitfalls.md P-5"
source_refs:
  - ".agent/pitfalls.md#P-5"
tags:
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
  - "#scene/ai-collaboration"
  - "#scene/learning-methodology"
  - "#scene/skill-engineering"
  - "#source_type/error"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - "dk-p1-model-switch-env"
  - "dk-p2-tmux-cache"
  - "dk-p6-session-resume-fail"
contradicts:
  - "master-systems-thinking"
  - "master-first-principles"
---

# P-5：cc-connect 切模型后 CLI 正常但飞书 401 + 找不到文件夹

## 原始表述

> **症状**：从 Kimi 切回 DeepSeek 后，WSL 终端的 `claude` 命令正常工作，但飞书黄药师报 `HTTP 401` 且无法访问 wiki/KDO。
>
> **根因（2 个残留文件未回切）**：
> 1. `~/.config/systemd/user/cc-connect.service.d/env.conf` — Kimi 时代的 systemd Environment drop-in，仍指向 `https://api.kimi.com/coding` + Kimi Key。systemd `Environment=` 注入的 env var 优先级最高，覆盖 `.bashrc` 和注册表
> 2. `~/.cc-connect/config.toml` — `work_dir` 从 `/mnt/c/Users/Administrator/Desktop/wiki` 被改为 `/home/dministrator`（Kimi 切换期间重置的），导致 Claude Code 从 home 目录启动，读不到 wiki 的 `CLAUDE.md`
>
> **为什么 CLI 黄药师正常**：CLI 走 `.bashrc` → tmux session env，和 cc-connect 的 systemd env 互不影响。两条独立的配置链路。
>
> **对策**：切模型/切 API 时，c-connect 的配置有独立的两个文件需要同步改完后 `daemon-reload && restart`。
>
> **关联**：Config Cascade Debug skill — 这本质是同一模式：多个独立配置层（.bashrc / 注册表 / systemd drop-in / cc-connect config.toml），改了三处漏了一处。

## 使用场景

- 你在同一台机器上同时运行 CLI Agent 和飞书 Agent（如黄药师）
- 你切换 LLM provider 或 API Key 后，发现一条链路正常、另一条报错
- 你修改了 cc-connect 的配置但飞书 bot 行为不变
- 你需要理解"多链路配置"的复杂性，避免改一处漏一处

## 操作方法

1. **识别 cc-connect 的配置链路**：
   - cc-connect 是 systemd 管理的服务，有自己独立的配置层
   - 不要假设改了 `.bashrc` 就等于改了 cc-connect

2. **同步两个文件**：
   - `config.toml` → 确保 `work_dir` 指向正确的 wiki 根目录
   - `cc-connect.service.d/env.conf` → 确保模型、API endpoint、Key 全部正确

3. **重启并验证**：
   - `systemctl --user daemon-reload`
   - `systemctl --user restart cc-connect`
   - `systemctl --user show cc-connect | grep Environment` 验证 env 正确
   - 发一条飞书测试消息，确认 bot 响应正常

4. **建立切换 checklist**：
   - CLI 链路：.bashrc → tmux → kill session 重开
   - 飞书链路：config.toml + env.conf → daemon-reload → restart
   - 两条链路分开检查，不要混为一谈

5. **不要做的事**：
   - 不要改了 `.bashrc` 就以为飞书也一起改了
   - 不要忽略 `work_dir` 的检查——它决定了 Claude Code 从哪里启动，读哪个 CLAUDE.md
   - 不要在不确认两条链路都正常前宣布"切换完成了"

## 适用边界

- 适用于所有使用 cc-connect 或类似 systemd wrapper 的多链路部署场景
- 不适用于单一链路部署（只有 CLI 或只有飞书）——那些场景下 P-5 不触发
- **与 P-1 的区别**：P-1 是单一链路内的"全局设置覆盖 env var"，P-5 是多链路之间的"改了 A 但 B 没改"。两者可以同时存在
- **与 P-6 的关系**：P-5 是事故链的第一环（配置错），P-6 是事故链的第三环（session 缓存）。中间还有 API Key 修复环
- 如果使用 Docker 或 Kubernetes 部署，配置层会更复杂（ConfigMap / Secret / 环境变量层级更多）——P-5 的模式仍然适用

## 为什么值钱

- 这是**多链路配置**的经典陷阱：同一台机器上运行多个实例，每个实例有独立的配置，改一处不影响其他处
- 极具迷惑性：CLI 正常 = 我的配置改对了 = 飞书也正常。这个推理是错的，但很自然
- 揭示了"Config Cascade"模式：现代开发环境有多个独立配置层（.bashrc、注册表、systemd drop-in、Docker env、K8s Secret等），改了三处漏了一处是常态
- **AI 训练语料中不会有这条**：没有任何官方文档会写"如果你同时运行 CLI 和飞书 Agent，切换模型时要分开检查两条链路"

## 与其他知识的关联

- dk-p1-model-switch-env — P-1 是单一链路的配置层级问题，P-5 是多链路的配置层级问题。两者组合起来构成完整的"切换模型时的配置集"
- dk-p2-tmux-cache — P-2 是 CLI 链路的缓存问题，P-5 是飞书链路的配置问题。两者是同一事故的不同表现
- dk-p6-session-resume-fail — P-6 是 P-5 的事故链延伸：配置修复后仍然失败，因为旧 session 缓存了旧配置
- `.agent/pitfalls.md` → P-5（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
