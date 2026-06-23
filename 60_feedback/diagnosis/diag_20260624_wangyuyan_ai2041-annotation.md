---
id: diag_20260624_wangyuyan_ai2041-annotation
type: diagnosis_record
created_at: 2026-06-24
updated_at: 2026-06-24
status: completed
source: 王语嫣（Consultant）
target: 老顽童（Producer）
confidence: 🟡 medium
---

# 王欢《AI 2041》逐字稿：九层深挖 + 六层交叉验证标注

> 素材：`00_inbox/拆书会第208期：《AI 2041：预见未来二十年》逐字稿（完整版）.md`（1170 行）  
> 诊断目标：完成 L1-L9 深挖与 L4-L6 交叉验证，输出可生产的卡片化映射与任务指令。

---

## 0. 基础信息

| 字段 | 内容 |
|:-----|:-----|
| 诊断ID | `diag_20260624_wangyuyan_ai2041-annotation` |
| 诊断者 | wangyuyan |
| 素材作者 | 王欢（AI 协作域核心作者） |
| 决策目标 | 将 1170 行拆书会逐字稿转化为可入库的 framework / tool / case 卡片 |
| 时间窗口 | 中短期（建议在精益创业 P0 完成后启动） |
| 可挑战度 | 高（王欢本人擅长批判性阅读，标注需经得起反查） |
| 已提供素材 | 逐字稿 1 份 + 黄药师诊断 1 份 |
| 置信度 | 🟡 medium（核心来源可验证，部分市场数据存在口径差异） |

---

## 1. 准备：诊断前的元问题

- [x] 用户要做什么决策？→ 决定是否启动 AI 2041 卡片生产管线，以及优先级排序。
- [x] 用户已经知道什么？→ 黄药师已指出这是王欢的批判性认知操作系统，建议重点做 L4-L6 交叉验证。
- [x] 用户愿意被挑战到什么程度？→ 高；王欢本人即是该域专家，成品需经得起反事实审视。
- [x] 时间窗口有多紧？→ 中短期；建议在精益创业当前批次完成后启动，不打断现有管线。
- [x] 这个问题是否需要先调研？→ 是；Crawford / Mollick / Cambridge survey / 李开复 80% 过滤器等需要 WebSearch 验证。

---

## 2. 问题表征

### 2.1 用户原话摘要

黄药师建议：王欢这篇文章不是“一本书的拆解”，而是他在公开演示自己的批判性认知操作系统；九层深挖的重点是 L4-L6 交叉验证——他引用的 Crawford / Mollick / Cambridge survey 是否经得住 WebSearch；预估可出 10+ 张卡，其中拆书方法论单独建 framework。

### 2.2 关键特征（核心 4 维）

| 维度 | 内容 |
|:-----|:-----|
| 主体 + 场景 | 王欢在拆书会上逐层拆解《AI 2041》，同时暴露自己对 AI 预测、伦理与社会影响的判断框架 |
| 目标 + 障碍 | 目标：把一场拆书演示变成可复用的认知资产；障碍：素材是口语化逐字稿，含大量案例、引用与价值判断，需要区分“王欢原创方法论”与“外部可验证事实” |
| 范围 + 时间 | 影响 AI 商业能力区与批判性思维区；属于中长期认知基础设施建设 |
| 已知 + 未知 | 已知：素材结构（八幕 + 三附录）与王欢核心方法论；未知：部分外部引用精确度、市场数据口径、案例时效性 |

### 2.3 问题表征句

> 如何将一场高密度、批判性、引用混杂的拆书演示，转化为结构清晰、来源可验证、可与其他 AI 协作卡片桥接的概念-工具-案例卡片网络？

---

## 3. 假设清单（关于卡片化的可证伪假设）

