---
id: infrastructure-inventory
title: 基建资产总表（识别靠表不靠记忆）
type: inventory
version: v1.0
created_at: '2026-08-24T01:00:00+08:00'
updated_at: '2026-08-24T01:00:00+08:00'
owner: 黄药师（基建单一实例）
audience: 全体 agent
---

# 基建资产总表（#488）

> 全厂基建资产地图：门禁/工具/服务/计划任务/数据资产/台账的"位置+职责+维护人+最近验证+关联+标记"。识别"基建有哪些、谁健康、哪里断、谁维护"查本表，不翻目录拼图。
> 分层定位：本表=资产状态视图；`memory-registry`=记忆真相源；`cap_hub`=能力注册；`40_outputs/code/scripts/README.md`=工具登记（存在）。四者并存不替代。
> **维护纪律（#488 任务4）**：新增基建组件必须登记入表（位置/职责/维护人/关联）；登记=纪律，未登记=不存在（与 README 同构）。维护人=黄药师（基建单一实例）。
> **改动走任务制（2026-08-24 用户拍板）**：本表及配套工具（infra-status.py 等）的任何改动必须**先入队再交付**（上板冻结纪律）；2026-08-24 覆盖对照补丁为唯一特例，下不为例（friction-log 已记）。

## 0 · 快速总览

| 域 | 数量 | 健康 | 说明 |
|:--|--:|:--|:--|
| 门禁/流转族 | 10 | 🟢 | queue_transition/queue_gate/audit/pre_submit/health-check 等 |
| 巡检/检查族 | 12 | 🟢 | check-*/scan-*（daily 自动） |
| 工具族 | 42 | 🟢 | conveyor_probe/胶囊/采集/lint/备份/拉起 工具（kdo-tools + 90_control/scripts 核心常驻，#627 补登记后重计） |
| 一次性修复批 | 28 | 🟡 | fix-*/repair-*（历史遗留待归档，#488 只标注不清理） |
| 服务 | 2 | 🟢 | hermes gateway（多实例）/ wx_video_download |
| 计划任务 | 13 | 🟢 | conveyor(×2)/inbox-watch(×2)/role-clock/l1-capture/l1-archive/health-daily/health-check/quality-metrics/daily-audit-digest/wechat-link-monitor/conversation-distill——**08-27 全部转 S4U 会话 0 无窗运行**（原 Interactive 每次触发弹黑框干扰桌面，老朱反馈后王语嫣转换+实跑验证 exit 0；今后新建计划任务硬纪律：LogonType 必须 S4U，禁 Interactive） |
| 数据资产 | 8 | 🟢 | L1 库+镜像+全量/索引/台账/基线 |
| 基线/轴文件 | 5 | 🟢 | tags-vocab 轴/role-routes/rescan-baseline 等 |

## 1 · 门禁/流转族（90_control/scripts/）

