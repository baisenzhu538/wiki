---

id: case-半肥猫-course-to-skill
title: 案例：半肥猫的课程转 Skill 八步法——从一堂转化率课程到可验证的 AI 工具
type: case
status: enriched
domain:
- skill-engineering
- yitang
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享——真实案例：将一堂《转化率黑客五组合落地》课程转化为 Skill
source_refs:
- 10_raw/sources/src_20260617_2b8a01ce-ai俱乐部-ai学习落地-半肥猫-口述.txt
- 10_raw/sources/src_20260617_629e996c-ai俱乐部-ai学习落地-半肥猫-笔记.txt
tags:
- '#perspective/professional'
- '#confidence/source-cited'
- '#confidence/verified-by-case'
- '#confidence/verified-by-test'
- '#domain/skill-engineering'
- '#domain/yitang'
- '#scene/agent-infrastructure/skill-registry'
- '#scene/ai-collaboration/problem-validation'
- '#scene/business-analysis/conversion-rate'
- '#scene/knowledge-management/case-library'
- '#scene/knowledge-management/tagging'
- '#scene/learning-methodology'
- '#scene/note-taking'
- '#scene/skill-engineering/course-to-skill'
- '#scene/skill-engineering/eval-testing'
- '#scene/skill-engineering/manifest-design'
- '#scene/skill-engineering/publish-deploy'
- '#content-format/case-study'
created_at: 2026-06-08
updated_at: '2026-06-17'
related:
  - '[[case-ban-fei-mao-skill-ab-test]]'
  - '[[tool-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie]]'
  - '[[dk-ban-fei-mao-skill-rejection-value]]'
  - '[[tool-ban-fei-mao-yong-skill-zuo-dui-bi-ce-shi-yan-zheng-xiao-guo]]'
  - '[[case-ban-fei-mao-conversion-hacker-skill]]'
  - '[[case-ji-hao-skills-market]]'
  - '[[case-truman-ai-partner]]'
  - '[[case-纪浩-focus-prompt-design]]'
  - '[[case-纪浩-from-zip-to-five-layers]]'
  - '[[kdo-ec-industrialization-migration-proposal]]'
  - '[[modeling-capability-for-kdo]]'
  - '[[yt-business-analysis-cognitive-biases]]'
  - '[[yt-five-step-level-blindspots]]'
author: 半肥猫
reviewed_by: 老顽童
confidence: 0.7
trust_level: low
diagnostic_signals:
- signal: 用通用 AI 问"怎么提高转化率"，得到流畅方案但没有评分标准和风险分级
  framework_lens: 缺少诊断协议与边界约束
  follow_up_question: 你的 Skill 有没有明确的评分规则、适用边界和风险分级？没有的话输出就是"裸 AI"。
- signal: 课程听完了、笔记做了很多，但每次遇到真实问题还是从头开始
  framework_lens: 知识未工程化为可调用 Skill
  follow_up_question: 这门课的核心方法能不能写成"输入→处理→输出→校验"四段式协议？
- signal: 做了一个 AI 工具，输出很流畅但不敢在真实决策中使用
  framework_lens: 证据链未校准
  follow_up_question: 工具中的每条关键 claim 是否有来源？哪些是个人经验、哪些是外部数据、哪些缺少反例？
- signal: 团队里每个人都在用 AI，但好的 prompt 无法复用、版本混乱
  framework_lens: 缺少工程化目录与封装机制
  follow_up_question: 你的 Skill 是否有 manifest、测试用例、版本记录和安装文档？
---

# 案例：半肥猫的课程转 Skill 八步法

> 半肥猫用一堂《转化率黑客五组合落地》课程作为原材料，经过八步工程化流程，做出了一个可验证的转化率方案推演 Skill。A/B 测试：用 Skill 得 36 分，不用 Skill 得 8 分——差值 28 分。这不是"AI 更强了"——是"工程化流程产出了更可靠的 AI 工具"。

## Background

半肥猫在 AI 俱乐部分享中演示了他如何把一门课程变成一个可用的 AI Skill。原材料是一堂的经典课程《转化率黑客五组合落地》。在动手之前，存在四个典型问题：

| 问题 | 具体表现 |
|:---|:---|
| **课程知识无法调用** | 听完就完了，知识停留在笔记里，遇到真实转化率问题仍从零开始 |
| **AI 输出空洞** | 通用 AI 回答"帮你提高业绩"——没有评分、没有边界、没有风险分级 |
| **可用性无标准** | 不知道什么场景该用、什么场景不该用，AI 什么都说 |
| **效果无法量化** | 无法判断一个方案好不好，缺乏可验证的通过线 |

关键前提：这个案例不是半肥猫私自加工——是得到官方许可后，官方给他出的题。

## What Happened

半肥猫用八步把课程转化为一个**实验约束型转化率方案推演 Skill**：

