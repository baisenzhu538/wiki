---
id: framework-ouyangfeng-review-methodology
title: 欧阳锋审查方法论：三阶段架构评审框架
type: framework
status: reviewed
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: high
domain:
- master
- kdo
author: 欧阳锋
created_at: '2026-06-21'
updated_at: '2026-07-20'
version: v2.0
source_refs:
- https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md
- https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation/
- https://github.com/veritasfuji-japan/veritas_os/blob/main/docs/en/architecture/adversarial-architecture-test-matrix-v1.md
- 30_wiki/decisions/plan_20260621_skill-iteration-standard.md
- .agent/pitfalls.md
- .agent/daily-review/错误模式库.md
related:
discoverable_by:
  - "欧阳锋审查方法论"
- '[[framework-yitang-research-quality-gate]]'
- '[[framework-yitang-six-layer-cross-validation]]'
- '[[system-yitang-research-workflow]]'
- '[[framework-yitang-research-weapon-system]]'
- '[[framework-kdo-self-attack]]'
tags:
aliases:
  - 欧阳锋审查方法论：三阶段架构评审框架
  - 欧阳锋审查方法论
  - 三阶段架构评审框架
  - 审查方法论
  - 阳锋审查方法论
  - 锋审查方法论
aliases:
  - 欧阳锋审查方法论：三阶段架构评审框架
  - 欧阳锋审查方法论
  - 三阶段架构评审框架
  - 阳锋审查方法论
- audience:ceo
- scene:diagnosis
- skill-level:advanced
aliases:
- daily
- review
- 错误模式库
---
# 欧阳锋审查方法论

> v2.1 · 2026-07-21 补丁：全量机械扫描（#197/#198 教训——深挖 2 张卡过不代表 8 张卡都过）

---

## Phase 0：全量机械扫描（MANDATORY — 深挖之前，先扫全量）

> **#197 教训**：深挖了 2 张 P0 卡全部通过，给了 A——但其余 6 张卡有 4 项 🔴 阻塞完全没发现。
> **#198 教训**：先说先扫——2 秒 grep 发现 4 卡全缺 `diagnostic_signals`。

**此步不可跳过。不做全量扫描 = 审查未开始。**

```
对提交的每张卡（不是抽检样本，是每一张），逐项检查：

□ diagnostic_signals 字段存在且非空（非 TODO/待补）
□ 按类型的 section 完整性：
   - dk: 原始表述/使用场景/操作方法/适用边界/为什么值钱/Critique/关联 — 七段缺一不可
   - case: 关键证据/可迁移场景/教训/失败模式
   - framework: Critique/When NOT to Use/失败模式/Action Triggers
   - tool: 操作步骤/适用边界/失败模式
□ 🆕 子卡定位声明（2026-07-25 补丁）：
   每张 tool/concept/case/dk 卡，related 含 framework 时，正文首段是否声明了框架归属？
   Grep: related 中 framework-* → Read body 前 3 行 → 有 "属于/定位/XX框架/第X步" 任意一个？
   缺少定位声明 = body has no positioning declaration → 🔴 退回
□ related 计数 ≥5 且 ≥2 跨域
□ source_refs 非 src_unknown
□ frontmatter 必填字段：id/type/status/domain/author/reviewed_by/review_date
```

**通过标准**：全部打勾 → 进入 Phase 1（溯源深挖）。任一项不打勾 → 直接退回，不进入深挖。

**执行方式**：Grep 批量扫描，不是 Read 每张卡。4 张卡 ≤30 秒。12 张卡 ≤90 秒。

---

---

## Pre-Phase：生产者自攻击（Producer Pre-Review）

> 欧阳锋开始审查之前，生产者必须先跑自攻击。欧阳锋看到的不是裸卡，是"卡 + 攻击报告 + 修复记录"。
> 自攻击的完整方法见 `[[framework-kdo-self-attack]]`。

### P.1 必选前置条件

生产者（老顽童/黄药师）在投递交付物前必须执行：

```
产卡完成
  ↓
/kdo-self-attack --batch <域>     ← 四路攻击
  ↓
读取攻击报告，修复 🔴 致命 + 🟡 严重 级别问题
  ↓
修复后重新攻击 → 确认问题已关闭
  ↓
投递：卡片 + 攻击报告 + 修复记录
```

### P.2 验收标准

欧阳锋检查投递包：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

