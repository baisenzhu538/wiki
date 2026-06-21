---
id: framework-ouyangfeng-review-methodology
title: 欧阳锋审查方法论：三阶段架构评审框架
type: framework
status: draft
confidence: 0.88
trust_level: high
domain:
  - master
  - kdo
author: 欧阳锋
created_at: "2026-06-21"
source_refs:
  - web: ATAM (Architecture Trade-off Analysis Method) — SEI/CMU
  - web: SARA (Software Architecture Review & Assessment) — Philippe Kruchten
  - web: NHS Digital Software Engineering Quality Framework
  - web: dycke-gurevych-2025 counterfactual evaluation framework
  - 30_wiki/decisions/plan_20260621_skill-iteration-standard.md
  - .agent/pitfalls.md §P-35
  - .agent/daily-review/错误模式库.md §E009
related:
  - "[[framework-yitang-research-quality-gate]]"
  - "[[framework-yitang-six-layer-cross-validation]]"
  - "[[system-yitang-research-workflow]]"
  - "[[framework-yitang-research-weapon-system]]"
---

# 欧阳锋审查方法论

> 基于软件工程架构评审最佳实践 + KDO 3 轮实地审查教训。三阶段走完，确保不遗漏、不偏见、不压数。

---

## Pre-Phase：生产者自攻击（Producer Pre-Review）

> 欧阳锋开始审查之前，生产者必须先跑自攻击。欧阳锋看到的不是裸卡，是"卡 + 攻击报告 + 修复记录"。

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

- [ ] 攻击报告存在（`60_feedback/adversarial/atk_*`）
- [ ] 🔴 致命问题已全部关闭
- [ ] 🟡 严重问题已全部修复或标注"已知但暂不修复（附理由）"
- [ ] 🟢 轻微问题已记录（可不修复）
- [ ] 修复记录有 git diff 或变更说明

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
- [ ] 拿到原始素材全量清单
- [ ] 对比"交付物覆盖范围 vs 原始素材范围"
- [ ] 覆盖率 < 80% → 退回补充或发起独立扫读
- [ ] 覆盖率 ≥ 80% → 进入第二阶段

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

*欧阳锋 · 2026-06-21 · 基于全网调研+3 轮实地审查教训提炼*