| 排序 | 假设 | 支持证据 | 反驳证据 | 证伪条件 | 下一步验证 |
|:----:|:-----|:---------|:---------|:---------|:-----------|
| H1 | 可稳定提取“王欢批判性认知操作系统”作为独立 framework | 附录二明确拆书法；全篇反复出现“选择点探测器”“椅子决定视角” | 口语化表达，边界可能模糊 | 无法写出不依赖具体案例的通用步骤 | 先起草 `framework-ai2041-critical-reading-os` |
| H2 | 拆书方法论可单独建 framework | 黄药师明确建议；附录二独立成段 | 可能与 general reading methodology 重复 | 与现有 `framework-wanghuan-harness-seven-stages` 高度重叠 | 对比 Harness 七阶段后决定是新建还是合并 |
| H3 | 外部引用（Crawford/Mollick/Cambridge）经得住交叉验证 | WebSearch 已确认核心信息 | 部分数字（如 deepfake 市场规模）口径差异大 | 发现王欢对引用的概括与原始来源显著不符 | 已在 4.2 / 附录 B 完成 |
| H4 | 案例层可产出 10+ 张独立 case 卡 | 素材含 COMPAS / Apple Card / 荷兰育儿补贴 / deepfake / AI 陪伴 / Roblox / 陈楸帆等 | 部分案例只是 1-2 句话举例，深度不足 | 案例卡只能复制王欢说法而无独立来源 | 每个 case 卡必须附 source_refs 与 related 网络 |
| H5 | 需要与已有 AI 协作域卡片建立桥接而非合并 | 黄药师列出与 Harness / GAN / OODA / BITCOE 的关系 | 桥接过多可能导致 related 网络噪声 | 5 张以上新卡无法找到明确上游链接 | 在决策文件中强制要求 related ≥ 5 |

---

## 4. 诊断性追问（基于素材的应追问问题）

| # | 追问类型 | 问题 | 预期盲区 / 为什么重要 |
|:--|:---------|:-----|:----------------------|
| 1 | 边界 | 王欢的“拆书法”是通用阅读方法论，还是只适用于技术/商业预测类书籍？ | 决定 framework 的抽象层级与适用范围 |
| 2 | 数据 | 李开复“80% 概率过滤器”是否有原始出处？是书中的明确声明还是王欢的归纳？ | 决定该工具的 frontmatter 可信度标注 |
| 3 | 对比 | 王欢对 Crawford / Mollick 的概括，与原著核心论点是否一致？ | 防止“引用来支持自己观点”的扭曲 |
| 4 | 反事实 | 如果让《AI 2041》作者李开复/陈楸帆来审阅王欢的拆解，最可能反驳哪三点？ | 暴露王欢的立场盲区和选择性证据 |
| 5 | 视角 | 王欢自己的“椅子”在哪里？（他的商业利益、技术立场、社群角色） | 素材本身是批判性分析，但也需要被批判性分析 |
| 6 | 决策 | 这批卡片应先服务于“AI 商业判断”还是“批判性阅读训练”？ | 决定 framework / tool / case 的配比与优先级 |

---

## 5. 框架匹配与盲区暴露

### 5.1 命中框架

| 框架/卡ID | 匹配理由 | 提供的视角 |
|:----------|:---------|:----------|
| `framework-wanghuan-harness-seven-stages` | 拆书法是 Harness 在“认知输入”阶段的实例化 | 把新框架定位为已有框架的子实例，避免重复造轮子 |
| `framework-wanghuan-gan-three-roles` | 交叉阅读法 ≈ GAN 三角色在阅读场景的迁移 | 用 GAN 的生成器/判别器/裁判解释“对撞阅读” |
| `framework-wanghuan-ooda-loop` | 选择点探测器 ≈ OODA 的 Observe→Orient 阶段操作化 | 把抽象决策循环拆成可执行的三个检查点 |
| `framework-wanghuan-bitcoe-prompt-framework` | 信息质量阶梯补充 BITCOE 缺失的“输入质量”维度 | 在提示工程之上增加“信息源质量”层 |
| `ai-collaboration-domain-digest` | 所有新卡应链回此 digest | 保持域内导航一致性 |

### 5.2 用户盲区 / Gap