| 资产 | 位置 | 职责 | 维护人 | 最近验证 | 关联 |
|:--|:--|:--|:--|:--|:--|
| queue_transition | 90_control/scripts/queue_transition.py | 队列状态机（claim/complete/review/cancel/myqueue）+ 门禁家族（五字段/意见书/负向判词/处置结构化） | 黄药师 | 08-23 全量 78 passed | queue_gate/queue_lock/gate-blocked.log |
| queue_gate | 90_control/scripts/queue_gate.py | 队列解析唯一真相源（parse_queue/find_task/can_claim） | 黄药师 | 08-23 全链路 | queue_transition/audit/探针 |
| queue_lock | 90_control/scripts/queue_lock.py | 队列写锁（防并发流转） | 黄药师 | 08-18 | queue_transition |
| shared_file_guard | 90_control/scripts/shared_file_guard.py | 共享文件写前 stale 检测（#505：snapshot/verify 基线比对，STALE 报警退出 1） | 黄药师 | 08-25 7 例 passed | file-flow-protocol 增补件/conveyor_probe |
| audit_queue_integrity | 90_control/scripts/audit_queue_integrity.py | 队列完整性审计（#456 盲区修复后：解析 0→61 行） | 黄药师 | 08-23 PASS A- | queue_gate/queue_integrity_audit_latest.md |
| pre_submit | 90_control/scripts/pre_submit.py | ⚠️ DEPRECATED（#377 收敛，新工作走 kdo pre-submit） | 黄药师 | 08-19 | KDO CLI pre_submit.py（#517 新增正文 src_unknown 占位门禁：新卡 ERROR/存量 WARNING，08-25 起只向前生效；仓=`Knowledge Delivery OS 0.0.1`） |
| health-check | 90_control/scripts/health-check.py | 健康检查统一入口（9 项：lint/source_refs/VLM/生产/配置/MCP/漂移/派生/复扫/标签健康） | 黄药师 | 08-23 每日自动 | check-* 族/计划任务 kdo-health-daily |
| kcard-quality-gate | 90_control/scripts/kcard-quality-gate.py | 卡片质量门（内容/结构） | 黄药师 | 08-16 | kdo validate |
| full-library-rescan | 90_control/scripts/full-library-rescan.py | 全库复扫（#399 归零声明唯一口径） | 黄药师 | 08-21 PASS A | rescan-baseline.json |
| kdo_lint / kdo_validate | 90_control/scripts/kdo_lint.py, kdo_validate.py | lint/validate（wiki 侧独立实现） | 黄药师 | 08-16 | KDO CLI lint |
| queue-archive | kdo-tools/queue-archive.py | 队列归档瘦身（#453） | 王语嫣执行 | 08-23 PASS A- | production-queue.md |

## 2 · 巡检/检查族（90_control/scripts/check-*）

| 资产 | 职责 | 最近验证 |
|:--|:--|:--|
| check-source-refs | source_refs 健康 | 每日 |
| check-mcp-roaming | MCP 挂载巡检（#326） | 08-16 17/17 |
| check-runtime-drift | 运行时漂移（#364） | 每日 |
| check-derivatives | 派生副本手改检测（#369） | 每日 |
| check-draft-aging | 存量 draft 超龄（#380） | 每日 |
| check-tags-health | 标签健康 5 指标（#474/#484） | 08-24 污染率 0.66% 达标 |
| check-agent-config | Agent 配置自检 | 每日 |
| scan-vlm-parse-errors | VLM 描述质量 | 每日 |
| track-production-progress | 生产进度 | 每日 |
| audit-kcard-baseline / changeset_audit / card_review_checklist 等 | 卡质量辅助审计 | 按需 |

## 3 · 工具族（kdo-tools/，核心常驻）

