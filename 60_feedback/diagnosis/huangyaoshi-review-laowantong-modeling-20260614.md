# 黄药师审查：老顽童 高阶建模域

> 批次：modeling domain，7 张卡（1 framework + 1 concept + 1 tool + 4 dk）
> 审查日期：2026-06-14

## 一、清单

| 卡 | 类型 | 位置 | confidence | source | wikilinks |
|:--|:--|:--|:--:|:--:|:--:|
| modeling-three-stages | framework | frameworks/ | ✅ 0.75 | ✅ 3 | ✅ 8 |
| modeling-capability-system | concept | concepts/ | ✅ 0.75 | ✅ 3 | ✅ 4 |
| modeling-level-map | tool | tools/ | ✅ 0.75 | ✅ 3 | ✅ 5 |
| dk-modeling-ai-without-judgment | dark-knowledge | dark-knowledges/ | ❌ missing | ✅ | — |
| dk-modeling-counterexample-driven | dark-knowledge | dark-knowledges/ | ❌ missing | ✅ | — |
| dk-modeling-essence-predictive | dark-knowledge | dark-knowledges/ | ❌ missing | ✅ | — |
| dk-modeling-sop-execution-locks | dark-knowledge | dark-knowledges/ | ❌ missing | ✅ | — |

## 二、好的一面

### 2.1 Claims 有源引

每一条 Claim 都带了源文件的具体行号引用：

```
C1 [conf=0.9]: 流程类建模针对具体、固定的业务场景...
→ src_20260614_42f1e977-一堂-建模能力培训-truman-笔记.md:32-37
```

之前 AI 短剧批次的 L3 验证引用虚——但这一批的 Claims 引用是实的。行号精确到原文位置，可复核。

### 2.2 Open Questions 有攻击性

不是装饰性的"TODO"，是真正的反问：

- "三阶段的分数标签（60/75/85）是否具有实际测量意义，还是仅为教学比喻？" — 质疑了框架本身的前提
- "是否存在'反本质提炼'的场景？过早提炼本质是否会固化错误认知？" — 在框架最核心处找漏洞

这两个问题如果让 Kahneman 来问，问法差不多。

### 2.3 框架结构层层递进

三段论 → 能力体系 → 段位地图 → 4 张暗知识（分别针对"AI 无判断""反例驱动""伪本质""SOP 锁死"四个坑）。知识链完整：是什么 → 怎么学 → 哪里容易踩。

### 2.4 整体质量

这是老顽童**第一个 A 级内容批次**。比 AI 短剧批更高——短剧批是方法论的忠实转译，这批次是理解后的结构重建。Constraints 表、Reusable Knowledge 决策树、Open Questions 攻击性——三个指标全过线。

## 三、待修

1. **4 张 dk 卡缺 confidence** → 入库门禁会 BLOCK。补上。
2. **dk-* 的 frontmatter 格式不一致** — `dk-modeling-essence-predictive` 用了带引号的 YAML 字符串，`dk-modeling-sop-execution-locks` 的 `source_person` 是 `Truman` 而其他卡是 `老顽童`。统一一下。

## 四、定级

**A-**。内容 A，格式 B+（dk 卡缺 confidence）。补上就 A。

---

黄药师  
2026-06-14

---

## 补充审查：素材消化完整度（用户反馈后）

口述稿 4461 行。老顽童产了 7 张卡。以下三块高价值内容未被提取：

### 遗漏 1：迭代递归深挖法（第 448-668 行）

Truman 完整讲述了直播 SOP 三年迭代历程——从 0 到 10 条到 50 条，每条规则怎么来的、什么场景触发的修改、为什么某些规则被废弃。这是"高阶建模"最核心的方法论现场演示。**当前无卡对应。**

建议出：`case-truman-livestream-sop-iteration`（案例卡）或 `method-iterative-recursive-deepening`（方法论卡）。

### 遗漏 2：AI Skills 工程指南产出过程（第 1194-1226 行）

Truman 完整讲了如何让 AI 封装一个 design case skill——把反馈全部喂给 AI → AI 扫描合并同类项 → 生成场景、审美底盘、协作流程、track list、评审表。**这是"人-AI 协作建模"的实战指南，价值极高。当前无卡对应。**

建议出：`method-ai-skill-packaging-from-feedback`（方法论卡）。

### 遗漏 3：做客流程案例（第 1448 行起）

Truman 说"过去没有完整分享过"的讲师遴选质控流程。首次公开的内部 case。**当前无卡对应。**

建议出：`case-truman-lecturer-selection-modeling`（案例卡）。

### 结构性缺失

- **案例层空白**：16 个 source 文件中标注了 6 个案例（抽象建模案例 ×2、本质建模案例 ×2、流程建模开播准备、个人地图案例），没有一个被提取为 case 卡。
- **素材利用率**：7 张卡 vs 4461 行 + 16 个 source，提取率偏低。

### 修正定级

框架层 A-，案例层 F，方法论实操层 F。**综合 B**——不是写得不好，是没写够。源材料里的核心资产没被识别。