**不满足 → 退回生产者，不进入欧阳锋审查阶段。**

### P.3 位置说明

自攻击是生产者的责任，不是欧阳锋的责任。欧阳锋不做自攻击——欧阳锋只审攻击报告。"生产者自检后再投递"是工业品出厂的通用纪律，不是审查流程的一部分。

---

## 第一阶段：范围确认（Pre-Review）

### 1.1 欧阳锋的第一步不是审质量，是审覆盖率

收到交付物后，第一件事不是读交付物内容，而是问：

> "原始素材的全量清单是什么？交付物覆盖了多少？"

**KDO 教训（E009/P-35）**：王语嫣诊断只覆盖了 ~10% 素材（73-97 张卡只识别了 10 张），但我直接在她的范围内做内容审查，没发现覆盖率问题。

**检查清单**：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 1.2 第二问：交付者的 bias 是什么

| 交付者角色 | 常见 bias | 审查者抵消方法 |
|:-----------|:----------|:--------------|
| 诊断者（王语嫣） | 只读笔记不读口述原文；scope 选自己熟悉的 | 独立 Agent 扫读原始素材 |
| 生产者（老顽童） | 爱把多个域压成一张大卡（F-EQG-001） | 检查每卡是否一卡一事 |
| 基础设施者（黄药师） | 自动化方案偏好 | 人工抽检验证 |

---

## 第二阶段：执行审查（Review Execution）

### 2.1 三通路并行法

不是串行读交付物，而是三条通路并行：

```
通路 A: 独立扫读原始素材（Agent 并行）
通路 B: 读交付物 + 对照原始素材
通路 C: 抽检典型样本
```

**KDO 教训**：第一次审查我只走了 B（读王语嫣交付物），没走 A（独立扫原始素材）。第二次审查我走了 A 但没走 C（抽检老顽童实际产出）。第三次才三条全走。

### 2.2 内容质量审查：三信号法

| 信号 | 好 | 差 |
|:-----|:---|:---|
| **反例具体性** | Critique 有真实的外部攻击者（Herbert Simon 批判 OSCAR） | "这个框架在X场景可能失效"——没说为什么 |
| **边界认识** | 明确写了"不要用"的场景，且理由可验证 | 全是正面论证 |
| **跨域连接** | 引用 ≥2 个其他域的卡片 | 孤立卡片，不和已有知识对话 |

### 2.3 Review Bias 自检

从 peer review 研究已知的 6 种 bias，审查者必须逐项自检：

| Bias | 症状 | 自检问题 |
|:-----|:------|:---------|
| **归属偏见** | 对某人的产出天然信任/不信任 | 如果这是另一个人做的，我的判断会不同吗？ |
| **锚定偏见** | 第一个数字/印象影响后续判断 | 我的判断是否被第一个接触到的数据锚定了？ |
| **确认偏见** | 只找支持自己判断的证据 | 我有没有主动找反例？ |
| **光环效应** | 因为某个亮点而忽略整体缺陷 | 如果去掉这个亮点，整体评分变吗？ |
| **刻度不一致** | 不同批次用不同标准 | 这次的标准和上次的一致吗？ |
| **多轮退化** | 审太多轮后判断力下降 | 这一轮前休息过吗？这一轮的评语和上一轮语气一致吗？ |

**外部证据**：peer review 研究显示 44% 的审查者认为自己找的是 defect，但实测只有 ~14% 的 review comments 真正找到了 defect（Kitchenham 系统综述）。

---

## 第三阶段：交付与注册（Post-Review）

### 3.1 裁决分类

| 裁决 | 含义 | 后续动作 |
|:-----|:------|:---------|
| ✅ 通过 | 质量达标，可直接入库 | 标记 status: reviewed_by=ouyangfeng |
| ✅ 条件通过 | 有小问题但不阻塞 | 列出待修项，标注"修后不用再审" |
| ⏳ 待修改 | 有实质问题需修正 | 给出具体修复方向，再审 |
| ❌ 驳回 | 质量不达标或 scope 问题 | 明确原因，回到 Pre-Review 阶段 |

### 3.2 审查产出的注册

每次审查完成后，必须做三件事：

1. **更新错误模式库**（`.agent/daily-review/错误模式库.md`）——有新模式追加，有复发更新次数
2. **写入 pitfalls.md**——新坑立新条目
3. **更新 context.md**——active_task 和 blockers

---

## 与调研域工具的关系