| 资产 | 位置 | 职责 | 最近验证 | 关联 |
|:--|:--|:--|:--|:--|
| conveyor_probe | kdo-tools/conveyor_probe.py | 传送带探针（六信号检出→登记→飞书通知，单扫描器纪律） | 08-25 #519 修复后计划触发实跑 PASS | 计划任务 kdo-conveyor-probe/gate-blocked.log |
| check-conveyor-state | 90_control/scripts/check-conveyor-state.py | 探针空转报警（#519：state 年龄>2×周期→exit 1，health-check 带动） | 08-25 5 例 passed | health-check/.kdo/conveyor_state.json |
| check-review-sla | 90_control/scripts/check-review-sla.py | 审查 SLA 超时必推（#574 R1：REVIEW-PENDING 最大年龄 30min→提醒/2h→升级，复用 conveyor 加签+todos 落盘） | 08-29 7 例 passed | health-check/production-queue.md |
| quality_metrics | kdo-tools/quality_metrics.py | 质量指标基线周报（#514：FAIL率/打回率/拦截率/误判率代理，口径=quality-metrics-spec-v1） | 08-25 7 例 passed | 计划任务 kdo-quality-metrics/60_feedback/auto/quality-metrics |
| check-depended-draft | 90_control/scripts/check-depended-draft.py | 被依赖卡 draft 门禁（#527：引用面三路识别含 glob 数据链；baseline 存量 WARNING/新引用 ERROR） | 08-25 8 例 passed | health-check/quality-gates/depended-draft-baseline.json |
| island_scan | kdo-tools/island_scan.py | 孤岛卡扫描（#528：双无卡清单 json+md 按域分组，WARNING 制不拦流转） | 08-26 4 例 passed | health-check/60_feedback/auto/island-cards |
| check-vlm-two-section | 90_control/scripts/check-vlm-two-section.py | VLM/OCR 卡两段式存量扫描（#540：合规计数+缺隔离清单） | 08-26 2 例 passed | health-check/schemas/vlm-two-section.md |
| scan_skills_registry | 40_outputs/code/scripts/scan_skills_registry.py | Skill 目录+挂载矩阵扫描生成（#588：INDEX.md + MOUNT-MATRIX.md 生成物；--check 新鲜度门禁 stale→exit 1；登记制=文件引用即挂载） | 09-01 73/73 fresh | infra-status skills-registry 行；登记维护归 Skills 助理（#587 分工表） |
| conversation_distill | kdo-tools/conversation_distill.py + kdo-conversation-distill.cmd/.xml | 对话蒸馏管线（#645 老朱 09-05 长期机制：kimi wire/headless/hermes 三源抽取→三层分流蒸馏 external→pending-cards / zhu→personal-os / human→pending-cards；增量游标 .kdo/conversation_distill_state.json；原文锚红线=quote 子串强校验，不过即弃） | 09-05 试跑 09-02~05 出三类样本 | 计划任务 kdo-conversation-distill/矩阵行 30/zhu-conversation-insights.md |
| pre_review | 90_control/scripts/pre_review.py | 机器预审管线（#515：差集/lint/负向判词/存在性核查四判据，报告随提审附任务单，参考层不放行不拦截） | 08-26 6 例 passed | queue_transition complete 内嵌调用 |
| token_meter | kdo-tools/token_meter.py | 全厂 token 计量（#549：claude/kimi jsonl 偏移增量 + hermes state.db 会话差值 → 日汇总落 60_feedback/analytics/ + 事件层 token_usage；不回溯历史，首日引导只计当日） | 08-27 7 例 passed | 挂 kdo-health-daily（02:07）/60_feedback/analytics/token-usage-*.md |
| on_duty | kdo-tools/on_duty.py | 在岗判定共享模块（#550：事件库近30min非机器事件 OR L1 当日新文件 → 在岗；双信号不可得默认激活；conveyor_probe/watch_inbox 同一判定源） | 08-27 6 例 passed | conveyor_probe/watch_inbox 通知静默判定 |
| role_registry | 90_control/scripts/role_registry.py + 90_control/role-registry.json | 角色活性注册表+心跳写钩（#552，#525 四拆之一：heartbeat/status/check-liveness；myqueue 蹭拍写钩；全死→gate-blocked 自报） | 08-27 5 例 passed + 狗粮实跑 | queue_transition myqueue 钩/on_duty 心跳优先判定 |
| kdo_session_heartbeat_hook | kdo-tools/kdo_session_heartbeat_hook.py + 90_control/session-roles.json | kimi-cli SessionHeartbeat 钩（#562 任务2：会话活跃=心跳——session_id→state.json title 解析角色→role_registry 蹭拍，补「会话内活跃未跑 kdo 命令」活性盲区；fail-open 静默） | 08-28 3 例 passed + 本会话活体心跳实测 | ~/.kimi-code/config.toml `[hooks]` SessionHeartbeat/role_registry |
| kdo_doorbell_guard | kdo-tools/kdo_doorbell_guard.py + kdo-tools/kdo-doorbell.cmd | OS 级门铃+守卫（#565：schtasks kdo-huangyaoshi-doorbell 15min 唤起 `kimi -c -p` 续会话施工；守卫=注册表 cli 心跳 <10min 则跳过——活着的会话不抢活，防平行工班；fail-open 读不出=放行） | 08-28 4 例 passed + 活体三连拍实证（#563/#564 两单门铃工班自主闭环） | 计划任务 kdo-huangyaoshi-doorbell/role_registry |
| kdo_session_boot_hook | kdo-tools/kdo_session_boot_hook.py | kimi-cli SessionStart 钩（#565：会话启动/恢复注入门铃自检指令进上下文——会话级 cron 随会话死，新会话自装；cwd=wiki 仓才注入，fail-open 静默） | 08-28 单测覆盖（wiki 注入/非 wiki 静默两路） | ~/.kimi-code/config.toml `[hooks]` SessionStart/.agent/startup.md 第0步（双保险） |
| role_clock | kdo-tools/role_clock.py + kdo-role-clock.cmd | 角色心跳调度器（#553，#525 四拆之二：pace 到点/欧阳锋事件驱动唤醒→todos 恒落+feishu 适配；唤醒日志 .kdo/role-clock.log 不进胶囊——防 on_duty 自欺） | 08-27 5 例 passed + 活体唤醒老顽童实测 | 计划任务 kdo-role-clock（5min）/90_control/todos/ |
| build_seed / seed-check | kdo-tools/build_seed.py, kdo-tools/seed-check.py | kdo-seed 种子包构建+装机自检（#532：机制层搬迁，KDO_ROOT 参数化） | 08-26 5 例 passed | 90_control/kdo-seed/BOOTSTRAP.md |
| tech_inventory | kdo-tools/tech_inventory.py | 技术域存量盘点三堆清单（#533：可审/返工/废弃，接管第一步） | 08-26 4 例 passed | 90_control/schemas/tech-domain-skeleton.md |
| memory_capsule | kdo-tools/memory_capsule.py | 记忆胶囊（L1 主库/镜像/verify/事件写入+log_event_safe 四类事件统一入口 #511） | 08-25 6 例 passed | L1 库+D 盘镜像 |
| l1_capture | kdo-tools/l1_capture.py | L1 全量采集（日期增量目录+判重游标+每日 zip 归档复活 #508） | 08-25 8 例 passed | 计划任务 kdo-l1-capture/kdo-l1-archive |
| daily-context-save | kdo-tools/daily-context-save.py | 复盘保存（存档+review-check+L0 事件+镜像联动；#512 重打改覆盖写+事件去重） | 08-25 4 例 passed | review-check/memory_capsule |
| review-check | kdo-tools/review-check.py | 复盘探测器（11 章判级+失败项明细 #478） | 08-23 PASS A- | daily-context-save |
| file-flow-check | kdo-tools/file-flow-check.py | 文件流转规范 lint（L1-L9 无状态冻结检测 #473） | 08-23 PASS A- | frozen 动态清单/git HEAD |
| tags-audit | kdo-tools/tags-audit.py | 标签体检 5 指标（脏词/来源轴/域地图/空值/来源形态词） | 08-24 2876 卡 5.9s | check-tags-health |
| queue_batch_accept | kdo-tools/queue_batch_accept.py | 批次验收四步一体（re.subn 断言禁静默 #479/#482） | 08-24 PASS A- | #426 批次线 |
| daily-audit-digest | kdo-tools/daily-audit-digest.py | 每日审计轮段①抽数（#507：胶囊事件/daily-context/friction/队列四原料→D 盘 digest，零 LLM token） | 08-25 增量双向验证 | 计划任务 kdo-daily-audit-digest/D:\KDO-memory\L2-digest |
| watch_inbox | kdo-tools/watch_inbox.py | inbox 监工（素材→编排登记） | 08-19 迁移 Windows | 计划任务 kdo-inbox-watch |
| skill_bridge_sync | kdo-tools/skill_bridge_sync.py | 双轨 skill 桥接同步（#267） | 08-16 | .claude/skills |
| feature_menu | kdo-tools/feature_menu.py | Feature 周期表查询 | 08-16 | cap_hub |
| flywheel | kdo-tools/flywheel.py | Y 模型认知迭代引擎 | 08-16 | 复盘 |
| remove-task-docid | kdo-tools/remove-task-docid.py | 任务单 doc_id 移除（#477） | 08-23 17 份 PASS A- | file-flow-check L9 |
| generate-dashboard | kdo-tools/generate-dashboard.py | 看板生成（队列→dashboard） | 08-23 流转自动 | production-queue.md |
| queue_audit / hook_queue_audit | kdo-tools/queue_audit.py | 队列审计辅助 | 08-16 | queue_gate |
| web_search / web_fetch | kdo-tools/web_search.py | 联网检索（研究用） | 按需 | research 系 |
| collect_wechat / wechat_knowledge / wechat_link_monitor / wechat_promote | kdo-tools/wechat_*.py | 视频号偶遇采集管线+转正（#516 去重键补 _processed 隔离区含 regen 变体） | 08-25 4 例 passed | 计划任务 wechat-link-monitor |
| daily_review | kdo-tools/daily_review.py + kdo-daily-review.cmd + kdo-daily-review.xml | 每日复盘定期任务化（#623 老朱 09-02 直令：三角色 headless Truman 复盘拉起+空班豁免 F-062；指令模板内嵌、禁编造诚实空班） | 09-03 首跑三实例拉起 rc=0 | 计划任务 kdo-daily-review（每日 23:37 S4U）/kimi-headless-launch/daily-context-save |
| skill_crystallize / skill_lifecycle / distill-own-skill | kdo-tools/skill_*.py | 技能结晶/生命周期 | 按需 | skills |
| vault_git_backup | kdo-tools/vault_git_backup.py | vault git 快照备份（#607：系统级 schtasks 30min 节拍，全树变更才 commit；替代会话级 cron；#625 门禁第二层——>100MB 移出暂存硬拦、>15MB WARNING 台账） | 09-03 00:20/00:50/01:20 三拍连实（logs/vault-git-backup.log） | 计划任务 kdo-vault-git-backup/90_control/large-file-gate.log（未触发=无记录） |
| vault-integrity-check | 90_control/scripts/vault-integrity-check.py | vault 完整性自检（#592 R3：工作树+bundle mtime/verify+异机副本三查；异常→gate-blocked #472 格式） | 09-02 亲跑三查 OK exit 0；挂 kdo-health-daily 每日 02:07 | gate-blocked.log/run-kdo-health.cmd/计划任务 kdo-wiki-bundle-backup |
| graph-index-coverage-probe | 90_control/scripts/graph-index-coverage-probe.py | graph 索引覆盖率探针（#671：30_wiki 各子目录卡数 vs graph_state path_map 逐目录对照，复用构建脚本同一收集逻辑不漂移；缺口>0 → gate-blocked 报警；标题撞车丢溯源映射同拦；心跳 logs/graph-index-coverage.log） | 09-07 03:05 首跑捕获 dk 族 332/332 闭环+13 张历史标题撞车卡【实证】；挂 kdo-health-daily 每日 02:07 | gate-blocked.log/run-kdo-health.cmd/日志 headless-dk-graph-rebuild-20260907.log |
| wiki-vault-restore | 90_control/scripts/wiki-vault-restore.py | 恢复演练脚本（#592 R2：bundle verify→clone→文件数+HEAD+git status 对照；只读源 vault） | 09-01 演练 24,896 文件恢复 dirty=0 | D:\KDO-memory\wiki-bundle-*.bundle/计划任务 kdo-wiki-bundle-backup |
| clock_watchdog | 90_control/scripts/clock_watchdog.py | 王语嫣值守 no_agent 看门狗（2026-09-01 老朱拍板选①：无事 SILENT exit 0/有事飞书简报/崩溃非 0；只探测不决策，只叫王语嫣） | 09-02 00:12 state 末拍 | 王语嫣时钟（Hermes no_agent 契约）/clock-watchdog-state.json、clock-watchdog-skip.json |
| kimi-headless-launch | 90_control/scripts/kimi-headless-launch.py | 角色无头拉起器（09-02 老朱直令：王语嫣时钟唯一→拉起角色施工；工具=变量 TOOLS 表登记；DETACHED 后台+logs/headless-&lt;role&gt;-&lt;ts&gt;.log） | 09-03 01:09~01:13 三实例拉起实证（logs/headless-*） | daily_review/计划任务 kdo-daily-review/role-registry |

