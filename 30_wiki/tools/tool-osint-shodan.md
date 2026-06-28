---

id: tool-osint-shodan
title: Shodan：互联网设备搜索引擎——发现竞对的技术栈
type: tool
status: enriched
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
source_refs:
- src_unknown
- src_unknown
related:
  - [[yitang-domain-digest]]
  - [[yitang-research-domain-digest]]
  - [[pending_unknown]]
  - [[pending_unknown]]
  - [[pending_unknown]]
---

# Shodan：互联网设备搜索引擎

> Shodan不是搜网页，是搜互联网上所有联网设备——服务器、摄像头、数据库、工控系统。输入竞对域名，看他们暴露了什么技术基础设施。

## 核心能力

| 搜索什么 | 能发现什么 |
|:---|:---|
| `org:"Company Name"` | 竞对使用了哪些云服务、托管在哪些IP段 |
| `hostname:target.com` | 竞对的子域名和开放端口 |
| `product:nginx` | 竞对是否使用特定技术 |
| `ssl:"target.com"` | SSL证书详情——证书里的组织名不会说谎 |
| 端口扫描 | 哪些服务对外开放（数据库直接暴露=重大安全信号） |

## Agent执行指令

```bash
# Shodan CLI安装
pip install shodan
shodan init YOUR_API_KEY

# 搜索竞对
shodan search "org:'Company Name'" --fields ip,port,org,hostnames

# 搜索竞对域名
shodan domain target.com

# 通过API（Agent更友好）
curl "https://api.shodan.io/shodan/host/1.2.3.4?key=YOUR_KEY"
```

## 实战场景

**场景**：判断竞对的技术投入
- src_unknown
- src_unknown
- src_unknown

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 过度解读 | 看到一个开放端口就推断技术栈 | 多指标综合判断，单信号不足以定论 |
| 信息过时 | Shodan快照可能是几个月前的 | 用 `shodan host --history` 查看历史变化 |
| 法律风险 | 直接访问竞对设备可能违法 | Shodan是搜索索引，不是入侵工具——只看不动 |

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
