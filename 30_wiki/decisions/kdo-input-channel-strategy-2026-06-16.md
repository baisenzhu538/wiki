---
id: kdo-input-channel-strategy-2026-06-16
title: KDO 输入渠道策略：飞书、微信、听脑如何接入
type: decision
status: proposed
domain:
- kdo-infrastructure
author: kimi
reviewed_by: pending
confidence: 0.80
trust_level: medium
source_refs:
- source_unknown
created_at: 2026-06-16
updated_at: 2026-06-16
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
- Kimi Code CLI 是本地开发/管理工具，运行环境是 Windows + Git Bash，不是飞书 agent。
- 段王爷能读飞书是因为他运行在 Hermes → 飞书 channel 上，天然携带用户的飞书登录态。
- 给 CLI 配置飞书 access_token 会增加权限泄露面和运维复杂度，且与 CLI 的核心职责（本地知识库管理）不匹配。
- 当前飞书文档抓取已验证失败（`kdo fetch-url` 返回 302 重定向循环）。

**结论**：保持 Kimi Code CLI 不直接访问飞书内部文档。

### 2. 不立即搭建 MCP

**理由**：
- MCP（Model Context Protocol）是连接 LLM 与外部数据源/工具的协议，适合多 agent、多工具、长期生态。
- 当前 KDO 核心流程（素材 → 入口质量门 → 老顽童量产 → 欧阳锋抽检）尚未跑顺，过早引入 MCP 会增加抽象层和维护成本。
- 当前稳定的输入源只有 2 个：听脑 API（微信/录音）、飞书文档（通过段王爷中转）。还没到必须用 MCP 统一的程度。

**结论**：MCP 作为 P2 长期规划，不立即实施。触发条件：
- 输入源稳定超过 3-4 个；
- 多个 agent（Kimi/Claude/段王爷/老顽童）需要共享同一套工具；
- 有明确的开发者愿意维护 MCP server。

### 3. 推荐的最小可行方案（MVP）

#### 3.1 飞书文档

- **段王爷作为飞书入口**：段王爷在飞书 channel 读取文档后，将内容转存到 Kimi Code CLI 可访问的位置。
- **转存方式**（按优先级）：
  1. 段王爷把文档正文发送到当前 Kimi 对话中；
  2. 段王爷把文档导出为 Markdown/PDF，放到 `00_inbox/`；
  3. 段王爷在飞书里生成一个脱敏摘要，再转给 Kimi。
- **禁止**：Kimi Code CLI 直接拿飞书链接去抓。

#### 3.2 微信群内容

- **继续用听脑 API**：这是已经验证的、结构化的文本输入源。
- **补充方式**：
  - 重要群聊精华由用户或指定整理员手动导出，放入 `00_inbox/`；
  - 不建议使用微信机器人/Hook，存在账号风险和 TOS 风险。
- **质量把关**：Kimi 对听脑输出做入口质量门，判断哪些内容值得进 KDO。

#### 3.3 统一输入规范

- 所有外部输入必须先落到以下位置之一：
  - `00_inbox/` 下的文件
  - 当前 Kimi 对话中的粘贴文本
  - 已公开可抓取的 URL（如公开博客、GitHub）
- 不处理需要登录态的内部链接。

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
- 判断素材级别（P0/P1/P2）
- 提取高价值段落
- 给出 confidence 分层
- 标注矛盾点和风险
- 输出建议出卡清单
- 不直接写最终卡片

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

- `90_control/ingestion-pipeline.md`
- `.agent/toolkit.md`
- `70_product/tasks/huangyaoshi-next-tasks.md`