## 3b · 辅助工具族（#488 登记纪律存量补登记，按族）

> 核心常驻见 §3；本族为辅助/按需工具（存在性登记，维护人=黄药师；职责见各自 docstring）。

**kdo-tools 辅助族**：
- agent-activity-check — Agent 活跃度检查
- agent-prompt-compiler — Agent prompt 编译
- agent-status — Agent 状态
- agent-trace — Agent trace 回放
- aesthetic-library-builder — 审美库构建
- audit-review-integrity — 审查完整性审计
- canvas-agent — 画布 Agent
- card-reader — 卡读取
- decision_add — 决策录入
- dedup_sources — 素材去重
- douyin_cookie_extract — 抖音 Cookie 提取
- douyin_user_videos — 抖音用户视频
- flywheel-export — Y 模型导出
- hermes-profile-guard — Hermes profile 防护
- infra-status — 基建健康快照（#488）
- recovery-check — 事件库恢复副本验证（健壮性 L5 自动化）
- mcp-reachability-check — MCP 可达性
- research_adapter — 调研适配
- scan-demo-sections — demo 节扫描
- scan-profit-demo-sections — 利润 demo 节扫描
- scan-ppt-gaps — PPT 缺口扫描
- sync-hermes-mcp — MCP 配置渲染同步（#326 单一真相源）
- test_feature_menu — Feature 菜单测试
- test_wechat_knowledge_smoke — wechat 管线 smoke 最小护栏（#585，skip 前置/骨架标记/#380 拦截 6 断言）
- transcript-index — 口述稿索引
- transcript-registry — 口述稿注册
- web_fetch / web_search / collect_wechat / wechat_knowledge / wechat_link_monitor / wechat_promote — 采集检索族（§3 已列，解析别名）
- transcribe_win — Windows 原生转写（faster-whisper-tiny，wechat-collect 管线 08-31 WSL 迁出——wsl.exe 僵死曾卡 180s+）

