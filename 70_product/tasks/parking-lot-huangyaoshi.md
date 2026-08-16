---
id: parking-lot-huangyaoshi
type: parking_lot
created_at: 2026-06-28
updated_at: 2026-08-08
owner: 黄药师
---

# 黄药师停车场清单

> **停车场机制**：主线任务进行中，把不阻塞当前主线的洞察、改进点、待讨论方案记录在此。等空下来再和大家讨论/排期。
> **升级路径**：`待讨论` → `待排期` → 进入 `70_product/tasks/production-queue.md` → 分配执行。
> **清理规则**：每月清理一次，超过 30 天未动的 P1/P2 任务强制 review，长期不做的标记 `已拒绝`。

---

## 当前停车场（仅保留待讨论/等依赖项）

| # | 任务 | 来源 | 优先级 | 工作量 | 状态 | 阻塞/依赖 |
|:--:|:---|:---|:---:|:---:|:---:|:---|
| P-2 | **domain 自动加权**：Agent 已知当前工作域，`kdo query` 自动加权同域结果 | 用户 2026-06-20 | P1 | 1d | 待排期 | domain 污染清零（欧阳锋/王语嫣进行中） |
| P-3 | **卡片语义去重**：全库 2100+ 卡，需近重复检测→合并建议 | 用户 2026-06-20 | P2 | 2-3d | 待讨论 | 无 |
| P-4 | **过期检测**：`freshness: stale` 卡降权+标注"可能过时" | 用户 2026-06-20 | P2 | 1d | 待讨论 | 无 |
| P-5 | **多库架构设计**：四库拓扑（商业+人 / 电子+软件 / 结构工程 / 平面设计+推广）。调度中枢王语嫣（跨库 dashboard/production-queue）+ 欧阳锋质量终审 + 子库精简配置 + 启动序列 + Agent 分拆。2026-06-27 角色调整已反映 | 用户 2026-06-20 / 更新 2026-06-28 | P2 | 待定 | 待讨论 | 需用户/王语嫣讨论四库拓扑 |
| P-23 | **能力中台 Phase 1**：VLM 能力上线——建 `_capability_hub/` 骨架（registry + base + config）+ VLM 核心模块。**核心交付：统一入口 `python -m capability_hub list`**——任何新 Agent 启动时跑这条命令，看到三层：① 可调用的工具（vlm/ocr/代码自检，含 import 路径）② 可参考的说明书（frameworks/workflows/skills 数量和 kdo query 关键词）③ 可实例化的 Agent 配置（agent-spec 清单）。API Key 写死在 config.py。**前置条件**：① 所有 Agent 启动序列加 `python -m capability_hub list` ② Hermes Agent Python venv 装 MiniMax SDK ③ 能力中台写入 startup.md 武器库清单。详见 `plan_20260707_capability-hub-architecture.md` | 洪七公建议书 + 黄药师架构方案 2026-07-07 | P1 | 0.5-1d | 待排期 | 无 |
| P-24 | **跨库角色模型**：每个子库是否需要自己的黄药师/老顽童/王语嫣/欧阳锋？还是主库角色覆盖全部子库？核心张力——领域知识需求（老顽童做设计卡需要设计知识）vs 管理开销（每个子库一套五绝 = 20+ Agent）。可能的答案：基础角色（黄药师/欧阳锋）主库共享，领域角色（老顽童/王语嫣）按子库配备——但未验证 | 用户 2026-07-07 | P2 | 待定 | 待讨论 | 需等 P-5 方向确定 + 至少一个子库试点 |
| P-25 | **跨库调用机制**：Agent 在子库 A 如何调用子库 B 的知识/能力？`kdo query` 能否跨库检索？能力中台是否跨库共享？**子问题——能力中台物理部署**：`_capability_hub/` 只放主库，子库 Agent 通过跨 vault 路径引用？还是每个子库拷一份（回到碎片化）？还是用一个独立 git repo 做 submodule？候选方案——① 能力中台全局共享（所有库 import 同一个 `_capability_hub`）② 知识检索用 `kdo query --cross-repo` ③ 跨库卡片引用用 `[[repo:card-id]]` 语法——全未验证 | 用户 2026-07-07 | P2 | 待定 | 待讨论 | 依赖 P-5 + P-23 先落地 |
| P-26 | **Agent 军团规模规划**：未来 30-40 个 Agent（设计/研发/内容/销售/项目……），相当于一个小公司的全部职能 Agent 化。核心问题——① Agent 之间如何发现彼此？（Agent Registry？）② 谁给 Agent 派活？（欧阳锋还是自动调度？）③ 同一个角色（如老顽童）如果有多个实例（设计老顽童、工程老顽童），怎么区分和协调？④ Agent 的创建/销毁/升级生命周期谁管？ | 用户 2026-07-07 | P2 | 待定 | 待讨论 | 等 Agent 数量 > 10 后再正式设计 |
| P-7 | **跨库路由脚本**：`kdo route "问题"` → 基于各库 digest + domain 关键词自动判断该查哪个库。单库命中直接路由，多库交叉由王语嫣审核。P-5 启动后优先做 | 用户 2026-06-28 | P2 | 1d | 待讨论 | 依赖 P-5 |
| P-9 | **多库架构设计**：四库拓扑（主库+个人OS+销售域+项目管理）。`30_wiki/decisions/plan_20260701_kdo-multi-repo-architecture.md` | 黄药师 2026-07-01 | P2 | 待定 | 待讨论 | 需用户详细梳理后讨论 |
| P-8 | **content-production-polish → v2 后续**：Vikki 的 4 标准（听得懂/听得下去/信得过/用得上）可转化为 `kdo validate` 的内容质量 gate。等 12 张 dk 卡入库后，基于萃取结果设计 WARN 规则 | 黄药师 2026-06-29 | P3 | 待定 | 待讨论 | 依赖王语嫣派老顽童萃取 12 张 dk 卡 |
| P-11 | **Y模型 Deferred 项**（欧阳锋 #52 审查建议） | 欧阳锋 2026-07-03 | P2 | 待定 | 待评估 | 标签 `post-agent-loop` |
| P-12 | **Agent Trace 回放自动验证** | 黄药师 2026-07-05 | P2 | 待定 | 依赖 agent-trace 积累 ≥3 次迭代 |
| P-13 | **五阶段记忆管线** | 黄药师 2026-07-06 | P2 | 待定 | 触发条件：Agent ≥10 且日均对话 ≥50 轮 |
| P-14 | **SQLite FTS 全文索引** | 黄药师 2026-07-06 | P2 | 待定 | 触发条件：口述稿 ≥20 份 |
| P-15 | **JSON索引瘦身**：`transcript-index.py` 当前在索引 JSON 里嵌入了全段原文（一份 673KB），口述稿超过 5 份后应改为只存行号，原文从原始口述稿按行号读取 | 黄药师 2026-07-06 | P2 | 待定 | 触发条件：已预处理口述稿 ≥5 份 |
| P-16 | **自动代码审查 Skill**：子 Agent 回头自检 KDO CLI 代码——Codex 自动代码审查模式迁移到 Claude Code。用 Workflow + Agent 工具实现：写代码→派子 Agent 审查→修复→再审查 | 用户 2026-07-07 | P1 | 1-2d | 待排期 | 需要先调研 Claude Code hooks/skills 的代码审查最佳实践 |
| P-27 | **Hermes terminal.cwd 固定为 wiki**：`config.yaml` L33 `cwd: .` → `/mnt/c/Users/Administrator/Desktop/wiki`。根治 search_files 搜 30_wiki 跨 /mnt/c 全树超时（老顽童+王语嫣都踩）+ 免每次 cd | 老顽童 2026-08-08（教练Agent闭环诊断） | P1 | 5min | 待排期 | 无 |
| P-28 | **飞书网关 approvals.mode 评估**：✅ **已落地(2026-08-08)**——laowantong-feishu 已切 `smart`（教练 Agent 实测验证生效，低风险自动批准、高危仍标记；网关审批走 /approve /deny）。Agent 不能直接 patch config.yaml（安全护栏防自改开关），走 `hermes config set approvals.mode smart --profile <name>`。**遗留**：① 网关需 /restart 生效 ② 其他 profile（laowantong/ouyangfeng/wangyuyan）仍是 manual——如需统一由黄药师批量评估 ③ `subagent_auto_approve: false` 子代理审批待评估 | 老顽童 2026-08-08（教练Agent闭环诊断）→ 2026-08-08 已落地 | P1 | 30min | ✅ 已落地 | 无 |
| P-29 | **queue_transition.py 编码修复**：production-queue.md GBK/UTF-8 混排乱码 → 脚本定位任务失败（O-3 已知，多任务已手动 patch + 标注）。方案：队列文件统一 UTF-8 或脚本加编码检测 | 老顽童 2026-08-08（O-3 复现） | P2 | 1d | 待排期 | #218 已知 O-3 |
| P-30 | **脚本输出 GBK 终端崩溃族统一修复**：print 含 emoji/中文在 Windows GBK 终端 exit 1——#269 generate-dashboard.py 终审 A- 扣分点（HTML 已生成不影响功能）+ #272 语境识别同源问题族。方案：脚本入口统一 `sys.stdout.reconfigure(encoding="utf-8")`（skill_bridge_sync/feature_menu 已做，generate-dashboard/其他待补）或 run 时 `PYTHONIOENCODING=utf-8` | 欧阳锋 #269 终审 2026-08-09 | P2 | 0.5d | ✅ 已提审 #323（2026-08-15） | 与 P-29 编码族归并一次清——P-29 仍待排期 |
| P-31 | **WSL Hermes 性能优化**：本机 .wslconfig 锁 memory=4GB/processors=2——多 Hermes gateway 挤爆开始 swap（540Mi/1Gi），反应慢；另一台 Hermes 跑 Windows 原生无此限制所以快。方案：① 停闲置 gateway（basic-skills-coach pid 340 常驻）② 改 .wslconfig（memory=6GB+processors=4，需 wsl --shutdown 全量重启，影响所有 WSL 服务）③ 迁 Windows 原生（大工程）。**✅ 已解决（2026-08-15）**：用户物理内存 16→32GB（实测 31.87GB，可用 18.17GB），.wslconfig 已 4GB→6GB，老顽童 CLI 已于 08-11 迁 Windows 原生；实测 WSL swap 0B 使用（原 540Mi）、8 个 gateway 正常 running、WSL 内存 2.9/6GB——无 swap 压力 | 用户 2026-08-10 提问 + 黄药师诊断 + Codex 观察者 08-15 复验 | P1 | 0.5-1d | ✅ 已解决 | 物理内存 15.9GB→31.87GB，可用 2.3GB→18.17GB；WSL 内存 4→6GB；swap 540Mi→0B |
| P-32 | **skill 双轨"同版本号内容不同"周检**：#267 bridge status 目前靠版本号发现漂移——同版本号但内容单侧更新（不改版本号）检测不到（task-orchestration 实证：1.0.0 双侧内容不同，靠洪七公手动 status + 内容比对才抓到）。方案：①skill_bridge_sync.py status 加**内容 hash 比对**（同版本号下 hash 不同 = 告警"同版本内容漂移"）②或并入"frontmatter round-trip 校验"结晶候选（8 个之一）③周检/CI 化。洪七公建议 2026-08-16（corr_20260816_hongqigong-task-orchestration-drift.md）；王语嫣核验采纳 | 洪七公纠偏 2026-08-16 → 王语嫣采纳 | P2 | 0.5d | 待排期 | #267 桥接脚本；与 frontmatter round-trip 校验可合并 |

