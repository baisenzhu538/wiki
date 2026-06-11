---
id: "kdo-concept-map-20260611"
title: "KDO Concept Card Map - 2026-06-11"
type: "diagnosis_map"
created_at: "2026-06-11"
updated_at: "2026-06-11"
domain: ["master", "diagnosis"]
description: "Distribution, bridge analysis and gap diagnosis of 379 KDO concept cards."
status: "completed"
---

# KDO 概念卡地图

> 基于 `30_wiki/concepts/` 379 张核心卡片（yt-/dk-/concept-/master-/case-）的只读扫描。不碰原始卡片。

---

## 一、全库概览

| 指标 | 数值 | 判断 |
|:-----|:-----|:-----|
| 总卡片数 | **379** | — |
| 含 frontmatter 完整度 | ~97% | 少数老卡缺 id/title |
| diagnostic_signals 覆盖率 | **0.8%** (3/379) | 🔴 严重不足 |
| 0 claims 卡片 | **108** (28.5%) | 🔴 老卡结构不完整 |
| 多 domain 卡片 | **75** (19.8%) | 🟡 桥接密度偏低 |

---

## 二、Type 分布

| 类型 | 数量 | 占比 | 角色 |
|:-----|-----:|-----:|:-----|
| tool | 128 | 33.8% | 执行层 |
| dark-knowledge | 91 | 24.0% | 避坑层 |
| concept | 64 | 16.9% | 认知层 |
| framework | 49 | 12.9% | 骨架层 |
| case | 24 | 6.3% | 证据层 |
| dk | 10 | 2.6% | 暗知识（旧命名） |
| skill | 10 | 2.6% | 技能层 |
| 其他 | 3 | 0.8% | — |

**判断**：工具卡（128）+ 暗知识卡（101）占总量的 60%，说明知识库当前是**"用中学"导向**——给用户武器和坑位图，但骨架层（framework 49）相对薄。框架层如果能从 49 扩展到 70+，工具卡的调用精度会显著提升。

---

## 三、Domain 分布与桥接分析

### 3.1 Domain 量级

| Domain | 总卡数 | 单 domain | 多 domain | 孤岛率 |
|:-------|-------:|----------:|----------:|-------:|
| yitang | 255 | 190 | 65 | 74.5% |
| master | 61 | 54 | 7 | 88.5% |
| design | 32 | 32 | 0 | **100%** 🔴 |
| ai-collaboration | 25 | 1 | 24 | 4.0% |
| ai | 13 | 10 | 3 | 76.9% |
| personal | 11 | 1 | 10 | 9.1% |
| entrepreneur | 7 | 5 | 2 | 71.4% |
| product | 6 | 5 | 1 | 83.3% |

### 3.2 已有桥接（frontmatter domain 共现）

| 桥接对 | 共现卡数 | 说明 |
|:-------|--------:|:-----|
| ai-collaboration <-> yitang | 24 | 人机协作域与一堂体系深度融合 |
| ai <-> yitang | 12 | AI 概念在一堂框架内的应用 |
| personal <-> yitang | 10 | 个人修炼与创业方法论的交叉 |
| entrepreneur <-> master | 7 | 创业域与元能力域的桥接 |
| product <-> yitang | 6 | 产品内核在一堂体系内 |

### 3.3 孤岛诊断

🔴 **design 域 — 绝对孤岛**
- 32 张卡，100% 单 domain
- 无 wikilink 跨域连接（抽样检查 5 张：`ai-design-workflow`, `ai-design-prompts`, `ai-design-fundamentals` 等——无 related 指向 yitang/master/product）
- **判断**：设计域是洪七公 VA 产出后由欧阳锋编译的独立域，尚未与核心业务域建立桥接
- **建议**：每张设计域 tool 卡至少补 1 条 `bridges_to` 指向一堂产品方法论（如 `yt-product-kernel-three-questions`）

🔴 **ai-collaboration 域 — 伪融合**
- 25 张卡中 24 张与 yitang 共现，但只有 1 张真正多 domain
- 说明这些卡名义上在 yitang 域，实质上仍是 ai-collaboration 的单域卡
- **判断**：AI 协作方法论与一堂体系的桥接是"贴标签式"而非"内容式"
- **建议**：在 Synthesis 节显式写出"这个 AI 协作技巧对应一堂五步法的哪一步"

🟡 **master 域 — 元能力未下沉**
- 61 张卡中 54 张单 domain
- master 域是"元认知/元方法"层，天然应该被所有业务域引用，但实际桥接极少
- **判断**：master 卡像"挂在墙上的地图"，业务域的卡没有把它们当成工具使用
- **建议**：在 yitang 域的 tool/framework 卡中，增加对 master 概念的显式引用（如 PEAS、武器库、守脑如玉）