**90_control/scripts 辅助族**：
- audit-kcard-baseline / card_review_checklist / changeset_audit / case-synthesis-check / bulk-generate-case-card — 卡质量辅助
- backup-sqlite / vault-backup / vault-snapshot — 备份与快照
- build_graph_index — 图索引构建
- check-yaml-related / check_dead_links / check_p0a_yaml / check_skill_cards — 链接/YAML 检查
- count_wiki_islands / cross_domain_audit / domain-decompression-audit / query-domain / scaffold-domain-index — 域辅助
- init_flywheel / init_zhu_personal_domain — 初始化
- kcard-diff-new-vs-existing / kcard-refinement-grader / kcard-simulate-feedback — 卡精修辅助
- normalize-tag-registry — 标签注册归一
- review_mark — 审查标记（#670 起翻转核心 mark_card() 由 queue_transition 终审 PASS 钩子复用；CLI 保留为存量卡人工批收口入口）
- rule-gate-inventory — 规则门禁盘点
- run_agent_spec_tests / run_v11_retests — spec 测试
- source-id-registry — 源 ID 注册
- stage4-trust-layer-audit / stage4-trust-layer-fix — 信任层审计
- summarize-agent-contexts — Agent context 摘要

## 4 · 服务

| 服务 | 位置 | 职责 | 健康 |
|:--|:--|:--|:--|
| hermes gateway（多 profile） | WSL systemd + Windows 原生 | 飞书 Agent 网关（教练/开会/基本功/R 型等） | 🟢 08-23 多实例 running |
| wx_video_download | Windows 服务（API 127.0.0.1:2022） | 视频号直链下载 | 🟢 08-17 |

