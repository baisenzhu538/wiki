---

id: tool-google-dorking
title: Google Dorking：高级搜索语法——挖出搜索引擎的隐藏信息
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.90
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- web: Google advanced search operators
- web: OSINT search techniques
related:
  - '[[tool-doris-industry-report-search-tips]]'
  - '[[tool-osint-spiderfoot]]'
  - '[[tool-dns-intelligence]]'
  - '[[tool-osint-wayback]]'
  - '[[tool-yitang-industry-report-search]]'
- "[[tool-yitang-weapon-media-search]]"
- "[[tool-doris-industry-report-search-tips]]"
---

# Google Dorking：高级搜索语法

> 零成本、零门槛、最高ROI。Google的高级搜索操作符能挖出普通搜索永远找不到的信息——竞对的内部文档、暴露的配置文件、忘记设权限的敏感页面。

## 核心操作符

| 语法 | 作用 | 示例 |
|:---|:---|:---|
| `site:` | 限定网站 | `site:target.com confidential` |
| `filetype:` | 限定文件类型 | `filetype:pdf site:target.com` |
| `intitle:` | 限定标题 | `intitle:"salary" site:target.com` |
| `inurl:` | 限定URL路径 | `inurl:admin site:target.com` |
| `-` | 排除关键词 | `"company name" -press -official` |
| `before:` | 限定日期前 | `before:2025-01-01 target.com news` |
| `after:` | 限定日期后 | `after:2024-06-01 target.com` |
| `""` | 精确匹配 | `"internal use only" site:target.com` |
| `*` | 通配符 | `"CEO * announced" site:target.com` |

## 实战组合

| 目的 | 搜索语句 |
|:---|:---|
| 找竞对内部文档 | `site:target.com filetype:pdf OR filetype:doc OR filetype:xlsx -press` |
| 找竞对员工信息 | `site:linkedin.com/in/ "Company Name" "Product Manager"` |
| 找竞对的测试环境 | `site:target.com inurl:staging OR inurl:test OR inurl:dev` |
| 找竞对的招标信息 | `site:target.com intitle:"RFP" OR intitle:"招标"` |
| 找曝光的价格表 | `site:target.com filetype:pdf intitle:price OR intitle:报价` |

## Agent执行指令

```bash
# 通过Google搜索API (需要API key)
curl "https://www.googleapis.com/customsearch/v1?key=KEY&cx=CX&q=site:target.com+filetype:pdf"

# 或通过Python
from googlesearch import search
results = search("site:target.com filetype:pdf", num_results=20)
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 关键词太宽 | 返回几万条结果 | 逐步加限定条件缩小范围 |
| 关键词太窄 | 零结果 | 去掉一层限定，放宽条件 |
| 误判"内部文档" | 抓到了只是公开的旧版PDF | 打开确认内容是否真的有价值 |

## 适用边界

- **适用**：所有有网站的公司、零成本快速摸底
- **不适用**：搜索被robots.txt屏蔽的内容
- **成本**：完全免费

---

*卡片类型：tool | 审核状态：待审*
