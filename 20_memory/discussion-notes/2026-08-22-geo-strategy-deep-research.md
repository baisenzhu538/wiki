# GEO 战略深度调研 · 认知简报

> 日期：2026-08-22（供 08-23 讨论）｜作者：小昭（外部协同）
> 目的：在「GEO 一致性核对」基础上，补全全网深度调研，形成可讨论的认知框架。**建卡延后到讨论之后**。
> 配套文件：`2026-08-22-geo-strategy-consistency-check.md`（结论：与 KDO 现有卡不冲突，三处印证，缺专属 GEO 范式卡）

---

## 0. TL;DR（一句话认知）

**GEO 不是 SEO 的替代品，而是 SEO 在"AI 生成式回答"场景下的能力延展。**
优化单元从「页面排名」升级为「段落级引用」，成败取决于三件事：

- **找得到**：技术可索引 + AI 爬虫未被 robots.txt 误拦
- **用得上**：首段直答 + 结构化 + Schema 机器可读
- **查得证**：实体权威 + 第一手数据 + 可追溯来源

> 心智模型：SEO 让页面"能被读"，GEO 让内容"能被引用"。**SEO 是 GEO 的前提地基，不是竞品。**

---

## 1. 范式转移：从「排名/点击」到「引用/提及」

### 1.1 AI 搜索的三阶段（RAG 心智模型）
生成式引擎（ChatGPT / Perplexity / Gemini / Google AI Overviews）的工作流：

1. **查询改写**（LLM 把问题拆成子查询）
2. **文档检索**（索引返回候选页）
3. **综合生成**（LLM 从多源合成一个带引用的答案）

→ 读者无需点击即可获得完整答案，**你没有"排名"这个仪表盘，只有"是否被引用"这个结果**。

### 1.2 零点击现实（为什么 GEO 不再是选修）
| 数据 | 来源 | 含义 |
|---|---|---|
| 68% Google 搜索无点击（2026） | SparkToro 2026 clickstream | 比两年前 60% 继续恶化 |
| AIO 出现使首条 CTR 降约 60% | Ahrefs | 即便排第一也几乎没点击 |
| AIO 首条位置 CTR 仅 2.6% | TheStacc | 蓝链排名的流量价值锐减 |

→ 可见性不再等于流量。**必须同时赢两局**：出现在结果页 + 出现在答案里。

---

## 2. SEO vs GEO 核心差异（不是替代，是叠加）

| 维度 | SEO | GEO |
|---|---|---|
| 优化单元 | 页面（Page） | 段落/区块（Section） |
| 成功指标 | 排名位置、CTR、自然流量 | 引用率、品牌提及、答案占比 |
| 信任信号 | 外链、域名权重 | 品牌提及、实体权威、被识别的实体 |
| 内容形态 | 长文围绕关键词 | 自包含、答案前置、可直接抽取 |
| 检索路径 | 抓取→索引→排名（线性） | 语义检索→重排→综合（网状） |
| 依赖关系 | 独立学科 | **延展 SEO，需 SEO 地基** |

**关键实证（The GEO Lab，2026）：**
- 跨 330 条查询测试：**排名位置与是否被引用相关性很弱**——很多 Google 排名第一的页面，在 AI Overview / Perplexity 中一次都没出现。
- Experiment 001（30 条查询）：同样 SEO 信号，叙事结构被引 36.7%（11/30），声明式结构被引 **60.0%**（18/30）。结构本身带来 23.3 个百分点的引用率差。
- 结论：强 SEO ≠ 自动被 AI 引用。GEO 是叠在 SEO 之上的额外一层。

---

## 3. 被 AI 引用的底层机制：三门槛

把"被引用"拆成可操作的三道门槛，每一道都不满足就出局：

### 门槛一：找得到（技术可索引 + AI 爬虫放行）
- 反向证据：SAGEO Arena（Yonsei, 2026）测试真实 RAG 全管道，发现**纯正文优化对检索反而 -9%、重排 -16%**；而标题/元信息/Schema 等结构性优化使**检索 +22%**。结构驱动检索，正文驱动引用，二者互补。
- 致命坑：UofT 比较研究（arXiv:2509.08919）显示 AI 引擎对**品牌自有内容**引用占比极低，**earned media（第三方权威媒体）占 53–95%** 的引用（ChatGPT 90–95%、Perplexity 53–74%、Claude 82–93%、Gemini 63–67%）；社媒在所有垂直领域 AI 搜索中降到 **0%**。