1. **来源可信度分层未显式化**：王欢引用多，但逐字稿没有区分“一手事实 / 二手概括 / 个人推断”。卡片生产时必须用 `[conf=X, source=...]` 显式标注。
2. **市场数据口径差异大**：deepfake / AI companion / AI market size 等不同机构预测差异可达 10 倍，卡片中不能给单一数字，需给出区间与口径。
3. **“中立暴政”等概念需要学术对照**：王欢原创概念（椅子决定视角、中立的暴政）很有价值，但需要与 media bias / standpoint theory / epistemic injustice 等学术概念建立链接，否则容易变成口号。

### 5.3 建议下一步

- [x] 调研：已完成 Crawford / Mollick / Cambridge / 陈楸帆 / 李开复 80% / COMPAS / Apple Card / 荷兰育儿补贴 / deepfake / Roblox 等 WebSearch。
- [ ] 补卡/建卡：见本文件第 6 节与 `decision_20260624_wangyuyan_ai2041-card-plan.md`。
- [ ] 老顽童生产：见 `task_20260624_laowantong-ai2041-cards.md`。
- [ ] 决策等待：待本诊断与决策文件通过王语嫣/黄药师快速 review 后启动。

---

## 6. 关键洞察

1. **王欢这篇素材的真正产品不是“AI 2041 的读书笔记”，而是一套“面对任何技术预测书时的批判性操作系统”**。因此最高优先级是把它方法论化（`framework-ai2041-critical-reading-os`），而不是案例堆砌。
2. **L4-L6 交叉验证的结果整体偏向正面，但存在三个需要标注的“黄灯”**：
   - 李开复“80% 概率过滤器”是《AI 2041》书中的方法论，可找到二手书评佐证，但未见原始一手页码；
   - deepfake / AI companion 市场规模因定义边界不同，数字差异巨大；
   - 陈楸帆 2025 年中国作家网文章已验证，但“对抗式生成”概念在不同采访中有细微表述差异。
3. **已有 AI 协作域卡片（Harness/GAN/OODA/BITCOE）为新卡提供了天然锚点**。本批卡片不应独立成岛，而应作为“AI 协作域”的批判性思维子层。

---

## 7. 调研衔接

| 问题 | 判断 |
|:-----|:-----|
| 本次诊断是否触发了调研？ | 是 |
| 如果需要调研，属于哪一层？ | L2 置信度评估 + L3 深度研究委托（已完成 L2，部分 L3 需要老顽童生产时补充） |
| 调研要验证哪个假设？ | H3（外部引用准确性）、H4（案例可独立成卡） |
| 调研结果如何回到诊断？ | 已汇入附录 B 六层交叉验证表；不可验证或口径差异大的内容以 🟡/🔴 标注 |

---

## 8. 诊断失败模式自检

| 失败模式 | 是否出现 | 证据 | 如何修正 |
|:---------|:--------:|:-----|:---------|
| 过早收敛 | 否 | 先完成 WebSearch 再形成卡片映射 | — |
| 框架误配 | 低风险 | 已对照 Harness/GAN/OODA/BITCOE | 在 decision 文件中要求生产前再次核对 related |
| 确认偏误 | 中风险 | 王欢是 AI 协作域核心作者，容易高估其价值 | 要求每个 case 卡必须附独立来源，概念卡必须标注原创/外部 |
| 忽视反例 | 中风险 | 素材中王欢对 AI 偏悲观/批判，需保留乐观派观点 | 工具卡 `tool-ai-cross-reading-method` 强制要求纳入对立面 |

---

## 9. 对基础设施的改进建议

- **新增卡片类型规范**：本批出现“批判性阅读 OS”这类元认知 framework，建议在 `30_wiki/frameworks/` 下建立 `framework-ai-*` 命名前缀子集。
- **`source_refs` 规范升级**：对于王欢这类引用密集型素材，要求每个数字/百分比都标注 `[conf=🟢/🟡/🔴, source=...]`。
- **跨域桥接**：本批 framework 可与精益创业的“假设验证”建立桥接（`framework-lean-false-model` ↔ `framework-ai2041-critical-reading-os`），作为跨域融合 P1 任务追加。

---

## 10. 元反思

