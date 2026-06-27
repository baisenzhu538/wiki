---

id: dk-p1-model-switch-env
title: P-1：切模型改环境变量无效——Claude Code 走全局设置
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: system
source_context: pitfalls.md P-1
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
---# P-1：切模型改环境变量无效——Claude Code 走全局设置

## 原始表述/核心洞察

> **症状**：在 WSL `.bashrc` / `.profile` 里 `export ANTHROPIC_*` 设为 Kimi，但 `claude.exe` 始终读不到，一直连 DeepSeek。改 Windows 注册表 + `wsl --shutdown` 也无效。
>
> **根因**：Claude Code 的模型/API 配置有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 侧等价路径），优先级高于环境变量。单独改 env var 或注册表都不生效——全局设置覆盖一切。
>
> **对策**：直接改 Claude Code 的全局设置文件，一处修改即生效，无需注销重登。
>
> **补充**：P-1 的初始诊断不完全准确。真正的覆盖源对飞书黄药师而言是 cc-connect 的 systemd `env.conf` drop-in（见 P-5），对 CLI 黄药师则可能是全局设置或注册表。两者互不影响——这就是为什么 CLI 黄药师正常工作而飞书黄药师 401。

核心洞察：**Claude Code 的模型/API 配置存在“全局设置 > 环境变量”的优先级，且 CLI 与 cc-connect 两条链路各自独立；改配置时必须对准对应链路的最高优先级文件并分别验证。** 只在 `.bashrc` 或注册表里改环境变量，往往是在优先级更低的层上做无用功。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别你的 Claude Code 启动链路**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **CLI 链路改配置**：
   - src_unknown
   - src_unknown

3. **飞书链路改配置**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **改完后验证**：
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|---|---|---|---|
| 在环境变量层改模型，期待覆盖全局设置 | WSL `.bashrc` 已 export ANTHROPIC_*，但 `claude.exe` 仍连 DeepSeek；改注册表/`wsl --shutdown` 无效 | Claude Code 全局设置（`~/.claude/settings.json`）优先级高于环境变量 | 直接改对应链路的全局设置文件；CLI 链路检查 `~/.claude/settings.json`，飞书链路检查 systemd `env.conf` |
| 误以为改一条链路等于改全链路 | CLI 正常但飞书 Agent 401，或反之 | CLI 与 cc-connect 是两条独立配置链路，互不影响 | 分别修改并分别验证：CLI 重开 tmux session，飞书 reload+restart cc-connect |
| 改完配置不验证实际生效状态 | 日志仍显示旧模型或旧 endpoint | 未重启 session/服务，或缓存未刷新 | CLI：kill 并重建 tmux session；飞书：`systemctl --user show cc-connect | grep Environment` 并查看日志 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
