---
title: "复盘：Codex + Kimi 安装踩坑全记录"
type: improvement-plan
status: stable
domain:
  - master
  - infrastructure
created_at: 2026-06-06
author: 黄药师
tags:
  - codex
  - kimi
  - proxy
  - windows-sandbox
  - protocol-translation
---

# 复盘：Codex + Kimi 安装踩坑全记录

> 目标：Windows 10 上安装 Codex CLI v0.137.0，接入 Kimi Code API
> 结果：❌ 未完全成功（沙箱阻断 localhost，无法修复）
> 后续：周一从办公室 Win11 电脑获取 CCX 完整配置

---

## 一、背景

用户另一台 Win11 电脑上，Claude Code 通过 CCX 十分钟装好了 Codex + Kimi，全程自动化。这台 Win10 电脑尝试复现。

## 二、尝试过的路径

### 路径 1：直连 Kimi Code API（失败）

Codex v0.137.0 强制使用 OpenAI Responses API（`wire_api = "responses"`），Kimi Code API 的 OpenAI 端点只支持 Chat Completions。

- 端点：`https://api.kimi.com/coding/v1`
- 错误：`/v1/responses` 不存在 → 404

### 路径 2：降级 Codex 到 v0.80.0 + chat wire_api（失败）

Codex v0.80.0 支持 `wire_api = "chat"`，兼容 Kimi Chat Completions。

- 错误：Kimi OpenAI 端点有 Agent 白名单，拒绝 Codex → 403
- 白名单：Kimi CLI / Claude Code / Roo Code / Kilo Code

### 路径 3：BenedictKing/ccx Go 代理（失败）

下载了 CCX v2.8.24（Go binary），试图通过它做协议翻译。

- 问题 1：CCX Web UI 的 API 鉴权过不去（尝试了所有已知 header）
- 问题 2：CCX config.json 的渠道配置格式不兼容
- 问题 3：Windows 10 上 Chat 渠道不被识别（WSL 上同样问题）
- GitHub 连不上 → 无法下载 CC Switch 桌面版

### 路径 4：自研 Python 代理（✅ 协议通，❌ 沙箱拦截）

自己写了 `kimi-proxy.py` 做完整协议翻译。

#### 4.1 架构

```
Codex (Responses API) → Proxy :8787 → Kimi Anthropic API
   显示 GPT-5.5          协议翻译         无白名单
```

#### 4.2 已解决的问题

| 问题 | 修复 |
|:------|:-----|
| Anthropic SSE `data:` 后无空格 | `startswith("data:")` 不带空格 |
| `developer` role 不被 Anthropic 接受 | 映射为 `user` |
| Codex system prompt 太长 | 放首条 user message，不走 `system` 字段 |
| SSE 事件序列不完整 | 补全 10 个事件（created/in_progress/output_item/...） |
| WebSocket 405 后不回退 HTTPS | `supports_websockets = false` |
| 工具调用协议翻译 | OpenAI tools → Anthropic tools + SSE 事件翻译 |
| 中文编码 | 强制 UTF-8 输出 |

#### 4.3 未解决的问题

**核心阻塞：Codex 的 Windows 沙箱阻断 localhost 连接。**

- PowerShell 测试 `curl localhost:8787` → ✅ 200
- Codex 访问 `localhost:8787` → ❌ 502（请求从未到达代理）

尝试了：
- 去除 Windows sandbox 配置
- 使用 unelevated sandbox
- 换端口（8787 → 80 → 9876）
- 绑 0.0.0.0 用物理 IP
- 把代理搬到 WSL
- 纯 Python stdlib（无 aiohttp）
- 完全重装 Codex

全部无效。Codex 的请求日志始终为空——请求从未到达代理。

### 路径 5：CC Switch 桌面版（未完成）

下载了 CC-Switch v3.16.1（带 Chat→Response 协议转换的桌面工具）。

- 问题：MSI 安装后找不到程序（疑似 Win10 兼容性问题）
- 尝试了两次安装均失败

### 路径 6：npm 包尝试（失败）

- `@t59688/ccx` v0.1.3：只是个配置管理工具，不做协议翻译
- `codex-kimi-hardwarex`：Windows 路径兼容性问题（ESM URL scheme 错误）

---

## 三、根本原因分析

**Windows 10 的 Codex sandbox 阻断了进程对 localhost 的网络访问。** Win11 上没有这个问题——用户办公室电脑相同配置能正常工作。

这个行为不取决于：
- sandbox_mode 配置值
- 端口号
- 代理实现（aiohttp vs stdlib）
- Codex 版本（v0.80.0 和 v0.137.0 均有此问题）

Windows 10 的 sandbox 机制可能与 Win11 不同——Win10 的 restricted token 隔离了 loopback 网络。

---

## 四、最终状态

| 组件 | 状态 |
|:------|:----:|
| Codex CLI v0.137.0 | ✅ 已安装 |
| kimi-proxy.py（协议翻译） | ✅ 完成，curl 测试通过 |
| 工具调用翻译 | ✅ 协议层完成 |
| 网络连通 | ❌ Codex sandbox 阻断 |
| 开机自启 | ✅ Kimi-Proxy 计划任务 |

**Codex 可以启动、显示 TUI、接收输入——但发送消息后请求被沙箱拦截，无法到达代理。**

---

## 五、周一行动计划

1. 从办公室 Win11 电脑获取：
   - `npm list -g --depth=0`（看安装了哪些包）
   - CCX / CC Switch 的 Web 管理界面截图（渠道配置、模型映射）
   - 任务管理器里 CCX 相关进程列表
2. 如果那台电脑用的是 CC Switch 桌面版——直接拷安装包
3. 如果 CCX 是特定版本/配置——原样复制

---

*黄药师 · 2026-06-06*