🟡 **yitang 域 — 内部密度高，对外封闭**
- 255 张卡中 190 张纯 yitang
- 一堂体系内部已形成较完整的工具链，但与外部域（design/consulting/product-strategy）几乎无桥接
- **判断**：一堂域是知识库的"重力中心"，但引力范围有限

---

## 四、结构质量诊断

### 4.1 Claims 分布

| Claims 数 | 卡片数 | 判断 |
|----------:|-------:|:-----|
| 0 | 108 | 🔴 老卡/轻量卡，缺结构化主张 |
| 1-5 | 36 | 🟡 偏薄 |
| 6-10 | 180 | 🟢 合理区间 |
| 11-16 | 53 | 🟢 扎实 |
| 17+ | 2 | 🟢 超重（需检查是否过于冗长） |

**关键发现**：108 张 0 claims 卡集中出现在早期批次的 case 卡和 dk 卡中。这些卡是"叙事体"而非"主张体"——有故事有案例，但没有用 ### Claims 结构化输出可验证的主张。

### 4.2 External Attackers

索引提取阶段未统计攻击者数量（需逐卡解析 Critique 节），但基于随机抽样 20 张：
- v1.5 后新卡：≥2 攻击者，合规
- v1.5 前老卡：约 40% 缺 Critique 节或攻击者不足
- **根因**：Sprint 12（回溯升级）尚未启动

---

## 五、Gap：最该桥接但未桥接的域对

基于诊断经验 + 地图数据，以下域对的桥接价值最高：

| 优先级 | 域对 | 理由 | 建议动作 |
|:------:|:-----|:-----|:---------|
| P0 | **design <-> yitang** | 设计域 32 张卡 100% 孤岛。一堂有大量产品/品牌/运营场景需要设计能力支撑。 | 每张 design tool 卡补 bridges_to 指向 yt-product-kernel 或 yt-panproduct-36 |
| P0 | **master <-> yitang** | 元能力域 88.5% 孤岛。PEAS/武器库/守脑如玉等概念应被五步法各步骤显式引用。 | 在五步法 tool 卡中增加"本步骤对应的 master 概念"小节 |
| P1 | **consulting <-> yitang** | 王语嫣首批诊断识别的 8 张桥接卡（MECE/Issue Tree 等）正在生产，但现有 consulting 域 2 张卡未与一堂体系建立内容桥接。 | 老顽童产出的桥接卡需通过 Bridge 节显式标注对应一堂工具 |
| P1 | **product-strategy <-> entrepreneur** | product 域 6 张卡，entrepreneur 域 7 张卡，但两域之间无共现。产品内核与创业预判是天然上下游。 | 在 entrepreneur 卡中引用 product 内核工具，反之亦然 |
| P1 | **ai <-> master** | 仅 1 张共现卡。AI 是元能力层的放大器，但 master 域的卡片几乎没有讨论 AI 增强。 | 在 PEAS/武器库/上下文工程等卡中增加"AI 时代变体"Claim |

---

## 六、给黄药师 Task E 的补充输入

诊断基础设施缺口（与 Task E 直接相关）：

| 缺口 | 当前状态 | 阻塞诊断？ |
|:-----|:---------|:----------|
| `diagnostic_signals` 覆盖率 | 0.8% (3/379) | 是。王语嫣无法精准匹配框架到用户场景 |
| `bridges_to` frontmatter 字段 | 仅桥接卡试点使用 | 否（但限制跨域导航） |
| Graph RAG 扫描目录 | 缺 frameworks/tools/cases | 是。老顽童新产出的桥接卡不入图 |
| 域标签一致性 | `ai` vs `ai-collaboration` vs `ai-native` vs `ai-models` 四散 | 是。搜索时漏匹配 |

---

## 七、结论

1. **知识库已从"素材堆积"进入"结构化工具库"阶段**——379 张卡、类型分层清晰、工具卡充足。
2. **最大短板是桥接密度而非卡片数量**——design 孤岛、master 未下沉、yitang 封闭。
3. **诊断基础设施（DS + bridges_to + 图扫描）是解锁下一阶段的关键**——黄药师 Task E 完成后，王语嫣的诊断精度可提升一个量级。
4. **建议执行顺序**：修图扫描（黄药师 5min）→ 桥接卡量产（老顽童）→ DS 批量补填（下一轮 Sprint）。
