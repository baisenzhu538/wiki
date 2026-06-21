---
name: research-web-scraping
description: 全网爬虫调研——10大工具+合规红线，对应一堂武器库逆向数据分析板块
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [research, 爬虫, 数据采集, scraping, crawl, 公开信息]
    related_skills: [research, research-osint]
---

# 全网爬虫调研

基于 2026 年全网调研最佳实践，10 大爬虫工具矩阵 + 合规决策树。

## 触发词

爬虫、抓取、数据采集、批量获取、scraping、crawl、扒数据

## 约束

- 必须先查 robots.txt
- API 优先于爬虫
- 速率限制 ≥1 秒/请求
- 只采公开页面
- 禁止绕过付费墙

## 决策树

| 需求 | 工具 |
|:--|:--|
| 读 1 个网页 | Jina Reader (`r.jina.ai/URL`) |
| 全站爬取为 Markdown | Firecrawl `/crawl` |
| 提取特定字段 | Firecrawl `/extract "<prompt>"` |
| JS 渲染 SPA | Playwright / Crawlee |
| 反爬对抗 | Crawlee + 住宅代理 |
| 本地自建 | Crawl4AI / Extracto |
| 大规模监控 | Apify / Bright Data |

## 合规检查

- [ ] robots.txt 允许？
- [ ] 有公开 API 替代？
- [ ] 速率 ≥1 秒/请求？
- [ ] 只采公开数据？
- [ ] 报告标注来源 URL + 时间？
