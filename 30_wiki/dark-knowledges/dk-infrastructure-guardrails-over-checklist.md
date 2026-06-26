---

id: dk-infrastructure-guardrails-over-checklist
title: 基础设施工具不能只有检查清单，还必须有硬护栏
type: dark-knowledge
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
  - '[[dk-small-format-error-cascades-to-system-failure]]'
  - '[[dk-f3-state-json-race-condition]]'
  - '[[dk-p16-validate-reads-state-json]]'
  - '[[dk-c10-batch-tool-no-dry-run]]'
  - '[[dk-tool-as-answer-trap]]'
  - '[[dk-c10-batch-tool-no-dry-run]]'
  - '[[dk-c11-hongqigong-skip-review]]'
  - '[[dk-p16-validate-reads-state-json]]'
  - '[[dk-p8-toolkit-forget]]'
  - '[[dk-tool-as-phased-validator]]'
bridges_to:
- dk-c10-batch-tool-no-dry-run
- dk-c11-hongqigong-skip-review
- dk-p16-validate-reads-state-json
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-18'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 事故复盘结论是"执行者没有按 checklist 操作"
  framework_lens: 工具只有软约束
  follow_up_question: 如果执行者完全跳过这步，工具/系统能否物理上阻止他？
- signal: 批量脚本有 --dry-run 选项，但直接跑 --write 也能成功
  framework_lens: 危险操作无二次确认
  follow_up_question: --write 是否需要显式确认目标范围、影响卡数、备份状态？
- signal: validator 通过后发现验证逻辑读错了数据源
  framework_lens: 验证器本身无校验
  follow_up_question: 验证器的结果是否被另一个独立数据源交叉校验过？
---# 基础设施工具不能只有检查清单，还必须有硬护栏

## 原始表述 / 核心洞察

第 26 节在清理 master 系统暗知识时，连续出现同一个模式：

- C-10：老顽童直接跑 `kdo scaffold --batch B --write`，71 张卡的攻击段落被清空。系统并非没有 checklist，但 `--write` 是一个随时可执行的软选项。
- C-11：洪七公把"快速提报"理解为"不需要提报"，三段画面连续产出，三次审查全部跳过。流程文档写了要停等，但工具没有强制停等点。
- P-16：`validate` 优先读取 `state.json` 而非文件 frontmatter，验证的是过期/错误的数据，但系统依然给出 PASS。
- P-8：欧阳锋忘记本地已有某工具，重新调研已部署工具。不是人不够细心，而是工具/系统没有在使用入口提示"已存在"。

**核心洞察**：当操作的影响范围大、恢复成本高、或执行者容易疲劳/误解时，仅靠检查清单、文档、口头约束是不够的。基础设施工具必须把关键约束变成"硬护栏"——即使执行者想犯错，系统也能在物理上阻止、减速或给出不可绕过的二次确认。

## 使用场景

- 设计批量写入、删除、覆盖类脚本时。
- 设计审查/提报/发布流程时，执行者可能跳过关键节点。
- 设计 validator、 linter、质量门禁时，需要防止验证逻辑本身出错。
- 工具库/武器库越来越多，需要防止重复调研、重复部署。
- 评估一次事故是"人的疏忽"还是"工具设计缺陷"时。

## 操作方法

1. **区分"必须阻止"和"建议提醒"**：
   - 对不可逆、批量、高风险操作，使用硬护栏（强制确认、备份、权限、白名单）。
   - 对可逆、低风险操作，使用软提醒（checklist、文档、日志）。
2. **给危险命令加"物理锁"**：
   - `--write` 需要显式传入 `--confirm-impact=N`。
   - 批量操作前强制要求 `--backup-path`。
   - 覆盖旧格式前必须展示 diff 并输入 `YES`。
3. **在阶段边界设置不可绕过的停等点**：
   - 不是"请在这里提报"，而是"下一段任务未收到上一段审批信号时无法开始"。
   - 审批信号必须写入不可被本地覆盖的持久化记录（如 commit、issue、state.json 签名）。
4. **让验证器自己也被验证**：
   - 定期用"已知坏样本"和"已知好样本"跑回归测试，确保 validator 没有读错数据源。
   - validator 的关键输出应被第二个独立数据源交叉校验。
5. **在工具入口提示"已存在"**：
   - 当用户尝试调研/部署一个已存在工具时，先弹窗展示已有工具及其负责人、使用场景。
   - 避免把"记住本地有什么"的责任完全放在人身上。

## 适用边界

- **适用于**：不可逆/批量/高风险/多人协作的基础设施操作。
- **不适用于**：探索性、创造性、需要快速试错的环境——过度护栏会拖慢迭代。
- **护栏不是替代培训**：再强的护栏也需要人理解为什么存在；否则用户会寻找绕过方法。
- **成本权衡**：为极低频操作加复杂护栏可能不划算；优先保护高频、高损失场景。

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 修复方法 |
|:---|:---|:---|:---|
| **把希望当约束** | 文档写了"请先做 dry-run"，但直接写也能跑 | 只有 checklist 没有硬拦截 | 危险命令默认不执行，必须显式解锁 |
| **阶段边界靠自觉** | 执行者跳过审查节点继续下一段 | 没有持久化审批信号 | 下一段任务检查审批信号，缺失则阻断 |
| **validator 只验证别人不验证自己** | 验证器读了错误数据源仍 PASS | 验证逻辑无回归测试 | 用已知好坏样本做回归，关键输出交叉校验 |
| **工具入口不提示已存在** | 团队重复调研/部署同一工具 | 记忆负担全在人 | 入口自动检索已有工具并提示 |
| **过度护栏拖慢正常操作** | 用户绕过或禁用护栏 | 护栏粒度太粗 | 按风险分级，低风险操作保持流畅 |

## 为什么值钱

- **把事故根因从"人不靠谱"转移到"工具缺护栏"**：大多数批量事故不是执行者故意违规，而是系统设计允许了危险操作。
- **降低协作摩擦**：硬护栏让审查、备份、确认变成默认路径，减少人与人之间的拉扯。
- **保护组织记忆**：通过工具入口提示"已存在"，避免知识重复造轮子。
- **与 AI 时代高度相关**：AI 生成和批量操作越来越频繁，硬护栏是防止"AI 帮你一键毁掉一切"的关键。

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 直接跑 `--write` 清空 71 张卡，是"缺硬护栏"的典型案例。
- [[dk-c11-hongqigong-skip-review]] — 阶段边界没有停等信号，审查节点靠自觉。
- [[dk-p16-validate-reads-state-json]] — validator 读了错误数据源仍 PASS，说明验证器也需要被验证。
- [[dk-p8-toolkit-forget]] — 忘记本地已有武器，是工具入口缺少"已存在"提示的结果。
- [[dk-tool-as-phased-validator]] — 工具应分阶段校验；硬护栏就是把这些阶段校验变成不可绕过的系统行为。
