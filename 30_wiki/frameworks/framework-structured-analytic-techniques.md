---

id: framework-structured-analytic-techniques
title: SATs结构化分析技术：CIA情报分析的八类工具箱
type: framework
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
- web: Richards Heuer & Pherson, Structured Analytic Techniques for Intelligence Analysis
- web: CIA Tradecraft Primer
related:
  - '[[tool-key-assumptions-check]]'
  - '[[tool-harness-adversarial-tester]]'
  - '[[framework-ci-operating-model]]'
  - '[[tool-red-team-analysis]]'
  - '[[tool-devils-advocacy]]'
- "[[framework-yitang-nine-layer-deep-dig]]"
- "[[framework-yitang-18-strategy-cards]]"
- "[[tool-key-assumptions-check]]"
- "[[tool-devils-advocacy]]"
---

# SATs结构化分析技术

> CIA情报分析员使用结构化分析技术（SATs）对抗认知偏差，系统化地产出更可靠的判断。八类技术中，一堂武器库覆盖了3类，缺失5类。

## 八类SATs与一堂映射

| # | SATs类别 | 代表技术 | 一堂武器库覆盖 | 缺口 |
|:---:|:---|:---|:---:|:---|
| 1 | **诊断技术** | Key Assumptions Check, ACH | △ ACH=九层深挖 | Key Assumptions Check未覆盖 |
| 2 | **逆向技术** | Devil's Advocacy, Red Team | ✗ | 完全缺失 |
| 3 | **想象力技术** | Scenario Generation, What If | ✗ | 完全缺失 |
| 4 | **指标技术** | Indicators/Signposts | ✗ | 完全缺失 |
| 5 | **假设检验** | Hypothesis Testing | △ | 第1掌有假设概念但无结构化检验 |
| 6 | **因果分析** | Cause & Effect Mapping | △ | 部分交叉验证 |
| 7 | **冲突管理** | Conflict Resolution | ✗ | 完全缺失 |
| 8 | **决策支持** | Decision Matrix, Pros-Cons-Fixes | ✗ | 部分决策框架 |

## 本批次补充的4项

| 技术 | CIA定位 | Agent天然优势 |
|:---|:---|:---|
| **Key Assumptions Check** | "你信以为真的东西里，哪些其实没有证据？" | Agent自动扫描商业计划生成假设清单 |
| **Devil's Advocacy** | "如果有人必须攻击这个结论，他会说什么？" | Agent换角色Prompt就能扮演挑战者 |
| **Red Team Analysis** | "如果你是竞对CEO，你会怎么打垮我们？" | Agent模拟竞对决策逻辑 |
| **Indicators/Signposts** | "什么信号出现时你得重新评估？" | Agent自动监控信号+阈值告警 |

## Agent执行指令

```python
# SATs选择逻辑（Agent根据决策场景自动推荐技术）
def recommend_sat(decision_type, confidence_level, stakes):
    if decision_type == "strategic" and stakes == "high":
        return ["Key Assumptions Check", "Devil's Advocacy", "Red Team"]
    elif confidence_level == "low":
        return ["Indicators", "Scenario Generation"]
    else:
        return ["Key Assumptions Check"]
```

## 适用边界

- **适用**：高风险决策、需要对抗认知偏差的分析场景
- **不适用**：日常小额决策、信息充分且无争议的判断
- **来源**：CIA Tradecraft Primer + Heuer & Pherson SATs文献

---

*卡片类型：framework | 审核状态：待审*
