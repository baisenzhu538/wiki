---
session_id: huangyaoshi-2026-09-06
agent_id: huangyaoshi
date: 2026-09-06
created_at: 2026-09-06T04:18:19.481868+00:00
updated_at: 2026-09-06T04:18:19.481868+00:00
git_head: bb422fc00
content_hash: a83918cbd535
---

# huangyaoshi · 2026-09-06

# 黄药师 daily-context 2026-09-06（claude 通道场，kimi 403 额度死）

## 差异栏（第 1 章）

vs 09-05 场：上次是造新管线（#645），本次是**两单连做的小修+根因场**（#647 两小修 + #648 graph_index 停拍），且全程跑在 claude 通道（kimi 周额度 403 已死，09-03 异构先例）。最大的差异：本次两处「任务单上的根因初判都不准，施工中用实证推翻」——#647 的「seq 解析只扫 70_product/tasks/」实为 parse_queue 断表 break + seq 解析缺失双层；#648 的「计划任务没跑/跑了失败？」实为根本没有任务可失败（重建无自动载体）。复发模式：接到的初判都当线索不当结论，先跑证据再定根因——这条这次做对了。

## 概要

一句话：#647 两修（E040 gitignore 豁免分支 + seq 号寻址 + parse_queue 断表续扫，回归 6 条）与 #648 三修（graph_index 停拍三层根因 + 增量重建 14s 解 73.9h 陈旧 + 哨兵陈旧分支自愈）先后施工、双双提审 pending_review，全量回归 517 passed。

## 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| #647 根因修正后扩修 parse_queue 断表（超出任务单原文范围） | 任务单倾向补扫「消除坑」，但 seq 解析的前置是行可见——#430-444/#647/#648 共 12 行落第二段连完整 task_id 都寻不到；只修 seq 解析不修断表=假修 | 229→241 行无重复，回归 6 条护栏 |
| E040 豁免判定用 `git check-ignore` 而非维护前缀清单 | 任务单说「取实现简单者」；check-ignore 一条子进程零维护跟真实规则，前缀清单每次改 .gitignore 都要同步 | 两仓通用，fail-open 维持硬拦 |
| claim 647/648 撞 #504 走 --force 台账 | 用户指令明确施工 + #646 挂审中；#504 有预设计 escape（force-exceptions.log 留痕） | 两单均留痕，无破窗 |
| #648 哨兵修复选「自动重建」而非「升级报警」 | 真机实测增量重建 14s/24 页——成本可忽略；升级报警已被证明会划销五拍无人动 | 自愈+失败升级双路，6h 防乒乓 |
| 自愈成功判据用 graphml mtime 前跳而非 rc=0 | 真机第一轮模拟抓到「No changes…」也 rc=0 的假成功（#175「不信脚本说它做了」同源） | 第二轮同场景正确判 FAIL 升级 |
| 模拟后如实盖章 mtime（utime 到 now）而非再跑 --full | 内容已同步（增量判 No changes），mtime 拨回是模拟假象；--full 是分钟级重操作 | lag -0.89h，扫描 [] 健康 |

## 思维盲点

1. **第一轮自愈模拟「成功」我就差点收工**——alerts=[] 看着很美，但 tail 日志才发现 `OK｜No changes since last rebuild`：rc=0 但什么都没修。为什么漏掉：把「命令成功」当「结果达成」，恰好是我自己报告里写过 #175 的教训。真机模拟的价值就在这种时刻——沙盒里桩掉的部分（真实 kdo 行为）才藏着第二层坑。
2. **看板显示 229 任务我最初以为是刷新延迟**——其实是 generate-dashboard 独立 parse_queue 副本没吃到断表修复（B3 同源病活的标本）。第一反应归因「延迟」而不是「另一个解析器」，差点漏掉这份建议书。
3. **#648 任务单问「哨兵为何没拦住」——预设了哨兵失灵**。查完发现哨兵完全按设计工作（逐拍告警+台账+推送），失灵的是「告警之后无行动出口」+「值守把逐拍重报误判回声」。问题预设会引导找错层——根因在链条下游不在哨兵本体。

## 顿悟

「幂等设计」在度量单调变化的场景下会自杀：graph_index 的 issue 串每小时 +1h（48h→49h→…），`issue != prev` 永远为真→每拍重报→长得像回声→被值守划销。防重复机制（去噪）和保真机制（不漏报）在缓变故障上互斥，解法不是调参而是让故障被自愈消灭在重报之前——修「物」优先于修「信号」。

## 过程资产

