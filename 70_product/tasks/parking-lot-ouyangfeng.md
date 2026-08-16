---
id: parking-lot-ouyangfeng
type: parking_lot
created_at: 2026-06-28
updated_at: 2026-08-02
owner: 欧阳锋
---

# 欧阳锋停车场清单

> **停车场机制**：主线任务进行中，把不阻塞当前主线的洞察、改进点、待讨论方案记录在此。等空下来再和大家讨论/排期。
> **升级路径**：`待讨论` → `待排期` → 进入 `70_product/tasks/production-queue.md` → 分配执行。
> **清理规则**：每月清理一次，超过 30 天未动的 P1/P2 任务强制 review，长期不做的标记 `已拒绝`。

---

## 当前停车场

| # | 任务 | 来源 | 优先级 | 工作量 | 状态 | 阻塞/依赖 |
|:--:|:---|:---|:---:|:---:|:---:|:---|
| O-1 | **欧阳锋工作模式调整与知识库三层化**：周伯通建议书，涉及①从"判官"到"风险标记员"；②卡片界面层/接口层/上下文层三层化；③"找老的干小的"审查优先级；④审查通过即投放（`deploy_status` 字段） | 周伯通 2026-06-14 | P1 | 待定 | ✅ 已确认（待升级实施） | 用户已拍板 |
| O-2 | **kdo_lint.py 命令行参数解析异常**：传入 10 个文件路径时报告 `Files checked: 0`，状态却显示 PASS，疑似未实际解析路径；需排查参数处理逻辑，避免误报 | 欧阳锋 2026-07-04 | P2 | 0.5 天 | 待排期 | 黄药师或 lint 维护者 |
| O-3 | **queue_transition.py review --verdict fail 执行异常**：#197 执行 fail 时报告"任务不在队列中"，但队列条目被异常标记为 reviewed。疑似脚本用 task_id 数字匹配时与队列 task 列格式不兼容（队列用 `task_YYYYMMDD_...` 字符串，脚本可能用纯数字 #197 查找）。需排查 | 欧阳锋 2026-07-21 | P2 | 0.5 天 | 待讨论 | 黄药师或脚本维护者 |
| O-4 | **kdo_lint.py 跨目录死链误报**：ai-collaboration 域内的 related 外链引用了 frameworks/concepts/dark-knowledges 目录下的卡，lint 报告全部为 BROKEN LINK。实际所有 ID 在跨目录搜索中均存在，疑似 lint 仅搜索当前卡所在目录 | 欧阳锋 2026-07-21 | P2 | 0.3 天 | 待讨论 | 黄药师或 lint 维护者 |
| O-5 | **审查时必须检查双目录版本冲突**：#197 案例——标准目录（frameworks/concepts/tools/cases/dark-knowledges）和域目录（ai-collaboration/）各有一套版本，内容分裂（一个 ds 真实但缺 Critique，一个内容完整但 ds 占位符）。以后每批审查先跑 `find` 检查所有卡片是否在标准目录和域目录各有一份 | 欧阳锋 2026-07-21 | P1 | 即时生效 | 审查 SOP 补充 | 无 |
| O-6 | **存量 tool/concept/case/dk 卡补定位声明**：400+ 张旧卡 related 含 framework-* 但正文无框架定位声明。不专门开批量任务（C-10 教训）；老顽童接到返工/enrich/修复任务时顺手补。新卡由 lint + 欧阳锋 Phase 0 拦截。覆盖率随返工自然增长。 | 欧阳锋 2026-07-26 | P2 | 随返工递增 | 待排期（不主动派发） | 依赖 lint 规则上线（黄药师） |
| O-7 | **L8 lint 关键词收紧**：`_check_position_declaration()` 中 `"前置知识"`/`"的子集"`/`"上层框架"` 过于宽松会漏检；`"XX框架"`/`"X步"` 是模板占位符字面量无实际匹配价值。建议改为正则：`属于 .+ 的 .+ 步` 或 blockquote 中 `定位.*属于.*框架`。当前 WARNING 级别可接受，后续排期优化。 | 欧阳锋 2026-07-26 | P2 | 0.3 天 | 待排期 | 黄药师 |
| O-8 | **pre-submit 未拦截 section 名拼写错误**：#213 审查发现 3 处 `## Critque` 拼写错误但 pre-submit 声称 14/14 PASS——标准 section 名（Critique/Synthesis/Failure Modes 等）无精确校验。建议 lint 增加标准 section 名白名单校验（拼写错误 → ERROR 或 WARNING） | 欧阳锋 2026-08-02 | P1 | 0.3 天 | ✅ 已升级（`task_20260802_huangyaoshi-kdo-section-lint-hardening`）| 黄药师 |
| O-9 | **索引自动刷新机制**：#218 R6a 手动 `kdo index` 已完成（Aug 3 01:52 重建，3755 文档，闭环合上）——但刷新仍是手动的。每次老顽童入库一批卡，索引又会过期（本次就是 7/27→8/3 过期 5 天导致搜索盲区）。建议黄药师加 pre-submit hook 或 review-mark 后自动触发增量索引更新 | 欧阳锋 2026-08-03 | P1 | 0.5 天 | 待排期 | 黄药师 |
| O-11 | **跨实例事实分歧裁决协议**（正式文档：`60_feedback/tasks/O11-cross-instance-dispute-protocol.md`）：#224 终审时王语嫣独立核查质疑"dk-yi-tang 7/27 就坏=历史遗留"，欧阳锋严格重验（git show 字节级 + UTF-8 严格解码 + yaml.safe_load）证明 7/27 原版健康——异议方法有误（宽容解码误判）。**协议**：跨实例对"文件原版状态/谁引入破坏"产生分歧时，双方各自跑严格 git 验证（字节级、明确提交 hash、严格解码），以字节证据为准，不凭"谁说的"——并附时间线证据链。**编号说明**：原编号 O-10 为避免与 #218 任务书内 O-10（自查脚本 import 劫持）混淆，统一为 O-11（王语嫣 2026-08-04 对齐） | 欧阳锋 2026-08-04 | P1 | 即时生效 | 审查 SOP 补充 | 全员 |


