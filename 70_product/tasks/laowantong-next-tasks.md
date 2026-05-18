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

## ② 出文章（本周）⚠️ 返工

**双三角模型纠错版**。初稿被指出两个问题：
1. 双三角对应关系写反了（人类=创造力×体系×审美，AI=场景×数据×基本功，不是反过来）
2. 偏"精炼搬运"而非"消化再表达"

**v2 状态**：已输出 `40_outputs/content/articles/art_双三角纠错_v2.md`，形式上符合要求（三角方向正确、≥5 wiki 引用、格式完整），但**老顽童自认是按方法论模板输出，未真正消化理解**。

**返工要求**：
- 先回答三个问题（证明你真的理解了，不是套模板）：
  1. 双三角为什么是"×"不是"+"？用你自己的例子说清楚，不要引用 Kahneman 或任何学者
  2. 六个角里，你自己最弱的是哪个？为什么你知道它弱？你打算怎么补？
  3. 这个模型最大的盲区是什么？（不是文章里写的三个，是你自己觉得没说透的地方）
- 用自己的语言重写，不用任何方法论模板结构
- 2000-3000 字
- 引 ≥5 个 vault 里已有的概念做交叉引用
- 收你自己的 Q3 金句

输出到：`40_outputs/content/articles/art_双三角纠错_v2.md`（覆盖当前文件）

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
| ② | 双三角文章 v2 | ⚠️ 返工：先回答三个理解问题，再重写 |
| ③ | 新域提案 | 欧阳锋审批通过 → 分配编译工单 |
