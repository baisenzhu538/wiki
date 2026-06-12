---
id: "dk-c8-format-complete-mind-empty"
title: "C-8：批处理格式升级产生格式完整但思维空洞的卡片"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "欧阳锋"
source_context: "Sprint 6 审查发现，2026-05-13"
source_refs:
  - "20_memory/corrections.md#C-8"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - "dk-c10-batch-tool-no-dry-run"
  - "master-decision-hygiene"
tags:
  - #domain/knowledge-management
  - #method/evaluation-method
  - #scene/hardware-debugging/prototyping
  - #scene/knowledge-management/tagging
  - #scene/skill-engineering/manifest-design
pipeline:
  - #boundary/requires-human-judgment
  - #source_type/error
  - confidence-draft
  - confidence-source-cited
  - confidence-verified-by-case
---

# C-8：批处理格式升级产生格式完整但思维空洞的卡片

## 原始表述

> Sprint 6 批处理升级的 panproduct tool 卡通过所有格式门禁（id 有、query_triggers 有、related 非空），但体检抽检两张卡发现：Constraints & Boundaries 节完全缺失——不是内容差，是不存在；Claims 是口述稿的直接摘录，零合成加工；无反例——未回答"什么场景下不该用这个工具"；无案例筛选——从大量素材中挑选最有区分度的案例这一步被跳过；跨域连接是薄标签。质量门禁只检测格式，检测不到理解深度。批处理脚本可以填满所有必填字段，但不会做"这个工具的边界在哪里""哪个案例最能说明它的独特价值""它和另一个工具的本质区别是什么"这种判断。

## 使用场景

- 你刚完成一批卡片的自动化格式升级（scaffold、enrich、clean），准备提交审查
- 你正在设计一个新的自动化管线脚本，它只检查"字段有没有"，不检查"内容好不好"
- 你抽检别人的批量产出时，需要区分"格式通过"和"理解通过"

## 操作方法

1. **格式门禁通过后，必须加理解门禁抽检**：从批次中随机抽 2 张卡
2. **检查三个信号**：
   - **反例具体性**：Constraints 节是否包含了具体的、可验证的反例？（不是"本方法有局限性"这种废话）
   - **案例筛选**：是否从素材中挑选了最有区分度的案例？（不是随便拿了一个）
   - **跨域连接**：related 字段是否指向了有实质关系的卡片？（不是薄标签）
3. **判定标准**：三个信号中至少两个为"有实质内容"，才算理解通过。否则整批退回。
4. **校准**：新域卡片建设前，先抽检两张旧卡做校准——让执行者看到"格式完整但思维空洞"的真实样本

## 适用边界

- 适用于所有**批量自动化内容操作**——scaffold、enrich、clean、tag、chunk
- 不适用于只读操作
- 理解门禁不能替代格式门禁——两者是 AND 关系，不是 OR
- 理解门禁的抽检率取决于批次大小：≤5 张抽 1 张，6-20 张抽 2 张，>20 张抽 3 张

## 为什么值钱

- C-8 揭示了 KDO 质量体系的结构性盲区：**格式门禁通过 ≠ 内容合格**
- 在同一批升级中，Validator 给了 PASS，Lint 给了零错误，审查者看到"格式完整"就放行了——四个环节全部漏过
- 这和 C-10 是同一模式：自动化工具的产出在格式上合法，但语义上是垃圾或空洞。格式门禁完全检测不到——只有人读了内容才能判断
- 核心教训：**任何只检查格式不检查内容的质量门禁，都是虚假安全感**

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一模式：格式门禁打假 PASS。C-10 是"内容被清空"，C-8 是"内容从未被填入"
- [[master-decision-hygiene]] — C-8 的"理解门禁抽检"类比决策卫生的 Step 3（独立评估）——不能让一个人审自己的产出
- `90_control/kdo-industrialization-manual.md` → 三层质量门禁（L1 结构完整性 / L2 内容质量 / L3 管线一致性）
- `20_memory/corrections.md` → C-8、C-9、C-10（批处理三连坑）
