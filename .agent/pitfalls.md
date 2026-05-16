# 踩坑记录

每踩一个坑追一条。格式：症状 → 根因 → 对策。

---

## P-1: 切模型改环境变量无效——Claude Code 走全局设置

**症状**：在 WSL `.bashrc` / `.profile` 里 `export ANTHROPIC_*` 设为 Kimi，但 `claude.exe` 始终读不到，一直连 DeepSeek。改 Windows 注册表 + `wsl --shutdown` 也无效。

**根因**：Claude Code 的模型/API 配置有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 侧等价路径），优先级高于环境变量。单独改 env var 或注册表都不生效——全局设置覆盖一切。

**对策**：
- **不要逐项改环境变量**——直接改 Claude Code 的全局设置文件
- 全局设置的模型/API endpoint/Key 一处修改即生效，无需注销重登

**关联**：`decisions.md` 2026-05-16 DeepSeek vs Kimi

**⚠️ 2026-05-16 补充**：P-1 的初始诊断不完全准确。真正的覆盖源对飞书黄药师而言是 cc-connect 的 systemd `env.conf` drop-in（见 P-5），对 CLI 黄药师则可能是全局设置或注册表。两者互不影响——这就是为什么 CLI 黄药师正常工作而飞书黄药师 401。

---

## P-2: tmux session 缓存旧配置

**症状**：改了 `.bashrc` 后 `claude` 行为没变。

**根因**：`claude()` 函数包装了 tmux session `claude`，只要 session 活着，用的是 session 创建时的环境，不是最新 `.bashrc`。

**对策**：改完配置后 `tmux kill-session -t claude`，再重新 `claude`。

---

## P-3: Hermes 换 API Key 后仍然 401 — auth.json 缓存覆盖 .env

**症状**：更新 `~/.hermes/profiles/*/.env` 中的 `KIMI_API_KEY` 后重启服务，仍然 HTTP 401，日志显示用的还是旧 Key。用户和欧阳锋多轮尝试换新 Key 无效——"系统顽固用旧的覆盖新的"。

**根因（3 层）**：
1. **改错了 .env** — Hermes 加载 `~/.hermes/.env`（全局），不是 `~/.hermes/profiles/<name>/.env`。profile 下的 .env 根本不被读取
2. **auth.json 缓存** — `~/.hermes/auth.json` 的 `credential_pool.kimi-coding[]` 缓存了旧 Key 的 access_token + `last_status: exhausted`，Hermes 优先用缓存而不是重读 env
3. **Provider 名** — 之前用过 `kimi-for-coding`，正确是 `kimi-coding`

**对策**：
- API Key 换新时三处同步更新：`~/.hermes/.env` + `~/.hermes/auth.json` credential_pool + `~/.hermes/profiles/*/config.yaml` provider 名
- 改完后清掉 auth.json 里的 `last_status/exhausted` 和 `last_error_code/401`，否则 Hermes 认为 Key 已死会跳过
- 用 `journalctl --user -u hermes-gateway-* --no-pager -n 30 | grep -i "401\|auth"` 验证无认证错误

---

## P-4: 批量格式升级产生"格式完整但思维空洞"卡片 (C-8)

**症状**：抽检 `motivation-resistance` 和 `peak-end-rule` 两张卡——格式符合 agent-native 标准，但 Claims 无具体反例、Constraints 模板化。

**根因**：批处理只改了结构和 frontmatter，没有触发真正的理解加工。格式门禁检测不到"搬运 vs 理解"。

**对策**：v1.5 新增理解门禁——每条 Constraint 必须有具体场景 + 可验证的失败模式。批量升级后至少抽检 2 张。

---

## P-5: cc-connect 切模型后 CLI 正常但飞书 401 + 找不到文件夹

**症状**：从 Kimi 切回 DeepSeek 后，WSL 终端的 `claude` 命令正常工作，但飞书黄药师报 `HTTP 401` 且无法访问 wiki/KDO。

