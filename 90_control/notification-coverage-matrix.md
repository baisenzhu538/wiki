# KDO 通知覆盖矩阵（基础设施总账 v1）

> 王语嫣 2026-08-26 建。缘起：老顽童建议书断言「终审落点无任何通知」，实际机制早已存在（#462/#521），
> 编排者无总账无法当场证伪——机制是二十多张单累积建成，碎片化记忆靠不住。
>
> **纪律**：凡新增/修改事件类型或通知通道的任务单，交付时必须同步更新本矩阵（验收项之一）。
> 王语嫣巡检照矩阵逐项核对，不再凭记忆。

## 事件 × 通道 × 角色

| # | 事件 | 检测源 | 通道 | 接收人 | 夜间静默口径 | 建设依据 |
|---|------|--------|------|--------|--------------|----------|
| 1 | 新 queued（可领取） | conveyor_probe `_queue_signal` | todos 推送 | assignee 路由（未知回落 laowantong） | 静默期 defer 天亮补发 | #501/#443 |
| 2 | 新提审（pending_review） | conveyor_probe | 叫醒推送 | 欧阳锋 | 豁免（终审类） | #421/#520 |
| 3 | 终审 PASS（reviewed） | conveyor_probe `new_reviewed`（#612：queue_transition review pass 终端输出附带提醒——交付物节含 30_wiki 卡片时提示「N 张交付卡待 review_mark 转正」；**#670 起该提醒降级为兜底网**——自动翻转钩子（行 31）识别不出交付卡写法时才触发，语义不变：只提醒不代写） | todos 推送 | assignee + 抄送王语嫣 | 豁免（终审类） | #462/#521 R1/R2；#612 转正提醒；#670 兜底化 |
| 4 | 终审退回 FAIL（failback） | conveyor_probe `new_failback` | todos 推送 | assignee 路由 | defer（未豁免，观察项 O1） | #462；#538 补「曾 reviewed」场景 |
| 5 | 门禁拦截（gate-blocked） | conveyor_probe `_scan_gate_blocked`（#562：时间戳锚定记录聚合——多行拦截消息（如 E040 交付物清单）续行并入首记录，不再按物理行切出垃圾残片；状态键 gate_seen_v2，旧行级方案升级首跑静默吸收存量防重报。#568：通知类打印一律改走 stderr——`--json` stdout 纯 JSON 可被机器 json.loads；queue_transition subprocess 全点强制 UTF-8/replace（GBK reader 线程崩溃族根治）；E040 fail-open 异常 stderr WARNING 可见化，门禁静默致盲→可见。#569：F-034 锚点改前缀匹配（`**改动文件清单**` 不再被闭合 ** 阻断）+E040 节边界放宽（`- **` 子弹行算字段行）+两门禁报错附期望格式样例——锚点容错不松语义） | 推送+看板登记 | 王语嫣 | — | #460；#562 多行解析修复；#568 GBK 族+stdout 污染根治；#569 锚点三层修复（#562/#568/#569 §3.19 三连合并补登 08-28）；#515 E040 `_tmp/` 划痕豁免（校准点1：`_extract_deliverable_paths` 提取层过滤中间产物非交付物，不判 missing/untracked，08-28 补登） |
| 6 | 建议书登记（三元组命中） | conveyor_probe `_scan_proposals` | 推送+PROPOSAL-PENDING 登记 | 王语嫣 | — | #421/#506 |
| 7 | 审查意见 🟠/🟡 无落点 | conveyor_probe F-036（#612：否定语境豁免——「不落/不构成/无」等前挂词紧邻的 emoji 不计入问题条目，🟠/🟡 连写对共享否定；报错文案附否定句写法提示。实证：#608「不落 🟠/🟡」被连拦两轮误伤） | 推送 | 欧阳锋 | 不豁免 | F-036 第七信号；#612 否定豁免 |
| 8 | near-miss 三元组违例 | conveyor_probe `_proposal_near_miss` + `_escalate_near_miss` | 仅日志 print + **≥3 轮未修正升级推王语嫣收件箱**（修正自动消项） | 王语嫣 | defer（非终审类） | ✅ #536 销项 |
| 9 | inbox 新素材 | watch_inbox `_notify_inbox`（#605：扫描面裁剪=00_inbox 顶层+pending-cards/ 白名单，Handle/_vlm_output/ocr_ingest 等大目录树出扫描面；dispatch 台账落盘停发下线——17 份零签收、职能并入看门狗 v5，看板登记+收件箱推送两通道不变。#619：白名单回补管线落点——#605 误裁 wechat-collect/video_transcripts/video_transcripts_small 出扫描面（05:47 六件漏登记实证），扫描面=顶层+SCAN_SUBDIRS 四目录白名单；白名单内 _ 前缀目录段与 wechat-collect/knowledge/（promote 中间产物，另有 pending-cards 落点）跳过防重复登记；EXCLUDE_DIRS 机制随白名单化移除） | 看板待编排区 + **王语嫣收件箱推送** | 王语嫣 | defer（P0 也静默落盘带 🔕） | ✅ #530 销项；#605 裁剪+台账停发；#619 落点回补 |
| 10 | friction 事件 | conveyor_probe `_scan_friction` | memory_capsule 事件层 | 复盘层可见 | — | #511 |
| 11 | 基础设施单 reviewed 总账未同步 | conveyor_probe `_matrix_sync_check`（第七信号） | 推送 | 欧阳锋+抄送王语嫣 | defer（非终审类） | #537（本单=元狗粮首查对象） |
| 12 | VLM/OCR 卡缺两段式隔离 | kdo pre-submit `_check_vlm_two_section`（#540） | pre-submit WARNING（提审输出可见） | 生产者 | — | #540（WARNING 起步，存量批次王语嫣裁定） |
| 12 | 终审改判（review --override，reviewed→queued） | queue_transition | 任务单改判记录节+台账（--reason 必填）+failback 通知 | 改判权=终审者专用 | — | #538（⚠️交付漏登，第七信号真阳性拦获，王语嫣 08-26 补登） |
| 13 | 检索结果低置信/冲突警告 | kdo_search 输出字段（confidence_flag/trust_level/conflict_warning）+标题后缀 | MCP 检索响应（消费 agent 可见） | 全体消费 agent | — | #541（trust 加权排序+conflict_with 警告，协议互链 consumer-retrieval-protocol） |
| 14 | source_refs 死引超基线 | check-source-refs（health-check 每日 02:07，--max-missing 1024/--max-contaminated 8 阈值制） | health-check FAIL + 报告落盘 60_feedback/analysis/source-refs-health-latest.{md,json} | 黄药师（治理）/王语嫣（阈值下调裁定） | — | #543（行号锚剥除+聚类治理报告；治理批次待王语嫣裁定） |
| 15 | 胶囊写入失败/只读自愈 | memory_capsule `log_event_safe`（#545：清只读属性自愈+退避重试+取证升级） | stderr + pending-git-commits.log（含 payload+db/wal/shm 属性快照） | 黄药师 | — | #545（readonly 复发 14 次根因取证：db 被外部置只读属性，置位者未抓到现行=环境性） |
| 16 | 产卡概念交叉验证 WARNING | kdo pre-submit `_check_concept_crosscheck`（#542：正文命中已有 concept/framework 概念词→提示对账，词表自动构建+mtime 缓存） | pre-submit WARNING（提审输出可见，不拦截） | 生产者 | — | #542（小昭事故根因 3 降档版：机器做存在性，人做正确性） |
| 17 | 终审权校验拒止（未登记实例 review） | queue_transition `_check_review_authority`（#546：cwd 无 ouyangfeng 登记 → 拒止；force 逃生落 force 台账） | 终端拒止提示 + gate-blocked 台账（第五探针可见） | 欧阳锋（登记一次即可） | — | #546（一具两职事件根治轻量版；登记表 .kdo/active-instances.json 供探针活性展示） |
| 18 | 基建停拍报警（l1-capture/conveyor/inbox-watch 停拍>2×周期） | conveyor_probe 第九信号 `_scan_infra_liveness`（10 分钟级，跨越沿幂等） | 推王语嫣 + gate-blocked.log 台账 | 王语嫣 | defer（夜间静默口径不动，台账恒写） | #547（console-killer 事件防复发；17h 延迟教训：health-check 日级太慢） |
| 19 | token 日计量汇总 | token_meter.py（挂 kdo-health-daily 02:07；三引擎增量游标，不回溯历史） | 日汇总落 60_feedback/analytics/token-usage-*.md/json + 事件层 token_usage | 黄药师/风清扬（#514 基线接口） | — | #549（只计量不限制；配额熔断属 F-055 阶段 2/3） |
| 20 | 角色时钟唤醒（【叫醒】） | role_clock.py（schtasks kdo-role-clock 5min；pace 到点/欧阳锋事件驱动）；**#565：载荷附 REVIEW-PENDING 明细（单号+挂起时长+阻塞谁，挂起>30min 升 🚨 加急）+ kimi-cli 门铃三层（会话级最小 cron 自装/SessionStart 钩注入自检/OS 级 kdo-huangyaoshi-doorbell 15min 兜底带活着跳过守卫）** | todos/<role>.md 恒落 + active 实例 feishu 适配；唤醒日志 .kdo/role-clock.log（不进胶囊——防 on_duty 自欺） | 全角色 | 不适用（唤醒本身就是在岗激活器） | #553+#555（四角色全开通；会话级 cron 已换轨停用；误发>漏发，降级不切执行权）；#565（落盘≠唤醒断点修复：门铃不做调度决策只按门铃，调度权仍归 role_clock） |
| 21 | 待老朱拍板上浮（reviewed + 拍板关键词） | conveyor_probe 第八信号 `_scan_pending_decision`（关键词前挂形态：老朱拍板/待老朱/需老朱/待拍板/需拍板/请老朱/待你拍板；向前生效 20260827 不回扫存量；队列侧只匹配备注列防名称列自举） | 新增即时推飞书 wangyuyan 群（老朱在群实测可达，本人 08-27 确认）+ todos 落盘 + daily-audit-digest ⑤「待你拍板」固定栏（每日在列直到字样移除/状态离开 reviewed 自动消项） | 老朱 | 无在岗 defer 同 #550 统一口径 | #556（#525 拍板断链两天实证；干跑校准：bare「拍板」命中已决归因→改前挂形态，「老朱已拍板」天然不匹配；消项不推送仅 stdout 留痕） |
| 22 | 角色全死自报（role-liveness） | role_registry `check_liveness`（挂 role_clock 5min；heartbeat 年龄 >2×该角色节奏=疑似死亡；**#562 起同角色 2h 报警冷却——只压频不删报、首次必报、恢复清零重新武装**；心跳写面=queue_transition 消费回执（myqueue/claim/complete/release/review）+ kimi-cli SessionHeartbeat 钩，消费回执=心跳） | gate-blocked.log 台账 → 第五探针拾取推送 | 王语嫣 | — | #552 信号上线（#562 前漏登矩阵，08-28 终审抄送补课）；#562 冷却+心跳语义修复（08-27 报警风暴 25+ 条误报止血） |
| 23 | 挂审超时必推（pending_review 最大年龄分级：30min 提醒 / 2h 升级） | check-review-sla.py（#574 R1：解析 REVIEW-PENDING 段活跃行取最大年龄，30min→推审查者 ouyangfeng webhook+todos 落盘；2h→升级推 ouyangfeng+wangyuyan 群（@ 负责人/老板，老朱在群可达）；复用 conveyor_probe._send_hook/_load_hooks/_append_role_todo 加签零新基建；`--dry-run` 只打印；通知类打印走 stderr） | 飞书 webhook + todos 落盘 | 欧阳锋（30min 提醒）/ 欧阳锋+王语嫣群（2h 升级 @ 老朱） | 豁免（终审类，超时必推不静默） | #574（#520 R3 升级：原只 print 无推送，2h 阈值从未触发过可见告警；落实 #521 R2 老朱「终审类通知不静默」） |
| 24 | vault backup 停拍（最后 backup commit 超 24h） | conveyor_probe 第十信号 `_scan_backup_stall`（git log --grep 心跳；跨越沿幂等，恢复重新武装；并入第九信号 infra_alerts 通道）+ 备份本体改系统级 schtasks kdo-vault-git-backup（30min，S4U，vault_git_backup.py） | gate-blocked.log 台账 + 推王语嫣（第九信号同通道） | 王语嫣 | defer（同第九信号口径，台账恒写） | #607（08-26 重启杀会话级 cron 致停摆 6 天空窗实证） |
| 25 | 伪逐字引文 + refs 区间漂移 | kdo pre-submit `_check_quote_verbatim`（引号块+L行号/「原话·口述」归因 → 剥空白标点逐字对源，不命中即报）+ `_check_source_range`（行号区间越界/全空白即报） | pre-submit WARNING（提审输出可见，不拦截） | 生产者 | — | #616（#614 补审实证：伪引文 3 张+区间漂移 5 张，欧阳锋建议书王语嫣裁定采纳；WARNING 档观察一周再定升阻断） |
| 26 | 编排骨架单翻转终审（assignee=ouyangfeng） | queue_transition `review --reviewer 王语嫣`（限编排骨架单，其余 reviewer/对象仍拒；终审权校验对称要求 cwd 有 wangyuyan 登记实例；F-035/F-036/台账留痕不变） | 终端+任务单终审记录+台账 | 王语嫣（翻转）/欧阳锋（主审） | — | #616 任务3（#544 手工翻转先例 + 09-02 #614 第二例，欧阳锋自己的单无人可终审的根治） |
| 27 | graph_index 空目录/0 records/陈旧超 48h | conveyor_probe 第十一信号 `_scan_graph_index_health`（空目录/缺失→报；graphml `<node` 字节扫描 0 节点→报；陈旧口径=graphml mtime 落后 search_index.json 超 48h——#356 双索引同步语义，规避手动重建节奏的绝对时间误报；沿触发幂等，恢复重新武装，原因切换重报；只告警不动作） | 并入第九信号 infra_alerts 通道：gate-blocked.log 台账 + 推王语嫣 | 王语嫣 | defer（同第九信号口径，台账恒写） | #622（08-31 事故清空 graph_index 语义腿空转 2 天无人发现；「修完没加哨兵=同类事故必再发」#357/#358 模式闭环） |
| 28 | 非节拍 backup commit（孤儿写手）+ 守卫跳拍误报停拍 | conveyor_probe 第十二信号 `_scan_offbeat_backup`（3h 窗内 `vault backup:` commit 距节拍格 :20/:50 超 ±10min → 报；沿触发幂等，全窗干净重新武装）+ 第十信号 `_scan_backup_stall` 口径细化（commit 超窗但守卫 SKIPPED 行在窗内 = #628 主动跳拍=健康，不报停拍；SKIPPED 也超窗则照报——守卫不能成停拍遮羞布） | 并入第九信号 infra_alerts 通道：gate-blocked.log 台账 + 推王语嫣 | 王语嫣 | defer（同第九信号口径，台账恒写） | #631（01:38 非节拍孤儿 commit 545bd0f5a 收走 #628 在制品；触发源锁定=obsidian-git 插件 auto backup 10min 同文模板，走自带 git 通道绕开 #628 守卫；信号上线真机首拍即现行：窗内 5 个非节拍 commit） |
| 29 | 产卡超长无分层段落（清单体结构缺失） | kdo pre-submit `_check_qingdanti_structure`（#639：连续散文化段落 ≥8 行 / 单段 ≥400 字 → 提醒按清单体标准重组，跳过代码围栏，只向前生效不回扫存量） | pre-submit WARNING（提审输出可见，不拦截） | 生产者 | — | #639（清单体方法论在库但生产规范零引用的知行断裂修复；规范层=工业化手册 §12.2.1，方法论锚 yt-note 卡族只链不抄） |
| 30 | 对话蒸馏每日运行结果 | conversation_distill（#645：计划任务 kdo-conversation-distill 每日 23:50 独立批次） | 无推送——落盘即交付：logs/conversation-distill-*.log + pending-cards 候选（走行 9 inbox 素材通道被王语嫣拾取过门禁）+ personal-os 追加；LLM 失败/锚校验丢弃计数写日志 | 王语嫣（经既有 inbox 通道）/ 黄药师（日志） | — | #645（老朱 09-05 长期机制；不新增推送通道，复用行 9 既有扫描面 pending-cards 白名单） |
| 31 | 终审 PASS 交付卡状态自动翻转 | queue_transition `_flip_delivered_cards`（#670：review --verdict pass 时按执行报告「交付物」节自动翻转交付卡 draft→reviewed+reviewed_by+review_date，三层解析兼容 #665/#666/#668 四种写法，只翻 draft 幂等护栏，识别不出降级行 3 的 #612 提醒不阻断；翻转卡随 chore(review) path-scoped 落仓，git 失败走 pending-git-commits.log 待收口） | 终端输出报告（翻转/未动/未识别三段）+ 卡 frontmatter + chore(review) commit | 欧阳锋（触发者=reviewed_by 归属）/生产者（零动作） | 不适用（终审同步动作，非通知） | #670（#612 提醒三次漏转复发 #586/#596/#666 的机制化根治；存量 33+7 张历史卡不代翻——reviewed_by 归属=审查者动作，清单 `60_feedback/diagnosis/working/audit-stuck-cards-20260907.md` 待欧阳锋核裁） |

## 缺口台账

- ~~**G1**：near-miss 只留日志不推送~~ → **已销项（2026-08-26 #536）**：≥3 轮未修正升级推王语嫣收件箱+修正自动消项+静默 defer 天亮补发，回归 4 例锁定
- ~~**G2**：inbox 素材检测到→只写看板~~ → **已销项（2026-08-26 #530，终审 PASS A）**：检测到即推王语嫣收件箱，幂等同 scan 判重键
- **O1（观察项）**：FAIL 退回通知夜间静默 defer 到天亮——FAIL 是「返工优先」却延迟送达，口径待裁（非阻塞，夜间本就不开工）。#535 已加收件箱置顶，推送层 defer 口径仍留本项

## 消费端纪律（机制送达 ≠ 被消费）

- 角色时钟扫描必须包含**自己的 todos 收件箱**，myqueue 只读视图不能替代（2026-08-26 老顽童实证：#531 终审通知躺收件箱 15 分钟未察觉）
- 通知类任务验收必须含「消费端知晓验证」：交付时向接收角色收件箱落一条使用说明，不只验发送端落盘（W 口径，随 #530/#535 起生效）
