---
id: 432
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-22T16:36:04.835784+00:00'
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
