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

## ⑤ 设计域（Design Domain）— 工具箱完成后启动

### 素材

已就位 `00_inbox/design/`（2026-05-19 欧阳锋核实）：

| 文件 | 内容 | 大小 | 状态 |
|------|------|------|------|
| `AI设计-AI设计基础01.txt` | 月白老师第一期分享：AI 生图历史（GAN→VAE→Diffusion）、模型对比（GPT-2/巨米4.0/Nano Banana）、"去油腻"概念、为什么 AI 不能替代设计师 | 72KB | ✅ 待清理 |
| `AI设计-AI设计师实操培训01.txt` | 月白老师第二期分享：Leo 文创案例、一堂方法论在设计场景的迁移（泛产品设计/设计MVP/最佳实践/审美十层解读）、AI prompt 的"拜拜"隐喻 | 122KB | ✅ 待清理 |
| `prompts/ai-image-generation.md` | NANO BANANA PRO 提示词集合链接 | 230B | ✅ 骨架 |

### 执行步骤

#### Step 0 — 清理转录稿

两份 `.txt` 是实时语音转文字（ASR 输出），口语化严重、有填充词、分段破碎、有回音/网络问题导致的乱码。先用 Agent 做**结构化清理**：

- 去除口头禅和重复（"呃"、"就是"、"有没有回音"→删除）
- 修复 ASR 错误（"去油腻"可能是"去塑料感"或保留为特色术语）
- 重新分段：按主题切分，每个主题一个 H2
- 提取核心概念和定义（斜体标注术语）
- 保留案例细节（Leo 案例、模型对比数据）
- 输出清理版到 `10_raw/sources/` 或 `00_inbox/design/cleaned/`

#### Step 1 — Ingest

清理后的转录稿走 `kdo ingest` → 创建 `10_raw/sources/` 副本 + wiki 骨架。

#### Step 2 — 编译卡片

从两份转录稿提取可复用知识，建议卡片地图（待老顽童消化素材后细化）：

| 编号 | 暂定标题 | 类型 | 内容 |
|------|---------|------|------|
| D1 | AI 生图技术演进 | concept | GAN→VAE→Diffusion→GPT-2o，技术路线 + 关键转折 |
| D2 | AI 设计模型选型指南 | tool | GPT-2o vs 巨米4.0 vs Nano Banana，场景匹配矩阵 |
| D3 | 设计 MVP 方法论 | tool | 大设计项目拆解为小 MVP，与一堂 MVP 方法论的区别 |
| D4 | AI 设计 Prompt 工程 | tool | "说出来→写下来→喂给AI"的口喷工作流 + NANO BANANA PRO 提示词 |
| D5 | 视觉最佳实践检索 | tool | 设计参考的搜寻→筛选→迁移策略 |
| D6 | 审美判断十层解读 | framework | 设计的十层评判维度（月白老师提炼版） |
| D7 | AI 时代设计师角色重塑 | concept | "AI 不会替代设计师，但会替代不会用 AI 的设计师" |

> ⚠️ 以上为初步印象。老顽童消化完素材后可能合并/拆分/新增。最终卡片数 5-8 张。

#### Step 3 — 攻击者配对

设计域学者方向建议（消化素材后确认）：

| 卡 | 建议攻击者 | 攻击角度 |
|----|-----------|---------|
| AI 生图技术 | Nelson Goodman（艺术语言）+ Flusser（技术图像哲学） | AI 生成的"图像"是否算"设计" |
| Prompt 工程 | Suchman（情境行动）+ Schön（反思实践） | prompt 可编码 vs 设计 tacit knowledge 不可编码 |
| 审美判断 | Bourdieu（区隔/品味阶级）+ Norman（情感化设计） | 审美是可教可学的技能还是文化资本 |
| 设计师角色 | Sennett（匠人）+ Crawford（动手的智慧） | AI 去技能化 vs 增强 |

#### Step 4 — 欧阳锋审查

老规则：全量 checklist（≥2 攻击者、≥2 不要用、≥3 AT、≥3 跨域引用）。

### 与工具箱的关系

工具箱 Batch 2（T3+T4+T5）优先完成，然后启动设计域。不并行——老顽童单线程产能，上下文切换成本高。

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
