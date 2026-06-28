---
id: dk-infrastructure-guardrails-over-checklist
title: 基础设施工具不能只有检查清单，还必须有硬护栏
type: dk
dark_knowledge_type: cross-domain-pattern
status: enriched
domain:
- master
- kdo
- ai-collaboration
source_person: KDO 团队复盘
source_context: 第26节master系统暗知识精修：C-10/C-11/P-16/P-8 共同暴露的护栏缺失问题
source_refs: []
related:
- [[dk-small-format-error-cascades-to-system-failure]]
- [[dk-f3-state-json-race-condition]]
- [[dk-p16-validate-reads-state-json]]
- [[dk-c10-batch-tool-no-dry-run]]
- [[dk-tool-as-answer-trap]]
- [[dk-c10-batch-tool-no-dry-run]]
- [[dk-c11-hongqigong-skip-review]]
- [[dk-p16-validate-reads-state-json]]
- [[dk-p8-toolkit-forget]]
- [[dk-tool-as-phased-validator]]
bridges_to:
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-18'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: 工具只有软约束
  follow_up_question: 如果执行者完全跳过这步，工具/系统能否物理上阻止他？
- signal: src_unknown
  framework_lens: 危险操作无二次确认
  follow_up_question: --write 是否需要显式确认目标范围、影响卡数、备份状态？
- signal: src_unknown
  framework_lens: 验证器本身无校验
  follow_up_question: 验证器的结果是否被另一个独立数据源交叉校验过？# 基础设施工具不能只有检查清单，还必须有硬护栏

## 原始表述 / 核心洞察

第 26 节在清理 master 系统暗知识时，连续出现同一个模式：

- src_unknown
- src_unknown
- src_unknown
- src_unknown

**核心洞察**：当操作的影响范围大、恢复成本高、或执行者容易疲劳/误解时，仅靠检查清单、文档、口头约束是不够的。基础设施工具必须把关键约束变成"硬护栏"——即使执行者想犯错，系统也能在物理上阻止、减速或给出不可绕过的二次确认。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **区分"必须阻止"和"建议提醒"**：
   - src_unknown
   - src_unknown
2. **给危险命令加"物理锁"**：
   - src_unknown
   - src_unknown
   - src_unknown
3. **在阶段边界设置不可绕过的停等点**：
   - src_unknown
   - src_unknown
4. **让验证器自己也被验证**：
   - src_unknown
   - src_unknown
5. **在工具入口提示"已存在"**：
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 修复方法 |
|:---|:---|:---|:---|
| **把希望当约束** | 文档写了"请先做 dry-run"，但直接写也能跑 | 只有 checklist 没有硬拦截 | 危险命令默认不执行，必须显式解锁 |
| **阶段边界靠自觉** | 执行者跳过审查节点继续下一段 | 没有持久化审批信号 | 下一段任务检查审批信号，缺失则阻断 |
| **validator 只验证别人不验证自己** | 验证器读了错误数据源仍 PASS | 验证逻辑无回归测试 | 用已知好坏样本做回归，关键输出交叉校验 |
| **工具入口不提示已存在** | 团队重复调研/部署同一工具 | 记忆负担全在人 | 入口自动检索已有工具并提示 |
| **过度护栏拖慢正常操作** | 用户绕过或禁用护栏 | 护栏粒度太粗 | 按风险分级，低风险操作保持流畅 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
