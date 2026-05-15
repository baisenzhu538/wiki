# 踩坑记录

每踩一个坑追一条。格式：症状 → 根因 → 对策。

---

## P-1: WSL 环境变量无法传给 Windows claude.exe

**症状**：在 WSL `.bashrc` / `.profile` 里 `export ANTHROPIC_*` 设为 Kimi，但 `claude.exe`（Windows PE）始终读不到，一直连 DeepSeek。

**根因**：WSL 启动 Windows 可执行文件时，Windows 侧环境变量（来自注册表 + 父进程）覆盖 Linux 侧 `export`。`WSLENV` 机制不可靠。

**对策**：
- 黄药师模型绑定用 Windows 注册表环境变量（`HKCU\Environment`），不要在 WSL 里改
- 如必须切模型，改 Windows 侧注册表 + 注销重登 + `wsl --shutdown` 三步
- 不要混用 WSL 里安装的 Linux 原生 Claude Code（它走 OAuth，不支持 API Key）

**关联**：`decisions.md` 2026-05-16 DeepSeek vs Kimi

---

## P-2: tmux session 缓存旧配置

**症状**：改了 `.bashrc` 后 `claude` 行为没变。

**根因**：`claude()` 函数包装了 tmux session `claude`，只要 session 活着，用的是 session 创建时的环境，不是最新 `.bashrc`。

**对策**：改完配置后 `tmux kill-session -t claude`，再重新 `claude`。

---

## P-3: 批量格式升级产生"格式完整但思维空洞"卡片 (C-8)

**症状**：抽检 `motivation-resistance` 和 `peak-end-rule` 两张卡——格式符合 agent-native 标准，但 Claims 无具体反例、Constraints 模板化。

**根因**：批处理只改了结构和 frontmatter，没有触发真正的理解加工。格式门禁检测不到"搬运 vs 理解"。

**对策**：v1.5 新增理解门禁——每条 Constraint 必须有具体场景 + 可验证的失败模式。批量升级后至少抽检 2 张。

