---
id: dk-P42-agent-fact-check-gap
title: "P-42：Agent 凭错误核查挑战审查结论——git 字节验证缺位"
type: dk
status: reviewed
domain: kdo
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: observed
aliases:
  - P-42
  - 事实争议
  - git字节验证
  - Agent记忆不可靠
source_refs:
  - 60_feedback/diagnosis/diag_20260804_huangyaoshi-cross-agent-fact-dispute-lessons.md
  - 20_memory/operating-principles.md
diagnostic_signals:
  - signal: 'Agent凭记忆断言文件历史状态——无git命令附证'
    severity: high
    implication: '王语嫣初判dk-yi-tang为历史遗留→欧阳锋git字节验证推翻→错误处置差点被采纳'
  - signal: '跨Agent事实争议无标准裁决流程——靠谁说的有道理'
    severity: high
    implication: '王语嫣vs欧阳锋各执一词→无git字节证据→争论升级'
  - signal: '审查者收到异议后倾向辩论而非验证——1秒能终结的问题争论了30分钟'
    severity: medium
    implication: '浪费审查轮次，延误处置决策'
related:
  - '[[dk-E010-duplicate-key-detection]]'
  - '[[framework-kdo-self-attack]]'
  - '[[workflow-cross-agent-fact-dispute]]'
  - '[[dk-P15-false-completion-report]]'
  - '[[framework-kdo-modeling-methodology]]'
  - '[[dk-c5-todo-false-positive]]'
created_at: 2026-08-04
updated_at: 2026-08-04
review_date: 2026-08-04
tags:
  - audience:builder
  - scene:reference
  - skill-level:advanced
discoverable_by:
  - P-42
  - 事实争议
  - git字节验证
  - Agent记忆
---
# P-42：Agent 凭错误核查挑战审查结论

> **定位**：属于 KDO 事故教训库的 P 系列——P-42 是 #224 终审分歧暴露的核查方法论缺陷。与 workflow-cross-agent-fact-dispute（争议裁决协议）配套使用。


## 原始表述

#224 终审，欧阳锋判 hermes 写入模板缺陷。王语嫣独立核查后提出异议："该卡 7/27 git 版本已损坏，是历史遗留而非 hermes 新引入"。

欧阳锋跑 git show + yaml.safe_load → 7/27 版本可解析，且该卡在 7/27 根本不存在。王语嫣的核查方法有误但结论自信且明确——几乎误导了处置方向。

## 使用场景

- 两个 Agent 对同一事实产生分歧时
- Agent 凭记忆断言"X 文件在某时间点是 Y 状态"时
- 审查者收到异议，决定是辩论还是验证时

## 操作方法

1. 任何关于文件历史状态的断言，必须附 `git show <commit>:<path>` 命令 + 完整输出
2. 跨 Agent 争议：双方各自跑 git show + yaml.safe_load，贴完整输出
3. 不贴命令和输出的争议 = 废争议
4. 不确定时说"需要第三方 git 字节验证"，不硬撑

## 适用边界

- 仅适用于有 git 历史的文件（8/2 新建卡不适用）
- 争议核心是"事实"（是什么）而非"判断"（该怎么做）

## 为什么值钱

1. 终结"谁说的"之争——git 字节 > Agent 记忆，1 条命令终结 30 分钟争论
2. 防止错误处置——王语嫣异议若被采纳，熔断会被错误解除
3. 可推广——任何涉及"历史状态"的争议，统一用 git 字节验证裁决

## 与其他知识的关联

- dk-E010-duplicate-key-detection → 同源：都是 Agent 断言需要独立验证
- workflow-cross-agent-fact-dispute → 配套：争议裁决的标准协议
- P-15（声称完成但实际未做）→ 同模式：Agent 的断言需要独立验证
- #224 终审分歧 → 直接来源
- framework-kdo-modeling-methodology → 牌 #14（先跑脚本确认再下结论）= 同构

## Critique

### 内部局限
- git 字节验证只能证明"文件在某时间点是什么"，不能证明"谁引入的修改"
- 需要 git 历史——8/2-8/3 未 commit 无法验证

### 外部挑战
- "Agent 审查不依赖 git"——对，此规则仅适用于"历史状态"争议
- "为什么不让 Agent 自己跑 git 验证"——可以，但命令和结果必须可复现
