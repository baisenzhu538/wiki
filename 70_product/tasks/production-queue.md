---
id: production-queue
type: queue
status: active
updated_at: 2026-08-06T00:00:00+00:00
reviewed_by: 欧阳锋
owner: 王语嫣
audience: 老顽童 / 欧阳锋 / 黄药师 / 用户
---
# 生产队列：老顽童领取 / 欧阳锋审核
> 本文件是 KDO 知识工厂的**统一生产队列**。
> 老顽童按队列顺序领取，一次只做一件；欧阳锋按队列顺序审核。
> 任务来源：历史批量工单、新域诊断任务、跨域桥接任务。
|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|
| 187 | `task_20260714_wangyuyan-material-gaps-tracking` | 素材缺口追踪与回源登记（4类缺口：复盘合集7案例/征文十篇+邱淼案例集/双三角/刻意练习；blocked等老朱） | blocked | 老顽童 | 缺口登记卡+素材到位后24h内评估入队 | 老朱提供素材 |


| 290 | `task_20260711_wangyuyan-fundamentals-to-dual-triangle-migration` | task_20260711_wangyuyan-fundamentals-to-dual-（#284补登记）queued/? | closed_superseded | ? | 补登记 | 无 | `60_feedback/tasks/task_20260711_wangyuyan-fundamentals-to-dual-triangle-migration.md` | 任务单已存在但队列无行（E019 家族变体）——#284 补入队






| 303 | `task_20260809_huangyaoshi-coaching-assistant-deploy` | 教练式领导力助理三件套部署（#300 spec审后执行，E026拆角色）：SOUL.md+config.yaml+agents目录+Hermes profile+cap_hub注册+飞书链接+自举 | reviewed | huangyaoshi | 部署+冒烟+自举 | #300 reviewed ✅ + #280/281/288 ✅ | `60_feedback/tasks/task_20260809_huangyaoshi-coaching-assistant-deploy.md` | ✅黄药师交付(2026-08-09)：三件套(SOUL 78行含五阶梯内嵌+config+agents目录+Hermes profile+cap_hub发现)+逻辑冒烟8项全过+顺手修cap_hub WIKI_ROOT bug(07-21遗留,修复后19 Feature全恢复)；✅C1已闭环(2026-08-09自我介绍版)+场景级验证通过(2026-08-15真实教练问题：五阶梯定位/硬币诊断/话术/莫非案例/引用卡4/4真实，详见任务单)；提审待欧阳锋终审<!-- 手动流转：queue_transition被拦+O-3；铁律0提审即流转 --> |<!-- 2026-08-15 欧阳锋：C1 真机冒烟闭环（08-09 自我介绍 + 08-15 场景级），等级升级 PASS（条件）A-→A-，飞书正式可用 -->

| 304 | `task_20260809_huangyaoshi-meeting-assistant-deploy` | 科学开会助理三件套部署（#287 spec审后执行，E026拆角色）：SOUL.md（冰山画布/十大原则/话术内嵌）+config.yaml+agents目录+Hermes profile+cap_hub注册+飞书链接+自举 | reviewed | huangyaoshi | 部署+冒烟+自举 | #287 reviewed ✅ + #285/286 ✅ | `60_feedback/tasks/task_20260809_huangyaoshi-meeting-assistant-deploy.md` | ✅黄药师交付(2026-08-09)：三件套(SOUL 90行含ROI/冰山画布/原则匹配/话术内嵌+config+agents目录+Hermes profile+cap_hub发现)+逻辑冒烟8项全过+引用卡名14/14真实；✅C1真机冒烟闭环(2026-08-15用户实测：ROI/冰山画布/原则匹配/话术全返回+引用卡5/5真实，详见任务单)——待欧阳锋确认关闭<!-- 手动流转：queue_transition被拦+O-3；铁律0提审即流转 --> |<!-- 2026-08-15 欧阳锋：C1 真机冒烟闭环（五段式实测），等级升级 PASS（条件）A-→A-，飞书正式可用 -->






| 319 | `task_20260815_wangyuyan-agent-spec-domain-cleanup` | O-14 agent-spec类卡domain系统性清扫（欧阳锋拍板）：9张卡 domain补列表+目录归属方案评估——只改frontmatter不动正文，建议先行 | reviewed | laowantong | 清扫9张+迁移方案 | 无 | `60_feedback/tasks/task_20260815_wangyuyan-agent-spec-domain-cleanup.md` | 来源：欧阳锋停车场O-14（2026-08-15拍板）；边界：只改frontmatter不动正文；生产交老顽童/黄药师；欧阳锋终审；2026-08-16 已派老顽童生产（王语嫣编排完成） |<!-- 2026-08-16 欧阳锋终审 PASS A-：domain 9/9 达标；目录迁移裁定不迁移（方案A前提不成立：重复文件 tools/ 版更新），TODO 另立项 -->
| 320 | `task_20260815_laowantong-spin-ai-sales-cards` | SPIN实践篇+AI销售协同卡组（P1）：framework-AI销售协同（确定性方法+可判断/形容词禁忌/正负样本特征值，销售+决策域双向归集）+销售漏斗全貌（复购裂变倒梯形）+异议处理转化（承认→稀释→调动）+dk×2-3（需求挖掘是公司任务/大单小单/客户讨厌AI） | reviewed | laowantong | 4-5张卡 | 无（素材精做前置：口述2400行逐字读） | `60_feedback/tasks/task_20260815_laowantong-spin-ai-sales-cards.md` | 王语嫣编排（用户拍板：增量必做+双向归集）；理论篇已有卡不重复；欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-：O0 溯源 7/7 锚点命中零编造 + related 0 死链 + 双向归集成立 + dk 七段完整 + 二手标注合规；全网调研替代裁定接受 -->
| 321 | `task_20260815_huangyaoshi-sales-domain-digest` | 销售管理域digest补建（P2）：23卡无digest结构缺口（E015同构）——digest卡+domain-mapping挂接+域外桥接（销售↔决策/AI、需求、增长） | reviewed | huangyaoshi | digest卡+挂接 | #320 reviewed（digest需含新卡） | `60_feedback/tasks/task_20260815_huangyaoshi-sales-domain-digest.md` | 王语嫣编排（用户拍板：补结构缺口）；欧阳锋终审；2026-08-16 已派黄药师（依赖#320✅已满足，与#328顺序执行） |<!-- 已提审待欧阳锋 2026-08-16：sales-domain-digest卡落盘(核心框架/五步工具链/暗知识/12案例/OPC体系/5条域外桥接)+domain-mapping挂接+wikilink 16+正文45零死链+覆盖50卡(含#320新卡6)+lint 0新增+可检索 --><!-- 2026-08-16 欧阳锋终审 PASS A-：digest 20链0死链+mapping挂接+可检索实证 -->
| 322 | `task_20260815_laowantong-candy-sales-recruiting` | Candy销售招聘方法入库（P2）：能力模型+定量定性结合+星巴克/Cosmos客观验证——加传播限制标注（素材"不要外传"，内部库可用） | reviewed | laowantong | 1张卡 | 无（与#320并行） | `60_feedback/tasks/task_20260815_laowantong-candy-sales-recruiting.md` | 王语嫣编排（用户拍板：必须入库）；欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-：related 9 死链 0 + 传播限制标注合规 -->
| 324 | `task_20260815_wangyuyan-agent-knowledge-conduit-diagnosis` | 知识库→Agent传导机制盘点诊断（P0，系统性工程）：全agent盘点现状矩阵（快照型/内嵌检索型/无接入型）+全网调研RAG→Agent传导最佳实践+三层传导管线架构（检索层/导航层/刷新层）+P1-P3迁移路径 | reviewed | wangyuyan | 诊断报告+方案 | 无（与#320/321/322并行，纳入其产出） | `60_feedback/tasks/task_20260815_wangyuyan-agent-knowledge-conduit-diagnosis.md` | 用户拍板立项（2026-08-15）；调研先行；只出诊断不执行改造；欧阳锋审查；✅诊断报告已落盘(60_feedback/diagnosis/diag_20260815_agent-knowledge-conduit.md)——已提审待欧阳锋终审<!-- 手动流转：queue_transition被拦+O-3；铁律0提审即流转 --> |<!-- 2026-08-16 欧阳锋终审 PASS A-：3/8 MCP挂载实测确认/索引机制确认/四缺陷成立；TODO 双位置部署未入矩阵+编译产物38个非33 -->