### 门槛二：用得上（首段直答 + 结构化 + Schema）
- 70% 的引用来自页面**前 500 字**（国内 GEO 实操数据）；首段 100–200 字内给出结论性直答。
- 表格、对比页、FAQ 是 AI 最易抽取的形态。案例研究中"对比页"单页贡献了 **40% 的新增引用**。

### 门槛三：查得证（实体权威 + 第一手数据 + 可追溯来源）
- 品牌提及与 AI 可见度相关系数 **0.664**，远高于反链 0.218（ContentForce 实体 SEO 研究）。
- Wikipedia 占 ChatGPT 顶部引用来源 **47.9%**；5W Research：Wikipedia + Reddit 合计驱动美国 ChatGPT 引用 **25%+**。
- 第一手原创数据/研究是最高杠杆——AI 偏爱"可被验证的事实"。

---

## 4. 学术证据：Princeton 九法 + 2025–2026 新论文

### 4.1 奠基论文（Princeton + IIT Delhi，KDD 2024，arXiv:2311.09735）
测试 9 种内容改写方法 × 10,000 查询 × 25 领域 × 3 个生成引擎。度量用 **PAWC（Position-Adjusted Word Count，位置加权词数占比）**：

| 方法 | 效果（PAWC 提升） | 类别 |
|---|---|---|
| 加直接引语（Quotation） | **+40–44%** | 新增证据 |
| 加统计数据（Statistics） | +30–40% | 新增证据 |
| 加来源引用（Cite Sources） | +30–40% | 新增证据 |
| 流畅度优化（Fluency） | +15–30% | 呈现改写 |
| 易理解（Easy-to-Understand） | +14% | 呈现改写 |
| 权威语气（Authoritative Tone） | +10% | 呈现改写 |
| 独特用词（Unique Words） | +6% | 呈现改写 |
| **关键词堆砌（Keyword Stuffing）** | **−8 ~ −10%** | 传统 SEO，**有害** |

> 结论：加"真实证据"的方法赢；老派关键词玩法对 AI 引用几乎零作用甚至负作用。

### 4.2 2025–2026 新论文（领域三年内的核心进展）
| 论文 | 机构 / 时间 | 关键发现 |
|---|---|---|
| **GEO-16 Framework** | UC Berkeley, 2025-09, arXiv:2509.10762 | 16 个结构因子与引用相关 0.63–0.68；≥12 个支柱落地时引用率 72–78%，8–11 个时 30–50% |
| **SAGEO Arena** | Yonsei, 2026-02, arXiv:2602.12187 | 首个测"真实 RAG 全管道"的基准：纯正文优化在真实检索下失败，结构优化 +22% 检索命中 |
| **UofT 比较研究** | Toronto + ktau.ai, arXiv:2509.08919 | 跨引擎证实 earned media 压倒性主导；媒体信任层级：同行评审 > 主流媒体 > 行业媒体 > 专家 > 品牌自有 |
| **AutoGEO** | CMU, ICLR 2026 | 首个自动化 GEO 优化框架（LLM 改写批量落地） |
| **Lost in the Middle** | Stanford, 2023 | 位置偏见：信息位置显著影响被抽取概率 |

> 四篇必读顺序：原始 GEO 论文 → UofT 比较 → AutoGEO → SAGEO Arena，构成"是什么→跨引擎表现→如何自动化→真实管道表现"的完整弧线。

---

## 5. 实战七杠杆（按影响力排序）

