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
