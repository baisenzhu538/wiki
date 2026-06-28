---
id: tool-agent-crawl4ai
title: Crawl4AI：开源AI爬虫——自然语言描述即可提取
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
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
---

# Crawl4AI

> 开源、免费、本地部署。用自然语言描述你想提取什么——不需要写CSS选择器或XPath。网页改版不影集爬虫。

## 核心能力

| 功能 | Firecrawl对比 |
|:---|:---|
| 自然语言提取 | ✅ "提取所有产品名和价格" |
| 开源免费 | ✅ 本地部署，零成本 |
| 离线可用 | ✅ 不依赖外部API |
| 自定义程度 | ⭐⭐⭐⭐⭐ 完全可控 |
| 开箱即用 | ⭐⭐⭐ 需要一定配置 |

## Agent执行指令

```bash
# 安装
pip install crawl4ai

# Python脚本（Agent友好）
from crawl4ai import WebCrawler

crawler = WebCrawler()
result = crawler.run(
    url="https://target.com/products",
    extraction_strategy="Extract all product names with their prices",
    output_format="json"
)
print(result.extracted_content)
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| LLM幻觉 | 提取的内容不存在于页面 | 设置 `validate_extraction=True` |
| 大页面超时 | 页面太大了处理不完 | 分块处理；只提取目标区域 |
| 本地资源消耗 | 需加载LLM导致内存不足 | 使用轻量模型；限制并发数 |

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
