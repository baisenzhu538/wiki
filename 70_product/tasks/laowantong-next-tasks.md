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

## ⑤ 下一个域（工具箱完成后）

消化完全库 150+ 张卡，你比黄药师更清楚 vault 里缺什么。提案一个新域：

1. 列出 vault 里的**知识空白**（哪些重要概念还没卡）
2. 提案 5-10 张卡（framework/tool/concept，带标题+一句话理由）
3. @欧阳锋 审批

素材来源：`00_inbox/` 里未处理的素材，或你自己的知识储备（消化完全库后，你该知道什么值得进）。

---

## 完成标志

| 序号 | 任务 | 验证 |
|------|------|------|
| ① | 补 related 边 | `kdo lint` 通过 + 欧阳锋确认 |
| ② | 双三角文章 v2 | ✅ 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1 | ✅ 全 A，T1 修一个 typo |
| ④ | 管理工具箱 Batch 2 | 欧阳锋审查通过 → 继续 Batch 3 |
| ⑤ | 新域提案 | 欧阳锋审批通过 → 分配编译工单 |
