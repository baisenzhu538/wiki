---
id: task_20260809_laowantong-scientific-meeting-p0
assignee: kimi
status: reviewed
reviewed_by: 欧阳锋
review_date: '2026-08-09'
updated_at: '2026-08-09T09:33:25.144255+00:00'
priority: P0
wsjf: 3.0
grade: A
---

# 科学开会 P0 认知+武器库+案例（#285 · 9 项）

## 建模方案（出牌 · 老顽童 kimi 实例 2026-08-09）

按 `framework-kdo-modeling-methodology` + `concept-kdo-component-library` 出牌，依赖链：

`[素材牌 #3 先口述稿再笔记 + #4 先扫信号词] → [边界牌 #6 先查已有卡再新建] → [结构牌 #8 先定总纲再子卡 + #9 先 framework 再 concept + #10 先骨架再填肉] → [过程牌 #14 先跑脚本确认再下结论] → [质量牌 #15 先自攻击再提交 + #16 先 lint 再 pre-submit]`

| 牌 | 一句话理由 |
|:--|:--|
| #3 先口述稿再笔记 | 任务单硬约束：话术逐字引用口述稿（行号主锚），笔记只覆盖 ~40% |
| #4 先扫信号词 | "我给你演示一下/举个例子/这是我真实的"段落 = 案例卡证据源 |
| #6 先查已有卡再新建 | 诊断 §三：启动会/例会/复盘/会议设计均有已有卡——只补链不新建（已核实 8 张已有卡文件存在） |
| #8 先定总纲再子卡 | 卡 1 concept 升级 + 卡 2/3 framework 是认知地基，tool/case 是解压 |
| #9 先 framework 再 concept | 生产顺序：冰山画布/十大原则 → tool 武器库 → case/dk |
| #10 先骨架再填肉 | 每卡先搭 Claims/Evidence/Critique/Synthesis/Action Triggers/Failure Modes 骨架 |
| #14 先跑脚本确认 | pre-submit / lint 实测数字写入执行报告，不凭印象 |
| #15 先自攻击再提交 | 批次完成后四路自攻击，修 🔴🟡 再交 |
| #16 先 lint 再 pre-submit | 强制门禁：每卡 `kdo pre-submit -f` 输出贴入执行报告 |

**外部对标（诊断 Step 0 已完成 WebSearch 动态饱和）**：ROTI（Hinds 2026）/ 4D-CEO / Disagree and Commit（Intel）/ Atlassian page-led（85% vs 69%）/ 右规模 5-8 人——critique 引用，不重复搜索。

## 任务目标

科学开会卡片化 P0 批次——认知地基 + 十大原则武器库 + 核心案例包（用户强调：案例卡和暗知识非常重要）。诊断：`60_feedback/diagnosis/diag_20260809_scientific-meeting.md`。

## 卡片规格（9 项）

