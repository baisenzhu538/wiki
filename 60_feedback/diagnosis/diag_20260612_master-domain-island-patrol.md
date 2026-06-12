---
title: master 域孤岛巡查报告
diagnostician: 王语嫣
date: 2026-06-12
type: diagnosis
domain: ["master", "yitang"]
source: 全库 related/wiki_refs 关联分析 + 7 张 master 卡 frontmatter 抽查
---

# master 域孤岛巡查报告

> **任务来源**：`70_product/tasks/wangyuyan-next-tasks.md`
> **前置诊断**：`kdo-concept-map-20260612.md`（发现 master 域 61 张卡中 54 张单 domain，88.5% 孤岛）
> **本次聚焦**：桥接卡（MECE/Issue Tree/7-S/Hypothesis-Driven/5 Whys）量产后的**引用变化**

---

## 一、master 域当前状态

| 指标 | 数值 |
|:-----|:----:|
| master 卡总数 | **7 张**（截至 06-12） |
| 有完整 related 字段的 master 卡 | 6 / 7（antifragile 的 related 为空字符串） |
| master 卡 related 中引用 yt- 的 | 6 / 7（仅 antifragile 缺） |
| yt- 卡中引用 master 的 | **8 / 238**（3.4%） |
| 平均每个 master 卡被 yitang 引用的 yt- 数 | **2.1** |

**结论**：master 卡向下桥接到 yt- 的情况明显改善了，但存在严重不均衡。

---

## 二、各 master 卡的连接详情

### 2.1 桥接密度分级

| Master 卡 | 向下引 yt- (related) | 被 yt- 引用 | 净连接度 | 等级 |
|:----------|:-------------------:|:----------:|:--------:|:----:|
| **master-knowledge-compound** | 5 个 yt- | **6 个 yt- 引用** | 11 | ✅ 活跃桥接 |
| **master-decision-hygiene** | 4 个 yt- | **5 个 yt- 引用** | 9 | ✅ 活跃桥接 |
| **master-first-principles** | 6 个 yt- | **1 个 yt- 引用** | 7 | 🟡 单向桥接 |
| **master-systems-thinking** | 8 个 yt- | **1 个 yt- 引用** | 9 | 🟡 单向桥接 |
| **master-cognitive-bias-checklist** | 3 个 yt- | **2 个 yt- 引用** | 5 | 🟡 弱桥接 |
| **master-ai-info-literacy** | 4 个 yt- | **0 个 yt- 引用** | 4 | 🔴 绝对孤岛 |
| **master-antifragile-checklist** | **0**（related: ""） | **0 个 yt- 引用** | **0** | 🔴 完全孤岛 |

### 2.2 关键发现

**活跃桥接的 2 张**（knowledge-compound + decision-hygiene）——是**管理工具域**在主动引用。yt-tool-strategy-workshop、yt-tool-okr-cycle、yt-tool-meeting-designer、yt-tool-hiring-scorecard、yt-tool-knowledge-extraction 这 5 张管理工具卡已经形成了"tool → master 双向链"的模式。**管理域是桥接的先行者。**

**绝对孤岛的 2 张**（ai-info-literacy + antifragile-checklist）：
- `master-ai-info-literacy`：向下有 related（4 个 yt-），但**没有任何 yt- 卡引用回去**。反向链断裂。
- `master-antifragile-checklist`：related 字段为空字符串，没有任何向外或向内的连接。完全孤岛。

**单向桥接的有 3 张**：
- first-principles 和 systems-thinking 都在 related 中引用了大量 yt- 卡（6 个和 8 个），但 yt- 卡几乎不引用回来（各 1 个）。这些是"master 在向 yitang 伸手，但 yitang 没接"的状态。

---

## 三、与 design 域对比（上次是绝对孤岛）

| 维度 | design 域（上一轮） | master 域（本轮） |
|:-----|:----------------:|:----------------:|
| 孤岛状态 | **绝对孤岛**——32 张卡全部单 domain，零跨域引用 | **部分桥接**——7 张卡中 5 张有桥接 |
| 最严重问题 | 无 domain 标签、无 related 字段 | 2 张完全孤岛 + 3 张单向桥接 |
| 根因 | 标签策略偏差（dk-yb 卡全部标 design 但 yt- 没标注） | 生产规范问题（antifragile related 为空，bridge 卡完成后 yt- 端未更新） |
| 修复进展 | ✅ 老顽童已补 P0+P1 共 9 对桥接 | ❌ 未开始 |