- 修改：`90_control/scripts/queue_transition.py`（_git_ignored + _resolve_task_ref）、`90_control/scripts/queue_gate.py`（断表续扫）、`kdo-tools/conveyor_probe.py`（_graph_index_selfheal + 陈旧分支自愈）
- 新增：`90_control/scripts/tests/test_seq_addressing_647.py`（4 条）、`logs/graph-selfheal.log`（自愈台账）、`60_feedback/diagnosis/diag_20260906_huangyaoshi-dashboard-parse-queue-copy.md`（最小建议书）
- 更新：`90_control/scripts/tests/test_complete_deliverable_gate.py`（+2 条）、`kdo-tools/tests/test_conveyor_probe.py`（+4 条改造 1 条）
- 数据：`.kdo/graph_index/` 增量重建（24 页/68 chunks/19 relations，lag 73.9h→-0.89h）
- commit：29821169f（#647 代码）、c0edfe65b（#648 哨兵）、#648 自愈台账 + 存在性核查节两笔
- 队列：#647/#648 双双 pending_review 待欧阳锋

## 元反思

本次最值钱的一步是「claim 647 失败时不急着用完整 task_id 绕过去」—— friction 本身就是需求规格，先复现、再诊断、把真根因（断表）和表层根因（seq 缺失）分开修，任务单原文的初判不准也没把施工带偏。下次接「XX 为什么不跑」类任务，第一问改成「这个机制到底存不存在」，先查存在性再查故障性——#648 的根因三层里最贵的一层（L1）就是用 schtasks 一条命令证伪了任务单的问题预设。

## Truman复盘

### 逐轮映射

| 轮次 | 人做什么 | 双三角要素 | AI做什么 | 双三角要素 |
|:---|:---|:---|:---|:---|
| 1 | 给任务令：claude 通道，claim #647 施工（E040 豁免+seq 寻址），完成后视 #646 终审状态决定 #648 | 方向+排序 | 启动恢复三读 → claim 647 双失败（seq/全 id 均不在队列）→ 不绕行，改诊断 | 执行校准 |
| 2 | （任务单预置两修范围） | 约束 | 诊断出断表真根因 → 三处修改（queue_gate/queue_transition ×2）→ #504 撞线 --force 留痕领取 | 侦察+建造 |
| 3 | — | — | 回归 6 条新增（含非豁免反例护栏）→ 全量 251 passed → commit → 五字段报告 → complete 647 | 验证+收口 |
| 4 | （指令预置依赖规则：#646 reviewed 才动 #648） | 决策点预授权 | 查证 #646 已 reviewed（终审恰在本场施工中落地）→ claim 648（seq 号直达） | 依赖判定 |
| 5 | — | — | 根因三层取证（schtasks/toolkit/时间戳对表）→ 增量重建 14s → 哨兵自愈落地 | 建造 |
| 6 | — | — | 真机模拟两轮抓假成功 → mtime 判据修正 → 517 passed → 提审 → 存在性核查节预防性补齐 → todos 落账 | 自纠+收口 |

### 飞轮效应

本轮吃到了 09-05 场留下的两份红利：#645 friction 记录直接变成 #647 任务单（friction→立项→修复全链 24h 内走通）；#622 的哨兵代码和测试夹具（_mk_graph_index）让 #648 哨兵改造从读到写只用几分钟。本轮又给下轮留了两份：seq 寻址让后续所有 claim/complete 都能报短号；自愈台账让 graph_index 从「手动节奏+每周事故」变成「自愈+升级」。

### 对照实验

- 无 AI：#647 两处门禁/解析器修改 + #648 三层根因取证 + 两套回归，人工估一天起步；本场 ~50 分钟交付两单
- 无人（无任务令排序）：#648 依赖 #646 终审，我会并行抢跑或干脆不动；预置的「查证后解锁」规则让依赖判定零犹豫
- 合在一起：人定优先级和依赖规则，AI 做「复现→诊断→修→验→留痕」全链——双方都在对方强区

### 下次改进

- Agent 自身：真机模拟后不要只看函数返回值，tail 日志对账（本次假成功藏在日志里不在返回值里）；接初判先跑存在性核查
- 方法论/机制候选：generate-dashboard 独立 parse_queue 副本（已落建议书 diag_20260906 待裁定）；幂等 vs 单调度量的互斥（graph_index 陈旧告警形态，若王语嫣裁定度量口径重设计可参考本条）

---

# 黄药师 daily-context 2026-09-06 续场（claude 通道场，02:54–04:05，#649+#650 两连单）

## 差异栏（第 1 章）

vs 同日早场（#647/#648）：早场是「门禁/解析器小修+根因取证」，本场是「采集链资源抢救+跨系统机制审计」。两点最大差异：①早场的教训「任务单初判不准」本场再现两次——#650 任务书说「09-02~03 hermes 通道四实例时代」，日志实证 09-02 全 37 条都是 kimi、hermes 只有 09-03 一个窗口；段王爷 diag 引的两条"hermes 成功日志"实为 kimi（首行 banner）。②早场在单仓内修门禁，本场跨了三个系统（vault 脚本/KDO CLI 仓/hermes 自身源码+state.db）——证据源升级到「消费端解析链源码+会话库账本」才把根因钉死。复发确认：初判当线索不当结论，这条已连续两场救场。

