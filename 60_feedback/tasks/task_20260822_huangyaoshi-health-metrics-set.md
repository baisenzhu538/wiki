---
id: 425
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-22T13:19:12.579042+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-22'
grade: A
---
# #425 KDO 健康度指标集（#399 复扫工具扩展）

- **任务号**：#425
- **状态**：queued
- **assignee**：huangyaoshi（指标定义王语嫣+风清扬会签）
- **优先级**：P1（G4 第 2 步：健康度度量——"不能积累太多问题"的仪器化）
- **立项**：2026-08-22 王语嫣（会诊 G4 拍板）

## 任务目标

把"KDO 健康运营"变成可复扫指标集，扩展 `full-library-rescan.py`（#399 工具同仓演进）：

| 指标 | 口径 | 当前基线（W3） |
|:--|:--|:--|
| draft 占比 | 30_wiki status:draft / 总卡 | 798/2865（27.9%） |
| 空壳卡率 | src_unknown 占位占比 | 待首扫 |
| 图谱孤儿率 | 零入链卡占比 | 20%（08-21 实测） |
| parse-error | YAML 解析失败数 | 58（#409 在修） |
| related-asymmetry | 单向链数 | 5265（#411 第十批后） |
| 复盘覆盖率/深度 | 各角色 daily-context 新鲜度+门禁等级 | 2/7 A 级（08-21 审计） |
| 队列一致性 | 队列行 vs 任务单 frontmatter | 0 漂移（audit_queue_integrity） |

## 动作

1. 七指标全部脚本化（一条命令出健康报告）；不接受人肉口径
2. 输出落 `60_feedback/auto/health-check-YYYYMMDD.md`（已有雏形——注意 W8：该报告第一读者=风清扬）
3. 卡片复用率指标标"待定义"（需检索/引用日志，本期只留接口不硬造）

## 验收

- `python full-library-rescan.py --health` 一条命令出七指标报告（附输出）
- 与 W3 基线数字可对账（draft 798/2865 等）
- 欧阳锋终审；commit 入档

---

## 追加（2026-08-22 王语嫣）：第八指标——未登记建议书数

> 来源：PROPOSAL-PENDING 自动登记改造（#421 追加节，老朱 08-22 拍板「想犯错也犯不了」）的兜底层。

- **指标**：未登记建议书数——`60_feedback/diagnosis/` 内命中三元组（`audience: 王语嫣` + `status: pending_orchestration`）但未在队列 PROPOSAL-PENDING 段登记的文件数，目标 = 0
- **口径纪律**：与 #421 扫描器同一份检出逻辑（yaml.safe_load，E017），健康报告只读计数、不代登记（登记动作归 #421，职责不混）
- **验收追加**：健康报告含第八指标行，附输出；与 #421 投递验收用同一份测试建议书交叉验证计数一致

---

## 追加二（2026-08-22 王语嫣）：交接保真度三指标

> 来源：风清扬五角色建议书组织层建议 3（采纳）。依据：L1 业务公式——多 Agent 团队价值 = Σ(角色深度 × 交接保真度) − 协调损耗；交接保真是 KDO 最该盯的数。

- **指标 9-11**：退回率（FAIL 占比）/ 返工轮次（任务单 complete→fail→complete 循环次数）/ 交接留痕完整度（任务单执行报告节非空率）——口径从 queue_transition 流转记录/git log 取数，不接受人肉申报
- 取数可行性先做单点验证，不可行的标「待定义」留接口（同卡片复用率先例，不硬造）

## 执行报告（2026-08-22 黄药师）

**交付物**：
1. `90_control/scripts/full-library-rescan.py` 新增 `--health` 模式——11 指标函数（m_draft_ratio/m_empty_shell/m_graph_orphan/m_retro_coverage/m_queue_consistency/m_unregistered_proposals/m_handoff_completeness + 复用 check_parse_error/check_related_asymmetry）+ 报告渲染（含 W3 基线列/趋势标记/待定义清单）
2. `90_control/scripts/audit_queue_integrity.py` bug 修复：frontmatter id 被 yaml 解析为 int，`find_review_file`/`queue_by_id` 按 str 匹配——两处 `str()` 统一（指标 7 取数依赖，修复前脚本必崩）
3. `90_control/scripts/tests/test_health_metrics.py` 新增 5 测试（draft/空壳/孤儿纯函数 + trend 容差 + --health 集成冒烟）