| 审查阶段 | 可调用的 KDO 工具 | 用途 |
|:---------|:-----------------|:-----|
| Pre-Review | `/research` | 接到审查任务→自动识别审查类型 |
| Pre-Review | `/research-multi-agent` | 派多个 Agent 并行扫读原始素材 |
| Review | `/research-cross-validation` | 六层验证交付物中的关键结论 |
| Review | `/research-sats` | Devil's Advocacy 挑战自己初始判断 |
| Review | `/research-quality-gate` | 六维门禁自检审查报告本身 |
| Post-Review | `framework-yitang-research-weapon-system` | 确保审查结论写入正确位置 |

---

## 案例：本次会话的自检

| 审查轮次 | 走的通路 | 漏了什么 | 对应错误模式 |
|:---------|:--------|:---------|:-------------|
| 第 1 轮（王语嫣交付） | B only | 没走 A，没发现覆盖率仅 10% | E009（新） |
| 第 2 轮（独立审查） | A + B | 没走 C，没核对老顽童实际产出 | E004 复发（萃取深度误判） |
| 第 3 轮（老顽童产出） | A + B + C | 都走了 | — |

---

*欧阳锋 · 2026-06-21 v1.0 · 2026-07-20 v2.0（注入全网审查最佳实践）*

---

## v2.0 升级（2026-07-20）：全网审查最佳实践注入