| 步 | 做什么 | 为什么这一步不能跳过 | 产物 |
|:--:|:---|:---|:---|
| **1. 判断是否值得做** | 评估课程是否有科学方法 + 可验证案例 + 明确边界 | 不是所有课都值得转 Skill。课不科学→后面七步都是浪费 | 结论：做/不做 + 定位 |
| **2. 整理课程主线** | 把讲稿/逐字稿/作业整理成结构化 Markdown，过滤噪声 | AI 需要干净的上下文，"垃圾进垃圾出" | 课程主文档 |
| **3. 抽取案例库** | 把稿子里的案例、问答、行业应用抽出来 | **案例库是 Skill 稳定性的底座**，没有案例就没有反例校准 | 案例库 + 问答示范库 |
| **4. 写诊断协议** | 把方法变成可执行流程：场景分类 / 评分规则 / 风险分级 | 让 Skill 会拒绝、会评分、会分级，而不是只生成内容 | Skill 核心协议 |
| **5. 证据校准** | 区分"课程经验"和"外部证据"，标注时间、地域、来源 | 课程观点只是候选参考，必须经过反例和边界校准 | 审查过的证据链 |
| **6. 建工程目录** | 按工程化方式组织——不只是一个 prompt 文件 | 否则迭代时找不到案例库、测试记录和版本差异 | Skill 目录结构 |
| **7. 测试 + 反例** | A/B 测试：用 Skill vs 不用 Skill。设定通过线（≥28 分可用） | 没有通过线的工具无法判断可用性 | 测试报告 |
| **8. 安装/调试/迭代/写文档** | 部署 + 持续优化 | 让 Skill 能被他人复用和升级 | 可用的 Skill + 文档 |

### 三个关键判断

**判断一：课程能不能转 Skill？**

半肥猫说了一句很重的话："不是每一堂课都像一堂的课是科学的。外面很多老师讲的课是东拼西凑的。那些经不起考验的内容，不要做。"

判断标准：课程有科学方法 + 可验证案例 + 明确边界 → 可以做。否则跳过。

**判断二：做成什么类型？**

目标定位极其重要——"做成实验约束型转化率方案推演的 skill，不需要做成转化率万能提效的"。**收窄目标 = 提高可靠性。**

**判断三：证据校准是必须的**

半肥猫原话："我看过很多人写的 skill，GitHub 上开源很多 skill，我一看看设计思路，但是我不去用它。因为那些内容就是用 AIGC 写出来的，没有证据链的，没有做过审查的。一帮程序员坐在里面为了刷积分写出来的。"

**Skill 的可信度不在于 prompt 写的多好——在于证据链有没有校准过。**

## 结果

### 可量化结果

| 指标 | 不用 Skill | 用 Skill | 差值 |
|:---|:---:|:---:|:---:|
| 转化率方案评分 | 8 分 | 36 分 | **+28 分** |
| 输出边界 | 无 | 明确适用/不适用场景 | 显著 |
| 风险分级 | 无 | 高/中/低三级 | 显著 |
| 拒绝能力 | 无 | 场景不对即拒绝 | 显著 |

### 关键产物

1. **课程主文档**：《转化率黑客五组合落地》结构化 Markdown
2. **案例库**：真实学员案例 + 行业应用问答
3. **诊断协议**：场景分类、评分规则、风险分级
4. **证据链**：课程经验 vs 外部数据标注
5. **工程目录**：manifest + 案例库 + eval + docs
6. **测试报告**：A/B 测试对照与通过线记录

### 本质差异

半肥猫的 A/B 测试不是"用 AI 比不用 AI 好"——是"加了工程约束的 AI 比裸 AI 好 28 分"。裸 AI 的问题不是"不够聪明"，是"太讨好"。半肥猫的 Skill 做了三件裸 AI 不会做的事：

1. **会拒绝**：场景不对就说"不建议用"
2. **会评分**：不是笼统方案，是打分
3. **会分级**：高风险场景不胡说

这与 [[yt-business-analysis-cognitive-biases]] 中提到的"框架不能自动克服认知偏差"互为补充：Skill 的工程约束就是用来对抗 AI 讨好偏差的结构化手段。

## 可迁移场景

1. **任何"有科学方法 + 可验证案例"的课程都可以走这套流程**：一堂的转化率/产品内核/Y模型等课程天然适合。
2. **KDO 的 `kdo encapsulate` + manifest 模式**：半肥猫的八步流程可以直接对接到 KDO 的 manifest → 编译 → 测试 → 发布管线（参考 [[kdo-ec-industrialization-migration-proposal]] 中的门禁思想）。
3. **团队内部知识→工具的转化**：不限于课程——任何已验证的内部方法论都可以按这个流程编译为 Skill（与 [[case-纪浩-from-zip-to-five-layers]] 中的 Skills Market 需求同构）。
4. **个人知识库建设**：把 [[yt-five-step-level-blindspots]] 中的段位盲区自检嵌入到 Skill 中，避免"以为自己会了但实际不会"。

