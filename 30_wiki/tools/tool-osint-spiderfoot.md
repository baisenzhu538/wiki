---
id: tool-osint-spiderfoot
title: SpiderFoot：一键自动化OSINT扫描
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
  - SpiderFoot：一键自动化OSINT扫描
  - 一键自动化
  - 一键自动化OSINT扫描
  - 自动化
source_refs:
- src_unknown
- src_unknown
related:
- '[[yitang-domain-digest]]'
- '[[yitang-research-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- agent-native-card-design
- tinyfish-agentic-web-infrastructure
updated_at: '2026-06-29'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---
# SpiderFoot：自动化OSINT扫描

> 开源、免费、一键式。输入目标（域名/IP/邮箱/姓名），SpiderFoot自动跑200+数据源扫描——情报界的"全自动侦察兵"。

## 核心能力

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Agent执行指令

```bash
# Docker一键启动（推荐）
docker run -d -p 5001:5001 --name spiderfoot spiderfoot/spiderfoot
# 浏览器访问 http://localhost:5001

# CLI模式（Agent友好）
python sf.py -s target.com -m all -o csv > report.csv

# 只跑特定模块（更快）
python sf.py -s target.com -m sfp_email,sfp_dns,sfp_names -q

# API模式
curl "http://localhost:5001/startscan?target=target.com&modules=sfp_email,sfp_dns"
```

## 实战场景

**场景**：快速摸底一家陌生公司
1. 输入域名 → 收集所有子域名、邮箱地址、员工姓名
2. 通过邮箱 → 在Have I Been Pwned查是否泄露
3. 通过IP → 查托管了哪些服务、使用什么技术栈
4. 输出：一份完整的公司数字足迹报告

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 扫描过慢 | 全模块扫描可能跑几小时 | 根据目标选择相关模块，不跑-all |
| 误报 | 某些模块返回不相关的结果 | 人工确认关键发现后再写入报告 |
| 版本过时 | 某些API Key过期或模块失效 | 每次用前 `git pull`，定期更新 |

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

- **具体假设**：该工具假设公开情报源能揭示目标的全貌，但公开数据只占目标信息的一小部分——真正的敏感信息不会出现在公开渠道中。在隐私法规收紧的趋势下，公开数据的覆盖面在持续缩小。
- **边界**：在全新领域或快速变化的环境中，已有数据和经验可能完全失效——工具的有效性高度依赖场景的稳定性。
- **前提**：该工具的前提是使用者能正确理解和执行工具的规则，但执行者的认知偏差和经验限制会影响工具的实际效果。

**Bruce Schneier**（安全技术专家）会质疑：工具的价值不在于"有没有"，而在于"用得好不好"。任何工具都是"能力放大器"——如果使用者的判断力不足，工具只会放大错误。真正的风险不是"缺少工具"，而是"有了工具后产生的虚假安全感"——让你以为自己已经覆盖了所有可能性，实际上只是走完了流程。
