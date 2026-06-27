---

id: dk-p5-cc-connect-config
title: P-5：cc-connect 切模型后 CLI 正常但飞书 401 + 找不到文件夹
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: system
source_context: pitfalls.md P-5
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
---# P-5：cc-connect 切模型后 CLI 正常但飞书 401 + 找不到文件夹

## 原始表述/核心洞察

> **症状**：从 Kimi 切回 DeepSeek 后，WSL 终端的 `claude` 命令正常工作，但飞书黄药师报 `HTTP 401` 且无法访问 wiki/KDO。
>
> **根因（2 个残留文件未回切）**：
> 1. `~/.config/systemd/user/cc-connect.service.d/env.conf` — Kimi 时代的 systemd Environment drop-in，仍指向 `https://api.kimi.com/coding` + Kimi Key。systemd `Environment=` 注入的 env var 优先级最高，覆盖 `.bashrc` 和注册表
> 2. `~/.cc-connect/config.toml` — `work_dir` 从 `/mnt/c/Users/Administrator/Desktop/wiki` 被改为 `/home/dministrator`（Kimi 切换期间重置的），导致 Claude Code 从 home 目录启动，读不到 wiki 的 `CLAUDE.md`
>
> **为什么 CLI 黄药师正常**：CLI 走 `.bashrc` → tmux session env，和 cc-connect 的 systemd env 互不影响。两条独立的配置链路。
>
> **对策**：切模型/切 API 时，cc-connect 的配置有独立的两个文件需要同步改完后 `daemon-reload && restart`。
>
> **关联**：Config Cascade Debug skill — 这本质是同一模式：多个独立配置层（.bashrc / 注册表 / systemd drop-in / cc-connect config.toml），改了三处漏了一处。

核心洞察：**同一台机器上的 CLI Agent 与飞书 Agent 走两条独立的配置链路；修改其中一条后必须显式检查另一条，否则"正常"的链路会掩盖"异常"的链路。**

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别 cc-connect 的配置链路**：
   - src_unknown
   - src_unknown

2. **同步两个文件**：
   - src_unknown
   - src_unknown

3. **重启并验证**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

4. **建立切换 checklist**：
   - src_unknown
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
| 只改 CLI 链路就宣布完成 | `claude` 命令正常，但飞书 bot 报 401 / 找不到文件夹 | 误以为 `.bashrc` 的修改会同步影响 cc-connect | 同时检查 `env.conf` + `config.toml`，并 `daemon-reload && restart` |
| work_dir 被旧配置覆盖 | Claude Code 从 `/home/dministrator` 启动，读不到 wiki | 切换模型时 config.toml 被重置或误改 | 将 `work_dir` 改回 wiki 根目录并重启服务 |
| env.conf 残留旧 provider | `systemctl show` 仍指向 Kimi endpoint 或旧 Key | systemd drop-in 未被覆盖或更新 | 重写 `env.conf` 后执行 `daemon-reload` |
| 两条链路混为一谈 | 改一处后凭"感觉"认为另一处也对了 | 不理解 CLI 与 systemd 的独立环境 | 建立分开的切换 checklist，分别验证 CLI 与飞书 |

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