**判断**：master 域比 design 域好得多。design 是"0 连接"，master 是"5/7 有连接但 2/7 为 0 + 3/7 单向"。不是重灾区，但有明确需要修补的缺口。

---

## 四、P0 桥接建议

### P0-1：master-antifragile-checklist 的 related 为空

**问题**：`related: ""`（空字符串），等于不存在。这张卡既没引用任何人，也没人引用它。

**建议**：补 related 数组，至少 3-5 条：
- 与 decision-hygiene 的互补关系（后者管过程，前者管策略）
- 与 cognitive-bias-checklist 的先后使用顺序
- 与 yt-entrepreneur-barriers / yt-foresight-ten-fatal-flaws 等业务域卡的关系

**适合谁**：老顽童（补内容，不动 frontmatter 格式）

### P0-2：master-ai-info-literacy 反向链为 0

**问题**：这张 master 卡向下有 4 个 related 指向 yt-（research-cognition / prompt-engineering / ai-capability / y-model），但没有任何 yt- 卡在 frontmatter 或 body 中引用它。

**建议**：在以下 yt- 卡中补反向 related 和 body wikilink：
- `yt-entrepreneur-research-cognition`（调研认知→AI 信息素养，直接重叠）
- `yt-model-prompt-engineering`（提示词工程→信息素养，互补）
- `yt-personal-ai-capability`（AI 能力→信息素养，前提）
- `yt-research-weaponry-course`（武器库→信息素养，调研场景）

**适合谁**：老顽童（补 related + wiki_refs）

### P0-3：first-principles 和 systems-thinking 的反向链过弱

**问题**：这两张是 master 域最核心的元框架。downward related 做得很好（6 个和 8 个），但 yt- 回过头来引它们的极少（各 1 个）。3.4% 的引用率意味着**master 卡被看到了，但没有被当成"工具"来用**。

**建议**：在 yt-personal-y-model-*、yt-panproduct-execution-*、yt-unit-model-* 等已经出现在 related 中的卡，在 body 中主动加 `[[master-first-principles]]` / `[[master-systems-thinking]]` 引用。

**适合谁**：老顽童或洪七公（跨卡补 wiki_refs，批量操作）

---

## 五、执行建议

| # | 修复项 | 影响范围 | 负责人 | 预估 | 优先级 |
|:-:|:-------|:--------|:------|:----:|:----:|
| 1 | antifragile 补 related 数组 | 1 张 master 卡 | 老顽童 | 15min | P0 |
| 2 | ai-info-literacy 补反向链（4 张 yt-） | 4 张 yt- 卡 | 老顽童 | 20min | P0 |
| 3 | first-principles / systems-thinking 反向链补强（6-8 张 yt-） | 6-8 张 yt- 卡 | 老顽童/洪七公 | 30min | P1 |
| 4 | 在自迭代检测器 C（桥接机会）中增加"单向桥接"信号 | 1 条检测规则 | 黄药师 | — | P2 |

**注意**：master 域不是重灾区。比 design 域好很多，但 2/7 的卡完全孤岛 + 3/7 单向桥接说明**桥接工作只完成了一半**——downward related（master→yt-）在批量生成时已经被填了，但 upward 引用（yt-→master）漏了。这是批量写卡流程的规范缺口，不是知识缺口。

---

## 六、核心判断

> **master 域桥接状况：比上不足，比下有余。**
> 
> 相比 design 域曾经的"0 连接"，master 域有 71% 的卡在向下连接，但只有 43% 的卡有双向连接。问题不是"桥断了"，而是"单向桥还没变成双向"。
> 
> 修复成本很低——每张 yt- 卡加一行 `- [[master-xxx]]` 即可。真正的门槛是**生产流程要让"补引用"成为发布的必经步骤**，而不是事后补。

---

*本诊断不修改 30_wiki/ 下任何文件。*