| # | 杠杆 | 动作 | 证据 | 风险/注意 |
|---|---|---|---|---|
| 1 | **放行 AI 爬虫** | robots.txt 显式 `Allow` GPTBot/OAI-SearchBot/PerplexityBot/ClaudeBot/Google-Extended | 6.9% 站点（6,944 样本）误拦至少一只 AI 爬虫；放行后中位 +16 AI 可见性分（9 天内） | 搜索爬虫≠训练爬虫，可分离；Cloudflare/WAF 默认可能拦 AI 爬虫，覆盖 robots.txt |
| 2 | **首段直答 + 前 500 字** | 首段 100–200 字给结论；每段自包含 | 70% 引用来自前 500 字 | 别堆砌前言/营销套话 |
| 3 | **加可引用证据** | 每个主张配具体数字+来源；加专家直引 | Princeton：引语 +40–44%、统计 +30–40%、来源 +30–40% | 来源须真实可追溯 |
| 4 | **结构化数据 Schema** | JSON-LD：FAQPage / Article / Organization / BreadcrumbList | FAQPage 使 AI 引用概率 **4.2x**（Pendium/Column Five）；Article **1.6x**；GEO-16 结构化数据 OR=4.2；Volpini 2026：JSON-LD 使 RAG 准确率 +29.6% | 2026-01 Google 已弃用 HowTo；canonical 须与 Schema url 一致；用 Rich Results Test 校验 |
| 5 | **实体一致性 / 知识图谱** | Organization schema + sameAs（Wikidata/LinkedIn/Crunchbase）；NAP 全平台一致；作者 Person schema | 品牌提及相关 0.664 vs 反链 0.218；Wikipedia+Reddit 占 ChatGPT 引用 25%+ | 命名/地址/电话不一致会造成实体歧义 |
| 6 | **内容集群 / Topical Authority** | hub-and-spoke：支柱页 + 辐射页互链；深度>数量 | GEO-16：≥12 支柱 72–78% 引用；内部链接即"迷你知识图谱" | 浅覆盖多主题=低实体权威 |
| 7 | **原创数据/研究** | 发布第一手数据、案例、行业研究 | Wikipedia 占 ChatGPT 顶部来源 47.9%，因其"原创+有据" | 不必做 Wikipedia，但须原创可验证 |

**杠杆 1 是地基**：AI 爬虫进不来，后面六个全白做。

---

## 6. 关键统计数据速查表

| 指标 | 数值 | 来源 |
|---|---|---|
| GEO 市场规模（2025） | $8.48 亿 → 2034 年 $337 亿（CAGR 50.5%） | TheStacc |
| 已做 GEO 优化企业报告可见性提升 | 63% | Foundation Inc. |
| 企业 SEO 团队已整合 AI 优化 | 86% | Foundation Inc. |
| 零点击 Google 搜索 | 68%（2026） | SparkToro |
| AIO 使首条 CTR 降幅 | ~60% | Ahrefs |
| Princeton 最高增益（引语） | +40–44% | KDD'24 |
| 关键词堆砌（有害） | −8 ~ −10% | KDD'24 |
| FAQPage Schema 引用倍率 | 4.2x | Pendium/Column Five |
| Article Schema 引用倍率 | 1.6x | Pendium/Column Five |
| 品牌提及 vs AI 可见度相关 | 0.664 | ContentForce |
| 反链 vs AI 可见度相关 | 0.218 | ContentForce |
| Wikipedia 占 ChatGPT 顶部来源 | 47.9% | TheStacc |
| 前 500 字占引用比例 | 70% | 国内实操 |
| earned media 占 AI 引用（区间） | 53–95% | UofT arXiv:2509.08919 |
| 社媒在 AI 搜索引用占比 | 0% | UofT |
| 误拦 AI 爬虫站点比例 | 6.9%（6,944 样本） | SearchScore 2026-07 |
| 放行后中位可见性提升 | +16 分（9 天） | Crawlux |
| GEO-16 结构化数据 OR | 4.2 | UC Berkeley |

---

## 7. 案例证据（证明"有效"，且有时效）

| 案例 | 周期 | 结果 |
|---|---|---|
| Rankio B2B SaaS | 6 周 | 可见性 12→50（+317%），AI 声量 3%→19%，对比页贡献 40% 引用 |
| Rankio 医疗平台 | 10 周 | 从 0 引用 → 相关 AI 答案 70% 被引 |
| Be The Answer PM 工具 | 6 月 | 0→55% ChatGPT 可见性，demo 请求 +23% |
| Be The Answer 法律科技 | 5 月 | 15/30 关键词进 AIO，自然流量 +41%，AI 线索转化 2.1x |
| Prominara（4 行业） | 90 天 | 引用率 2x–5x，GEO 分 +25–45 |
| Brandi GovTech SaaS | 60 天 | AI 可见性 **7x**，竞争排名 #7→#2，70% 优化页 2 周内进 AI 答案 |
| Anqa 加密寿险 | 30 天 | 0→956 用户，60 次 AI 引用，品牌搜索 +340% |
| Inspira 曼谷地产 | ~2 月 | 12 个服务页改写首段直答后，进入 Perplexity + AIO 对比查询引用 |

