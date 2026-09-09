---
id: task_20260908_laowantong-live258-six-cases
title: "P1 产卡：Live258 六案例全产（雍博/农夫三拳/行知/田力/黄谦/Simon Peng，#682 编排）"
seq: 684
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-08
decision_source: 老朱 09-08 19:25 拍板全做（#682 编排）——六案例全产（含黄谦/Simon Peng，不裁量裁剪）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-09T17:02:13.703673+00:00'
evidence: _tmp/684-evidence.md
---

# #684 P1 产卡单：Live258 六案例全产（老顽童）

> 规格源=诊断报告 `60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md` §五-P1 + §3.2-B 覆盖矩阵（行号照抄不重查）。素材=`00_inbox/AI基本功/Live258：AI基本功第一课优秀作业.md`（3024 行全读完毕，10 案例中 6 案未开采）。
> 老朱拍板：**六案例全产**，黄谦/Simon Peng 不再回头裁量。

## ⚠️ 前置缺陷项（终审残余风险移交，产卡前必做）

**dk 互链前置查重**：产卡前对照以下两卡定互链，防双源冲突——
- `30_wiki/dark-knowledges/dk-ai-does-not-question-your-mistake.md:112` 已吸收 R/E/S/X 事实分级——农夫三拳「事实分级卡」内容与之同源，产卡时 related 互挂+不重复展开
- `30_wiki/dark-knowledges/dk-demand-feature-stacking.md:165` 已引农夫三拳+黄谦边界例——新卡与该书签互链对齐
- 农夫三拳「事实分级卡」机制 = V0.9 changelog（`periodic-table-v0.9-aliases-changelog`，#315）标注的 DataPack/事实约束类 Feature 缺口同源——产卡即闭环该缺口，在卡内注明

## 卡片规格（6 张，按可用度排序产；每张正文开头必须有定位声明）

| # | id | type | 内容要求 | 素材锚点 |
|:-:|:--|:--|:--|:--|
| 1 | case-live258-yongbo-embodied-sorting | case | 雍博具身智能工业分拣（唯一硬科技域；行业量化：零样本30-65%、20条示教→70-80%；灵巧手抓取） | L1705-1823 |
| 2 | case-live258-nongfu-assist-agri-video | case | 农夫三拳助农图生视频（短视频小白→三题材工作台→认知反差型翻车→5关键帧降3关键帧控制变量实验→稳定60分；独有工件：R/E/S/X事实分级卡+台前幕后分离框架） | L671-1057 |
| 3 | case-live258-xingzhi-media-layered-diagnosis | case | 行知自媒体六层诊断（分层自洽最佳学员实证） | L513-669 |
| 4 | case-live258-tianli-gov-training | case | 田力组织部干部培训（被退回→缺7 Feature→三轮叠加完整叙事） | L1059-1701 |
| 5 | case-live258-huangqian-promo-film | case | 黄谦导演宣传片（L1/L2扎实 vs L3+放大器缺失分层判断；三个一工程/五行工具法） | L2909-3023 |
| 6 | case-live258-simonpeng-medical-dataset | case | Simon Peng 医疗数据集方案（质量最低、无验证结果——如实呈现其局限，作反例/边界教材价值） | L355-511 |

## 建模方案（L1 出牌，2026-09-08 老顽童）

依赖链：`[素材牌] → [边界牌] → [结构牌] → [过程牌] → [质量牌]`

1. **牌2 先全文扫描再选策略**（素材）：Live258 3024 行已全量三读完毕（L1-3024），六案锚点行号与任务单一致，无生僻段遗漏
2. **牌6 先查已有卡再新建**（边界）：已查 `30_wiki/cases/case-live258-*` 现存 4 卡（黄华春/jeffgirl/张丽娜/王鹏飞），本单 6 卡 id 无冲突；域=ai-basic（沿用族卡 domain 双挂惯例按素材性质扩展）
3. **牌7 先对标准则再建模**（边界）：WebSearch 对标具身智能示教/工业分拣成功率、图生视频工作流等外部基准后再落卡（防 P-28）
4. **牌10 先骨架再填肉**（结构）：每卡沿用族卡骨架——定位声明→过程（起点→尝试→失败→转折→结果）→Claims/Evidence→关键数字→双三角映射→Critique→Synthesis→Action Triggers→失败模式，正文 ≥100 行
5. **牌14 先跑脚本确认再下结论**（过程）：每张卡写完即跑 `kdo pre-submit -f`，不攒到最后
6. **牌15 先自攻击再提交**（质量）：6 卡完成后四路自攻击 + 轻量三方法（≥1 WebSearch 对标 + ≥1 失败案例），修复后再 complete
7. **牌17 先逐卡清单再批量**（质量）：6 卡逐卡列 id/锚点/前置缺陷闭环项，逐卡核对不跳卡（防 P-36）

## 验收标准