**验证（附输出）**：`python full-library-rescan.py --health` → 报告落 `60_feedback/auto/health-check-20260822.md`；pytest 5 passed；回归 `--check parse-error` rc 0 / `--check missing-updated-at` rc 1（FAIL 语义未破坏）。

**与 W3 基线对账**（数字见报告原文）：
- draft 占比 **798/2865（27.9%）= 基线完全一致**（分母=30_wiki 全量 md find 口径同源；脚本排除区 _archive/_tmp/raw 等 26 文件 draft=0 不影响分子）
- parse-error **0**（#409 修复生效，基线 58）
- related-asymmetry **1274**（基线 5265，#411 持续回填中实时下降——运行时快照）
- 队列一致性漂移 **0**；未登记建议书 **0**（2 个 proposal 均已登记）
- 首扫基线：空壳卡率 418/2839（14.7%）/ 复盘 A 级 4/7 / 交接留痕 115/426（27.0%）
- 图谱孤儿率 178/2839（6.3%）vs 基线 20% → 改善

**待定义（留接口，附单点验证结论）**：
- 卡片复用率：需检索/引用日志，本期留接口（任务单动作 3）
- 退回率/返工轮次：单点验证 git log 关键词计数（fail 仅 11 条）脆弱、无 queue_transition 流转日志文件——不可行，标待定义；建议立项流转日志基建

**边界与口径说明**：
- 指标 8 只读计数不代登记（登记动作归 #421，职责分离）；检出与 #421 同一份 yaml.safe_load 逻辑（E017）
- 指标 11 口径 = 任务单含 `## 执行报告` 节比例（排除"完成后写执行报告"指引文本）
- 复盘覆盖率角色集合 = 7 主角色（含 fengqingyang），A 级 = daily-context 最新文件 ≤3 天
- 未动其它文件；时间胶囊 git_head/queue_tail 同步更新（维护职责）

## 终审记录（2026-08-22 欧阳锋 · PASS A）

**验收标准逐条核对（O3 实测）**：
1. `full-library-rescan.py --health` 一条命令 ✅——实测输出 11 指标表（1-8/11，含 W3 基线列/趋势标记/待定义清单）+ 报告落盘 `60_feedback/auto/health-check-20260822.md`
2. W3 基线对账 ✅——draft 798/2865（27.9%）与基线完全一致（分母同源 find 口径）；parse-error 0（#409 修复生效）；related-asymmetry 1274（#411 实时快照）；队列漂移 0；未登记建议书 0
3. 指标 8 职责分离 ✅——只读计数不代登记（#421 归登记），检出同源 yaml.safe_load（E017）

**O3 独立验证**：
- 测试：`test_health_metrics.py` **5 passed**（独立跑）✅
- audit_queue_integrity bug 修复实锤：L246/L280 `task_id = str(fm.get("id", ...))`——yaml 解析 id 为 int 统一转 str 匹配（指标 7 取数依赖，修复前必崩）✅
- 回归：--check parse-error rc 0 / missing-updated-at rc 1（FAIL 语义未破坏）✅

**A 级理由**：
1. **G4 第 2 步仪器化落地**——"不能积累太多问题"从口号变可复扫体检（11 指标 + 基线列 + 趋势标记）
2. 取数依赖 bug 自查自修（audit int/str）
3. **待定义诚实**——卡片复用率/退回率/返工轮次留接口不硬造，单点验证结论明确（退回率 git log 计数脆弱 → 建议立项流转日志基建，已记观察）

**遗留**：流转日志基建（退回率/返工轮次取数依赖）建议立项；健康报告第一读者=风清扬（W8 路由）。
