# 架构决策

格式：日期 → 背景 → 决策 → 原因 → 否决的替代方案。

---

## 2026-05-16: DeepSeek V4 Pro 保留为 WSL 黄药师模型

**背景**：尝试将黄药师从 DeepSeek V4 切换到 Kimi 模型（月之暗面 `kimi-for-coding`）。API 本身可用（Anthropic Messages 协议兼容），Windows PowerShell 下测试通过。但在 WSL 中 `claude.exe` 始终读到 Windows 侧的 DeepSeek 环境变量，无法覆盖。

**决策**：保留 DeepSeek V4 Pro，放弃切换到 Kimi。

**原因**：WSL → Windows exe 的环境变量传递由 Windows 注册表和父进程主导，Linux 侧 `export` 被忽略。要让 Kimi 生效需改 Windows 注册表 + 注销重登 + `wsl --shutdown`，且 tmux session 继承链可能仍有缓存。维护成本高于收益。

**替代方案**：Kimi `kimi-for-coding` — API 测试通过，模型质量待评估。被否决原因：WSL 环境变量传递不可靠，不是模型本身的问题。

**后果**：黄药师固定用 DeepSeek V4 Pro。如果未来要切模型，优先考虑在 Windows 原生终端（而非 WSL）运行 Claude Code。

---

## 2026-05-16: 创建 .agent/ 外挂大脑（本文件）

**背景**：黄药师 tmux session 被杀后完全失忆，不知道自己是 Builder、不知道 KDO、不知道 Sprint 12。每次恢复上下文消耗大量 token。

**决策**：在 vault 根目录创建 `.agent/` 三个文件（context.md / pitfalls.md / decisions.md），作为 agent 启动时的最小上下文入口。

**原因**：节省 ~80% 上下文恢复 token。三个文件跟着 git 走，换电脑不丢。任何 agent（不限于 Claude Code）都能读。

**替代方案**：Claude Code `/memory` — 被否决，因为锁在工具里、换工具/换电脑就丢。

**后果**：每次 session 结束需花 2 分钟更新 context.md。新 agent 启动时先读这三个文件。
