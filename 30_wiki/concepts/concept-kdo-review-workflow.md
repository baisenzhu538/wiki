---

id: concept-kdo-review-workflow
title: KDO 生产审查工作流（欧阳锋模式）
type: concept
domain:
- ai-collaboration
- knowledge-management
status: reviewed
created_at: 2026-06-29
updated_at: 2026-06-29
author: 欧阳锋
reviewed_by: 欧阳锋
review_date: 2026-06-29
confidence: 0.85
trust_level: high
source_refs:
- pending_archive:2026-06-29 review retrospective
- 60_feedback/tasks/task_20260629_kimi-lint-content-debt-by-domain.md
related:
- "[[ec工业化规范手册-v2.8.0|EC 工业化规范手册]]"
- "[[concept-yitang-facts-first]]"
- <code>kdo pre-submit</code>
- <code>kdo lint</code>
- "[[framework-kdo-self-attack|KDO 知识自攻击]]"
---

# KDO 生产审查工作流（欧阳锋模式）

> **Burn line**: 审查者的任务是验证「交付物是否达到可合并状态」，不是替生产者改代码或卡内容。

---

## Purpose

本工作流定义 KDO 知识工厂中「欧阳锋」角色的审查标准动作。目标是：

1. **防止虚假完成**：确认任务单中的交付标准被真实满足，而非仅被勾选。
2. **守住质量门禁**：确保 `kdo lint` 和 `kdo pre-submit` 不因本次任务退化。
3. **控制债务转移**：识别「把 A 类 WARNING 批量转成 B 类 WARNING」的降噪假象。
4. **保持角色边界**：审查者发现问题后，应退回或记录修复要求，而不是越俎代庖修改生产代码/卡片内容。

---

## Protocol/Procedure

### 审查前准备

1. **读取任务单**：明确任务范围、交付标准、依赖任务。
2. **读取生产队列/上下文**：确认任务状态、blockers、上一轮基线。
3. **确认工具版本**：`kdo --help`、`kdo lint --help`、`kdo pre-submit --help`，避免任务单引用不存在选项。

### 审查中检查项

| 检查项 | 方法 | 通过标准 |
|:---|:---|:---|
| 文件存在且状态正确 | `git status`、`git log --stat` | 任务产出文件在预期路径；`status` frontmatter 正确 |
| frontmatter 完整 | 抽样读取 + `kdo lint` | 无 ERROR，无任务相关 WARNING |
| 链接与索引 | 检查 `related`、检查 `30_wiki/index.md` | 新卡被索引；核心卡片双向链接 |
| 内容结构 | 抽样 grep section 标题 | concept/framework/tool/case 各自 section 完整 |
| lint 基线 | `kdo lint --summary` | 0 新增 ERROR；WARNING 变化与任务目标一致 |
| pre-submit 基线 | `kdo pre-submit` | 本次修改文件不在错误列表中；全局 FAIL 需说明是否历史遗留 |
| 债务转移检查 | 对比各类 WARNING 数量变化 | 没有「删 section 导致 copy-paste↓ 但 body-too-short↑」的等价转移 |

### 审查后动作

1. **更新任务单**：添加审查记录、勾选/未勾选交付标准、状态变更。
2. **更新生产队列**：状态、备注、基线数字。
3. **更新 `.agent/context.md`**：active_task、blockers、next_session_hint。
4. **明确下一步**：继续推进 / 退回修复 / 进入下一任务。

### 输出物模板

```markdown
## 欧阳锋终审记录

- **审查时间**：YYYY-MM-DD
- **实测验证**：
  - `kdo lint`：0 ERROR / N WARNING
  - `kdo pre-submit`：目标文件无 ERROR；全局 FAIL 原因为 ...
- **发现问题**：...
- **已修复 / 待修复**：...
- **结论**：reviewed / 退回
```

---

## When NOT to Use

- **审查者自己也是同一任务的执行者**：必须换角色或换 Agent 审查，否则丧失独立性。
- **任务单引用了不存在的 CLI 选项**：不要直接替生产者实现；应先退回任务单修正，或在明确授权后作为独立基建任务实现。
- **发现基础设施 bug 时**：记录并分配给黄药师/老顽童作为独立任务，而不是在审查过程中直接修改已安装 CLI 源码（会导致源码与仓库不同步）。
- **全局 pre-submit 因历史遗留 FAIL 时**：不能因此直接拒绝一个只做新卡/清理类任务，但必须在审查记录中明确区分。

---

## Critique

### 本工作流的局限

- **依赖抽样检查**：全库卡片数量巨大，审查只能抽样；可能漏掉边缘 case。
- **无法自动识别内容质量**：lint 只能检测格式，critique 深度、外部反对者相关性、可迁移场景真实性仍需人判断。
- **角色边界在紧急修复时容易模糊**：当工具 bug 阻塞多条任务线时，审查者可能被拉去改代码。

### 常见失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 审查者改代码 | 审查记录里出现「已修复 CLI bug」 | 把改代码动作拆成独立任务，由生产者执行，审查者只验收 |
| 测试污染工作区 | 审查时遗留 stash/tag/临时文件 | 审查测试前 `kdo snapshot`，测试后 `git status` 确认干净 |
| 债务转移被放行 | copy-paste↓ 但 body-too-short↑ | 要求生产者给出「真实净减」证据，否则退回 |
| 任务单写不存在命令 | `kdo lint --domain` 当时不存在 | 审查前先验证 `--help`；发现即退回或升级基建 |
| 全局失败误伤任务 | pre-submit FAIL 就拒绝 | 区分目标文件错误与历史遗留错误 |

---

## Action Triggers

- **用户说「你去审查」** → 按本工作流执行，给出 reviewed/退回结论。
- **lint 0 ERROR 但 WARNING 结构变化** → 检查是否债务转移。
- **任务单引用不存在命令** → 退回或升级为基建任务。
- **全局 pre-submit FAIL** → 先 grep 目标文件，再判断是否与本次任务相关。

---

## Synthesis

### 关联概念

- [[ec工业化规范手册-v2.8.0|EC 工业化规范手册]] — 回退预案、预提交自检、依赖冻结、环境锁定等 EC 概念
- [[framework-kdo-self-attack|KDO 知识自攻击]] — 对知识卡片的四路自攻击，可作为深度内容审查补充
- [[concept-yitang-facts-first]] — 事实先于观点，审查时先跑工具再下判断

### 跨域桥接

| 目标域 | 桥接点 | 使用场景 |
|:---|:---|:---|
| 产品管理 | [[productization-judgment]] | 判断审查发现的问题是否值得产品化修复 |
| 团队协作 | [[yai-counsel-role]] | 审查者与生产者冲突时如何反馈 |
| 教育设计 | [[yai-tcp-teacher-role]] | 把审查记录作为后续教学的反面案例 |

---

## Feedback Path

- 每次审查后回顾：是否越界修改了代码/内容？是否留下测试污染？是否误放行了债务转移？
- 每轮大任务结束后更新本工作流卡片，沉淀新发现的失败模式。
