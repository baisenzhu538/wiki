---

id: tool-agent-research-pipeline
title: Pipeline模式：OSCAR五步法的Agent实现
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, research, ai-collaboration]
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

# Pipeline模式

> OSCAR五步法的Agent原生实现：O(搜索)→S(筛选)→C(提取)→A(分析)→R(报告)，每步一个Agent，串行流水线。步骤依赖明确的调研任务最适合Pipeline。

## OSCAR → Pipeline映射

| OSCAR步骤 | Pipeline Agent | 输入 | 输出 | 验收标准 |
|:---|:---|:---|:---|:---|
| **O** 搜索 | Search Agent | KIQ列表 | 原始信息集合 | 每个KIQ至少5条来源 |
| **S** 筛选 | Filter Agent | 原始信息 | 去重+排序后的信息 | 剔除重复率<5% |
| **C** 提取 | Extract Agent | 筛选后信息 | 结构化数据表 | Schema完整率>95% |
| **A** 分析 | Analysis Agent | 结构化数据 | 洞察+建议 | 每条洞察有数据支撑 |
| **R** 报告 | Report Agent | 分析结果 | 最终报告 | 决策者可据此行动 |

## Agent执行指令

```python
# LangChain Pipeline模式示例
from langchain import SequentialChain

pipeline = SequentialChain([
    SearchAgent(kiqs=["KIQ1", "KIQ2", "KIQ3"]),
    FilterAgent(dedup=True, min_relevance=0.7),
    ExtractAgent(schema=report_schema),
    AnalysisAgent(framework="OSCAR"),
    ReportAgent(template="research_report")
])
result = pipeline.run()
```

## 与人工OSCAR的差异

| 维度 | 人工 | Pipeline Agent |
|:---|:---|:---|
| 速度 | 2-3天 | 数小时（24h可运行） |
| 验收标准 | 人判断"够了" | 需要量化标准（如"每个KIQ≥5个来源"） |
| 灵活性 | 高（中间发现可以随时转向） | 低（Pipeline结构固定） |

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 单步失败全链崩溃 | Step 2出错，Step 3-5全停 | 每步加timeout+fallback |
| 中间结果格式不兼容 | Step 3输出的JSON Step 4读不了 | 用固定Schema+验证 |
| 累积误差 | Step 2的筛选偏差在Step 4被放大 | 关键中间结果人工抽查 |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