| # | 卡 id | type | 核心内容 | source_refs 主锚 |
|:--|:--|:--|:--|:--|
| 1 | yt-management-scientific-meetings **升级** | concept | 补 source_refs（3 口述稿）+ 冰山三层（目标/原则/流程）+ 会议三层价值（同步/推动/决策）+ 非必要不开会 + 深度讨论开会浅度讨论化简 | 认知篇 L736-1150/L900-1128 |
| 2 | framework-meeting-iceberg-canvas | framework | 会议冰山模型 + 思考画布（目标→原则→流程）+ "不开会有什么问题"反向推导 + 四类会议（例会/项目/团队建设/主题专项） | 认知篇 L672-900/L1142-1264 |
| 3 | framework-meeting-ten-principles | framework | 十大原则花瓣图：人（点燃/学习/民主/良性/激发）+ 事（投入/务实/高效/责任/落实）+ 对角线对立（高效×民主/务实×务虚）+ "方法丢一半效率掉一半" | 认知篇 L1378-1486 + 上篇 L1150-1164 |
| 4 | case-meeting-roi-awakening | case | A 同学启动会（流程→原则→ROI 三次觉醒，ROI 5-10 倍）+ B 同学复盘会（20 倍）+ Truman 砍周会（成本 10-20%，一年半无全员周会） | 认知篇 L194-660/L908-980 |
| 5 | tool-meeting-basic-principles | tool | 务实（准备数据/还原事实/追问定量/蓝军/借假修真发彪）+ 良性（提前铺垫/check-in/参与标准/对齐目标/降温/会后私聊）——话术级 | 下篇 L526-1408 |
| 6 | tool-meeting-execution-principles | tool | 高效（会议申请/边角料时间/参会知会名单/内容前置/开头一分钟/会议地图/停车场）+ 激发（提前准备/活跃分子/抛砖引玉/立 flag/可视化/想法归属 50-30-20）+ 点燃（点燃自己/起名/打仗氛围/上价值三维度）+ 投入（规则前置/订餐/预热思考三段论/可视化）+ 责任（角色赋予/规则郑重/友善提醒/红黄牌）+ 民主（老板克制/提前约定/发言顺序/民主集中/重新推导 80%） | 上篇 L18-1132 + 下篇 L1418-2550 |
| 7 | tool-meeting-result-principles | tool | 落实（二次确认/to do 反述/纪要三级/RS 计划/上周 to do 回顾/"如刚才沟通"）+ 学习（刻意练习埋周会/会议资产/经验萃取两只手/定期汇报/李蕊一句话） | 上篇 L1162-1740 |
| 8 | case-meeting-scene-mastery | case | 场景案例包：私董会收手机（规则前置）/ 张磊 KPI 原点（还原事实）/ 花匠降温（良性冲突）/ 高管口算数据（务实文化）/ 日本盖章传阅（内容前置）/ 创意公司脑暴前置（激发）/ 产品经理评审两版本（责任规则）——每个含完整过程+可迁移 | 下篇 L98-210/L792-820/L1338-1350/L602-646 + 上篇 L594-644/L1664-1680 |
| 9 | case-truman-meeting-leadership | case | Truman 会议领导力实践：重新推导 80%（民主集中进阶）/ 一堂选题会民主集中（报选题→投票→拍板）/ 马拉松筹备会（结束条件开场）/ 视频号大航海计划（点燃上价值）/ 美团 VP 发彪（借假修真）——一号位开会的完整姿态 | 上篇 L1056-1130/L992-1010 + 下篇 L744-750/L2412-2460/L924-968 |

## 生产纪律

- **话术级引用**：每个策略附口述稿逐字话术（行号主锚）——tool 卡可直接照抄使用
- **升级卡规则**：卡 1 是升级（保留原 reviewed 结构，补 source_refs + 新章节），不重写不降级
- **不新建重叠卡**：启动会/例会/复盘会/会议设计均有已有卡（tool-yitang-project-kickoff-meeting / tool-yitang-daily-weekly-meeting-hosting / yt-tool-meeting-designer / 复盘域 10+）——只 related 补链
- **定位声明必写**（#199）：每卡声明"属于管理域 L3 会开会子域 / 与 Y 的关系"
- **回链必做**：yt-management-scientific-meetings / yt-decision-consensus-iceberg / 复盘域（16 字诀/复盘引导）/ 刻意练习域 / kdo-self-attack（蓝军）/ 教练式领导力（同日编排）
- **外部对照**：ROTI（Hinds 2026）/ 4D-CEO / Disagree and Commit（Intel）/ page-led 数据（Atlassian）——critique 引用

## 验收标准

- 每卡 `kdo pre-submit` 通过 + lint 0 ERROR
- 定位声明 7/7；source_refs 行号可核实（抽查 3 卡回口述稿原文）
- 升级卡 source_refs 补齐（不再"无法追溯"）
- tool 卡话术逐字命中口述稿
- 无重复建卡（对照 §三 已有卡清单）

## 边界

- 不新建 MOC（管理域 digest 已含 L3 会开会，补链即可）
- 不生产七大会议模板电子版（P2 停车场）
- 案例卡不杜撰数字（ROI 倍数为口述原值）

## 参考素材

- 诊断：`60_feedback/diagnosis/diag_20260809_scientific-meeting.md`
- 口述稿：`00_inbox/科学开会/` 三篇（认知篇 2292 行 / 武器库上 2008 行 / 下 2690 行）
- 洪七公建议书（框架参考，深度以口述稿为准）

---

## 执行报告（老顽童 kimi 实例 · 2026-08-09）

### 交付物（9 项全齐）

