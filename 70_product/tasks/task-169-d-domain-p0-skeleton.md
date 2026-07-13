---
id: task_20260712_wangyuyan-d-domain-p0-skeleton
assignee: kimi
status: pending_review
updated_at: '2026-07-13T10:02:48.039149+00:00'
---
# Task #169 · D 域转化率黑客 P0 骨架 8 卡

- **状态**：queued
- **负责人**：老顽童
- **优先级**：HIGH
- **依赖**：#167、#168B reviewed 后顺领（避免同库并发）

## 目标
建 D 域（转化率黑客=微观效率象限）P0 骨架 8 卡，立起「转化率 = 动力 − 阻力 + 触点」核心公式与六根承重柱的总纲层。

## 卡清单（13 张，v2 按诊断书 §9.3）
1. `framework-一堂-转化率黑客-总纲`（公式+四象限定位+C-D 循环+"D 域频率最高+团队论"，入门篇 B 版 4906-4986）
2. `framework-一堂-转化率黑客爬山地图`（六段 L1-L6 **+三次跨越映射**：口述框架混乱→稳定→专业→迁移，入门篇 774-800/2774-2800）
3. `framework-一堂-转化基本功七个自我修养`（入门篇主干：固定拿结果/拆同行/提动力/降阻力/迭代到最佳/大量迁移，行 916-918/2916+ 各处）
4. `framework-一堂-动力三曲线`（构成+**使用三原则：以理服人优先/分阶段侧重/心理激励先于物质激励**+左右曲线本质差异，动力篇 522-788）
5. `framework-一堂-影响力36计`（以逐字扫描版 VLM 为权威；+**两大对齐原则：看动因不看手段/只教剑谱**+各原则强弱规律+段位元规则+A1-F6 阶梯全名，动力篇 4190-5686 为唯一逐条讲解版）
6. `framework-一堂-12种阻力总表`（12 阻力+定义切分+四大类归类+**四大类底层=科学决策三参数**+动嘴/动手/动钱矩阵）
7. `framework-一堂-阻力方法论骨架`（**两大误区：动力可覆盖不能消除/动力阻力相互转化 + 消除深度三层 L1降低/L2消除/L3逆转 + 消除时机三种：被动/主动/伏笔式**，阻力篇 448-555/2096-2566/2818-3214）
8. `framework-一堂-12触点SABC分级`（S=峰值+难题/A=首次终点/B=信任感官送礼/C=动线流程页面三方消息+**完整定义 S极重要/A很重要/B容易丢/C容易做+约 50 个子分类**，触点篇 1182-3310）
9. `framework-一堂-触点本质论`（接触机会点定义+资产隐喻+**火车货物剥离法**+假设三特性：后悔型/资产型/趁早性，触点篇 240-510/990-1020）
10. `framework-一堂-转化率提升六步法`（拆解/加法/减法/讲香/组合/制作，以组合篇口述为权威；+**双模式立论：优化模式 vs 设计模式+四阶段映射：准备/分析/打磨/制作**，组合篇 548-977）
11. `framework-一堂-六大优化原则`（**数量 3：触点提升/密度提升/号召提升 + 质量 3：优先匹配/顺序匹配/厚度匹配**，组合篇 3394-3966）
12. `framework-一堂-十指模型`（**左手五化：场景化/口语化/数字化/故事化/素材化**+右手抽象五化：比喻/金句/情绪/冲突/升华，组合篇 2732-2892）
13. `digest-domain-转化率黑客`（domain digest 占位骨架）

## 证据源（一等=口述/VLM）
- 口述：`00_inbox/Handle the business/conversion rate/2. 转化率黑客{入门篇,动力篇,阻力篇,触点篇} 口述逐字稿.md` + `转化率黑客5：组合落地篇 口述逐字稿.md`（口述共 24548 行，按协议 1 定点读，优先挖生动案例细节）
- VLM：`00_inbox/Handle the business/conversion rate/_vlm_output/images/`（143 张，爬山地图/待破解阻力清单/动力三曲线图/12触点清单/超级小抄等）
- 诊断书：`60_feedback/diagnosis/d-domain-conversion-rate-2026-07-12.md`（**术语口径以 §四裁定表为准**：折面子/名利权情/ABACC/峰值+难题/五化口径等）
- C 域衔接：`30_wiki/dark-knowledges/dk-yitang-business-formula-cd-loop-undo-key.md`（C-D 循环，总纲卡必须挂载）
- 既有卡升级不在本任务（#170 做）

