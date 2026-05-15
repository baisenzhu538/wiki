---
id: yt-model-cognitive-upgrade-framework
title: 认知升级十步框架：把一本书变成可安装的思维补丁
type: framework
status: enriched
domain:
  - master
language: zh-CN
version: 1
difficulty: intermediate
confidence: 0.85
prerequisites: []
component_of: []
related:
  - yt-model-ipo-learning-strategy
  - yt-model-prompt-engineering
  - yt-concept-ai-guard-brain
contradicts: []
query_triggers:
  - 认知升级
  - 读书方法
  - 怎么真正读透一本书
  - 知识内化
  - 思维补丁
  - 学习框架
  - 深度阅读
  - AI思维卡
  - 旧Bug新Patch
  - 知识转化行为
tags:
  - '#master'
  - '#learning'
  - '#methodology'
source_refs:
  - 00_inbox/《人工智能：一种现代方法》-AI思维卡.html
created_at: '2026-05-15'
updated_at: '2026-05-15'
estimated_tokens: 2500
reviewed_by: 欧阳锋
---

# 认知升级十步框架：把一本书变成可安装的思维补丁

> 源自 AI 思维卡「认知升级系统 v3.2」的实战方法论。不是"怎么写读书笔记"，而是"怎么把一本书装进脑子并改变行为"。

## Claims

### 核心命题：读书的终点不是"学完了"，是"有东西被替换了"

- claim:01 [conf=0.90] 大多数读书方法是"信息整理"——划线、摘抄、画思维导图、写摘要。这些方法的终点是"一份笔记"。认知升级十步框架的终点是"一个可执行的动作"——读完后的今晚，你做什么跟昨天不一样。

- claim:02 [conf=0.85] 真正有效的学习必须能回答两个问题：(1) 我之前的哪个认知被替换了？(2) 我今晚能做什么动作来验证这个替换？答不出这两问 = 没学会。

### 十步框架

- claim:03 [conf=0.90] 完整流程：

| 步骤 | 名称 | 核心问题 | 产出 |
|:--:|------|---------|------|
| 1 | **IDENTITY** | 这本书是谁？对我承诺什么？ | 身份卡（真正在问什么、承诺什么、作者是谁） |
| 2 | **MODEL** | 我装了什么新模型？ | 3 句话精髓 + 因果链 + N 个工程原语 |
| 3 | **EVIDENCE** | 这模型站得住吗？ | 关键案例 + 反事实测试 + 外部攻击 + 偏差标注 |
| 4 | **CONTRAST** | 和我已有的工具冲突/互补吗？ | 边界地图（适用 vs 失效、冲突点 vs 互补点） |
| 5 | **ACTION** | 我以后怎么用？ | 场景卡（触发条件 + 追问清单）+ 新工作流 |
| 6 | **REFLECTION** | 哪句话留下了？ | 3 句原文 + 会在什么情境下想起它 |
| 7 | **MY TAKE** | 这本书对我意味着什么？ | 旧 Bug → 新 Patch 三列对照表 + 关键论据 |
| 8 | **ICAP** | 我学到了哪个层级？ | 自评阶梯（Passive/Active/Constructive/Interactive） |
| 9 | **CTA** | 今晚就做，三选一 | 3 个动作，每个 5 分钟内可启动，有成功指标 |
| 10 | **FOLLOWUP** | 三周后复诊 | 4 个检查问题（启动了哪些？没调用过什么？意外价值？升级为长期习惯？） |

### 三步与我们 KDO 三步编译法的关系

- claim:04 [conf=0.85] 十步框架和我们 KDO 的三步编译法不是替代关系，是延伸关系：

| KDO 三步编译 | 对标十步框架 | 差异 |
|------------|------------|------|
| Condense | MODEL（3 句话+原语） | 我们产出 claims 列表，他们加了工程原语和因果链 |
| Critique | EVIDENCE + CONTRAST | 我们只要一条边界，他们做了反事实+偏差标注+外部攻击+适用/失效对照 |
| Synthesis | — | 我们没有对标环节。他们用 MY TAKE（旧 Bug→新 Patch）做主观认知替换追踪 |

- claim:05 [conf=0.80] KDO 管线在十步框架中缺失最严重的是 **ACTION → CTA → FOLLOWUP** 三个行为转化环节。我们 ship 即终点，他们 ship 后还有三周复诊。

