---

id: tool-dns-intelligence
title: DNS情报：从域名和网络基础设施反推竞对动态
type: tool
status: reviewed
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
aliases:
  - DNS情报
  - DNS情报：从域名和网络基础设施反推竞对动态
  - 从域名和网络基础设施反推竞对动态
  - 名和网络基础设施反推竞对动态
source_refs:
- src_unknown
- src_unknown
discoverable_by:
  - DNS情报：从域名和网络基础设施反推竞对动态
  - 从域名和网络基础设施反推竞对动态
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- business-research-skill-oscar-13-weapon-system
updated_at: '2026-06-29'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
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

- **具体假设**：该工具假设"DNS 记录和 SSL 证书能可靠反映竞对动态"，但越来越多的企业开始使用 Cloudflare、CDN 等中间层——DNS 记录不再直接暴露企业基础设施，SSL 证书也可能是泛域名证书，无法区分具体子产品。
- **边界**：在以 App 为主的产品形态中（不依赖 Web 域名），DNS 情报几乎完全失效——竞对的新产品在 App Store 上线，但没有新域名注册。
- **前提**：该工具的前提是"竞对不会主动隐藏基础设施"，但成熟的企业会使用 WHOIS 隐私保护、代理注册、内部域名等手段——公开 DNS 数据只是冰山一角。

**Bruce Schneier**（安全技术专家，《Click Here to Kill Everybody》作者）会质疑：DNS 情报的价值在于"基础设施不会说谎"——但这个前提正在被侵蚀。现代企业的基础设施越来越不透明：CDN 隐藏了真实 IP，泛域名证书隐藏了子产品，云服务共享 IP 隐藏了业务边界。DNS 情报从"高价值情报源"退化为"低噪声信号"——它仍然有用，但需要与更多信源交叉验证才能产生可靠结论。