---

## 建议书逐条摘要与决策

| 建议 | 核心变化 | 决策 | 实施方式 |
|:---|:---|:---:|:---|
| 建议一：审查角色调整 | 从"通过/不通过"改为"风险点+对比视图" | 🟡 有条件同意 | 低风险/常规卡维持现有通过/退回模式；高风险/复杂卡/新域卡使用风险标记+对比视图 |
| 建议二：卡片三层化 | 界面层（人）+ 接口层（系统）+ 上下文层（Agent） | ✅ 同意 | 先定义接口层标准 → 为 P0 深黑节点添加上下文层摘要 → 逐步扩展 |
| 建议三：找老的干小的 | P0 机械检查优先，P2 判断任务后置 | ✅ 同意 | frontmatter 完整性、Constraints 节、diagnostic_signals 填充等作为 P0 机械检查；Critique 攻击质量评估作为 P2 判断任务 |
| 建议四：先投放再精修 | 审查通过即加 `deploy_status: live` | 🟡 原则同意，暂缓全面实施 | 从 wave5 开始试点 `deploy_status: live`，等接口层标准确定后再扩展 |

---

## 升级计划

O-1 已从停车场**升级进入实施阶段**。下一步动作：

1. **王语嫣/黄药师**：定义接口层标准字段（含 `deploy_status`）
2. **欧阳锋**：从 wave4/wave5 开始试行新的审查输出格式
3. **黄药师**：为 P0 深黑节点添加上下文层摘要
4. **王语嫣**：将 O-1 拆分为具体执行任务，进入 `production-queue.md`

---

## 状态说明

| 状态 | 含义 |
|:---|:---|
| 待讨论 | 还没和大家对齐是否要做 |
| 待排期 | 已确认有价值，但依赖未满足或时机不成熟 |
| 已拒绝 | 确认不做，保留记录 |
| 已确认（待升级实施） | 用户已拍板，等待拆分为具体任务进入队列 |
| 已升级 | 已进入当前任务清单或 production-queue |

---

## 升级记录

| 日期 | 任务 | 动作 | 操作人 |
|:---|:---|:---|:---|
| 2026-06-28 | O-1 工作模式调整 | 从 dashboard "待欧阳锋确认" 移入停车场，等待用户拍板 | 王语嫣 |
| 2026-06-28 | O-1 工作模式调整 | 用户逐条确认决策，状态改为"已确认（待升级实施）" | 用户/王语嫣 |

---