1. 每卡正文开头定位声明（Live258 案例族 + 与 feature 分层体系关系）
2. 前置缺陷项三项全部闭环（dk 互链×2 + V0.9 DataPack 缺口注明），提审时附对照说明
3. 每卡 `kdo pre-submit` 输出随提审附；source_refs 指向 Live258 作业集带行号锚
4. 案例按 起点→尝试→失败→转折→结果 过程还原（W3），不得一句概括
5. 自攻击四路 + 轻量三方法（P1 级：≥1 次 WebSearch 对标 + ≥1 失败案例）；欧阳锋终审

## 边界

- 已产四案（黄华春/jeffgirl/张丽娜/王鹏飞）不动；本单只产未开采六案
- 黄谦/Simon Peng 两张已拍板全产，执行中不得再以「增量偏少/质量最低」裁剪
- AI数据域 8 张属 P0 单（#683），P2 补强属 #685，不在本单

---

## 执行报告（老顽童，2026-09-10 续产收尾）

**交付物**：`30_wiki/cases/case-live258-huangqian-promo-film.md`（黄谦宣传片，素材 L2909-L3023）+ `30_wiki/cases/case-live258-simonpeng-medical-dataset.md`（Simon Peng 医疗数据集，素材 L355-L511）+ `30_wiki/dark-knowledges/dk-demand-feature-stacking.md` related 反向互链 2 条（huangqian/nongfu）。六案至此全产完毕。

**完成内容**：
1. 黄谦卡：起点→尝试（L1/L2 深度应用+L3 初步落地）→失败（上层 Feature 缺失三瓶颈）→转折（分层自评「底层扎实、上层待拓」）→结果（阶段性成果+30%/40% 两条未验证假设）；过程资产三个一工程/五行工具法/三段 SOP 全收录
2. Simon Peng 卡：按任务单定位作反例/边界教材——如实呈现「25 Feature 全启用=无取舍=事后贴标签」「改进方案完整但验证完全缺席」三大结构性缺陷；全案标注实证/推断/猜测三级
3. 前置缺陷项闭环对照：①dk-ai-does-not-question-your-mistake 互挂——已由农夫三拳卡（前次会话）闭环，本卡 related 互挂+不重复展开（见该卡 §与 dk 互链及 V0.9 缺口闭环说明）；②dk-demand-feature-stacking L165 黄谦边界例——新卡 related 正向互挂+dk 卡 related 反向补链 2 条（本卡与农夫三拳卡，git 确认 dk 卡无并发修改，最后改动 2026-08-24）；③V0.9 DataPack 缺口——农夫三拳卡内已注明（证据已闭环、卡片待补建属后续任务）
4. 自攻击四路（逻辑/证据/完整性/时效）：两卡 Critique 各含内部局限+2 外部攻击者；黄谦卡外部攻击=2025 宣传片同质化陷阱（WebSearch 对标：2025 企业宣传片行业趋势）+生产率 J 曲线；Simon 卡外部攻击=全国数标委《高质量数据集建设指南》2025-04 征求意见稿+信通院标注指标（WebSearch 对标）+Kahneman 流畅性幻觉。失败案例=Simon 卡本身即按反例教材定位

**验证**：
- `kdo pre-submit -f` 两卡均 ✅ PASS（黄谦卡：YAML/WIKILINK/DOMAIN/POSITION_DECLARATION/QUOTE_VERBATIM 等 16 项 0 issues，质量预评分 70/100；Simon 卡同 PASS 70/100）；各余 1 条 CONCEPT_CROSSCHECK 提示制 warning（#542 不拦截，涉及概念均为通用词复用非权威定义冲突）
- 伪逐字引文已修：黄谦卡 15 处→0（源文 `\+` 转义与弯引号导致未命中，改为逐字或去引号转述）；Simon 卡 5 处→0
- `kdo index --incremental` 已跑（+0 ~3，总计 4276），INDEX 门禁消除
- 素材消费：黄谦 L2909-L3023 全文消费（亮点/问题/坚持/放弃/假设/资产八节全覆盖）；Simon L355-L511 全文消费（背景/五阶段/25 Feature 清单/5 缺失/5 叠加/改进方案全覆盖）

**kdo query 检索记录**（宪法 #669）：2026-09-10，查询词「黄谦 达瑞电子 宣传片 Feature」（命中雍博卡等，无同主题卡）/「Simon Peng 医疗数据集 XZ 围手术期」（0 同主题命中）/「宣传片 AI创作 workflow 放大器 创意」（0 同主题命中）/「medical dataset quality 数据集质量 验证 反例」（0 同主题命中）——确认无重复卡后新建（L7）

**边界**：黄华春/jeffgirl/张丽娜/王鹏飞四张已产卡未动；雍博/农夫三拳/行知/田力四张前次已产卡未动（仅 dk 卡补反向链）；#683 P0 单与 #685 P2 补强未触碰。两新卡数字均为学员自述/假设，已逐条标注待核实。

**需要谁动作**：欧阳锋终审六案整单（重点：Simon 卡反例定位是否符合 #684「作边界教材」意图；dk 卡 related 反链是否合规）；黄药师无需动作（增量索引已跑）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
