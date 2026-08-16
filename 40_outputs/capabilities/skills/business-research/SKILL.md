---
name: business-research
version: "2.2.0-kdo"
allowed-tools:
  - Bash
  - Read
  - Write
description: |
  商业调研方法论（OSCAR + 13武器体系）：将模糊的商业问题转化为可决策的情报报告。
  触发词：商业调研、竞品调研、竞品分析、行业调研、尽职调查、尽调、
  调研这个公司/行业/市场、做个竞品分析、竞争对手分析、
  这个赛道怎么样、项目靠谱吗、加盟调研、投资调研、摸底、情报收集。
  区分规则：有明确的「商业主体」（公司/品牌/产品/市场）→ 本 Skill；
  纯技术/概念/学术调研 → deep-research。
status: published
owner: huangyaoshi
---

# Business Research（商业调研 OSCAR 武器库）

将用户提出的商业问题，通过 OSCAR 方法论 + 13 武器体系，转化为可指导决策的情报报告。

## 运行环境

本 Skill 已适配 KDO/Hermes 运行环境。

| Claude Code 工具 | KDO 等效命令 |
|:---|:---|
| `WebSearch(query)` | `python kdo-tools/web_search.py "query" --json` |
| `WebFetch(url)` | `python kdo-tools/web_fetch.py "url" --json` |
| `Agent(prompt)` | Bash 子进程或直接调用 |

> 工具位置：`C:\Users\Administrator\Desktop\wiki\kdo-tools\web_search.py`、`web_fetch.py`

## Constraints

<hard_limits>
- 严禁捏造信源：每条事实必须附可验证的 URL 或"来源名称+日期"，无来源者标为 ❓
- 核心结论必须有 ≥2 个独立 L1/L2 来源交叉验证，否则降级标注 ⚠️
- Step 0 用户确认意图前，禁止任何搜索或分析动作
- Step 14 报告生成前必须通过 Step 13 综合质量门（BLOCKING）

## 13 武器速查

| # | 武器 | 用途 | 搜索示例 |
|:--|:---|:---|:---|
| 1 | 搜索引擎 | 全网信息搜集 | `python kdo-tools/web_search.py "query" --json` |
| 2 | 行业报告 | 市场规模/趋势/格局 | `python kdo-tools/web_search.py "行业名 市场报告 2026 PDF" --json` |
| 3 | 财报分析 | 上市公司财务数据 | `python kdo-tools/web_search.py "公司名 investor relations annual report" --json` |
| 4 | 媒体验证 | 新闻报道交叉验证 | 多源搜索同一事件 |
| 5 | OSINT | 公开情报搜集 | domain/whois/备案查询 |
| 6 | 专家访谈 | 行业专家观点收集 | `python kdo-tools/web_search.py "专家名 观点 行业" --json` |
| 7 | CI 框架 | 竞争情报系统化 | 见 `references/ci-platforms.md` |
| 8 | 另类数据 | 招聘/专利/供应链 | 见 `references/research-principles.md` |
| 9 | Google Dorking | 精确搜索技术 | 见 `references/databases-index.md` |
| 10 | 跨验证 | 多源交叉验证 | SATs 方法论 |
| 11 | 多 Agent | 分布式并行调研 | 多进程调用 web_search |
| 12 | Web Scraping | 结构化抓取 | `python kdo-tools/web_fetch.py "url" --text` |
| 13 | 质量门 | 最终质量控制 | 见 Step 13 |

## 执行流程

### Step 0：确认调研目标（必须）

先向用户确认：
1. 调研对象（公司/品牌/产品/市场/赛道）
2. 调研目的（投资决策/竞品对标/市场进入/加盟评估/可行性判断）
3. 时间范围（近期/过去 5 年/不限）
4. 可接受的信源等级（L1 一手 / L2 权威二手 / L3 综合）

用户确认前禁止搜索。

### Step 1-4：搜索与收集

```
python kdo-tools/web_search.py "query" --json  > result.json
python kdo-tools/web_fetch.py "url" --json      > page.json
```

每个武器执行后记录：（来源 URL / 日期 / 可信度 / 关键发现）

### Step 13：质量门

| 检查项 | 标准 |
|:---|:---|
| 核心结论交叉验证 | ≥2 个 L1/L2 来源 |
| 信源可追溯 | 每条事实可追溯 |
| 无捏造 | 无 AI 幻觉 |

## References

- `references/weapon-action-templates.md` — 13 武器操作模板
- `references/research-principles.md` — 调研方法论原则
- `references/ci-platforms.md` — CI 竞争情报平台
- `references/databases-index.md` — 数据库索引
- `references/report-guide.md` — 报告撰写指南
- `references/bias-checklist.md` — 偏见速查
- `references/market-sizing.md` — 市场规模估算
- `references/style-guide.md` — 写作风格指南
