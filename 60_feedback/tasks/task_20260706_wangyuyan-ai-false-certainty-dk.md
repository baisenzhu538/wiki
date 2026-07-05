---
id: task_20260706_wangyuyan-ai-false-certainty-dk
type: task
status: reviewed
assignee: claude
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-06
updated_at: '2026-07-05T17:22:20.841364+00:00'
source_refs:
- 对话记录：2026-07-05 老朱 Codex Claude Windows 10 案例
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt L950-957
related:
- '[[dk-ai-collaboration-degradation-spiral]]'
- '[[concept-yihang-dual-triangle-core]]'
reviewed_by: 欧阳锋
review_date: '2026-07-05'
---

# 任务 #115：AI 错误笃定模式 dk 卡

## 来源

老朱实战：Claude 多轮调试后斩钉截铁说"Windows 10 系统无解"。老朱没放弃——追问逻辑依据→让 AI 全网调研→喂一堂调研方法论→最终解决。

Truman 在口述稿 L950-957 讲了同样的模式："AI 内部特别随性，对外就特别笃定——他要是说我不知道这个置信区间是多少，反而你还能理性一点。"

## 核心内容

- AI 的"放弃模式"：遇到限制→给出笃定的错误结论→不会告诉你"其实可能有其他路径"
- 根因：AI 被设计用来回答问题，没有被设计用来"意识到自己不知道"
- 对抗方法：不接"无解"的答案→追问逻辑→让 AI 调研→用方法论改变 AI 的搜索路径
- 信号识别：AI 说"这个搞不好""这个问题无解""这是系统限制"→立刻启动质疑


## 执行报告

pre-submit PASS。dk-yihang-ai-false-certainty 含老朱案例+Truman口述稿引用+对抗流程。
