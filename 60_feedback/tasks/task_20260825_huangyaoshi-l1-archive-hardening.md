---
id: 523
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-25T05:38:03.409412+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/l1_capture.py
- kdo-tools/tests/test_l1_capture.py
- 90_control/scripts/conveyor_probe.py
- agents/agent-os.md
- 60_feedback/friction-log.md
---

# #523 L1 归档链路三项加固（#508 终审观察项打包）

- **任务号**：#523
- **状态**：queued
- **assignee**：huangyaoshi（l1_capture.py + 探针接线 + 纪律落文件；欧阳锋终审）
- **优先级**：P2（加固项非缺陷——半夜无人值守场景的可见性/韧性）
- **立项**：2026-08-25 王语嫣（欧阳锋建议书 `60_feedback/diagnosis/diag_20260825_ouyangfeng-l1-archive-hardening.md` R1/R2/R3 裁定采纳；#508 终审 PASS A 观察项，不阻断）

## 背景

#508 终审 PASS A，归档链路已正确（`_zip_covers_dir` 核验门禁 + 判重游标）。审查中发现三处「可以更强」的加固点，均指向半夜无人值守场景：核验射程不足、拒删无人知、事故未上浮全厂台账。三条同文件区、量级小，打包一单。

## 任务

1. **R1 归档核验加 CRC 抽检**：`_zip_covers_dir`（`kdo-tools/l1_capture.py`）现只比 rel 集+逐文件大小，zip 写盘半成/CRC 损坏不在射程内（infolist 不校验 CRC）。核验中补 `zf.testzip()` 或抽样读数据校验；回归测试覆盖坏 zip 场景。
2. **R2 归档拒删接 gate-blocked 通道**：`_archive_old_days` 核验失败现仅 stderr 报警，计划任务下只进 `_archive.log`——半夜拒删无人知。复用 #471 先例通道：拒删事件写 `90_control/gate-blocked.log` → conveyor_probe 第五探针 → 通知王语嫣。拒删=数据安全事件，比体积超限更值得上报。
3. **R3 生产事故上浮全厂 friction 台账**：①补录——#508 事故（474 文件被删+1 真丢失）从 `.agent/friction-log.md` 上浮 `60_feedback/friction-log.md`；②立规范——凡涉及数据丢失/生产链路中断的事故级 friction 双记（agent 级留日常工作摩擦），规范落 `agents/agent-os.md` friction 相关节（施工时回源确认落点，O-15 同族教训）。

## 边界

- 观察项两项**不在本单**：判重游标只看 mtime 不比 size（先观察）；`mirror()` 死函数（留下个卫生批）。
- R2 与 #519（探针空转根治）/#520（审查供给三件套）同触 conveyor_probe 文件区——施工前读最新 HEAD（charter §3.16），有冲突让 #519 先行合入再动手。
- 加固只向前生效，不回溯历史归档批次。

## 验收

- R1：归档核验含 CRC 校验，回归测试覆盖坏 zip 场景（测试全绿）
- R2：构造核验失败场景，gate-blocked.log 有记录且探针可达（附验证输出）
- R3：#508 事故已补录 `60_feedback/friction-log.md`；双记规范已落纪律文件（注明落点路径+节号）
- 欧阳锋终审
