---
id: concept-mcp-protocol
title: MCP协议：Agent调用外部工具的统一标准
type: concept
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.82
trust_level: high
language: zh-CN
domain: [yitang, research, ai-collaboration]
source_refs:
- web: MCP specification (modelcontextprotocol.io)
- web: Anthropic MCP documentation
related:
- "[[tool-agent-native-overview]]"
- "[[tool-yitang-ai-research-workflow]]"
---

# MCP协议

> **⚠️ 供应商锁定风险：MCP由Anthropic主导，可能有生态偏向。** Model Context Protocol——让AI Agent说一句话就调用一个外部工具，无需人工配置。

## 核心概念

```
传统：人配置工具 → Agent调用工具 → 人管理工具
MCP：  Agent发现工具 → Agent调用工具 → Agent管理工具
```

MCP是Agent和外部工具之间的"USB接口"——只要工具支持MCP，Agent就能即插即用。

## 对调研的意义

一堂武器库的每一种调研手段，理论上都可以封装为MCP Server：
- "查一下竞对的招聘信息" → Agent自动调用Boss直聘MCP
- "对比A和B的APP数据" → Agent自动调用七麦MCP
- "搜索竞对的技术博客" → Agent自动调用Google搜索MCP

## 当前MCP生态

| 类别 | 已支持的MCP工具 |
|:---|:---|
| Web搜索 | Brave Search, Tavily, Exa |
| Web抓取 | Firecrawl, Apify, Bright Data |
| 数据库 | PostgreSQL, SQLite, Supabase |
| 文件系统 | Filesystem MCP Server |
| GitHub | GitHub MCP Server |

## Agent执行指令

```json
// MCP配置文件示例 (claude_desktop_config.json)
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "@anthropic/firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "your-key" }
    }
  }
}
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 供应商锁定 | Anthropic标准可能导致生态偏向 | 关注竞品协议（如Google A2A） |
| 工具发现失败 | Agent看不到已配置的工具 | 检查MCP Server是否正常运行 |
| 工具权限过大 | Agent可以执行危险操作 | 配置权限白名单 |

## 适用边界

- **适用**：Agent需要自主调用多工具的复杂调研场景
- **不适用**：简单的一次性查询（不需要MCP）
- **注意**：MCP仍在快速演进中，2026年的实现可能半年后就变了

---

*卡片类型：concept | 审核状态：待审*