## 5 · 计划任务（Windows schtasks）

| 任务 | 频率 | 职责 | 关联 |
|:--|:--|:--|:--|
| kdo-conveyor-probe | 每 10 分钟 | 探针扫描（队列/建议书/friction/gate-blocked→通知） | conveyor_probe（#519：TR 改 kdo-conveyor-probe.cmd 包装——嵌套引号 TR 被 cmd 剥壳静默失败 15h 根治） |
| kdo-l1-capture | 每 30 分钟（:07/:37 错峰） | L1 全量采集+镜像+verify+体积红线 | l1_capture |
| kdo-inbox-watch | 每 10 分钟 | inbox 素材监工 | watch_inbox |
| kdo-health-daily | 每日 02:07 | 健康检查（9 项+标签健康） | health-check |
| KDO-Health-Check | 每日 08:47 | 健康检查计划任务（#364 漂移巡检） | health-check |
| wechat-link-monitor | 每 10 分钟 | 微信链接监测（偶遇采集） | wechat_link_monitor |
| datapacks 库 | 按需 | 厂级领域弹药库（金标准/踩坑/对照数据；#660/#661 双试点 PASS） | 40_outputs/capabilities/datapacks/ |
| channel-model-map + channel_health | 每次拉起预检 | 通道-真实供应商台账+健康预检 fallback（#656 PASS A-） | 90_control/channel-model-map.md + scripts/channel_health.py |
| kdo-daily-audit-digest | 每日 06:00 | 每日审计轮段①抽数（四原料→D 盘 digest） | daily-audit-digest |
| kdo-l1-archive | 每日 06:00 | L1 旧天日期目录 zip 归档（核验覆盖才删目录 #508） | l1_capture --archive |
| kdo-quality-metrics | 每周一 06:35 | 质量指标周报（上周一~周日，#514 阶段 0 纯统计） | quality_metrics |
| kdo-daily-review | 每日 23:37 | 四主力每日复盘计划任务化（#623：三角色 headless 复盘拉起+空班豁免 F-062；与 backup 30min 节拍错开；S4U 无窗硬纪律） | daily_review（经 kimi-headless-launch 拉起；laowantong/huangyaoshi/ouyangfeng） |
| kdo-conversation-distill | 每日 23:50 | 对话蒸馏每日增量批次（#645 老朱 09-05 长期机制：三层分流+原文锚红线；S4U 无窗；与 daily-review 23:37 错开） | conversation_distill（kdo-conversation-distill.cmd 包装） |
| kdo-wiki-bundle-backup | 每日 02:30（**周一=全量 bundle**，非周一 skip-only；09-05 老朱改：日全量 2GB/天×2盘 C盘95%） | wiki vault git bundle 备份（rolling 2+obsidian 快照+周一后异机副本；日志 D:\KDO-memory\wiki-bundle-daily.log） | wiki-bundle-backup.bat #589/#673 |

