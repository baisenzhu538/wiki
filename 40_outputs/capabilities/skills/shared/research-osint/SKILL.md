---
name: research-osint
description: OSINT开源情报工具链——SpiderFoot/Maltego/Shodan/Sherlock/Wayback，老顽童2026盲区发现
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, OSINT, 开源情报, Maltego, Shodan, Sherlock, Wayback]
    related_skills: [research, research-web-scraping, research-cross-validation]
---

# OSINT 开源情报工具链

OSINT 是情报界几十年的积累。一堂武器库未覆盖的盲区，老顽童 2026 年独立调研发现。

## 触发词

OSINT、开源情报、Maltego、Shodan、Sherlock、Wayback Machine、SpiderFoot

## 约束

- 仅用于公开信息采集
- Shodan 仅查看公开暴露的信息
- 不得伪造身份绕过认证

## 工具矩阵

| 工具 | 用途 | 费用 |
|:--|:--|:--|
| **SpiderFoot** | 自动 200+ 数据源扫描 | 开源免费 |
| **theHarvester** | 被动收集邮箱/域名/员工 | 开源免费 |
| **Maltego** | 实体关系图谱 | 付费 |
| **Shodan** | 搜索全球联网设备 | 免费+付费 |
| **Sherlock** | 跨 300 平台追人 | 开源免费 |
| **Wayback Machine** | 网页历史快照 | 免费 |
| **ExifTool** | 文件元数据提取 | 开源免费 |

## 决策树

| 需求 | 工具 |
|:--|:--|
| 画关联网络 | Maltego |
| 全自动扫描 | SpiderFoot |
| 找竞对暴露的设备 | Shodan |
| 追一个人的社交账号 | Sherlock |
| 看竞对 5 年前的官网 | Wayback Machine |
| 验证图片真实性 | ExifTool |
