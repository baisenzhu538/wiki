---
title: master 域孤岛巡查报告
diagnostician: 王语嫣
date: 2026-06-12
type: diagnosis
domain: master
supersedes: prev-master-analysis
---

# master 域孤岛巡查报告

## 一、现状总览

| master 卡 | domain | related 有值? | 链接到 yitang | 被 yt- 引用 | 桥接状态 |
|:----------|:------:|:------------:|:-------------:|:----------:|:--------:|
| master-first-principles | master | ✅ 7条 | 7张 yt- 卡 | 2张 | 🟡 弱双向 |
| master-systems-thinking | master | ✅ 6条 | 4张 yt- 卡 | 1张 | 🟡 弱 |
| master-decision-hygiene | master | ✅ 7条 | 4张 yt- 卡 | **8张** | ✅ 强双向 |
| master-cognitive-bias-checklist | master | ✅ 8条 | 5张 yt- 卡 | **3张** | 🟡 中等 |
| master-knowledge-compound | master | ✅ 5条 | 3张 yt- 卡 | **8张** | ✅ 强双向 |
| **master-antifragile-checklist** | master | **❌ 空字符串** | 0条 | **0张** | 🔴 完全孤岛 |
| **master-ai-info-literacy** | master | ✅ 5条 | 5张 yt- 卡 | **0张** | 🔴 单向出 |

### 关键指标

| 指标 | 数值 | 解读 |
|:-----|:----|:------|
| master 卡总数 | 7 张 | 卡片本身深度足够（每张 1000-1600 tokens） |
| 有 related 的 | 6/7 | antifragile-checklist 的 related 为空字符串 |
| 引用 yitang 卡 | 6/7 | ai-info-literacy 无反向引用（但出链完整） |
| **被 yt- 引用的** | **5/7** | 2 张完全没人引用 |
| 引用 master 的 yt- 卡数 | 仅 **8 张**（3.4%） | 238 张 yt- 卡中只有 8 张 |
| 8 张引用的分布 | 全在 yt-tool-* + yt-management-* 域 | entrepreneur / foresight / panproduct 域完全不引用 master |

### 与 design 域对比

| 维度 | design 域（上次） | master 域（本轮） |
|:-----|:-----------------|:------------------|
| 卡数 | 40 | 7 |
| domain 标签 | 完全无 domain 标签 | 全部有 domain: master |
| related 字段 | 部分缺失 | 6/7 有 |
| 被其他域引用 | **0 张** | **5/7 张被引用** |
| 完全孤岛 | 100% | 29%（2/7） |

**结论**：master 域 **比 design 域好得多**——至少 5/7 张卡已经被 yitang 域发现并使用了。但好得不够。

---

## 二、真实缺口

### Gap 1：master-antifragile-checklist 完全孤岛

`related: ""` — 空字符串而非数组。不仅没有任何 related 链接，这个字段的格式也不对（应该是 YAML list）。

被引用数：**0**。238 张 yt- 卡中没有任何卡引用反脆弱清单。

**根因推测**：antifragile 是一堂课程中较少涉及的域（Nassim Taleb 的内容），不直接对应一堂的任何方法论。所以编卡时没有自然的链接锚点。

**建议**：
- 为 master-antifragile-checklist 补充 related（至少链接到 yt-decision-review、yt-decision-y-model、yt-foresight-probability-engineering 等决策类卡片）
- `related:` 格式修正（空字符串 → YAML list 或删除）

### Gap 2：master-ai-info-literacy 出链完整但无人回链

5 条出链指向 yitang 卡（research-cognition、prompt-engineering、ai-capability 等），但没有一条回链。

**说明**：master → yt 的出链已经由编卡者建立，但 yt → master 的反向引用未在 yt- 卡 pr（批量升级 Sprint）中补充。

**建议**：
- 在 5 张目标 yt- 卡中补充 `related: master-ai-info-literacy`

### Gap 3：桥接集中在工具/管理域，创业/预判/泛产品域完全没有

8 张引用 master 的 yt- 卡分布：

```
yt-tool-hiring-scorecard          yt-tool-meeting-designer
yt-tool-okr-cycle                 yt-tool-strategy-workshop
yt-tool-knowledge-extraction      yt-tool-mental-model-refinement
yt-management-toolkit-overview    yt-foresight-15-char-mantra
```

完全没有引用的域：**panproduct（33 张）、entrepreneur（23 张）、model（32 张）、personal（22 张）**。

**这意味着**：当创业者用 `kdo query` 搜索"第一性原理"或"系统思考"时，返回的 master 卡不会出现在他们的工具路径中。

### Gap 4：master-decision-hygiene 和 master-knowledge-compound 是明星卡

这两个被 8 张 yt- 卡引用——证明 master → yitang 桥接可以成功。但参考他们建立桥接的方式（决策卫生 → 决策卡片，知识复利 → 个人学习卡片），可以用同样的模式推广到其他 master 卡。

---

## 三、P0 桥接建议

| 优先级 | 动作 | 预期影响 |
|:------:|:-----|:---------|
| **P0** | master-antifragile-checklist 补 related + 格式修复 | 从 0→至少 4 条出链 |
| **P0** | 5 张 yt- 卡补 `related: master-ai-info-literacy` | 从 0→5 条回链 |
| **P1** | 创业修链域 top 卡（yt-entrepreneur-liberate-thinking、yt-entrepreneur-five-step-method）引用 master-first-principles | 从 2→5 |
| **P1** | yt-panproduct-* 中的核心卡引用 master-systems-thinking | 从 1→5 |
| **P2** | 全线 yt- 卡批量补充 master 引用（通过脚本扫描 `related` 相似性） | 覆盖 238 张 |

---

## 四、与上次 design 域诊断的对比总结

```
上次（design 域）：40 张卡，0 domain 标签，0 条跨域链接
  → 方案：补 domain + 补 related + 建桥

本轮（master 域）：7 张卡，全部有 domain，但 2 张完全孤岛
  → 方案：补 2 张孤岛卡的 related + 补 5 条反向链接
```

**master 域的问题比 design 域轻得多**。不需要大规模重建，只需要修复 `antifragile-checklist` 的格式错误 + 补 5 条反向链接。

---

## 五、诊断元数据

- **扫描范围**：7 张 master 卡 → related 出链 + yt- 反向引用 + 格式检查
- **发现形式**：格式错误 1 处（antifragile-checklist.related），孤岛 2 张，单向出链 1 张
- **置信度**：高（全部 7 张已逐张核验）
- **处理**：建议由老顽童在 15min 内完成修复