## 概要

一句话：#649 两修（wechat 转写动态 timeout+超时/失败留痕+3 败熔断；pre-submit ALIASES 取 basename+剥扩展名）施工+止血恢复+148MB 视频补转写（3214 段/实测 RTF 0.63）提审；#650（launcher hermes 改 -p flag+移除死 env 配置+历史影响面核查：09-03 有 11 个老顽童意图会话错载黄药师的 hermes profile，涉 #626/#629/#630/#632，KDO 层身份未串、记忆层无污染）施工+狗粮+阴性对照提审；两单均 pending_review 待欧阳锋。

## 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| #649 修法三选一取「timeout 挂媒体时长」而非异步任务化 | 用补转写实测 RTF 0.63 定系数（时长×1.0+300s）——异步化要引入任务队列/收割状态机，对单视频死循环是高射炮打蚊子；降 tiny 被 #634 质量裁定直接排除 | 动态 timeout=4205s（1.7x 余量），回归 6 条 |
| 补转写前先杀掉在途注定失败的 02:51 拍（父+子） | 该拍 03:06 必被 900s 超时杀；父进程一死管道断子进程也崩，无法救援；早杀省 7 分钟双 CPU 竞争 | 起止时间显式落执行报告（02:54:17 停拍/02:59:11 杀在途/03:43:51 恢复） |
| 转写失败留痕+同素材 3 败熔断 | 原设计「成功才 seen→失败无限重试」在长视频场景=无限烧；一次即弃又会放过瞬时故障 | transcribe_fails.txt 留 key+时间+原因尾段，3 败人工清账——熔断语义写进「需要谁动作」请裁定 |
| 修二取「只取 basename+剥扩展名」而非给 NOISE_DIRS 加目录名 | capabilities/shared 是打地鼠（每个新目录都要补清单）；basename+剥扩展名是消类别，且 #643 卡 alias 实存仍误报的根因就是 .md 没剥 | #643 场景复跑 ALIASES 0 issues；目录段素材名出比对范围的取舍用测试双向钉死 |
| 历史影响面弃日志抽样改 state.db sessions 全量 enumeration | 0 字节日志但 state.db 有 69 msgs 会话——日志是 stdout 渲染层（损失源），会话库才是账本层 | 17 条窗口会话全定性：11 错载+5 正确+1 探针；logs 只用来抽验自称 |
| 阴性对照补测（env-only 直跑一次） | 段王爷的结论是昨日证据，且其 diag 有一处引证已被证伪——机制类修复必须今日当场双测 | env-only 自称 huangyaoshi 当场复现，-p 正确路径狗粮 PASS，正反两面闭环 |

## 思维盲点

1. **日志通道分类第一版用内容关键词**——一条正文里提到"hermes 网关实测零误报"的 kimi 日志被误判成 hermes 通道。抓到自己后改成「只认首行 banner」（kimi version/Reading from stdin/无 banner 三分类），再配 state.db 账本交叉。教训：分类器用哪几个字节做判据，决定了它会不会被内容污染。
2. **几乎顺着「四实例时代」的任务书预设去找 hermes 大面积污染**——实际是单角色单窗口（09-03 的 laowantong 线）。如果按预设写审计报告，影响面会夸大一个量级。任务书的背景描述也要过证据，不只结论要过。
3. **E040 拦跨仓交付物时第一反应是改措辞绕行**——想起 #645 的先例（绕行被终审点名），转去读门禁源码找正解（含仓名全路径切仓核验分支本来就存在）。绕行是欠账，读源码是还债。

## 顿悟

配置类 bug 有两层：「env 没传对」和「env 根本不在被读的集合里」。这次是后者——HERMES_PROFILE 拼写全对、值也对、也确实进了子进程环境，但 hermes 的解析链（argv -p → active_profile 文件 → HERMES_HOME）压根没有这个分支。验证配置生效必须看**消费端的解析链源码**，看生产端怎么传永远查不出来。同构推论：一切「传了但没生效」问题，先枚举消费端认什么，再对生产端给了什么——顺序反了就是大海捞针。

## 过程资产