**L1 断流判读口径（#513 落档，08-25 黄药师核查闭环）**：判读某源「断流」前必须三对照——①该源 sessions 存储目录在窗口期是否有 mtime 活动（无活动=正常空转，非断流）；②检查时刻距会话启动是否 <30min 采集节拍（节拍内未采到属正常滞后）；③kdo-l1-capture 各拍是否在 `90_control/l1-size.log` 连续在跑。kimi 源实证：CLI 活跃期间 wire.jsonl/state.json/logs 实时写盘（非退出才写），采集路径 `~/.kimi-code` 全目录覆盖 sessions/ 无缺口；08-24「7.5h 断流」实为无活动窗口+节拍内检查的复合误判（zip 内 workspaces.json=23:39 版本实证 00:07 拍已采到）。

**bundle「过期/停摆」判读口径（#673 落档，09-07 黄药师核查闭环）**：判读 bundle 备份停摆前必须三对照——①`D:\KDO-memory\wiki-bundle-daily.log` 尾部有无当日 02:30 运行行（任务**每日**都跑：周一产 bundle，非周一合法 skip-only 不产 bundle）；②schtasks 上次结果是否 0；③`wiki-bundle-daily.last-result.txt` 是否 OK。已知故障族两条：**09-07「47.6h 过期」误报**——09-05 老朱改周节拍（周一 full bundle）后 vault-integrity-check 的 26h 阈值未同步，每周一 02:07 探针必然误报（02:07 探针在 02:30 拍前，bundle 龄恰 47.6h）；已改双层阈值（日志活性 26h+bundle 新鲜度 180h，停摆检测不降级）。**待办疑点**：bat 头注释写「Obsidian snapshot 仍每日跑」，实际 obsidian 快照代码在 `goto :daily_only` 之后仅周一执行（08-31 事故的盲点修复被周节拍静默削弱）——#673 边界外，待老朱拍板补日拍或改注释。

## 6 · 数据资产

