---
id: dk-p5-cc-connect-config-cascade
title: "P-5：cc-connect 切模型后 CLI 正常但飞书 401 + 找不到文件夹"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-5"
source_refs:
  - .agent/pitfalls.md#P-5
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

# P-5：cc-connect 切模型后 CLI 正常但飞书 401 + 找不到文件夹

## 原始表述

> **症状**：从 Kimi 切回 DeepSeek 后，WSL 终端的 `claude` 命令正常工作，但飞书黄药师报 `HTTP 401` 且无法访问 wiki/KDO。
>
> **根因（2 个残留文件未回切）**：
> 1. `~/.config/systemd/user/cc-connect.service.d/env.conf` —— Kimi 时代的 systemd Environment drop-in，仍指向 `https://api.kimi.com/coding` + Kimi Key。systemd `Environment=` 注入的 env var 优先级最高，覆盖 `.bashrc` 和注册表
> 2. `~/.cc-connect/config.toml` —— `work_dir` 从 `/mnt/c/Users/Administrator/Desktop/wiki` 被改为 `/home/dministrator`（Kimi 切换期间重置的），导致 Claude Code 从 home 目录启动，读不到 wiki 的 `CLAUDE.md`
>
> **为什么 CLI 黄药师正常**：CLI 走 `.bashrc` → tmux session env，和 cc-connect 的 systemd env 互不影响。两条独立的配置链路。
>
> **对策**：切模型/切 API 时，cc-connect 的配置有**独立的两个文件**需要同步：1) `config.toml` → 模型/API 通过 provider 或 env 注入  2) `cc-connect.service.d/env.conf` → systemd 环境变量。改完后 `systemctl --user daemon-reload && systemctl --user restart cc-connect`。验证：`systemctl --user show cc-connect | grep Environment`
>
> **关联**：Config Cascade Debug skill — 这本质是同一模式：多个独立配置层（.bashrc / 注册表 / systemd drop-in / cc-connect config.toml），改了三处漏了一处。

## 使用场景

- 你切换了 AI 模型或 API provider，发现部分通道正常而部分通道 401
- 你的 cc-connect 服务启动后无法访问 wiki vault，需要排查 `work_dir` 配置
- 你在调试"同一个系统为什么有两种行为"的问题
- 你设计多通道 AI 系统时，需要理解每个通道的独立配置层级

## 操作方法

1. **确认所有配置层**：切换模型时列出完整的配置清单：`.bashrc` → 注册表 → `~/.claude/settings.json` → `cc-connect.service.d/env.conf` → `~/.cc-connect/config.toml`
2. **逐层验证**：每修改一处后，用 `systemctl --user show cc-connect | grep Environment` 验证 systemd 层的配置是否更新
3. **检查 work_dir**：`cat ~/.cc-connect/config.toml | grep work_dir`——确保是 wiki vault 路径而非 home 目录
4. **daemon-reload 必须执行**：修改 systemd drop-in 后必须运行 `systemctl --user daemon-reload`，否则 systemd 不会重新读取 drop-in
5. **分通道验证**：修复后分别测试 CLI 和飞书两个通道，确认两者都正常——一个正常不代表另一个正常

## 适用边界

- 适用于所有使用 cc-connect 或类似 daemon 服务接入 Claude Code 的场景
- 不适用于纯 CLI 使用场景——纯 CLI 只有 `.bashrc` 和全局设置两层，没有 systemd 和 config.toml 层
- 如果没有使用 systemd 管理 cc-connect（如用 docker-compose 或直接运行），配置层级会更少，但仍然可能有类似的级联问题
- systemd drop-in 的优先级高于所有其他配置层——这是它最危险的地方，也是最容易被遗漏的地方
- 当多个通道同时存在时，**不能用一个通道的正常行为推断另一个通道也正常**

## 为什么值钱

- 这是多通道 AI 系统特有的调试难题：**同一个系统有两条独立的配置链路**，行为不一致时极其迷惑
- "CLI 正常但飞书 401"是配置级联调试的典型症状：它强烈地暗示"有一个被遗漏的配置层"
- 揭示了系统思维中的一个核心原理：**多通道系统的每个通道必须独立验证**——不能用一个通道的正常推断其他通道
- 任何 AI 训练语料中都不会有"cc-connect 的 systemd drop-in 优先级高于 .bashrc"这条知识

## 与其他知识的关联

- [[dk-p1-model-switch-env-var]] — 同一事故链的第一环。P-1 是"切模型改环境变量无效"，P-5 是"切模型后多通道行为不一致"——两者共同构成 Config Cascade 调试的完整案例
- [[master-systems-thinking]] — 系统思维中的"级联效应"和"多通道系统"：当一个系统的多个组成部分有独立配置时，级联失败的概率指数级上升
- `.agent/pitfalls.md` → P-5（原始记录）
- `90_control/decisions.md` → 2026-05-16 DeepSeek vs Kimi 决策（关联案例）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
