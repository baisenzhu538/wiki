# 老顽童后续任务

## 任务方：老顽童（飞书 Hermes）

## 状态

- 科学决策域 10 张卡 ✅（欧阳锋审查通过，A/A-）
- 调研方法论域 8 张卡 ✅（欧阳锋审查通过，全 A）
- 全库消化 ✅（三道跨域合成考试通过，总评 B+）
- 双三角文章 v2 ✅（用户已通过，任务关闭）
- 管理工具箱 Batch 1 ✅（F1+T1+T2，欧阳锋审查全 A — Mintzberg+Pfeffer / Kahneman+Perrow / Kahneman+Tetlock）
- Blocker 解除：可以接新编译任务

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

**⚠️ T1 需修一个小 typo**（Line 88 "只需要知会议会把议程定好"语义不通），修完直接推进 Batch 2。

---

## ④ 管理工具箱 Batch 2（下一步）— T3+T4 + T5

**T3 [[yt-tool-okr-cycle]]** — OKR 制定与复盘罗盘（L4 管业务）
**T4 [[yt-tool-strategy-workshop]]** — 战略研讨会引导手册（L5 管公司）
**T5 [[yt-tool-knowledge-extraction]]** — 知识萃取器（L2-L3 交叉）

攻击者选择方向：
- T3 OKR：Doerr（OKR 原教旨）+ Müller（指标暴政/Goodhart's Law）或 Deming（目标管理的系统代价）
- T4 战略会：Rumelt（好战略坏战略）+ Mintzberg（战略即涌现，不是研讨会里规划出来的）
- T5 知识萃取：Nonaka&Takeuchi（SECI 模型）+ Snowden（Cynefin——复杂域知识不可萃取）

老规则：独立可用、≥2 攻击者、≥2 不要用、≥3 AT、≥3 跨域引用。

---

## ⑤ 设计域（Design Domain）— 工具箱完成后启动

### 素材

已就位 `00_inbox/design/`：

| 文件 | 内容 | 状态 |
|------|------|------|
| `AI设计-AI设计基础01.txt` | 月白老师第一期分享：AI 生图历史（GAN→VAE→Diffusion）、模型对比（GPT-2/巨米4.0/Nano Banana）、"去油腻"概念、为什么 AI 不能替代设计师 | 语音转文字，需清理 |
| `AI设计-AI设计师实操培训01.txt` | 月白老师第二期分享：Leo 文创案例、一堂方法论在设计场景的迁移（泛产品设计/设计MVP/最佳实践/审美十层解读）、AI prompt 的"拜拜"隐喻 | 语音转文字，需清理 |
| `prompts/ai-image-generation.md` | NANO BANANA PRO 提示词集合链接 | 骨架 |

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

## 完成标志

| 序号 | 任务 | 验证 |
|------|------|------|
| ① | 补 related 边 | `kdo lint` 通过 + 欧阳锋确认 |
| ② | 双三角文章 v2 | ✅ 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1 | ✅ 全 A，T1 修一个 typo |
| ④ | 管理工具箱 Batch 2 | 欧阳锋审查通过 → 继续 Batch 3 |
| ⑤ | 新域提案 | 欧阳锋审批通过 → 分配编译工单 |