| # | 卡 | 路径 | 正文行数 | pre-submit | quality |
|:--|:--|:--|:--:|:--|:--:|
| 1 | yt-management-scientific-meetings（升级） | 30_wiki/concepts/ | ~290 | ✅ PASS 0 err 0 warn | 90 |
| 2 | framework-meeting-iceberg-canvas | 30_wiki/frameworks/ | 151 | ✅ PASS | 80 |
| 3 | framework-meeting-ten-principles | 30_wiki/frameworks/ | 151+ | ✅ PASS | 80 |
| 4 | case-meeting-roi-awakening | 30_wiki/cases/ | 184 | ✅ PASS | 65 |
| 5 | tool-meeting-basic-principles | 30_wiki/tools/ | 166 | ✅ PASS | 65 |
| 6 | tool-meeting-execution-principles | 30_wiki/tools/ | 272 | ✅ PASS | 65 |
| 7 | tool-meeting-result-principles | 30_wiki/tools/ | 145+ | ✅ PASS | 80 |
| 8 | case-meeting-scene-mastery | 30_wiki/cases/ | 153 | ✅ PASS | 80 |
| 9 | case-truman-meeting-leadership | 30_wiki/cases/ | 199 | ✅ PASS | 65 |

### 生产纪律执行

- **口述稿逐字消费**：3 篇 6990 行由 3 个子代理逐字通读提取证据库（`_tmp/scientific-meeting-evidence/evidence-*.md`），主代理抽查 6 处话术 `sed` 对照原稿全部命中；锚点偏差已勘误（"新手高手"金句实出下篇 L426；私董会收手机实在上篇 L98-144；认知篇 L2148+ 重复段/下篇 L2602+ 重复段/燕窝广告段/红豆歌词段已标注跳过）
- **升级卡规则**：卡 1 保留原 reviewed 结构，source_refs 只追加不替换（旧 src 保留+新增 3 口述稿），新增核心框架四节（冰山三层/会议三层价值/非必要不开会/深度讨论化简）；旧版无源内容（承诺级 L1/L2/L3、30→8 人案例、Useem/Doyle 待补充引用位）已加"旧版遗留、不可追溯"批注而非删除
- **不新建重叠卡**：启动会/例会/复盘会/会议设计已有卡均未动正文，仅 #286 批补 related
- **定位声明**：9/9 卡含"管理域 L3 会开会子域"定位声明（pre-submit POSITION_DECLARATION 0 issues）
- **话术级引用**：全部「」+行号主锚；ASR 还原表执行（出门/楚门→Truman 等 15 组）
- **数字诚实**：案例数字全部标注"讲师/学员自述，数字待独立核实"

### 自攻击（四路，报告：`_tmp/scientific-meeting-evidence/self-attack-285.md`）

🔴×1（概念卡旧版无源数字→已批注隔离）+ 🟡×9（脑暴会降权三原则/二次承诺备忘邮件话术/花匠案例指针/30→85 分改造示范→已修复）——修复后 pre-submit 复跑全 PASS。数据攻击 45 处带行号引用逐一 sed 对照原稿全部命中。

### pre-submit 输出（终态摘要）

16 卡批量 sweep（含 #286）：全部 `Result: PASS — ready for human review`。本批 9 卡 quality pre-score 65-90/100。逐卡完整输出可随时复跑：`kdo pre-submit -f <卡路径>`。

### 已知残留（不阻断）

- kdo_lint.py 单文件模式 F2 断链误报（工具索引缺陷，范例卡同报）——以 pre-submit 为准；source_refs 指 00_inbox 的 WARN 为全库口径问题
- case 卡 quality 65 分（tacit/decomp 关键词计数偏低，内容实质达标）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O0 溯源验证：
1. 覆盖率 9/9 卡存在；口述稿 3 篇 6990 行确认（认知 2292/上 2008/下 2690）
2. 行号抽查 7 处原文逐条命中：认知 L900-905（要不要开会=ROI 先行）、L244-250（A 同学照最佳实践失败=原则>流程）、上篇 L1026-1032（有答案不拍板=重新推导）、下篇 L916-925（认真发一次彪=借假修真）、L2018-2024（设 flag 灵感压力下产生）、**勘误验证**：下篇 L426（"新手都在执行流程高手把控原则"——卡内按实际行号引用 ✅）、上篇 L98-104（私董会收手机 ✅）
3. 卡内行号引用精确（dk-meeting-roi-first: L984-986/L1018-1024/L1118-1126 等）
4. 自攻击 🔴 隔离批注真实：升级卡 L238"「承诺级 L1/L2/L3」无出处不可追溯——保留备参不作为已验证内容"+ L240"真实案例（旧版遗留，数字无源）"——无源数字隔离而非删除，诚实处理 ✅
5. 定位声明 9/9（pre-submit POSITION_DECLARATION 0 issues）；pre-submit 9 卡批量 PASS
6. 数字诚实：案例 ROI 倍数标注"讲师/学员自述，数字待独立核实"（边界条款"案例卡不杜撰数字"遵守）

五维：溯源 95/逻辑 90/暗知识 90/可操作 90/表达 90 → 总分 92（A）