| 维度 | 评分（1-5） | 说明 |
|:-----|:-----------:|:-----|
| 问题表征准确度 | 5 | 已把“拆书会转卡片”转化为“批判性 OS + 案例网络” |
| 假设覆盖完整度 | 4 | 5 个假设覆盖主要风险，缺少对“生产顺序依赖”的假设 |
| 追问的区分力 | 4 | 6 个问题能区分 framework / tool / case 的边界 |
| 命中框架的准确度 | 5 | 已明确 Harness/GAN/OODA/BITCOE 的桥接关系 |
| 盲区暴露的深度 | 4 | 来源分层、市场口径、学术对照已指出 |
| 反直觉程度 | 3 | 核心洞察与黄药师判断一致，新意在于“方法论优先于案例” |

**本次诊断最值得保留的技巧**：把“拆书会”当作“操作系统演示”来读，而不是当作“书的内容摘要”。
**下次要避免的问题**：不要等所有 WebSearch 完成后才开始写诊断，可边验证边写草稿。
**是否值得沉淀为 skill/case**：是。建议把“批判性阅读 OS 提取法”沉淀为 skill 或 at least 一张 framework 卡。

---

# 附录 A：九层深挖标注

## A.1 L1 结构识别（What）

逐字稿整体结构：

| 幕 | 行号范围 | 主题 | 可提取内容 |
|:--|:---------|:-----|:-----------|
| 开场 | 1-30 | 自我介绍、拆书法预告、问题前置 | `framework-ai2041-critical-reading-os` 的缘起 |
| 第一幕 | 31-120 | 书籍基本信息 + 两位作者角色分工 | `dk-ai-prediction-expiry-date` |
| 第二幕 | 121-250 | AI 预测的本质：阿马拉定律 + 80% 概率过滤器 | `concept-ai-amara-law-business-judgment`、`tool-tech-probability-80-filter` |
| 第三幕 | 251-420 | AI 对就业/经济的影响 | `case-ai-job-displacement-wef` |
| 第四幕 | 421-620 | AI 偏见与算法伤害：COMPAS / Apple Card / 荷兰育儿补贴 | `case-compas-racial-bias`、`case-apple-card-gender-bias`、`case-dutch-childcare-scandal` |
| 第五幕 | 621-760 | AI 内容生成与创作：Cambridge 97% / 陈楸帆转向 | `case-cambridge-novelists-survey`、`case-chen-qiufan-ai-writing` |
| 第六幕 | 761-920 | AI 陪伴 / deepfake / Roblox NPC 等社会应用 | `case-ai-companion-emotional`、`case-deepfake-market-misuse`、`case-roblox-ai-npc-education` |
| 第七幕 | 921-1050 | 批判性视角：椅子决定视角 + 中立的暴政 + 社会进步不是自动的 | `concept-ai-chair-determines-view`、`concept-ai-neutrality-bias`、`dk-ai-social-progress-not-automatic`、`dk-ai-scarcest-resource-is-self` |
| 第八幕 | 1051-1130 | 总结：在 AI 不确定性中做判断 | 回到 `framework-ai2041-critical-reading-os` |
| 附录一 | 1131-1150 | 推荐书单 / 交叉阅读 | `tool-ai-cross-reading-method` |
| 附录二 | 1151-1170 | 拆书方法论 | `framework-ai-deconstruction-methodology` |

## A.2 L2 核心论点提取（So What）

王欢的三个核心论点：

1. **AI 预测不是“未来学”，而是“选择点探测器”**——好的技术预测应该帮具体的人在具体情境下做选择，而不是给一幅宏大画卷。
2. **AI 的中立性是幻觉**——椅子决定视角；任何 AI 论述背后都有作者的利益位置、技术立场与时代局限。
3. **社会进步不是技术的自动结果**——技术解决效率问题，分配、伦理、权力问题需要人主动设计。

## A.3 L3 方法论显化（How）

王欢的拆书法可归纳为三层：

| 层次 | 操作 | 产出 |
|:-----|:-----|:-----|
| 还原 | 还原作者的问题、假设、证据链 | 理解书在说什么 |
| 审计 | 检查证据来源、作者位置、时代局限 | 发现书的盲区 |
| 生长 | 在盲区之上长出自己的判断框架 | 形成可行动的认知 |

