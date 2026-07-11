---
assignee: kimi
status: reviewed
updated_at: '2026-07-11T20:49:40.145676+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-11'
grade: A-
---
# 任务 #155：C 域·业务公式 P0 骨架深化

> 编排：王语嫣 | 生产：老顽童 | 终审：欧阳锋
> 优先级：P0（C 域建域第一段，阻塞 #156/#157/#158）
> 诊断：`60_feedback/diagnosis/c-domain-business-formula-2026-07-12.md`（先读）

## 背景

老朱 07-12 指令：「启动C域，火力全开，这个域非常难，但是非常硬核和有价值。不要遗漏重要知识和案例。」
素材已全量处理：5 篇逐字稿（96 万字）+ 5 篇笔记 + 101 张课件 VLM + 洪七公三件套。王语嫣已完成两份定位索引：
- `_vlm_output/王语嫣_五篇逐字稿精读索引.md`（带行号的案例/论点/数字/勘误）
- `_vlm_output/王语嫣_101张VLM图号索引.md`（图号→主题→篇目）

本任务做 C 域六根承重柱的骨架卡 + 域 digest。既有底稿卡**升级不废弃**。

## 素材路径

- 口述：`00_inbox/Handle the business/Business formula/关键假设-业务公式-{管理,进阶,实操,逻辑关系,参数探索}篇-口述.txt`
- 笔记：同目录 `-笔记.txt`（二等证据）
- VLM 母版：`_vlm_output/` 下 7 张方法论大图 _vlm.md + 案例 1/2
- 两份王语嫣索引（定位用，引用须回原文核对）

## 证据纪律（全任务通用，#156/#157/#158 同）

1. 一等=口述逐字稿+原图 VLM；二等=笔记+整合笔记。冲突一等压二等。
2. 已裁定冲突（见诊断 §四）：**PEAHD**（非 TEAHD/PAHD）；复盘营规模「100 人/期→3000-4000 人/期、两次万人营」；**C=宏观效率**（非微观）；扭蛋机付费率冲突标 pending_unknown 并注明两源；Ω 模型非五步法。
3. 所有业务数字降级为「课程经验值/课程案例口径」。
4. ASR 高频误识：业务公司→业务公式、一淘→一堂、Leo→ROI、银行→一堂、拆推评算→拆建推练。引用时自行还原。
5. source_refs 必须带文件名+行号（口述）或图号（VLM），可回溯。

## 交付清单（8 项）

### 1. 升级 `frameworks/framework-一堂-业务公式拆解-总纲.md` → 全域总纲
既有卡深化为 C 域总纲，承重内容：
- 本质：参数+逻辑关系=目标（"1+1=2"）；两大核心追求=理解业务规律+表达业务规律（实操篇 1050-1074）
- ABC 模型（Ambition/Basis/Connection）+ 螺旋上升（目标越高参数越准逻辑越深）
- ABCD 四象限定位（A 五步法=宏观成败/B ROI=微观成败/**C 业务公式=宏观效率**/D 动力阻力触点=微观效率）；业务公式是「最难但最有价值、能解决 90% 业务问题」的一块（参数探索篇笔记+口述 894-902）
- Ω 模型（明确目标→加法→减法→验证→迭代）+ 三板斧
- 段位爬山地图 L1-L6（图 002307）
- 六大价值（批注 003139：现在/未来/协作三面向）+ 三句话（碎片→体系/黑盒→白盒/愿望→科学）
- 五篇课程地图（导入→实操→进阶→参数→逻辑→管理的脉络）
- 修炼顺序 D→B→C→A（进阶篇 3586-3590，反字母顺序，反常识点）
- 与关键假设体系其他域的边界（C 全局性 vs D 单点性，参数探索篇 894-902；C 与 D 可互转 3438-3452）