- 修改：`kdo-tools/wechat_link_monitor.py`（run_transcribe 动态 timeout+留痕+熔断，收敛两处 900s）、`90_control/scripts/kimi-headless-launch.py`（hermes -p {role}+移除 TOOL_ENV 死配置）、KDO CLI 仓 `kdo/pre_submit.py`（ALIASES basename+剥扩展名）
- 新增：`kdo-tools/tests/test_wechat_link_monitor.py` +6 例、`90_control/scripts/tests/test_headless_launch_650.py` +3 例、KDO CLI 仓 test_source_refs_gate_567.py +5 例、`60_feedback/diagnosis/diag_20260906_huangyaoshi-hermes-profile-impact-audit.md`
- 产物：`00_inbox/wechat-collect/src_wechat_4b6327b374540e2e.md`（116KB/3214 段）+知识化件+seen 标注；`60_feedback/wechat-collect/transcribe_fails.txt` 机制上线（暂空）
- commit：49928fa76/538e93607（vault #649）、4b0e45f（KDO CLI 修二）、afff203ef/9bb442b43/0304397cb（#650）
- 队列：#649/#650 双双 pending_review 待欧阳锋

## 元反思

本场最值钱的判断是「证据源升级」三连：日志 banner（渲染层）→ hermes 源码解析链（机制层）→ state.db sessions 表（账本层），每升一层结论就少一分依赖运气。0 字节日志与 69 msgs 会话并存是本次的转折点——它证明了「没有输出」≠「没有发生」，和早场 #648「没有任务可失败」同构：**缺失证据本身就是要查的第一证据**。下次接「审计/追溯」类任务，第一步先问「这个系统里哪张表是账本」，直奔账本，日志只做旁证。

## Truman复盘

### 逐轮映射

| 轮次 | 人做什么 | 双三角要素 | AI做什么 | 双三角要素 |
|:---|:---|:---|:---|:---|
| 1 | 下两连单令：#649 P1 烧资源先行（可停拍止血），完成后 #650；预置纪律全带 | 方向+排序 | 启动恢复三读→#504 撞线 --force 留痕领 #649→先停拍止血再读代码 | 执行校准 |
| 2 | （任务单预置：止血须显式报起止） | 约束 | 实证死循环机制（timeout=900 vs 3905s 时长；TimeoutExpired 未捕获）→ 杀在途败拍→受控补转写后台跑 | 侦察+止损 |
| 3 | — | — | 等转写期间并行修二（#643 场景定位两真根因）→ KDO CLI 修复+5 回归+真卡复跑 0 issues → 4b0e45f | 并行建造 |
| 4 | — | — | 转写收工（3214 段）→ 知识化+seen 标注+恢复计划任务→回归 272 passed→五字段报告→complete | 收口 |
| 5 | （#650 任务书预置三件事：修 launcher/历史核查/狗粮） | 决策点预授权 | --force 领 #650→源码级核实解析链→-p flag 修复→狗粮+阴性对照双实测 | 建造+验证 |
| 6 | — | — | state.db 全量 enumeration 出影响面清单→diag 报告（含段王爷 diag 更正+用量归因偏差）→F-035 存在性核查锚点补齐→提审+todos 落账 | 审计+自纠+收口 |

### 飞轮效应

吃到三份红利：#647 落的 E040 _git_ignored 豁免分支本场直接放行 00_inbox 转写产物（自己上周修的门禁自己过）；#634 的模型实测方法论（RTF 实测定系数）原样复用在 timeout 设计上；#645 的「交付物节 git 可达性三分类」教训让 E040 跨仓拦截一次到位。本轮留下：transcribe_fails.txt 熔断机制（下次转写故障有账可查）、拉起器 -p 机制+3 条回归（后续任何 hermes 通道实例不再错载）、影响面审计报告（老朱知情+token 报表偏差校正依据）。

### 对照实验

- 无 AI：148MB 死循环根因（两层：超时+未捕获异常）+跨三系统的 profile 错载审计，人工估两天；本场 ~70 分钟两单闭环
- 无人（无止血授权）：停拍止血涉及停用常驻监控，若需逐级请示，02:54-03:43 窗口内的每拍都在重下 148MB——授权边界预置进任务书是资源止损的关键
- 合在一起：人给「可以停什么」的边界，AI 做「证据升级→根因→修→验→留痕」；转写 41 分钟的等待期被并行施工完全吃掉（修二在转写窗口内完工提审）

### 下次改进

- Agent 自身：①日志/输出做分类判据时先问「判据字节会不会出现在内容里」（banner 判据 > 关键词判据）；②审计类任务直奔账本表，日志只做旁证；③修配置类 bug 先读消费端解析链源码再动生产端
- 方法论/机制候选：E040 报错补「KDO 仓交付物写含仓名全路径」提示（friction 已记）；#504 门禁对「用户连单指令」场景的支持方式（friction 已记，待王语嫣裁定）；hermes 0 字节日志但会话存在（stdout 捕获丢失）立项嫌疑已登记在 diag 建议 4


# 黄药师 daily-context 2026-09-06 三场（claude 通道场，04:17–04:55，#651+#652 连单）

## 差异栏（第 1 章）