**时效规律（Be The Answer）：** Perplexity 1–2 周见效 → Google AIO 1–3 月 → ChatGPT 2–4 月。有强 SEO 地基者快得多。

**失败模式：** 只改格式不管权威 / 当一次性项目 / 忽略技术 SEO / 无测量体系——四类都会让 GEO 归零或数月衰减。

---

## 8. 与 KDO 现有卡片的衔接（建卡前的锚点）

| KDO 现有卡 | 与 GEO 的衔接 |
|---|---|
| **渠道经济学**（"渠道不是越多越好，渠道互相蚕食"） | GEO 印证"聚焦垂直 > 多站群撒网"：相似站群（PBN）会被 AI 关联识别、去重降权；正经多品牌独立运营才有利 |
| **品牌三度**（"信任 > 流量"，"只做知名度不做美誉度会塌"） | GEO 的 E-E-A-T / 实体权威 / 品牌提及，正是"信任"的可操作化；AI 引用本质是"信任的机器代理" |
| **飞书发布 SKILL（内置 GEO 优化）** | 已有落地能力（标题关键词、结构化摘要、可引用片段），建 GEO 卡可直接复用，不必从零造 |
| **一服多域架构对 GEO 技术中性**（前次结论） | 架构本身不加分减分；相似站群被去重，独立多品牌有利——决定"哪些站做 GEO、哪些做品牌隔离" |

> 缺口（前次已识别）：KDO 缺专属 **GEO 范式卡**（G1 范式转移 / G2 架构中性 / G3 垂直=topical authority）；raw source `src_20260614_45ab8b35-GEO业务-最佳实践讨论.md` 仍未蒸馏。

---

## 9. 待明天讨论的开放问题（决策点）

1. **建卡形态**：GEO 范式卡走工厂流水线（欧阳锋分发→建卡→终审），还是直接在 `30_wiki` 落 concept/tool 卡？是否把"七杠杆"做成一张 **tool/checklist 卡**？
2. **覆盖边界**：G1/G2/G3 三张范式卡是否够？要不要补"AI 爬虫放行""Schema 优先级栈""实体一致性"三张偏技术/战术的卡？
3. **一服多域落地**：你手里那批站点，哪些该做 GEO（垂直权威型）、哪些该做品牌隔离（防被 AI 关联去重）？需要我先出一版站点清单诊断吗？
4. **测量机制**：用固定 Prompt Panel 定期重测 AI 引用率——跑哪些 prompt、谁来跑、频率？要不要做成可重复的自动化任务？
5. **raw source 蒸馏**：`src_20260614_45ab8b35` 是把 GEO 当"客户委托投放业务"的视角，与"内容被引用"视角有张力，建卡时以哪个为准？

---

## 10. 参考来源（按章节）

**学术 / 论文**
- Aggarwal et al., *GEO: Generative Engine Optimization*, KDD 2024, arXiv:2311.09735
- Kumar & Palkhouski, *GEO-16 Framework*, UC Berkeley, arXiv:2509.10762
- Kim et al., *SAGEO Arena*, Yonsei, arXiv:2602.12187
- Chen et al., *GEO: How to Dominate AI Search*, UofT, arXiv:2509.08919
- Liu et al., *Lost in the Middle*, Stanford, 2023
- Volpini et al. (2026), JSON-LD + RAG 准确率实验

**行业 / 实操**
- TheStacc / Princeton GEO 解读、GEO 市场数据
- The GEO Lab（330 查询排名 vs 引用相关性、Experiment 001）
- typescape.ai、thegeocommunity.com、klientsolutech.com、auspia.ai（GEO vs SEO）
- searchscore.io、crawlux.com、okara.ai、besourceable.com（AI 爬虫 robots.txt）
- overthetopseo.com、contentforce.ai、genrank.io、w3era.com、madx.digital（实体/知识图谱）
- pendium.ai / Column Five、authoritytech.io（Schema / GEO-16）
- rankio.studio、betheanswer.online、prominara.com、mybrandi.ai、wrodium.com、inspiradigitalagency.com（案例）

---

*备注：本简报基于 2026-08-22 发起的全网检索（7 轮并行 + 本轮 6 轮复核），数据点多来自 2025–2026 年论文与行业实测，较 2023 年早期 GEO 内容更可靠。建卡动作按用户指示推迟到讨论之后。*
