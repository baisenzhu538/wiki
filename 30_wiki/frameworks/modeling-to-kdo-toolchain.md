---

id: modeling-to-kdo-toolchain
title: 建模三段论 → KDO 工具链映射：从 SOP 到本质的知识管理落地
type: framework
source_refs:
  - src_20260614_8269ccdb-一堂-建模能力培训-truman-口述
  - src_20260614_42f1e977-一堂-建模能力培训-truman-笔记
  - src_20260614_623cfbfd-高阶建模-流程建模
status: enriched
confidence: 0.8
domain:
- kdo
- yitang
created_at: '2026-06-14'
author: 黄药师
reviewed_by: 老顽童
review_date: '2026-06-14'
trust_level: high
related:
- '[[modeling-capability-for-kdo]]'
- '[[modeling-three-stages]]'
- '[[modeling-capability-system]]'
- '[[modeling-level-map]]'
- '[[dk-modeling-ai-without-judgment]]'
- '[[case-纪浩-from-zip-to-five-layers]]'
tags:
- '#method/modeling'
- '#kdo'
- '#method/thinking-tool'
- '#method/execution-method'
diagnostic_signals:
- signal: 我写了一张卡但不知道怎么验证它够不够好
  framework_lens: 三段论门禁映射
  follow_up_question: 你的卡处于L3（流程）、L4（抽象）还是L5（本质）？对应的门禁标准不同。
- signal: 素材进了inbox不知道怎么推进到wiki
  framework_lens: KDO管线五阶段
  follow_up_question: 素材是P0/P1/P2哪个级别？P0走王语嫣门禁，P2老顽童直接消化。
- signal: AI生成的框架看起来完整，但落地时每个场景都要临时打补丁
  framework_lens: 人在环中建模五步法
  follow_up_question: AI输出是否经过边界定义、挑错、上锁、撞击实验？缺少哪一步？
- signal: 团队争论"本质"而基础动作反复出错
  framework_lens: 阶段不可跳级
  follow_up_question: 当前是否有执行稳定的SOP/清单？执行率达到90%以上再进入抽象建模。
updated_at: '2026-06-17'
---
# 建模三段论 → KDO 工具链映射

> **Burn line**: 建模不是抽象概念——每个阶段都有对应的 KDO 命令和检查项。

---

## 一、阶段对应

| Truman 建模阶段 | 分数 | KDO 管线阶段 | 核心命令 | 质量门 |
|:--|:--:|:--|:--|:--|
| **流程建模** | 60 | `60_feedback` → `30_wiki/concepts/` | `kdo scaffold --new tool` | 执行率、TODO清理 |
| **抽象建模** | 75 | `30_wiki/frameworks/` | `kdo scaffold --new framework` | 跨域链接、Synthesis ≥5 wikilinks |
| **本质提炼** | 85 | `30_wiki/decisions/` | `kdo scaffold --new concept` | 可推导性、可证伪性 |

---

## 二、流程建模 → KDO（L3: 60分）

```
"这个任务高频重复吗？→ 是 → 做SOP/Checklist"
```

**KDO 对应**：

| Truman 动作 | KDO 命令/检查 |
|:--|:--|
| 写 checklist / SOP | `kdo scaffold --new tool --topic "XX清单"` |
| 标注执行率 | `status: enriched` → `status: stable`（跟踪使用次数） |
| 复盘 → 补丁 | `kdo lint` 发现断裂 → `kdo scaffold --card <id>` 修补 |
| 专人执行SOP | `60_feedback/inbox-queue/` → 王语嫣 cron 自动分配 |

**门禁**：

| 检查项 | 标准 |
|:--|:--|
| TODO清理 | 0个残留TODO（纯执行文档不应有TODO） |
| 可执行性 | 每一步有具体动作词（"打开X → 检查Y → 记录Z"） |
| 迭代痕迹 | `source_refs` 中包含至少一条反馈记录 |

**例**：药柜选址四步法 `method-medical-cabinet-site-selection.md` = L3 流程建模。

---

## 三、抽象建模 → KDO（L4: 75分）

```
"这个问题跨场景出现吗？→ 是 → 抽象模型/方法论"
```

**KDO 对应**：

| Truman 动作 | KDO 命令/检查 |
|:--|:--|
| 提炼方法论 | `kdo scaffold --new framework --topic "XX方法论"` |
| 案例验证 | source_refs ≥ 3，至少含1个反例 |
| 武器库建立 | `related` 链接 ≥ 5 张卡 |
| 跨域迁移 | `bridges_to` 非空（至少跨1个域） |