---

## 已升级任务（已进入当前任务清单）

| # | 任务 | 升级去向 | 升级时间 |
|:--:|:---|:---|:---|
| P-1 | 查询结果 Core 优先排序 | `huangyaoshi-next-tasks.md` 当前任务第 3 项 | 2026-06-28 |

---

## 已完成任务

| # | 任务 | 完成证据 | 完成时间 |
|:--:|:---|:---|:---|
| P-6 | business-research skill KDO 适配 | `40_outputs/capabilities/skills/shared/research/SKILL.md`、`kdo-tools/research_adapter.py`、wiki 卡修复 | 2026-06-28 |
| P-10 | 跨域模式层 | `30_wiki/cross-domain-patterns/`：3 个模式索引（分层+匹配/假设+验证/工具→建模），75 wikilinks 全有效 | 2026-07-07 |

---

## 状态说明

| 状态 | 含义 |
|:---|:---|
| 待讨论 | 还没和大家对齐是否要做 |
| 待排期 | 已确认有价值，但依赖未满足或时机不成熟 |
| 已拒绝 | 确认不做，保留记录 |
| 已升级 | 已进入当前任务清单或 production-queue |

---

## 升级记录

| 日期 | 任务 | 动作 | 操作人 |
|:---|:---|:---|:---|
| 2026-06-28 | 全部 P 系列 | 从 `huangyaoshi-next-tasks.md` 迁移到本停车场 | 王语嫣 |
| 2026-06-28 | P-1 / P-6 | 已形成明确任务清单，移出停车场，进入 `huangyaoshi-next-tasks.md` 当前任务 | 王语嫣 |
| 2026-07-07 | P-10 | 完成并移入已完成表 | 黄药师 |

