---
id: tool-osint-shodan
title: Shodan：互联网设备搜索引擎——发现竞对的技术栈
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
source_refs:
- src_unknown
- src_unknown
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- tinyfish-agentic-web-infrastructure
updated_at: '2026-06-29'
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

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设网络扫描数据能反映目标基础设施的真实状态，但越来越多的企业使用云服务和CDN隐藏了真实IP——扫描结果可能只是代理层而非真实基础设施。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Ross Anderson**（剑桥大学安全工程教授）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
