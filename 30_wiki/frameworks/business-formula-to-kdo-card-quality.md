---



id: business-formula-to-kdo-card-quality
title: 业务公式 ABC → KDO 卡片质量：用公式思维诊断知识卡的健康度
type: framework
source_refs:
- src_20260613_6edbf0af-yitang-business-formula-decomposition-notes
- src_20260613_a8bcfd38-yitang-business-formula-decomposition-oral
- src_20260613_6b939d2b-yitang-business-formula-decomposition-transcript
status: enriched
confidence: 0.8
domain:
  - yitang- kdo
  - yitang
created_at: '2026-06-15'
author: 黄药师
reviewed_by: 老顽童
review_date: '2026-06-17'
trust_level: high
related:
  - '[[case-toc-ecommerce-formula-misjudgment]]'
  - '[[proposal-yaml-frontmatter-standardization]]'
  - '[[modeling-to-kdo-toolchain]]'
  - '[[model-quality-four-levels]]'
  - '[[yt-business-formula-abc-model]]'
  - '[[yt-business-formula-abc-model]]'
  - '[[yt-business-formula-parameter-iceberg]]'
  - '[[yt-business-formula-six-level-logic]]'
  - '[[case-toc-ecommerce-formula-misjudgment]]'
  - '[[modeling-to-kdo-toolchain]]'
  - '[[modeling-three-stages]]'
  - '[[yt-research-osl-framework]]'
  - '[[concept-mckinsey-mece]]'
tags:
- '#method/evaluation-method'
- '#kdo'
- '#method/thinking-tool'
diagnostic_signals:
- signal: 我写了一张卡但不知道缺什么
  framework_lens: ABC三要素诊断
  follow_up_question: 你的A（要回答的决策问题）定义清楚了吗？B（核心主张）能量化吗？C（逻辑关系）是因果还是相关？
- signal: 我的卡看起来完整但用不起来
  framework_lens: L1-L6逻辑层级诊断
  follow_up_question: 你的卡在哪一层——模糊(L1)、相关(L2)、因果(L3)、公式(L4)、定量(L5)、还是动态(L6)？
- signal: 我的卡被3+张其他卡引用，但越引用越心虚
  framework_lens: 放量健康度诊断
  follow_up_question: 被引用次数≥3时，Synthesis出链是否≥5条？每次更新是否触发下游关联卡复查？
updated_at: '2026-06-17'

---# 业务公式 ABC → KDO 卡片质量

> **Burn line**: GMV = 线索×转化×客单价×复购 拆太粗 = 亏损。卡片质量 = id+title+type 凑齐 = 看着完整但用不了。

---

## 一、用 ABC 模型诊断一张卡

孔阳的 ABC 模型：`目标(A) = 参数(B) ⊗ 逻辑关系(C)`

**翻译到 KDO**：

| ABC 要素 | KDO 卡片对应 | 诊断问题 |
|:--|:--|:--|
| **A. 目标** | 卡片解决什么决策问题？ | 读者读完这张卡能做什么决定？ |
| **B. 参数** | Claims + source_refs | 核心主张有量化证据吗？来源可追溯吗？ |
| **C. 逻辑关系** | Synthesis + Constraints | 卡与卡之间的链接是因果、对比还是关联？边界条件写清楚了吗？ |

### 例：ToC 电商放量亏损 → 一张"看着完整但用不了"的卡

```
卡面：id 有、title 有、type 对、domain 不空 → 门禁 PASS ✅
诊断：
  A. 目标模糊      —— "帮助理解业务公式" ← 没有决策问题
  B. 参数无定量    —— Claims 没有行业基准对比（转化率 2% vs 基准 3-4%）
  C. 逻辑断裂      —— Synthesis 链接了 5 张卡但没说它们之间是因果还是对比
→ 结论：和 "GMV=线索×转化×客单价×复购" 拆太粗一样——看着对，用不了。
```

---

## 二、六层逻辑 → KDO 卡片成熟度

