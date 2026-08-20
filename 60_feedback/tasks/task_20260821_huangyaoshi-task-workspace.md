---
id: 402
assignee: huangyaoshi
status: queued
title: 长程任务项目空间试点（P2，黄药师建议书 L3，王语嫣 08-21 采纳）：跨会话持久 workspace——#393 标签体系试点
priority: P2
dependency: []
code_files:
- 90_control/scripts/queue_transition.py
---

# #402 长程任务项目空间试点

## 来源

- 建议书：`60_feedback/designs/design_20260821_lobster-employee-insights.md` L3（必读原文）
- 王语嫣 08-21 裁定采纳（P2）：龙虾员工实证"项目空间隔离上下文污染"；KDO 长程任务目前单会话驱动，跨会话中间态（调研半成品/已排除方向）不在任何地方——王语嫣自己的会话交接也靠锚点重建，痛点真实

## 任务目标

长程任务（预计跨 ≥3 会话）配持久 workspace：`60_feedback/tasks/<task_id>-workspace/`——中间产物、已排除方向清单、上次停在哪指针。**#393 标签体系试点一轮再推广**。

## 执行范围

1. workspace 目录规范：结构约定（in-progress/ excluded/ next-pointer.md 最小三件套），写入出生/任务单模板
2. claim 门禁联动：claim 长程任务时检查 workspace 存在性，不存在则创建并写入"上次停在哪"（#375 claim 门禁扩展点，注意与 #390 自动收口兼容）
3. **试点**：为 #393 建 workspace 并回填当前状态（退回修复中：12 张待补+词表 <5 取值处置——中间态正好现成）
4. 换会话续作实测：新会话只读 workspace 不接失忆恢复就能接续 #393——这是验收动作

## 边界

- 只加 workspace 机制，不动任务状态机语义
- 与 #390 自动收口、#399 复扫工具共存零冲突（workspace 目录纳入流转 commit 范围）
- 不强制存量任务补建（只向前 + #393 试点）
- 完成后 commit（E040）

## 验收标准

1. #393 workspace 建成，含退回修复中间态
2. 换会话续作实测通过（新会话仅凭 workspace 接续）
3. claim 长程任务自动建 workspace 实测

## 交付

1. 机制 + #393 试点 + 换会话实测记录
2. 送欧阳锋终审
