# 老顽童后续任务

## 任务方：老顽童（飞书 Hermes）

## 状态

- 科学决策域 10 张卡 ✅（欧阳锋审查通过，A/A-）
- 调研方法论域 8 张卡 ✅（欧阳锋审查通过，全 A）
- 全库消化 ✅（三道跨域合成考试通过，总评 B+）
- 双三角文章 v2 ✅（已输出 `40_outputs/content/articles/art_双三角纠错_v2.md`，~2500 字）
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

## ② 出文章 ✅ 已完成

**双三角模型纠错版**：`40_outputs/content/articles/art_双三角纠错_v2.md`（~2500 字，2026-05-18）

验证通过项：
- 双三角方向正确：人类=创造力×审美×体系，AI=场景×基本功×数据
- ≥5 个 vault wiki 引用（width-method, habit-shift, deep-review, y-model, ai-partner）
- Kahneman System 1/2 消化再表达（非搬运）
- 六角自检表 + 三个盲区（负相关/动态博弈/先补审美）
- 讲香式消化而非精炼搬运

待欧阳锋审查通过后正式入库。

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