---

*维护人：黄药师 | 最后更新：2026-06-28（欧阳锋：P-6 已完成并移入本表）*
| R3 | **审查统计脚本**：`kdo review-stats --month`——pass率/等级分布/平均复审轮数/leniency信号。来源：欧阳锋建议书 R3（2026-08-09）。欧阳锋先手动 grep 统计，脚本上线后替换。**联动**：与 #269 dashboard 首交率同数据源，R3 入队后 #269 可复用其数据 | 欧阳锋建议书 2026-08-09 | P2 | 1d | 待排期 | 无 |
| P3 | **事实核对门（DataPack 模式）**：素材精做时产出"事实清单"（数字/名称/关系+行号），生产卡时 pre-submit 软门核对。素材证据：王鹏飞 18 桥翻车（AI 不质疑口误只扩散错误）。现状：语义核对 lint 做不了硬门禁，设计需想清楚（范围/成本/误报率）再出池 | Live258 优秀作业 2026-08-13（王语嫣裁定采纳黄药师洞察） | P3 | 待设计 | 待排期 | 王语嫣+欧阳锋裁定设计后出池 |
| P2-DYN-01 | **知识传导动态化（agent 出生模板固化 + 持续校验）**：①#263 流水线部署步骤加"挂 kdo MCP"为模板固定动作（新 agent 出生即带检索能力）②08-14 健康检查升级为例行巡检（新 agent 必检 MCP 挂载、新卡必检可检索）③P3 快照迁移定位为"消灭最后一个静态依赖"（快照淘汰后传导=索引更新即传导） | 王语嫣编排 2026-08-16（#324 终审后用户质询：两变量=持续产出 agent + 知识库增长） | P2 | ✅ 已执行 #326（2026-08-16） | ①✅ 已落盘 ②✅ check-mcp-roaming 挂入 health-check ③P3 快照迁移为本任务完成后的立项输入 |
| P2-DYN-02 | **双轨 skill 同版本号漂移周检**：task-orchestration 双轨漂移实证（8-09 shared 加 E028 节未同步 .claude+未升版本号——版本机制发现不了内容差异）。防复发：周检 diff 双轨（或 #267 桥接脚本补内容 hash 校验）；与"frontmatter round-trip 校验"（8 个结晶候选）可合并 | 王语嫣裁定 2026-08-16（黄药师问排停车场或留 friction-log） | P2 | 待设计 | 待排期 | 洪七公发现+黄药师修复+欧阳锋裁定；周检制度化防 52 skill 普遍漂移 |
