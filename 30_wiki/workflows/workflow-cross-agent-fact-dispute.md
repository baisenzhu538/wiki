---
id: workflow-cross-agent-fact-dispute
title: "跨 Agent 事实争议裁决协议"
type: workflow
status: reviewed
domain: kdo
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: observed
aliases:
  - 争议裁决
  - git字节验证
  - 跨Agent争议
  - 事实核查
source_refs:
  - 20_memory/operating-principles.md
  - 60_feedback/diagnosis/diag_20260804_huangyaoshi-cross-agent-fact-dispute-lessons.md
diagnostic_signals:
  - signal: '跨Agent事实争议靠谁说的有道理裁决——无git字节验证'
    severity: high
    implication: '#224王语嫣vs欧阳锋争论30分钟→git show 1秒终结'
  - signal: 'Agent凭记忆/错误核查挑战审查结论——无标准流程'
    severity: high
    implication: '王语嫣初判错误→差点误导处置方向→欧阳锋git验证才纠正'
  - signal: '争议本身有价值——暴露了核查方法论的缺口'
    severity: low
    implication: '不是因为有人错了才需要协议——是因为正确的人也会错'
related:
  - '[[dk-P42-agent-fact-check-gap]]'
  - '[[framework-kdo-self-attack]]'
  - '[[dk-E010-duplicate-key-detection]]'
  - '[[dk-P15-false-completion-report]]'
  - '[[framework-kdo-modeling-methodology]]'
  - '[[dk-c5-todo-false-positive]]'
created_at: 2026-08-04
updated_at: 2026-08-04
review_date: 2026-08-04
tags:
  - audience:ouyangfeng
  - scene:review
  - skill-level:intermediate
discoverable_by:
  - 争议裁决
  - git字节验证
  - 跨Agent争议
---
# 跨 Agent 事实争议裁决协议

> **定位**：属于 KDO 工厂流程——跨 Agent 协作的质量保障协议。当两个 Agent 对同一事实产生分歧时，以 git 字节验证为最终裁决。已写入 operating-principles.md。


## 触发条件

两个 Agent 对同一事实产生分歧。例：Agent A 说"文件 X 在某时间点已损坏"，Agent B 说"不对，是后来引入的"。

## 证据效力层级

git 字节验证 > 审查报告记录 > 时间线证据链 > Agent 记忆

## 裁决流程

1. 双方各自跑 `git show <commit>:<path>` + `yaml.safe_load`，贴出完整命令和输出
2. 不贴命令和输出的争议 = 废争议
3. 时间线证据链优先：git log → 逐时间点 git show + yaml.safe_load → 定位第一个失败时间点 → 确定引入者
4. 退出机制：Agent 不确定时说"需要第三方 git 字节验证"，不硬撑不可靠结论

## 验收标准

争议以 git 字节验证结果为准，不以"谁说的更有道理"为准。

## 失败模式

- 8/2-8/3 未 commit 期间的改动无法通过 git 验证——需额外证据（操作日志/审查报告时间线）
- 双方核查方法不同导致结论不同 → 升级至黄药师做第三方独立验证

## 使用场景

- 欧阳锋和王语嫣对同一张卡的历史状态产生分歧时
- 任何 Agent 断言"文件 X 在某时间点是 Y 状态"需要被验证时
- 审查者收到异议后，需要决定是辩论还是跑 git 验证时
- 事故归因争议——破坏是历史遗留还是新引入

## 操作步骤

1. 双方各自跑 `git show <commit>:<path>` 获取文件历史版本
2. 对获取的内容执行 `yaml.safe_load` 验证 YAML 完整性
3. 贴出完整命令和输出——不贴命令的争议 = 废争议
4. 若双方结论不一致 → 升级至黄药师做第三方独立 git 字节验证
5. 以 git 字节验证结果为最终裁决，更新审查记录

## 适用边界

- 仅适用于有 git 历史的文件（8/2 新建卡不适用——它们无法从 git 恢复）
- 争议核心是"事实"（是什么）而非"判断"（该怎么做）
- Agent 审查结论本身不依赖 git——此协议仅用于"历史状态"争议
- 若 git 历史不完整（未 commit 期间）→ 需要额外证据（操作日志/审查报告时间线）

## 为什么值钱

1. **终结"谁说的"之争**：git 字节 > Agent 记忆，1 条命令终结 30 分钟争论
2. **防止错误处置**：王语嫣异议若被采纳，熔断会被错误解除，hermes 模板 bug 不会被修复
3. **可推广**：任何涉及"历史状态"的争议统一用此协议裁决
4. **降低审查成本**：从"双方各自论证"变为"一条命令验证"，审查轮次从 N 降到 1

## 与其他知识的关联

- dk-P42-agent-fact-check-gap → 配套暗知识：Agent 为什么会错误核查
- framework-kdo-self-attack → 端到端验证 > Agent 判断
- dk-E010-duplicate-key-detection → 同为基础设施缺陷——缺验证手段
- dk-P15-false-completion-report → 同模式：Agent 断言需要独立验证

## Critique

### 内部局限
- git 字节验证只能证明"是什么"，不能证明"谁引入的"——需要时间线证据链辅助
- 需要 git 历史——未 commit 期间的改动无法验证
- 双方核查方法不同导致结论不同时仍需第三方介入

### 外部挑战
- "Agent 审查不依赖 git，依赖当前文件状态"——对，此协议仅适用于历史状态争议
- "为什么不让 Agent 自己跑 git 验证"——Agent 可以跑，但命令和输出必须可复现
