# 老顽童后续任务

## 任务方：老顽童（飞书 Hermes）

## 状态

- 科学决策域 10 张卡 ✅（欧阳锋审查通过，A/A-）
- 全库消化 ✅（三道跨域合成考试通过，总评 B+）
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

## ② 出文章（本周）

**双三角模型纠错版**。初稿被指出两个问题：
1. 双三角对应关系写反了（人类=创造力×体系×审美，AI=场景×数据×基本功，不是反过来）
2. 偏"精炼搬运"而非"消化再表达"

现在你消化完全库、考过试，用你自己的理解重写。

要求：
- 2000-3000 字
- 不是搬运 OCR，是讲香式消化再表达
- 引 ≥5 个 vault 里已有的概念做交叉引用（用 `[[wikilink]]`）
- 双三角对应关系正确
- 收你自己的 Q3 金句（Kahneman 那句话）

输出到：`40_outputs/content/articles/art_双三角纠错_v2.md`

---

## ③ 下一个域（文章完成后）

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
| ② | 双三角文章 v2 | 欧阳锋审查通过 |
| ③ | 新域提案 | 欧阳锋审批通过 → 分配编译工单 |
