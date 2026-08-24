---
type: proposal
status: pending_orchestration
audience: 王语嫣
date: 2026-08-25
author: 欧阳锋
source: "#508 终审观察项（PASS A 不阻断）"
---

# L1 归档链路三项加固建议（#508 终审观察项立项）

## 背景

#508（L1 日期增量+归档复活）终审 PASS A，链路已正确。审查中发现三处"可以更强"的加固点，非缺陷、不阻断，但均属半夜无人值守场景的可见性/韧性问题，建议立一个小单打包处理。

## 建议

- **R1 归档核验加 CRC 抽检**：`_zip_covers_dir`（`kdo-tools/l1_capture.py:73`）现只比 rel 集+逐文件大小。当前场景够（zip 刚写完或同内容目录，大小碰撞概率极低），但 zip 写盘半成/CRC 损坏不在大小比对射程内（ZipFile 读 infolist 不校验 CRC）。建议核验中加 `zf.testzip()` 或抽样读数据校验——黄药师人工处置时已跑过 testzip，代码化只是顺手。
- **R2 归档拒删接 gate-blocked 通道**：`_archive_old_days` 核验失败仅 stderr 报警（`l1_capture.py:123,136`），计划任务下进 `D:\KDO-memory\L1-full-archive\_archive.log`——半夜拒删无人知。#471 已有先例：体积红线超限写 `90_control/gate-blocked.log` → conveyor_probe 第五探针 → 飞书通知王语嫣。拒删=数据安全事件，比体积超限更值得上报，建议复用同一通道接线。
- **R3 生产事故上浮全厂 friction 台账**：#508 事故（474 文件被删+1 真丢失）只记 `.agent/friction-log.md`（agent 级），未上浮 `60_feedback/friction-log.md`。这正是 O-15 教训（"Agent 本地记忆的 bug 不自动上浮工厂层"）同族——事故级（含真实数据损失）应统一上浮全厂台账，agent 级留日常工作摩擦。建议规范：凡涉及数据丢失/生产链路中断的事故，双记。

## 观察项（非本建议范围）

- 判重游标只看 mtime 不比 size（size 存了未用）——mtime 回拨场景漏采，概率低，先观察。
- `mirror()` 遗留死函数未接命令（#491 移除 C 镜像后遗留）——下卫生批顺手清。

## 验收

- R1：归档核验含 CRC 抽检，回归测试覆盖坏 zip 场景
- R2：拒删事件写 gate-blocked.log，conveyor_probe 可达
- R3：#508 事故补录 60_feedback/friction-log.md；规范写入相应 AGENTS.md/纪律文件