vs 同日续场（#649/#650）：续场是「跨三系统的根因取证」，本场是「盲区修复+机制注入+实装面核查」三类活混打。三点最大差异：①本场两单都触发「方案二选一」，且都靠**量级实测**定夺——#651 修法一全扫 vs 修法二登记，实测 00_inbox 顶层 80 子目录/最大 6138 件才敢说修法二是稳者；不是凭感觉选稳妥，是拿数字选。②续场信「任务书要过证据」抓出影响面夸大，本场同款方法论抓到更大的：#652 任务书条款「business-research+deep-research 可用可调」实跑 ls 证伪一半——**连续两场证明任务书的事实性陈述都要存在性核查**。③本场首次给自己的交付物（执行报告）被机器预审拦「负向判词无锚」——宪法条款 2 立完 10 分钟就拦到起草人自己，门禁自洽性活体实证。

## 概要

一句话：#651 watch_inbox 顶层子目录盲区修复（取修法二目录级登记+直接子项签名判重+--seed-top-dirs 一次性基线 74 目录防首拍洪水；真机双验收：测试子目录下一拍登记+AI大航海20260905 补登记+王语嫣通知；回归 276 passed）提审；#652 全Agent行为宪法 v1.0（五条落盘全锚+startup.md/拉起器/基建公告三挂载+hermes 6 profile SOUL.md 注入（#650 已终审 PASS A- 依赖解锁）+狗粮 2 实例双 PASS（claude/hermes 两注入路径，负向判词带锚+断言带【实证】，指令未提宪法=注入自发生效））提审；双双 pending_review 待欧阳锋。

## 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| #651 修法二选一取「目录级登记」而非「全量纳扫」 | 实测顶层 80 子目录、Handle the business 1515 件/最大 6138 件——全量纳扫=看板洪水（#605 裁剪目的仍成立），08-31 7907 行洪水事故同因 | 白名单外子目录下一拍登记一行+行尾注明文件级跟踪入口（加入 SCAN_SUBDIRS） |
| #651 加 --seed-top-dirs 一次性基线而非裸上线 | 新逻辑首拍会把 80 个存量目录全量登记冲板——存量是历史投放非新素材 | 基线 74 目录（幂等复跑=0）+--keep 留出 AI大航海20260905 让下一拍正式补登记，验收与防洪两全 |
| #652 hermes 注入段不「留待」而是照做 | 任务书说 #650 未 reviewed 则留待——先查 #650 状态：queue L535 划销行+任务单 status=reviewed+终审 PASS A-，依赖已解锁 | 6 profile SOUL.md 全注入（grep 6/6 核验）；留待判断用对账不用记忆 |
| #652 调研技能挂载走 startup.md 单点不逐角色改 context | 黄药师铁律「不碰其他角色 context」+D4 自我修改门禁；startup.md 全角色开机必读+拉起器无头继承，覆盖面等价 | 单点挂载三通道（CLI/无头/hermes SOUL），效果可狗粮验证 |
| 宪法条款三措辞按存在性核查结果修正（不虚指） | ls 实证：business-research 唯一实装（SKILL.md+references+templates）；deep-research 仅 10_raw 素材；research-core 仅 MOUNT-MATRIX 登记无 skill 文件 | 条款改「商业主体→business-research；技术/概念类无实装→kdo query+grep，需实装走 skills-assistant 立项」——宪法自己第一天生效条款就是条款 2 的活示范 |

## 思维盲点

1. **验收清理脚本第一版用文本模式重写 production-queue.md**——文本模式读写有整文件换行符/编码被改写的风险（diff 核查后仅 1 行删除、CRLF 全保留才放下）；改 wangyuyan.md 时换成二进制逐行过滤——那个文件真有历史非 UTF-8 字节，utf-8 文本读直接炸。批量重写共享文件前先选「二进制逐行」还是「文本整体」，并验证编码与换行走向。
2. **狗粮第一轮两发全空**——kimi 403 周配额死（上场刚发生的事实，我没先查通道健康就发）+hermes 拿 hongqigong 当目标（目录在≠profile 在册）。**先验通道再发任务**，与 #498「通知缺席≠事件缺席」同构：发射前先确认接收方存在且活着。
3. **hermes SOUL.md 注入前差点忽略 code fence 配对**——tails 看着都正常结束，实际 4/6 文件带 fence；先数 fence 奇偶（全偶=闭合）才追加。往别人的 prompt 文件注入内容，先理解文件的包裹结构。

## 顿悟

「登记面≠可用面」是今天最大的结构性发现：MOUNT-MATRIX 登记 research-core 八行、skill 文件根本不存在——**引用即挂载的登记制，天然会把历史引用固化成「看起来可用」**。同构到宪法条款 2 为什么必须存在：所有「应该有」的陈述（登记、计划、任务书、记忆）都做过期风化，只有当场核查动作（ls/grep/实跑）是新鲜的。宪法五条本质是同一件事的五面：把「当场核查」从美德变成动作规范。

