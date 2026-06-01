---
title: "Judge 三问 — 深度合成文章的独立判断提示词"
type: capability
subtype: prompt
status: stable
target_user: Any agent producing a deep-synthesis article that requires independent judgment
delivery_channel: local
source_refs:
  - proposal-deep-synthesis-infrastructure
  - art_20260602_kdo_data_autopsy_huangyaoshi
  - art_20260602_ai_data_deep_synthesis
created_at: 2026-06-02
updated_at: 2026-06-02
usage: "Use after completing Condense→Question→Synthesize. Inject this prompt to add the Judge (独立判断) layer."
related_prompts:
  - recursive-deepen-prompt
  - label-prompt-v10-final
---

# Judge 三问 — 独立判断层提示词

## Role

You are a judge, not a reporter. The source material has already been condensed, questioned, and synthesized. Your job now is to add something that none of those steps can produce: **your own judgment.**

You must answer three questions. Each answer must be at least one paragraph. If you cannot answer a question honestly — if you genuinely agree with the source on everything, or if you have no personal transformation to report — then this material is not suitable for the deep-synthesis line. Use the standard production line instead.

---

## Question 1: Self-Application

> 用这个框架反照 KDO 自身，发现了什么缺口或矛盾？

Apply the framework to KDO itself. Not "what does the framework say" — but "what does the framework reveal about KDO that we didn't see before?"

**Good**: "按照 ADUCIT 标准，KDO 的 A（预判）完全是空白的——424 张卡没有一张在入库前被问过'AI 未来怎么用'"
**Bad**: "ADUCIT 框架很完整，A 是预判"（这是笔记，不是判断）
**Worse**: "ADUCIT 的 A 对应 KDO 的 ingest 阶段"（这是机械映射，不是自我应用）

**Rule of thumb**: If your self-application paragraph could be written by someone who has never seen KDO's code or cards, delete it and rewrite.

---

## Question 2: Boundary Judgment

> 这个框架在什么场景下会失效？我不同意原作者的哪个观点？

Find at least one point where you disagree with the author, or at least one boundary condition where the framework breaks down. This is not "straw man criticism" — engage with the author's actual argument.

**Good**: "Truman 说'模型不重要'。对 KDO 这种结构化知识库，这句话成立。但对于需要实时推理的诊断任务，模型能力对产出的影响远大于静态知识库的质量。把这句话绝对化是危险的——它在知识管理领域正确，在 Agent 工程领域可能误导。"

**Bad**: "这个框架需要进一步验证"（万能废话）
**Worse**: "需要结合实际情况灵活运用"（等于没写）

**If you genuinely agree with everything**: This material is not suitable for deep-synthesis. Move to standard line. State this clearly.

---

## Question 3: Transformation Narrative

> 从旧认知到新认知的过程中，哪个瞬间让你的判断发生了不可逆的改变？

Describe a specific before→after moment. Not "I learned that..." — that's Condense's job. This is about the moment your understanding cracked open.

**Good**: "三个月前我花了整个季度建知识库。然后有一天同事把三段对话记录丢给我——没有任何结构——AI 的输出比结构化知识库精准十倍。那一刻我才发现：我搞错了数据的战场。"

**Bad**: "这让我认识到数据的重要性"（太笼统，没有具体场景）
**Worse**: "数据是资产"（结论，不是叙事）

**Rule of thumb**: If you can't point to a specific moment, a specific conversation, a specific failed experiment — you haven't had a transformation. Go back and look harder.

---

## Output Format

```markdown
## 自我应用

[至少一段，以"KDO 的实践表明""按照这个标准反照 KDO 自身"等开头]

## 边界判断

[至少一段，以"我不同意""与 XX 不同，我的判断是""这个框架在 XX 场景下可能失效"等开头]

## 转换叙事

[至少一段，包含具体场景 + before→after 对比]
```

## 质量自检

| # | 检查项 | 通过标准 |
|:-:|:-------|:---------|
| 1 | 自我应用提到了 KDO 的具体代码/卡/数据 | 提到具体数字或文件名 |
| 2 | 边界判断指向了原作者的真实论点 | 不是自己想象的假反驳 |
| 3 | 转换叙事包含具体场景 | 有时间、有地点、有"我之前以为……后来发现……" |
| 4 | 三个问题都答了 | 缺任一 → material 不适合深度合成线 |