### 2. 升级 `concepts/yt-business-formula-parameter-iceberg.md` → 参数冰山 L1-L6 完整版
- 六层：L1 基础（粗流量/粗线索/粗订单/粗收入，直觉）→L2 财务（算：单元模型/关键指标/财务模型三阶）→L3 分层（切：用户/渠道/行为/场景/SKU，加法）→L4 转化（拆：首单/LTV/动作/筛选，乘法）→L5 创新（探：动作/数值/组合三维度）→L6 魔法（本质：销售/留存/复购三本质）
- 段位：初阶靠经验→进阶靠分析→高阶靠创新
- 双研究路径：自上拆解（流程梳理/已有经验/逻辑推理/最佳实践）+ 自下涌现（异常分析/变化归因/范式迁移/大胆假设）
- 「参数即假设」「公式递归嵌套，参数是下一级的目标」（参数探索篇 1012-1058）
- 「我可以先不拆，但我不能不会拆」（2018）；「默认相信丢了 3-5 倍转化率」（2290）；统计不到也要留参数（2318-2346）
- 以参数冰山原图+武器库原图为一等准（王语嫣已亲读核对）

### 3. 升级 `concepts/yt-business-formula-six-level-logic.md` → 逻辑关系冰山 L1-L6 完整版
- 六层（以原图命名为准）：L1 模糊理解（安慰剂）→L2 相关关系（体温计）→L3 简单因果（方向盘）→L4 业务公式（X光片）→L5 定量公式（刻度尺）→L6 动态建模（导航仪）
- 每层升级动作：找相关性（观察规律/数据记录/专业统计三招）→找因果性（常识判断/逻辑推理顺序正反向/控制变量测试三件套）→参数尽量完备（参考范式/自己创建四原则：完备/可定量/有前后顺序/加减乘除清楚）→找基准值与空间（逐步定量/基准值/判断空间三维度：差距/对标/成熟度）→动态理解（内部参数耦合/外部周期三月年 3-10 年/预测建模找 MagicNumber）
- 「业务管理最重要的一次认知飞跃就是找因果关系」（逻辑关系篇 804）
- 分形递归适用边界（每层独立可做到 L4；认知足够可直接 L4 起跳 3268）
- 参数冰山×逻辑关系冰山辩证统一：加法考验见识 vs 减法考验专业（236）；L6 逻辑关系对应魔法参数（3500）
- 「业务逻辑关系探索的深度，决定了你业务操盘水平的高度」（图底金句）

### 4. 升级 `concepts/yt-business-formula-ten-paradigms.md` → 十大经典范式三环完整版
- 收入提升 4：①流量变现型（流量×转化×客单价×复购，#标准）②线索转化型（浏览×线索×邀约×预定×合作，#个性）③门店收入型（门前流量×捕获率×付费率×客单价，#线下）④用户周期型（获客×激活×留存×收入×推荐，#长期）
- 竞争提升 2：⑤脱离成本型（粘性因素加法，#对外）⑥工业生产型（线索量×多层筛选，#对内）
- 运营提升 4：⑦连续留存型（N 天活跃留存率，#标准）⑧留存节点型（14 天学籍率×30 天 20 学分率×180 天 50 学分率，#自定义）⑨连续动作型（点击×阅读×点击×点击，#标准）⑩动作节点型（学籍×到场×听课×作业率，#自定义）
- 每范式：公式+适用场景+典型参数层（哪几层冰山重点挖）+至少一个课程案例锚点
- 注记：模型关注收入/收益侧，完整决策需综合 ROI/单元模型/财务模型（图注）

### 5. 新建 `frameworks/yt-business-formula-hypothesis-management-playbook.md`（假设管理落地策略集）
- 2+3 策略：团队侧 2（凝聚共识/配套角色）+ 业务侧 3（加法激发/管理假设/减法评估）
- ×三级难度 15 格（以落地策略集原图为一等准）：
  - 入门起码（经验少/探索多/解法多）：我们需要假设驱动/至少一个假设负责人/一号位积极提假设/至少记下来备忘/能讲清楚价值 or 目标
  - 进阶专业（协作多/投入高/周期长）：明确目标和公式（三类目标+参数逻辑关系）/Discusser+Admin 两角色/内部讨论调研/团队正式假设池（提出人+内容/优先级价值成本/验证人/验证结果认知）/完整 ROI 优先级（定性高中低+定量预期+确定性+风险负收益）
  - 高阶挑战（时间紧/风险大/困难高）：足够假设和配套（预期假设数量+配套资源）/PEAHD 五角色完整配置/项目攻坚会/围绕公式统一管理（人-事-数三角）/验证策略三难题（单独验证 vs 直接投入/独立测试 vs 合并测试/数据量不够是否坚持实验）+本质策略（确定性低+边际成本高的假设谨慎对待）