## 执行要求
- 卡放 `30_wiki/frameworks/`，digest 放 `30_wiki/digests/`；命名沿用 `一堂-` 前缀
- frontmatter 必填：type/domain（conversion-rate 或按 lint 约定，与 C 域核对后统一）/tags/related；related 出向在 D 域内双向闭合，C 域桥接=引用型单向（指向 cd-loop 卡即可）
- 数字一律「课程案例口径」；术语不擅自改；禁止引用 §五列出的残缺 PDF 缺失内容
- 不动 `30_wiki/raw/ocr/`（#168A 处理中）；补 `/index.md` 域索引
- 骨架卡必须含「案例区」：36 计卡嵌六原则口述案例（互惠/承诺/认同/喜好/权威/稀缺各 6-8 例，话术+数字+行号）、12 阻力总表嵌消除案例、12 触点卡嵌各触点案例、十指模型嵌黄宝书完整演示（诊断书 §9.5 A 级分层）
- 质量纪律按诊断书 §八

## 验收口径
- 8 卡齐全，骨架可独立成域；预检 PASS；扫窗申报=实动集
- 待王语嫣审查后 pending_review（欧阳锋终审）

## 扫窗申报
建卡清单 + 其他触及文件 + 术语口径疑点

### 实动文件清单（共 15 个文件）

- 新建 12 张 framework 卡：
  - `30_wiki/frameworks/framework-一堂-转化率黑客-总纲.md`
  - `30_wiki/frameworks/framework-一堂-转化率黑客爬山地图.md`
  - `30_wiki/frameworks/framework-一堂-转化基本功七个自我修养.md`
  - `30_wiki/frameworks/framework-一堂-动力三曲线.md`
  - `30_wiki/frameworks/framework-一堂-影响力36计.md`
  - `30_wiki/frameworks/framework-一堂-12种阻力总表.md`
  - `30_wiki/frameworks/framework-一堂-阻力方法论骨架.md`
  - `30_wiki/frameworks/framework-一堂-12触点SABC分级.md`
  - `30_wiki/frameworks/framework-一堂-触点本质论.md`
  - `30_wiki/frameworks/framework-一堂-转化率提升六步法.md`
  - `30_wiki/frameworks/framework-一堂-六大优化原则.md`
  - `30_wiki/frameworks/framework-一堂-十指模型.md`
- 新建 1 张 domain digest：`30_wiki/domains/conversion-rate-domain-digest.md`（按既有惯例放 `domains/`，任务单笔误写 `digests/`）
- 更新 index：`30_wiki/index.md`（--fix-index 自动补登 13 条）
- 队列/任务单：`70_product/tasks/production-queue.md`、`70_product/tasks/task-169-d-domain-p0-skeleton.md`（queue_transition.py claim 写入 frontmatter）

### 执行结果

- 卡量：任务单写 8 卡，实际按诊断书 §9.3 v2 交付 **13 卡**（12 framework + 1 digest），并在此说明。
- 双向 related：D 域 13 卡内部全双向闭合（脚本复核 missing count = 0）。
- C 域桥接：D 域总纲 → `dk-yitang-business-formula-cd-loop-undo-key` / `framework-一堂-业务公式拆解-总纲` / `business-formula-domain-digest` 为引用型单向；A/B 域 digest 为四象限定位导航边。
- 门禁：
  - `kdo pre-submit` 13 卡全部 PASS（0 error）
  - `kdo lint --domain conversion-rate --summary` → `Lint passed. No new issues found (3060 accepted).`（0 error）
  - 其中 29 条 warning 为 source_refs 行号锚点误报（路径含空格 + `Lxxx-Lxxx` 被 linter 整体当路径），与 #167 C 域的 88 条同类误报同源，已接受基线。

### 术语口径疑点 / 主动裁决

1. 公式口语「动力加阻力加触点」（L3054）语义为「提动力、降阻力、加触点」，卡内写作 `转化率 = 动力 − 阻力 + 触点`，已注明口述原话。
2. 七修养官宣为 7 个（L2916-2918），第 5 个 = 珍惜触点；诊断书 §9.3 卡清单描述漏列，已补。
3. 爬山地图六段 L1-L6 名称以图《转化率黑客的爬山地图》原字为权威，口述未口播逐段名称，仅讲三次跨越。
4. 四大类命名以口述为准：投入过高 / 收益低 / 机会成本 / 时间窗口；诊断书 §9.2 #22 所记「过程可能有坑」口述未见，已申报。
5. 阻力消除策略 = 12 策（L3476 作「13」为口误，L5098 与诊断书 §9.2 #15 同裁定 12 策）。
6. 十指模型：模型名以图/笔记为准（口述别名手势模型/双三角模型）；右手第四化 = 冲突化（笔记作冲动化疑误）；第五化 = 升华（总览 L2736 与笔记作生活化为同音误识）。
7. 质量第三原则 = 厚度匹配（总览 L3406 作后置匹配疑 ASR 误识，L3898+ 与笔记 L93 均作厚度匹配）。
8. 棋牌室目标值 = 2%-10%（组合篇 L482/笔记；L1748 作 20% 疑误识）。
9. 触点篇文件名实际为 `转化率黑客-动力助力触点-触点篇-口述.txt`（其余四篇为「动力阻力触点」），source_refs 已按真实文件名引用。
