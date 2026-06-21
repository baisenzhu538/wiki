---
id: tool-alt-data-free
title: 免费替代数据：小团队的Hedge Fund武器
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- web: Alternative data sources accessible to individuals
- web: Google Trends, Reddit, Glassdoor, App Store APIs
related:
- "[[tool-alt-data-overview]]"
- "[[tool-yitang-database-index]]"
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

- **适用**：小团队/个人创业者的日常调研需求
- **不适用**：需要高精度数据的投资决策（免费数据的误差不可忽略）
- **成本**：全部免费

---

*卡片类型：tool | 审核状态：待审*