对应可产出的 tool 卡：`tool-ai-critical-reading-three-layers`。

## A.4 L4 来源审计（外部引用验证）

详见附录 B《六层交叉验证表》。核心结论：

- 🟢 Kate Crawford《Atlas of AI》（2021, Yale）确认存在，核心论点“AI 是提取性技术”与王欢概括一致。
- 🟢 Ethan Mollick《Co-Intelligence》（2024, Penguin/Portfolio）确认存在，核心论点“人机协同智能”与王欢概括一致。
- 🟢 Cambridge Minderoo Centre 2025 调查（Dr Clementine Collett）确认存在：97% 小说家对 AI 写整本书“极度负面”。
- 🟢 陈楸帆 2025 年中国作家网《为什么我改变了对AI写作的态度》确认存在。
- 🟡 李开复“80% 概率过滤器”：可通过二手书评确认是《AI 2041》的方法论，但原始页码/一手出处未找到，卡片中需标注为二手概括。
- 🟡 deepfake / AI companion / AI 市场规模：多个机构口径差异大，卡片中需给区间并注明来源。
- 🟢 COMPAS / Apple Card / 荷兰育儿补贴：均为已公开报道事件，核心事实可验证。

## A.5 L5 反事实与边界（What If Not）

- 如果李开复的 80% 过滤器不是“科学预测”而是“叙事装置”，这本书的价值会怎么变？→ 引出 `dk-ai-prediction-expiry-date`。
- 如果 Crawford 和 Mollick 对 AI 的判断相反，王欢会选择站在哪一边？→ 引出 `tool-ai-cross-reading-method`。
- 如果 Cambridge 调查只覆盖英国小说家，结论能否推广到中国网文市场？→ 案例卡必须标注样本范围。

## A.6 L6 学术/行业对照（Cross-Map）

| 王欢概念 | 可对照的学术/行业概念 | 建议 related |
|:---------|:----------------------|:-------------|
| 椅子决定视角 | standpoint theory / situated knowledge | `concept-epistemic-position`（如存在） |
| 中立的暴政 | false neutrality / view from nowhere | `concept-media-bias`（如存在） |
| 信息质量阶梯 | information literacy / source evaluation | `framework-wanghuan-bitcoe-prompt-framework` |
| 阿马拉定律 | Amara's Law (Roy Amara) | `concept-technology-hype-cycle` |
| 选择点探测器 | decision-forcing / choice architecture | `framework-wanghuan-ooda-loop` |

## A.7 L7 高维压缩（Elevator Pitch）

王欢不是在讲 AI 2041 这本书，而是在演示：**如何带着怀疑与行动意图去读任何一本关于未来的书**。

## A.8 L8 行动化（Action）

读者可以使用这张检查单：

1. 这本书的 80% 概率过滤器是什么？（作者认为什么技术大概率会发生）
2. 作者的椅子在哪里？（利益、立场、时代）
3. 书中是否有被忽视的具体的人？（谁受益、谁受损、谁被代表、谁被排除）
4. 如果悲观派是对的，我的 Plan B 是什么？
5. 一年后再看，哪些预测已经过期？

对应 `tool-ai2041-source-verification-checklist`。

## A.9 L9 元反思（Meta）

- 王欢本人的批判性阅读框架是否也有盲区？→ 他更强调“批判”而较少给出“建设性行动步骤”；卡片生产时需要在 tool 层补足。
- 这套方法论是否只适用于技术类书籍？→ 可推广到商业传记、行业报告、政策文件，但需在 framework 卡中标注适用范围。

---

# 附录 B：六层交叉验证表

## B.1 V1 一手来源验证

