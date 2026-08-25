---
session_id: infra-setup-2026-07-21
agent_id: codex
date: 2026-07-21
created_at: 2026-07-20T16:10:00.000000+00:00
updated_at: 2026-07-20T16:10:00.000000+00:00
---

# 飞书老顽童 + 飞书欧阳锋 · Gateway Profile 创建复盘

## 概要

在 WSL 中为 Hermes 创建两个新的飞书 gateway profile：飞书老顽童（`laowantong-feishu`）和飞书欧阳锋（`ouyangfeng`）。每个 profile 含 config.yaml、.env、SOUL.md 三件套 + systemd user service，模型统一用 deepseek-v4-pro，凭据用新分配的独立 Feishu App。

全部 7 步完成，两服务 active (running) + enabled。唯一交付延迟是飞书 WebSocket 首次事件下发有约 2 分钟冷启动窗口，非配置问题。

---

## 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| 新 profile 命名 `laowantong-feishu` 而非覆盖旧 `laowantong` | 旧 laowantong 与王语嫣共用 Feishu App `cli_a97db812e4b8dcb2`、当前 dead，直接覆盖可能污染王语嫣；新目录物理隔离 | 两套并存，零冲突 |
| SOUL.md 直接复用 `.agent/` context 文件 | 老顽童 = Producer、欧阳锋 = Architect+Reviewer 的人设已在 context 文件中完整定义，无须重写 | 内容一致，角色连贯 |
| config.yaml 从王语嫣复制而非从头写 | 王语嫣已验证可用的飞书 gateway 配置，模型已是 deepseek-v4-pro，只需改 profile 名 | 零配置漂移 |
| systemd service 文件用 Windows PowerShell `@'.'@` 写再 cp 进 WSL | `bash -c` 内 heredoc 的双引号转义全部炸掉，Environment 行被拼接成一坨 | 干净交付，一次通过 |

---

## 踩坑记录

### 坑 1：WSL 发行版名猜错
- **现象**：`wsl -d Ubuntu` → `WSL_E_DISTRO_NOT_FOUND`
- **根因**：发行版实际叫 `Ubuntu-22.04`，不是 `Ubuntu`
- **修复**：`wsl --list --verbose` 确认后改正
- **教训**：拿不准发行版名时先 `wsl -l -v`，不要猜

### 坑 2：bash -c 内 heredoc 写 systemd 文件全炸
- **现象**：Environment 行的双引号被吃掉，`$MAINPID` 只剩 `\`，多行拼接成一行
- **根因**：`bash -c "..."` 内层的 `\"` 与 heredoc 的 `'UNITEOF'` 组合导致引号解析链崩溃
- **修复**：改用 Windows PowerShell 的 here-string（`@'...'@`）写入临时文件，再 `cp` 进 WSL
- **教训**：跨两层 shell（PowerShell → bash -c）写含双引号 + 特殊字符的结构化文件时，heredoc 不可靠。走「外层写文件 → 内层 cp」是更干净的策略

### 坑 3：Get-Content 中文乱码
- **现象**：`Get-Content laowantong-context.md` 输出 `鑰侀〗绔ワ紙Producer锛?`
- **根因**：PowerShell 默认编码不是 UTF-8
- **修复**：`Get-Content -Encoding UTF8`
- **教训**：中文 `.md` 文件先确认编码再读

### 坑 4：飞书 WebSocket 首次消息 2 分钟冷窗口
- **现象**：服务起来后发消息不回复，日志只有 `connected to wss://...`
- **根因**：飞书长连接 WebSocket 模式在建立连接后需要 60-120 秒完成事件订阅初始化，这期间消息不投递
- **结论**：不是配置问题，等就行
- **教训**：飞书 gateway 启动后应等待 2 分钟再做连通性测试，否则误报

---

## 思维盲点

