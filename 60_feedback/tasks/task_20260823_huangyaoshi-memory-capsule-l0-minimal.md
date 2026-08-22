---
id: 432
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-22T17:05:42.534742+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-22'
grade: A-
---
# #432 记忆胶囊 L0 最小实现（A 本机主库 + B 第二盘镜像）

- **任务号**：#432
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（F-027 第一阶段；只做 L0 最小闭环，不做 L1/L2/L3）
- **立项**：2026-08-23 王语嫣（#427 老朱拍板：A+B 先行，C 缓议；建设者已校正为黄药师）

## 任务目标

把 L0 全量留痕从「方案」落成最小可用：SQLite 主库在 git 外，第二盘镜像可恢复，verify 可证明能恢复。只建 L0，不做摘要/洞察/沉淀。

## 范围

1. 建 A 主库：`C:\Users\Administrator\.kdo-memory\L0\activity_log.db`（含 WAL），schema 含 agent_id/session_id/ts/event_type/payload 摘要/hash。
2. 建 B 镜像脚本：`D:\KDO-memory\L0-backup\`，`robocopy /MIR` 或等效脚本；先手动跑通，不注册常驻计划任务。
3. 建 verify：`memory_capsule.py status/verify` 或同仓脚本，能输出行数、最新 ts、WAL 完整性、B 镜像可恢复校验。
4. 恢复演练：从 B 恢复到临时目录，verify 通过；写清命令与输出。
5. 常驻计划任务（schtasks/服务）**不默认注册**；如需要，先把 exact 命令写进任务单请老朱确认后再注册。

## 边界

- 风清扬不实施；只做审计/建议。黄药师建设，建设后必须狗粮测试：用一条测试事件写入→镜像→删除 A 临时副本→从 B 恢复→verify。
- 不写 KB 卡；不碰 wiki 30_wiki；不改复盘内容；不进迁移专案。
- L1/L2/L3 不在本单；消费端 ≤1KB 精华段另单。
- 任何「可恢复」声明必须附 verify 输出；不附=未验证。

## 验收

- A/B 路径、schema、脚本、verify 输出齐全；恢复演练成功。
- 交付五字段（F-034）；审查意见落盘（F-035）；commit 入档。
- 欧阳锋终审抽：是否只做 L0、是否无计划任务擅注册、是否 verify 真恢复。

## 关联

- 停车场：F-027（本单只完成第一阶段；L1-L3 仍留 F-027 后续）
- 拍板：#427 A+B 先行、C 缓议；备份路径拍板后需登记 `memory-registry.md` 表 1

## 内容价值判断（#375 处置门禁补充节，2026-08-23 黄药师领取时补）

- **本任务为备份基建**：新建 A 主库 + B 镜像 + verify 脚本——**零删除存量**（全部为新建文件/目录）
- 唯一"删除"动作：狗粮演练中删除**自己刚写入的测试事件**（临时副本，测完即删，非存量素材）
- 不碰 wiki/复盘/中文旧轨；PROTOCOL §7 素材零触碰

## 执行报告（2026-08-23 黄药师）

**完成内容**：记忆胶囊 L0 最小实现——A 本机主库 + B 第二盘镜像 + verify 可恢复证明，狗粮全链路通过。

**交付物**（改动文件清单）：
1. `kdo-tools/memory_capsule.py`：init/log/mirror/status/verify/restore 六命令——A 主库（SQLite WAL，schema：agent_id/session_id/ts/event_type/payload_summary(≤1KB)/payload_hash(sha256)）+ robocopy /MIR 镜像（先 wal_checkpoint(TRUNCATE) 防半写）+ B 可恢复校验（文件 hash 对比 + 从 B 打开 integrity_check）
2. A 主库 `C:\Users\Administrator\.kdo-memory\L0\activity_log.db`（git 外）；B 镜像 `D:\KDO-memory\L0-backup\`
3. `20_memory/memory-registry.md` 表 1 登记 L0 主库/镜像路径（任务单关联要求）

**验证**（命令+输出）：
- 狗粮全链路（#432 边界要求）：init → log（测试事件 #1）→ mirror → verify PASS（hash 全一致 + B 打开 integrity=ok 行数 1）→ **模拟丢失**（A 移走）→ restore 从 B 恢复 → **verify PASS**（A 回填后全通）→ 现场清理（.gone/临时恢复目录已删）
- status：行数 1 / integrity ok / B 镜像存在
- 测试事件 #1 保留在 L0（L0 语义=全量留痕，保留合理）

**未做项**：
- L1 摘要/L2 洞察/L3 沉淀不在本单（F-027 后续阶段）
- 常驻计划任务**未注册**（#432 边界：需老朱确认 exact 命令后再注册）——当前 mirror 手动跑；建议命令：`schtasks /create /tn kdo-memory-mirror /tr "python kdo-tools/memory_capsule.py mirror" /sc daily /st 03:00`（待老朱确认）
- 消费端 ≤1KB 精华段另单；未写 KB 卡、未碰 30_wiki

**需要谁动作**：
- 老朱：确认是否注册常驻镜像计划任务（命令见上）；B 盘（D: 36G 可用）为 L0 镜像载体
- 欧阳锋：终审本单（抽"是否只做 L0 / 无计划任务擅注册 / verify 真恢复"）
- 王语嫣：F-027 状态更新（第一阶段完成，L1-L3 留后续）

---

## 终审记录（欧阳锋 · 2026-08-23 凌晨）

**结论：PASS / A-**

**版本对齐三问**（代码类，全绿）：① 入仓：3a62943e2（00:36 feat(capsule)）在 HEAD ② 生效：A 主库实存（.kdo-memory/L0/activity_log.db 12288B）+ B 镜像实存（D:\KDO-memory\L0-backup\ 12288B 与 A 一致）+ memory-registry.md 表 1 已登记 ③ 对齐：审查对象=HEAD

**O0 逐条溯源**：
1. **schema 精确匹配** ✅：SQLite 实测 7 列（id/agent_id/session_id/ts/event_type/payload_summary/payload_hash）——与任务单逐一对应；journal_mode=wal
2. **六命令齐全** ✅：init/log/mirror/status/verify/restore；mirror 先 `wal_checkpoint(TRUNCATE)` 防半写（代码 L101 起）
3. **只做 L0 边界** ✅：L1/L2/L3 仅 docstring 范围声明（L5），无越界实现；未写 KB 卡/未碰 30_wiki
4. **无计划任务擅注册** ✅：schtasks 枚举 NONE（kdo-memory-mirror 不存在）——老朱确认前的红线遵守；建议命令已写任务单待拍板
5. **registry 登记** ✅：表 1 L0 主库/镜像/verify 三行（#427 拍板动作落实）

**O3 独立复现**：
- `status`：行数 1 / 最新 ts 2026-08-22T16:34:51（=报告测试事件 #1）/ integrity ok / B 存在
- `verify`：**PASS**——B 镜像文件 hash 全一致 + 从 B 打开 integrity=ok 行数 1（A 同 1）——"可恢复"声明附 verify 输出 ✅

**发现问题**：
- 🟠 镜像无常驻调度：mirror 手动跑（拍板决策，老朱待确认计划任务）——遗忘风险：长期不 mirror → B 过时。TODO：老朱拍板后注册 `kdo-memory-mirror`（命令已列任务单）
- 🔵 恢复演练为终态验证（我复现了 verify PASS；完整 restore 链路为执行者狗粮实测，A 库未被我再动——演练无残留）

**魔鬼代言人**：3 个月后最可能出问题——B 镜像长期不更新（手动调度遗忘，🟠）；或 D 盘 36G 被占满导致镜像失败（verify 会暴露，需巡检）。

**残余风险**：手动镜像待老朱拍板；F-027 L1-L3 留后续阶段。

*欧阳锋 · 2026-08-23 · A-*

**存在性核查**（#433 门禁，2026-08-23 补）——本意见书负向断言及核查证据：
- 「kdo-memory-mirror 计划任务不存在」→ 核查：`schtasks /query /fo csv` 全量枚举（409 任务），Python 过滤 memory+mirror → 0 命中（输出：`memory-mirror tasks: NONE`）
- 「未写 KB 卡/未碰 30_wiki」→ 核查：git show 3a62943e2 --stat 仅 kdo-tools/memory_capsule.py + memory-registry.md + 任务单，30_wiki 零改动
- 「只做 L0 无越界实现」→ 核查：grep -n "L1\|L2\|L3" memory_capsule.py 仅 L5 docstring 一处范围声明
- 「无测试残留」→ 核查：ls .kdo-memory/L0/ 仅 activity_log.db 单文件；D:\KDO-memory\L0-backup\ 仅 activity_log.db
- 「B 与 A 一致」→ 核查：ls -la 两文件均 12288B；verify 输出 hash 全一致 + integrity=ok
