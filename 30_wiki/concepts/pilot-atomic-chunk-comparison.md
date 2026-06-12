---

id: "pilot-atomic-chunk-comparison"
title: "Pilot：master-decision-hygiene 真原子切分对比"
type: "comparison"
status: "draft"
created_at: 2026-05-31
source_refs:
  - "30_wiki/concepts/master-decision-hygiene.md"
tags:
  - #domain/knowledge-management
  - #quality/high-signal
  - #scene/agent-infrastructure
  - #scene/knowledge-management/atomization
  - #scene/knowledge-management/tagging
  - #scene/learning-methodology/mental-models
  - #scene/note-taking/live-field
pipeline:
  - #boundary/requires-human-judgment
  - confidence-draft
  - confidence-source-cited

domain: []---

# Pilot：master-decision-hygiene 真原子切分对比

## 素材：Section "三、核心模型：五步法"（原文 ~2200 字）

---

## 假原子（v1.1 heading 级切分）

**切分方式**：按 `###` 标题切。整个 section 产出 **7 个 chunk**：

```
master-decision-hygiene/definition/001   — "三、核心模型：五步法" 概述 + ASCII图 (100字)
master-decision-hygiene/claim/001        — "Step 1：分解判断" 全部内容 (350字)
master-decision-hygiene/claim/002        — "Step 2：外部视角" 全部内容 (280字)
master-decision-hygiene/claim/003        — "Step 3：独立评估" 全部内容 (250字)
master-decision-hygiene/claim/004        — "Step 4：聚合" 全部内容 (350字)
master-decision-hygiene/claim/005        — "Step 5：延迟直觉" 全部内容 (250字)
master-decision-hygiene/example/001      — "四、完整流程示例" 全部内容 (400字)
```

**问题**：Step 1 的 chunk 包含 5 段文字——核心操作、为什么有效、具体做法×3、陷阱。任何一个 query 只能拉取整块。AI 拿到 350 字的混合内容，无法精确定位"分解的具体做法"和"为什么这样有效"的区别。

---

## 真原子（v1.3 主张/事实/规则级切分）

**切分方式**：每个可独立引用、独立验证、独立反驳的最小单元作为一块。同一 section 产出 **35 个 chunk**：

### Step 1：分解判断 → 6 chunks

```
chunk_id: master-decision-hygiene/claim/001
  类型: claim
  内容: "Step 1 核心操作：把'这个项目能成吗？'拆成'市场规模→竞争强度→团队能力→资金需求→执行风险'五个子判断"

chunk_id: master-decision-hygiene/claim/002
  类型: claim
  内容: "复杂判断的噪声 > 简单判断的噪声之和。人对整体的估计充满噪声，但对子部分的估计更稳定"

chunk_id: master-decision-hygiene/procedure/001
  类型: procedure
  内容: "做法1：列出决策涉及的所有维度（≥3个）"

chunk_id: master-decision-hygiene/procedure/002
  类型: procedure
  内容: "做法2：每个维度给一个独立评分（1-10或具体数值）"

chunk_id: master-decision-hygiene/constraint/001
  类型: constraint
  内容: "禁止在分解前就给出整体判断"

chunk_id: master-decision-hygiene/error_data/001
  类型: error_data
  内容: "陷阱：分解维度本身也可能有噪声。不同的人拆出不同的维度。对策：用同一套维度模板（如Y模型的五步法画布）"
```

### Step 2：外部视角 → 5 chunks

```
master-decision-hygiene/claim/003:
  "在分析特定案例之前，先看同类案例的历史统计"

master-decision-hygiene/claim/004:
  "人对具体案例的估计充满噪声，但对同类案例的基率判断更稳定"

master-decision-hygiene/procedure/003:
  "问自己：在过去5年里，有多少类似项目成功了？比例是多少？如果找不到历史数据，问行业平均成功率"

master-decision-hygiene/procedure/004:
  "把基率作为起点，再用具体案例的信息调整"

master-decision-hygiene/constraint/002:
  "陷阱：外部视角容易被'我们的项目不一样'绕过。对策：强制写出三个关键差异，再判断差异是否足以推翻基率"
```

