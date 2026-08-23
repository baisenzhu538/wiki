---
id: 456
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-23T08:08:16.663451+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-23'
grade: A-
---
# #456 记忆胶囊 agent_id 统一 + 审计器解析盲区修复（两小修复合一单）

- **任务号**：#456
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P2（两个小修复，合并避免碎片化；素材来自两份建议书编排决策）
- **立项**：2026-08-23 王语嫣（风清扬查询通道建议书建议 3 + 欧阳锋 #188 残留处置建议之审计器修复项）

## 任务 1：记忆胶囊 agent_id 统一（风清扬建议 3 采纳）

- 统一口径：拼音角色名 `fengqingyang / wangyuyan / ouyangfeng / laowantong / huangyaoshi / hongqigong / duanwangye`（无工具名、无中文）——与 #444 frontmatter assignee 角色名口径同族
- 库 `~/.kdo-memory/L0/activity_log.db`：清 `__test434__` 测试残留；`老顽童`（中文）历史事件改 `laowantong`（或迁移注明）
- 写入端对齐：daily-context-save 挂钩（#434）写入的 agent_id 以本口径为准，防继续混入
- 只动数据层与写入端口径；query 命令**不在本单**（挂 F-045 等老朱拍板 L1 开放口径）

## 任务 2：审计器解析盲区修复（欧阳锋 #188 处置建议采纳）

- `audit_queue_integrity.py`：行数异常的队列行**禁止静默跳过**——应报「无法解析」并列入报告（#188 实证：双列数异常行被跳过，掩盖 pending_review 残留，审计器报 0 不一致=假阴性）
- 修复后全量重跑审计，输出真实残留清单（可能不止 #188 一条）交王语嫣编排处置

## 验证（验证分层声明）

- L1：单测（agent_id 清洗用例/解析异常报错用例）
- L2：狗粮——修复后审计器跑出 #188（已知残留）= 盲区消除实证；agent_id 清洗后 status/verify 走通
- L3 待活体：下次真实 daily-context-save 写入的 agent_id 落库为新口径

## 边界

- 不做 query 命令（F-045 待拍板）；不动 memory_capsule.py 的 L0→L1 改名（F-044）；不碰队列状态机

## 执行报告（2026-08-23 黄药师）

**完成内容**：①审计器解析盲区修复——parse_queue 表检测改 `|:---` 分隔行（旧 `| 队列序号` 表头整表静默失败=审计假阴性，实测解析 0→61 行），行数异常（<5 列）禁静默跳过→收集进 unresolved 入报告；②agent_id 口径对齐——daily-context-save 写入端加 `_normalize_agent_id`（中文角色名映射拼音 + `__x__` 测试残留拒绝写入），L1 库数据清洗（删 `__test434__`/`__test464__` 残留 + `老顽童`→`laowantong`），A/B 镜像重跑 verify PASS。

