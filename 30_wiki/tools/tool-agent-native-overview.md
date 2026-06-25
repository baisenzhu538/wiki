---

id: tool-agent-native-overview
title: Agent原生调研工具总览：2025-2026新范式
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
trust_level: high
language: zh-CN
domain: [yitang, research, ai-collaboration]
source_refs:
- web: Web scraping APIs for AI agents (Grokipedia, 2026)
- web: Firecrawl, Crawl4AI, ScrapeGraphAI docs
- web: MCP protocol specification (modelcontextprotocol.io)
related:
  - '[[tool-agent-firecrawl]]'
  - '[[tool-agent-crawl4ai]]'
  - '[[tool-dns-intelligence]]'
  - '[[tool-osint-wayback]]'
  - '[[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]]'
- "[[tool-osint-overview]]"
- "[[tool-yitang-ai-research-workflow]]"
---

# Agent原生调研工具总览

> **⚠️ 2025-2026新范式，工具变化快。本卡信息截至2026-06。** 传统调研工具以"人手动操作"为假设。2025年后涌现了大量专为AI Agent设计的工具——输入自然语言，输出结构化数据。

## 核心范式转变

```
传统：人 → 浏览器 → 搜索 → 阅读 → 复制 → 粘贴 → 整理
Agent原生：Agent → API调用 → 结构化输出 → 自动分析
```

## 核心工具速览

| 工具 | 一句话 | 为何对Agent重要 |
|:---|:---|:---|
| **Firecrawl** | URL→Markdown，专为LLM设计 | Agent直接"读取"网页 |
| **Crawl4AI** | 开源+自然语言提取 | "提取这个页面所有产品名和价格" |
| **ScrapeGraphAI** | LLM理解网页结构 | 网页改版不影集提取 |
| **MCP协议** | Agent调用外部工具的标准 | Anthropic主导的开放标准 |

## Agent执行指令

```bash
# Firecrawl API
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H "Authorization: Bearer $FIRECRAWL_KEY" \
  -d '{"url":"https://target.com","formats":["markdown"]}'

# Crawl4AI (本地部署)
pip install crawl4ai
crawl4ai --url https://target.com --output-format markdown
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| API变化 | 工具升级后旧代码失效 | 固定API版本号，定期检查changelog |
| 反爬升级 | 某些网站开始封锁Agent请求 | 轮换IP/UA，降级到截图+OCR |
| 供应商锁定 | 过度依赖单一工具 | 每个能力至少备选2个工具 |

## 适用边界

- **适用**：Agent自主调研场景、需要批量采集的场景
- **不适用**：需要登录的页面、强反爬网站、法律禁止采集的内容

---

*卡片类型：tool | 审核状态：待审*