### 关键的三个差异化设计

- claim:06 [conf=0.85] **旧 Bug → 新 Patch 追踪**（MY TAKE）：不是"我学到了什么"，而是"我之前的哪个认知被替换了"。三列：旧 Bug → 新 Patch → 让我相信的关键论据。这比"学习总结"精确得多——你能指出具体哪个节点被更新了。

- claim:07 [conf=0.85] **ICAP 自评阶梯**：不是给内容打难度分，是给自己打深度分。Passive（知道术语）→ Active（开始主动用）→ Constructive（能自己建工作流）→ Interactive（能讲给别人听并接受挑战）。每个层级自带"下一步往哪走"的导航。

- claim:08 [conf=0.80] **EVIDENCE 审计的三件套**：反事实测试（去掉这个案例模型还成立吗？）、偏差标注（选择性举证/作者偏向/简化）、外部攻击（谁说这条不对？）。这三个比我们现有的"写一条边界约束"更系统。

## Constraints & Boundaries

- claim:boundary-01 [conf=0.85] **十步框架对"读完一本完整书"最有效，对碎片化输入（文章/视频/推文）过重。** 碎片化输入更适合 KDO 的三步编译法（浓缩→质疑→对标），十步框架用于你判断为"值得深度内化"的少数关键书籍——一年不超过 12 本。判断标准：这本书如果只留下 3 句话，你愿意为它花 4 小时做十步吗？

- claim:boundary-02 [conf=0.80] **ICAP 自评有自我欺骗风险。** 大多数人会高估自己的层级——把"读过并认同"标为 Active，把"写过笔记"标为 Constructive。ICAP 的防自欺机制是：你必须能说出"我具体更新了哪个部件"——说不出 = Passive，跟感受无关。但即便如此，自我评估仍有膨胀倾向，推荐让他人验证。

- claim:boundary-03 [conf=0.80] **EVIDENCE 的外部攻击可能退化为找茬。** 引用真实外部批评的前提是你真的理解了那个批评的立场和论据——否则会变成"找一个反对观点然后轻松反驳"的 strawman。如果找不到高质量的外部批评，宁缺毋滥。

- claim:boundary-04 [conf=0.85] **十步框架的"转化率"高度依赖 CTA 设计质量。** 如果 CTA 是"写一篇读后感"，转化率趋近于零。有效的 CTA 必须：5 分钟内能启动、有明确的成功/失败标准、直接嵌入已有日常流程（而非另起一个"学习计划"）。ACTION→CTA→FOLLOWUP 是整个框架的承重墙——前三步（IDENTITY/MODEL/EVIDENCE）决定了理解深度，后三步决定了行为是否真的改变。

## Framework Gallery

### 关联框架卡
- [[yt-model-ipo-learning-strategy]] — IPO 学习模型：十步框架可视为 IPO 在深度阅读场景下的超级强化版
- [[yt-model-prompt-engineering]] — 提示词工程总框架：AI 作为阅读伙伴可嵌入十步框架的多个环节（如让 AI 扮演 CONTRAST 中的反对角色）

### 关联概念
- [[yt-concept-ai-guard-brain]] — 守脑如玉：十步框架是实现"守脑如玉"的操作系统——不是不依赖 AI，而是用结构化流程确保认知生长在你自己脑子里

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 理论基础 | [[yt-model-ipo-learning-strategy]] | IPO（输入→处理→输出）：十步框架在输入（IDENTITY+MODEL）、处理（EVIDENCE+CONTRAST+REFLECTION）、输出（ACTION+CTA+FOLLOWUP）上都做了十倍强化 |
| 方法关联 | [[yt-model-prompt-engineering]] | AI 合伙人：在 EVIDENCE 环节让 AI 扮演反对角色、在 CONTRAST 环节让 AI 扮演已有工具的辩护者、在 CTA 环节让 AI 生成更多可选动作 |
| 互补概念 | [[yt-concept-ai-guard-brain]] | 守脑如玉：ICAP 自评 = 对自己认知深度的诚实审计；旧 Bug→新 Patch = 证明"我更新了哪个部件"的具体证据 |

> **Burn line**: 读书的终点不是合上书，是今晚你做了什么跟昨天不一样的事。