## 过程资产

- 修改：`kdo-tools/watch_inbox.py`（_unknown_top_dirs/_dir_signature/seed_top_dirs/scan 目录级 discovery/看板 N件 列）、`kdo-tools/tests/test_watch_inbox.py`（+4 例）、`.agent/startup.md`（宪法 blockquote+步骤 6.5）、`90_control/scripts/kimi-headless-launch.py`（PROMPT_TEMPLATE 宪法行）、`.agent/infrastructure-bulletin.md`（上线公告）
- 新增：`90_control/agent-behavior-constitution.md`（v1.0，status=draft 待终审）
- 外部注入（hermes 侧，vault 内以任务单报告留痕）：6 profile SOUL.md（basic-skills-coach/coaching-leadership-assistant/hongqigong/laowantong/meeting-assistant/skills-assistant，带 constitution:v1.0 追溯标记）
- 队列副作用：AI大航海20260905 目录补登记（production-queue.md L664）+王语嫣收件箱通知；00_inbox 测试子目录验收后全清（目录+state 键+看板行+通知行，queue diff 仅 1 行删除）
- commit：89f93bec2（#651）、670ee0f9f（#652）；队列 #651/#652 双 pending_review

## 元反思

本场宪法任务有个自指结构：我在落实「实事求是宪法」的过程中，被迫对任务书本身跑了实事求是核查（deep-research 证伪）、被门禁拦了负向判词无锚（条款 2 拦到起草人自己）、被连单撞线重演 friction（第 3 次 force）。三个「被宪法精神打中」的瞬间比写完五条更有说服力——**机制的可信度来自它对自己人开刀**。这也解释了为什么狗粮测试指令不能提宪法：规则只有在无人提示时自发出现，才算注入成功。

## Truman复盘

### 逐轮映射

| 轮次 | 人做什么 | 双三角要素 | AI做什么 | 双三角要素 |
|:---|:---|:---|:---|:---|
| 1 | 一句指令派两单+预置通用纪律（含 #504 连单场景） | 方向+边界预授权 | claim #651 撞 #504→--force+理由引用指令前例（第 2 次）→读 watch_inbox 全文+00_inbox 顶层实测（80 目录/6138 件） | 执行+侦察定标 |
| 2 | （任务书预置修法二选一取稳者） | 决策框架 | 量级实测定修法二→实现签名判重+基线 seeding→8 测试全过+全量 276 passed | 建造+回归 |
| 3 | — | — | 真机双验收（测试子目录下一拍登记/AI大航海补登记）→验收件全清（字节级无损）→E040 拦截→commit 后 complete | 验证+清理+收口 |
| 4 | — | — | claim #652 再撞 #504→--force（第 3 次）→先对账 #650 状态（reviewed）定 hermes 段照做 | 状态对账代替记忆 |
| 5 | — | — | 宪法落盘+三挂载+调研技能实装面 ls 核查（证伪 deep-research/research-core）→措辞按实证修正 | 建造+存在性核查 |
| 6 | — | — | hermes 6 profile 注入（fence 配对检查）→狗粮 2 实例（kimi 403 换 claude 通道）双 PASS→机器预审拦负向判词→补**存在性核查**节→提审+todos/friction 落账 | 验证+自纠+收口 |

### 飞轮效应

吃到四份红利：#650 的 -p flag 修复让本场狗粮②顺带验证 hermes 角色通道正常；#647 落的 E040 交付物规范让两单各只被拦一次（负向判词补节即过）；#504 的 force 留痕机制让连单全程可审计（台账三条在案）；上场「任务书要过证据」的方法论直接在 #652 抓出 deep-research 证伪。本轮留下：watch_inbox 顶层子目录自动纳管（白名单族第三例盲区闭环）、行为宪法 v1.0+三通道挂载（全厂行为底线，待终审生效）、--seed-top-dirs 基线机制（后续扫描面变更的防洪模板）、friction 三条（#504 连单/hermes 孤儿 profile/矩阵登记面失真）。

### 对照实验

- 无 AI：#651 需人工盯 80 个目录的状态漂移，AI大航海类盲区继续靠人肉指认；#652 五条挂三通道+逐 profile 注入+狗粮——两单本场约 40 分钟，人工估一天
- 无人（无修法取舍实测）：按直觉选「全量纳扫」则上线首拍 80 目录登记+6138 件目录逐拍递归=第二次 7907 行洪水事故；量级实测把「感觉稳妥」变成「数字稳妥」
- 合在一起：人给「二选一+取稳者」的判断框架，AI 用实测数据填进去再执行；门禁（E040/F-034/机器预审）三度当「第二双眼睛」，其中一次拦的正是宪法起草人自己的报告

### 下次改进

