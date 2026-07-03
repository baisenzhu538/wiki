---
id: kdo-input-channel-strategy-2026-06-16
title: KDO 输入渠道策略：飞书、微信、听脑如何接入
type: decision
status: proposed
domain: kdo-infrastructure
author: kimi
reviewed_by: pending
confidence: 0.8
trust_level: medium
source_refs:
- src_unknown
created_at: 2026-06-16
updated_at: '2026-06-29'
related:
- '[[Kimi-月之暗面]]'
- '[[dk-p5-cc-connect-config]]'
- '[[dk-p1-model-switch-env]]'
- '[[tool-ai-voice-input-doubao]]'
- '[[knowledge-delivery-os-快速体验指南-飞书云文档]]'
- agent-native-card-design
- tinyfish-agentic-web-infrastructure
---
# KDO 输入渠道策略：飞书、微信、听脑如何接入

## 背景

用户参加了一场线上分享，分享内容沉淀在飞书文档中。用户希望 Kimi（KDO 入口质量门）能直接读取该文档并做分析。同时用户正在与段王爷（飞书 Hermes agent）沟通，段王爷可以读取飞书文档。用户问：

1. 是否需要给 Kimi Code CLI 同样的飞书权限？
2. 微信群内容除了听脑 API，是否需要搭建 MCP 接入？
3. 输入质量由 Kimi 把关，如何设计？

## 独立判断

### 1. 不给 Kimi Code CLI 飞书权限

**理由**：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

**结论**：保持 Kimi Code CLI 不直接访问飞书内部文档。

### 2. 不立即搭建 MCP

**理由**：
- src_unknown
- src_unknown
- src_unknown

**结论**：MCP 作为 P2 长期规划，不立即实施。触发条件：
- src_unknown
- src_unknown
- src_unknown

### 3. 推荐的最小可行方案（MVP）

#### 3.1 飞书文档

- src_unknown
- src_unknown
  1. 段王爷把文档正文发送到当前 Kimi 对话中；
  2. 段王爷把文档导出为 Markdown/PDF，放到 `00_inbox/`；
  3. 段王爷在飞书里生成一个脱敏摘要，再转给 Kimi。
- src_unknown

#### 3.2 微信群内容

- src_unknown
- src_unknown
  - src_unknown
  - src_unknown
- src_unknown

#### 3.3 统一输入规范

- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
- src_unknown

### 4. 输入质量门由 Kimi 负责

**流程**：

```
外部输入
  ├── 听脑 API 输出 → Kimi 入口质量门
  ├── 飞书文档 → 段王爷转存 → Kimi 入口质量门
  ├── 00_inbox 文件 → Kimi 入口质量门
  └── 用户对话粘贴 → Kimi 入口质量门
              │
              ↓
        高价值段落索引 + 置信度分层
              │
              ↓
        老顽童主力量产卡片
```

**Kimi 质量门职责**：
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 决策

| 事项 | 决定 | 优先级 |
|---|---|---|
| 给 Kimi CLI 飞书权限 | ❌ 不做 | — |
| 立即搭建 MCP | ❌ 不做 | P2 |
| 段王爷中转飞书文档 | ✅ 做 | P0 |
| 微信群继续走听脑 API | ✅ 保持 | P0 |
| 统一输入落到 `00_inbox/` 或对话 | ✅ 做 | P0 |
| Kimi 负责入口质量门 | ✅ 做 | P0 |

## 下一步行动

1. **黄药师**：把本决策中的"统一输入规范"写入 `90_control/ingestion-pipeline.md`。
2. **段王爷**：确认飞书文档转存方式（发送到对话 / 导出到 `00_inbox/` / 生成摘要）。
3. **Kimi**：对当前飞书分享文档，等段王爷或用户把内容转存后，做入口质量门分析。
4. **老顽童**：根据 Kimi 质量门输出量产卡片。

## 关联文件

- src_unknown
- src_unknown
- src_unknown
