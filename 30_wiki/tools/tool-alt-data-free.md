---

id: tool-alt-data-free
title: 免费替代数据：小团队的Hedge Fund武器
type: tool
status: reviewed
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
aliases:
  - Fund武器
  - 免费替代数据
  - 免费替代数据：小团队的HedgeFund武器
  - 小团队的
  - 小团队的Hedge
  - 替代数据
source_refs:
- src_unknown
- src_unknown
discoverable_by:
  - 免费替代数据：小团队的Hedge Fund武器
  - 免费替代数据
  - 小团队的Hedge
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- business-research-skill-oscar-13-weapon-system
- tool-yitang-app-store-data
updated_at: '2026-06-29'
tags:
- audience:manager
- scene:execution
- skill-level:advanced
---
# 免费替代数据

> ⚠️ 注意：免费API和网站可能随时变化或关闭。本卡信息截至2026-06，使用前验证。

## 八大免费数据源

| # | 数据源 | 能看什么 | Agent接入方式 | 时效风险 |
|:---:|:---|:---|:---|:---:|
| 1 | **Google Trends** | 搜索需求趋势、品牌对比 | pytrends库 | 🟢 稳定 |
| 2 | **Reddit .json API** | 任何subreddit/帖子的结构化数据 | URL后加 `.json` | 🟢 稳定 |
| 3 | **Glassdoor** | 员工评价、薪资、面试经验 | 需爬虫（无官方API） | 🟡 可能改版 |
| 4 | **App Store评论** | 竞对App的用户反馈 | RSS Feed `itunes.apple.com/rss` | 🟢 稳定 |
| 5 | **SEC EDGAR** | 美股上市公司完整财报 | `sec.gov/cgi-bin` API | 🟢 稳定 |
| 6 | **Google Patents** | 全球专利全文搜索 | `patents.google.com` API | 🟢 稳定 |
| 7 | **YouTube字幕** | 竞对视频的逐字内容 | `youtranscript.com` 或 Innertube API | 🟡 非官方 |
| 8 | **Wikipedia API** | 行业/公司词条全文 | `wikipedia.org/api/rest_v1` | 🟢 稳定 |

## Agent执行指令

```bash
# Reddit - 搜索竞对相关讨论
curl -H "User-Agent: ResearchBot/1.0" \
  "https://www.reddit.com/search.json?q=COMPANY_NAME&sort=new&limit=25"

# Glassdoor - 提取评分和评价（需爬虫）
# 用 Firecrawl 或 Crawl4AI 抓取 overview 页面

# SEC EDGAR - 搜竞对的财报文件
curl "https://efts.sec.gov/LATEST/search-index?q=COMPANY_NAME&dateRange=custom&startdt=2024-01-01&enddt=2026-06-01"

# YouTube 字幕
# 通过 yt-dlp 获取
yt-dlp --write-auto-sub --sub-lang en --skip-download "VIDEO_URL"
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| API突然失效 | Reddit .json被限流 | 加User-Agent头，降低频率 |
| 网站改版 | Glassdoor页面结构变了 | 检查更新爬虫选择器；备选Firecrawl |
| 数据量太大 | Reddit一次搜出几千条 | 用 `sort=new` + 限定时间范围 |
| 过于依赖免费 | 免费数据的覆盖面和精度不如付费 | 关键决策用付费源交叉验证 |

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

- **具体假设**：该工具假设"免费数据源的稳定性和准确性足以支撑决策"，但免费 API（如 Reddit .json）随时可能被限流或关闭，数据覆盖率远不如付费源——用免费数据做关键决策存在"看不见的盲区"。
- **边界**：在低风险探索阶段（如竞品初步调研），免费数据足够；但在高风险决策（如投资并购）中，免费数据的精度和时效性可能造成误导。
- **反例**：Google Trends 的数据是"相对搜索量"而非"绝对搜索量"，且经过采样和平滑处理——用它做精确趋势预测时，小众关键词的数据噪声可能被误读为"趋势变化"。

**James Scott**（耶鲁大学政治学教授，《国家的视角》作者）会质疑：免费数据源的"免费"本身就是一种幻觉。平台提供免费 API 的目的是吸引用户锁定生态——今天免费，明天收费。对数据的依赖越深，被平台"收割"的风险越大。更深层的问题是：免费数据只包含"平台想让你看到的数据"，它本身就经过了平台的筛选和过滤，你以为在用"原始数据"，实际上在用"被框架化的数据"。