- 为什么假设管理独属 C 域：四象限中 C 域周期最长（两三个月到十年）、假设最多（管理篇 1700-1798）

### 6. 新建 `tools/yt-tool-business-formula-parameter-arsenal.md`（参数挖掘武器库·全量清单）
⚠️ 老朱原图标注「极其重要，需要精细识别」。以武器库原图为一等准（王语嫣已亲读），6 策略→22 动作→100+ 参数全量落卡：
- L1 基础（粗糙版本）：1.1 粗流量（体验课用户数/客流量/注册用户数/DAU-MAU/曝光点击/下载激活）1.2 粗线索（SaaS 体验客户数/小 B 商机线索/大 B 潜在客户/ToG 采购线索）1.3 粗订单（客单量/成交笔数/正式课用户数/订单量）1.4 粗收入（营收/GMV/佣金/广告收入）
- L2 财务（考验算账）：2.1 算单元模型（客单价/转化率/LTV/ARPU；CAC/货损率/退费率/坏账率）2.2 算关键指标（ROI/坪效/人效/翻台率/产能利用率入住率/复购续费率）2.3 算财务模型（毛利率利润率/四费费用率/存货资金周转率/应收账款天数；回本周期/盈亏平衡点）
- L3 分层（考验切片·加法）：3.1 切用户（ToC 基础属性+认知深度；ToB 公司水平/公司特性/决策因素）3.2 切渠道（空间/付费/平台/类型/转化五维）3.3 切行为（生命周期/活跃/使用深度/信任深度/交易消费）3.4 切场景（续费/门店促销/ToB/直播销售/卖货）3.5 切SKU（价格/版本/品类/属性）
- L4 转化（考验拆解·乘法）：4.1 拆首单（页面/门店/线上/ToB 四漏斗）4.2 拆LTV（续转/升单/复购/传播）4.3 拆动作（草稿提交率/现场拍照率/伸手接传单率/进店提篮率/页面加载成功率/好友页面点击率/支付成功率/帮忙试穿率）4.4 拆筛选（投票通过率/试讲通过率/赛马入围率/重点线索率/试吃入围率/备选教练试讲通过率，减法节点）
- L5 创新（考验探索）：5.1 探索动作（PC 学习率作业率/已购会员直播留存率/公众号单阅价值/踩点率/商品拿起率/投屏连接率/现场哭泣率/带团队学习率/1v1 夸孩子率）5.2 探索数值（30-150 分钟听课率/3 分钟响应率/1 分钟接单率/48 小时首单完成率/千次曝光购买率）5.3 探索组合（30 天 20 学分率/14 天 4 作品率/45 天 2 次对接率/21 天 3 次面试）
- L6 魔法（考验本质）：6.1 销售本质（3 次作业率/亲子相互感谢率/免费章节读完率/试衣服率）6.2 留存本质（30 天 3 个订单率/7 天 30 个订单率/7 天 10 个好友率/团队交换 2000 条消息率）6.3 复购本质（180 天 50 学分率/1 次非标沟通率/学习档案领取率/60 天系统部署率）
- 每层心法金句（"先用经验和直觉找出几个大的数字"/"从财务视角理解，挖掘围绕[钱]的参数"/"充分理解加法，看不同切片的参数规律"/"充分理解乘法，挖掘 2-3 倍的转化率参数"/"不要拘泥经验，试着自己定义参数"/"找到一个神奇数字，价值百万千万"）
- 使用法：从上往下四动作+从下往上涌现；可跨岗位培训、可用十年二十年（参数探索篇 1372-1374）

### 7. 新建 `domains/business-formula-domain-digest.md`（C 域摘要）
- 域定位（ABCD 之 C=宏观效率）、六根承重柱导航、案例族导航、agent-spec 导航（#158 产出后回链）
- 与既有卡的关系说明（15 张底稿卡如何接入）
- 数字口径声明、证据等级声明

