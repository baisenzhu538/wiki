# 踩坑记录

每踩一个坑追一条。格式：症状 → 根因 → 对策。

---

## P-1: 切模型改环境变量无效——Claude Code 走全局设置

**症状**：在 WSL `.bashrc` / `.profile` 里 `export ANTHROPIC_*` 设为 Kimi，但 `claude.exe` 始终读不到，一直连 DeepSeek。改 Windows 注册表 + `wsl --shutdown` 也无效。

**根因**：Claude Code 的模型/API 配置有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 侧等价路径），优先级高于环境变量。单独改 env var 或注册表都不生效——全局设置覆盖一切。

**对策**：
- **不要逐项改环境变量**——直接改 Claude Code 的全局设置文件
- 全局设置的模型/API endpoint/Key 一处修改即生效，无需注销重登
- 黄药师已验证此路径可行（最终修好以此为准）

**关联**：`decisions.md` 2026-05-16 DeepSeek vs Kimi（注意：该决策写于错误诊断之前，实际可通过全局设置切模型）

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