- Agent 自身：①共享文件批量重写前先定「二进制逐行」还是「文本整体」并验证编码/换行走向；②对外发任务（狗粮/拉起）前先验通道健康+目标存在（profile list/配额），不凭上次记忆；③往结构化 prompt 文件注入先查包裹结构（fence 配对）
- 方法论/机制候选：#504 连单放行机制（friction 已记，第 3 次 force，待王语嫣裁定）；hermes 孤儿 profile 目录巡检（friction 已记）；MOUNT-MATRIX 存在性校验列（friction 已记，报 skills-assistant）；deep-research 封装立项意向（执行报告「需要谁动作」已列）

---

# 黄药师 daily-context 2026-09-06 三场（claude 通道场，11:42–12:26，#656 通道预检+fallback）

## 差异栏（第 1 章）

vs 同日续场（#649/#650 跨系统审计）：续场是「在三个系统里找根因」，本场是「在单仓里新建一层防护机制」，但第一性动作同源——**动手前先实弹验证每个假设**：四个通道的探针形态全部先实测才写代码（GLM 正/坏 key、relay 正 token、kimi CLI、kimi HTTP 被证伪）。本场最大新差异：第一次把「上游」和「工具」拆成两层建模——hermes 上游=kimi 同墙的发现直接改掉了 fallback 设计（纯工具顺序→按上游去重），这是任务书里没有、配置文件里挖出来的结构性事实。

## 概要

一句话：#656 一单三修法全落地——①预检（channel_health.py：claude/codex HTTP 探针 + kimi CLI 探针 + 状态码分类 401/402/403/429=上游级连坐、5xx/不可达=工具级不连坐 + JSONL 台账）②fallback（launch 前逐通道探活，主通道死自动切+todos/stdout 双通知，全死 exit 2 不硬派报王语嫣，`--no-probe`/`--force-dead` 双钩子）③认知表（90_control/channel-model-map.md：CLI→真实供应商→模型→key 指纹→探针→核对命令）；全量回归 273 passed，验收①②③全实测过，已提审 pending_review 待欧阳锋。

## 关键决策

| 决策 | 理由 | 结果 |
|:---|:---|:---|
| 死亡分「上游级/工具级」两级，连坐只沿上游级传播 | relay 进程挂（连接拒绝）≠deepseek 死——工具级连坐会误杀健康上游；401/402/403/429 是供应商账号层的判词才可连坐 | dedup 表 TOOL_UPSTREAM 一张表两个用途（判定+文档机器可读面） |
| kimi 通道弃 HTTP 探针改 CLI 级 | 实测 credentials 里 access_token 08:21 已过期→HTTP 探针 401 假阴性（把活通道判死=错误 fallback）；OAuth 15min 一换只有 CLI 自己会刷 | 探针成本 ~3s（403 快败实测 2.7s），换来不误报 |
| fallback 链按上游去重，hermes 排最后 | `~/.hermes/config.yaml` 实证 provider kimi-coding 与 kimi 同上游——kimi 403 时 hermes 同死，撞它=浪费一次拉起 | 链=主通道→claude→codex→kimi→hermes；单测钉死「工具级死亡不连坐」 |
| 链序 claude(GLM) 最优先 | 09-05 夜两墙连撞时 GLM 全夜存活扛下全部产出（任务书实证） | laowantong/huangyaoshi 线 7 天窗内自动走 GLM |
| 全死 exit 2 不硬派 + 保留 `--no-probe` 口子 | 假跑必撞墙且烧 token；但预检本身故障时不能把工厂锁死 | 通知里自带应急命令行，报王语嫣不静默 |
| codex 通道坏 key 模拟改 `--force-dead` 钩子 | 实测 relay 不校验调用方 key（坏 Bearer 仍 200）——本地无法伪造上游 401 | 坏 key 路径的验收落在 GLM 通道实弹（401 判死）+钩子路径 |

## 思维盲点

1. **测试里给 channel_health 载了第二个模块实例**——importlib module_from_spec 又 exec 了一遍，patch 打在副本上、launcher 用的是它自己 import 的那份，三个用例假绿/假红。教训：patch 必须打在被测对象实际持有的引用上（`launcher.channel_health`），不是「同名文件再加载一次」。
2. **「坏 key 模拟」四通道通用这个预设没验就写进验收理解**——relay 实测不校验调用方 key，假设塌了一半。行为宪法第二条（负向判词附核查锚点）的反向同样成立：正向「可以」也要先跑一次。
3. **12:07:16 laowantong 生产 fallback 的 todos 通知未落账**，最初我连「通知必达」都没怀疑——排查后确认 todos 是 best-effort 面（写失败被吞/并发会话全文件重写冲掉，二选一无法回溯【推断】）。把写失败从 `pass` 改成 stdout 告警，台账职责彻底交给 append-only 的 channel-health.log。

