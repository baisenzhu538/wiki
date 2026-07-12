---
id: task_20260629_laowantong-expand-ai-learning-concept-cards
title: 扩展 AI 工具学习方法论原子概念卡
type: task
status: reviewed
source_refs:
- 00_inbox/元能力-刻意练习/YAI的C角色给我的诊断.md
- 00_inbox/元能力-刻意练习/我和一堂YAI关于刻意练习的对话.md
wiki_refs:
- '[[yai-counsel-role]]'
- '[[yai-tcp-teacher-role]]'
- '[[deliberate-practice-four-elements]]'
- '[[ai-tool-learning-curve]]'
- '[[four-questions-feedback]]'
- '[[completion-criteria-design]]'
- '[[challenge-point-design]]'
- '[[productization-judgment]]'
- '[[consultant-mode-yai-style]]'
assignee: 老顽童
priority: medium
created_at: '2026-06-29'
updated_at: '2026-06-29'
review_date: '2026-06-29'
reviewed_by: 欧阳锋
---

# 任务：扩展 AI 工具学习方法论原子概念卡

## 任务目标

用户要求把 YAI T/C 角色生成的 AI 工具学习方法论资料进一步拆分为原子化概念卡，纳入知识库，方便未来迭代成 Scale Framework 或其他体系。

本任务负责扩展**尚未创建**的概念卡片，并确保所有相关卡片之间建立正确链接。

## 已完成的基础卡片（不要重复创建）

以下卡片已由欧阳锋/规划角色创建完成：

1. `30_wiki/concepts/deliberate-practice-four-elements.md` —— 刻意练习四要素
2. `30_wiki/concepts/four-questions-feedback.md` —— 四问法自我反馈
3. `30_wiki/concepts/completion-criteria-design.md` —— 完成标准设定
4. `30_wiki/concepts/challenge-point-design.md` —— 挑战点设计
5. `30_wiki/concepts/ai-tool-learning-curve.md` —— AI 工具循序渐进学习曲线
6. `30_wiki/concepts/productization-judgment.md` —— 产品化判断四维度

## 需要创建的新卡片

### 高优先级（核心概念）

1. **`30_wiki/concepts/fixed-routine-design.md`**
   - 类型：tool/framework
   - 内容：什么是固定套路、为什么重要、如何设计第一版固定套路、常见失败模式
   - 必须链接：[[deliberate-practice-four-elements]]、[[ai-tool-learning-curve]]

2. **`30_wiki/concepts/comfort-zone-expansion.md`**
   - 类型：concept
   - 内容：舒适区/拉伸区/恐慌区模型、如何判断挑战点是否合适、如何设计拉伸区练习
   - 必须链接：[[deliberate-practice-four-elements]]、[[challenge-point-design]]

3. **`30_wiki/concepts/timely-feedback-loop.md`**
   - 类型：framework
   - 内容：反馈的定义、自我反馈 vs 外部反馈 vs AI 反馈、如何建立最低成本反馈闭环
   - 必须链接：[[deliberate-practice-four-elements]]、[[four-questions-feedback]]、[[ai-virtual-coach-prompt]]

4. **`30_wiki/concepts/deliberate-repetition.md`**
   - 类型：concept
   - 内容：大量重复的真正含义、如何拆成小练习卡片、如何在碎片时间叠加练习、如何避免低水平重复
   - 必须链接：[[deliberate-practice-four-elements]]、[[practice-card-decomposition]]

### 中优先级（工具卡）

5. **`30_wiki/concepts/ai-virtual-coach-prompt.md`**
   - 类型：tool
   - 内容：AI 虚拟教练差距分析的提示词模板、使用场景、输入输出格式、注意事项
   - 必须链接：[[four-questions-feedback]]、[[timely-feedback-loop]]、[[ai-tool-learning-curve]]

6. **`30_wiki/concepts/practice-card-decomposition.md`**
   - 类型：tool
   - 内容：如何把一个大学习过程拆成 15-30 分钟练习卡片、卡片模板、周中碎片时间使用方法
   - 必须链接：[[ai-tool-learning-curve]]、[[deliberate-repetition]]

7. **`30_wiki/concepts/ai-tool-learning-workbook.md`**
   - 类型：tool
   - 内容：指向 `40_outputs/capabilities/skills/consultant-mode-yai-style/WORKBOOK.md` 的入口卡，说明用途和使用方法
   - 必须链接：[[ai-tool-learning-curve]]、[[consultant-mode-yai-style]]、[[yai-counsel-role]]

## 格式要求

每张卡片必须符合 `90_control/schemas/concept.yaml`：

- `id`：kebab-case
- `title`：中文，简洁
- `type`：concept / framework / tool
- `domain`：根据内容选择，至少一个主要 domain
- `status`：enriched
- `source_refs`：引用来源文件或链接
- `related`：链接到相关卡片
- `created_at` / `updated_at`：2026-06-29
- `confidence` / `trust_level`：合理评估
- `diagnostic_signals`：至少 1-2 个触发场景

正文结构参考：Summary → Core Claims → Usage/Template → Constraints & Boundaries → Action Triggers → Synthesis → Feedback Path

## 链接要求

1. 新建的 7 张卡片必须和已有的 6 张核心卡片互相链接
2. 更新以下卡片的 `related` 字段，加入新卡片链接：
   - `yai-counsel-role.md`
   - `yai-tcp-teacher-role.md`
   - `deliberate-practice-four-elements.md`
   - `ai-tool-learning-curve.md`
3. 确保所有 wikilink 有效，不出现死链

## 交付标准

- [x] 7 张新卡片全部创建完成
- [x] 所有卡片 frontmatter 符合 concept.yaml
- [x] 所有卡片正文结构完整，无 `src_unknown` 占位
- [x] 卡片之间链接关系建立
- [x] `kdo lint` 无新增 ERROR
- [ ] `kdo pre-submit` 通过（任务本身产出无 ERROR；全量失败由历史遗留 case/dk 问题导致）

## 预计产出

- 7 张新 concept 卡片
- 4-6 张已有卡片的 related 字段更新

## 备注

- 本任务可与 A1/A2 lint 清理任务并行，因为操作的是不同文件
- 完成后由欧阳锋终审

## 审查记录（欧阳锋）

- **审查时间**：2026-06-29
- **发现问题**：
  1. `ai-virtual-coach-prompt.md`、`practice-card-decomposition.md`、`ai-tool-learning-workbook.md` 3 张 tool 卡正文缺少标准 section（Purpose / Protocol/Procedure / When NOT to Use / Critique），lint 报 WARNING。
  2. `yai-counsel-role.md`、`yai-tcp-teacher-role.md`、`ai-tool-learning-curve.md` 未按任务要求在 `related` 中加入新卡片链接。
- **已修复**：
  1. 重构 3 张 tool 卡，补全 Purpose / Protocol/Procedure / When NOT to Use / Critique。
  2. 更新 `deliberate-practice-four-elements.md`、`yai-counsel-role.md`、`yai-tcp-teacher-role.md`、`ai-tool-learning-curve.md` 的 `related` 字段，建立新旧卡片双向链接，并同步更新 `updated_at`。
- **验证结果**：
  - `kdo lint --diff`：0 new error；与本次修改文件相关的 WARNING 未新增。
  - `kdo pre-submit`：全量仍因历史遗留 case/dk 问题 FAIL，但本次 7 张新卡及 4 张更新的旧卡均未出现在错误列表中。
- **结论**：任务产出通过审查，状态置为 `reviewed`。