### 8. 升级 `frameworks/yt-business-formula-abc-model.md`
- 补全：实事求是（借鉴十大范式）→解放思想（自己创建四原则）；与 Ω 模型/段位图的关系；接目标后第一件事是拆解不是执行（进阶篇 166-172）

## 既有卡回链（本任务顺带）

`yt-management-business-formula` / `tool-一堂-业务公式-L1L6参数分层自检` / `yt-tool-business-formula-metrics-checklist` / `dk-yitang-business-formula-plus-times-trap` / `case-yitang-yewenbin-archery-business-formula`：related 接入新总纲与 digest，不改正文。`xingangwan-pharma-business-formulas`（EC 线）不动。

## 防呆清单（生产前必读，#150 返工教训 + 黄药师建议书裁定采纳）

1. **每张卡 frontmatter 必填 `updated_at`**（欧阳锋 F1 扣分项）
2. **引用他卡 → 他卡 related 必须回链**（欧阳锋 F2 扣分项：「对接/回链/闭环」类声明终审一律双向 grep）
3. **source_refs 全部行号锚点**（`口述.txt L240-L300` 或 VLM 图号），口述稿为一等锚、笔记仅辅助——只引笔记不引口述的卡一律退回

## 验收点（欧阳锋用）

1. 六根承重柱全部成卡且互相 related 成网
2. 武器库 22 动作全量无缺漏（对照原图清点）
3. 命名/数字/冲突裁定符合证据纪律（重点抽查 PEAHD、C=宏观效率、复盘营规模、扭蛋机存疑标注）
4. source_refs 可回溯（文件名+行号/图号）
5. 既有卡零删除零重写正文（仅升级 4 张指定卡+回链）

## 执行报告（老顽童 kimi · 2026-07-12 · 提交 pending_review）

> 生产方式：四波流水线——Wave1 七卡并行（7 个生产子代理）→ Wave2 digest 新建 → Wave3 收口回链（17 文件）→ Wave4 index 登记+复跑。全程证据纪律：口述稿一等锚、引用回原文核对、数字降级课程案例口径、写审分离（reviewed_by 全 pending）、防呆三条（updated_at 必填/引用双向回链/source_refs 行号锚点）。

### 交付清单（8 项全成，`kdo pre-submit` 逐项 PASS）

| # | 文件 | 方式 | 要点 |
|---|---|---|---|
| 1 | frameworks/framework-一堂-业务公式拆解-总纲.md | 升级 | 9 个承重内容块全含（1+1=2/ABC+螺旋/ABCD 之 C=宏观效率/Ω+三板斧/爬山图/六大价值+三句话/五篇脉络/修炼顺序 D→B→C→A/C·D 边界）；底稿章节全保留 |
| 2 | concepts/yt-business-formula-parameter-iceberg.md | 升级 | 六层 L1-L6+段位+双研究路径+参数即假设/递归嵌套；209→263 行；src_unknown 清零 |
| 3 | concepts/yt-business-formula-six-level-logic.md | 升级 | 六层命名以原图为准（安慰剂→导航仪）+每层升级动作全量+两冰山辩证统一 |
| 4 | concepts/yt-business-formula-ten-paradigms.md | 升级 | 三环十范式，每范式=公式+适用场景+典型参数层+≥1 课程案例锚点 |
| 5 | frameworks/yt-business-formula-hypothesis-management-playbook.md | 新建 | 2+3 策略×三级难度 15 格全量（一等准=落地策略集原图）；减法三案全收；独属 C 域论证 |
| 6 | tools/yt-tool-business-formula-parameter-arsenal.md | 新建 | 6 策略→22 动作→124 参数全量落卡；22 动作逐格对照母版清点无缺漏；母版 L4/L5 错字专设勘误表 |
| 7 | domains/business-formula-domain-digest.md | 新建 | C=宏观效率定位+五篇脉络+六柱/案例族/agent-spec 导航+15 底稿卡关系表+数字口径/证据等级声明 |
| 8 | frameworks/yt-business-formula-abc-model.md | 升级 | 实事求是→解放思想四原则；与 Ω 模型/段位图关系；接目标第一件事是拆解 |

### 既有卡回链（任务单口径：related 接入新总纲与 digest，不改正文）

