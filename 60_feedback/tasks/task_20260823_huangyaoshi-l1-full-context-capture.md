---
id: 463
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-23T07:30:21.975855+00:00'
version: v1.0
doc_id: D-20260823-004
instance: huangyaoshi
---
# #463 L1 全量上下文采集基建（甲会话原文+乙工作痕迹，D 盘+镜像）

- **任务号**：#463
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（老朱 2026-08-23 追问触发+拍板口径：甲乙两类都要、D 盘保存；记忆胶囊从「事件指针层」升级「真全量」的基建）
- **立项**：2026-08-23 王语嫣（风清扬建议书 `diag_20260823_fengqingyang-memory-capsule-l1-full-context.md` 采纳，老朱口径已拍板）

## 采集口径（老朱 2026-08-23 拍板）

- **甲类=CLI 会话原文**：老朱↔各角色 agent 的完整对话流
- **乙类=工作痕迹**：session trace + 产出物变动（文件 mtime/diff 摘要）
- **保存位置=D 盘**（原始资料另处保存，git 外）+ 第二盘镜像 + verify 可恢复

## 范围（依建议书，实施细节黄药师定）

1. 甲类采集：各 CLI 工具会话存储的增量抽取落 D 盘（工具会话路径盘点→采集脚本→增量对齐）
2. 乙类采集：session 目录 trace + 产出物变动记录的采集/汇总
3. 与既有 L0 库（activity_log.db 事件指针层）的关系：并存分层——事件指针库继续（#434），全量原文库新增；命名与 L1 口径对齐（含 F-044 的 L0→L1 改名一并处理）
4. 镜像+verify：同 #432 双盘模式（A 主库 D 盘/B 镜像第二盘/verify 定期）

## 验证（验证分层声明）

- L1 单测；L2 狗粮=采一段真实会话+一次真实文件变动→D 盘落盘→verify 过；L3 待活体=次日复盘自动含全量原文可回放

## 边界

- 原始日志 D 盘 git 外（B3-1 口径）；体积红线监控（30min 频率注体积，超限告警降频）
- 不做 L2-L4（已由风清扬口径+定期报告覆盖）；不动 #460（独立线）

## 执行报告（2026-08-23 黄药师）

**完成内容**：L1 全量上下文采集基建——甲类（CLI 会话原文）+ 乙类（工作痕迹）落 D 盘 + C 盘镜像 + verify 可恢复；F-044 L0→L1 改名顺带完成。

**交付物**（改动文件清单）：
1. `kdo-tools/l1_capture.py`：甲类采集（Claude Code projects/*.jsonl + kimi-code + hermes profiles 增量，mtime 对齐、OSError 容错）→ `D:\KDO-memory\L1-full\YYYY-MM-DD\<tool>\`；乙类 trace.md（文件清单+mtime+大小）；镜像（D → C 盘 `~/.kdo-memory/L1-full-backup`）+ verify（文件数+抽样 hash）
2. `kdo-tools/memory_capsule.py` + 目录 + `20_memory/memory-registry.md`：**F-044 L0→L1 改名**（`.kdo-memory/L0`→`L1`、`D:/KDO-memory/L0-backup`→`L1-backup`，镜像重跑 verify PASS）

**验证**（命令+输出）：
- L1：采集脚本无 pytest（文件系统工具）——dry-run 增量断言 + 幂等（二扫零新增）
- L2 狗粮：**真实采集全链路**——新增 5554 个会话文件 → D 盘 + trace.md + C 盘镜像 7310 文件 + **verify PASS**（文件数一致 + 抽样 hash 全同）；改名后 memory_capsule status（L1 主库 5 行 integrity ok）+ 重镜像后 verify PASS
- L3 待活体：次日复盘自动含全量原文可回放（老朱或风清扬审计抽查）

**未做项**：
- 原始日志 D 盘 git 外（B3-1 口径）；体积红线监控（30min 频率注体积）未做——记遗留（可挂 #425 或独立小单）
- 不做 L2-L4（风清扬口径+定期报告覆盖）；不动 #460

**需要谁动作**：
- 风清扬：L1 数据审计权履职（D 盘全量原文可查）
- 欧阳锋：终审本单（抽「采集面正确/增量幂等/改名无破坏」）
- 王语嫣：体积红线监控立项（可选）