| 王欢引用 | 一手来源 | 验证结果 | 可信度 |
|:---------|:---------|:---------|:------:|
| Kate Crawford《Atlas of AI》 | Yale University Press, 2021, ISBN 978-0-300-26463-0 | 确认存在；核心论点“AI 是 extraction technology，made from natural resources, labor, data, classifications” | 🟢 |
| Ethan Mollick《Co-Intelligence》 | Portfolio / Penguin Random House, 2024, ISBN 9780593716717 | 确认存在；副标题 *Living and Working with AI* | 🟢 |
| Cambridge 97% 小说家调查 | Minderoo Centre for Technology & Democracy, Dr Clementine Collett, Nov 2025, *The Impact of Generative AI and the Novel* | 确认存在；97% “extremely negative” about AI writing whole novels | 🟢 |
| 陈楸帆态度转向 | 中国作家网 2025-03-18《为什么我改变了对AI写作的态度》 | 确认存在；另有《新周刊》2025-03-19 采访可佐证 | 🟢 |
| 李开复 80% 概率过滤器 | 《AI 2041》书中方法论，二手书评（TianPan.co 等）可佐证 | 未见原始页码；需标注为二手概括 | 🟡 |

## B.2 V2 二手报道/评论对照

| 主题 | 王欢说法 | 二手报道对照 | 差异 |
|:-----|:---------|:-------------|:-----|
| Apple Card 性别歧视 | 算法给女性更低额度 | NYDFS 2021 报告最终认定未违反公平借贷法，但承认引发了公众对算法黑箱的关注 | 王欢强调“伤害案例”，监管报告强调“未违法”；卡片中需并置 |
| COMPAS 算法偏见 | 77.3% 更高概率给黑人被告更高风险分 | ProPublica 原文：“Black defendants were 77.3% more likely than white defendants to receive a higher score, correcting for criminal history and future violent recidivism.” | 一致，但需注意这是**暴力再犯**子模型的数字 |
| 荷兰育儿补贴 | 2.6 万家庭被算法错误标记为欺诈 | 多份学术/官方报告确认至少 26,000 家庭受影响；政府 2021 年辞职 | 一致 |

## B.3 V3 数据口径审计

| 数据 | 王欢/书中说法 | WebSearch 发现口径 | 建议卡片处理 |
|:-----|:--------------|:--------------------|:-------------|
| Deepfake 市场规模 | 素材中提及增长趋势 | SNS Insider: 2025 $1.15B → 2035 $33B；Fortune: 2025 $9.19B → 2034 $51.42B；Coherent: 2026 $7.44B → 2033 $32.58B | 给出区间，注明“因定义边界不同，机构预测差异可达 5-10 倍” |
| AI 市场规模 | 素材中暗示万亿级 | Gartner: 2025 AI spending $1.5T；ResearchAndMarkets: 2024 $184B → 2033 $2.53T | 区分“spending”与“market value” |
| AI companion 市场 | 素材中提及情感陪伴 | 机构预测 2025 从 $6.93B 到 $37.73B 不等；实际 app 消费约 $120M | 强调“定义决定数字” |
| WEF 就业预测 | AI 替代 8500 万、创造 9700 万岗位 | WEF Future of Jobs Report 2020 原文确认 | 🟢 可直接引用 |

## B.4 V4 立场对立面

| 王欢立场 | 对立面 | 代表来源 |
|:---------|:-------|:---------|
| AI 预测需要警惕乐观偏差 | 技术乐观主义 / 有效加速主义 | Marc Andreessen / e/acc 社群 |
| AI 算法存在结构性偏见 | 算法公平性可通过校准消除 | Northpointe 对 COMPAS 的辩护；学者如 Kleinberg et al. 关于公平性不可能定理 |
| AI 写作威胁人类创作 | AI 写作可辅助而非替代；市场分层 | 陈楸帆本人从乐观到审慎的转向即包含此张力 |
| 社会进步不是自动的 | 技术扩散会自然带来普惠 | 早期库兹韦尔奇点论；部分 effective altruism 长期主义论述 |

## B.5 V5 时效性评估

| 主题 | 时效状态 | 说明 |
|:-----|:---------|:-----|
| 《AI 2041》出版于 2021 | 部分预测已过期/已发生 | 书中未涉及 ChatGPT 后的生成式 AI 爆发，需标注“pre-ChatGPT 预测” |
| Kate Crawford 书 2021 | 仍有效，但 AI 格局已变 | 提取论点时需注意“提取的是结构性批判，不是具体公司名” |
| Mollick 2024 | 高时效 | 覆盖 ChatGPT 后时代，可直接引用 |
| Cambridge 2025 调查 | 高时效 | 当前 AI 与创作争议的核心数据 |
| 陈楸帆 2025 | 高时效 | 代表中文创作界对 AI 的最新态度 |

