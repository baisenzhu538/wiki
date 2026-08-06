---

id: tool-osint-overview
title: OSINT工具总览：情报界的调研武器库
type: tool
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.9
trust_level: high
language: zh-CN
domain:
- yitang
- research
aliases:
  - OSINT工具总览
  - OSINT工具总览：情报界的调研武器库
  - 工具总览
  - 情报界的调研武器库
  - 界的调研武器库
source_refs:
- src_unknown
- src_unknown
discoverable_by:
  - OSINT工具总览：情报界的调研武器库
  - OSINT工具总览
  - 情报界的调研武器库
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- tool-yitang-research-exhaust-means
- framework-doris-industry-report-4step
updated_at: '2026-06-29'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---
# OSINT工具总览

> OSINT（Open Source Intelligence）是情报界积累了几十年的开源情报方法论和工具链。一堂武器库以人工执行为主，OSINT补充了自动化扫描、实体关联、网络发现等能力。

## 核心原则

1. **先搜索再问人**：OSINT第一原则——能用公开数据回答的，不要打扰任何人
2. **用工具放大带宽**：人手动搜能看10个页面，SpiderFoot一次跑200+数据源
3. **交叉验证是铁律**：OSINT信息需2+独立来源确认

## 核心工具速览

| 工具 | 一句话 | 免费 | Agent友好度 |
|:---|:---|:---:|:---:|
| Maltego | 实体关系图谱——输入一个名，画出关联网 | 付费 | ⭐⭐⭐ |
| SpiderFoot | 一键扫描200+数据源 | 开源 | ⭐⭐⭐⭐⭐ |
| theHarvester | 被动收集邮箱/域名/子域名 | 开源 | ⭐⭐⭐⭐⭐ |
| Shodan | 搜索全球联网设备 | 免费+付费 | ⭐⭐⭐⭐ |
| Sherlock | 用户名跨300+平台搜索 | 开源 | ⭐⭐⭐⭐⭐ |
| Wayback Machine | 查看网站历史版本 | 免费 | ⭐⭐⭐⭐ |

## Agent执行指令

```bash
# SpiderFoot - 全自动OSINT扫描
docker run -p 5001:5001 spiderfoot/spiderfoot
# 访问 http://localhost:5001 开始扫描

# theHarvester - 被动邮箱/域名收集
theHarvester -d target.com -b all -f report.html

# Sherlock - 用户名搜索
sherlock username --output results/

# Wayback Machine - 查看历史快照
curl "https://archive.org/wayback/available?url=target.com"
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 信息过载 | 一次扫描返回几千条无法消化 | 先明确目标再选择工具，不要全扫 |
| 工具链断裂 | 某工具不再维护/API变了 | 定期检查工具更新；备用方案 |
| 数据不交叉验证 | 单一工具的结果直接采信 | 关键信息至少2个独立工具确认 |

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

- **具体假设**：该工具假设公开情报源能揭示目标的全貌，但公开数据只占目标信息的一小部分——真正的敏感信息不会出现在公开渠道中。在隐私法规收紧的趋势下，公开数据的覆盖面在持续缩小。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Bruce Schneier**（安全技术专家）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