## 诊断信号

以下信号出现时，说明当前做法偏离了课程转 Skill 的工程化标准：

| 信号 | 镜头 | 跟进问题 |
|:---|:---|:---|
| 通用 AI 输出流畅但无评分、无边界、无风险分级 | 缺少诊断协议与边界约束 | 你的 Skill 有没有明确的评分规则、适用边界和风险分级？ |
| 课程听完了，笔记做了很多，真实问题仍从头开始 | 知识未工程化为可调用 Skill | 核心方法能不能写成"输入→处理→输出→校验"四段式协议？ |
| AI 工具输出很流畅但不敢在真实决策中使用 | 证据链未校准 | 每条关键 claim 是否有来源？哪些是个人经验、外部数据、缺少反例？ |
| 团队里 prompt 无法复用、版本混乱 | 缺少工程化目录与封装机制 | Skill 是否有 manifest、测试用例、版本记录和安装文档？ |

## Constraints & Boundaries

### 适用边界

| 边界 | 说明 |
|:-----|:------|
| ✅ 课程有科学方法 + 可验证案例 + 明确边界 | 一堂转化率/产品内核/Y模型等课程天然适合；东拼西凑的课程第一步就应拒绝 |
| ✅ 有明确的真实问题和使用者 | 解决具体业务问题，而不是"为了有一个 Skill" |
| ✅ 有时间做证据校准和 A/B 测试 | 八步法中第 5、7 步不能跳过，需要投入额外时间 |
| ✅ 目标窄、场景单一 | "实验约束型转化率方案推演"比"万能转化率提升助手"更可靠 |
| ✅ 已有结构化的 Markdown/笔记资料 | 原始资料需要先整理成干净上下文，否则先补第 2 步 |

### 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:------|:------|
| **把课程逐字稿直接当 prompt** | AI 输出听起来很专业，但遇到真实场景就偏离，没有拒绝能力 | 先做"判断→整理→抽案例→写协议"四步，再生成 prompt |
| **目标定成"万能转化率提升助手"** | 输出泛泛而谈，用户不敢用，A/B 测试分数低 | 收窄为"实验约束型转化率方案推演"，明确"不解决什么" |
| **跳过证据校准** | AI 引用过期数据/宏观叙事/不相关案例，看起来流畅但不可靠 | 区分课程经验/外部证据/缺反例声明；标注时间、地域、来源 |
| **没有 A/B 测试和通过线** | 上线后不知道好不好，用户反馈两极分化 | 设计"用 Skill vs 不用 Skill"对照，设定通过线（如 ≥28 分可用） |
| **工程目录只有一个 prompt 文件** | 迭代时找不到案例库、测试记录、版本差异 | 按 manifest + case 库 + eval + docs 四目录组织 |

## 工具：课程转 Skill 预检清单

在启动八步流程前，用下面 10 个问题自检。如果 ≥3 题答案为"否"，先回到准备阶段：

| # | 检查项 | 是/否 | 备注 |
|:--:|:---|:---:|:---|
| 1 | 这门课是否有明确的科学方法和可验证案例？ | ☐ | 参考半肥猫判断标准一 |
| 2 | 是否已定位到要解决的真实问题和使用者？ | ☐ | 避免"为了有 Skill 而做" |
| 3 | 是否有足够的时间做证据校准（≥课程转写时间的 30%）？ | ☐ | 第 5 步不能省 |
| 4 | 是否能把目标收窄到单一、可验证的场景？ | ☐ | 例如"转化率方案推演"而非"万能提升" |
| 5 | 课程资料是否已整理成结构化 Markdown？ | ☐ | 去除噪音，保留方法、案例、边界 |
| 6 | 是否已抽取 ≥3 个真实案例用于案例库？ | ☐ | 案例库是 Skill 稳定性的底座 |
| 7 | 诊断协议是否包含评分规则和风险分级？ | ☐ | 让 Skill 会拒绝、会评分 |
| 8 | 是否已设计 A/B 测试方案和通过线？ | ☐ | 如"用 Skill 36 分 vs 不用 8 分，差值 ≥28" |
| 9 | 工程目录是否包含 manifest / case / eval / docs？ | ☐ | 不是单文件 prompt |
| 10 | 是否有明确的安装、调试、迭代文档？ | ☐ | 否则无法复用 |

## 对 KDO 的直接启发

半肥猫的八步流程 = KDO 的 **manifest → encapsulate → publish** 管线的手工版。他做的每一步在 KDO 里都有等价物：