孔阳的 L1-L6 逻辑层级，直接映射卡片质量：

| 逻辑层 | KDO 卡片状态 | 检测方法 |
|:--|:--|:--|
| **L1 模糊** | 概念卡只有 Summary，无 Claims | TODO 残留 |
| **L2 相关** | 有 Claims 但无量化证据 | confidence < 0.5 |
| **L3 因果** | 有因果主张 + 至少 1 条 source | confidence 0.5-0.7 |
| **L4 公式** | 有完备 Claims + Constraints + 跨域链接 | confidence 0.7-0.85 |
| **L5 定量** | 有诊断信号 + 行业基准 + 反例测试 | confidence ≥ 0.85 |
| **L6 动态** | 被引用 ≥ 3 次 + 有至少一次 corrigendum 更新 | review_count ≥ 3 + has corrections |

**当前全库状态**：大部分卡在 L2-L3。王语嫣的复合卡锁在 0.65 = L3 因果。目标：核心框架卡推到 L4，决策卡推到 L5。

---

## 三、放量前必须验证——KDO 版

ToC 电商的教训：**"小规模跑通 ≠ 大规模可复制。"** KDO 的"放量"是什么？一张卡被 3+ 张其他卡引用时，它的质量缺陷会被放大。

放量前检查清单：

| 电商版 | KDO 版 |
|:--|:--|
| 转化率是否达到行业基准？ | Synthesis 出链 ≥ 5？ |
| 复购率是否支撑 LTV？ | 被引用次数 ≥ 3？ |
| 边际获客成本是否可控？ | 每次更新是否触发关联卡复查？ |

**例**：`master-decision-hygiene` 被 46 张卡引用——它已经是"放量卡"。但它的 Synthesis 有 0 条 wikilink。这就是"转化率显著低于基准但还在放量"的 KDO 版本。Detector N 已经标了它，需要限制它的引用扩散。

---

## 四、反模式对照

| 电商反模式 | KDO 反模式 |
|:--|:--|
| 把 GMV 拆成 4 个变量就以为够了 | 把卡片拆成 Summary+Claims+Synthesis 就以为完整了 |
| 转化率 2% 不知道是漏斗哪一层的问题 | 卡片用不了不知道是 A（目标不清）、B（参数不足）还是 C（逻辑断裂） |
| 首单单位模型 OK = 可以放量 | 一张卡门禁 PASS = 可以被大量引用 |
| 追加 200 万只增长 100 万 | 追加 10 张卡但互链密度没提升 |

---

## 五、每张新卡上线前做一次 ABC 诊断

```
A: 这张卡帮读者做什么决定？
   → 如果答不上来 → BLOCK，不要出草稿

B: 核心主张有量化证据吗？来源可追溯吗？
   → 如果 Claims 没有数字 → WARN，标注 confidence < 0.7

C: 链接是因果、对比还是关联？边界写清楚了吗？
   → 如果 Synthesis 全是 TODO 或 "related" → WARN，补 Constraints 表
```

已集成到 Detector S 门禁：缺 confidence → BLOCK/WARN，单信源 → WARN。

---

## 六、Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:------|
| 1. 仅诊断有 frontmatter 的 KDO 结构化卡片 | 纯文本、OCR 草稿、frontmatter 损坏卡需先修复结构，否则 ABC 三要素无法定位 |
| 2. 适用于框架/概念/决策/工具卡，轻量 skill 卡需降维 | 操作步骤卡的核心质量是 checklist 完整性，不必强行套用 L1-L6  maturity 评级 |
| 3. 诊断的是"卡片健康度"，不是"知识真理性" | 内容正确≠卡片质量好；无来源、无边界、无链接的正确知识仍会被判低质量 |
| 4. 需要 source_refs 与 confidence 字段才有诊断力 | 若卡缺失 source 或 confidence，ABC 诊断会退化为格式检查，失去定量意义 |
| 5. 批量诊断前必须先校准组织基准 | 不同团队对"高 confidence"的定量标准不同，直接跨库比较会失真 |

