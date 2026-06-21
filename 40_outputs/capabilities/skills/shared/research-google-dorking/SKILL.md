---
name: research-google-dorking
description: Google Dorking高级搜索+DNS/SSL域名情报——零成本挖出竞对隐藏信息
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [Google Dorking, 高级搜索, WHOIS, DNS, SSL, crt.sh]
    related_skills: [research]
---

# Google Dorking + DNS/SSL 域名情报

Google 9 个高级操作符 + WHOIS/DNS/SSL 证书透明度日志——零成本获取竞对隐藏信息。

## Constraints

<hard_limits>
- Google Dorking 仅用于公开信息搜索，不得结合漏洞利用
- DNS/WHOIS 查询仅查公开记录，不得对目标系统进行扫描
</hard_limits>

## Google Dorking 操作符手册

| 操作符 | 功能 | 示例 |
|:--|:--|:--|
| `site:` | 限定域名 | `site:example.com 财务报表` |
| `filetype:` | 限定文件类型 | `filetype:pdf site:example.com` |
| `intitle:` | 标题包含 | `intitle:"内部" site:example.com` |
| `inurl:` | URL 包含 | `inurl:admin site:example.com` |
| `before:` | 指定日期前 | `before:2024-01-01 site:example.com` |
| `after:` | 指定日期后 | `after:2024-06-01 产品发布` |
| `-` | 排除词 | `site:example.com -招聘` |
| `*` | 通配符 | `site:example.com "*计划"` |
| `""` | 精确匹配 | `"Q4 战略规划" site:example.com` |

## 实战组合

| 目标 | 组合 |
|:--|:--|
| 找竞对内部文档 | `site:competitor.com filetype:pdf -site:competitor.com/blog` |
| 找竞对招聘透露的技术栈 | `site:jobs.com "company name" intitle:"工程师" after:2025-01-01` |
| 找竞对供应商关系 | `site:competitor.com ""合作伙伴"" OR ""供应商""` |
| 找竞对被遗忘的页面 | `site:competitor.com inurl:old OR inurl:backup OR inurl:test` |

## DNS 情报

| 工具 | 命令 | 发现什么 |
|:--|:--|:--|
| **WHOIS** | `whois example.com` | 注册人/注册时间/DNS服务器 |
| **SSL 证书** | `crt.sh/?q=%.example.com` | 所有子域名/曾经用过的域名 |
| **DNS 记录** | `dig example.com ANY` | A/MX/TXT/NS 记录 |
| **子域名枚举** | `subfinder -d example.com` | 隐藏子域名 |

## 执行流程

```
输入：目标公司名/域名
  ↓
Step 1: SSL 证书透明度 → 发现所有子域名和曾用域名
  ↓
Step 2: 对关键子域名跑 Google Dorking 组合
  ↓
Step 3: WHOIS 查注册信息
  ↓
Step 4: 汇总发现 → 输出情报报告
```

## 相关 wiki 卡片
- `tool-google-dorking`
- `tool-dns-intelligence`
- `research-osint` — OSINT 工具链（互补）