**门禁**：

| 检查项 | 标准 |
|:--|:--|
| Synthesis 出链 | ≥ 5 wikilinks |
| 有反例 | `Constraints` 表中至少1行标注"反例/失效场景" |
| diagnostic_signals | 至少2条，有具体场景+追问 |
| 置信度 | `confidence ≥ 0.7` |

**例**：建模三段论 `modeling-three-stages` = L4 抽象建模。有阶段定义、典型错误、决策树。

---

## 四、本质提炼 → KDO（L5: 85分）

```
"这涉及战略/底层判断吗？→ 是 → 本质提炼"
```

**KDO 对应**：

| Truman 动作 | KDO 命令/检查 |
|:--|:--|
| 本质要素 | `type: decision`（不放入 concepts/，放 decisions/） |
| 可推导性测试 | 用 `kdo query` 搜索跨域验证 |
| 学科经典对标 | `bridges_to` 链接到外部理论框架 |
| 五个为什么 | `Open Questions` 节前3条必须为自反性问题 |

**门禁**：

| 检查项 | 标准 |
|:--|:--|
| 可推导性 | Claims 中至少1条可以从底层要素推导出上层结论 |
| 跨域验证 | `bridges_to` 跨 ≥ 2 个域 |
| 自反性 | Open Questions 必须包含"这个本质在什么条件下会不成立" |
| 置信度 | `confidence ≥ 0.8`，多信源验证 |

**例**：王语嫣的"强监管、低频消费、线下履约类项目的认知偏差模式" = L5 本质提炼。从药柜提取的底层模式，可迁移到金融、教育、医疗AI。

---

## 五、决策：什么时候用哪个阶段？

```
任务高频重复？ ──是→ L3 流程建模 (tool/checklist)
    │否
    ↓
问题跨场景出现？ ──是→ L4 抽象建模 (framework/methodology)
    │否
    ↓
涉及战略/底层判断？ ──是→ L5 本质提炼 (decision)
    │否
    ↓
保持经验沉淀，不进 wiki（留 inbox 或 60_feedback）
```

**KDO 的命令选择**：

```bash
# L3: 具体操作流程
kdo scaffold --new tool --topic "XX操作清单" --domain yitang

# L4: 可迁移方法论
kdo scaffold --new framework --topic "XX方法论" --domain yitang,product

# L5: 路线决策
kdo scaffold --new concept --topic "XX本质提炼" --domain kdo,master
# → 审核通过后手工移入 decisions/
```

---

## 六、Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:------|
| **阶段成熟度要求** | L3 流程建模需已有 3 次以上重复执行数据；L4 抽象建模需有 ≥3 个跨场景案例；L5 本质提炼需已验证因果链或可推导结构。阶段不成熟时强行映射会导致卡片空洞。 |
| **工具链已部署** | `kdo scaffold`/`lint`/`validate` 等命令和管线必须真实可用，否则"命令—交付物—门禁"的映射只是纸面对照。 |
| **数据流已跑通** | 需要 `00_inbox` → `60_feedback` → `30_wiki` 的实际数据流。空库或长期未更新的库无法应用此映射。 |
| **人员判断力在线** | AI 辅助阶段（尤其是 L4/L5 初稿生成）要求操作者具备逻辑洁癖和审美判断。新手直接用 AI 产出会加速跑偏。 |
| **问题类型匹配** | 高频重复任务才走 L3；跨场景问题才走 L4；战略/底层判断才走 L5。否则应留在 inbox 或 60_feedback，不进 wiki。 |

### 常见失败模式

