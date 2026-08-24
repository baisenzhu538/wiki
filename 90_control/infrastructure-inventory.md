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
| 工具族 | 20 | 🟢 | conveyor_probe/胶囊/采集/lint 工具（kdo-tools 核心） |
| 一次性修复批 | 28 | 🟡 | fix-*/repair-*（历史遗留待归档，#488 只标注不清理） |
| 服务 | 2 | 🟢 | hermes gateway（多实例）/ wx_video_download |
| 计划任务 | 5 | 🟢 | conveyor/l1-capture/inbox-watch/health-daily/health-check |
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
| pre_submit | 90_control/scripts/pre_submit.py | ⚠️ DEPRECATED（#377 收敛，新工作走 kdo pre-submit） | 黄药师 | 08-19 | KDO CLI pre_submit.py |
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
| conveyor_probe | kdo-tools/conveyor_probe.py | 传送带探针（六信号检出→登记→飞书通知，单扫描器纪律） | 08-23 六信号全通 | 计划任务 kdo-conveyor-probe/gate-blocked.log |
| memory_capsule | kdo-tools/memory_capsule.py | 记忆胶囊（L1 主库/镜像/verify/事件写入） | 08-24 verify PASS 9 行 | L1 库+D 盘镜像 |
| l1_capture | kdo-tools/l1_capture.py | L1 全量采集（日期增量目录+判重游标+每日 zip 归档复活 #508） | 08-25 8 例 passed | 计划任务 kdo-l1-capture/kdo-l1-archive |
| daily-context-save | kdo-tools/daily-context-save.py | 复盘保存（存档+review-check+L0 事件+镜像联动） | 08-23 🟢 A 级 | review-check/memory_capsule |
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
| collect_wechat / wechat_knowledge / wechat_link_monitor | kdo-tools/wechat_*.py | 视频号偶遇采集管线 | 08-17 全自动链路 | 计划任务 wechat-link-monitor |
| skill_crystallize / skill_lifecycle / distill-own-skill | kdo-tools/skill_*.py | 技能结晶/生命周期 | 按需 | skills |

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
- transcript-index — 口述稿索引
- transcript-registry — 口述稿注册
- web_fetch / web_search / collect_wechat / wechat_knowledge / wechat_link_monitor / wechat_promote — 采集检索族（§3 已列，解析别名）

**90_control/scripts 辅助族**：
- audit-kcard-baseline / card_review_checklist / changeset_audit / case-synthesis-check / bulk-generate-case-card — 卡质量辅助
- backup-sqlite / vault-backup / vault-snapshot — 备份与快照
- build_graph_index — 图索引构建
- check-yaml-related / check_dead_links / check_p0a_yaml / check_skill_cards — 链接/YAML 检查
- count_wiki_islands / cross_domain_audit / domain-decompression-audit / query-domain / scaffold-domain-index — 域辅助
- init_flywheel / init_zhu_personal_domain — 初始化
- kcard-diff-new-vs-existing / kcard-refinement-grader / kcard-simulate-feedback — 卡精修辅助
- normalize-tag-registry — 标签注册归一
- review_mark — 审查标记
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
| kdo-conveyor-probe | 每 10 分钟 | 探针扫描（队列/建议书/friction/gate-blocked→通知） | conveyor_probe |
| kdo-l1-capture | 每 30 分钟（:07/:37 错峰） | L1 全量采集+镜像+verify+体积红线 | l1_capture |
| kdo-inbox-watch | 每 10 分钟 | inbox 素材监工 | watch_inbox |
| kdo-health-daily | 每日 02:07 | 健康检查（9 项+标签健康） | health-check |
| KDO-Health-Check | 每日 08:47 | 健康检查计划任务（#364 漂移巡检） | health-check |
| wechat-link-monitor | 每 10 分钟 | 微信链接监测（偶遇采集） | wechat_link_monitor |
| kdo-daily-audit-digest | 每日 06:00 | 每日审计轮段①抽数（四原料→D 盘 digest） | daily-audit-digest |
| kdo-l1-archive | 每日 06:00 | L1 旧天日期目录 zip 归档（核验覆盖才删目录 #508） | l1_capture --archive |

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

## 8 · 一次性修复批（标记"历史遗留待归档"，#488 只标注不清理）

> 90_control/scripts/ 中 fix-*/repair_*/migrate-*/update_*/batch_* 等 28 个——多数为历史批次一次性脚本（YAML 修复/卡片修复/域迁移），**留存用于追溯，不推荐新使用**；清理另立项。

代表：backlink_fixer / batch_fix_mkt / bulk-fix-frontmatter / fix-card-metadata / fix-legacy-author-batch / fix-ocr-cards-batch / fix-yaml-errors-batch-v1-v3 / fix-yaml-list-issues / fix-yaml-quote-issues / fix_230_cards / fix_attacker / fix_body_short / fix_copy_paste / fix_frontmatter / fix_mkt_no_placeholder / fix_tool_sections / hermes_lint_batch1_repair / label-quality-migrate / migrate_domains / migrate_domains_v2 / normalize-tag-registry / ocr_deadlink_cleanup / purge-dead-source-refs / rebuild_229_cards / repair_double_aliases / repair_final_pass / tag-cleanup-phase2 / tag-cleanup-phase3 / update_related_44/47/49 / update_agent_specs_after_wave1 / clean-metadata-371 / fix_230_cards / fix_cb_ew / fix-yaml-errors-batch-v2/v3（含重复副本，归档时去重）

## 9 · 边界声明（#488 验收 5）

- 本表只记录资产状态+职责+关联，**不替代**：memory-registry（记忆真相源）、cap_hub（能力注册）、40_outputs README（工具登记）、domain-mapping（域清单）
- 本表不重复登记 KDO CLI 源码侧（Knowledge Delivery OS 0.0.1\kdo\，47 文件）——CLI 与 wiki 侧分工边界：**CLI=可安装命令体系（kdo query/lint/ship），wiki 侧脚本=工厂运行机制（门禁/探针/胶囊）**，CLI 侧登记见 KDO 仓库自身文档
- 存量一次性批只标注不清理；新组件必须登记（维护纪律）

---

*黄药师 · #488 首版 · 08-24 · 快照命令见 kdo-tools/infra-status.py*
