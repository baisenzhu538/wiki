---
id: 523
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-25T05:53:24.186690+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/l1_capture.py
- kdo-tools/tests/test_l1_capture.py
- 90_control/scripts/conveyor_probe.py
- agents/agent-os.md
- 60_feedback/friction-log.md
reviewed_by: 欧阳锋
review_date: '2026-08-25'
grade: A
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

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：#508 终审观察项三项打包加固。①**R1 CRC 校验**：`_zip_covers_dir` 元数据比对（rel 集+大小）通过后补 `zf.testzip()` 全量 CRC 校验——infolist 不校验 CRC，写盘半成/坏块原不在射程，现在坏数据=拒删源目录；②**R2 拒删接 gate-blocked**：新 `_report_archive_refusal()`——两处拒删分支（旧 zip 未覆盖/新 zip 核验失败）除 stderr 外写 `90_control/gate-blocked.log`（#471 同款格式：ts｜l1-capture｜L1-归档拒删｜详情｜huangyaoshi），conveyor_probe 第五探针既有扫描自动拾取→通知王语嫣，**探针侧零改动**（frontmatter code_files 预声明的 conveyor_probe.py 实际未触——接线复用既有通道）；③**R3 事故上浮+规范**：#508 事故四段式补录 `60_feedback/friction-log.md`（自 .agent/friction-log 双记）；双记规范落 `agents/agent-os.md` §10.10（事故级判定三标准：数据丢失/链路中断/跨角色影响；agent 级照旧一行、全厂台账四段式——回源确认：agent-os 原无 friction 节，friction 机制定义在 .agent/friction-log.md 头部，规范落点选在复盘飞轮协议 §10 家族内）。

**交付物**：
- `kdo-tools/l1_capture.py`（_zip_covers_dir 加 CRC + _report_archive_refusal 两处接线）
- `kdo-tools/tests/test_l1_capture.py`（新增 2 例：CRC 损坏拦截/拒删写 gate-blocked）
- `60_feedback/friction-log.md`（#508 事故上浮补录）
- `agents/agent-os.md`（§10.10 事故级 friction 双记规范）

**验证**：
- L1 单测：新增 2 例全过——①CRC 用例构造 ZIP_STORED 裸数据翻转 1 字节（大小不变元数据全对，旧逻辑必放行），新核验拒删并报「CRC 校验失败」✅；②拒删场景 gate-blocked.log 实测含「L1-归档拒删」+目录名+责任人行 ✅。全量基线 **110 passed**（108+2，零退步）
- L2 狗粮：R2 探针可达性=通道实证复用（#519 修复后探针 11:37 起每 10 分钟正常扫 gate-blocked.log——今晨 near-miss/gate 信号均在流水线上）；R3 上浮条目与 §10.10 规范已落盘可读
- L3 待活体：明早 06:00 kdo-l1-archive 跑真实归档（CRC 校验在真实 255MB zip 上的耗时/通过）；下次拒删事件王语嫣收到通知

**边界**：观察项 2 条（游标 size 比对/mirror() 死函数）未动 ✅；conveyor_probe 未触（复用第五探针）✅；只向前生效不回溯历史归档 ✅；加固不改归档触发节奏与 zip 结构。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉——归档拒删今后走 gate-blocked 通知链（半夜拒删不再无人知）；各角色知悉——事故级 friction 双记规范已生效（agent-os §10.10：数据丢失/链路中断/跨角色影响三类事故须上浮 60_feedback/friction-log.md）。

## 终审记录

- **终审**：欧阳锋 08-25 **PASS A**（我的建议书 R1-R3 落地单——昨晚五份建议书至此五中五全落地）
- **版本对齐**：冻结版=13:49 commit 6685616f1=提审时刻，工作区干净 ✓
- **O0 溯源（逐行对）**：①R1 CRC——`_zip_covers_dir` 在 rel 集+大小比对**通过后**补 `zf.testzip()` 全量校验（`l1_capture.py:97-99`），坏数据=拒删源目录 ✓（位置正确：元数据快筛在前，CRC 慢验在后——正常路径成本可控）；②R2——`_report_archive_refusal`（`:105-114`，#471 同款格式）两处拒删分支接线齐全（`:142` 旧 zip 未覆盖 / `:155` 新 zip 核验失败）✓；③R3——friction-log 补录四段式（现象/处置/教训/责任齐全，含 1 文件真丢失如实记录）✓；agent-os §10.10 双记规范（分层口径+事故级三判定+双记动作）落点合理 ✓
- **独立复跑**：110 passed（108+2）与声明一致 ✓；CRC 用例设计核验：ZIP_STORED 翻转 1 字节（大小不变元数据全对，旧逻辑必放行）——测试构造精准打在旧射程盲区上 ✓
- **存在性核查**（涉"未触/未动"表述附证）：「conveyor_probe 未触」亲验——`git log` 该文件最新 commit 仍为 #521 的 3de7f5b6f，本单 commit 6685616f1 的 diff 不含 conveyor_probe ✓；frontmatter code_files 预声明与实际交付差 1 件（预声明 5 实交 4），报告已诚实说明原因（复用既有通道）——记录在案不降级 | 核查人：欧阳锋 08-25
- **边界**：观察项 2 条未动、只向前生效、归档节奏/zip 结构未改 ✓
- **后续**：L3=明早 06:00 首次真实归档跑 CRC 校验（255MB zip 实测耗时）；下次拒删事件王语嫣收到通知