| 资产 | 位置 | 职责 | 健康 |
|:--|:--|:--|:--|
| L1 事件主库 | C:\Users\Administrator\.kdo-memory\L1\activity_log.db | 记忆胶囊事件指针层（WAL） | 🟢 9 行 integrity ok |
| L1 镜像 | D:\KDO-memory\L1-backup | 主库镜像（robocopy /MIR） | 🟢 verify PASS |
| L1 全量原文 | D:\KDO-memory\L1-full + C 盘镜像 | 甲类会话原文+乙类 trace | 🟢 7315 文件 762MB |
| search_index | .kdo/search_index.json | 检索索引（kdo query BM25） | 🟢 #327 修复后 |
| graph 索引 | .kdo/（graph rebuild） | 图检索 | 🟢 08-16 |
| gate-blocked.log / gate-blocked-test.log | 90_control/ | 门禁拦截机器自报（#460/#483 分流） | 🟢 探针第五探针 |
| force-exceptions.log | 90_control/ | force 例外台账（#444） | 🟢 |
| cancel-ledger.log / l1-size.log | 90_control/ | cancel 台账/体积日志 | 🟢 |

## 7 · 基线/轴文件

| 资产 | 位置 | 职责 |
|:--|:--|:--|
| role-routes | 90_control/role-routes.md | 角色路由层（技能/知识路由，#472） |
| tags-vocab 轴 | 90_control/tags-vocab/*.yaml | 域词池轴（decision-making v0.1 等，#426） |
| tags-vocab-design | 90_control/tags-vocab-design.md | 词表设计（v0.3 双原则） |
| rescan-baseline | 90_control/baseline/rescan-baseline.json | 全库复扫基线（#399） |
| CAPSULE_STARTUP | .kdo/CAPSULE_STARTUP.md | 唯一启动指针（git_head/queue_tail 校验） |
| role-clock-architecture | 90_control/role-clock-architecture.md | 角色级时钟与探针架构设计 v1（#525：工具是变量角色是恒量；注册表/调度器/唤醒语义统一层/接入契约/切换剧本） |
| quality-metrics-spec | 90_control/quality-metrics-spec-v1.md | 质量指标口径裁决稿（#514 施工依据，王语嫣 v1） |

## 8 · 一次性修复批（标记"历史遗留待归档"，#488 只标注不清理）

> 90_control/scripts/ 中 fix-*/repair_*/migrate-*/update_*/batch_* 等 28 个——多数为历史批次一次性脚本（YAML 修复/卡片修复/域迁移），**留存用于追溯，不推荐新使用**；清理另立项。

代表：backlink_fixer / batch_fix_mkt / bulk-fix-frontmatter / fix-card-metadata / fix-legacy-author-batch / fix-ocr-cards-batch / fix-yaml-errors-batch-v1-v3 / fix-yaml-list-issues / fix-yaml-quote-issues / fix_230_cards / fix_attacker / fix_body_short / fix_copy_paste / fix_frontmatter / fix_mkt_no_placeholder / fix_tool_sections / hermes_lint_batch1_repair / label-quality-migrate / migrate_domains / migrate_domains_v2 / normalize-tag-registry / ocr_deadlink_cleanup / purge-dead-source-refs / rebuild_229_cards / repair_double_aliases / repair_final_pass / tag-cleanup-phase2 / tag-cleanup-phase3 / update_related_44/47/49 / update_agent_specs_after_wave1 / clean-metadata-371 / fix_230_cards / fix_cb_ew / fix-yaml-errors-batch-v2/v3（含重复副本，归档时去重）

## 9 · 边界声明（#488 验收 5）

- 本表只记录资产状态+职责+关联，**不替代**：memory-registry（记忆真相源）、cap_hub（能力注册）、40_outputs README（工具登记）、domain-mapping（域清单）
- 本表不重复登记 KDO CLI 源码侧（Knowledge Delivery OS 0.0.1\kdo\，47 文件）——CLI 与 wiki 侧分工边界：**CLI=可安装命令体系（kdo query/lint/ship），wiki 侧脚本=工厂运行机制（门禁/探针/胶囊）**，CLI 侧登记见 KDO 仓库自身文档
- 存量一次性批只标注不清理；新组件必须登记（维护纪律）

---

*黄药师 · #488 首版 · 08-24 · 快照命令见 kdo-tools/infra-status.py*