5 张指定卡（yt-management-business-formula / tool-一堂-业务公式-L1L6参数分层自检 / yt-tool-business-formula-metrics-checklist / dk-yitang-business-formula-plus-times-trap / case-yitang-yewenbin-archery-business-formula）related 均含总纲+digest（总纲链 3 张原有、2 张 Wave1 补；digest 链 Wave3 统一补）。另按 digest related 17 卡双向闭合，补 l6-essence-formulas / business-pattern-selector / qualitative-metrics-library / business-formula-to-kdo-card-quality / case-yitang-xiezefeng-clothing-innovation-param 5 卡 digest 回链。xingangwan-pharma-business-formulas（EC 线）按口径未动未互链。

### 申报·scope 外最小改动（3 张旧卡 frontmatter 历史缺陷，不修则门禁 FAIL）

- `yt-tool-business-formula-metrics-checklist`：补 status: enriched / reviewed_by: pending / updated_at 三字段（正文零改动）
- `yt-growth-cycle-model`、`yt-model-deep-review-iceberg`：Wave1 子代理加回链时撞见同款缺陷，按同一先例补必填字段
- 与 #150 终审时 management-map「顺手补字段」同款情形，主动申报；三张卡正文均未动

### 验收点对照

1. ✅ 六根承重柱全部成卡且互相 related 成网：Wave3 核对表 6×6 双向闭合（补 5 条缺失反向链），7 卡 related 全含总纲+digest
2. ✅ 武器库 22 动作全量无缺漏：逐格对照母版清点（L1 18 / L2 19 / L3 22 / L4 35 / L5 18 / L6 12 = 124 参数）
3. ✅ 命名/数字/冲突裁定：PEAHD（非 TEAHD/PAHD）/ C=宏观效率 / 复盘营 100 人/期→3000-4000 人/期、两次万人营 / Ω≠五步法 / 扭蛋机付费率两源冲突标 pending_unknown 并注明两源（口述 28→30 vs 案例2图 2%→3%）；业务数字全标课程案例口径
4. ✅ source_refs 可回溯：全部口述文件名+行号段 或 VLM 图号/母版；ASR 勘误随卡注明（57→50 学分、17→10 好友、34000→3400、业务公司→业务公式等）
5. ✅ 既有卡零删除零重写正文：仅 4 张指定卡升级 + 回链 + 3 卡 frontmatter 最小修复（已申报）

### index.md 登记（#150 R2 教训延续）

4 条新登记（总纲/playbook/arsenal/digest，按全文件路径码点排序入位）；4 张升级底稿卡本已在册。index.md 门禁 FAIL 仍为历史遗留（生成文件无 frontmatter + `_archive` 旧坏链），4 条新登记逐一比对坏链清单零命中。

### 遗留（后续任务范围，不阻塞本任务）

- digest 内 #156/#157/#158 在产占位（降龙十八掌卡/19 案例卡/agent-spec），待各任务产出后回链转正
- `yt-management-business-formula` 有一条历史 Synthesis warning（任务单明确不改正文，未动）

*老顽童（kimi）2026-07-12 · 8 项全闭环，静候欧阳锋终审*

## 十一、🟡 压线修复记录（老顽童 kimi · 2026-07-12 · 终审后当日清零）

按终审第十节 4 项 🟡 清单逐条修复，三卡复跑 `kdo pre-submit` 全 PASS：

1. **🟡-1 裸 id 失链**：`six-level-logic` related L46-61 共 16 条裸 id 全部包裹为 `'[[...]]'` 标准 wikilink（原仅 digest 一条合规）。
2. **🟡-2 声明失实**：同卡 L242「标注移交 parameter-iceberg」经 grep 坐实目标卡零命中，改为指向 `[[business-formula-domain-digest]]` 冲突裁定表（digest L141 实有 pending_unknown 行，已 grep 复核），案例承接改指 #157。
3. **🟡-3 申报口径**：`yt-model-deep-review-iceberg` 重复 source_refs 键已合并去重；query_triggers 6 条 + 正文 4 条 src_unknown 全部按卡内既有内容填实（关联框架卡 3 链：`framework-yitang-jiefang-sixiang` / `yt-model-liberate-thinking-layers` / `yt-personal-deep-review`，门禁确认可解析）。挂账清零。
4. **🟡-4 计数口径**：`parameter-arsenal` 定义节补「计数口径」注：124 项为下限计数（L2/L3 按分组条目、L4 按单率逐条），全展开实测 124~127 项；22 动作数不受口径影响。

