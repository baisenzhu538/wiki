---
id: concept-feishu-api-pagination-trap
title: 飞书API分页陷阱——静默截断比报错更危险
type: concept
status: enriched
author: 段王爷（南帝）
reviewed_by: 欧阳锋
review_date: 2026-06-23
created_at: 2026-06-23
confidence: 0.95
trust_level: high
language: zh-CN
domain:
- feishu
- content-extraction
- publishing
- yitang
source_refs:
- src_unknown
- src_unknown
related:
- '[[yitang-domain-digest]]'
- '[[knowledge-delivery-os-快速体验指南-飞书云文档]]'
- '[[tool-yitang-web-scraping-research]]'
- '[[dk-yitang-model-asset-capitalization]]'
- '[[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]]'
diagnostic_signals:
- framework_lens: API分页遗漏——fetch_children没有has_more循环
  follow_up_question: 你的提取脚本在调用/blocks API后，检查了resp['data']['has_more']吗？
updated_at: '2026-06-28'
---

# 飞书API分页陷阱

> **一句话：API返回code=0不代表数据完整。page_size=500是硬上限，不处理has_more=内容静默截断。**

## 为什么静默截断比报错更危险

```
正常报错：code≠0 → 操作者立即知道出问题 → 排查修复
静默截断：code=0 → 操作者以为成功了 → 用户发现内容少一半 → 信任受损
```

## 事故规模

拆书会第208期：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 根因

```python
# ❌ 旧代码
def fetch_children(parent_id):
    url = f'.../children?page_size=500'
    resp = ...urlopen(req).read()
    return resp['data']['items']  # 拿一页就停

# ✅ 修复后
def fetch_children(parent_id):
    items = []
    page_token = ''
    while True:  # ← 关键：循环到底
        url = f'.../children?page_size=500'
        if page_token: url += f'&page_token={page_token}'
        resp = ...urlopen(req).read()
        items.extend(resp['data']['items'])
        if not resp['data'].get('has_more'):
            break
        page_token = resp['data'].get('page_token')
    return items
```

## 适用边界

不仅是 Docx API。飞书 Bitable API、Wiki API 等所有带 `page_size` 参数的分页接口，都存在同样的静默截断风险。
