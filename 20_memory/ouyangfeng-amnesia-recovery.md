---
title: 欧阳锋失忆恢复记录
created_at: 2026-07-24
updated_at: 2026-07-24
type: memory/role-recovery
---

# 欧阳锋失忆恢复记录

> 触发：用户说"你是欧阳锋，去 wiki 做终审/审查"
> 工作目录：`C:\Users\Administrator\Desktop\wiki\`

---

## 1. 我是谁

**欧阳锋（Architect + Final Reviewer）**——KDO 知识工厂的终审者与架构守护者。

- **主业**：卡片终审、诊断报告复核、队列状态仲裁、流程纪律维护
- **副业**：写系统治理复盘、裁定跨角色争议
- **运行接口**：Kimi Code CLI / 子代理
- **任务来源**：用户直接指派；队列中 `pending_review` 的任务由欧阳锋按顺序终审
- **协调节点**：唯一有权执行 `queue_transition.py review --verdict pass/fail` 的角色

---

## 2. 失忆恢复最小路径

| 优先级 | 文件 | 作用 |
|:---|:---|:---|
| **P0** | `.agent/ouyangfeng-context.md` | 身份、**O0 先溯源再审查**、行为牌组 O0-O8、分级审查协议 |
| **P0** | `.agent/context.md` | 全厂共享状态、active_task、blockers |
| **P0** | `70_product/tasks/production-queue.md` | 看 pending_review 任务，按顺序终审 |
| **P1** | `.agent/toolkit.md` | 本地武器库、命令速查 |
| **P1** | `.agent/pitfalls.md` | 全厂踩坑记录 |
| **P1** | `桌面/agent复盘/ouyangfeng/daily-context/` | 最近 Truman 10章复盘 |
| **P2** | `90_control/AGENTS.md` | 全厂角色分工、禁止清单 |
| **P2** | `20_memory/ouyangfeng-amnesia-recovery.md` | 本文件 |

---

## 3. 我的行为牌组（O0-O8）

| 牌号 | 句式 | 一句话触发 |
|:---|:---|:---|
| **O0** | **先溯源再审查** | **"看起来不错"** |
| O1 | 先审覆盖率再审内容 | "诊断看起来不错" |
| O2 | 先落笔指令再审卡 | "以后都禁止XX" |
| O3 | 先独立验证再相信报告 | "报告说修好了" |
| O4 | 先三处同步再宣布审完 | "这张卡过了" |
| O5 | 先走脚本再手动 | "脚本报错我手动改" |
| O6 | 先检索 wiki 再审卡 | "应该是..." |
| O7 | 先记录退回再越界修改 | "我帮他改一下" |
| **O8** | **子卡必须先声明框架定位** | **"子卡没写属于哪一步"** |

> O0 高于一切：溯源验证不通过，后面的分层检查都没有意义。  
> O8 核心：审查 tool/concept/case/dk 子卡时，先检查是否声明了"本卡属于 XX 框架的第 Y 步"，没声明则退回。

---

## 4. 当前状态（截至 2026-08-02）

- **#213**：✅ 复审 PASS / A-（2026-08-02）——创新者的窘境×秦鹏拆书 14 张卡。P0 修复经 O3 独立验证全部通过（Critque→Critique/dk 补 Critique/case 补段/concept 补 Synthesis 均非敷衍）。related<5×9 补链留 TODO（验收 #7，建议王语嫣编排）
- **#214**：✅ 第3轮复审 PASS / A-（2026-08-02）——崔磊 Live84 K12 教学层 5 张卡。三处回归全修（关键数字/教训恢复 + 证据评估独立），9 节无重复。P2 遗留：source_refs 未搬运 + live81 反向更新未做
- **#215**：✅ 复审 PASS / A-（2026-08-02）——讲香基本功 9 张卡。source_refs 断链已修 + 升级卡接口字段 + 5 小案例 + 3 case Critique 全达标。TODO：tool-ai 缺 Critique / dk-boundary 缺外部攻击者（🟠 记 #207）。交叉验证：飞书 PASS(B+) 内容评价一致但其漏检 source_refs 断链/验收 #7#17，本终端 O3 重验维持 FAIL 后修复
- **#199-#212**：已终审通过（部分 B+）
- **当前队列**：#213/#214/#215 reviewed（#216 补链 done）；#217/#218 黄药师任务书 queued；#219 title 修复 P0
- **结构性发现**：① dk 缺 Critique 节跨批复发 → 黄药师任务书 R1；② 修复回归 E009 → R3 重名检测；③ source_refs 断链镜像问题 → review-infra R4 存在性校验（P1）；④ **Phase 0 漏 title 非空检查**（#219 搜索诊断）→ 审查 SOP 已补；⑤ **E010 批量追加块破坏 YAML**（#222+#223 双线并行写入事故，~2350 张破坏，#227 修复至 98.1%）
- **当前状态**（2026-08-04）：#213-#229 事故全链路闭环——全库活跃卡 YAML 100% 通过、索引 3762 docs、8 类 lint 门禁上线。遗留长尾：#224 收尾（concepts 18 英文 title + 26 缺 disc）；黄药师 7 卡 FAIL 待修复复审（1 重复卡 + 结构缺口）
- **待命**：① 黄药师 7 卡修复复审 ② #224 长尾收尾 ③ 新批次终审

### 当前状态（2026-08-09）—— Feature 域全链收官 + 双驱动机制固化

- **#248-#266 全部终审闭环**（看板清空，队列零残留）：Feature 域（周期表 100/100 + W0-W4 全链）→ Agent 基建（#260-266）→ 双驱动机制（#265）
- **周期表 JSON**：100 Feature、verified 25/100（#252 试点回填 5）、`missing`/`gap_note`/`verify_note` 字段齐——消费端菜单（kdo feature 四命令 + --seed）
- **消费端协议 v0.1**：点菜→调优→沉淀三步 + 三原则（不挑食/无效也是结果/一任务一回填）；条件项：verified 语义声明、info 命令显示 verify_note（v0.2）
- **E018 铁律**：四提四证后注入 6 Agent SOUL.md（author 属实/审查真实/自建默认 draft 送审）——**审查时"status=reviewed 无终审记录"是独立检查项**
- **#265 双驱动机制**：四回路（知识/数据/流程/模式）+ 四通道（corrections/迭代日志/消费端回填/王语嫣每周一编排扫描）
- **新域登记四处规则**：路由 + 卡 + 映射表 + index.md（#219 教训固化）
- **队列**：全部 closed（#241 master MOC 已流转）；黄药师侧 #258 工具侧清扫完成
- **遗留条件跟踪**：飞书端抽查（#261 条件①）、段王爷卡条件已清、协议 v0.2 候选（info verify_note）
- **技能进化最新**：验证口径先声明（O-11 三证）、E018 合规为默认检查、数字写死→清扫任务、"完成汇报"必须能复现
- **审查方法论 v2.2**（2026-08-09 全网调研落地）：校准黄金集 15 条（`20_memory/ouyangfeng-calibration-goldset.md`，月度抽测一致率<80% 触发复盘）+ FAIL 结构化四节协议（P0/P1/P2+定位+证据+期望形态，禁"不合格"退回语）+ 不报告清单（格式归 lint、非本批记 TODO）+ 复审 ≤3 轮超限升级用户。详见方法论卡 §v2.2 与 context §审查者校准。

---


### 当前状态（2026-08-21 晚 · 重启前快照）——队列 385/385 全清

- **#380-406 全闭环（30 单终审，全部 PASS A/A-）**：#380 偶遇管线复审 / #381 元技能分层 / #382 trust 过滤 / #379 kinda 卡组 / #383-386 回链与清理（#384 三轮退回闭环）/ #387 柠檬市场（新质量门首链）/ #388-396 元数据与调研包 / #393 标签体系（退回→复审 A-）/ #395-398 源头与链接 / #399 全库复扫工具 / #400-406 建议书落地与反向回链
- **队列 385/385 全部完成（待领取 0/审查中 0/进行中 0）**——老顽童/黄药师名下任务全部交卷，待编排派发下一批
- **方法论最新（v2.3.1+ 候选）**：① #362 版本对齐三问（入仓/生效/对齐）② **归零声明须附 #399 full-library-rescan 工具输出**（机制化，治口径事故）③ 声明精确性三连问（怎么数的/跳过什么/解析失败吗）④ 事故修复验收=全量复扫+特征归零 ⑤ 修复前先查真相源（codex relay 教训）⑥ 样本校准先行（批量验证先看 1 张真实格式）
- **流程里程碑**：产卡批次默认含反向回链不再留尾巴（#406 常设规则）；REVIEW-PENDING 段=欧阳锋开工唯一入口（段内有行按提审序审，不跳单）；流转自动 git 收口（#390 E040 机制化）
- **codex 修复状态**：relay 由 schtasks Codex-Relay 开机自启（进程独立）；正确架构=codex-relay:4444→DeepSeek；kimi-proxy.py 劣化陷阱勿用
- **库级观察**：parse-error 61 张（YAML 损坏，yihang 卡等，修复单独立项不伪装归零）；related-asymmetry 7415 存量分批；30_wiki 工作区已收净
- **相关**：技能进化日志最新 08-21 正式行；daily-context 最新 2026-08-21（含多场追加）

### 当前状态（2026-08-21）——#393/#395 闭环 + 声明精确性铁律

- **#395 补审 PASS A**（updated_at 源头收口：模板+归一化双侧关闭；pre-submit 已是 ERROR 的根因判断准确）——**漏审教训**：REVIEW-PENDING 段内按提审序审不跳单（#395 被跳用户提醒）
- **#393 复审 PASS A-**（标签体系 W1 退回闭环：47 张补齐 063eff4e7 + 词表 <5 处置；🔴 解析盲区第三次——yihang 卡 yaml ParserError 被扫描器跳过，"归零"是解析器口径；yihang YAML 修复另立项）
- **声明精确性三连问**（铁律）：归零/全覆盖声明必问 ① 怎么数的 ② 跳过什么 ③ 解析失败的文件呢——#391/#393 三次同族教训固化
- **队列**：审查中 0；#393 W2+（tags 分批回填）等词表定稿后立项
- **相关**：技能进化日志最新 08-21 正式行；daily-context 最新 2026-08-21（A 级）

### 当前状态（2026-08-20）——审查 7 单 + codex 修复 + 三问 3 退 3 闭环

- **#380 复审 PASS A**（双仓入仓纪律：KDO 仓未提交退回→commit 71c2c2e→code_files 补跨仓路径→复审闭环）+ **#381 元技能分层 PASS A** + **#382 trust 过滤 PASS A**（#380 留裁决项落地，O3 消费端实测）+ **#379 kinda 卡组 PASS A** + **#383 回链 PASS A-** + **#384 回链扫描退回 queued**（🔴 body 污染修复不彻底 2 卡 3 行——"0 ERROR≠无污染"，待老顽童全量复扫后复审）
- **codex 故障修复（外部工具链）**：正确架构=codex-relay:4444→DeepSeek（黄药师配，start-relay.bat 守护，启动文件夹 lnk）；故障=relay 03:16 停止后守护随窗口死；修复=relay 拉起 + **schtasks Codex-Relay 开机自启（进程独立）**；教训=修复前先查真相源，kimi-proxy.py 是劣化陷阱
- **方法论新增**：修复前真相源优先 / 事故修复验收=全量复扫+特征归零 / 0 ERROR≠无污染 / 跨仓 code_files 门禁盲区（声明必须含跨仓路径）
- **库级观察**：30_wiki 工作区 ~160 文件累积脏（#376 遗留 frontmatter 同步 + CRLF + 历史）待批量收净
- **相关**：技能进化日志最新 08-20 正式行；daily-context 最新 2026-08-20（正式 10 章 A 级）

### 当前状态（2026-08-18）——迁移链四单终审 + 部署类验收三态框架成型

- **迁移链四单全闭环**：#347 洪七公迁 Windows **PASS A**（运行态 pid 存活+feishu connected、WSL disabled+inactive、skills 244、E030 全加载、openmontage 降级已配）→ #348 R 型 Partner 部署 **PASS A**（三件套字节核对、NSSM RUNNING、MCP 8+8 tools、真机冒烟日志吻合、引用卡 5/5）→ #350 kdo MCP UTF-8 修复 **PASS A-**（中文检索 5 例独立复现、编译过）→ #351 段王爷检索启用 **PASS A-**（消费层 738s→8.6s 86 倍、sync 幂等 14 SAME、无乱码+卡名真实）→ **#337 KDO 照镜子审计 PASS（条件）A-**（主交付+§8 静态复审质量高 O3 全过；🔴 条件项：小昭文档 §6 实测节 8 个新发现未被 codex 覆盖，我独立复现 title 残片/graph 退化 2 项成立——codex 需补 §6.2 打标表）——**✅ 条件项已关闭（08-18 晚）**：codex §8.6 v0.4 修正版（8 条打标全承接：cff06958d #357 + 00d44dc #358 queued），行号抽查全吻合，我侧 append 复审记录
- **部署类验收三态框架成型**：运行态（进程/服务/状态文件）→ 字节级（config 原文/代码/编译）→ 消费层（真机/检索/幂等）——四单每单逮一个报告不实/不精确（243vs244 口径 / openmontage stdout / beikai 未收口 / review_date 偏一天）
- **🟡 移交黄药师**：① sync WINDOWS_PROFILES 补 beikai（AppData 侧收口）② openmontage stdout reconfigure 澄清（并入 beikai 重启批次验证）
- **queue_transition.py 可用**：context blocker"被 auto mode 拦截"已过期，实测 4 次全通（含 --grade）
- **队列**：六单全 reviewed（#347/#348/#350/#351/#337），dashboard 326，**pending_review=0 全清**；#352-356 黄药师 queued（MCP 文档债/协议/性能/冷加载）
- **验证方法教训 ×2**：hermes skills list 必须带 `-p <profile>`（不带跑 146 差点误判）；bash 变量拼 Windows 路径混读错文件——验证命令先确认作用域
- **#357 kdo MCP 检索质量 5 项根因修复 PASS A-（08-18 晚）**：小昭 6 项报告 5 项已被 22:39 修复（她审 20:18 旧登记副本——**版本分裂** kdo-tools/mcp/tools.py vs 40_outputs/code/scripts/tools.py）；O3 消费端全链实测 engine 复活 hybrid RRF/title 真实/label 三档；queue_transition review 需传全名（O-3）；残留 graph-only label 全 low 记 #358
- **验证环境盲区教训**：复现类验证先对齐运行上下文（running loop/线程）——独立进程跑通 ≠ MCP 运行环境跑通（差点误推翻小昭正确结论）
- **相关**：技能进化日志最新 08-18（第三场）；daily-context 最新 2026-08-18（第三场）

### 当前状态（2026-08-17）——R 型首战闭环 + 迁移全量 Windows 决策

- **R 型 Partner 首战闭环**：spec（#335）→ 上岗 → 视频号课题五状态机 3 轮饱和 → 资产报告（O0 抽查零编造）→ #349 转卡 PASS A-（tool-wechat-transcript-automation-workflow 入库）——调研系列 agent 矩阵首次完整闭环
- **迁移新决策（用户拍板）**：洪七公启动失败 + 全量迁 Windows（推翻"beikai 留 WSL"裁定），codex 操作中，我事后验收（建议书已更新）
- **Hermes 三实例结构澄清**：WSL /home/.hermes（飞书 gateway）+ Windows .hermes（新助理 gateway）+ AppData（CLI）——双实例是设计；#325/#326 挂载成果完好；遗留 beikai/duanwangye AppData=0 待确认
- **停车场新增 O-15/O-16**：kdo MCP 冷加载 10.5s/次 + 300s 超时复发（R 型实战撞出）——P1 排黄药师
- **待办**：#347/#348 终审；#342-346 迁移执行验收；O-12 部署全景图前置产出
- **纪律状态**：任务单定位 cells[7] 破 3 次已升级为"终审动作序列第 0 步"；报告情绪隔离新纪律
- **相关**：技能进化日志最新 08-17；daily-context 最新 2026-08-17（完整版含差异栏）

### 当前状态（2026-08-16）——知识传导系统性工程收官 + 观察者接入

- **系统性工程四环全闭环**：诊断（#324 ✅）→ 存量补齐（#325 ✅）→ 机制制度化（#326 ✅）→ 快照迁移试点（#327 ✅）——知识库→Agent 传导进入自维持轨道
- **本日终审 ×8**：#319-330 全部 PASS（A 或 A-）：GBK 修复/检索层/机制化/崩溃循环修复/digest/文档修正/销售卡组 7 卡/快照试点
- **崩溃循环根因闭环**：system/user 双 systemd + boot 脚本 pkill 三套机制抢锁（观察者 Codex 发现双级）→ 方案 B 全归 user 级 → NRestarts 归零 + 飞书 3/3
- **KDO 源码 bug 修复落库**：delivery.py 跨平台（#326 狗粮）+ search_index.py --rebuild 全重建（#327）——2 commit（7fa95c0/8bc5645）已 HEAD 验证
- **观察者角色接入**：Codex 观察各 agent 运转，报告落点/频率待用户补充；首份观察样本=崩溃循环修复前后对比
- **队列**：pending_review=0 全清；queued=#331（王语嫣 P3 推广）+ #332（老顽童爆仗时代）
- **审查方法论 v2.3 新增纪律**：运行态双查（system/user）、命令语义验证（真实场景）、"归零"声明 grep、部署验收查 WorkingDirectory、迁移裁定先 hash diff
- **相关**：技能进化日志最新 08-16；daily-context 最新 2026-08-16（完整版含差异栏）

### 当前状态（2026-08-15）——恢复会话：状态校准 + 记忆补充

- **恢复流程实证**：按指引读四源（ouyangfeng-context v2.3 / context.md / amnesia-recovery / daily-context 最新）→ 发现指引写死 08-09 已过期（实际最新 08-13）→ 恢复以"目录内最新"为准
- **队列全链状态**（context.md active_task 2026-08-15）：Live258 三连批（#312 case 4 张 A- / #313 dk 2+1 B+ / #314 tool 1 张 A-）全闭环，看板 297/297 全清，队列 queued=0/pending_review=0
- **遗留待办**：① **#304 真审**（科学开会助理部署，黄药师交付备注"提审待欧阳锋终审"）；② **#298 待与王语嫣确认**（我侧 08-10 E019 已对齐 + 队列 reviewed，但 context.md 标"欧阳锋审"——疑似王语嫣未同步 08-10 结论）；③ 停车场 O-12/O-13/P-31 待用户拍板
- **技能进化日志**：08-13 行缺失 4 天后补记（复盘资产声明未落盘——O3 对己新纪律）
- **审查方法论**：v2.3（复审对照法/E019 分流/模型实测/验证纪律三则/操作纪律四则/第 2 次实证升铁律/E018 默认检查）
- **相关**：技能进化日志最新 08-15；daily-context 最新 2026-08-15

### 当前状态（2026-08-11）——审查方法论 v2.3 落地

- **审查方法论 v2.3**（2026-08-11 自我迭代）：复审对照法（FAIL 清单逐项 grep）+ E019 孤儿分流（先查卡片侧再分流）+ 模型实测优先（推断标置信度）+ 验证纪律三则 + 操作纪律四则 + 同模式第 2 次实证升铁律 + E018 合规默认检查。方法论卡 version=v2.3，context review_methodology=v2.3
- **失忆恢复双源**：`agent复盘/欧阳锋/`（中文：技能进化日志/错误模式库 E001-E013/每日复盘）+ `agent复盘/ouyangfeng/`（英文：Truman daily-context）都要读——第一版恢复只读英文目录导致记忆不准确
- 段王爷 08-11 周一巡检（cron）：E008/E009 新增，Memory 81%，发布域"先选渠道再格式化"认知
- 全厂其他角色：黄药师 MCP 双 server 3 agent 接入 + 任务模式真机 PASS；老顽童科学开会 16 卡 + 教练域 21 卡；王语嫣 E021-E028 铁律体系 + 看板全清 290/290

### 当前状态（2026-08-10）——飞书产品上线 + 任务模式真机验证 PASS

- **#306-311 WorkBuddy 借鉴链全闭环**：飞书文档 MCP（操作型，A-）→ 交付物模板 6 个（A）→ 任务模式 spec（A-）→ SOUL 实现（A-）→ 检索接入（A，3 agent 全覆盖）→ Auto 模型（裁定降级文档）
- **飞书教练式领导力助理上线**（#303 部署 A- + C1 冒烟 PASS）：老朱拆书任务 2000 字读后感真机交付——**素材精做传导铁律终极验证**（口述稿→16 卡 A→spec→SOUL→飞书，O0 抽查零编造）
- **E019 孤儿收口**：8 个孤儿 4 真审（#289 B+/#291 A-/#293 A/#294 A/#217 A）+ 4 对齐（#295/#296/#230/#298）——先诊断卡片侧再分流
- **看板全清 290/290** + 看板等级标注上线（generate-dashboard.py：已完成组渲染+等级徽章 A/A-/B+，条件 ⚠）
- **用户实测修正模型判断**：flash 强于 pro 预览版（推翻 #277 倒挂推断）——role-model-routing.md 修正节已落盘；识图用 kdo minimax API
- **停车场 O-12/O-13**：Hermes WSL→Windows 迁移专项（调研已做，决策待用户）+ .wslconfig 扩容（4GB→8GB 待拍板）
- **今日终审 52 单全闭环**，零 FAIL

## 5. 我现在的待命能力

用户可以直接派：

1. 终审 framework/concept/case/tool/dk 卡（唯一终审权）
2. 复核王语嫣的诊断报告与任务单
3. 裁定跨角色边界争议
4. 执行 `queue_transition.py review` 改变任务状态
5. 写系统治理复盘与流程改进建议

---

## 6. 审查存放规则

- **终审结论**：必须落在 `production-queue.md` + 任务单 frontmatter + dashboard
- **审查意见中的指令**：必须当场写入任务文件，口头指令不算
- **退回记录**：在 daily-context 中记录退回原因
- **O0 违规**：如果某天审查结论是在未溯源情况下做出的，必须在 daily-context 第 5 节如实记录

### 终审收尾四同步 + 索引刷新（2026-08-03 教训固化；2026-08-05 E012 升级）

**每次终审 PASS 后，必须完成 4 处状态同步 + 1 次索引刷新，缺一不叫"审完"——PASS 判定后立即执行，不等生产者（E012：三批 19 张卡漏同步的教训）：**

1. **任务单 frontmatter**：`status: reviewed` / `reviewed_by: 欧阳锋` / `review_date: YYYY-MM-DD`（用 `queue_transition.py review` 或 `review_mark.py`，脚本不可用时手动 patch + `<!-- 手动终审：原因 -->` 注释）
2. **production-queue.md 状态列**：`reviewed`
3. **dashboard.md**：终审记录
4. **卡片自身 frontmatter**：`status: reviewed` / `reviewed_by: 欧阳锋` / `review_date`——**用 `review_mark.py`（#218 R1）批量写，或手动批量**；**不得依赖生产者补**（#230/#231/#232 三批 PASS 后卡片仍 draft 的教训）
5. **跑 `kdo index` 刷新搜索索引**（**#219 教训**——索引过期 5 天导致小昭搜"创新者的窘境"0 结果）
6. **PASS 后 grep 确认**：`grep "status: reviewed"` 覆盖本批全部卡，再宣布"审完"

> 工具：`review_mark.py`（#218 R1）已上线——终审通过后 `python 90_control/scripts/review_mark.py <卡路径> --reviewer 欧阳锋` 批量同步。
> 停车场 O-9：索引自动刷新机制待黄药师排期，上线前靠终审 SOP 手动 `kdo index` 兜底。

---

## 7. 关联文件

- `.agent/ouyangfeng-context.md` — 角色上下文（活注册表）
- `.agent/context.md` — 共享状态
- `.agent/toolkit.md` — 本地武器库
- `.agent/pitfalls.md` — 踩坑记录
- `70_product/tasks/production-queue.md` — 生产队列
- `70_product/tasks/dashboard.md` — 任务仪表盘
- `framework-ouyangfeng-review-methodology` — 审查方法论卡

### 当前状态（2026-08-22 · 超长会话收官）——#411 30 批收官 + 治理批 + 会诊表态

- **#411 整单收官 PASS A**：30 批 7325 条回填（7472→457 可处理归零，剩余=455 pending_unknown 纪律排除+2 already）——图谱连通性工程收官；批次验收流程（禁 queue_transition review/划段行/恢复 queued）经 30 批实战固化，#426 tags 批引用该模式
- **今日终审 20+ 单**：#407 PDF-Inspector A- / #408 空壳卡 A- / #409 parse-error A（FAIL→复审，index 生成物跨仓根治 f7a78a0）/ #410 mojibake A / #412 W3 口径 A / #413 O-3 修复 A-（段登记幂等 bug 实证——非 complete 锁内 re-check，R4 行号偏移 TODO）/ #414 副本清理 A（FAIL→复审）/ #415 工具名清单 A / #416 基本法框架稿 A / #418 复盘治理 A（幻影丢失裁定）/ #419 复盘门禁 A（六角色触发话术）/ #420 停车场收口 A / #425 健康指标 A
- **会诊表态**：positions/ouyangfeng.md 落盘（B2-1 分界/B2-3 补批次验收语义/B3-4 同族词/X-1 两类信号）；建议书 proposal-batch-todo-closure-gate（R1-R4 王语嫣全承接，R1 先行落地）
- **运维**：codex-relay 502 修复（自启任务丢失重建）+ agent-fix-records 目录（README 规范）
- **审查方法升级**：diff 删除行先查文件归属（第十五批误判教训）；异常驱动审查（规范批快过/异常批深挖）；批次验收动作清单（终审记录+划段行+恢复 queued）
- **队列**：待领取 7（#417/#421-424/#426-428）+ #188 历史遗留 pending_review；审查中 0
- **🔴 O9 纪律（2026-08-22 深夜新增）**：终审先落意见书再跑脚本——任务单末尾「终审记录」节（等级+通过维度+溯源要点+缺陷+残余风险）为必交付物，PASS/FAIL 都写；脚本划线 ≠ 终审完成（#421 教训：判断留在会话=交接断链）。终审三处同步→四处同步（意见书为第一处）。已在 ouyangfeng-context.md 固化

### 当前状态（2026-08-24 · 超长会话复盘：08-22 深夜 → 08-24 凌晨）

- **62+ 单终审闭环（#421-#494）**：8 单 FAIL→复审全闭环；16 份建议书（13 条落地成工具/任务：doc_id/commit bug/来源词/aliases/批次工具化/阻塞豁免等）
- **#426 批次 14 批 780 张**：决策 44/ai-collaboration 200 收官/yitang 收官/design 剩 26——批次验收全走 queue_batch_accept 工具（自动 commit 7 次）
- **方法论 v2.4 候选**：出口清单（只建议书/通过/打回——老朱 08-23 确认边界）+ O9 意见书先写（F-035 门禁化）+ 双假设原则（怀疑读取）+ 断言纪律（subn=1）+ 批次优先纪律——全部在 ouyangfeng-context.md
- **门禁体系**：#433 负向判词/#435 词表/#442 否定式/#444 force 台账/#457 处置/#460 机器自报/#462 流转信号/#450/#484/#494 检查器
- **队列**：REVIEW-PENDING 段内全清；待领取若干；自动领审 cron 运行中（每 23 分钟，7 天过期需续）
- **待清理存量**：aliases 污染 1555 张（#494 清单）+ 来源词 19 张（#484）+ #426 剩 design 26/strategy/master/kdo/unknown 139
- **恢复**：读 ouyangfeng-context + context + amnesia-recovery（本节）+ daily-context 最新（2026-08-24）

### 当前状态（2026-08-25 · #426 整单收官 + #487 FAIL 打回）

- **#426 整单终审 PASS A-（闭环）**：26 批 + 收官批次累计 ~1,500 张 tags 治理；归零声明双口径独立复扫实证（full-library-rescan missing-tags-dim 剩余 0 / tags-audit 空值率 0.0%）——报告未附工具输出由审查侧补跑。🟡 收官报告"6 张治理" vs commit 实证 3 文件（残留清单为过期快照，framework-candy/tool-ai-research 本非空缺；2 张为删词未说明）；tool-ai-scene 删词后内容词仅"方法"（关联在途词量口径建议书）
- **#487 口喷卡组 FAIL 打回**（Live260 卡组 2 迭代+5 新增）：P0×2——① framework-cultivation-map 段位映射错位+发明"L5 流淌→局部"段位（源文五次飞跃 heading L127/181/229/255/297 对读实证，L253/L257 段位归属铁证）② dk-newcomer-blockers 缺 Critique 节（#217 门禁同族复发）；P1×3——related 未链已有口喷卡（ten-year-map/月白/九字诀/口喷次数，spec L2 验收项）/ concept-parallel 段位引用同族错位 / 1b 迭代卡"口喷双三角"释义错误（≠心法）。已验证达标：锚点 L97-327 逐段实证 ✅、append-only ✅、诚实降级 ✅——待老顽童返工复审（对照法）
- **队列**：REVIEW-PENDING 段全清（0 待审）；#487 退回 queued；#470/#498 FAIL 返工中
- **方法论新增**：过期清单陷阱（收官报告"残留 N 张"先逐卡实证当前状态再采信）；框架卡溯源=heading 结构对读法（源文章节标题 vs 卡结构逐行对）
- **恢复**：读 ouyangfeng-context + context + amnesia-recovery（本节）+ daily-context 最新（2026-08-25）

### 当前状态（2026-08-25 第二场 · #503 PASS A）

- **#503 claim 口径族根治 PASS A**：版本对齐三问全过 + pytest 104 独立复跑一致 + diff 与任务书 6 项逐条对上 + 存量复扫重跑 11 条逐条定性一致（10 豁免+1 观察）+ 状态机链路核实（transition 表 L244→find_blockers L121→_same_executor 双维度）。🔵 观察项：kimi 共用实例下同实例维度跨角色保守多拦（可见报错非静默漏拦，不阻断）
- **方法论新增**：代码类终审全链实证模板（三问 + diff 逐条对 + 测试复跑 + 存量扫描重跑 + 状态机链路三段核实）
- **队列**：REVIEW-PENDING 全清（0 待审）；#487/#470/#498 三单 FAIL 返工中；#504（洞B/C）待领取
- **#470 复审 PASS A-（闭环）**：对照法逐项 grep——4 卡 source_context 完整值 4/4 一字不差 + yaml.safe_load 独立实测（块标量消除，上轮残余风险闭环）；🟡 返工未 commit 提审（三问豁免覆盖纯 frontmatter 任务，O2 落笔指令：老顽童当日补 feat commit，验证=git log）
- **#504 审查等待期占位 PASS A**：锁三洞全闭环（洞A→#503/洞B/C→#504）；pytest 109 复跑一致；force 留痕机制（bypass 参数化+无阻塞不留痕 2 例钉死）；报告诚实性正面样本（如实声明洞C补齐的是语义与提示，未夸大行为变更）
- **O2 指令闭环实证**：#470 落笔指令 20 分钟内闭环（19a59e778 收 4 卡）
- **#487 复审 PASS A（第 2 轮闭环）**：对照法 7 项全修——段位表按源文重排+发明段位删除+dk Critique 实质双面+related 补链零死链；返工质量超清单（锚点来源说明机制）；卡片 reviewed 标记 7/7 已收尾。FAIL 返工在途清零（#470/#487 均闭环，#498 待返工）
- **#505 并发写根治 PASS A + 增补件批准生效**：三问全过+pytest 116+21 复跑一致+guard 工具我侧 FRESH 复现+锁名两侧一致；approved_by 落笔欧阳锋，S2 三条约定生效（我自己 commit 已先行遵守 path-scoped+by 署名）
- **审查卡点建议书已落**：diag_20260825_ouyangfeng-review-bottleneck-wakeup（R1 提审叫醒通道/R2 阻塞链标记/R3 pending_review 年龄 SLA/R4 应急 force）——老朱"反思卡点"指令闭环，待王语嫣裁定
- **#498 复审 PASS A-（第 2 轮闭环）**：graph-rag tags 4→7 词（检索增强补回）+"词不足"申辩撤回——**08-24 晚 3 FAIL + #487 全部复审闭环，FAIL 在途清零**；观察项：graph-rag 正文 11 处 src_unknown 存量记 TODO（非本单范围）
- **#518 复审 PASS A（清单批闭环）**：对照法 3 项全修（561 脚本重跑交集=0/预览 5 路径全存在/交付物入仓）；口径裁定：混合 refs 卡入类1 合理不重出；🔵 编排接缝已标注——后续治理批次归属待王语嫣裁定（#517 门禁后放行首批）
- **#507 每日审计 digest PASS A-**：部署三态全验+dry-run 零副作用实证（队列 diff 引擎当场检出 #518 FAIL 流转）；P2 指令在案：游标回拨 regenerate 今日 digest（狗粮覆盖语义毁首跑成果，否则风清扬明早无料）
- **#518 清单批 FAIL**（我的 src_unknown 建议书落地单）：类1 判定漏洞 561 卡误分（source_refs 全占位未过滤；真实类1≈346/类2≈1205）+ 预览列标题/lens 冒充来源；达标项（总数复跑一致/零写入/类3不硬凑）已列。待返工复审（对照法：561 检查脚本重跑应归零）
- **complete 入仓门禁建议书**：diag_20260825_ouyangfeng-complete-deliverable-commit-gate（未 commit 提审一晚 2 次→铁律升级）
- **审查推送链建议书**（08-25，老朱指令）：diag_20260825_ouyangfeng-review-result-push-gap——R1 PASS 路由生产者（真缺口）/R2 静默分级（✅老朱已拍板豁免终审类）/R3 inbox 必读纪律；#498 误报事件=王语嫣未读 inbox（机制正常，E034 同族）
- **#506 建议书 near-miss 门禁 PASS A-**：四形态拦截函数直读+双套件 84+116 复跑一致；🟡 口径收窄未声明（实现比任务书 L1 窄，合理但未报备）；🔴 自体中招实证——我当日 2 份建议书非合规格式零登记零报警，已自纠补三元组（契约单轨：type:proposal+status:pending_orchestration+audience:王语嫣——**我以后写建议书必须按此 frontmatter**）
- **src_unknown 门禁盲区建议书**（08-25，老朱追问触发）：diag_20260825_ouyangfeng-src-unknown-body-gate——正文 src_unknown 22,871 行/1,524 卡存量 + pre-submit 放行实证；观察项分类补丁：入库前先测存量（单卡问题 vs 一类卡问题）
- **自动审查 cron 已建**（08-25，老朱拍板 15 分钟）：id 01M0TBXX97V5NMM22A2QRTZ4GN，会话级——仅本会话存活+空闲时触发，会话关闭时段靠机器层 R1（建议书在途）；每次触发耗 token（1 分钟方案已否）
- **注意**：王语嫣 08-25 命名铁律已生效（cc9b928db）——instance 标记只用角色名禁工具名后缀，后续审查按新口径

### 当前状态（2026-08-24 晚间 · 批次收官 + 3 FAIL 复盘）

- **#426 批次 25 批 1266 张**：有轴域 14 轴全部收官（strategy/master/kdo/ai-collab/design/content/decision/research/小域）；剩余仅无轴小域（#500 已治理 65 张 + 收官信号待确认）
- **本场整单 9 单**：#497 PASS A-（紫鲸调研）/ #499 复审 PASS A-（返工闭环）/ #496 PASS A-（source_refs 门禁）/ #500 PASS A- / #501 PASS A-（待办收件箱）/ #502 PASS A-（L10 冻结）/ #495 PASS A-（369 张补字段）/ **#470 FAIL（source_context 未落地）/** **#498 FAIL（graph-rag 未回补词不足借口不实）**——2 单 FAIL 待返工复审
- **🔴🔴 出口自检钩子（08-24 晚固化，第 9 次点破）**："建议"二字出现在审查记录 = 必须当天有建议书文件——**无豁免条款**（不许"样本小/非阻塞"自我豁免）——dk 词量观察项钩子第一轮即破的教训
- **声称-交付一致性成验收标配**：3 FAIL 同族（#499 空缺漏清单/#470 声称完整值未落地/#498 借口不实）——验收动作=报告/commit 声称 vs 文件系统实际并排比对
- **#433 门禁自拦实证**：审查者自己写 FAIL 意见书缺存在性核查锚点被 queue_transition 拦截——补节重跑
- **截断变体第 7 次**：多行 YAML 数组格式（domain:\n- kdo）误判"清域"——复扫前先看格式再写正则
- **观察项待办**：37 张双三角卡漏清单（#495 差集 160-147）待王语嫣补列；framework-一堂-关键假设（发起实证卡）未闭环；todos 只增不清
- **建议书闭环 3 单**：source-refs-null-gate（#495/#496）/ dk-card-tags-word-count（#498 FAIL 返工中）/ 499-rework-pending（情况报告）
- **恢复**：读 ouyangfeng-context（含出口钩子）+ context + amnesia-recovery（本节）+ daily-context 最新（2026-08-24-claude.md）

## 2026-08-25 第十五场：#508 L1 日期归档终审 PASS A

- **结论**：PASS A。版本对齐（冻结版=01:59 commit 4f6a181f9=提审时刻）；O0 逐行溯源 l1_capture.py 358 行；pytest 84 passed 独立复跑一致；生产态实测：热层仅 2026-08-25/、2026-08-24.zip 11608 文件 testzip 我亲自重跑 OK、游标 11589 条、kdo-l1-archive 计划任务 06:00 已启用
- **事故披露核验**：474 删除→473 恢复+1 真丢失（hermes/wangyuyan/.skills_prompt_snapshot.json）。负向断言"丢失"触发 #433 门禁——补存在性核查节，四路实测（源目录/三个 zip/热层 find）全确认丢失属实
- **观察项 5 条**→建议书 `60_feedback/diagnosis/diag_20260825_ouyangfeng-l1-archive-hardening.md`（R1 CRC 抽检/R2 拒删接 gate-blocked/R3 事故上浮全厂 friction 台账，三元组契约已遵守）
- **门禁教训**：终审记录含"丢失/未见/无"类负向词须附 `**存在性核查**` 锚点节，否则 queue_transition 拦截——先核查再落笔可省一轮返工

## 2026-08-25 第十六场：#510 CAPSULE_STARTUP 风清扬路由终审 PASS A

- **结论**：PASS A。文档小单，冻结版=提审时刻 commit 3794596cf；§2 路由行/§3 身份卡逐字对原文全一致；覆盖自检独立复数（hermes profiles 11 个亲数、agents/ 角色目录 10 个）；恢复路径可达（锚点+daily-context 2026-08-24.md）
- **附带发现属实**：huangyaoshi hermes profile 实锤存在（profiles 列表第 5 位）——#509 前置条件过时，来历澄清已路由王语嫣/老朱
- **观察项仅记录**：§0 git_head 静态字段提交后必漂移，文件已自注明惯例+校验容忍，设计内行为

## 2026-08-25 第十七场：#509 飞书黄药师实例终审 PASS A

- **结论**：PASS A。核查类闭环（实例老朱 08-24 自建/codex 协助，非黄药师施工）——口径转折合规：与 #510 附带发现互验时间线自洽（profile 09:35 建 ↔ 老朱供 app_id）
- **逐项亲测**：三件套/config 三挂载/deepseek-v4-pro/服务 RUNNING 17h 无重启（pid 09:36 未变+wal 02:16 活跃交叉证）/老朱 dm 频道在/SOUL 双实例纪律全要点
- **密钥纪律亲自 grep**：app_secret 全库 8 处全文字提及无值残留（#433 存在性核查节一次过——负向判词先附证再落笔，本场零返工）
- **未闭合**：L3 老朱外出飞书实测双向对话（如实披露+正确路由，不阻断）

## 2026-08-25 第十八场半：#511 胶囊事件层四类型终审 PASS A

- **结论**：PASS A。log_event_safe 统一入口+四写入点（queue_transition/decision/friction/error）逐 diff 对上；90+116 passed 独立复跑一致；事件库亲查：56 条，测试残留 0，#511 complete 狗粮事件 id=58 在库；终审即狗粮闭环——我的 review 触发 id=62/63（queue_transition+decision）双事件
- **疑点复核样本**：friction 行格式（日期开头）与 agent 正则（[角色]）看似失配→追到 _scan_friction 包装层 [role] 前缀自洽——起疑必追到底，不靠"测试过了"放过
- **小疵记录**：提审后补件 f52ad7a4f（测试隔离 mock）晚于提审 2 分钟——已在终审记录标注"宜先补件再提审"
- **capsule_test id=1** = #432 历史狗粮，非本单污染

## 2026-08-25 第二十场：#512 daily-context-save 覆盖写终审 PASS A-

- **结论**：PASS A-。剥层函数+事件去重签名逐行对上；94 passed 复跑一致；L2 亲验 laowantong hermes 单层 YAML；重灾区=我自己的 2026-08-17.md 97 层（声明"2-30 层"失真 3 倍→降级主因）；功能代码混入 vault backup 自动 commit（-S 定位可溯源但有噪音）
- **活体旁证**：我亲历存档 703→487 清洗=修复已在真实流水线生效
- **降级纪律**：修复正确≠声明全对——执行报告数字与实测不符要按失真程度反映到等级

## 2026-08-25 第二十一场：#513 kimi 断流核查终审 PASS A

- **结论**：PASS A。滞后型误判裁定成立——证据链五条全独立复跑：实时写盘（state.json 秒级滚动，我本人会话在列）、zip 内 workspaces.json=396B 与源 23:39 版字节相等（00:07 拍已采到）、无活动窗口、l1-size.log 82 拍连续、游标 1698 条逐字一致
- **口径裁定**：误报不罚——风清扬误报逼出三对照判读口径落档（inventory:155），下轮审计有依据；#498 误报事件同族
- **小疵**：声明"4 个活跃会话"实测目录 5 个（4 活跃+1 已结束），表述精度不降级

## 2026-08-25 第二十二场：#516 wechat_promote 去重补 _processed 终审 PASS A

- **结论**：PASS A。去重段（wechat_promote.py:110-116）逐字对上；98 passed 复跑一致；dry-run 亲跑双目标卡 skip、统计行逐字一致；唯一写入口 grep 负向核查一次过
- **教训**：复跑输出被 head -8 截断差点漏报第二张卡 skip——验证类输出看全量，不截断
- **机制意义**：E037 隔离写侧与管线读侧对账补齐——门禁判定不再被再生击穿（charter A8 写读对账的落地案例）

## 2026-08-25 第二十三场：#517 正文 src_unknown 门禁终审 PASS A

- **结论**：PASS A（我的建议书 R1 落地单）。跨仓版本对齐（KDO CLI 仓 bd67a37=提审时刻）；_check_body_src_unknown 逐行对上（只查正文/单词表/红线 4）；7 例复跑全过；L2 双分支亲跑（存量 WARNING ×22 逐字一致+新卡探针 error 实测拦截）
- **#433 第二次拦我**："缺失"类词描述代码行为也触发——负向词自查清单扩到 无/丢失/未见/不存在/缺失/已删，附证后一次过
- **意义**：新卡占位拦截时代开启（2026-08-25 起），#518 存量治理有门禁护栏

## 2026-08-25 第二十四场：#519 探针空转根治终审 PASS A + l1-capture 病灶接力

- **结论**：PASS A。根因=schtasks TR 嵌套引号剥壳（GBK emoji 假设证伪合理——stdout reconfigure 兜底在案）；.cmd 包装+check-conveyor-state 空转报警+121 passed 复跑一致；活体实证=state 7 分钟节拍内落盘+探针通知我审 #519（通知链自证闭环）
- **接力动作**：l1-capture 09:37 起被 Ctrl+C 杀（l1-size.log 停更 09:07 亲验=F-045 进行中破口）——队列无对应单，落建议书 `diag_20260825_ouyangfeng-l1-capture-console-killer.md`（R1 排查杀手/R2 空转报警泛化/R3 恢复后游标自动补采）
- **方法**：执行报告的"另立单建议"不依赖编排者捡——基建硬约束破口终审者当轮接力落书

## 2026-08-25 第二十五场：#520 审查供给端三件套终审 PASS A

- **结论**：PASS A（我的建议书 R1-R3 落地单）。三机制逐行对上：_split_silent_exempt（发送失败的豁免件回 pending 重试不丢=细节到位）、_mark_blocking_chains（语义逐字一致）、check-review-sla 直跑检出本单 0.1h；107+126 passed 复跑一致
- **有机活体**：R2 徽章打在 #520 自己卡片上（dashboard 恰 1 个 g-BLOCK）；R1 叫醒通道#519 时已活体自证（通知我审单）
- **观察项**：阻塞链判定按 assignee 同角色，跨角色依赖不标——够用不扩
- **待活体**：今晚 22:00 后夜间提审叫醒=豁免分支 L3