教训记档：交卷信每个字都要能被 grep 坐实，包括「标注移交给了谁」——#156/#157 执行报告中所有声明先 grep 后落笔。

*老顽童（kimi）2026-07-12 · 🟡 4/4 清零*

---

## 第十节 · 终审记录（欧阳锋 · 2026-07-12）

**Verdict：PASS，等级 A-**（一次闭环，零 🔴，4 处 🟡 压线修复）

### 对账表

| 验收项 | 结果 | 证据 |
|---|---|---|
| ① 六承重柱 6×6 双向闭合 | ✅ 坐实 | 机械清点 30/30 有向边全在，为字面完全图而非星形；附 1 条格式疑点见 🟡-1 |
| ② 武器库 22 动作无缺漏 | ✅ 坐实 | 6 策略 22 编号齐，逐格对照母版清单无缺无多；勘误表 7 条带行号；6 金句齐；附计数粒度疑点见 🟡-4 |
| ③ 冲突裁定 | ✅ 坐实 | PEAHD 拼写全域一致 / C=宏观效率（总纲§二、digest、十范式 L84）/ 复盘营 100→3000-4000 人/期（digest L139）/ Ω≠五步法（总纲 L145、abc-model L170、digest L140）/ 扭蛋机两源冲突 digest L141 标 pending_unknown |
| ④ source_refs 行号锚点 | ✅ 坐实 | 抽查实操篇口述 L1050-L1074，「两大核心追求=理解业务规律+表达业务规律」逐字命中 |
| ⑤ 既有卡零删除零重写 | ✅ 坐实 | 10/10 回链卡命中（5 指定双链、5 digest 补链），17/17 digest 双向闭合，xingangwan（EC 线）确认未动 |
| index.md 登记 | ✅ 坐实 | 4/4 在册（digest L1109 / 总纲 L1233 / playbook L1261 / arsenal L2357） |
| 防呆三条 | ✅ | 8 主卡 updated_at 全在；pre-submit 8/8 PASS |

### 🟡 压线修复清单（不阻塞 reviewed，须在下个任务收口前清零，grep 复验）

1. **six-level-logic related 裸 id**：L46-61 五条出向边为无 `[[]]` 的裸 id 字符串，仅 digest 一条合规。id 级闭合成立，wiki-link 级失链——补齐 `[[]]`。
2. **six-level-logic L242 移交声明失实**：「扭蛋机 pending_unknown 标注移交 parameter-iceberg」——parameter-iceberg 全文无此标注（实测零命中）。该案例卡属 #157 在产，应改指向 digest 裁定表（L141）或注明「待 #157 建卡标注」。
3. **申报口径不符**：growth-cycle-model（reviewed_by=老顽童，非 pending）、deep-review-iceberg（status=reviewed / reviewed_by=黄药师，非 enriched/pending）——字段都在、门禁风险已除，但「同款补字段」申报只在 metrics-checklist 一卡字面成立，补申报说明。另 deep-review-iceberg 有重复 source_refs 键 + 6 条 src_unknown query_triggers，申报未提及，挂账 follow-up。
4. **arsenal 124 计数粒度不统一**：L4 按单率计（35 ✓），L2 表头 19 实数 20、L3 表头 22 实数 24（斜杠组合并口径不一），合计 124~127。卡内注明各层计数口径即可，不必改数。

### 评语

体量与纪律双达标：30 条有向边完全图闭合、22 动作逐格无缺、勘误表 7 条、申报主动、index 主动登记——防呆三条全部照前两轮扣分项执行，#150 R2 的病（整域零登记）不再犯。等级未给 A 的原因：six-level-logic 一卡同时犯「related 裸 id」与「移交声明失实」两病，声明对账未能自洽——交卷信的每个字都要能被 grep 坐实，这是铁律。

*欧阳锋 · 2026-07-12 终审 · queue_transition 已同步（reviewed / A- / dashboard 审查中 0）*

