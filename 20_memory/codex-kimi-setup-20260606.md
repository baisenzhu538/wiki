# Codex + Kimi Code API 配置复盘

> Windows 10 · Codex v0.137.0 · Kimi Code API · 2026-06-06

---

## 一、核心问题

Kimi Code API 有两个限制导致 Codex 无法直连：

| 问题 | 原因 |
|:------|:-----|
| Agent 白名单 | Kimi OpenAI 端点只允许 Kimi CLI / Claude Code / Roo Code / Kilo Code |
| 协议不匹配 | Codex v0.137.0 只用 Responses API，Kimi OpenAI 端点只支持 Chat Completions |

**解法**：Codex → 本地代理 → **Kimi Anthropic 端点**（无白名单，且 Claude Code 天生用这个协议。）

```
Codex (Responses API) → proxy :8787 → Kimi Anthropic API (/v1/messages)
  显示 GPT-5.5            协议翻译           无白名单，Claude Code 同款通道
```

---

## 二、文件清单

| 文件 | 位置 | 用途 |
|:------|:-----|:-----|
| `kimi-proxy.py` | `~/.codex/` | 协议翻译代理 |
| `config.toml` | `~/.codex/` | Codex 配置 |
| `auth.json` | `~/.codex/` | API Key（写 dummy 值即可） |
| 开机自启 | 计划任务 `Kimi-Proxy` | 重启后自动启动代理 |

---

## 三、Codex 配置

`~/.codex/config.toml`：

```toml
#:schema https://developers.openai.com/codex/config-schema.json

model_provider = "kimi"
model = "gpt-5.5"
sandbox_mode = "workspace-write"

[model_providers.kimi]
name = "kimi"
base_url = "http://127.0.0.1:8787/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false

[windows]
sandbox = "elevated"

[features]
experimental_windows_sandbox = true
elevated_windows_sandbox = true
```

**关键配置说明**：

- `base_url` 指向本地代理
- `supports_websockets = false` **必须设置**——否则 Codex 先试 WebSocket 失败后不降级 HTTPS
- `model = "gpt-5.5"` —— Codex 显示这个模型名，实际由代理转发到 Kimi

---

## 四、代理脚本

`~/.codex/kimi-proxy.py`，依赖 `aiohttp`：

```bash
pip install aiohttp
```

### 4.1 协议翻译

```
Codex 请求 (Responses API)          →  Kimi 请求 (Anthropic Messages API)
─────────────────────────────────       ──────────────────────────────────
instructions (system prompt)         →  system（截断为简短提示）
input[].role = "developer"           →  role = "user"（Anthropic 不认 developer）
input[].role = "user"                →  role = "user"  
input[].content (string or list)    →  content (string)
max_output_tokens                    →  max_tokens
stream: true                         →  stream: true
```

### 4.2 SSE 事件翻译

代理必须输出完整的 OpenAI Responses SSE 事件序列：

```
response.created          → Kimi message_start
response.in_progress      → （代理生成）
response.output_item.added → Kimi content_block_start
response.content_part.added → （代理生成）
response.output_text.delta → Kimi content_block_delta（逐个 token）
response.output_text.done  → （代理生成）
response.content_part.done → Kimi content_block_stop
response.output_item.done  → （代理生成）
response.completed         → Kimi message_stop
```

**SSE 格式要求**：`\r\n\r\n` 分隔，每事件含 `event:` 和 `data:` 行。

### 4.3 踩过的坑

| 坑 | 表现 | 修复 |
|:----|:-----|:-----|
| Anthropic SSE 的 `data:` 后面无空格 | 解析不到事件 | `startswith("data:")` 不带空格 |
| `developer` role 发给 Anthropic | Kimi 400 "tokenization failed" | 映射为 `user` |
| Codex system prompt 太长 | Kimi 400 "tokenization failed" | 替换为简短 system prompt |
| 少发 SSE 事件 | Codex 静默无回复 | 补全 10 个事件的完整序列 |
| WebSocket 405 后不回退 | 一直重连 | `supports_websockets = false` |
| aiohttp SSE chunk 截断 | 0 chars streamed | 用 `await r.text()` 全量读再解析 |

---

## 五、开机自启

Windows 计划任务 `Kimi-Proxy`：

```
触发器：用户登录时
操作：python C:\Users\Administrator\.codex\kimi-proxy.py
工作目录：C:\Users\Administrator\.codex
```

PowerShell 创建命令：

```powershell
$action = New-ScheduledTaskAction -Execute "python" `
  -Argument "C:\Users\Administrator\.codex\kimi-proxy.py" `
  -WorkingDirectory "C:\Users\Administrator\.codex"
$trigger = New-ScheduledTaskTrigger -AtLogon
$principal = New-ScheduledTaskPrincipal -UserId "Administrator" -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -RestartCount 5 `
  -RestartInterval (New-TimeSpan -Minutes 1)
Register-ScheduledTask -TaskName "Kimi-Proxy" -Action $action `
  -Trigger $trigger -Principal $principal -Settings $settings -Force
```

---

## 六、故障排查

```powershell
# 代理是否在运行？
curl -s http://127.0.0.1:8787/v1/models

# 代理日志
cat ~/.codex/proxy.log

# 端口被占用？
netstat -ano | findstr 8787

# 查看计划任务
schtasks /query /tn Kimi-Proxy
```

---

## 七、已知限制

1. **Codex 显示 GPT-5.5 但实际用 Kimi**——代理劫持了请求，模型名只是显示
2. **system prompt 被替换为简短版本**——Codex 原版引导语太长，Kimi tokenizer 处理不了
3. **调试日志写入 `~/.codex/proxy.log`**——正常使用时可以关掉日志
4. **Anthropic API Key 硬编码在代理中**——如需换 Key，改 `kimi-proxy.py` 第 9 行

---

## 八、另一台电脑（Win11）为什么用 CCX 十分钟装好

那台电脑上的 Claude Code 推荐并安装了 CCX（BenedictKing/ccx + CC Switch 组合），它是一个完整的代理方案，自带：
- 协议翻译（Responses ↔ Chat / Anthropic）
- Web UI 配置管理
- 开机自启

这台电脑因为 GitHub 连不上，无法下载 CCX 运行所需的完整组件，所以手写了代理。**功能等价，只是安装方式不同。**