### 常见失败模式

| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| 1. 字段凑齐即合格 | 门禁 PASS，但读完卡仍不知该做什么决定；A（目标）缺失或写成"帮助理解 XX" | 用 Burn line 强制回答"读者能做什么决定"，写不出则回炉到 concept 阶段 |
| 2. L1-L6 当绩效排名 | 给卡贴完 L2/L3 标签就停止改进，甚至据此批评作者 | 明确 L 层级是"下一步改进方向"，同一主题应规划 L4→L5 的升级路径 |
| 3. 无 Claims 先堆链接 | Synthesis 里列了 8 条“双括号占位链接”，但都是目录式关联，无因果/对比说明 | 先补 B（参数/主张）与证据，再写 C（链接）；链接必须带"因为…所以…"或"与之相反" |
| 4. 单信源强行高 confidence | confidence 0.9+，但 source_refs 只有 1 个且无定量 claim | confidence ≥0.85 必须 ≥2 个独立来源 + 至少 1 条带数字的 claim |
| 5. 机械套用"放量"阈值 | 被引用 3 次就视为核心卡继续向外推荐，结果缺陷被放大 | 检查引用是否为 genuine synthesis；非 genuine 则先修复或加"引用风险提示" |

---

## 七、模板：KDO 卡片 ABC 诊断报告

```
卡片 ID: _____________
诊断日期: _____________
诊断人:   _____________

A. 目标（决策问题）
   [ ] 能一句话说出读者读完能做什么决定：________________________
   [ ] 若答不上来 → BLOCK，回到 concept 阶段

B. 参数（Claims + 来源）
   [ ] 至少一条带数字的 claim：________________________
   [ ] 来源可追溯到 source_id：________________________
   [ ] 有行业基准 / 反例 / 边界：________________________

C. 逻辑关系（Synthesis + Constraints）
   [ ] 每条相关链接说明因果 / 对比 / 关联：________________________
   [ ] Constraints & Boundaries ≥4 条：________________________
   [ ] Common Failure Modes ≥4 条且含症状+修复：________________________

成熟度判定：L__ / L6
放量检查：被引用 __ 次 | Synthesis 出链 __ 条 | 下游复查记录 __ 条
下一步升级动作：________________________
```

**示例**：对 `yt-business-formula-abc-model` 的诊断
- **A**：帮读者判断"业务公式拆解是否到位"
- **B**：claim "GMV = 线索 × 转化 × 客单价 × 复购" 过于粗糙；需补充行业基准转化率 3-4%
- **C**：与 `yt-business-formula-parameter-iceberg` 是递进关系；与 `case-toc-ecommerce-formula-misjudgment` 是反例关系

---

## 八、对老顽童写卡的具体建议

1. **每张卡开头加一句"Burn line"**——这张卡帮读者做什么决定。这就是 ABC 的 A。
2. **Claims 至少要有一条带数字。** 不是"转化率需要提升"，是"转化率 2% vs 行业基准 3-4%，差距 1-2 个百分点"。
3. **放量前自查**：这张卡被 3+ 张卡引用时，Synthesis 够不够 5 条出链？

---

黄药师 · 2026-06-15 初稿 · 老顽童 2026-06-17 精修 · 基于孔阳业务公式 ABC 模型 + KDO 门禁体系

---

## 单卡收尾检查

- [x] status：`enriched`
- [x] reviewed_by：`老顽童`
- [x] updated_at：`2026-06-17`
- [x] diagnostic_signals：3 条（≥3）
- [x] Constraints & Boundaries：5 条适用边界（≥4）
- [x] Common Failure Modes：5 条，含真实症状 + 可执行修复（≥4）
- [x] 新增案例/模板：`KDO 卡片 ABC 诊断报告`模板 + `yt-business-formula-abc-model` 诊断示例
- [x] 新增互链：`[[yt-research-osl-framework]]`、`[[concept-mckinsey-mece]]`（共 2 条新互链）
- [x] 质量门禁：单卡无新增 P0/P1
