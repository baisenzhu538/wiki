---
title: 黄药师失忆恢复记录
updated_at: 2026-09-05
---

# 黄药师失忆恢复（重启后 3 分钟加载）

## 2026-09-05（#645 对话蒸馏管线交付提审）

- **新工具**：`kdo-tools/conversation_distill.py`——对话蒸馏管线（kimi wire/headless/hermes 三源 → 三层分流 external→pending-cards / zhu→`30_wiki/personal-os/zhu-conversation-insights.md` / human→pending-cards；原文锚子串强校验；增量游标 `.kdo/conversation_distill_state.json`）。每日 23:50 计划任务 `kdo-conversation-distill`（S4U）自动增量
- **试跑实证**：09-02~05 真实历史 8 块 LLM 调用 0 失败，external 43/zhu 13/human 8，伪锚拦截 3；51 张候选卡在 00_inbox/pending-cards/distill-*-20260905-*（免仓区不进 git）
- **登记面**：矩阵行 30 + inventory（工具族+§5 计划任务，计划任务总数 13）
- **新教训**：交付物节路径先做 git 可达性三分类再加反引号（E040 vs gitignore 铁律交集无解，friction-log 09-05 已记）
- **hermes 源边界**：Windows 侧 `~/.hermes/state.db` 是 0 字节空镜像，实库在 WSL gateway——蒸馏器优雅跳过，接 WSL 侧需另立项

## 2026-09-03 早场（记忆恢复+#620/#623 双单终审闭环+建议书 ×3）

- **#620 实例命名铁律已终审 PASS A-**（queue_transition `_claimed_by_role` 旧名兼容+claim 裸名门禁 `_legacy_dash_ok`+launcher 裸名+翻转通道口径，7 用例 238 passed）——老朱 09-02 铁律落地；**matrix_exempt 教训**：动 queue_transition 等信号面文件必须预置矩阵声明或豁免注记（探针反查会抓，§3.19 半条学费）
- **#623 每日复盘计划任务化已提审**：schtasks `kdo-daily-review`（每日 23:37 S4U）→ `kdo-tools/daily_review.py`（三角色 headless Truman 复盘+空班豁免 F-062+指令模板内嵌禁编造），首跑 00:50 三实例 🟡B 级实证；今晚 23:37 自动首拍=自然验证点
- **#622 graph_index 重建+哨兵终审 PASS A-**（复审闭环）；#625 门禁套件批2 已提审（同夜 headless 完成，git 大文件三层门禁）
- **建议书 ×3 待王语嫣裁定**（PROPOSAL-PENDING 09-03 01:02）：① 6 资产未登记基建总表（infra_status 测试持续红：transcribe_win/vault_git_backup/clock_watchdog/kimi-headless-launch/vault-integrity-check/wiki-vault-restore）② queue-archive 月界漂移测试红 ③ vault backup 30min 自动 commit 扫入 agent 在制品互撞（建议纪律+机制层二选一）
- **新教训**：多生产者仓禁用 stash 隔离（用 git worktree）；backup 节拍 :02/:32 觉知=子任务完成即 commit；Edit 文档后 H1/结构自检；heredoc 不写编码混合内容
- **下次启动**：读本文件 → CAPSULE_STARTUP（git_head 32f536ca3/队尾 625 已校）→ myqueue huangyaoshi（待终审 #623/#625；若 6 资产登记债获裁定先补登记清红）→ daily-context 目录最新

## 2026-09-02 夜班（施工链五连单：#603/#604/#605/#607/#608 全 reviewed）

- **#607 最大机制产出——vault backup 系统级化**：历史「vault backup: <ts>」commit 一直是**会话级 cron** 扛的（无 schtasks/无脚本/节拍随会话生死），08-26 22:56 系统重启（事件日志 6005/6006 实证）杀会话→停摆 6 天无人察觉。修复=`kdo-tools/vault_git_backup.py` + `vault-git-backup.cmd` + schtasks `kdo-vault-git-backup`（每 30min，S4U 后台模式，XML 照 kdo-role-clock 模板）+ conveyor_probe **第十信号 `_scan_backup_stall`**（最后 backup commit 超 24h→gate-blocked 台账+推王语嫣，并入第九信号通道）。矩阵行 24 已登记
- **#605 dispatch 收口**：watch_inbox 扫描面改白名单（00_inbox 顶层+pending-cards/，大目录树结构性出局）+ `DISPATCH_LEDGER_ENABLED=False` 台账停发（17 份零签收，职能并看门狗 v5）+ 49 份存量台账入隔离区。看板登记/收件箱推送零改动（沙盒验证）
- **#603 tmp 清理**：根目录 44+kdo-tools 22 归档 `_tmp/603-archive/`；3 个读凭据脚本随 #600 口径入隔离区；`_tmp_skill_health.json` 迁 `90_control/baseline/`（建议书引用已改指）；例外保留=tmp_video/（已发布 manifest 引用）+_tmp_m371_domain_unknown.txt（clean-metadata-371.py 写引用）
- **#604 散点归位**：假盘符树 `C\uf03a`（1 截断文件+2 散落 PUA txt，无独有内容）+Harness 连字符重复版入隔离区（保留全角冒号版=plan_20260621 引用）；6 个 wechat mp4 git mv→`10_raw/assets/wechat-collect/`+14 处转写稿源引用改指
- **#608 image_detail 死循环**：wechat_link_monitor 公众号分支前置识别 `pages/image_detail` 即 mark_seen 跳过（08-31 起 3 条链接循环重试 ~29h 封死，两轮实跑对比验证）
- **关键坑**：①git 批量移动必须 `git status` 双向核验——D 侧（删除）未 add=交付未完成（#605 首轮 FAIL）②`ls-files|head` 取样≠untracked 判定 ③schtasks XML Command 别内联引号参数（0x80070002），走 .cmd 包装 ④S4U=后台可跑，「只使用交互式」=注销即停
- **下次启动**：读本文件 → myqueue huangyaoshi → 无单待命。backup 面已系统级自治，不用再管会话 cron

