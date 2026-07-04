---
id: tool-agent-firecrawl
title: Firecrawl：专为LLM设计的Web抓取API
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
- yitang
- research
- ai-collaboration
source_refs:
- src_unknown
- src_unknown
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[ai-collaboration-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- web-scraping-三剑客-scrapling-crawl4ai-firecrawl
- agent-native-card-design
updated_at: '2026-06-29'
---
# Firecrawl

> 输入一个URL，输出干净Markdown。专为LLM/RAG设计——Agent不需要"看网页"，直接拿到结构化内容。

## 核心能力

| 功能 | 说明 |
|:---|:---|
| **单页抓取** | URL → Markdown（含标题/列表/表格） |
| **递归爬取** | 从一个URL出发，自动跟随链接爬取整站 |
| **Schema化提取** | 指定JSON Schema，自动从页面提取结构化字段 |
| **搜索引擎抓取** | 抓取Google搜索结果 |
| **MCP支持** | 支持Model Context Protocol，Agent原生调用 |

## Agent执行指令

```bash
# 单页抓取
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIRECRAWL_KEY" \
  -d '{"url": "https://target.com/pricing", "formats": ["markdown"]}'

# 递归爬取整站（限同域名）
curl -X POST https://api.firecrawl.dev/v1/crawl \
  -H "Authorization: Bearer $FIRECRAWL_KEY" \
  -d '{"url": "https://target.com", "maxPages": 50}'

# Schema化提取
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H "Authorization: Bearer $FIRECRAWL_KEY" \
  -d '{"url": "https://target.com/team", "formats": ["extract"], "extract": {"schema": {"type": "object", "properties": {"employees": {"type": "array", "items": {"type": "object", "properties": {"name": {"type": "string"}, "title": {"type": "string"}}}}}}}'
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 反爬封锁 | 某些网站返回403 | 用Browser模式(需付费)；换Crawl4AI作为备选 |
| JS渲染不完整 | 动态内容未加载 | 等待时间设置过短，增加waitFor参数 |
| 递归爬取超限 | 爬到第10页就停了 | maxPages设置过低，但注意成本 |

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设"URL → Markdown 的转换是无损的"，但网页中的交互元素（折叠面板、Tab 切换、懒加载内容）在静态抓取时会丢失——Markdown 输出的完整性取决于页面的渲染模式，这是其适用**边界**。
- **反例**：需要登录才能查看的内容（如 LinkedIn 个人资料、付费墙后的文章），Firecrawl 无法获取——此时"干净 Markdown"只是公开部分的子集。

**Roy Fielding**（Apache HTTP Server 联合创始人，REST 架构风格作者）会质疑：Firecrawl 将网页转为 Markdown 喂给 LLM，但 REST 的核心理念是"超媒体作为应用状态的引擎"（HATEOAS）——剥离超链接后的 Markdown 丢失了状态转移信息，AI 可能做出错误的上下文推断。