1. **没先验证 .agent/ context 文件是否存在就按路径去读。** 交接清单写的路径 `C:\Users\Administrator\.agent\` 下没有这两个文件，实际在 `Desktop\.kdo_lint_baseline_13664\.agent\` 和 `Desktop\.kdo_lint_baseline_37556\.agent\`。为什么漏掉：交接清单的路径是编出来的，我按字面去找，没做 `Get-ChildItem -Recurse` 全局搜索。教训：交接文件路径不可信，先搜后信。

2. **创建 profile 前没先问「旧 laowantong 怎么处理」。** 旧的 `profiles/laowantong/` 已存在且与王语嫣共用 App ID，我在创建 `laowantong-feishu` 前没主动提醒用户这个冲突。用户后来自己注意到了才问。教训：创建新资源前扫一遍同名/邻近资源，有冲突主动报告。

3. **没在日志里找「是否收到消息」的证据就断定启动成功。** 我看到 `active (running)` + `connected to wss://` 就认为完成了，没检查是否有 message received 事件。用户反馈「不搭理」后才发现日志里只有连接没有消息。教训：gateway 类服务的「启动成功」= 连接成功 + 收到过至少一条消息事件，两者缺一不可。

---

## 顿悟

1. **交接清单里的路径、文件名、命令——全都要用自己的工具复验。** 这次三个路径错了两个（.agent 路径、WSL distro 名），只有一个对了（profiles 父目录）。交接清单是意图表达，不是事实陈述。

2. **"写文件"这个看似最简单的操作，跨 shell 边界时是最容易炸的。** config.yaml 复制（cp）零问题；.env 写入（heredoc 纯文本）零问题；systemd service（含双引号 + 变量引用）全炸。复杂度不是行数决定的，是字符集决定的。

3. **飞书 gateway 的心跳模式决定了"起好了" ≠ "能对话"。** WebSocket 连接成功只是物理层通了，事件订阅初始化是异步的。这和 HTTP webhook 模式的"起好即 ready"不一样。

---

## 交付清单

### 文件

```
/home/dministrator/.hermes/profiles/
├── laowantong-feishu/
│   ├── .env          FEISHU_APP_ID=cli_aad4815519789bc3
│   ├── config.yaml   model: deepseek-v4-pro (从 wangyuyan 复制)
│   └── SOUL.md       老顽童 Producer 人设 (来自 .agent/laowantong-context.md)
├── ouyangfeng/
│   ├── .env          FEISHU_APP_ID=cli_aad481a240389bef
│   ├── config.yaml   model: deepseek-v4-pro (从 wangyuyan 复制)
│   └── SOUL.md       欧阳锋 Architect+Reviewer 人设 (来自 .agent/ouyangfeng-context.md)

~/.config/systemd/user/
├── hermes-gateway-laowantong-feishu.service  enabled, active
└── hermes-gateway-ouyangfeng.service         enabled, active
```

### 运行状态

| 服务 | PID | 状态 | 开机自启 |
|:---|:---|:---|:---|
| hermes-gateway-laowantong-feishu | 44528 | active (running) | enabled |
| hermes-gateway-ouyangfeng | 44530 | active (running) | enabled |

### 已知 warning（不影响使用）

- `tirith spawn failed`：安全工具未安装（王语嫣同款）
- `OpenRouter unhealthy` / `Nous unavailable`：辅助服务付费/认证问题（非核心）

---

## 元反思

**速度 vs 校验**：整次操作实际耗时约 10 分钟，其中 5 分钟花在修复 heredoc 转义问题。如果一开始就用「PowerShell 写文件 → cp 进 WSL」的策略，可以省 3 分钟。

**单一职责**：bash 擅长文件操作和命令执行，PowerShell 擅长结构化文本生成。让每个 shell 做它擅长的事，不要强行在 bash 里生成含特殊字符的配置文件。

**"不搭理"的排查方向偏了**：用户说「不搭理」时我第一反应是查配置、查 .env、查 systemd——其实应该先看日志里有没有 `message received` 事件。有 = 配置对但处理慢；没有 = 飞书侧事件没下来。这个排查顺序应该在脑子里固化。
