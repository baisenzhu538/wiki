---
id: task_20260706_wangyuyan-non-expert-judgment-dk
type: task
status: reviewed
assignee: claude
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-06
updated_at: '2026-07-05T17:18:32.777066+00:00'
source_refs:
- 对话记录：2026-07-05 老朱结构工程师案例
- 对话记录：2026-07-05 老朱代码库梳理案例
related:
- '[[dk-yitang-over-abstraction]]'
- '[[concept-yihang-dual-triangle-core]]'
reviewed_by: 欧阳锋
review_date: '2026-07-05'
---

# 任务 #114：非专家判断替代法 dk 卡

## 来源

老朱在两个非专业域（结构工程图纸识别、10年代码库梳理）的实战经验：永远不可能成为该域专家的人，如何通过 AI 集群建立可用的判断力。

## 核心方法论

```
非专家 → 多 AI 独立分析 → 交叉比对分歧 → 多轮辩经收敛 → 真机/实证最终验证
```

与 #112（多 AI 交叉比对）的区别：#112 是通用验证方法论，本卡聚焦"非专家场景"——用户自己无法判断 AI 输出质量时，如何建立替代判断体系。

## 必含内容

- 结构工程图纸案例：完全不熟悉的域，多 AI 交叉比对→找到正确图纸→和加工厂对接成功
- 代码库梳理案例：不懂代码，多 AI 分析模块功能→分歧互喂→真机部署验证
- 非专家场景的审美替代策略：≥3 个 AI 独立判断一致 + 实证验证
- 边界：只适用于"对就是对、错就是错"的严格域，不适用于开放式创意域


## 执行报告

3/3 pre-submit PASS。非专家判断/错误笃定/HR Agent 三张卡。