| 半肥猫的八步 | KDO 等价物 | 状态 |
|:--:|:---|:--:|
| 1. 判断是否值得 | 四要素验证 + dk 经验库 | ✅ case 卡可做参考 |
| 2. 整理主线 | `kdo ingest` + `kdo enrich` | ✅ |
| 3. 抽取案例 | case 卡 + 案例库 | 🟡 刚建 |
| 4. 写诊断协议 | manifest.yaml（capabilities + constraints） | ✅ |
| 5. 证据校准 | source_refs 溯源 + lint 校验 | ✅ |
| 6. 建工程目录 | `40_outputs/capabilities/skills/<id>/` | ✅ |
| 7. 测试+反例 | `kdo skill validate`（eval cases 结构校验 + 覆盖率报告） | ✅ |
| 8. 装调迭 | `kdo publish` + `kdo install` | ✅ |

这与 [[modeling-capability-for-kdo]] 中"kdo/wiki 的建设本质上就是在做一条从原始素材到结构化知识的建模流水线"的判断一致：课程转 Skill 是 KDO 内容建模能力的一个具体实例。

---

## 黄药师分析：三层理解

### 第一层：八步流程是软件工程思维用在 Skill 建设上

每一步有输入、有产出、有通过标准。最值钱的两步：

**第 4 步"写诊断协议"**是 Skill 的骨架。不是"AI 帮你分析转化率"——是定义了场景分类、评分规则、风险分级。评分规则让输出可量化（36 vs 8），风险分级让 Skill 知道什么时候闭嘴。Truman 的"L1-L2 硬边界"在这里变成了可执行的协议字段。

**第 5 步"证据校准"**是价值观判断，不是技术判断。半肥猫原话："GitHub 上开源很多 skill 我不敢用。那些内容是用 AIGC 写出来的，没有证据链的，没有做过审查的。"Skill 的可信度不在于 prompt 写得多好——在于证据链有没有校准过。这和 Truman 的"1500 篇模型笔记不是训练数据，是验证过的知识"完全同构。

### 第二层：36 vs 8 的本质——加了工程约束的 AI vs 裸 AI

半肥猫的 A/B 测试不是"用 AI 比不用 AI 好"——是"加了工程约束的 AI 比裸 AI 好 28 分"。

裸 AI 的问题不是"不够聪明"，是"太讨好"。问它"怎么提高转化率"，它给你一个流畅、完整、看起来很有道理的回答——但那个回答没有评分、没有风险分级、没有"这个场景不建议用"的拒绝能力。

半肥猫的 Skill 做了三件裸 AI 不会做的事：① 会拒绝（场景不对就说"不建议用"）② 会评分（不是笼统方案，是打分）③ 会分级（高风险场景不胡说）。

这就是 Truman 的"P 角色不是 C 角色"的工程实现。裸 AI 是 C 角色——你说什么它都顺着你说。半肥猫的 Skill 是 P 角色——只做协议里定义的事，该闭嘴就闭嘴。

### 第三层：KDO 八步全有等价物——Agent 做，人判断

八步全部有 KDO 等价物（见上表）。但关键的两步不是全自动的——是"Agent 做，人判断"：

**第 5 步"证据校准"**：Agent 可以帮做——让 AI 扫描课程中的每条 claim，标注哪些有引用来源、哪些是老师个人经验、哪些缺反例。但**判断**这件事必须由人做——这个证据够不够？这个反例对不对？半肥猫和课程官方沟通了两三个月做访谈，这个过程 Agent 替代不了。

**第 7 步"A/B 测试"**：Agent 可以设计测试方案、跑两组对照、输出分数。但**判断**——28 分的差值够不够？测试场景是不是覆盖了边界？——由人做。

这和 KDO 的角色分工完全一致：老顽童（Producer/Agent）写卡，欧阳锋（Architect/人）审查判断。Truman 说的"L4-L5 必须由人来做"不是说 Agent 不能参与这些步骤——是说**判断权不能外包**。

---

## 单卡收尾检查

- [x] `status` 已从 `draft` 改为 `enriched`
- [x] `reviewed_by` 已更新为 `老顽童`
- [x] `updated_at` 已更新为 `2026-06-17`
- [x] `diagnostic_signals` ≥ 3（实际 4 条）
- [x] 适用边界 ≥ 4（实际 5 条）
- [x] 常见失败模式 ≥ 4（实际 5 条），每条含真实症状 + 可执行修复
- [x] 新增至少 1 个模板/checklist（课程转 Skill 预检清单）
- [x] 新增至少 2 条互链（实际新增 5 条：[[case-纪浩-from-zip-to-five-layers]]、[[kdo-ec-industrialization-migration-proposal]]、[[modeling-capability-for-kdo]]、[[yt-business-analysis-cognitive-biases]]、[[yt-five-step-level-blindspots]]）
- [x] 正文包含 Background / What Happened / 结果 / 可迁移 / 诊断信号 / Constraints & Boundaries / 常见失败模式