## 2026-09-01 上午（#588 Skill目录与挂载矩阵：扫描生成制上线）

- **#588 交付**（已提审 pending_review，commit b958575a8）：`scan_skills_registry.py`（40_outputs/code/scripts/）+ `INDEX.md` + `MOUNT-MATRIX.md`（40_outputs/capabilities/skills/）+ workflow 出生模板增补「已挂载skills」节 + 增量钩子三挂（health-check 第 20 项检查 / infra-status skills-registry 行 / infrastructure-inventory.md 巡检族）。73/73 fresh 亲验；增量演示（测试 skill→stale→重跑收录→清理）通过
- **挂载=登记制**：文件引用即挂载，扫三类登记处（role-routes 路由2 / 30_wiki/agent-specs / agents/*四件套文件）。状态三档：已挂载 31/单点 1/无主 41——无主归属裁定归 Skills 助理（#587 分工），不是我
- **关键坑**：①#504 审查等待期 claim 被拦（#590 pending_review 占位）→ 老朱直令任务走 `--force` 留痕合法绕过 ②**部分 SKILL.md 带 UTF-8 BOM**——frontmatter 正则 `^---` 失配静默丢 description，读文件一律 `utf-8-sig` ③shared 目录本身就是容器（shared/shared 双层是我自己写错的，不是库结构）
- **74 vs 73 口径裁定**：73 个 skill 目录（验收「73/73」成立）+ README.md = ls 显示 74 项。实测写进执行报告，不猜
- **下次启动**：读本文件 → startup.md 第 0 步门铃自查 → myqueue huangyaoshi → #588 若有终审意见先返工

## 2026-08-28 凌晨收官（唤醒链革命夜：九连单全闭环+门铃体系建成+门铃工班自主干完两单）

- **九连单全 PASS**：#556（待拍板第八信号）/ #558（hermes 工具双 bug：grep 兜底 BRE→ERE + read_file 字节采样切断多字节误判 binary）/ #559（profile 配置巡检：16 profile approvals.mode 全 smart+漂移巡检挂 kdo-health-daily+SOUL charter 指针）/ #560（cron 卡死根因更正=进程层无 tick 属主非调度器病，隔离活体回归实证恢复逻辑健康）/ #561（四实例 SOUL 对齐+wangyuyan 角色重写）/ #562（心跳语义=消费回执+SessionHeartbeat 钩+第五探针记录聚合）/ #563（飞书四实例时钟上线+心跳入注册表，门铃工班自主完成）/ #564（read_file 尾部豁免收紧，门铃工班自主完成）/ #565（门铃机制三层）。唯一 FAIL=#566（mojibake 假前提，返工回滚后 PASS）
- **门铃体系（#565，今晚最大机制产出）**：todos 落盘≠会话唤醒的断点已修。三层=①会话级最小 cron 自装（`.agent/startup.md` 第 0 步：新会话 CronList 自查缺了自建）+SessionStart 钩注入自检指令（`kdo_session_boot_hook.py`）②OS 级兜底=计划任务 `kdo-huangyaoshi-doorbell`（15min，`kdo-doorbell.cmd`+`kdo_doorbell_guard.py` 活着跳过守卫）③唤醒载荷带 REVIEW-PENDING 明细+30min 加急（role_clock）。**会话级 cron 随会话死**（08-26 时钟巡航 v2 随旧会话死亡的实证）——门铃不在=自己装，不等提醒
- **门铃工班实证**：03:29-04:39 门铃唤起的自主工班零人肉完成 #563/#564 双单双 PASS——「明早没人喊也会自己干活」已兑现
- **关键坑（两连撞同族）**：①GBK 控制台+heredoc 链路里**含非 ASCII 字面量的检测代码不可信**——`count("")` 字面量被吃成空串返回 len+1（22782=22781+1 逐数吻合的鬼数字），#566 假损坏结论由此而来；检测用字节转义（`\xef\xbf\xbd`）或结果落文件用 Read 读 ②mojibake 三问铁律（欧阳锋终审给的）：字节层→解码链→显示层，断言「文件损坏」必须落在字节层证据上
- **§3.19 三连补课**（#562/#568/#569 触基建信号面未同步矩阵，王语嫣三次转办）：已合并登记矩阵行 5；**今后交付清单纪律：动 queue_transition/conveyor_probe/role_clock 等信号面文件→矩阵登记进交付物**，再犯王语嫣将立项挂终审门禁
- **门禁自咬实录**（都是好事）：#488 inventory 覆盖门拦下 #562/#565 新组件未登记两次；E040 拦下相对路径/花括号路径多次——报错样例已由 #569 补可操作化
- **hermes 仓分支锚定**：原 checkout 在 tag v2026.8.3 detached HEAD，今晚三个 commit 曾悬空——已建 `kdo-prod` 分支锚住（含 #558/#560/#564），入主干留仓主裁定
- **外部阻塞**：DeepSeek 402 余额耗尽（04:05 急报落王语嫣收件箱）——飞书四实例调度+心跳正常但 LLM 调用全哑，等老朱充值或裁定换 provider
- **下次启动**：读本文件 → startup.md 第 0 步门铃自查（CronList，没有就 CronCreate 15min 门铃）→ myqueue huangyaoshi → 队列空就待命报告
- **在途/观察**：无在途单；观察点=飞书欧阳锋兜底自起（402 恢复后 #563 延迟验收自然闭环）；v0.9/v1.0 feature-json 同源损坏已证伪撤回；段王爷系 5 卡虚构 capability 引用挂账（debt_20260828）等编排

## 2026-08-26 收官（时钟自治两日：19 单全闭环+静默失效家族治理+种子包跨机+漏检自迭代）

- **角色时钟建成（老朱指令「像欧阳锋一样 15 分钟扫看板」）**：cron `01M0Z16GVGR0ZKTN57GNXGSA9B`（每 15 分钟 :06/:21/:36/:51，v2=myqueue 全表驱动——v1 模式 grep 漏检 #528 两天被老朱三问抓包，已重建+建议书 diag_20260826_huangyaoshi-clock-myqueue-standard 给王语嫣统一全角色口径）。**cron 不跨全新会话**（resume 同会话才续火）——重启后先 CronList，没有就用下方「时钟 prompt 本体」重建
- **时钟 prompt 本体（重启重建用，一字不改照抄）**：【黄药师时钟巡检 v2】①巡检面= `python 90_control/scripts/queue_transition.py myqueue huangyaoshi` 五栏输出（可领/等依赖/冻结/进行中/待终审），禁模式 grep；②待终审栏有单→读任务单终审/复审记录节领意见，FAIL 先返工；③可领栏取序号最小者 claim（完整 task_id，被 pending_review 阻塞不 force 除非老朱明说继续）→读任务单全文→施工→测试（kdo-tools/90_control 基线 160/159 不退步）→执行报告五字段→path-scoped commit（标 by huangyaoshi）→complete 提审；④无单即报结论收工不硬找活。纪律：新工具登记 infrastructure-inventory.md；中文路径/批量操作用 Python 不用 bash；预审红项逐条标注处置；会话结束动作等老朱说结束
- **19 单全闭环**（#503-#513/#516/#517/#519-#524/#527/#530/#532-#538）：终审全 A，唯一 FAIL=#515（attach 吞字段，返工后 A）；#537 走了 PASS→改判 FAIL→复审 PASS 三轮（改判通道 #538 由此立项建成）
- **关键资产**：预审管线（#515 四判据参考层随提审附单）/质量基线周报（#514 每周一 06:35）/审查供给三件套（#520 叫醒+阻塞链+SLA）/通知矩阵 G1G2 销项/kdo-seed 种子包+D:\tech-wiki 狗粮场在跑（第二套探针 -tech 后缀已注册）/E040 交付物入仓门禁
- **新错误入库**：E023 按预期扫描（模式 grep 当巡检面）/E024 写操作不自检（attach 无写后断言）/E025 申报数字凭估计
- **纪律新规**：提审前自体应用一拍；预审红项提审前逐条标注处置（误报+原因）；申报数字一律实测
- **下次启动**：读本文件 → CAPSULE_STARTUP → `myqueue huangyaoshi`（禁 grep 看板）→ 时钟 cron 若在跑就别重复建（CronList 查 01M0Z16…）
- **在途**：#540（VLM 两段式）等终审；#528 已 PASS A；可领 #541（检索 trust 加权）/#542（概念交叉验证 WARNING）/#543（source_refs 死引治理 1024 条存量）；#515 判据清单=欧阳锋欠的作业；D:\tech-wiki 第 4-5 步=那边王语嫣；l1-capture 参数化修复单等王语嫣编排



- **本场 3 单全提审**：#496（source_refs 判定升级——判 FAIL 先查正文来源段，KDO 561→567 passed）/ #501（**角色待办收件箱**：90_control/todos/<role>.md，探针通知 CLI 收件箱+CAPSULE_STARTUP 入口+双实例欧阳锋双通道）/ #502（**落盘冻结机械化 L10**：任务单正文越界报警，四类豁免+按状态收紧，挂 health-check 每日兜底，97 passed）
- **探针故障全链条排查（重大事故）**：kdo 秘书不发消息 → 三重根因：①schtasks TR 不经过 shell（`>>` 字面传给 python → 失败码 -2147020576，cmd /c 包装修复）②20:51 失败=F-036 编辑中途 ③**dry-run 更新 state 去重=消费真实信号**——#499 FAIL 打回通知飞书+CLI 双丢（用户两次报告"没收到"）。修复：dry-run 不保存 state（诊断工具零副作用纪律）
- **F-036 机制落地（用户"为什么总是要提醒"质询→方案 C 拍板）**：门禁（queue_gate.check_issue_disposition 共享判定）+探针第七信号；干跑即抓到 #domain-reclassification 违规提示补落点
- **用户纪律（本场 4 条）**：①特例下不为例（#488 未入队封口，一律任务制）②"这是你的职责，你发现了可以主动做"（主动健壮性检查职责化）③git=容灾（L1-full 无备份≠缺口，表述修正）④执行报告节提审后不豁免（L10 收严拍板）
- **教训固化**：dry-run 零副作用；计划任务改后真机验证；豁免区间测试用坏位置；探针三层（信号→通道→去重）复杂度警戒
- **队列**：我名下 pending_review 3（#496/#501/#502），可领 0；等欧阳锋终审
- **待办/观察**：探针三层解耦（信号→通道→去重）立项候选；aliases 1555 清理（老顽童）；周全量周基线待立项；kdo infra status CLI 集成待拆单；#490 codex-homes 试点
- **下次启动**：读本文件 → CAPSULE_STARTUP（git_head 以实际为准）→ myqueue huangyaoshi → 队列 → 复盘目录最新（2026-08-24.md 第二场节）

## 2026-08-24 收官（基建体系化日：8 单全闭环，总表+日增量+batch 豁免）

- **本日 8 单全 PASS A- 或提审**：#482（batch accept commit bug）/ #483（gate-blocked 噪声分流）/ #484（来源形态词黑名单）/ #488（**基建资产总表**：infrastructure-inventory.md 八域六字段 + infra-status.py 27 项全绿 + 覆盖对照检查 67→0 未登记）/ #489（L1 采集面四源：codex/opencode/qwen+敏感排除）/ #491（**L1 体积治理**：去 C 镜像删 1698MB+hash 去重+旧天归档+**日增量结构**——二次跑 13/11098）/ #492（**batch 豁免**：F-050，#426 长程不再卡主线）/ #494（aliases 污染检查器第 6 指标：全库 53.94% 大面，清单交老顽童）
- **建议书**：D-20260824-001（基建造表→#488 当天交付）；用户裁定"#488 覆盖对照补丁=特例下不为例"（总表维护纪律落盘）
- **教训固化**：任务书执行期间可被收紧（#491 任务 2 硬性化，补做才闭环）——领任务记版本+提审前重读逐项核；占位节 append 4 次致 complete 拦截——执行报告替换占位节不 append；删除类操作先说明再执行
- **队列**：我名下 #494 待终审；可领 0
- **待办/观察**：aliases 1555 张清理（老顽童，随 #426/#493）；周全量周基线待立项；kdo infra status KDO CLI 集成待拆单；#490 codex-homes 切换试点待启
- **下次启动**：读本文件 → CAPSULE_STARTUP → myqueue huangyaoshi → 队列 → 复盘目录最新

## 2026-08-23 深夜收官（第二场 12 单全闭环：路由层落地+队列清零日）

- **本场 12 单全 PASS A-**：#463 复审（registry P1）/ #456 审计器盲区（0→61 行，3 残留浮出）/ #450 文件流转 lint L1-L9 / #471 L1 采集常驻调度+体积红线 / #472 角色路由层（**myqueue 五态视图+role-routes 技能知识路由+CAPSULE_STARTUP 入口**——用户"有没有路由"提问→建议书 D-018→采纳入队当天交付）/ #473 wiki 卡 L9+冻结无状态化（kdo lint 集成拆出）/ #474 全库标签体检（2876 卡 5.9s，脏词 275/空值 577/来源轴 1258，+🟠校准：微差根因=#426 第二批治理）/ #477 任务单 doc_id 清理 17 份 / #478 review-check 失败项明细 / #479 批次验收四步一体
- **建议书 2 份**：D-20260823-018（三路由，已交付 #472）/ D-20260823-022（review 失败明细，②已采纳落地 #478）
- **队列**：我名下全 0（可领/等依赖/冻结/进行中/待终审）；活跃全是老顽童（#426/#469/#470）与王语嫣（#468/#480）
- **新工具**：myqueue（任务路由）/ role-routes.md / tags-audit.py+check-tags-health.py（健康线挂 health-check 第 8 项）/ queue_batch_accept.py（re.subn 断言禁静默）/ remove-task-docid.py / review-check 失败明细
- **待办/观察**：kdo lint 集成独立单；agent-os §10.4.1 对齐挂老朱窗口；#426 第三批走工具验收；#474 治理批次排产王语嫣
- **下次启动**：读本文件 → CAPSULE_STARTUP（git_head 以实际为准）→ myqueue huangyaoshi → 队列 → 复盘目录最新

## 2026-08-23 收官状态（17 单交付：机制层从人肉纪律到全自动化的一天）

- **今日 17 单全交付**：#430 agent复盘 git 化 / #432 胶囊 L0 / #433 负向判词门禁 / #434 L0 自动写入 / #435 词表扩展 / #442 误伤返工 / #443 探针路由 / #444 force 台账+assignee 口径 / #445 一键启动（WT 5 标签 5 色） / #453 队列归档瘦身 / #457 处置门禁结构化 / #460 问题上报最终设计（机器自报 gate-blocked+第五探针） / #461 cancel 命令 / #462 流转完成信号 / #463 L1 全量上下文（F-044 改名） / #464 镜像联动——全终审 A/A- 或待审；#458（被 #460 取代，冻结待王语嫣 cancel）
- **记忆胶囊全家桶闭环**：L1 事件库（改名后）+ 自动写入 + L1 全量原文（D 盘 5554 文件+C 盘镜像）+ save 后自动 mirror 联动——风清扬审计权履职
- **探针六信号全通**：新提审/可领取（按 assignee）/建议书/friction/gate-blocked/已终审+退回——飞书真实通知（签名修复后 code 校验）
- **用户新纪律（08-23）**：①协作文件只增不改（已交/resolved 冻结，增补另起新文件带日期+原因）②验证分层四态（L1/L2/L3/待活体，执行报告必声明）③上板冻结（已上板任务不能改范围合并，调整须另下任务编排书）
- **待办**：我名下 #456（P2 胶囊 agent_id 统一）/ #450（等 #449 规范生效）/ #459（冻结勿领）；飞书 huangyaoshi 独立通道可后补；体积红线监控立项候选
- **下次启动**：读本文件 → 队列 → 停车场（F-033/034/035/036/039/044/045）→ 复盘目录最新

## 2026-08-22 收官状态（5 单全终审闭环：#425 A / #419 A / #421 A- 复审维持 / #422 A- / #424 A-）

- **今日 5 单全闭环**：#425 健康度指标集 A / #419 复盘门禁 A / #421 传送带探针 A-（P1 静默吞通知+P2 序号显示已修，复审维持；P3 写队列无锁随 F-029）/ #422 agent复盘 P1 A-（T5 退役实例归并 codebuddy→huangyaoshi、kimi-code+Kimi→wangyuyan + T6 顶层 16 文件归类 + T8 清理，用户确认删 _test_mv_probe.txt）/ #424 agent复盘 P2 A-（T7 归档统一补 2 README + T9 白名单 agent复盘/README.md，TODO=agent复盘 git 化已登记 F-036）
- **停车场 08-22 新增**：F-033（飞书 agent 探针响应闭环，用户指定黄药师建议案）/ F-034（交付五字段硬格式，老朱校准）/ F-035（审查意见书强制落盘，老朱校准）/ F-036（agent复盘 git 化，我登记）
- **#421 上线后运转**：计划任务 kdo-conveyor-probe 每 10 分钟自动跑；三类信号飞书真实通知已通（加签 HMAC-SHA256）；测试建议书 3 份（probe-test-1/2/3）待王语嫣裁定处置
- **下次启动**：读本文件 + 队列（我名下 0 剩余）+ 停车场 F-033/036 待会诊

## 2026-08-22 深夜状态（第三场：三连交付 #425/#419/#421 全提审）

- **三单全提审（等欧阳锋终审）**：#425 健康度指标集（--health 11 指标，W3 基线对账 798/2865 一致，顺带修 audit_queue_integrity int/str bug）/ #419 复盘门禁双查（四源 11 章收口 + 六角色触发话术统一 + 深度四条硬指标，王语嫣 3 样本校准全对齐，8 测试）/ #421 传送带探针（契约 + 单扫描器登记/通知同源 + pre-submit 三元组门禁，5 测试，夜间静默实测生效）
- **#421 通知全线上线（深夜用户配合）**：飞书群机器人（加签 HMAC-SHA256，URL+密钥在 `kdo-tools/.feishu_webhooks.json` git 忽略）+ 三类信号真实通知实测全通（欧阳锋新提审/老顽童可领取/王语嫣建议书到达）+ **计划任务 kdo-conveyor-probe 已注册（每 10 分钟，result 0）**——全自动；测试建议书 3 份（probe-test-1/2/3）由王语嫣裁定处置
- **教训固化**：①批量替换宽模式会误伤历史叙述（agent-os §10.9 被改 10→11 章，人工恢复并注明）②段重写按文件名去重会误删同文件多条历史裁定记录（orchestration-audit 双裁定，git HEAD 恢复，策略改"保留全部历史行只防新增"）③KDO 回归 1 个历史失败（test_end_to_end_smoke KeyError 'sources'）与本次无关
- **队列**：#425/#419/#421 pending_review；我名下剩 #422/#424（agent-retro 治理，依赖 #418 已 reviewed 可做）

## 2026-08-22 晚状态（会诊批次七单全交付 + 幻影丢失事故）

- **会诊批次交付（白天已记录外的后续）**：#409 YAML 修复 58 张（PASS A）/ #410 mojibake 186 行恢复（PASS A）/ #412 W3 口径核实（会诊前置）/ #413 O-3 分批提审无声修复（PASS A-）/ #414 副本清理 4 处（FAIL 补件后重审中）/ #415 工具名引用面清单（提审中）/ #418 agent复盘 治理 T1-T3（提审中）；会诊表态 14+6 条落盘 positions/huangyaoshi.md
- **幻影丢失事故（E022，最大教训）**：#418 T2 用 bash 链式 mv/rmdir 执行，sales-dialogue-assistant 目录消失→报丢失；王语嫣复核裁定=**文件从未存在**（事故前审计基线三处枚举皆空）。教训：①报丢失前验证最后一次存在的证据 ②中文路径文件操作一律 Python（禁 bash mv/ls）③禁 2>/dev/null 吞错 ④批量移动前枚举核实+before/after
- **队列**：#418 等 3 单提审中；我名下 queued：#419 review-gate-depth-upgrade / #421 conveyor-probes（X-1）/ #422 agent-retro-p1 / #424 agent-retro-p2 / #425 health-metrics-set
- **复盘**：2026-08-22.md 全日合并版（A 级）；技能进化日志第二场段；E022 入错误模式库

## 2026-08-22 状态（pdf-inspector 注册五落点 + 自动化闭环实证 + 九层调研）

- **pdf-inspector 注册完成（用户直令）**：①包装脚本 `40_outputs/code/scripts/pdf_inspector_route.py`（classify-then-route，任意 python 自举 `_tmp/pdf-inspector/` venv，单文件/批量/--json/--stdout）②README 登记 ③cap_hub `F_PDF_INSPECTOR`（parsing 类，26 features）④document-parsing-toolkit 引擎矩阵+决策树+详细节 ⑤toolkit.md 武器库"PDF 进料"小节；kdo index 4066 文档已刷新，路由文档可检索
- **狗粮实证**：5 份 KDO 真实 PDF 5/5 分类正确（conf 0.875-1.0，0.2-0.42s/份），混合页正确标出（pages_needing_ocr [27]/[18]）；**重要教训：小昭声称"已装 pdf-inspector 1.15.0 实测"实为未安装**（P-15 同模式）——声称必须落盘验证
- **外部 agent 越权收编闭环实证**：小昭直接写 30_wiki 的工具卡 → 移 00_inbox/pending-cards + watch_inbox 登记 → **王语嫣已编排入队 #407**（外部建议稿核验入库）——素材→编排→入队全链路打通
- **知识库建设九层调研**（用户指令，明天讨论认知输入）：`60_feedback/diagnosis/diag_20260822_huangyaoshi-kb-building-9layer.md`——核心发现：**KDO 架构=Karpathy LLM Wiki 编译器模式完整实现（2026 最前沿）**，不需要架构革命；真正缺口=调用回路/组织机制/消费端自动化/合规基线；70% 死库规律；3 个讨论问题提案
- **分角色自动化方向**（用户澄清后对齐）：探针只做"推送/流转"，判断留人（编排/产卡/终审各角色自己做）；传送带骨架全通，缺"角色间飞书通知"层（王语嫣/老顽童/欧阳锋三个探针，纯机械，待立项）
- 队列状态：387 总任务，queued 1（#407 待领）、pending_review 1

## 2026-08-21 状态（建议书 L 系列五连发 · 全 PASS A）

- **我名下任务全清**：#399-#404 五单全闭环——#399 全库复扫工具（**PASS A**，6 检查项+delta 增量报警挂 health-check，归零声明唯一口径）/ #401 规则门禁化盘点（PASS A，182 条→22 簇清单）/ #402 长程 workspace（PASS A，claim 联动自动建三件套+#393 试点）/ #403 出生两问（PASS A，模板前置闸）/ #404 trust 实证（PASS A，无痛点诚实关阶段二）
- **🆕 新机制三件**：#399 `full-library-rescan.py`（全库复扫标准口径——任何"归零"声明须附其输出，否则终审 FAIL）；#402 `long_running: true` workspace（claim 自动建 + 随流转 commit）；#403 出生两问（新 agent 前置闸，agent-context.md 模板）
- **记忆恢复路径修正**：认知复盘 6 件套在拼音轨 `agent复盘/huangyaoshi/`（中文旧轨 DEPRECATED）；daily-context 最新=2026-08-21.md；技能进化日志最上方追加
- **下次启动快速通道**：读 `.kdo/CAPSULE_STARTUP.md`（git_head 以实际为准）+ `.agent/huangyaoshi-context.md`（行为牌 B1-B6）+ 本文件 08-21 节 + `agent复盘/huangyaoshi/daily-context/` 最新
- **待办**：_tmp 23M 测试产物删除（等老朱过目）；PARA 未消化素材交王语嫣；#401 Top 3 门禁化建议待王语嫣立项（口述稿 source 引用检测 ×16 / D4 事前检测 ×9 / 口述稿全文半门禁化 ×8）；处置门禁关键词族收窄评估（friction-log 08-21 记）

## 2026-08-19 状态（治理批次后）

- **我名下任务全清**（#357-375 十二任务交付完毕：#357/#361/#363/#364/#366/#367/#369/#371/#372/#374/#375 全部终审或提审）
- **⚠️ 路径变化（#367 双轨冻结）**：认知复盘 6 件套（技能进化日志/错误模式库/成功模式库/用户反馈档案/索引/能力雷达图）已从 `agent复盘/黄药师/daily_cognitive_review/` **移到拼音轨 `agent复盘/huangyaoshi/` 根**（中文旧轨 DEPRECATED，观察期至 08-26 归档）；Truman 复盘仍在 `agent复盘/huangyaoshi/daily-context/`
- **新机制**：① claim 处置门禁（#375：处置类任务缺"内容价值判断"节拒绝领取）② 提审 git 门禁（#363）③ 漂移巡检 check-runtime-drift（#364，schtasks KDO-Health-Check 每日 08:47）④ 启动指针 v2（.kdo/CAPSULE_STARTUP.md，git_head 校验）⑤ 派生物手改检测 check-derivatives（#369）
- **PARA 教训（最大）**：未消化≠不重要——处置类判断先问内容价值，默认保守保留。PARA 库（00_inbox/Handle the business 等 4 库）是核心资产，原位保留
- 待办：_tmp 23M 测试产物删除（等老朱过目）；PARA 未消化素材清单（AI数据第一课口述 02/03/闲聊）交王语嫣评估


> **用户说"继续"时**：按最小恢复路径读文件 → 3 分钟回到全链状态。
> **⚠️ 2026-08-15 修订**：恢复路径以「目录内最新」为准，不采信写死的日期/路径——本文件各节是快照，目录实际状态是真相。

## 最小恢复路径

| 优先级 | 文件 | 作用 |
|:--|:--|:--|
| P0 | `.agent/huangyaoshi-context.md` | 身份、行为牌组 B1-B6、启动步骤、铁律 0（提审即流转） |
| P0 | `agent复盘/huangyaoshi/daily-context/` **目录内最新文件**（当前 2026-08-16.md） | 最近一次完整复盘（含差异栏）——⚠️ 不要读本表写死的旧日期，以目录内最新为准 |
| P0 | `20_memory/` 本文件 | 关键状态速查 |
| P1 | `cap_hub/features.json` | KDO 20 Feature 注册表（含 FEISHU_DOC_MCP） |
| P1 | `kdo-tools/mcp/config.yaml` | MCP deployments 部署记录（谁挂在哪） |
| P1 | `90_control/domain-mapping.md` | 域清单单一真相源 |

## 2026-08-17 校准补充（恢复会话 B1 门禁实证）

### 视频号采集管线（proj_20260816_wechat-collect）状态
- **楚门两种方式已对齐顶层文档**（§零）：方式一偶遇（口述稿 L2612/L2648-2652 AI 超级入口）+ 方式二博主定向（L2622-2630）——`--scan-wechat` 对应方式一、`--author` 对应方式二
- **断链已修复**：collect_wechat.py 补 import shutil / 下载带 Referer / processed.log normcase 去重 / 成功才记录；wechat_knowledge.py 覆盖保护+跳过已知识化+NO_PROXY
- **🆕 全自动偶遇链路打通（方式一终态，2026-08-17 实测）**：
  - `wechat_link_monitor.py`：微信 4.x 数据库解密（密钥=段王爷 build_keys.py passphrase，19/19）→ 文件传输助手 ZSTD 解压 → 链接提取 → **ltaoo wx_channels_download parse_sph**（元宝 Cookie）→ 直链下载 → WSL GPU 转写 → LLM 三层次 → 全部落 `00_inbox/wechat-collect/`
  - 服务：`wx_video_download.exe`（API 127.0.0.1:2022，config.yaml `cloudflare.sphCookie` 已配全量 Cookie）
  - 计划任务：`wx-channels-download`（登录自启）+ `wechat-link-monitor`（每 10 分钟）
  - 元宝 Cookie 有效期约 1 个月，失效后：Edge 调试端口 9222 → `kdo-tools/_tmp_get_cookie.py` 重新提取（需用户在元宝页面扫码）
- **res-downloader**（MITM 嗅探）降级为播放兜底
- **待办**：small/large-v3 模型升级（tiny 够用但质量一般）；视频标题语义化（文件名是 hash）；KDO 侧接入 30_wiki 前的 ingest/validate 流程

### 2026-08-19 修复批次（偶遇采集 + inbox 监工）
- **链接规范化键去重**：公众号 `__biz+mid+idx`、头条 gid——修掉同一文章多分享链接重复采集（《重构协同》曾 3 份，已合并归档 duplicates-archive/）
- **文章知识化**：公众号/头条文章入库后自动走 LLM 三层次（洪七公 §五-1 闭环）
- **inbox 监工（watch_inbox.py）迁 Windows**：原 WSL cron 因 WSL 不常驻静默失效（08-17 23:50 后停了 2 天，洪七公交付汇总无人派发）→ 计划任务 `kdo-inbox-watch` 每 10 分钟；P2 项落 dispatch 文件（原只 print 无人消费）；排除 wechat-collect/
- **WSL cron 清仓（用户确认 WSL 无 agent 后）**：`kdo watch --health` → `kdo-health-daily`（每日 02:07，`run-kdo-health.cmd` 实测 PASS）；老顽童 state.db 备份 → `hermes-laowantong-backup`（每小时，`backup-hermes-state.ps1` 背 Windows 侧 profile，实测 PASS）；WSL crontab 已清空只留注释；`hermes-capsule-sync.timer` 已 disable（#366 FAIL 裁定方向——它曾在 3 分钟内把 CAPSULE_STARTUP v2 覆盖回 v1）
- **教训**：①Windows 迁移后任何"挂 WSL cron 的自动化"都要当作已失效排查——WSL 只在被调用时启动 ②.ps1 带中文必须存 UTF-8 BOM（PS 5.1 无 BOM 按 GBK 解析会吞字符，变量变空静默 skip）；.cmd 保持纯 ASCII ③**查清后续 commit 再定性**——我曾凭 #366 终审 FAIL 旧记录把 capsule_sync 当"v2 覆盖元凶"停用了它的 WSL 定时器，实际 08-19 01:33 commit 131815020 已做 v2 兼容改造并复审 PASS A；发现误判后立即 re-enable 恢复。FAIL 意见的"停用或升级"是二选一，升级已完成=风险已消除 ④**00_inbox 只增不删**（用户铁律 08-19 晚：方便用户去找）——我给重复文章做"合并归档"时把 2 个文件移出 inbox，被规则纠正后当场恢复；去重只能靠规范化键防新采，存量一律原地保留

### 2026-08-19 晚：检索索引门禁（L2+L3，用户拍板）
- **问题**：新卡入库不跑 `kdo index` = 检索不到（一盏神灯卡实证；graph 与 search_index 是两套分离索引，`graph rebuild` 不管后者）
- **L2 提审门禁**：`kdo pre-submit` 新增 `_check_index_freshness`——卡片 mtime > `.kdo/search_index.json` → ERROR 拦下。只检测不重建（毫秒级；全量重建分钟级，慢门禁会催生绕行）
- **L3 巡检**：`kdo watch --health` 新增第 7 项"检索索引滞后"（每日 02:07 kdo-health-daily 自动跑）——上线首日就抓到 13 张真实滞后卡
- **坑**：`_is_card()` 用 safe_read(limit=500) 截断长 frontmatter，规范卡反而误判非卡——门禁里改用"30_wiki/ 路径 + frontmatter 起始"判定（狗粮实测抓到）
- **KDO 源码改动未 commit**：`pre_submit.py` + `health_check.py`（pytest 15/15 过）——待用户/欧阳锋确认后提交
- **L1（治本，未做）**：SearchIndex 增量更新 + 入库路径自动挂索引——立项候选



> 08-16 晚重大事件：**全量 Windows 迁移启动**（洪七公断连生产事故 → 用户拍板"以后全量 Windows"）——codex 主导 T0-T4（#342-346）+ #347 洪七公迁移（已完成，用户确认成功）+ #348 R 型调研 Partner 部署（原黄药师→改派 codex，飞书真机冒烟 PASS）。我的日常复盘只覆盖 08-16 凌晨两次会话，迁移大事件由 codex/王语嫣推进，未参与。

### 队列真实状态（2026-08-17 B1 门禁）
- 总 328：queued=6 / claimed=0 / pending_review=2
- pending_review：#347（洪七公迁移，codex）+ #348（R 型部署，codex）——均等欧阳锋终审
- **我的任务：#345 T3（duanwangye 飞书 Windows 就绪测试）queued/挂起**——触发条件：等老顽童 CLI 工作完成 + 用户命令
- 迁移系列 #342/#343/#344/#346 均 ⏸ 挂起（同触发条件）
- hermes MCP 修复：venv 误装 mcp 2.0.0 → 降级 1.28.1（isError 兼容）；**8 个运行中 gateway 待重启加载**（重启时机等用户）
- kdo_search 178s 慢已修复（王语嫣 O-15：search_index.py 进程级缓存 + graph 缓存）



### 基建状态
- **周期表 Feature 工具链 v1.0 全就位**：`feature_menu.py`（kdo-tools/）——list/query(--layer/--dimension/--scenario/--keyword 别名命中)/pick/info/stale/combo/by-layer；数据源 `10_raw/sources/feature-periodic-table-v1.0.json`（100 Feature，47 卡 aliases，13 条三级证据，25 verified）；组合种子 `kdo-tools/feature_combos.json`（4 实测组合）；测试 `test_feature_menu.py` 28 断言
- **MCP 双 server 已接入 3 个飞书 agent**（教练/开会/基本功）：kdo 检索型 + feishu_doc 操作型——重启 gateway 后生效（WSL 侧）
- **任务模式已真机验证跑通**：老朱拆书作业五节流程完整（背景→出口式多轮→三支柱检索→第一人称成稿→待确认）

### 队列状态（2026-08-16 B1 门禁实证）
- 队列 304 任务：queued=4 / claimed=0 / pending_review=0——我的任务全清
- #323（GBK 修复）终审 PASS A-；#325（统一检索层）终审 **PASS A**（六层 O3 全过零瑕疵）
- #304/#303 C1 已闭环（双助理飞书可用）；#298 reviewed 无待办
- 在产（非我）：#319 O-14 domain 清扫（王语嫣）、#320-322 销售卡组（老顽童）

### 待办/条件项
- ~~KDO 工作区 24 处未提交改动~~ ✅ **2026-08-16 已 commit**（2 个主题 commit：7fa95c0 检索与索引基建修复 + 8bc5645 历史累积+GBK；工作区 0 残留；pytest 561 passed 1 历史失败）
- Windows 侧 5 profile（duanwangye/hongqigong/laowantong/wangyuyan/note-coach）已挂 kdo MCP——**gateway 重启后各发一条飞书消息验证检索生效**（欧阳锋提示）
- 停车场：P-31 ✅ 已解决（08-15 内存 16→32GB）、P-3 事实核对门（等裁定）、P-2 domain 加权（等 domain 污染清零）、P-29 队列编码修复（归并待排）
- P2-DYN-01（新 agent 模板固化 + health-check MCP 巡检）已登记，P2 立项时执行（欧阳锋审）
- 快照迁移 P3 未立项

### 关键教训（E020 等）
- **回答前先检索验证**（TCPR 定义错误教训——SOUL 写错 = 全错）
- **实测 > 推断**（Flash 强于 Pro 预览版——用户实测修正）
- **先确认对象身份**（小昭是 WorkBuddy 不是 Codex——搜错地方）
- **查源码确认机制存在**（Hermes smart_model_routing 无实现）
- **2026-08-15 新增：记忆体系自身也是快照**——恢复时以目录内最新为准，不信写死日期（欧阳锋同日独立收敛同一结论）

## 关键数字
- 全库 YAML 100%
- cap_hub 20 Feature（含 FEISHU_DOC_MCP）
- 3 agent 已接 MCP（kdo + feishu_doc）
