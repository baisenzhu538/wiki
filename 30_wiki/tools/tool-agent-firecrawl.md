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
  - [[yitang-domain-digest]]
  - [[yitang-research-domain-digest]]
  - [[ai-collaboration-domain-digest]]
  - [[pending_unknown]]
  - [[pending_unknown]]
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
