---

id: tool-dns-intelligence
title: DNS情报：从域名和网络基础设施反推竞对动态
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- web: DNSDumpster, crt.sh, whois.domaintools.com
- web: OSINT DNS analysis techniques
related:
  - '[[tool-agent-firecrawl]]'
  - '[[tool-osint-spiderfoot]]'
  - '[[tool-agent-native-overview]]'
  - '[[tool-osint-wayback]]'
  - '[[tool-google-dorking]]'
  - "[[tool-osint-overview]]"
  - "[[tool-osint-shodan]]"
---

# DNS情报

> 竞对的域名、DNS记录、SSL证书——这些"基础设施"层面的信息不会说谎。新域名=新项目，新SSL证书=新产品。

## 三大免费工具

| 工具 | 能看什么 | URL |
|:---|:---|:---|
| **DNSDumpster** | DNS记录图谱——子域名、邮件服务器、NS记录 | dnsdumpster.com |
| **crt.sh** | SSL证书透明度日志——什么时候申请了新证书 | crt.sh |
| **WHOIS查询** | 域名注册人、注册时间、变更历史 | whois.domaintools.com |

## 实战信号

| 信号 | 含义 |
|:---|:---|
| 新注册域名 | 可能的新品牌/新产品/独立项目 |
| 域名whois变更 | 公司所有权变更/品牌转让 |
| 新增SSL证书 | 新服务上线（证书里的域名=服务名） |
| 子域名增加 | 业务规模化（每个子域可能对应一个服务） |
| 更换DNS服务商 | 技术栈迁移（如迁移到Cloudflare=安全意识提升） |

## Agent执行指令

```bash
# crt.sh API - 查竞对的SSL证书历史
curl "https://crt.sh/?q=%.target.com&output=json" | jq '.[].common_name'

# DNSDumpster (需要手动交互，不适合全自动)
# 或用 dig 命令查询DNS记录
dig target.com ANY
dig target.com MX     # 邮件服务
dig target.com NS     # DNS服务商
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 过度解读 | 注册了域名并不等于在做这个项目 | 很多公司注册防御性域名（.net/.org等），不代表在开发 |
| 隐私保护 | WHOIS信息被隐私保护隐藏 | 改用crt.sh看证书信息（证书必须暴露真实域名） |

## 适用边界

- **适用**：技术公司调研、发现竞对未公开的新项目
- **成本**：完全免费

---

*卡片类型：tool | 审核状态：待审*