*维护人：欧阳锋 | 最后更新：2026-07-04*
| R4 | **攻击问题集自动注入**：kdo-self-attack 攻击模板源——从错误模式库 E001-E013 + pitfalls P-系列自动生成"这张卡最可能犯的错"攻击问题。欧阳锋先文件落地（`40_outputs/capabilities/skills/shared/kdo-self-attack/` 内引用静态问题集），机制化后置 | 欧阳锋建议书 R4 2026-08-09 | P2 | 0.5-1d | 待排期（文件落地欧阳锋自担） | R1 部分规则 |
| O-12 | **Hermes WSL→Windows 迁移专项**（2026-08-16 用户澄清修正：**迁移尝试未成功已回退 WSL 侧，失败原因不清，计划搞清楚原因后再迁移**——双位置部署为长期结构性状态，非临时态）：本机 Hermes gateway 跑在 WSL（.wslconfig 限 4GB/2 核，swap 活跃）反应慢，另一台原生 Windows 明显更快。2026-08-10 已完成调研+决策分析：迁 Windows 好处（内存直通/消除 /mnt/c/ 跨文件系统 I/O 惩罚/生产服务稳定性）；弊端（4 gateway systemd→Windows 服务迁移/全量路径改造/Linux 工具链丢失/迁移期中断）。**修正后的正确形态 = 先诊断失败原因**（复盘上次迁移过程/失败点：gateway 路径解析？服务启动依赖？环境变量？）→ 原因清楚后再评估迁移方案。双位置漂移第 2 次实证（#325 空挂：WSL 侧=实际运行真相源，Windows 副本空挂）→ 迁移未落地前，部署验收必须按 systemd WorkingDirectory 验证（#326 已按此修正）。来源：2026-08-16 用户澄清 + 2026-08-10 调研 + WebSearch 2026（WSL2 不适合 always-on 生产服务） | 欧阳锋 2026-08-10 / 2026-08-16 用户修正 | P2 | 待诊断后估 | 待讨论（用户拍板） | 王语嫣编排 + 黄药师实施；先诊断后迁移 |
| O-13 | **.wslconfig 扩容快速缓解**（✅ 2026-08-15 已执行：6GB→8GB + processors=4，wsl --shutdown 后 8 gateway 全部自动拉起，swap 0B；备份 .wslconfig.bak-20260815；顺带解锁 #303/#304 C1 飞书真机冒烟）：4GB→8GB / 2→4 核（宿主机 15.9GB），消除 WSL swap 活跃（诊断：used 2.6Gi+swap 540Mi）。5 分钟改动 + `wsl --shutdown` 重启（4 gateway 重启）。与 O-12 同族，用户确认后再动 | 欧阳锋 2026-08-10 | P2 | 0.2 天 | 待讨论（用户拍板） | 与 O-12 一并决策 |
| O-14 | **agent-spec 类卡系统性 lint FAIL/WARN**（✅ 2026-08-15 已立项：任务单 task_20260815_wangyuyan-agent-spec-domain-cleanup 已写，待王语嫣编排入队）（08-14 健康检查实证）：`agent-spec-meeting-assistant.md` + `agent-spec-coaching-leadership-assistant.md` 等全部 agent-spec 卡 non-list domain: None（FAIL）+ type=agent-spec in dir=tools/（WARN）——非 #304 引入，全类历史债。处理：domain 字段批量补齐（9 张）+ 目录类型规则评估（agent-spec 放 tools/ 是否符合新 schema）。建议王语嫣编排清扫任务 | 欧阳锋 2026-08-15 | P2 | 0.5d | 待排期 | 王语嫣编排清扫 |
| O-15 | **kdo MCP server 检索引擎缓存**（2026-08-16 R型 Partner 卡顿实证）：每次 kdo_search 调用都重新加载 585MB 索引 + LightRAG graph 3468 nodes + 3 vdb（10.5 秒/次冷启动）——MCP server 是常驻进程，应模块级缓存索引实例（首调加载/后续复用）。影响：R 型 Partner 一轮迭代 3 分钟、所有挂 kdo MCP 的 agent 检索延迟 10 秒+。修复方向：server.py 模块级 lazy 单例 + 失效策略（kdo index 重建后重启 server 或带 mtime 检测） | 欧阳锋 2026-08-16 | P1 | 0.5d | 待排期 | 黄药师 |
| O-16 | **kdo MCP 检索 300s 超时复发**（2026-08-16 R型 Partner 实证 ×2）：MCP 调用 kdo_search 撞 300s 超时——R 型记忆记录"修过一次又犯"，全厂 friction-log 无此记录（记录在 R 型自身 memories 未上浮）。疑似并发场景（多 agent 同时调 kdo_search → 多 server 进程争抢 585MB 索引 IO）或 stdio 管道抖动。与 O-15（冷加载 10.5s）同族：kdo MCP 稳定性专项。短期兜底：agent 检索纪律第 3 条 grep 兜底已生效；根治待黄药师诊断 | 欧阳锋 2026-08-16 | P1 | 0.5-1d | 待排期 | 黄药师（与 O-15 合并诊断） |
| O-17 | **R 型 Partner 配 GitHub Token**（2026-08-16 R型Partner 状态2 实证）：GitHub API 未认证限流 10 次/分钟——R 型 Partner 状态 2 验证 6 工具时已撞限流（自报"GitHub API 未认证限流了…再查也白搭"），状态 3 饱和送高频搜 GitHub 必被卡死。处理：给 `research-explosion-partner` profile 配 `GITHUB_TOKEN`（.env 或环境变量），未认证 10 次/分钟 → 认证后 5000 次/小时。影响：阻塞 #348 状态 3 饱和送（门控点=欧阳锋确认状态 2 后、进状态 3 前必须完成）。 | Codex 2026-08-16 | P1 | 0.1d | 待排期 | Codex（与 O-15/O-16 一并处理） |
