---
name: research
description: 商业调研总入口——基于一堂OSCAR方法论+武器库，自动路由到对应子Skill
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
tools:
  search: kdo-tools/web_search.py
  adapter: kdo-tools/research_adapter.py
metadata:
  hermes:
    tags: [research, 调研, OSCAR, 尽调, 行业分析, 竞品分析]
    related_skills: [research-financial-report, research-industry-report, research-web-scraping, research-cross-validation, research-expert-interview, research-osint]
---

# 商业调研总入口

基于一堂 OSCAR 方法论 + 调研武器库，将模糊的调研问题转化为可决策的情报报告。

本 Skill 已适配 KDO 工具链：在线搜索统一走 `kdo-tools/web_search.py`，OSCAR 流程封装在 `kdo-tools/research_adapter.py` 中。

## 触发词

调研、帮我查、分析一下、尽调、做个调研、行业分析、竞品分析、这个公司怎么样、这个赛道、市场研究、对标分析

## 约束

- 严禁捏造数据：每条事实必须附可验证的来源 URL 或标注"口述待独立核实"
- 核心结论必须 ≥2 个独立来源交叉验证
- 数字/金额/市占率必须回查原始链接核验
- 信源时效：AI/监管/融资 ≤30 天；行业报告 ≤12 个月

## 执行流程

### Step 0: 意图分类

| 类型 | 路由到 | 示例 |
|:--|:--|:--|
| 上市公司/财报分析 | research-financial-report | "分析老百姓大药房的招股书" |
| 行业报告/市场研究 | research-industry-report | "药品零售市场规模和趋势" |
| 需要爬虫采集公开数据 | research-web-scraping | "爬取竞品网站的价格信息" |
| 专家访谈 | research-expert-interview | "怎么找到并访谈行业专家" |
| 多源交叉验证 | research-cross-validation | "多个数据源互相矛盾怎么办" |
| OSINT工具链 | research-osint | "用Shodan搜竞对设备" |
| 高级搜索/域名情报 | research-google-dorking | "site:filetype:WHOIS查竞对" |
| 替代数据 | research-alt-data | "Google Trends/卫星/信用卡" |
| 验证图片/视频真伪 | research-media-verification | "这张图是真的吗" |
| 结构化分析 | research-sats | "魔鬼代言人/Red Team" |
| 建立CI竞争情报系统 | research-ci-framework | "持续监控竞对" |
| 多Agent协作调研 | research-multi-agent | "复杂任务分工" |
| 调研质量自检 | research-quality-gate | "够好了吗" (Step7) |
| 综合调研 | 按顺序调用多个子 Skill | "全面分析XX行业" |

### Step 1: OSCAR 定目标
- **O**bjective（目标）：要验证什么假设？
- **S**cope（范围）：时间/地域/竞品范围？
- **C**hecklist（清单）：需要哪些具体信息？

### Step 2: 执行 → 交叉验证 → 输出

#### KDO 工具调用

1. **OSCAR 第一轮搜索**（自动按 Checklist 拆 query）：
   ```bash
   python kdo-tools/research_adapter.py oscar \
     --objective "验证某假设" \
     --scope "2024-2026, 中国" \
     --checklist "市场规模,竞品定价,渠道结构" \
     --json
   ```
2. **单点/多 query 搜索**：
   ```bash
   python kdo-tools/research_adapter.py search "query1" "query2" --json
   # 或直接调用底层搜索工具
   python kdo-tools/web_search.py "query" --json
   ```
3. **报告 P0 质量门自检**：
   ```bash
   python kdo-tools/research_adapter.py validate report.md --json
   ```

> 输出为 JSON，包含 `timestamp`、`backend`、`queries`、`results`，可直接写入 KDO 引用块或事实卡片。

## 相关 wiki 卡片
- `business-research-skill-oscar-13-weapon-system` — OSCAR + 13 武器体系总览
- `yitang-research-domain-digest` — 域索引入口
- `framework-yitang-oscar-research` — OSCAR 五步法
- `framework-yitang-six-layer-cross-validation` — 六层交叉验证
- `kdo-yaml-frontmatter-safety` — KDO 卡片引用规范