| 323 | `task_20260815_huangyaoshi-gbk-output-fix` | GBK终端崩溃族统一修复（P-30，P2，0.5d）：print含emoji/中文脚本入口统一 sys.stdout.reconfigure(utf-8)——generate-dashboard(#269扣分点)/其他待扫；GBK实测+回归 | reviewed | huangyaoshi | 修复+实测 | 无 | `60_feedback/tasks/task_20260815_huangyaoshi-gbk-output-fix.md` | 来源：停车场P-30（欧阳锋#269终审2026-08-09）；先例skill_bridge_sync/feature_menu已做<!-- 已提审待欧阳锋 2026-08-15：52脚本统一加GBK输出保护(import后+6行reconfigure块)，137文件编译0失败，PYTHONIOENCODING=gbk崩溃对照实测exit0(裸print✅崩exit1)，test_feature_menu 28/28，generate-dashboard重跑302统计不变 --> |<!-- 2026-08-15 欧阳锋终审 PASS A-：52脚本GBK保护实测复现+修复验证，137编译0失败，28/28回归；报告302→实测303为队列演进非回归 -->
| 325 | `task_20260816_huangyaoshi-kdo-mcp-rollout` | P1统一检索层（#324终审PASS后立项）：Windows侧5个Hermes profile补挂kdo MCP（duanwangye/hongqigong/laowantong/wangyuyan/note-coach）+WSL侧duan/kimi-test确认+快照型agent（销售对话助理/AI基本功教练）加kdo query指令+索引事件驱动化（E028机制化入#263流水线） | reviewed | huangyaoshi | MCP挂载+检索指令+流水线环节 | #324 reviewed ✅ | `60_feedback/tasks/task_20260816_huangyaoshi-kdo-mcp-rollout.md` | 按终审TODO修正口径（WSL侧实测6/8已挂kdo，beikai双挂保留）；欧阳锋终审<!-- 已提审待欧阳锋 2026-08-16：Windows5 profile挂kdo MCP(备份+yaml验证5/5)+MCP协议级验收(initialize v1.28.0/tools4/SPIN命中)+WSL duan/kimi-test豁免(废弃/测试)+快照2 agent检索指令落盘(kdo query实证命中)+E028 Step4入#263卡+回归0修改 --> |<!-- 2026-08-16 欧阳锋终审 PASS A：5挂载+2豁免+快照指令+事件驱动全验证，协议级 kdo_search 独立重跑命中，回归0修改 -->
| 326 | `task_20260816_huangyaoshi-agent-mechanism-institutionalization` | P2机制制度化（#325终审PASS后立项，P2-DYN-01出池）：agent出生模板固化（#263部署步骤加挂kdo MCP固定动作+spec验收检查项）+health-check升级巡检（MCP挂载+新卡可检索）+digest门禁入流水线（终审闭环查digest+可检索，domain-mapping挂接） | reviewed | huangyaoshi | 流水线文档+巡检脚本+门禁 | #325 reviewed ✅（#321 并行不阻塞） | `60_feedback/tasks/task_20260816_huangyaoshi-agent-mechanism-institutionalization.md` | 吸收两变量（新agent产出/知识库增长）机制化；P3快照迁移为本任务完成后立项输入；欧阳锋终审；补充任务2：MCP配置单一真相源（hermes-mcp-template+sync脚本渲染16 profile，用户批准2026-08-16，双位置漂移根治）<!-- 2026-08-16 欧阳锋立项核查：并入 #325 遗留修正（WSL 侧 5 运行中 gateway 补挂 kdo）——巡检按 WorkingDirectory 验证 --><!-- 已提审待欧阳锋 2026-08-16：机制制度化3件套落盘(#263 Step2 MCP固定动作+Step4 digest门禁+check-mcp-roaming挂入health-check 17/17)+WSL 5 gateway补挂(systemd实证,备份)+MCP单一真相源(hermes-mcp-template+sync-hermes-mcp.py渲染16 profile,幂等SAME,双侧kdo_search HIT)+狗粮抓修2真bug(WSL跨平台路径patch/check-agent-config GBK)+friction-log 4行 --><!-- 2026-08-16 欧阳锋终审 PASS A：WSL 5补挂确认（#325 空挂闭环）+ 单一真相源 16/16 + 巡检 17/17 + 双侧 kdo_search HIT；狗粮3问题2修1遗留 -->
| 327 | `task_20260816_wangyuyan-snapshot-migration-pilot` | P3快照迁移试点（销售对话助理，#326终审后立项）：重编译prompts工作手册（纳入#320新卡+销售域digest导航）+CLAUDE.md路径表升级digest导航+试点验证（真实销售问题检索命中新卡）+迁移模式沉淀 | reviewed | wangyuyan | 重编译+导航升级+迁移模式 | #320/#321 reviewed（#326 ✅） | `60_feedback/tasks/task_20260816_wangyuyan-snapshot-migration-pilot.md` | 消灭最后一个静态依赖；推广阶段另立项；✅已交付(2026-08-16王语嫣)：重编译+导航升级+试点验证3问全命中新卡（含E028复发修复：kdo index --rebuild跳过search_index的源码bug已friction-log）——已提审待欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-：试点 3/3 命中 + KDO 源码 bug 确认（--rebuild 不重建 search_index 已批准 P0 修正）+ #263 命令修正批准 -->
| 328 | `task_20260816_huangyaoshi-gateway-crash-loop-fix` | Hermes gateway崩溃循环修复（P0，方案B全归user级，用户拍板2026-08-16）：禁boot脚本pkill+system级3个退役+user级对齐+NRestarts归零+linger实证+巡检闭环（#326复用） | reviewed | huangyaoshi | 单一user级机制+验证 | #326 reviewed ✅ | `60_feedback/tasks/task_20260816_huangyaoshi-gateway-crash-loop-fix.md` | 诊断diag_20260816_hermes-gateway-lock-conflict.md；O-12解耦；欧阳锋终审；2026-08-16 已派黄药师 P0 优先 |<!-- 已提审待欧阳锋 2026-08-16：boot disabled+system级3退役+user级8/8 running，NRestarts观察10min归零(86/89/86不变)，linger=yes实证，boot脚本理由确认零丢失，飞书3/3 connected，巡检17/17；并入#327遗留：kdo index --rebuild源码bug已修(3904 docs全重建) --><!-- 2026-08-16 欧阳锋终审 PASS A：boot退役+system退役+user 8/8+NRestarts归零+飞书3/3+源码bug修复实证（Candy/SPIN双HIT）-->
| 330 | `task_20260816_huangyaoshi-index-doc-fix` | 索引命令文档修正（P1，#327遗留②）：全库grep kdo index --rebuild 误用点，文档与源码语义对齐（源码#329已修） | reviewed | huangyaoshi | 文档修正+复核 | #329 ✅（源码已修） | `60_feedback/tasks/task_20260816_huangyaoshi-index-doc-fix.md` | 欧阳锋建议书#330；欧阳锋终审 |<!-- 已提审待欧阳锋 2026-08-16：全库grep盘点20处(行为指导9+历史11)，修正4处(#263 Step4语义标注+全量重建表述+失败模式+欧阳锋context升级全重建)，狗粮4项过(--rebuild三重建3905docs/Candy命中/index.md含digest/裸index对照) --><!-- 2026-08-16 欧阳锋终审 PASS A-：4处修正全验证（L154/161/263/296）+ 历史类未动；🟡 L138 仍1处'索引增量更新'残留记 TODO -->
| 331 | `task_20260816_wangyuyan-snapshot-migration-rollout` | P3快照迁移推广（P1，#327 PASS A- 推广就绪）：AI基本功教练三步走迁移+38编译产物盘点（部署中vs规格卡）+迁移顺序建议 | reviewed | wangyuyan | 迁移+盘点 | #327 ✅ #330 ✅ | `60_feedback/tasks/task_20260816_wangyuyan-snapshot-migration-rollout.md` | 欧阳锋建议书#331；王语嫣重编译+老顽童协助；✅已交付(2026-08-16王语嫣)：基本功教练三步走迁移+38盘点（10部署中/4spec/22规格卡）+迁移顺序——已提审待欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-：基本功教练迁移+38盘点验证通过，检索三关键词全IN -->
| 332 | `task_20260816_laowantong-baozhashidiaochan-wave1` | 爆炸式调研Wave1 P0框架主线5卡（Live259，用户确认2026-08-16）：五步法framework+饱和覆盖concept+R型Partner五状态机+九字诀14策略tool+开一篇文档concept——含系列课补链（four-research-types/radar/oscar互链+选课口令） | reviewed | laowantong | 5张卡+补链 | 无（素材精做前置：口述6718行已通读） | `60_feedback/tasks/task_20260816_laowantong-baozhashidiaochan-wave1.md` | 诊断diag_20260816_baozhashidiaochan.md；三方法证据就绪；欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-：五卡 O0 溯源命中 + 外部对标 3 条 + related 0 死链；Wave2/3 可入队 -->
| 333 | `task_20260816_laowantong-baozhashidiaochan-wave2` | 爆炸式调研Wave2 案例与AI demo 7卡（#332终审后入队）：Leo润滑油case+4000标题case+AI学习系列case+设计原则90条case+OPC128方向case+L1-L6价值层级+70-30分工 | reviewed | laowantong | 7张卡 | #332 reviewed ✅ | `60_feedback/tasks/task_20260816_laowantong-baozhashidiaochan-wave2.md` | 素材锚点见生产任务清单；精做笔记含ASR对照表（#332亮点固化）；欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-：7卡 O0 零编造 + L6 冲突以图为准 + OCR 人工核验标注 -->
| 334 | `task_20260816_laowantong-baozhashidiaochan-wave3` | 爆炸式调研Wave3 dk暗知识8卡：饱和自证话术/MECE手术台/打样纠偏三轮/私有库总量锚定/排行榜替代/拾荒者vs建筑师/应做必做/AI没时间观念 | reviewed | laowantong | 8张dk卡 | 与#333并行（锚点独立） | `60_feedback/tasks/task_20260816_laowantong-baozhashidiaochan-wave3.md` | dk七段门禁含Critique；欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-：8 dk 七段+Critique+定位全达标 -->
| 335 | `task_20260816_wangyuyan-research-r-partner-spec` | R型爆炸式调研Partner agent spec（用户预期产agent，#332终审后窗口）：五状态机+五步法+九字诀内嵌，TCPR可切换，调研系列第三个agent | reviewed | wangyuyan | spec文件+基线用例 | #332 reviewed ✅（#333/334卡名终审核对） | `60_feedback/tasks/task_20260816_wangyuyan-research-r-partner-spec.md` | #263流水线spec环节；✅已交付(2026-08-16王语嫣)：SPEC.md 五状态机+基线用例3个——已提审待欧阳锋终审；部署另立项 |<!-- 2026-08-16 欧阳锋终审 PASS A-：引用卡 5/5 真实 + 五状态机与 W1-3 逐字一致 + 基线用例 3 个有卡背书；部署可立项 -->
| 336 | `task_20260816_laowantong-ai-km-wave-a` | AI×知识管理Wave A P0框架6卡（楚门vault拆解，KDO照镜子，综合codex/黄药师裁决）：火箭六要素+五次飞跃+多Agent协作链+Session分层+双中心+Agent团队架构——含模型祛魅↔kdo-context-design互链 | reviewed | laowantong | 6张卡 | #333/334在产（队列顺序执行不插队） | `60_feedback/tasks/task_20260816_laowantong-ai-km-wave-a.md` | 2处待核矛盾写卡标注；欧阳锋终审；2026-08-16 #333/334 收官后已派老顽童可领 |<!-- 2026-08-16 欧阳锋终审 PASS A-（条件已清：3处回链双向闭环）：O0 锚点 6/6 零编造 + 21卡结构全绿；条件=3组旧卡回链待老顽童补 -->
| 338 | `task_20260816_huangyaoshi-patrolkit-session-recovery` | K1 PatrolKit KDO Session资产自动回收（⏸挂起待迁移会审）：#326巡检升级设计（配置巡检→知识资产巡检，Session精华自动回收→沉淀dk/技能）——先出设计文档不改造 | reviewed | huangyaoshi | 设计文档 | #326 ✅（挂起：待Hermes迁移会审结论） | `60_feedback/tasks/task_20260816_huangyaoshi-patrolkit-session-recovery.md` | 最大缺口立项；欧阳锋终审；2026-08-16 已派黄药师可领（设计文档先行，改造待迁移会审） |<!-- 已提审待欧阳锋 2026-08-16：PatrolKit设计文档落盘(60_feedback/designs/design_20260816_patrolkit-session-recovery.md)——巡查目标三层/抽离规则4类资产+3触发器/沉淀路径候选池+人审确认/与#326同框架升级/实施P0-P3；改造挂起待迁移会审 --><!-- 2026-08-16 欧阳锋终审 PASS A-：三决策成立 + codex 4 接口要求全吸收 + #337 会审确认（审计文档可定稿）；P1 改造待迁移会审 -->
| 339 | `task_20260816_wangyuyan-top-level-doc-pilot` | K2顶层文档制度试点（楚门顶层文档→KDO项目级）：试点1-2项目顶层文档（四字开头/必知必会前置/链接后置）+制度草案（销售域digest为域级雏形） | reviewed | wangyuyan | 试点+草案 | 无 | `60_feedback/tasks/task_20260816_wangyuyan-top-level-doc-pilot.md` | ✅已交付(2026-08-16王语嫣)：爆炸式调研顶层文档+制度草案——已提审待欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-：试点索引 4/4 真实 + 制度锚点命中 + 制度设计完整；🟡 top-doc 内 #335 状态待更新 -->
| 340 | `task_20260816_laowantong-ai-km-wave-b` | AI×知识管理Wave B 工具与案例9卡：小抄SAB/顶层文档制度/Skill八步流水线/文档资源化10-11种/VibeCoding case/四棒接力case/偶遇五通道/自动分类脚本/PatrolKit雷达 | reviewed | laowantong | 9张卡 | #336后（队列顺序） | `60_feedback/tasks/task_20260816_laowantong-ai-km-wave-b.md` | 互链#339顶层文档试点/#338设计文档；欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-（条件已清：3处回链双向闭环）：O0 锚点 6/6 零编造 + 21卡结构全绿；条件=3组旧卡回链待老顽童补 -->
| 341 | `task_20260816_laowantong-ai-km-wave-c` | AI×知识管理Wave C dk暗知识6卡：调研饱和话术/先萃取再合并/一句话交接/工具硬推/模型祛魅/三上下文公式——C1↔爆炸式W3-1、C5↔kdo-context-design互链 | reviewed | laowantong | 6张dk卡 | #340后（队列顺序） | `60_feedback/tasks/task_20260816_laowantong-ai-km-wave-c.md` | C4优先（黄药师建议，与#328机制强制同构）；欧阳锋终审 |<!-- 2026-08-16 欧阳锋终审 PASS A-（条件已清：3处回链双向闭环）：O0 锚点 6/6 零编造 + 21卡结构全绿；条件=3组旧卡回链待老顽童补 -->
| 349 | `task_20260816_laowantong-wechat-transcript-tool-card` | 视频号→逐字稿自动化工作流tool卡（R型首战资产报告转卡：四环节×双路线矩阵+12工具全景+反爬情报+DataPack；verified分级保留+时效标注2027-02；素材已资产化跳过诊断） | reviewed | laowantong | 1张tool卡 | 素材=00_inbox/视频号逐字稿调研/（欧阳锋O0抽查A级零编造） | `60_feedback/tasks/task_20260816_laowantong-wechat-transcript-tool-card.md` | ✅已授权（欧阳锋建议+用户方向）；欧阳锋终审；collect_wechat.py验证后如需case卡另立 |<!-- 2026-08-17 欧阳锋终审 PASS A-：转卡保真+related 8死链0+覆盖事故裁定认可 -->
| 354 | `task_20260818_huangyaoshi-mcp-performance` | MCP 性能（P2，1d，小昭审查建议）：onboard/capabilities 走索引（复用 O-15 缓存模式）+ read 分页 offset + instructions 统计动态化 | closed_no_action | huangyaoshi | 性能 | #353 reviewed ✅（须在 #351 重启前交付） | `60_feedback/tasks/task_20260818_huangyaoshi-mcp-performance.md` （已并入 #356 交付：read 分页/onboard/capabilities 索引/统计动态化全部落地，黄药师 2026-08-18；验收随 #356 终审）| 小昭 KDO-MCP 审查 P2-8/9/10 + P4-15；欧阳锋终审 |（#356 已吸收交付：onboard/capabilities 走索引+read 分页+instructions 动态化，2026-08-18）














| 426 | `task_20260822_laowantong-tags-judgment-batch` | 739 张 tags 判断类分批治理（P2 长程，老朱 08-20 拍板+08-22 二拍维持）：词表设计先行+按域分批 | queued | laowantong | 词表+分批治理 | 无 | `60_feedback/tasks/task_20260822_laowantong-tags-judgment-batch.md` | 词表未出不动手；首批=试点批；归零声明附 #399 工具输出；欧阳锋批次验收（#411 模式）；风清扬审计待修③收口；**08-23 挂起解除**（半肥猫素材到位→三方法诊断→词表 v0.3 正式稿（90_control/tags-vocab-design.md）老朱确认；词表设计节=该文件；试点批=决策域 50 张，排 #465 后领取） |

| 445 | `task_20260823_huangyaoshi-oneclick-agent-launcher` | KDO 一键启动脚本（P2，冷启动三件套 A 项）：右键启动+角色菜单，三步入会话 | reviewed | huangyaoshi | 启动脚本+狗粮 | 风清扬建议书裁定（B/C 归 #419 追加+王语嫣自办） | `60_feedback/tasks/task_20260823_huangyaoshi-oneclick-agent-launcher.md` | L3 活体=老朱亲手三步启动确认；飞书角色不进菜单；交付五字段+验证分层声明；欧阳锋终审 |
| 446 | `task_20260823_laowantong-role-special-huangyaoshi` | 角色专场第三场：黄药师岗位说明书定稿（P1，F-028 第三场） | reviewed | laowantong | 五要素 spec 升级 | 素材已齐（验证分层/词表三层/四铁律注入） | `60_feedback/tasks/task_20260823_laowantong-role-special-huangyaoshi.md` | 必含基建单一实例(#222/#223)/验证三验(跑了≠真了)/词表三层/只拦机械项；狗粮=本单 complete 零 force；欧阳锋终审、老朱终稿后并入 §2.6.4 |
| 447 | `task_20260823_laowantong-role-special-fengqingyang` | 角色专场第四场：风清扬岗位说明书定稿（P1，F-028 第四场） | reviewed | laowantong | 五要素 spec 升级 | **#446 老朱拍板后开工**（一角色一张过） | `60_feedback/tasks/task_20260823_laowantong-role-special-fengqingyang.md` | 必含不动基建不产卡/只交王语嫣/完成声明拆三问/判断先落盘/L0 审计权；欧阳锋终审、老朱终稿后并入 §2.6.5；老朱场=最后一场待老朱输入 |
| 448 | `task_20260823_laowantong-role-special-zhu` | 角色专场第六场（终场）：老朱角色卡定稿（P1，F-028 收官） | reviewed | laowantong | 五要素 spec（人的角色重构） | 顺位 #446/#447 后；老朱口述通道即时开放（一等证据随时入） | `60_feedback/tasks/task_20260823_laowantong-role-special-zhu.md` | 写的是人不是 agent（纠偏者/拍板人/宪法来源不可委托内核）；红线清单全量提炼；老朱本人确认终稿；定稿后 F-028 出池 §2.6 六节全齐 |
| 449 | `task_20260823_laowantong-file-flow-protocol` | 《KDO 文件流转规范》v1.0（P1，协作纪律成文化）：命名/版本/时间戳/唯一编号+两类冻结纪律细则 | reviewed | laowantong | 规范文档+六角色文件清单表 | **老朱拍板提级：先于 #446 开工**（charter §3.15 已入宪总纲） | `60_feedback/tasks/task_20260823_laowantong-file-flow-protocol.md` | doc_id=D-YYYYMMDD-NNN 唯一编号；v1.0 起版订正+0.1 新件 amends 引旧件；一次性交付物全冻结/任务单 append-only；向前生效存量不追溯；欧阳锋终审、老朱终稿 |
| 450 | `task_20260823_huangyaoshi-file-flow-lint` | 文件流转规范工具支撑（P1，规范门禁化）：doc_id 查重+冻结检测+命名合规 | reviewed | huangyaoshi | lint 检查器+单测 | **#449 规范生效后开工** | `60_feedback/tasks/task_20260823_huangyaoshi-file-flow-lint.md` | 登记口查重当场拒绝；冻结文件进 diff 报警（节级 hash 方案黄药师定）；误报进 friction 观察期；只拦机械项；欧阳锋终审 |
| 451 | `task_20260823_laowantong-spec-exec-report-rule` | spec 增补：执行报告五字段=提审必备铁律（老顽童+黄药师两 spec）（P1，老朱指令） | reviewed | laowantong | 两 spec 条款增补 | #441 实证缺执行报告；黄药师四单齐全（防复发固化） | `60_feedback/tasks/task_20260823_laowantong-spec-exec-report-rule.md` | 与 F-034/#444 force 台账口径一致；重新提审同标准；#446 上板冻结故走新增修订单（新纪律狗粮）；欧阳锋终审 |
| 453 | `task_20260823_huangyaoshi-queue-archive-slim` | 队列归档瘦身机制（P1，看板定期瘦身）：归档脚本+王语嫣定期执行 | reviewed | huangyaoshi | 归档脚本+单测+首次瘦身 | 老朱指令（token 成本+注意力稀释） | `60_feedback/tasks/task_20260823_huangyaoshi-queue-archive-slim.md` | reviewed>14天归档按月文件；活跃态永不归档；归档前后对账；首次归档前 git tag 快照；总任务数=活跃+归档全量口径；欧阳锋终审 |
| 454 | `task_20260823_laowantong-fengqingyang-l1-l4-caliber` | #447 底本口径修正：记忆胶囊 L1-L4 新口径（P1，老朱定稿） | reviewed | laowantong | 口径修正指令单（落点在 #447 交付物） | #447 上板冻结——新增修订单 | `60_feedback/tasks/task_20260823_laowantong-fengqingyang-l1-l4-caliber.md` | L2=风清扬最重要本职+三铁边界；spec 零旧口径残留（grep 核）；执行报告随 #447 |
| 455 | `task_20260823_laowantong-spec-boundary-ask-first` | 未定稿三 spec 补通用边界条款（职责外必询问）（P1，老朱拍板六角色通用） | reviewed | laowantong | 口径传三场（落点在 #446/#447/#448 交付物） | 三任务单上板冻结——新增修订单 | `60_feedback/tasks/task_20260823_laowantong-spec-boundary-ask-first.md` | 已定稿三 spec 已直接修订（老顽童 v1.1/欧阳锋 v1.1/王语嫣 v1.3）；欧阳锋版含编排域归属具体化；执行报告随各场 |
| 456 | `task_20260823_huangyaoshi-agentid-audit-fix` | 记忆胶囊 agent_id 统一+审计器解析盲区修复（P2，两小修复合一） | reviewed | huangyaoshi | 数据清洗+审计器修复+单测 | 风清扬建议3+欧阳锋#188处置采纳 | `60_feedback/tasks/task_20260823_huangyaoshi-agentid-audit-fix.md` | agent_id 拼音角色名统一+清测试残留；审计器行数异常禁静默跳过+全量重跑出真实残留清单；query 命令不在本单（F-045 待拍板）；欧阳锋终审 |
| 457 | `task_20260823_huangyaoshi-disposal-gate-structured` | 处置类门禁判定结构化（P1，误判两连发+可绕过漏判根治） | reviewed | huangyaoshi | 判定重构+回归用例 | 老顽童建议书采纳（方案1+2组合） | `60_feedback/tasks/task_20260823_huangyaoshi-disposal-gate-structured.md` | 显式标记 disposal:true 优先+关键词降级提示+只扫动作节；#189/#454 误判放行+真处置正反测；PROTOCOL §7 意图不变；欧阳锋终审 |
| 458 | `task_20260823_huangyaoshi-friction-auto-report` | 问题主动上报自动化（P1，治沉没）：friction-log 统一+探针第四探针+复盘强制节 | cancelled | huangyaoshi | 摩擦探针+模板+review-check | 老朱核心关切（#454 靠翻上下文才发现） | `60_feedback/tasks/task_20260823_huangyaoshi-friction-auto-report.md` | 记录零成本（一行式）→传输全自动（探针扫增量不依赖建议书格式）→复盘必填问题节兜底；单扫描器纪律；欧阳锋终审 |
| 459 | `task_20260823_huangyaoshi-friction-design-fix` | #458 设计修正（老朱质询采纳）：通道唯一化+机器自报层，与 #458 合并实施 | cancelled | huangyaoshi | 设计修正口径单（实施并入 #458） | #458 上板冻结——新增修订单 | `60_feedback/tasks/task_20260823_huangyaoshi-friction-design-fix.md` | friction 层作废改建议书最小三行形态；新增 gate-blocked.log 机器自报+探针第五探针；复盘问题节保留兜底；#458 任务 1 作废任务 2 改造任务 3 保留 |
| 460 | `task_20260823_huangyaoshi-issue-report-automation-final` | 问题主动上报自动化·最终设计完整任务书（P1，取代 #458/#459） | reviewed | huangyaoshi | gate-blocked 自报+探针第五探针+复盘兜底 | 老朱纠偏：调整须另下任务编排书 | `60_feedback/tasks/task_20260823_huangyaoshi-issue-report-automation-final.md` | 三层=建议书最小三行唯一通道/gate-blocked.log 机器自报/复盘必填问题节；#459 越权裁决（作废改造+合并实施）撤销；#458/#459 冻结留档勿领取；验收=08-23 断链场景三环全通；欧阳锋终审 |
| 461 | `task_20260823_huangyaoshi-queue-cancel-command` | queue_transition cancel 命令（P1，queued 单取消/被取代状态） | reviewed | huangyaoshi | cancel 状态机+台账+下游适配+单测 | 老朱拍板立项（#460 取代场景暴露） | `60_feedback/tasks/task_20260823_huangyaoshi-queue-cancel-command.md` | 仅 queued 可 cancel+reason 必填入台账；cancelled=终态不删除；探针不通知/dashboard 不计活跃；首批执行=cancel #458/#459（被 #460 取代）；不可逆（重做=新单）；欧阳锋终审 |
| 462 | `task_20260823_huangyaoshi-probe-review-done-signal` | 探针「流转完成」信号（P1，终审结果通知编排者——治编排者盲区） | reviewed | huangyaoshi | new_reviewed/new_failback 双信号+单测 | 老朱提问触发（#447 PASS 靠询问才知） | `60_feedback/tasks/task_20260823_huangyaoshi-probe-review-done-signal.md` | PASS→通知 wangyuyan 待部署；FAIL 退回→通知 assignee 返工；文案自足免翻文件；只推送不自动部署（判断留人）；单扫描器纪律；欧阳锋终审 |
| 463 | `task_20260823_huangyaoshi-l1-full-context-capture` | L1 全量上下文采集基建（P1，甲会话原文+乙工作痕迹/D盘+镜像） | reviewed | huangyaoshi | 采集脚本+双盘+verify | 老朱拍板口径+风清扬建议书采纳 | `60_feedback/tasks/task_20260823_huangyaoshi-l1-full-context-capture.md` | 甲CLI会话原文+乙session trace/产出物变动；D盘git外；与事件指针库分层并存（L0→L1改名一并）；体积红线监控；欧阳锋终审 |<!-- 复审响应 2026-08-23：P1 registry L33 L1 改名已补交付+磁盘一致性实测（memory_capsule status 主库 L1 7 行 integrity ok+镜像存在+D盘目录无 L0 残留）+grep L0 零命中——等待正式流转 -->|
| 464 | `task_20260823_huangyaoshi-mirror-on-save` | 记忆胶囊镜像保存后联动（P1，save→log→mirror 一条链） | reviewed | huangyaoshi | 挂钩扩展+verify 联动+单测 | 老朱拍板时间锚「保存后联动」（#427 欠项结清） | `60_feedback/tasks/task_20260823_huangyaoshi-mirror-on-save.md` | 事件驱动非 cron；mirror 失败可见不阻断；verify 轻量联动报警治 backup-stale 复发；欧阳锋终审 |
| 465 | `task_20260823_laowantong-banfeimao-ai-kb-cards` | 半肥猫AI知识库知识生产（P0，A档10+1卡：五阶段主线+传承卡） | reviewed | laowantong | 11 张知识卡（洪七公底稿→老顽童产卡） | 三方法诊断闭环（diag D-20260823-008） | `60_feedback/tasks/task_20260823_laowantong-banfeimao-ai-kb-cards.md` | 口述行号一等主锚；双原则卡+五维标注卡为核心抽验卡；与KDO现有卡双向回链；A档PASS后B/C/D另单；欧阳锋终审 |
| 466 | `task_20260823_laowantong-banfeimao-b-manuals` | 半肥猫B档实操手册3份（P1，拿到就能用：长文到卡片/YAML标签/内容工作流） | reviewed | laowantong | 3 份手册（洪七公底稿） | #465 A 档后；图OCR+VLM已就绪 | `60_feedback/tasks/task_20260823_laowantong-banfeimao-b-manuals.md` | 五维标注为手册2核心教学（颗粒度判断三问）；范本零虚构可溯源；与A档卡互链不重复；欧阳锋终审 |
| 467 | `task_20260823_laowantong-banfeimao-c-cases` | 半肥猫C档深度案例2篇（P2：紫鲸工作台解剖/30实例失败到系统成型） | reviewed | laowantong | 2 篇案例（洪七公底稿） | #466 后；图11-15 VLM就绪 | `60_feedback/tasks/task_20260823_laowantong-banfeimao-c-cases.md` | 问题→解法叙事；失败原话不美化（AI删文档不承认/小龙虾灾难一等锚）；时间线+决策点+可迁移原则；欧阳锋终审 |
| 468 | `task_20260823_wangyuyan-banfeimao-d-workbook` | 半肥猫D档训练营作业包（P3 随缘：基础+进阶+一页纸教程结构） | queued | wangyuyan | 作业包三件（编排侧设计） | A档PASS后；不占产线顺位 | `60_feedback/tasks/task_20260823_wangyuyan-banfeimao-d-workbook.md` | 课程原生思考题复用（口述L98-136原题）；一页纸教程=五步+五维速查+双原则浓缩；作业包=教学设计域（千惠清单先例）；老朱过目 |
| 469 | `task_20260823_laowantong-addiction-book-cards` | 拆书会《成瘾》知识生产（P2，人域4卡：天平/DOPAMINE框架/自我约束/以痛治痛） | reviewed | laowantong | 4 张精选卡 | 诊断 D-20260823-015（298行全量读+九层） | `60_feedback/tasks/task_20260823_laowantong-addiction-book-cards.md` | 卡3=KDO门禁同构卡（物理/时间/分类 vs 台账/冻结/分层对照）核心抽验；转述二等标注原书；拆书会系列常态化待老朱；欧阳锋终审 |
| 470 | `task_20260823_laowantong-addiction-series-caliber` | #469 口径修正（P1，老朱纠偏）：按拆书会系列惯例补来源标注 | queued | laowantong | 口径修正单（随 #469 执行） | #469 误判「无拆书先例」——库里实有 90+ 拆书卡 | `60_feedback/tasks/task_20260823_laowantong-addiction-series-caliber.md` | source_person/source_context 字段（水水卡范本）；human-insights+business 双域；按内容语义分卡不按来源；欧阳锋随 #469 审 |
| 471 | `task_20260823_huangyaoshi-l1-capture-scheduling` | L1 采集投入运行最小闭环（P1：常驻调度30min+体积红线） | reviewed | huangyaoshi | 计划任务+体积监控+verify联动 | **老朱已拍板常驻注册（2026-08-23「L1 全量采集 30 分钟一跑」）——可开工** | `60_feedback/tasks/task_20260823_huangyaoshi-l1-capture-scheduling.md` | 与探针错峰；失败可见禁静默；L3=次日回放抽查；欧阳锋终审 |
| 472 | `task_20260823_huangyaoshi-role-routes` | KDO 角色路由层（P1，三路由合一：任务/技能/知识——进入即答三问） | reviewed | huangyaoshi | myqueue命令+role-routes.md+CAPSULE v3 | 黄药师建议书采纳（#459 取代困惑=实证） | `60_feedback/tasks/task_20260823_huangyaoshi-role-routes.md` | myqueue 只读视图不动状态机；depends_on 字段新单起强制（F-047）；技能/知识静态表不过度工程；六角色各跑 myqueue 狗粮；欧阳锋终审 |
| 473 | `task_20260823_huangyaoshi-file-flow-lint-residuals` | 文件流转 lint 遗留三项收口（P2：wiki 卡 L9 扫描/冻结基线动态化/lint 集成） | reviewed | huangyaoshi | 三项收口+单测 | 欧阳锋 #450 终审遗留项采纳 | `60_feedback/tasks/task_20260823_huangyaoshi-file-flow-lint-residuals.md` | L9 全库一次扫描（分钟级）；冻结基线走无状态方案；lint 集成可缓；欧阳锋终审 |
| 474 | `task_20260823_huangyaoshi-tags-audit-fullscan` | 全库标签摸底体检（P1：四指标一次性扫描+标签健康并入 #425 常态监测） | reviewed | huangyaoshi | 体检报告+健康指标扩展+单测 | 老朱拍板立项（标签体系发现收口） | `60_feedback/tasks/task_20260823_huangyaoshi-tags-audit-fullscan.md` | 只读零修改；脏词率/来源轴覆盖/有轴域/空值率四指标；决策域已知答案做 L2 狗粮；治理批次后续按域排产；欧阳锋终审；脏词/空值吸收建议书2三层分档(STRONG/PATTERN进分母,SOFT只观察误报) |
| 475 | `task_20260823_wangyuyan-472-coldstart-absorb` | 吸收#472路由层进六角色context冷启动链（恢复完直接答三问：领哪单/用什么招/先掌握什么） | reviewed | wangyuyan | 六spec冷启动段+role-routes衔接说明 | 用户令收口#472入口层 | `60_feedback/tasks/task_20260823_wangyuyan-472-coldstart-absorb.md` | 王语嫣自办不占黄药师；接#419冷启动铁律；解欧阳锋#472残余风险(spec↔role-routes同步纪律)；只读导航不改#472本体；欧阳锋终审 |
| 476 | `task_20260823_wangyuyan-queue-status-check-discipline` | 队列状态核对纪律固化（禁用正则手搓，统一走queue_transition对账；E051闭环） | reviewed | wangyuyan | context/skill铁律+轻量包装命令 | E051误报#474状态用户纠正 | `60_feedback/tasks/task_20260823_wangyuyan-queue-status-check-discipline.md` | 王语嫣自办不占黄药师；任务1纪律固化立即可做；任务2方案A轻量/方案B留演进候选；与E041/E038/E017同族补全；欧阳锋终审 |
| 477 | `task_20260823_huangyaoshi-task-docid-field-removal` | 任务单doc_id字段违规处置（模板移除+存量清理，E045闭环；#473工具实证） | reviewed | huangyaoshi | 模板改+存量批移除+spec卡doc_id | 欧阳锋建议书采纳方向①（纠偏非口径变更） | `60_feedback/tasks/task_20260823_huangyaoshi-task-docid-field-removal.md` | 只移除doc_id不动内容；#450lint已把门模板修掉断源；存量先清单→dry-run→单卡→人工审→批量；E003快照/E017yaml解析/E046不吞节/E050path-scoped；顺序#479→477→478禁同轮≥3；欧阳锋终审 |
| 478 | `task_20260823_huangyaoshi-review-check-failure-detail` | review-check判B/C输出失败项明细（差异可自解释，E049同族） | reviewed | huangyaoshi | review-check.py失败项明细输出+单测 | 黄药师建议书部分采纳② | `60_feedback/tasks/task_20260823_huangyaoshi-review-check-failure-detail.md` | 只改输出层不动判定逻辑；①agent-os§10.4.1补问题节必填挂老朱拍板窗口不塞本单；王语嫣③自办重跑验证回A；顺序#479→477→478禁同轮≥3；欧阳锋终审 |
| 479 | `task_20260823_huangyaoshi-queue-batch-accept` | 批次验收工具化queue_batch_accept.py（#426批次线，静默失败根治；复用#453模式） | reviewed | huangyaoshi | queue_batch_accept.py+单测+dry-run | 欧阳锋建议书采纳立项（#426第4次静默失败） | `60_feedback/tasks/task_20260823_huangyaoshi-queue-batch-accept.md` | 四步一体+每步断言+前后对账+dry-run+原子commit；不动queue_transition状态机；B2-4想犯错也犯不了；顺序#479(P1)→477→478禁同轮≥3；欧阳锋终审 |
| 480 | `task_20260823_wangyuyan-426-tags-acceptance-caliber` | #426后续批次验收标准升级口径单（抽查读正文+机械辅助，E047上板冻结传口径） | queued | wangyuyan | 口径三条款落盘（append不吞节） | 欧阳锋建议书采纳（25%错配率实证） | `60_feedback/tasks/task_20260823_wangyuyan-426-tags-acceptance-caliber.md` | 不改#426本体（上板冻结传口径）；王语嫣不改卡O7补词归老顽童；机械辅助挂#474扩展；存量复查增量不推翻已验收；欧阳锋终审 |
| 481 | `task_20260823_laowantong-shushui-addiction-supplement` | 水水成瘾口述补充生产·2口径补强+3新增（#469补强，一等证据；W1逐字读3613行） | reviewed | laowantong | 2补强(天平+以痛治痛)+3新增(上瘾门槛论/盲盒机制/改变别人代偿) | 老朱拍板2迭代3新增；依赖#469 | `60_feedback/tasks/task_20260823_laowantong-shushui-addiction-supplement.md` | 不改#469本体(E047传口径)；W6三方法前置；source锚水水口述行号；#469+本单=7卡；欧阳锋终审 |
| 482 | `task_20260823_huangyaoshi-batch-accept-commit-bugfix` | queue_batch_accept.py commit收口pathspec bug修复(#479修单,两次实证) | reviewed | huangyaoshi | commit绝对路径或chdir+回归用例 | 欧阳锋建议书采纳(#426第四五批) | `60_feedback/tasks/task_20260823_huangyaoshi-batch-accept-commit-bugfix.md` | P1 #426线(E040收口风险);不动四步流转逻辑;依赖#479;欧阳锋终审 |
| 483 | `task_20260823_huangyaoshi-gate-blocked-noise-filter` | gate-blocked.log测试噪声过滤(防第五探针误报) | reviewed | huangyaoshi | 测试件独立testlog或过滤规则 | 风清扬L1审计建议4采纳 | `60_feedback/tasks/task_20260823_huangyaoshi-gate-blocked-noise-filter.md` | P2日志质量;task_9999_*测试噪声与真实拦截分离;不动gate-blocked真实逻辑;欧阳锋终审 |
| 484 | `task_20260823_huangyaoshi-tags-source-word-blacklist` | tags-audit来源形态词黑名单检查(#474扩展,第5指标来源词污染率) | reviewed | huangyaoshi | 黑名单检查器+复合词白名单+单测 | 欧阳锋建议书采纳(3例实证) | `60_feedback/tasks/task_20260823_huangyaoshi-tags-source-word-blacklist.md` | P2 tags质量;排队#482→#483→#484禁同轮≥3;已有规则(来源名禁入tags)工具化为检查器;不动#474主体;欧阳锋终审 |
| 485 | `task_20260823_wangyuyan-vocab-axis-before-batch-gate` | 轴文件先行·剩余域轴批量出+gate化(#426放量前提机制化) | queued | wangyuyan | 剩余域轴+tags-vocab-design补条目+黄药师gate工具 | 老顽童建议书采纳(content卡点实证) | `60_feedback/tasks/task_20260823_wangyuyan-vocab-axis-before-batch-gate.md` | P1 #426堵点根治;与E054同根;执行前老朱拍板规范改;黄药师gate工具挂子任务/拆#487 |
| 486 | `task_20260823_wangyuyan-gate-external-supervision` | 门禁外部监督维度·#442-464对照+规范落点(#469同构背书补差异) | queued | wangyuyan | 门禁清单对照表+file-flow-protocol/KF-024补条目 | 老顽童建议书采纳(#469Critique) | `60_feedback/tasks/task_20260823_wangyuyan-gate-external-supervision.md` | P2门禁维度扩展;防假门禁+监督盲区;执行前老朱拍板规范改;与#433/#435同族 |
<!-- REVIEW-PENDING-BEGIN（queue_transition 自动维护，勿手改） -->

## ⚖️ 待终审（提审任务，queue_transition 自动登记）

> 欧阳锋开工只看这段：有行就审，终审后自动划掉。历史任务不回填（#389，只向前生效）。

- ~~#446 task_20260823_laowantong-role-special-huangyaoshi｜laowantong｜提审 08-23 12:29｜60_feedback/tasks/task_20260823_laowantong-role-special-huangyaoshi.md~~ → 已终审 PASS A（2026-08-23 欧阳锋）
- ~~#445 task_20260823_huangyaoshi-oneclick-agent-launcher｜huangyaoshi｜提审 08-23 12:46｜60_feedback/tasks/task_20260823_huangyaoshi-oneclick-agent-launcher.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#451 task_20260823_laowantong-spec-exec-report-rule｜laowantong｜提审 08-23 13:16｜60_feedback/tasks/task_20260823_laowantong-spec-exec-report-rule.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#453 task_20260823_huangyaoshi-queue-archive-slim｜huangyaoshi｜提审 08-23 13:18｜60_feedback/tasks/task_20260823_huangyaoshi-queue-archive-slim.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#447 task_20260823_laowantong-role-special-fengqingyang｜laowantong｜提审 08-23 13:24｜60_feedback/tasks/task_20260823_laowantong-role-special-fengqingyang.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#454 task_20260823_laowantong-fengqingyang-l1-l4-caliber｜laowantong｜提审 08-23 13:25｜60_feedback/tasks/task_20260823_laowantong-fengqingyang-l1-l4-caliber.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#455 task_20260823_laowantong-spec-boundary-ask-first｜laowantong｜提审 08-23 13:49｜60_feedback/tasks/task_20260823_laowantong-spec-boundary-ask-first.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#449 task_20260823_laowantong-file-flow-protocol｜laowantong｜提审 08-23 13:51｜60_feedback/tasks/task_20260823_laowantong-file-flow-protocol.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#457 task_20260823_huangyaoshi-disposal-gate-structured｜huangyaoshi｜提审 08-23 13:55｜60_feedback/tasks/task_20260823_huangyaoshi-disposal-gate-structured.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#458 task_20260823_huangyaoshi-friction-auto-report｜huangyaoshi｜提审 08-23 14:05｜60_feedback/tasks/task_20260823_huangyaoshi-friction-auto-report.md~~ → 终审退回 queued（2026-08-23 欧阳锋）
- ~~#460 task_20260823_huangyaoshi-issue-report-automation-final｜huangyaoshi｜提审 08-23 14:15｜60_feedback/tasks/task_20260823_huangyaoshi-issue-report-automation-final.md~~ → 终审退回 queued（2026-08-23 欧阳锋）
- ~~#448 task_20260823_laowantong-role-special-zhu｜wangyuyan｜提审 08-23 14:30｜60_feedback/tasks/task_20260823_laowantong-role-special-zhu.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#460 task_20260823_huangyaoshi-issue-report-automation-final｜huangyaoshi｜提审 08-23 15:08｜60_feedback/tasks/task_20260823_huangyaoshi-issue-report-automation-final.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#461 task_20260823_huangyaoshi-queue-cancel-command｜huangyaoshi｜提审 08-23 15:19｜60_feedback/tasks/task_20260823_huangyaoshi-queue-cancel-command.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#462 task_20260823_huangyaoshi-probe-review-done-signal｜huangyaoshi｜提审 08-23 15:22｜60_feedback/tasks/task_20260823_huangyaoshi-probe-review-done-signal.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#463 task_20260823_huangyaoshi-l1-full-context-capture｜huangyaoshi｜提审 08-23 15:30｜60_feedback/tasks/task_20260823_huangyaoshi-l1-full-context-capture.md~~ → 终审退回 queued（2026-08-23 欧阳锋）
- ~~#464 task_20260823_huangyaoshi-mirror-on-save｜huangyaoshi｜提审 08-23 15:34｜60_feedback/tasks/task_20260823_huangyaoshi-mirror-on-save.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#463 task_20260823_huangyaoshi-l1-full-context-capture｜huangyaoshi｜提审 08-23 15:44｜60_feedback/tasks/task_20260823_huangyaoshi-l1-full-context-capture.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#456 task_20260823_huangyaoshi-agentid-audit-fix｜huangyaoshi｜提审 08-23 15:52｜60_feedback/tasks/task_20260823_huangyaoshi-agentid-audit-fix.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#465 task_20260823_laowantong-banfeimao-ai-kb-cards｜laowantong｜提审 08-23 16:00｜60_feedback/tasks/task_20260823_laowantong-banfeimao-ai-kb-cards.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#450 task_20260823_huangyaoshi-file-flow-lint｜huangyaoshi｜提审 08-23 16:12｜60_feedback/tasks/task_20260823_huangyaoshi-file-flow-lint.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#466 task_20260823_laowantong-banfeimao-b-manuals｜laowantong｜提审 08-23 18:26｜60_feedback/tasks/task_20260823_laowantong-banfeimao-b-manuals.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#467 task_20260823_laowantong-banfeimao-c-cases｜laowantong｜提审 08-23 18:35｜60_feedback/tasks/task_20260823_laowantong-banfeimao-c-cases.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#426 task_20260822_laowantong-tags-judgment-batch｜laowantong｜提审 08-23 19:15｜60_feedback/tasks/task_20260822_laowantong-tags-judgment-batch.md~~ → 首批试点批验收通过（2026-08-23 欧阳锋，批次验收——队列行恢复 queued 继续）
- ~~#471 task_20260823_huangyaoshi-l1-capture-scheduling｜huangyaoshi｜提审 08-23 19:26｜60_feedback/tasks/task_20260823_huangyaoshi-l1-capture-scheduling.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#472 task_20260823_huangyaoshi-role-routes｜huangyaoshi｜提审 08-23 19:30｜60_feedback/tasks/task_20260823_huangyaoshi-role-routes.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#473 task_20260823_huangyaoshi-file-flow-lint-residuals｜huangyaoshi｜提审 08-23 19:33｜60_feedback/tasks/task_20260823_huangyaoshi-file-flow-lint-residuals.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#426 task_20260822_laowantong-tags-judgment-batch｜laowantong｜提审 08-23 19:51｜60_feedback/tasks/task_20260822_laowantong-tags-judgment-batch.md~~ → 第二批（ai-collaboration）验收通过（2026-08-23 欧阳锋，批次验收——恢复 queued 继续）
- ~~#474 task_20260823_huangyaoshi-tags-audit-fullscan｜huangyaoshi｜提审 08-23 20:18｜60_feedback/tasks/task_20260823_huangyaoshi-tags-audit-fullscan.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#426 task_20260822_laowantong-tags-judgment-batch｜laowantong｜提审 08-23 20:46｜60_feedback/tasks/task_20260822_laowantong-tags-judgment-batch.md~~ → 第三批（ai-collaboration dk）验收通过（2026-08-23 欧阳锋，批次验收——恢复 queued 继续）
- ~~#477 task_20260823_huangyaoshi-task-docid-field-removal｜huangyaoshi｜提审 08-23 21:01｜60_feedback/tasks/task_20260823_huangyaoshi-task-docid-field-removal.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#478 task_20260823_huangyaoshi-review-check-failure-detail｜huangyaoshi｜提审 08-23 21:03｜60_feedback/tasks/task_20260823_huangyaoshi-review-check-failure-detail.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#479 task_20260823_huangyaoshi-queue-batch-accept｜huangyaoshi｜提审 08-23 21:08｜60_feedback/tasks/task_20260823_huangyaoshi-queue-batch-accept.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#426 task_20260822_laowantong-tags-judgment-batch｜laowantong｜提审 08-23 21:12｜60_feedback/tasks/task_20260822_laowantong-tags-judgment-batch.md~~ → 批次验收（A）（2026-08-23）
- ~~#426 task_20260822_laowantong-tags-judgment-batch｜laowantong｜提审 08-23 21:44｜60_feedback/tasks/task_20260822_laowantong-tags-judgment-batch.md~~ → 批次验收（A）（2026-08-23）
- ~~#426 task_20260822_laowantong-tags-judgment-batch｜laowantong｜提审 08-23 22:46｜60_feedback/tasks/task_20260822_laowantong-tags-judgment-batch.md~~ → 批次验收（A）（2026-08-23）
- ~~#469 task_20260823_laowantong-addiction-book-cards｜laowantong｜提审 08-23 23:40｜60_feedback/tasks/task_20260823_laowantong-addiction-book-cards.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#482 task_20260823_huangyaoshi-batch-accept-commit-bugfix｜huangyaoshi｜提审 08-23 23:51｜60_feedback/tasks/task_20260823_huangyaoshi-batch-accept-commit-bugfix.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#483 task_20260823_huangyaoshi-gate-blocked-noise-filter｜huangyaoshi｜提审 08-23 23:53｜60_feedback/tasks/task_20260823_huangyaoshi-gate-blocked-noise-filter.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#484 task_20260823_huangyaoshi-tags-source-word-blacklist｜huangyaoshi｜提审 08-23 23:55｜60_feedback/tasks/task_20260823_huangyaoshi-tags-source-word-blacklist.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）
- ~~#481 task_20260823_laowantong-shushui-addiction-supplement｜laowantong｜提审 08-24 00:02｜60_feedback/tasks/task_20260823_laowantong-shushui-addiction-supplement.md~~ → 已终审 PASS A-（2026-08-23 欧阳锋）

<!-- REVIEW-PENDING-END -->

<!-- INBOX-PENDING-BEGIN（watch_inbox 自动维护，勿手改） -->

## 📥 待编排（inbox 新素材，watch_inbox 自动登记）

> 王语嫣维护看板时处理：诊断 → 写任务单 → 入队后把对应行划掉。编排规则不变，这里只解决「没人被通知」。

- ~~00_inbox/半肥猫开放麦-AI知识库文件夹/AI×知识管理-开放麦-逐字稿.md｜P2｜59975B｜检测到 08-22 16:41｜待王语嫣编排~~ → 已编排：三方法诊断（九层深挖+逐字读+全网调研，diag D-20260823-008）+ 知识生产 #465（A档11卡）+ #426 词表方向（五维标注框架）——2026-08-23 王语嫣
- 00_inbox/半肥猫开放麦-AI知识库/AI×知识管理-开放麦-逐字稿.md｜P2｜59975B｜检测到 08-23 06:31｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/AI知识库-知识库搭建与落地-半肥猫-口述.txt｜P0｜139481B｜检测到 08-23 07:01｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/AI知识库-知识库搭建与落地-半肥猫-笔记.txt｜P0｜9489B｜检测到 08-23 07:01｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823145914.png｜P2｜1461080B｜检测到 08-23 07:01｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823145932.png｜P2｜1650162B｜检测到 08-23 07:01｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/_ocr_text.md｜P2｜9441B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/_vlm_desc.md｜P2｜21773B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150146.png｜P2｜805084B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150154.png｜P2｜345935B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150203.png｜P2｜322050B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150216.png｜P2｜867325B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150223.png｜P2｜868352B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150231.png｜P2｜1407452B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150247.png｜P2｜1334738B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150307.png｜P2｜2117101B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150324.png｜P2｜2335680B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150336.png｜P2｜237804B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150342.png｜P2｜211502B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150350.png｜P2｜174736B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150358.png｜P2｜1326426B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/一堂DOC-20260823150410.png｜P2｜1235595B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/批注 2026-08-23 150123.png｜P2｜146628B｜检测到 08-23 07:11｜待王语嫣编排
- 00_inbox/半肥猫开放麦-AI知识库/给王语嫣的任务编排建议-半肥猫开放麦-AI知识库.md｜P0｜11494B｜检测到 08-23 07:31｜待王语嫣编排
- 00_inbox/拆书会第216期-成瘾-逐字稿.md｜P2｜32637B｜检测到 08-23 08:01｜待王语嫣编排
- 00_inbox/拆书会第216期：《成瘾》逐字稿.md｜P2｜32400B｜检测到 08-23 08:11｜待王语嫣编排
- 00_inbox/一堂-成瘾与自我管理分享-口述.docx｜P0｜76513B｜检测到 08-23 14:11｜待王语嫣编排
- 00_inbox/一堂-成瘾与自我管理分享-口述.md｜P0｜162598B｜检测到 08-23 14:21｜待王语嫣编排

<!-- INBOX-PENDING-END -->

<!-- PROPOSAL-PENDING-BEGIN（自动登记：conveyor_probe.py；勿手改——王语嫣复核后划掉） -->

## 📬 PROPOSAL-PENDING（建议书到达，conveyor_probe.py 自动登记）

> 王语嫣复核立项后划掉该行（流程不变）。勿手改段结构——重跑会整块重写。

- ~~diag_20260823_huangyaoshi-verification-tier-addendum.md｜08-23 12:05｜待王语嫣复核裁定~~ → 编排决策（08-23 王语嫣）：**关闭**——四态口径已被 #446 入宪 §2.6.4 吸收（黄药师 spec v1.0 含三铁律+分层四态声明）；文档留档作口径演进链
- ~~diag_20260823_fengqingyang-memory-capsule-4layer-l1-l4.md｜08-23 12:45｜待王语嫣复核裁定~~ → 已复核裁定（2026-08-23 王语嫣独立判断，老朱令）：**单项说明为主**——架构入宪 charter §3.12（L1-L4+三铁边界，已修订）；风清扬 spec 只写他那一层（L2 本职+三边界，#454 传口径给 #447）；外部残留改名挂 F-044（黄药师，缓）
- ~~diag_20260823_ouyangfeng-queue-slim-handover.md｜08-23 12:48｜待王语嫣复核裁定~~ → 编排决策（08-23 王语嫣）：**关闭**——移交确认（首次瘦身保留价值，cron 已删，维护权已固化 spec v1.2）；踩坑三教训（表头正则排除/归档后双验证/终态口径）供 #453 黄药师实施参照
- ~~diag_20260823_fengqingyang-memory-capsule-query-and-agent-id.md｜08-23 13:21｜待王语嫣复核裁定~~ → 编排决策（08-23 王语嫣）：**部分采纳**——建议 3（agent_id 统一拼音角色名+清测试残留）立项 **#456**（黄药师）；建议 1（query 只读命令）挂停车场 F-045 等老朱拍板 L1 开放口径后连同实施；建议 2 上报老朱（开放对象/只读权限/查询审计痕迹三点）
- ~~diag_20260823_ouyangfeng-188-residual-disposition.md｜08-23 13:37｜待王语嫣复核裁定~~ → 编排决策（08-23 王语嫣）：**采纳推荐项①补登记对齐**——#188 队列行走 queue_transition review 补登记（任务单 07-19 已终审 A-，纯历史对齐）；审计器解析盲区修复并入 **#456**（黄药师，行数异常禁静默跳过）
- ~~diag_20260823_laowantong-disposal-keyword-misjudgment.md｜08-23 15:45｜待王语嫣复核裁定~~ → 编排决策（08-23 王语嫣）：**采纳方案 1+2 组合立项 #457**（显式标记优先+关键词降级提示+限定动作节）；注：本建议书 status: pending 三元组不全致探针未登记——沉没问题活体实例，自动上报机制立项 #458 一并根治
- ~~[gate-blocked] task_20260823_huangyaoshi-issue-report-automation-final｜08-23 14:21｜待王语嫣复核处置｜2026-08-23 14:15:21｜task_20260823_huangyaoshi-issue-report-automation-final｜F-034-五字段｜执行报告缺 5 个字段（#429 F-034）：改动文件清单、完成内容一句话、验证命令+输出、未做项/边界、需要谁动作。请补全后重试，或 --force --reason '<理由>' 声明例外（#4｜huangyaoshi~~ → 已处置关闭（黄药师实施中被拦后自修复；#460 后被终审 FAIL 退回修复中——机器自报层首日活体运行实证 ✅）
- ~~[gate-blocked] task_9999_force-test｜08-23 14:31｜待王语嫣复核处置｜2026-08-23 14:27:13｜task_9999_force-test｜F-034-force无理由｜--force 未配 --reason（#444 例外留痕要求）｜wangyuyan~~ → 测试件关闭（#460 L2 狗粮：force 无 reason 拦截验证，拦截正确=验收通过）
- ~~[gate-blocked] task_20260823_laowantong-role-special-zhu｜08-23 14:31｜待王语嫣复核处置｜2026-08-23 14:29:30｜task_20260823_laowantong-role-special-zhu｜F-034-五字段｜执行报告缺 5 个字段（#429 F-034）：改动文件清单、完成内容一句话、验证命令+输出、未做项/边界、需要谁动作。请补全后重试，或 --force --reason '<理由>' 声明例外（#4｜wangyuyan~~ → 已处置关闭（占位节拦截，当场补齐归位后 complete 通过，#448 已 pending_review）
- ~~[gate-blocked] task_9999_force-test｜08-23 15:11｜待王语嫣复核处置｜2026-08-23 15:08:42｜task_9999_force-test｜F-034-force无理由｜--force 未配 --reason（#444 例外留痕要求）｜wangyuyan~~ → 测试件关闭（#460 修复中 L2 狗粮：force 无 reason 拦截复验）
- ~~[gate-blocked] task_9999_test｜08-23 15:11｜待王语嫣复核处置｜2026-08-23 15:08:42｜task_9999_test｜处置-硬门禁｜disposal:true 缺「内容价值判断」节（PROTOCOL §7）｜task_9999_test~~ → 测试件关闭（#460 处置硬门禁插桩验证——插桩已生效实证 ✅）
- ~~[gate-blocked] task_t_disposal｜08-23 15:11｜待王语嫣复核处置｜2026-08-23 15:11:02｜task_t_disposal｜处置-硬门禁｜disposal:true 缺「内容价值判断」节（PROTOCOL §7）｜task_t_disposal~~ → 测试件关闭（同上，处置门禁拦截落盘验证）
- ~~diag_20260823_ouyangfeng-dictation-record-discipline.md｜08-23 15:15｜待王语嫣复核裁定~~ → 已采纳（08-23 王语嫣）：①№5/№6 补录=新增件 D-20260823-007（amends:D-20260823-002），spec source_refs 已补指向；②口述落盘纪律入宪 §3.13（到达即转录不隔夜+№溯源 lint 挂 #450）——断链教训：№5/№6 只在会话顺手织入卡片未录原文
- ~~[gate-blocked] task_9999_force-test｜08-23 15:21｜待王语嫣复核处置｜2026-08-23 15:15:57｜task_9999_force-test｜F-034-force无理由｜--force 未配 --reason（#444 例外留痕要求）｜wangyuyan~~ → 测试件/已处置关闭（#460 验证期拦截记录）
- ~~[gate-blocked] task_9999_test｜08-23 15:21｜待王语嫣复核处置｜2026-08-23 15:15:57｜task_9999_test｜处置-硬门禁｜disposal:true 缺「内容价值判断」节（PROTOCOL §7）｜task_9999_test~~ → 测试件/已处置关闭（#460 验证期拦截记录）
- ~~[gate-blocked] task_20260823_huangyaoshi-issue-report-automation-final｜08-23 15:22｜待王语嫣复核处置｜2026-08-23 14:15:21｜task_20260823_huangyaoshi-issue-report-automation-final｜F-034-五字段｜执行报告缺 5 个字段（#429 F-034）：改动文件清单、完成内容一句话、验证命令+输出、未做项/边界、需要谁动作。请补全后重试，或 --force --reason '<理由>' 声明例外（#4｜huangyaoshi~~ → 测试件/已处置关闭（#460 验证期拦截记录）
- ~~[gate-blocked] task_20260823_laowantong-role-special-zhu｜08-23 15:22｜待王语嫣复核处置｜2026-08-23 14:29:30｜task_20260823_laowantong-role-special-zhu｜F-034-五字段｜执行报告缺 5 个字段（#429 F-034）：改动文件清单、完成内容一句话、验证命令+输出、未做项/边界、需要谁动作。请补全后重试，或 --force --reason '<理由>' 声明例外（#4｜wangyuyan~~ → 测试件/已处置关闭（#460 验证期拦截记录）
- ~~[gate-blocked] task_t_disposal｜08-23 15:22｜待王语嫣复核处置｜2026-08-23 15:11:02｜task_t_disposal｜处置-硬门禁｜disposal:true 缺「内容价值判断」节（PROTOCOL §7）｜task_t_disposal~~ → 测试件/已处置关闭（#460 验证期拦截记录）
- ~~diag_20260823_ouyangfeng-file-flow-lint-residuals.md｜08-23 18:25｜待王语嫣复核裁定~~ → 已采纳立项 **#473**（08-23 王语嫣）：三项按优先级收口；L9 全库一次扫描；冻结基线采无状态方案
- ~~diag_20260823_fengqingyang-l1-capture-scheduling.md｜08-23 18:51｜待王语嫣复核裁定~~ → 已采纳立项 **#471**（08-23 王语嫣）：常驻调度+体积红线并入一单；**老朱拍板常驻注册**为开工前提（#432 边界）；L3 回放抽查延后可
- ~~diag_20260823_huangyaoshi-role-routes.md｜08-23 19:01｜待王语嫣复核裁定~~ → 已采纳立项 **#472**（08-23 王语嫣）：三路由合一；四个待讨论点已裁定（depends_on 字段/编排维护路由表/10-20 张 Core/任务路由 only 脚本化）；F-047 登记 depends_on 字段演进
- ~~[gate-blocked] task_20260822_laowantong-tags-judgment-batch｜08-23 19:21｜待王语嫣复核处置｜2026-08-23 19:13:58｜task_20260822_laowantong-tags-judgment-batch｜F-034-五字段｜任务单缺少「## 执行报告」节（#429 F-034：交付必须落执行报告，口头完成=未完成；#444：evidence 附件不能替代）｜hermes~~ → 已处置关闭（#426 已恢复 queued 继续分批，第五六批验收通过；批次报告已补，gate-blocked 19:21 历史拦截记录关闭）
- ~~[gate-blocked] task_9999_force-test｜08-23 19:31｜待王语嫣复核处置｜2026-08-23 19:29:12｜task_9999_force-test｜F-034-force无理由｜--force 未配 --reason（#444 例外留痕要求）｜wangyuyan~~ → 测试件关闭（#460 force 无 reason 拦截验证期记录）
- ~~[gate-blocked] task_9999_test｜08-23 19:31｜待王语嫣复核处置｜2026-08-23 19:29:12｜task_9999_test｜处置-硬门禁｜disposal:true 缺「内容价值判断」节（PROTOCOL §7）｜task_9999_test~~ → 测试件关闭（#460 处置硬门禁拦截验证期记录）
- ~~diag_20260823_ouyangfeng-task-docid-violation.md｜08-23 19:38｜待王语嫣复核裁定~~ → 编排决策（2026-08-23 王语嫣独立判断）：**采纳方向①**——任务单模板移除 doc_id 字段（回归规范 #449，E045 三套编号不混用维持）；存量 10+ 份 lint 全扫出清单→dry-run→单卡验证→人工审→批量移除；spec 卡 doc_id 同步移除；#450 lint 已把门，模板修掉断源；纠偏非口径变更不需老朱拍板 → 立项 **#477**（黄药师，P2）
- ~~diag_20260823_huangyaoshi-review-check-a-criteria.md｜08-23 19:58｜待王语嫣复核裁定~~ → 编排决策（2026-08-23 王语嫣独立判断）：**部分采纳**——①agent-os §10.4.1 补「问题节必填(#458)」与探测器逻辑对齐（**改 agent-os 需老朱拍板窗口**，文档对齐非新规则）；②review-check 判 B/C 输出失败项明细（差异可自解释，E049 同族）立项 **#478**（黄药师，P2）；③王语嫣自办重跑 review-check 验证 08-23 复盘（晚间场已含问题节）能否回 A
- ~~diag_20260823_fengqingyang-codex-instance-isolation.md｜08-23 20:11｜待王语嫣复核裁定~~ → 编排决策（2026-08-23 王语嫣独立判断）：**部分采纳**——建议1 CODEX_HOME 分家**缓议**（当前无角色用 codex，#445 映射证实；预防性基建无即时收益，触发=某角色切 codex）登记停车场 **F-048**；建议2 L1 采集面是否纳 Codex sessions **上报老朱拍板**（codex 定性=个人工具/工厂角色工具决定）；建议3 通用纪律（角色 CLI 实例独立+L1 采集面覆盖）**采纳方向**挂 F-043 charter v1.0 修订窗口
- ~~diag_20260823_ouyangfeng-batch-accept-tool.md｜08-23 20:15｜待王语嫣复核裁定~~ → 编排决策（2026-08-23 王语嫣独立判断）：**采纳立项**——#426 剩余 100+ 张 tags 批次，批次验收静默失败已实证（漏恢复队列行，第 4 次执行输出与实测不符）；queue_batch_accept.py 复用 queue-archive(#453) 成熟模式（四步一体+每步断言+前后对账+dry-run+原子 commit）；治静默失败在工具层（B2-4 想犯错也犯不了） → 立项 **#479**（黄药师，P1，#426 批次线）
- ~~diag_20260823_ouyangfeng-tags-content-check-audit.md｜08-23 20:44｜待王语嫣复核裁定~~ → 编排决策（2026-08-23 王语嫣独立判断）：**采纳**——1 #426 后续批次验收标准升级（抽查≥3 张读正文+机械辅助高频词重叠比对<50%标记+验收记录声明抽查范围）；2 存量决策域44+ai-collaboration35 按域抽 10-15% 读正文复查（机械辅助优先筛可疑卡，增量不推翻已验收）；3 dk-research-decision-first-mapping 补主题词（老顽童执行）。#426 上板冻结(E047)→走口径单传口径不改本体；机械辅助挂 #474 tags-audit 扩展 → 立项 **#480**（口径单，传老顽童+欧阳锋）
- ~~diag_20260823_ouyangfeng-batch-blocking-exemption.md｜08-23 21:40｜待王语嫣复核裁定~~ → 编排决策（2026-08-24 王语嫣独立判断）：**采纳方向**（方案一 batch:true 标记 + can_claim 跳过 batch 任务 pending_review 阻塞，状态机小改根治）——但改 can_claim 状态机逻辑需老朱拍板方案（一/二/三）；#479 queue_batch_accept 已上线保障批次验收节奏，阻塞仅批次 pending_review 期间暂态 → 登记 **F-050**（待老朱拍板）
- ~~diag_20260823_ouyangfeng-batch-accept-commit-bug.md｜08-23 22:30｜待王语嫣复核裁定~~ → 编排决策（2026-08-24 王语嫣独立判断）：**采纳立项 #482**——#479 queue_batch_accept.py commit 收口 pathspec 相对路径 bug（两次实证：#426 第四五批，欧阳锋手动补 commit 兜底）；修复=绝对路径或 chdir 对齐+回归用例（从非仓库根调用场景）；P1 #426 批次线（收口 bug 影响 E040）；黄药师小修 → 立项 **#482**
- ~~diag_20260823_fengqingyang-l1-periodic-audit.md｜08-23 22:35｜待王语嫣复核裁定~~ → 编排决策（2026-08-24 王语嫣独立判断）：**部分采纳**——L1 第一期审计洞察报告留档（L2 产出不入队列，洞察1/2 已工具化 #433/#435+执行报告五字段，洞察3/4 认知沉淀）；建议1（L1 采集面补 Codex/opencode/qwen）+建议2（codex-homes 切换时机）挂 **F-048**（codex 定性老朱拍板，同族）；建议3（agent复盘 目录双轨收敛+事件库 agent_id 与落盘路径一致）挂 **#367**（双轨收敛 08-26 到期后一并）；建议4（gate-blocked.log 测试噪声过滤）立项 **#483**（黄药师小修）；建议5（ouyangfeng/hongqigong 08-23 快照缺口）王语嫣自办核对（不催）；建议6（activity_log 缺 id 2/6 核查）采纳黄药师核查
- ~~diag_20260823_ouyangfeng-source-word-blacklist.md｜08-23 23:19｜待王语嫣复核裁定~~ → 编排决策（2026-08-24 王语嫣独立判断）：**采纳**——建议1（tags-audit 加来源形态词黑名单检查，第5指标=来源词污染率，目标<1%）立项 **#484**（黄药师 P2，挂 #474 tags-audit 扩展，排队 #482→#483→#484 禁同轮≥3）；建议2（存量清理 2 张已发现卡+随 #426 批次）挂 #426/#480 批次；建议3（轴文件注记：内容词=主题词，来源形态词禁入内容词池）王语嫣自办——与 F-046（来源轴）+ tags-vocab-design「来源名禁入 tags」同族，本建议把已有规则工具化为检查器（想犯错也犯不了）

- ~~diag_20260823_laowantong-vocab-axis-before-batch.md｜08-23 23:30｜待王语嫣复核裁定~~ → 编排决策（2026-08-24 王语嫣）：**采纳**——③gate化「轴文件先行」（域未出轴不得进#426治理队列）+①剩余域轴批量出；与E054同根（建轴义务主动化机制层）；落tags-vocab-design补条目（需老朱拍板）→ 立项 **#485**
- ~~diag_20260823_laowantong-gate-external-supervision-dimension.md｜08-23 深夜｜待王语嫣复核裁定~~ → 编排决策（2026-08-24 王语嫣）：**采纳**——门禁设计加「外部监督者」必问维度（无外部监督者=个人自绑定，不得声称组织级门禁）；补#469诊断同构背书的监督差异边界；落file-flow-protocol/KF-024补条目（需老朱拍板）→ 立项 **#486**
<!-- PROPOSAL-PENDING-END -->
| 430 | `task_20260823_huangyaoshi-agent-review-gitify` | agent复盘 目录 git 化 / E040 适用范围裁定（P1，F-036 提升）：组织记忆可追踪或口径兜底 | reviewed | huangyaoshi | 裁定+实施/口径+实测 | 无 | `60_feedback/tasks/task_20260823_huangyaoshi-agent-review-gitify.md` | #423 条件项第 2 次实证升级；方案 A 独立 git 化为主，B 仅兜底；不迁目录不改复盘内容；08-26 归档前定；欧阳锋终审 |
| 431 | `task_20260823_laowantong-role-special-laowantong` | 角色专场第一场：老顽童岗位说明书定稿（P1，F-028 开场） | reviewed | laowantong | 五要素 spec 升级 | 无 | `60_feedback/tasks/task_20260823_laowantong-role-special-laowantong.md` | 底本=风清扬五角色建议书；必含 B2-3 两条血泪+老顽童两条补充+G1/G2；一角色一张过，老朱拍板后才开欧阳锋场；欧阳锋终审 |
| 432 | `task_20260823_huangyaoshi-memory-capsule-l0-minimal` | 记忆胶囊 L0 最小实现（P1，F-027 第一阶段）：A 本机主库 + B 第二盘镜像 + verify 恢复演练 | reviewed | huangyaoshi | L0 库+镜像+verify | 无 | `60_feedback/tasks/task_20260823_huangyaoshi-memory-capsule-l0-minimal.md` | #427 拍板 A+B/C 缓议；只做 L0，不做 L1-L3；不注册常驻计划任务（需老朱确认命令）；狗粮=写入→镜像→恢复→verify；欧阳锋终审 |
| 433 | `task_20260823_huangyaoshi-negative-claim-gate` | 负向判词证据层门禁（P1，审查端 F-035 对称补全）：无 `**存在性核查**` 锚点的「无/缺/未」判词不闭环 | reviewed | huangyaoshi | 门禁+复现用例 | 无 | `60_feedback/tasks/task_20260823_huangyaoshi-negative-claim-gate.md` | 风清扬建议书采纳；不改已审 #419/#429；只拦锚点不判核查质量；复现用例=#430 坚果云/FQ-E04/FQ-E01；欧阳锋终审 |
| 434 | `task_20260823_huangyaoshi-memory-capsule-l0-autowrite` | 记忆胶囊 L0 自动写入端（P1，F-027 下一阶段）：daily-context-save 成功保存即自动写 L0 事件 | reviewed | huangyaoshi | save 挂钩+失败可见 | #433 先序 | `60_feedback/tasks/task_20260823_huangyaoshi-memory-capsule-l0-autowrite.md` | 黄药师建议书采纳：方案 A 先行，B 扫描器缓议，C 挂 F-033；单写入面/失败可见；权责=黄药师建设、风清扬审计；欧阳锋终审 |
| 441 | `task_20260823_laowantong-role-special-ouyangfeng` | 角色专场第二场：欧阳锋岗位说明书定稿（P1，F-028 第二场） | reviewed | laowantong | 五要素 spec 升级 | #431 老朱已拍板 | `60_feedback/tasks/task_20260823_laowantong-role-special-ouyangfeng.md` | 底本=风清扬五角色建议书；必含终审分界/审而不改/批次验收≠整单终审/审查者不直接编排/建议书抽查回查数据层/F-035+#433 审查门禁；aliases 禁路径词；欧阳锋终审、老朱终稿 |
| 435 | `task_20260823_huangyaoshi-negative-gate-vocab-data` | 负向判词门禁词表扩展（P1，数据异常类修正落点）：为空/空值进强词；截断/损坏/乱码/半写走正则或宽词观察 | reviewed | huangyaoshi | 词表+正则+回归 | #433 已 reviewed | `60_feedback/tasks/task_20260823_huangyaoshi-negative-gate-vocab-data.md` | 欧阳锋方向采纳 + 风清扬修正落点；数据视图声明归 SOP 不进门禁；不改已审 #433 内容；欧阳锋终审 |
| 442 | `task_20260823_huangyaoshi-negative-gate-strong-word-fix` | 负向门禁强词误伤返工（P1，#435 审计返工）：STRONG 删「为空/空值」走正则 + 补「不为空/非空值」否定式反例 | reviewed | huangyaoshi | 词表修正+反例回归 | #435 已 reviewed（风清扬审计 diag_20260823_fengqingyang-gate-435-audit.md） | `60_feedback/tasks/task_20260823_huangyaoshi-negative-gate-strong-word-fix.md` | 一行级修正：STRONG 10→8 词，正则不动；正测「grade 为空/值为空」仍拦，反测「不为空/非空值」不误伤；pytest 全过；欧阳锋复审抽否定式反例 |
| 443 | `task_20260823_huangyaoshi-probe-notify-assignee-routing` | 探针可领取通知按 assignee 路由（P1，#421 演进）：修硬编码 laowantong + 补 huangyaoshi 通道 | reviewed | huangyaoshi | 路由映射+通道+用例 | #442 立项实证（老朱指令入队） | `60_feedback/tasks/task_20260823_huangyaoshi-probe-notify-assignee-routing.md` | 未知 assignee 回落 laowantong 不静默丢；通道缺失 dry-run 降级；不动已审 #421 幂等/静默/单扫描器纪律；REVIEW/PROPOSAL 两条既有路由不改；活体验收=下张 huangyaoshi 单落队实测；欧阳锋终审 |
| 444 | `task_20260823_huangyaoshi-queue-force-ledger-assignee-role` | queue_transition 交接语义加固（P1，风清扬建议 1+3 裁定合并）：--force/--evidence 例外台账 + frontmatter assignee 角色名口径 | reviewed | huangyaoshi | 台账+口径改造+用例 | #441 complete --force 绕过 F-034 实证 | `60_feedback/tasks/task_20260823_huangyaoshi-queue-force-ledger-assignee-role.md` | force 无 --reason 拒绝；evidence 路径留档且五字段必须落任务单；assignee 只写角色名+instance 另存，存量实例名兼容不回改；裁定=diag_20260823_wangyuyan-441-rework-ruling.md §二；欧阳锋终审 |
