---
id: tool-osint-spiderfoot
title: SpiderFoot：一键自动化OSINT扫描
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.90
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- web: SpiderFoot GitHub (smicallef/spiderfoot)
- web: OSINT tools comparison 2026
related:
- "[[tool-osint-overview]]"
---

# SpiderFoot：自动化OSINT扫描

> 开源、免费、一键式。输入目标（域名/IP/邮箱/姓名），SpiderFoot自动跑200+数据源扫描——情报界的"全自动侦察兵"。

## 核心能力

- **200+模块**：涵盖DNS、SSL、WHOIS、社交媒体验证、数据泄露查询、暗网搜索
- **被动扫描**：不直接与目标交互，无法被检测
- **可视化输出**：自动生成关联图和时间线
- **API支持**：可以被Agent通过API调用

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

- **适用**：快速摸底陌生公司、安全评估、数字足迹审计
- **不适用**：需要实时数据的场景（SpiderFoot做的是快照扫描）
- **成本**：完全免费开源

---

*卡片类型：tool | 审核状态：待审*
