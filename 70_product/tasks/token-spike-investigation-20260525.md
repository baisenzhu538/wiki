---
title: Token 暴涨排查报告
type: report
status: stable
created_at: 2026-05-25
updated_at: 2026-05-25
---

# Token 暴涨排查报告

## 排查范围

| 系统 | 路径 | LLM Provider | 是否消耗 DeepSeek |
|------|------|:--:|:--:|
| Claude Code (本会话) | `deepseek-v4-pro` via `api.deepseek.com/anthropic` | DeepSeek | ✅ |
| Claude Code Hub (WSL) | `wslrelay` → WSL uvicorn :8765 | DeepSeek | ✅ |
| Claudian (Obsidian 插件) | 通过 Hub 调用 Claude Code | DeepSeek | ✅ |
| KDO CLI `enrich --llm` | `api.kimi.com/coding/v1/messages` | **Kimi** | ❌ |
| Hermes 老顽童 Gateway | `api.kimi.com/coding/v1/messages` | **Kimi** | ❌ |
| Hermes 段王爷 Gateway | kimi-coding | **Kimi** | ❌ |
| Hermes Beikai Gateway | kimi-coding | **Kimi** | ❌ |

**结论：DeepSeek token 消耗唯一来源 = Claude Code 及其 Obsidian 插件。**

---

## 发现

### 1. Claude Code 会话量巨大

| 会话 ID | 大小 | 行数 | 用户消息 | 活跃期 |
|------|:--:|:--:|:--:|------|
| `5012c759` | **58.6 MB** | 19,414 | 4,955 | May 5-23 |
| `c9f1d934` | **36.76 MB** | 12,221 | 2,934 | May 23 高峰 |
| `b339a7e2` | 2.47 MB | — | 211 | May 23-24 |

- `5012c759`：Claudian SDK (`entrypoint: sdk-ts`) 持续 19 天，日均 ~260 条用户消息
- `c9f1d934`：5 月 23 日单日 1,734 条消息——这很可能是 token 暴涨的直接原因

### 2. Claude Code Hub 持续运行

- `wslrelay` (PID 9744) 监听端口 8765，将 WSL 内 uvicorn hub 转发到 Windows
- Claudian Obsidian 插件通过 Hub 持续调用 Claude Code
- Hub 自 May 2 起持续运行，未重启

### 3. Hermes Gateway 有 60 秒 Cron Ticker

- 老顽童 Gateway 每 60 秒执行 cron ticker（虽然用的是 Kimi）
- 如果未来切到 DeepSeek，这是一个风险点

### 4. 无死循环证据

- KDO CLI `while True` 循环均不调用 LLM（watch / validate-watch / health_check 都是纯文件扫描）
- Hermes agent 日志显示正常的用户对话模式，无异常重试风暴
- 无 Claude Code `/loop` 或 scheduled task 配置

---

## 根因判断

**5 月 23-24 日 token 暴涨最可能的原因：Claudian (Obsidian 插件) 大量调用 + Claude Code 会话累积。**

`c9f1d934` 会话在 5 月 23 日单日 1,734 条消息，加上 `5012c759` 持续 19 天的高频使用，Claude Code 的 DeepSeek 消耗被 Claudian 放大。不是某个进程"死循环"，而是 Obsidian 侧的自动补全/内联建议等功能持续触发 API 调用。

用户重启电脑后未复现，是因为重启后旧的 Claudian 会话被终止，新会话从零开始。

---

## 风险清单

| # | 风险 | 严重度 | 说明 |
|:--:|------|:--:|------|
| 1 | Claudian 无频率限制 | 🔴 高 | Obsidian 插件可无限制调用 Claude Code，无 rate limit 或 cooldown |
| 2 | Claude Code Hub 永不超时 | 🔴 高 | uvicorn hub 自 May 2 运行至今，会话永不过期 |
| 3 | Hermes cron ticker 60s | 🟡 中 | 目前用 Kimi 无影响，切 DeepSeek 后每天 1,440 次调用 |
| 4 | 4 个 Hermes Gateway 计划任务 | 🟡 中 | 系统启动自动拉起，多个实例可能同时运行 |
| 5 | 会话文件无限增长 | 🟡 中 | 58MB + 36MB 会话文件不清理，磁盘和内存压力 |

---

## 建议

1. **给 Claudian 加频率限制**：在 Obsidian 插件侧设置最小调用间隔（如 2 秒），防止连续触发
2. **定期重启 Claude Code Hub**：每周重启一次 WSL 内的 uvicorn hub，防止会话无限累积
3. **监控 DeepSeek 用量**：在 DeepSeek 控制台设置用量告警（如单日超过 X tokens 即通知）
4. **清理旧会话文件**：>1MB 的 `.jsonl` 会话文件可定期归档或删除
5. **暂停不需要的 Hermes Gateway**：Beikai 和 Duanwangye 的 Gateway 当前非活跃状态，可禁用计划任务

---

## 立即行动项

- [ ] 关闭不需要的 Hermes 计划任务（Beikai / Duanwangye）
- [ ] 在 DeepSeek 控制台设置用量告警
- [ ] 后续观察：如果 token 再次暴涨，重点检查 Claudian + `wslrelay` 进程
