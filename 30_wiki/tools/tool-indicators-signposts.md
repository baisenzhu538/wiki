---

id: tool-indicators-signposts
title: Indicators & Signposts：设置"重新评估"的触发信号
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- src_unknown
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---

# Indicators & Signposts

> 不要等事情发生了才反应过来。对每个关键假设设置"重新评估"的触发信号——什么信号出现时你必须重新思考？

## 方法

### Step 1：列出你的关键假设

从Key Assumptions Check中提取RED和YELLOW假设。

### Step 2：为每个假设定义Signposts

| 假设 | 触发重新评估的信号 |
|:---|:---|
| "企业客户会为Skill付费" | 3个月内<5家企业主动询价 |
| "竞对不会在12个月内进入" | 竞对注册相关商标/域名 OR 招聘相关岗位 |
| "我们的成本优势可以维持" | 供应商涨价>10% OR 竞对找到替代供应商 |

### Step 3：区分Leading vs Lagging Indicators

| 类型 | 特点 | 例子 |
|:---|:---|:---|
| **Leading**（先行指标） | 变化早于结果，给你反应时间 | 竞对招聘JD变化、新商标注册、融资新闻 |
| **Lagging**（滞后指标） | 结果已经发生，只能确认 | 季度财报、市场份额报告 |

**原则**：Leading indicators才是你的"预警系统"。Lagging indicators只能告诉你"已经输了"。

### Step 4：设定监控和告警

- src_unknown
- src_unknown
- src_unknown

## Agent执行指令

```python
# Agent监控Signposts方案
signposts = {
    "假设1_企业付费": {
        "signal": "企业客户主动询价<3家",
        "check": "每两周统计一次inbound",
        "alert_threshold": "连续2个周期<3家 → 升级告警"
    },
    "假设2_竞对不进入": {
        "signal": "竞对注册相关商标",
        "check": "crt.sh监控SSL证书 + Google Alerts",
        "alert_threshold": "任何匹配 → 立即告警"
    }
}

# Cron: 每周一运行signpost检查
# 0 9 * * 1 python check_signposts.py
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 信号太多 | 每周收到20条告警，麻木了 | 只设置3-5个最关键signposts |
| 只设lagging | 等财报出来才知道竞对超了我们 | 强制每个假设至少1个leading indicator |
| 信号出现不行动 | 告警发了但没人处理 | 每个告警绑定负责人+行动清单 |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
