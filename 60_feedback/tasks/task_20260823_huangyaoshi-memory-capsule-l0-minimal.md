---
id: 432
assignee: huangyaoshi
status: queued
updated_at: '2026-08-23T00:20:00+08:00'
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
