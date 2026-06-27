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
- src_unknown
- src_unknown
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
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
