---
id: "dk-p2-tmux-cache"
title: "P-2：tmux session 缓存旧配置"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "system"
source_context: "pitfalls.md P-2"
source_refs:
  - ".agent/pitfalls.md#P-2"
tags:
  - "#boundary/single-use-only"
  - "confidence-draft"
  - "confidence-source-cited"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
  - "#scene/ai-collaboration"
  - "#scene/learning-methodology"
  - "#source_type/error"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - "dk-p1-model-switch-env"
contradicts:
  - "master-systems-thinking"
  - "master-first-principles"
---

# P-2：tmux session 缓存旧配置

## 原始表述

> **症状**：改了 `.bashrc` 后 `claude` 行为没变。
>
> **根因**：`claude()` 函数包装了 tmux session `claude`，只要 session 活着，用的是 session 创建时的环境，不是最新 `.bashrc`。
>
> **对策**：改完配置后 `tmux kill-session -t claude`，再重新 `claude`。

## 使用场景

- 你修改了 `.bashrc`、`.profile` 或任何 shell 配置文件，期望立即生效
- 你通过 tmux 或 screen 运行长期会话（如 Claude Code、Jupyter、开发服务器）
- 你改了 API Key、模型 endpoint 或其他环境变量，但进程行为没有变化
- 你排查"为什么配置改了但程序还是用旧的"

## 操作方法

1. **识别 tmux 缓存**：
   - `tmux ls` 查看活跃的 session
   - 如果目标 session 存在，它的环境变量是创建时的快照，不会自动刷新

2. **正确刷新流程**：
   - `tmux kill-session -t <session-name>` 彻底杀死 session
   - 重新启动程序，新 session 会读取最新的 `.bashrc`

3. **验证配置已生效**：
   - 在新 session 里 `echo $TARGET_VAR` 确认值正确
   - 运行程序，观察行为是否符合预期

4. **预防措施**：
   - 改配置前 `tmux ls` 确认是否有活跃 session
   - 养成习惯：改环境变量后一律 kill session 重开，不要假设它会自动刷新
   - 对于生产环境的长期进程，使用 `source /etc/profile` 或 systemd 的 `EnvironmentFile=` 而非依赖 shell 配置文件

## 适用边界

- 适用于所有使用 tmux/screen 包装长期会话的场景
- 不适用于一次性进程（如直接 `python script.py`）——那些进程每次启动都会读取最新环境
- **与 P-1 的区别**：P-1 是"配置层级优先级"问题（全局设置覆盖 env var），P-2 是"运行时缓存"问题（session 创建时的 env 快照不刷新）。两者可能同时触发
- 如果进程不是通过 tmux 启动的（如 systemd service、Docker container），P-2 不适用——那些有自己的配置刷新机制

## 为什么值钱

- 这是**运行时缓存 vs 静态配置**的经典盲区：开发者习惯改文件 → 期望生效，但忽略了中间层的缓存（tmux session、systemd 环境、Docker 镜像层等）
- 极具迷惑性：`.bashrc` 确实改了，文件系统确认无误，但进程行为不变。没有 tmux 知识的人会在这个环节浪费大量时间
- **AI 训练语料中不会有这条**：没有任何文档会写"如果你用 tmux 运行 Claude Code，改 .bashrc 后需要 kill session"。这是运维实战经验

## 与其他知识的关联

- dk-p1-model-switch-env — P-1 和 P-2 是同一事故链：改模型配置 → 改 `.bashrc` → tmux 缓存旧配置 → 配置不生效。理解 P-2 才能完整诊断"为什么我改了配置但 Claude Code 没变化"
- dk-p5-cc-connect-config — P-5 的 session 缓存（P-6）是 P-2 在 systemd/cc-connect 链路的变体：都是"旧运行时状态阻碍新配置生效"
- `90_control/failure-modes.md` → F-KDO-004（错误工作目录）— 配置类问题的另一维度
- `.agent/pitfalls.md` → P-2（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