> 调研来源：
> - [Code Review Best Practices 2025-2026](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md) — Stay Green 质量门模型、五轴审查、盲审+魔鬼代言人
> - [Google Cloud AI Agent Evaluation](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation/) — 三支柱评估（成功质量/过程轨迹/信任安全）
> - [Veritas OS Adversarial Architecture Test Matrix v1](https://github.com/veritasfuji-japan/veritas_os/blob/main/docs/en/architecture/adversarial-architecture-test-matrix-v1.md) — 治理投毒/评估漂移等 8 类对抗性验证
> - [Snyk 2025 AI Agent Security Report](https://snyk.io/) — 36.82% 公开 skill 含安全缺陷

### v2.0.1 五轴审查维度（升级原三信号）

| 轴 | 知识卡对应 | 检查问题 |
|:--|:--|:--|
| **正确性** | Claims 有源行号支撑？数字可复核？ | "这条 claim 的口述稿原文在哪？" |
| **边界感** | When NOT to Use + 失败模式 + 外部攻击者 | "如果我是反对者，我会攻击哪个前提？" |
| **架构** | 域内关系 + 跨域桥接 + 无死链 | "related >=5 且 >=2 跨域？和已有卡是对标/互补/矛盾？" |
| **可读性** | 标题精准 + 一句话摘要准确 + 结构清晰 | "只看标题和一句话，Agent 能判断这张卡是否相关？" |
| **暗知识密度** | 反常识发现 + 可执行操作 + 失败信号具体 | "读完后有没有学到搜 Google 搜不到的东西？" |

### v2.0.2 魔鬼代言人机制

当审查结论 >= A- 且自攻击报告 🔴🟡 均为 0 时，强制触发：

```
"假设这张卡入库 3 个月后被发现有问题——最可能是什么问题？"
→ 30 秒内说不出一条具体风险 → 审查太浅，重审
→ 说得出 → "这个风险卡里预判了吗？够具体吗？"
→ 补充到审查结论「残余风险」栏
```

**依据**：peer review 研究显示审查者自评找到 defect 比例 44%，实测仅 14%（Kitchenham 系统综述）。魔鬼代言人抵消这 30% 差距。

### v2.0.3 分层阻断刚性化

| 等级 | 定义 | 阻断？ |
|:--|:--|:--:|
| 🔴 Critical | source_refs 伪造、Claims 与原文矛盾、跨域桥接方向错误 | **阻断** |
| 🟡 High | 缺关键 section、related < 3、外部攻击者为 straw man | **阻断** |
| 🟠 Medium | related < 5、缺 1 条攻击者、标题不够精准 | 放行+TODO |
| 🔵 Low | 格式微瑕、术语未标注全称 | 放行 |

🔴+🟡 未清零 → 不得 pass。

### v2.0.4 对抗性治理验证（月度抽检用）

| # | 攻击类 | 检查问题 |
|:--:|:--|:--|
| A | 治理投毒 | 近一月审查标准是否被"大家都这么写"稀释了？抽查 3 张近期 A 级卡用 v1.0 标准重审 |
| B | 准入漂移 | 复查最近 5 条 B+/B 裁决的追补项是否真的修了 |
| C | 评估漂移 | 王语嫣独立审 1 张我已审的卡，对比差异 |
| D | 外部影响 | 任务优先级是否影响了质量判断？ |
| E | 审查疲劳 | >=5 张卡后强制暂停 |
| F | 信任锚漂移 | "老顽童近期质量高"→少审几张？月度抽检比例不得低于矩阵最低值 |
| G | 历史≠现在 | 禁止用"上次类似卡过了"作为通过理由 |
| H | 隐性放松 | pre-submit PASS != 理解门禁通过 |

### v2.0.5 审查可追溯性

每次审查结论必须包含：

```yaml
reviewer: 欧阳锋
methodology_version: v2.0
verdict: pass-A- | pass-B+ | fail
blocking: [🔴N, 🟡N]
residual_risks: [魔鬼代言人发现的未解决风险]
devil_advocate_triggered: true | false
```

### v2.1 多维数字评分（2026-07-26 升级——全网调研落地）

> 依据：Prompt-to-Paper 8 维评分 + Agent Book Factory 5 维评分 + 全网最佳实践。
> 字母等级仍是终审结论，数字分是诊断工具——让生产者知道"哪里弱"。

**5 维评分标准**（每维 0-100，加权总分 → A/B/C 等级）：

| 维度 | 权重 | 0-40 分（不及格） | 40-70 分（及格） | 70-90 分（优秀） | 90-100 分（卓越） |
|:--|:--:|:--|:--|:--|:--|
| **溯源完整** | 25% | source_refs 空或伪造；Claims 与原文矛盾 | source_refs 有但缺行号；部分 claims 无出处 | source_refs 完整带行号；关键 claims 全部可溯源 | 所有 claims 有行号+原文摘录；外部对标有出处 |
| **逻辑骨架** | 25% | 要素罗列无依赖关系；缺定位声明 | 有依赖关系但不完整；定位声明存在但模糊 | 依赖关系清晰+定位精准；related 双向链接≥5 | 依赖关系呈现为可视化结构；与新域首卡有跨域同构 |
| **暗知识密度** | 20% | 失败模式模板化（"步骤跳过→严格按步骤"）；无反例 | 失败模式≥2条且带症状；至少有1条真实反例 | 失败模式≥3条且每条带"症状+修复"；Critique 有外部攻击者≥2 | 失败模式含具体案例引用；外部攻击者与卡内容紧密相关 |
| **可操作性** | 15% | 无 Action Triggers；无解压资产 | Action Triggers 有但模糊；related 有 tool/skill 但<3 | Action Triggers 有触发条件+成功指标；解压资产≥3 | 解压资产有已实现版本（非"待建"）；有配套 case 验证 |
| **表达质量** | 15% | AI 味重（排比堆砌/概念太密/说教感）；正文<50行 | 基本流畅但有少量模板话；正文 50-100 行 | 人类语调自然；正文≥100行；无可传播金句或场景锚点 | 正文≥150行且每段有信息增量；有 burn line；首段有场景锚点 |

**总分 → 等级映射**：
| 加权总分 | 等级 | 说明 |
|:--|:--|:--|
| ≥90 | **A** | 全维度卓越，可作为该类型卡片的参考标准 |
| 80-89 | **A-** | 深度达标，有 1-2 个小遗漏 |
| 70-79 | **B+** | 结构完整，但暗知识密度或可操作性不足 |
| 60-69 | **B** | 基本合规，深度不够 |
| 50-59 | **B-** | 格式合规但内容空洞 |
| <50 | **C** | 不及格，退回重做 |

**使用方式**：欧阳锋终审时给每张 framework 卡打出 5 维分 + 总分 + 等级。concept/tool/case 卡只需总分+等级，不需逐维打分。评分写入审查结论的 `scores` 字段：

```yaml
reviewer: 欧阳锋
methodology_version: v2.1
verdict: pass-A-
scores:
  sourcing: 85     # 溯源完整
  structure: 78    # 逻辑骨架
  tacit_density: 65  # 暗知识密度
  actionability: 72  # 可操作性
  expression: 80   # 表达质量
  total: 76.2      # 加权总分
blocking: [🟡1]
residual_risks: ["暗知识密度偏低——失败模式仅2条且第2条无具体案例"]
```
