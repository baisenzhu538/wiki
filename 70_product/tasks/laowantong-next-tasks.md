# 老顽童后续任务

## 任务方：老顽童（飞书 Hermes）

## 状态

- 科学决策域 10 张卡 ✅（欧阳锋审查通过，A/A-）
- 调研方法论域 8 张卡 ✅（欧阳锋审查通过，全 A）
- 全库消化 ✅（三道跨域合成考试通过，总评 B+）
- 双三角文章 v2 ⚠️（已输出 `40_outputs/content/articles/art_双三角纠错_v2.md`，待返工）
- **管理工具域提案 ✅**（2026-05-19 提交，9 张卡：F1+T1~T8，待启动编译）
- Blocker 解除：可以接新编译任务
- ⑤ 设计域素材已就位（3 份文件），清理转录稿后即可开工

**⚠️ 以下任务顺序执行**。做完一个看下一个，不要跳。

**🆕 新素材（优先）**：Anthropic 创始人手册 → 见 [[#⑧ Anthropic AI 原生初创公司手册]]

**⚠️ 黄药师正在建 `kdo scaffold` 工具**（[[70_product/tasks/huangyaoshi-next-tasks.md]]）。完工后你修 89 卡时用它加速——不再从空白页搭 Critique 框架。

---

## ① 补 related 边（立即，30min）

判卷 Q1 发现：三道跨域连接只在嘴上说了，卡里的 `related:` 字段还没加。

需补的 wikilink + frontmatter relation：

### 卡 yt-decision-y-model 补

```yaml
related:
  - yt-entrepreneur-key-hypotheses  # "拆假设"工具
```

body 关键假设相关段添加：`[[yt-entrepreneur-key-hypotheses]]`

### 卡 yt-decision-review 补

```yaml
related:
  - yt-personal-deep-review  # 冰山图五层→决策复盘上限
```

body 深度复盘段添加：`[[yt-personal-deep-review]]`

### 卡 yt-decision-height-toolkit 补

```yaml
related:
  - yt-model-liberate-thinking-layers  # 高度瓶颈诊断
```

body 高度提升段添加：`[[yt-model-liberate-thinking-layers]]`

### 完成后

跑 `kdo lint` 确认新增 wikilink 的目标页都存在。

---

## ② 双三角文章 v2 — ✅ 已关闭

用户已通过文章，任务关闭。

---

## ③ 管理工具箱 Batch 1 — ✅ 已完成（F1+T1+T2）

欧阳锋审查通过，全 A：

| 卡 | 评级 | 攻击者 |
|----|------|--------|
| F1 [[yt-management-toolkit-overview]] | A | Mintzberg+Pfeffer |
| T1 [[yt-tool-meeting-designer]] | A | Kahneman+Perrow |
| T2 [[yt-tool-hiring-scorecard]] | A | Kahneman+Tetlock |

**⚠️ T1 typo 仍未修复**（Line 90 "只需要知会议会把议程定好"语义不通）。

---

## ④ 管理工具箱 Batch 2 — T3+T4+T5 全部完成 ✅

| 卡 | 评级 | 攻击者 | 状态 |
|----|------|--------|------|
| T3 [[yt-tool-okr-cycle]] | **A** | Mintzberg（涌现战略）+ Ordonez（目标副作用） | ✅ 审查通过。⚠️ typo 仍未修复：Line 105 `团队脚脑暴`→`团队头脑风暴` |
| T4 [[yt-tool-strategy-workshop]] | **A+** | Christensen（创新者窘境）+ Taleb（黑天鹅/规划伪科学） | ✅ 审查通过。全库迄今最佳 tool 卡，建议作为后续标准 |
| T5 [[yt-tool-knowledge-extraction]] | **A** | Nonaka&Takeuchi（SECI 模型）+ Snowden（Cynefin——复杂域知识不可萃取） | ✅ 审查通过。typo 已修复 ✅ |

**审查备注**：
- T4 是全工具箱 5 张 tool 卡的结构标杆：会前四件套+会中五段式+会后三检查，11 步各有时间分配+关键约束+退出标准
- T3 的 Ordonez 是非显而易见但高度相关的选择（"Goals Gone Wild"研究），体现了独立学术判断
- Mintzberg 已在 F1/T3/T4 三次出场，攻击角度有区分（管理手艺 vs 涌现战略 vs 战略涌现）但目前频次触顶，T5-T8 应避开
- Taleb 已出场 ~3 次，同样建议 T5-T8 避开

---

## ⑤ 设计域 → 洪七公/段王爷 Skills（方向调整）

> **2026-05-19 欧阳锋拍板**：废弃 D1-D7 卡片地图 + 两篇文章方案。这不是知识卡片（不需要 Critique/攻击者），是操作手册。产出改为 3 个 skill 文件，供洪七公和段王爷直接调用。格式参照 `[[40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md]]`。

### 素材

已就位 `00_inbox/design/`（2026-05-19 欧阳锋核实）：

| 文件 | 内容 | 大小 | 状态 |
|------|------|------|------|
| `AI设计-AI设计基础01.txt` | 月白老师第一期分享 | 72KB | ✅ 已清理 → `cleaned/` |
| `AI设计-AI设计师实操培训01.txt` | 月白老师第二期分享 | 122KB | ✅ 已清理 → `cleaned/` |
| `prompts/ai-image-generation.md` | NANO BANANA PRO 提示词集合链接 | 230B | ✅ 骨架 |

### 产出：3 个 Skill

| # | Skill 名称 | 给谁用 | 素材来源 | 核心内容 |
|---|-----------|--------|---------|---------|
| **S1** | AI 生图模型选型指南 | 洪七公 | 素材1 前半 | GPT-2o / 巨米4.0 / Nano Banana 场景匹配矩阵、"去油腻"概念、何时用/不用 |
| **S2** | AI 设计 Prompt 工程 | 洪七公 | 素材2 | "拜拜"工作流（说出来→写下来→喂给AI）、设计MVP、灵感画布五维检索 |
| **S3** | 设计资产管理规范 | 段王爷 | 素材1 后半 | 8要素命名法、四类资产沉淀、输出格式规范 |

### Skill 格式规范

参照 `[[40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md]]`，每个 skill 必须包含：

```markdown
# Skill Name

## Purpose（一句话说清干什么）

## When to Use（触发条件）

## When NOT to Use（边界——这很重要）

## Protocol / Guide（操作步骤，能照着做）

## Examples（至少一个真实案例）
```

**不需要**：Critique、攻击者、不要用场景、Action Triggers、wikilink 引用。这是操作手册，不是知识卡片。

### 执行顺序

S1 → S2 → S3，分段输出。每完成一个发欧阳锋审查。

---

## ⑥ v1.5 全库修复流水线（设计域完成后）

### 背景

`kdo validate --v15` 诊断结果：205 张卡，45 pass / 89 fail / 71 warn。`kdo scaffold`（黄药师 Task 1）已经搭好了工具。

### 执行方式

```bash
# 1. 先看全局
kdo validate --v15 --upgrade-plan

# 2. 按优先级分批（黄药师的 scaffold 已可用）
kdo scaffold --batch A --write    # 全信号缺失高引卡（~3 张）
kdo scaffold --batch C --write    # 缺 Action Triggers（~6 张）
kdo scaffold --batch B --write    # 缺外部攻击（~80 张，大头）
kdo scaffold --batch D --write    # 研究降级（~26 张）

# 3. 逐张填内容（scaffold 给了 TODO + 学者建议）
# 4. 填完验证
kdo validate --v15 --card <id>
```

### 优先级

| 顺序 | Batch | 内容 | 卡数 | 策略 |
|------|-------|------|------|------|
| 1 | C | 缺 Action Triggers | ~6 | **先做**。每张只需补一个 3 行表，15min/张，最快看到 PASS 增长 |
| 2 | A | 全信号缺失高引 | ~3 | 工作量大（90min/张）但价值最大——修一张 = 0→3 信号 |
| 3 | B | 缺外部攻击 | ~80 | **大头**。每张需研究 2 位学者 + 写攻击段落，60min/张 |
| 4 | D | 研究降级 | ~26 | 标准降低但仍需 ≥1 攻击 |
| 5 | E | Warnings | ~71 | 不算 fail，精修 |

> 注意：不是一次做完 89 张。按批推进，每做完一批通知欧阳锋抽检。

---

## ⑦ 管理工具箱 Batch 3（89 卡修复喘口气时穿插）

工具箱还剩最后 3 张，可以在 89 卡修复的间隙穿插（换脑休息）：

**T6 [[yt-tool-project-health-radar]]** — 项目健康度雷达（L2-L4 交叉）
**T7 [[yt-tool-onboarding-90day]]** — 新人 90 天融入加速器（L3 管团队）
**T8 [[yt-tool-equity-checklist]]** — 股权设计检查清单（L5 管公司）

攻击者方向：
- T6 项目雷达：Flyvbjerg（巨型项目铁律）+ Goldratt（约束理论——局部最优≠全局最优）
- T7 新人融入：Van Maanen&Schein（组织社会化策略）+ Edmondson（心理安全——融入≠同化）
- T8 股权清单：Coase（交易成本/企业边界）+ Williamson（资产专用性——股权是一种治理结构选择）

---

## ⑧ Anthropic AI 原生初创公司手册（🆕 优先）

### 素材

| 文件 | 来源 | 大小 |
|------|------|------|
| `00_inbox/Anthropic 官方发布：《创始人手册：打造 AI 原生初创公司》.md` | Anthropic 2026.5.17 | 82KB |

已 ingest → source `src_20260519_f6ec0400`，wiki 骨架已生成：[[anthropic-官方发布创始人手册打造-ai-原生初创公司]]

### 执行步骤

标准三步编译法：

1. **读素材**：`10_raw/sources/src_20260519_f6ec0400-*.md`
2. **Condense**：提取 3-5 条核心观点（AI 四阶段创业法、创始人角色演变、精益独角兽模式、三类 AI 能力）
3. **Question**：写 `## Constraints & Boundaries` + `### [Critique]` 节
   - 至少 2 位外部攻击者（建议方向：Christensen 创新者窘境——AI 原生是否是新颠覆？Pfeffer 领导力 BS——AI 指挥家是否是新包装？）
   - 至少 2 个不要用场景
4. **Synthesize**：对标已有卡片（管理工具箱 F1/T4、决策域 Y 模型等），创建 wikilink
5. **Action Triggers**：≥3 条可执行触发器

### 卡片类型

`concept`（方法论概念卡），domain 建议 `entrepreneur`

### 验收

- v1.5 三信号齐全（≥2 attackers, ≥2 don't-use, ≥3 AT）
- 引用 Anthropic 原文关键数据
- 跨域引用 ≥3 张已有卡片
- `kdo validate --v15 --card anthropic-官方发布创始人手册打造-ai-原生初创公司` 返回 PASS

---

## 完成标志

| 序号 | 任务 | 验证 |
|------|------|------|
| ① | 补 related 边 | `kdo lint` 通过 + 欧阳锋确认 |
| ② | 双三角文章 v2 | ✅ 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1 | ✅ 全 A，T1 修一个 typo |
| ④ | 管理工具箱 Batch 2 | T3 (A) ✅ + T4 (A+) ✅ + T5 (A) ✅ |
| ⑤ | 设计域 7 张卡 | 素材已就位，清理转录稿后可开工 |
| ⑥ | v1.5 全库修复（89 FAILED） | `kdo validate --v15` FAILED → 0 |
| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 欧阳锋审查通过 |