**交付物**（改动文件清单）：
1. `90_control/scripts/audit_queue_integrity.py`：parse_queue 表检测 robust + 返回 (rows, unresolved) + 报告新增「无法解析队列行」节 + 退出码含 unresolved
2. `kdo-tools/daily-context-save.py`：`_normalize_agent_id`（AGENT_ID_CN_MAP 中文→拼音 + `__.*__` 测试残留拒绝）+ `_write_l0_event` 入口规范化
3. `90_control/scripts/tests/test_audit_queue_integrity.py`（新建）：6 用例（解析盲区回归 3 + agent_id 口径 3）
4. `20_memory/queue_integrity_audit_latest.md`：修复后审计报告（脚本自动生成）
5. 数据层：`~/.kdo-memory/L1/activity_log.db` 清洗（A 主库 7→5 行，无中文/测试残留 agent_id）

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_audit_queue_integrity.py` → 6 passed；scripts 目录全量回归 `pytest tests/` → **56 passed**（含 queue_transition 45 + health_metrics 5）
- L2 狗粮：①修复前 parse_queue 解析 **0 行**（假阴性实证）→ 修复后 **61 行**，真实不一致 **3 条**浮出（#319/#323/#331 队列 reviewed 但任务单 status=pending_review，即 #188 同族残留清单，交王语嫣处置）；②`audit_queue_integrity.py` 全量重跑落盘报告（exit=1=有残留需处置，符合预期）；③L1 库清洗后 `memory_capsule` status（A 5 行 integrity ok）+ 重镜像 + **verify PASS**（B 镜像 5 行 hash 全一致）
- L3 待活体：下次真实 daily-context-save 写入的 agent_id 落库为新口径（中文名自动映射拼音，`__x__` 测试残留被拒绝）

**未做项**：
- query 命令不在本单（F-045 待老朱拍板 L1 开放口径）
- 33 条任务单元数据历史欠账（缺 review_date/reviewer）不在本单范围——审计报告如实列出，处置待编排
- 3 条真实残留（#319/#323/#331 frontmatter status 未同步）**只输出清单不自行修复**——交王语嫣编排处置（任务书边界）

**需要谁动作**：
- 王语嫣：处置 3 条真实残留（#319/#323/#331 任务单 status 同步 reviewed）——审计器修复后已可见
- 欧阳锋：终审本单（抽「解析盲区回归用例/清洗后 status+verify/写入端口径」）

---

## 终审记录（欧阳锋 · 2026-08-23）

**结论：PASS / A-**

**版本对齐三问**（代码类，全绿）：① 入仓：b6de91c55（15:52）在 HEAD ② 生效：审计器重跑 61 行解析 ③ 对齐：审查对象=HEAD

**O0 逐条溯源**：
1. **任务 1 审计器盲区修复** ✅：parse_queue 表检测改 `|:---` 分隔行（旧"| 队列序号"表头整表静默失败=审计假阴性——修复前解析 0 行实证）+ 行数异常（<5 列）禁静默跳过 → unresolved 收集入报告 + 退出码含残留
2. **任务 2 agent_id 统一** ✅：`_normalize_agent_id`（AGENT_ID_CN_MAP 中文→拼音 + `__.*__` 测试残留拒绝写入）；L1 库清洗实证（**6 行全拼音**：huangyaoshi/fengqingyang/wangyuyan/laowantong/duanwangye——无中文、无 __x__ 残留）
3. **独立复现（O3）** ✅：审计器全量重跑——**解析 61 行**（修复前 0=假阴性消除）+ **状态不一致 3 条浮出**（#319/#323/#331——#188 同族残留，证实我 #188 建议书"可能不止一条"判断）+ **无法解析 0**（unresolved 节在）+ exit=1（有残留需处置语义正确）
4. **测试独立复现** ✅：6 passed（盲区回归 3 + 口径 3）；报告全量 56 passed（含 queue_transition 45 + health_metrics 5）
5. **边界** ✅：query 命令不在本单（F-045 待拍板）；3 条真实残留只输出清单不自行修复（交王语嫣编排——出口清单合规）；33 条历史欠账如实列出
6. **verify** ✅（清洗后 A/B 镜像重跑 PASS——报告附输出）

**发现问题**：🔵 无实质缺陷——观察项：33 条任务单元数据历史欠账（缺 review_date/reviewer）长期挂账，建议王语嫣编排补录批（或按 #389 只向前生效裁定搁置）

**魔鬼代言人**：3 个月后最可能出问题——新表头格式变化再次触发解析盲区（分隔行正则需随 queue 模板演进）；或 agent_id 新实例名（codex 等）未入 CN_MAP（中文名写入被拒 vs 拼音直写——观察期确认）

**存在性核查**（本意见书负向断言证据）：
- 「解析 61 行」→ 核查：audit 独立重跑输出（61 行 + 无法解析 0）
- 「3 条残留」→ 核查：audit 输出"队列/任务单状态不一致数: 3"（#319/#323/#331）
- 「L1 清洗」→ 核查：SQLite 全列读取 6 行 agent_id 全拼音（输出附上）
- 「测试 6 passed」→ 核查：pytest 独立复现

**残余风险**：3 条残留处置待王语嫣；33 条欠账编排决策；F-045 query 口径待老朱。

*欧阳锋 · 2026-08-23 · A-*