### Step 3：独立评估 → 4 chunks

```
master-decision-hygiene/claim/005:
  "一旦知道了别人的答案，你的判断会被锚定——即使不认同，也会不自觉向中间靠拢"

master-decision-hygiene/procedure/005:
  "先分发问题清单→每人独立填写、禁止讨论→收集所有答案后再开始讨论"

master-decision-hygiene/constraint/003:
  "如果讨论前已经有人说了自己的看法，这轮独立评估已失效——必须重新来过"

master-decision-hygiene/claim/006:
  "群体智慧的数学基础：独立判断的平均值比任何一个人的判断都更准确"
```

### Step 4：聚合 → 6 chunks

```
master-decision-hygiene/procedure/006:
  "数值估计→取中位数（比平均数更抗极端值）。例：2%, 5%, 10%→中位数5%"

master-decision-hygiene/procedure/007:
  "是非判断→取多数票"

master-decision-hygiene/procedure/008:
  "排序判断→取Borda计数"

master-decision-hygiene/constraint/004:
  "聚合前没确保独立性→聚合结果仍有噪声。Step 3的独立评估必须严格执行"

master-decision-hygiene/error_data/002:
  "陷阱：中位数对极端值不敏感。如果极端值恰好包含关键信息（Taleb肥尾），中位数会丢失这些信息"

master-decision-hygiene/constraint/005:
  "重大决策建议同时看中位数和最极端的两个估计"
```

### Step 5：延迟直觉 → 4 chunks

```
master-decision-hygiene/claim/007:
  "直觉（系统1）太快、太自信、太容易被最近信息污染。延迟让系统2有机会检查系统1的结论"

master-decision-hygiene/procedure/009:
  "走完前四步后强制等待至少24小时（重大决策等1周）。等待期间不要主动想，让大脑孵化"

master-decision-hygiene/procedure/010:
  "重新审视时问：24小时前的判断，我现在还同意吗？有什么不同？"

master-decision-hygiene/claim/008:
  "你的第一反应不是你的最佳反应，只是你最快的反应"
```

### 完整流程示例 → 5 chunks（数值数据拆为独立单元）

```
master-decision-hygiene/example/001:
  "场景：团队要决定是否投资一个新项目"

master-decision-hygiene/example/002:
  "Step 1 分解数据：市场规模 A=7 B=6 C=8 / 竞争强度 A=8 B=7 C=9 / 团队能力 A=5 B=6 C=4 / 资金需求 A=3M B=5M C=4M / 执行风险 A=7 B=6 C=8"

master-decision-hygiene/example/003:
  "Step 2-4 聚合结果：市场规模中位数7，竞争强度中位数8，团队能力中位数5，资金需求中位数4M，执行风险中位数7"

master-decision-hygiene/example/004:
  "综合判断：市场规模OK，但竞争强+团队弱+风险高→不建议投资"

master-decision-hygiene/example/005:
  "Step 5 延迟验证：24小时后重新审视→如果同意就拍板，如果不同意回到Step 1找分歧来源"
```

### 关联金句 → 2 chunks

```
master-decision-hygiene/claim/009:
  "偏差是'枪总打偏'，噪声是'枪到处乱飞'。框架修的是'偏'，卫生修的是'散'"

master-decision-hygiene/claim/010:
  "先外部，后内部。先基率，后特性"
```

---

## 对比汇总

| | 假原子 (v1.1) | 真原子 (v1.3) |
|------|:---:|:---:|
| Chunk 数（同一 section） | **7** | **35** |
| 每块平均字数 | ~315 字 | **~60 字** |
| 能否独立回答 query | 部分能 | **每条都能** |
| 能否独立被反驳 | 不能 | **能** |
| AI 检索精度 | "Step 1 整段" | "Step 1 的具体做法第2条" |
| 标注粒度 | 7 块各一个视角 | **35 块各有独立视角标签** |
| 矛盾检测 | 整段对比 | **逐条对比** |

## 结论

**35 vs 7**。同一段文字，真原子切分产出的可寻址知识单元是假原子的 5 倍。这不是"多切了几刀"——是让 AI 从"找到一段混合内容"变成"精确获取单条规则并独立使用"。