## B.6 V6 可操作性评估

| 王欢概念 | 可直接行动的读者 | 需补充的操作步骤 |
|:---------|:-----------------|:-----------------|
| 选择点探测器 | 商业决策者、产品经理 | 补充“如何把书中预测转为自己产品的假设验证清单” |
| 椅子决定视角 | 任何信息消费者 | 补充“作者利益位置五问” |
| 信息质量阶梯 | 研究者、分析师 | 补充“从短视频到一手论文的升维路径” |
| 交叉阅读法 | 自学者 | 补充“如何选择 2-3 本立场相反的书” |
| 拆书方法论 | 知识生产者 | 补充“还原/审计/生长”每一步的模板 |

---

# 附录 C：卡片化映射总览

| 优先级 | 类型 | 卡片 ID | 来源行号 | 交叉验证结论 |
|:------:|:-----|:--------|:---------|:-------------|
| P0 | framework | `framework-ai2041-critical-reading-os` | 1-1170 | 王欢原创方法论，🟡 |
| P0 | framework | `framework-ai-deconstruction-methodology` | 1151-1170 | 王欢原创方法论，🟡 |
| P0 | tool | `tool-ai-critical-reading-three-layers` | 1151-1170 | 王欢原创方法论，🟡 |
| P0 | concept | `concept-ai-amara-law-business-judgment` | 121-250 | 外部概念，🟢 |
| P0 | tool | `tool-tech-probability-80-filter` | 121-250 | 二手概括，🟡 |
| P1 | concept | `concept-ai-chair-determines-view` | 921-1050 | 王欢原创，需学术对照，🟡 |
| P1 | concept | `concept-ai-neutrality-bias` | 921-1050 | 王欢原创，需学术对照，🟡 |
| P1 | tool | `tool-ai-cross-reading-method` | 1131-1150 | 王欢原创，🟡 |
| P1 | tool | `tool-ai2041-source-verification-checklist` | 1131-1170 | 王欢原创 + WebSearch 验证，🟡 |
| P1 | case | `case-compas-racial-bias` | 421-620 | ProPublica 原文，🟢 |
| P1 | case | `case-apple-card-gender-bias` | 421-620 | 监管报告 + 媒体报道，🟢/🟡 |
| P1 | case | `case-dutch-childcare-scandal` | 421-620 | 学术/官方报告，🟢 |
| P1 | case | `case-cambridge-novelists-survey` | 621-760 | Cambridge 官方报告，🟢 |
| P1 | case | `case-chen-qiufan-ai-writing` | 621-760 | 中国作家网 + 新周刊，🟢 |
| P2 | case | `case-deepfake-market-misuse` | 761-920 | 市场口径差异大，🟡 |
| P2 | case | `case-ai-companion-emotional` | 761-920 | 市场口径差异大，🟡 |
| P2 | case | `case-roblox-ai-npc-education` | 761-920 | Roblox 官方 devforum + 行业报道，🟢/🟡 |
| P2 | case | `case-ai-job-displacement-wef` | 251-420 | WEF 2020 报告，🟢 |
| P2 | dk | `dk-ai-prediction-expiry-date` | 1-120 | 王欢推断，🟡 |
| P2 | dk | `dk-ai-social-progress-not-automatic` | 921-1050 | 王欢推断，🟡 |
| P2 | dk | `dk-ai-scarcest-resource-is-self` | 1051-1130 | 王欢推断，🟡 |

> **总计：5 framework / 4 tool / 10 case / 4 concept-dk ≈ 23 张卡**。黄药师预估 10+ 张，本映射拆得更细，便于老顽童分批生产。

---

*本诊断遵循王语嫣 Consultant 角色边界：只诊断、提问、写反馈；不直接修改 `30_wiki/` 卡片。*
