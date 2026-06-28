---

id: tool-alt-data-overview
title: 替代数据总览：Hedge Fund级别的调研武器
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
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

# 替代数据总览

> 对冲基金每年花28亿美元购买替代数据。这些数据源远超传统调研——卫星图像、信用卡交易、App使用数据、海关提单——但它们也分"免费可用"和"年费百万"。

## 替代数据三级分类（按ROI）

### 🟢 免费层（个人/小团队可用）

| 数据源 | 能做什么 | 例子 |
|:---|:---|:---|
| Google Trends | 搜索需求趋势对比 | 品牌A vs 品牌B搜索热度 |
| Reddit/社媒分析 | 用户真实讨论 | 某品类被提及的频率和情感 |
| Glassdoor/看准网 | 员工评价和薪资 | 竞对的工作氛围、薪资水平 |
| 公开财报脚注 | 被隐藏的财务细节 | 用NLP提取脚注里的异常数据 |
| App Store评论 | 产品反馈和竞品对比 | 按时间排序看评价趋势变化 |

### 🟡 中成本层（年费数千到数万美元）

| 数据源 | 能做什么 | 代表供应商 |
|:---|:---|:---|
| Sensor Tower / data.ai | App下载量、收入、DAU估算 | $10K-$50K/年 |
| SimilarWeb | 网站流量来源和用户行为 | 免费基础版+付费 |
| Panjiva / ImportGenius | 海关进出口提单 | 按查询/订阅付费 |
| Second Measure | 信用卡交易数据（脱敏） | $10K+/年 |

### 🔴 高成本层（年费十万到百万美元，仅对冲基金级别）

| 数据源 | 能做什么 | 年费区间 |
|:---|:---|:---|
| Planet Labs卫星图像 | 追踪零售客流、工厂开工率、建筑进度 | $100K+ |
| 实时信用卡交易数据 | 竞对的真实每日销售额 | $100K-$500K |
| SafeGraph地理位置 | 消费者线下行为轨迹 | $50K+ |
| 供应链实时追踪 | 海运/AIS船舶位置追踪 | $20K-$100K |

## ROI判断原则

1. **先问：这个数据能直接回答我的决策问题吗？** 不能=别买
2. **先穷尽免费层**：Google Trends + Reddit + Glassdoor 能回答80%的问题
3. **中成本层的ROI评估**：如果调研的决策价值>$50K，$10K的数据投入合理
4. **高成本层**：小团队别碰——这些数据的价值来自"别人没有"，但维护成本极高

## Agent执行指令

```bash
# Google Trends (非官方API, 需要pytrends)
pip install pytrends
python -c "
from pytrends.request import TrendReq
pytrends = TrendReq()
pytrends.build_payload(['brand_a', 'brand_b'], timeframe='today 12-m')
print(pytrends.interest_over_time())
"

# Reddit分析 (通过.json API)
curl "https://www.reddit.com/r/SUBREDDIT/search.json?q=COMPANY_NAME&sort=new&restrict_sr=on"
```

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