**根因（2 个残留文件未回切）**：
1. `~/.config/systemd/user/cc-connect.service.d/env.conf` —— Kimi 时代的 systemd Environment drop-in，仍指向 `https://api.kimi.com/coding` + Kimi Key。systemd `Environment=` 注入的 env var 优先级最高，覆盖 `.bashrc` 和注册表
2. `~/.cc-connect/config.toml` —— `work_dir` 从 `/mnt/c/Users/Administrator/Desktop/wiki` 被改为 `/home/dministrator`（Kimi 切换期间重置的），导致 Claude Code 从 home 目录启动，读不到 wiki 的 `CLAUDE.md`

**为什么 CLI 黄药师正常**：CLI 走 `.bashrc` → tmux session env，和 cc-connect 的 systemd env 互不影响。两条独立的配置链路。

**对策**：
- 切模型/切 API 时，cc-connect 的配置有**独立的两个文件**需要同步：
  1. `config.toml` → 模型/API 通过 provider 或 env 注入
  2. `cc-connect.service.d/env.conf` → systemd 环境变量
- 改完后 `systemctl --user daemon-reload && systemctl --user restart cc-connect`
- 验证：`systemctl --user show cc-connect | grep Environment`

**关联**：Config Cascade Debug skill — 这本质是同一模式：多个独立配置层（.bashrc / 注册表 / systemd drop-in / cc-connect config.toml），改了三处漏了一处。

---

## P-6: cc-connect 修好 work_dir + API Key 后仍然空响应 — session 缓存了失效的 Claude Code session ID

**症状**：cc-connect 的 `work_dir` 和 `env.conf` 都已修正（→ wiki vault + DeepSeek），飞书发消息后 bot 返回空。日志显示 `is_resume=true`，紧接着 `exit status 1: No conversation found with session ID: cb687591...`。

**根因**：cc-connect 的 session 文件（`~/.cc-connect/sessions/huangyaoshi_53de3c3f.json`）里存了 `agent_session_id`，指向 Claude Code 在**旧 work_dir**（`/home/dministrator`）下创建的 session。work_dir 已改为 wiki vault 后，Claude Code 的 wiki 项目里不存在这个 session ID，resume 失败，返回空。

**为什么之前的 401 错误也写入了同一个 session**：这个 session 是在 Kimi 配置期间创建的，所有 401 错误都被写入了 session history。修好 API Key 后 session 里仍有 `agent_session_id` 指向不存在的位置，所以 Claude Code 启动即失败。

**对策**：
- 修改 cc-connect 的 `work_dir` 后，必须同时删除对应的 session 文件（`~/.cc-connect/sessions/<project>_<hash>.json`），否则旧 session ID 无法 resume
- 删除后重启 cc-connect，下次消息自动创建全新 session

**关联**：P-5（同一个事故链的第三环：work_dir 错 → env.conf 错 → session 缓存错）。Config Cascade Debug skill 的 Layer 0（运行时缓存）又一次成为最后一层漏网之鱼。

---

## P-7: 素材预处理缺少 OCR 强制检查——执行者跳过图片

**症状**：科学决策文件夹有 35 张关键框架图（共识四层冰山、ROI 全景图、X 型 Y 型对比等），老顽童声称"没有图片需要 OCR"。欧阳锋未核实即采信。后发现 35 张图全部未 OCR，图中含有口述稿未系统展开的结构信息。

**根因**：
1. inbox 素材预处理缺少 OCR 检查点——没有强制步骤要求"如果文件夹里有 PNG，先跑 OCR 再进管线"
2. 架构者（欧阳锋）在长对话中判断力下降，未独立核实执行者的声明

**对策**：
- 新域素材消化第一步：扫描文件夹 → 如有图片，强制 OCR 全部后再读文本
- 架构者审查新域提案时，独立验证"素材是否全部消化"——不能只信执行者的自述
- 长对话中出现判断失误时主动收尾，下次干净状态接手

