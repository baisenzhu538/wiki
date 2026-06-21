---
name: research-alt-data
description: 替代数据调研——从免费层到百万级，按预算分级推荐数据源
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [替代数据, Google Trends, Reddit, Glassdoor, alt data]
    related_skills: [research]
---

# 替代数据调研

对冲基金级替代数据——免费层（Google Trends/Reddit/Glassdoor）到百万级（卫星/信用卡），分级推荐。

## Constraints

<hard_limits>
- 替代数据通常不是"官方数据"——必须标注"口述待独立核实"或来源可靠度
- 免费数据源标注时间敏感性（API 可能变化/关闭）
- 中高成本数据源标注价格区间和适用场景
</hard_limits>

## 数据源分级

### 🟢 免费层（零成本，立刻可用）

| 数据源 | 能发现什么 | 操作 |
|:--|:--|:--|
| **Google Trends** | 搜索趋势、地域热度、相关话题 | `trends.google.com` 输入关键词 |
| **Reddit** | 用户真实讨论、痛点、竞品口碑 | `site:reddit.com "品牌名"` |
| **Glassdoor** | 员工评价、薪资、面试题 | `glassdoor.com` 搜公司 |
| **GitHub** | 技术栈、commit 活跃度、招聘信号 | `github.com/orgs/公司名` |
| **海关提单** | 进出口品类/数量/供应商 | `panjiva.com` 免费查询 |
| **SimilarWeb** | 网站流量估算（免费层有限） | `similarweb.com` |

### 🟡 中成本层（$100-1000/月）

| 数据源 | 能发现什么 | 价格 |
|:--|:--|:--|
| **Sensor Tower** | App 下载量/收入估算 | ~$79/月起 |
| **SimilarWeb Pro** | 网站流量/来源/跳出率 | ~$200/月起 |
| **LinkedIn Sales Navigator** | 公司员工数/增长/职位变动 | ~$100/月 |
| **Crunchbase Pro** | 融资/收购/投资方 | ~$99/月 |

### 🔴 高成本层（$1000+/月或定制）

| 数据源 | 能发现什么 | 适用场景 |
|:--|:--|:--|
| **卫星图像** | 工厂开工率/停车场密度/在建工程 | 制造业/零售尽调 |
| **信用卡数据面板** | 真实消费流水（脱敏聚合） | 消费品竞争分析 |
| **AppAnnie/data.ai** | 全量 App 数据 | 移动互联网尽调 |
| **Earnest Analytics** | 消费收据级数据 | 零售/餐饮尽调 |

## 决策树

| 调研目标 | 推荐数据源 | 成本 |
|:--|:--|:--|
| 竞对大概规模 | Google Trends + LinkedIn | 免费 |
| 竞对真实流量 | SimilarWeb Free + Reddit | 免费 |
| 竞对员工满意度/文化 | Glassdoor | 免费 |
| 竞对 App 收入 | Sensor Tower | $79/月 |
| 竞对真实销售额 | 信用卡数据（如 Earnest） | $1000+ |
| 工厂产能验证 | 卫星图像 | $1000+ |

## 执行流程

```
输入：调研目标 + 预算区间
  ↓
Step 1: 按分级推荐数据源
  ↓
Step 2: 免费层先跑——获取基线
  ↓
Step 3: 需要更高精度？→ 推荐中高成本方案
  ↓
Step 4: 每条数据标注来源 + 可靠度
```

## 相关 wiki 卡片
- `tool-alt-data-overview`
- `tool-alt-data-free`
- `research-industry-report` — 行业报告（互补）