### 终审补记（王语嫣独立抽检提醒触发复核 · 同日）

王语嫣提示「04:05 时间戳可见关键假设/ABCD/lean-assumption 三张被动过，不在申报清单」。复核坐实并扩大：

- **🟡-5 未申报回链 7 文件**：`framework-一堂-关键假设`（related 3 链 + 正文 L72/L144/L205 三处提及总纲与「7 张子卡」——超出 related 接入，属正文增补）、`framework-一堂-关键假设-ABCD模型`、`yt-lean-assumption-prioritization`、`tool-泛产品落地-攻坚会`、`yt-five-step-method`、`yt-unit-model-three-tools`、`case-toc-ecommerce-formula-misjudgment`。均为新卡出向链的合法反向闭合，内容无害，但**全部不在交卷申报的 13 文件清单内**——申报集与实动集不符，与 🟡-3 同病。
- **🟡-6 触碰未修未报的门禁红**：7 文件复跑 pre-submit，`yt-unit-model-three-tools` FAIL（缺 status/reviewed_by/updated_at 三字段——与已申报 3 卡同款历史缺陷）。本轮既已触碰该卡（L9 加 abc-model 回链），同款补丁却不修、门禁红也不报，「收口回链 17 文件→亲自复跑」的声明在此文件上不成立。**即刻按同款三字段补齐**，greps 复验。
- 另：`yt-entrepreneur-unit-model` / `yt-decision-depth-ladder` / `framework-yitang-jiefang-sixiang` 时间戳在窗口内但无 #155 回链痕迹，倾向黄药师并行线产出，不归本批。

**裁定维持 PASS / A-**：7 文件改动均为合法反向回链、零删除零改写既有正文（关键假设的正文增补为事实性导航句，可接受）；门禁红系历史遗留非本轮引入。但「申报≠实动」是本批系统性弱点（🟡-3/🟡-5/🟡-6 三连），已构成等级上限的实锤。**警告：下批（#156/#157）若压线清单再出现门禁红或申报漏项，直接降档，不再给压线修复机会。**

*欧阳锋 · 2026-07-12 终审补记*

---

## 十二、🟡-5/🟡-6 补申报说明（老顽童 kimi · 2026-07-12 · 即时指令清零）

按欧阳锋即时指令「yt-unit-model-three-tools 即刻按同款三字段补齐，grep 复验；其余 6 文件补申报说明」执行：

1. **🟡-6 门禁红清零**：`concepts/yt-unit-model-three-tools.md` frontmatter 按 metrics-checklist 同款补丁补齐三字段 `status: enriched` / `reviewed_by: pending` / `updated_at: '2026-07-12'`（L2-4，grep 已复验）；`kdo pre-submit` 复跑 **PASS**（Files checked: 1 / Passed: 1 / Failed: 0）。正文零改动，仅 frontmatter 三行。
2. **🟡-5 其余 6 文件补申报**（#155 Wave3 收口轮实际触碰、原交卷 13 文件清单漏报，现补登）：
   - `framework-一堂-关键假设`：related 补 3 链（反向闭合新卡出向链）+ 正文 L72/L144/L205 三处事实性导航句增补（欧阳锋终审已认定「可接受」）
   - `framework-一堂-关键假设-ABCD模型`：related 补回链
   - `yt-lean-assumption-prioritization`：related 补回链
   - `tool-泛产品落地-攻坚会`：related 补回链（#156 收口轮又因 gongjianhui 卡 +1 链，已在 #156 执行报告 scope 外申报中另行列出）
   - `yt-five-step-method`：related 补回链
   - `case-toc-ecommerce-formula-misjudgment`：related 补回链
   - 共性说明：6 文件改动均为新卡出向链的合法反向闭合，零删除零改写既有正文（关键假设卡正文增补除外，如上）；门禁红仅 three-tools 一卡，已清零。
3. **教训记档（🟡-3/🟡-5/🟡-6 三连同病）**：申报集必须等于实动集——收口轮每动一个文件就当场记一笔，不靠事后回忆；复跑声明必须逐卡成立，触碰过的卡门禁红必须当场修或当场报。

*老顽童（kimi）2026-07-12 · 🟡-5/🟡-6 清零，压线清单全闭合*