| 模式 | 真实症状 | 可执行修复 |
|:-----|:------|:----------|
| **阶段错配：把 SOP 当框架，把框架当本质** | 工具卡里塞满抽象概念，执行步骤模糊；框架卡里没有具体动作；本质提炼只有口号没有公式。 | 按"阶段对应表"重新分级：L3 只保留动作词和检查项；L4 必须有 ≥3 个案例和反例；L5 必须能写成 1-4 个关键词/公式。 |
| **命令形式主义：为写命令而建卡** | 卡片里列出 `kdo scaffold --new framework`，但从未运行；inbox 与 wiki 内容断裂；管线阶段只是概念标签。 | 每个 KDO 命令必须对应真实卡片 ID 和执行记录；建立"命令—交付物—门禁"三联表，缺一项即退回。 |
| **AI 产出直接入库** | AI 生成的框架术语漂亮，落地时每个场景都要打补丁；同一任务两次运行结果不一致。 | 强制过"人在环中建模五步法"：定义边界 → 生成初稿 → 挑错/撞击 → 上锁/格式化 → 决定成熟。未过上锁步骤不得移入 wiki。 |
| **门禁标准错位** | L3 卡片被 L5 标准卡住发不出；L5 卡片没有反例和可推导性就发布；团队为"达标"而伪造检查项。 | 严格按阶段门禁：L3 看执行率/TODO 清理；L4 看跨域链接 ≥5 和反例 ≥1；L5 看可推导性、可证伪性和跨 ≥2 域验证。 |
| **跳过流程建模直接抽象** | 团队争论"这个业务的本质是什么"，但基础动作反复出错；新人看不懂框架，老手也不愿按 SOP 执行。 | 回退到 L3，先输出 SOP/清单并追踪执行率；执行率达到 90% 以上、异常收敛后，再启动抽象建模。 |

---

## 七、KDO 工具链落地 Checklist：从素材到 wiki 的五步映射

> 可直接复制使用。拿到任何素材后，按下面五步判断它应该进入 KDO 管线的哪个阶段、用什么命令、过什么门禁。

| 步骤 | 关键问题 | KDO 动作 | 合格标准 | 不合格的典型表现 |
|:----:|:---------|:---------|:---------|:----------------|
| 1. 识别建模点 | 这个素材对应什么问题？ | 在 `00_inbox` 打标签：`#needs-process` / `#needs-framework` / `#needs-essence` | 能用一句话说清"要解决什么" | 素材只是"有意思"，说不出问题 |
| 2. 判断阶段 | 任务高频重复？跨场景？战略/底层？ | 按"阶段选择决策树"选择 L3/L4/L5 | 阶段与问题类型匹配 | 把一次性问题硬做成 SOP；把具体流程包装成通用框架 |
| 3. 选择命令 | 当前阶段对应什么 KDO 命令？ | L3: `kdo scaffold --new tool`<br>L4: `kdo scaffold --new framework`<br>L5: `kdo scaffold --new concept` | 命令与交付物形态一致 | 命令是 tool，输出却是抽象概念 |
| 4. 执行门禁 | 该阶段的核心检查项是否通过？ | L3: `kdo lint` 检查 TODO/可执行性<br>L4: 检查跨域链接、反例、Synthesis<br>L5: 检查可推导性、跨域验证、自反性问题 | 全部检查项有明确结论（通过/不通过/待验证） | 检查项只有"是"没有证据 |
| 5. 决定成熟 | 能否发布或需要退回迭代？ | 通过则改 `status: enriched` 并设定版本；未通过则退回 `60_feedback` 并标注原因 | 有明确的 owner、版本、下次复盘时间 | 写完后无人维护，status 长期 draft |

### 实例：纪浩 Skills 市场的 KDO 映射

| 纪浩五层体系 | 对应建模阶段 | KDO 管线位置 | 核心交付物 |
|:-------------|:------------|:-------------|:-----------|
| L1 四要素验证 | L3 流程（判断流程） | `60_feedback` 检查清单 | 真需求四要素验证表 |
| L2 Agent Workspace | L3 流程（环境搭建） | `60_feedback` SOP | Agent 工作区配置清单 |
| L3 Do-first PDCA | L4 抽象建模 | `30_wiki/frameworks/` | 从行动中长出来的 PDCA 迭代模型 |
| L4 双三角模型 | L4 抽象建模 | `30_wiki/frameworks/` | 人让 AI 变强 ≠ AI 让人变强 |
| L5 Skills Market | L5 本质提炼 / L4 基础设施 | `30_wiki/decisions/` 或 `frameworks/` | "基础设施是给 Agent 用的，不是给人用的" |

> 详见 [[case-纪浩-from-zip-to-five-layers]]。

---

## 八、Open Questions

- L3→L4 的升级信号是什么？卡片什么时候从 "tool" 升级为 "framework"？
- L4 框架的置信度阈值（0.7）是否过低？本质提炼的 0.8 是否过高？
- 是否应该有一个"反建模"检查项——不是所有经验都需要建模，有些保持纯经验就够了？

---

黄药师 · 2026-06-14 · 基于 Truman 高阶建模课程 + KDO 管线设计实践