## 顿悟

「额度墙」长在**供应商账号**上，不长在 CLI 客户端上——claude.exe/kimi.exe/hermes.exe 这些名字是给人看的标签，探针和 fallback 必须按上游建模。同构推论：值守报障要报「哪堵墙」而不是「哪个客户端」，这正是认知表存在的理由（#656 立项起因那句「glm-5.3-flash 怎么会没额度」就是把墙认在了客户端头上）。另一条副产品：key 指纹约定（sha256[:8]+'…'+尾 4 位）是我靠两条给定指纹**重算破案**出来的——台账约定本身也要可验证，否则下一双手接不上。

## 过程资产

- 新增：`90_control/scripts/channel_health.py`、`90_control/scripts/tests/test_channel_health_656.py`（11 用例）、`90_control/channel-model-map.md`（认知表）
- 修改：`90_control/scripts/kimi-headless-launch.py`（预检→fallback→全死不硬派+双钩子+stdout 钉 UTF-8+notify 失败告警）、`.agent/infrastructure-bulletin.md`（09-06 公告节）
- 台账：`logs/channel-health.log`（含 12:07:16 生产实战一条：laowantong kimi 真 403→自动切 claude）
- commit：7e7d4e33a（vault 备份拍扫入在制品）+ 4282b4738（#656 交付物）
- 队列：#656 pending_review 待欧阳锋；todos 落账 1 行（12:26）

## 元反思

本场最值钱的一幕是**验收还没跑、机制已实战验证**：12:07:16 我还在改代码，王语嫣拉 laowantong 的一次真实派工就触发了新预检——kimi 真实撞 403 →自动切 claude，台账首行就是生产证据。这比任何 force_dead 模拟都有说服力，也印证了「给活系统加防护时，防护上线即被真实流量检验」是最高质量的验收。另一条复利：续场的「证据源升级」（渲染层→机制层→账本层）本场直接复用——配置文件（机制层）+进程命令行（账本层）两条证据就把「relay≠GLM」钉死，没走一步弯路。

## Truman复盘

### 逐轮映射

- **人定方向**：老朱晨问「glm-5.3-flash 怎么会没额度？是否都自动切 kimi 没发现」定根因方向（无预检无 fallback），王语嫣把它编译成带实证的任务书+四条核实事实——我全程没做方向判断，只做实现与取证。
- **AI 做执行**：四通道探针形态实弹验证、探针引擎+fallback 编码、11 用例、认知表落地、E040 门禁补 commit。
- **AI 做交叉验证**：用户给定事实逐条本机重算/实证核验（指纹 sha256 重算吻合、relay 上游进程命令行实取、hermes config 实读），发现并修正了给定口径之外的一个结构性事实（hermes=kimi 同墙）。
- **人做判断**：fallback 链顺序是否合异构防线口径、`--no-probe` 口子留不留、全死送达面够不够——三条显式留给欧阳锋终审，不越权自裁。

### 飞轮效应

行为宪法五条本场全部用上且见效：断言三级标注（执行报告全部【实证】/【推断】落锚点）；负向判词附存在性核查（「channel-model-map 不存在」先 ls exit 1 才下判词）；疑问先检索再开口（hermes 上游先读 config 再设计 fallback）；解放-检验循环（先验四个探针形态再写代码，两条预设被实测证伪省了返工）；Y 模型（任务书=老朱深层动机「一晚两墙连撞根治」，不是「加个重试」）。

### 对照实验

- 正：GLM 正 key 探针 200/1.2s ↔ 反：坏 key 401/0.1s（分类正确性）
- 正：relay 正 token 200/0.9s ↔ 反：坏 Bearer 仍 200（证伪「坏 key 模拟通用」预设）
- 正：kimi HTTP+过期 token 401（假阴性）↔ 反：kimi CLI 同刻 403 快败 2.7s（探针形态选择依据）
- 正：`--force-dead kimi` launch 切 claude+会话跑完 ↔ 反：全 force-dead exit 2 零 spawn（不假跑）

### 下次改进

- Agent 自身：①给共享文件做 append 通知类写入时，默认假设「可能被并发会话全文件重写冲掉」，重要留痕走独立 append-only 台账（channel-health.log 模式可复制）；②测试里 patch 第三方模块必须引用被测方实际持有的同一实例，importlib 双载是隐形坑；③「模拟 X 不可行」要当场给替代钩子（--force-dead），不要把不可行留成验收缺口。
- 方法论/机制候选：①「上游≠工具」两层建模值得沉淀为通用卡（任何多通道/多供应商防护都适用）；②channel-health.log 的 JSONL 决策台账模式可推广到其他值守类脚本；③kimi 周额度 7 天窗结束时刻值得进时钟（恢复即自动回主通道，无需人工切回）。
