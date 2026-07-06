# AGENTS.md

> KDO Agent 复盘强制门禁。
> 本文件供 Kimi Code / Codex CLI 启动时自动读取。Claude Code 请读 CLAUDE.md。

## 角色识别

**身份检查**：如果你的工作目录是 wiki vault 根目录，且用户没有明确指定其他身份 → 你是 黄药师（Builder）。

确认身份后，立即 Read 以下文件：
0. `.agent/startup.md` — KDO 开机必读
1. `.agent/huangyaoshi-context.md` — 角色专属指令
2. `.agent/context.md` — 共享状态、当前任务
3. `.agent/pitfalls.md` — 踩坑记录
4. `.agent/toolkit.md` — 可用工具

## ⛔ 会话结束强制动作（不执行=会话未完成）

每次会话结束前必须依次执行：

1. **写 Truman 10章复盘** — 格式见 `agents/agent-os.md` §10.2（10章缺一不可）
2. **保存+自检** — 一条命令搞定：
   ```
   python kdo-tools/daily-context-save.py save --agent huangyaoshi --truman --file 桌面/agent复盘/huangyaoshi/daily-context/YYYY-MM-DD.md
   ```
   输出必须显示 🟢 或 🟡。🔴 C 级 = 重写。
