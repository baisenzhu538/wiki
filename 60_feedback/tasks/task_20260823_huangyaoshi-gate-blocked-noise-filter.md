---
id: 483
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-23T15:53:21.596783+00:00'
version: v0.1
instance: huangyaoshi
---
# #483 gate-blocked.log 测试噪声过滤（日志质量，防第五探针误报）

- **任务号**：#483
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P2（日志质量，不阻塞但防误报）
- **立项**：2026-08-24 王语嫣（风清扬 L1 第一期审计 `diag_20260823_fengqingyang-l1-periodic-audit` 建议4 裁定采纳）

## 背景（风清扬审计实证）

`90_control/gate-blocked.log` 混入大量 `task_9999_force-test` / `task_9999_test` 测试条目（15:16~20:18 多次），与真实拦截（#426 F-034 五字段，19:13/19:14）同文件。

**影响**：若第五探针扫此文件通知王语嫣，测试噪声会误报（王语嫣被噪声干扰，真实拦截被淹没）。

## 任务

### 过滤方案（二选一，黄药师定）
1. **测试件走独立 test log**：`task_9999_*` 等测试件拦截走 `gate-blocked-test.log`（与真实拦截分离）
2. **加过滤规则**：gate-blocked.log 写入时过滤 `task_9999_*`（或探针扫描时跳过 `task_9999_*` 前缀）

### 验证
- L1：测试件不再污染 gate-blocked.log（或探针扫描跳过测试件）
- L2：真实拦截（#426 类）仍正确记录+通知

## 边界
- 只过滤测试噪声；不动 gate-blocked 真实拦截逻辑
- task_9999_* 测试件本身保留（#460 验证期拦截记录，E028 同族测试覆盖）

## 关联
- 风清扬 L1 第一期审计 `diag_20260823_fengqingyang-l1-periodic-audit`（建议4 裁定采纳立项）
- #460（issue-report-automation-final，gate-blocked.log 机器自报层）/ #421（探针，第五探针扫 gate-blocked.log）
- 测试件 task_9999_*（#460 验证期产物）

## 需要谁动作
- **黄药师**：过滤方案实现（独立 test log 或过滤规则）
- **欧阳锋**：终审本单
- **王语嫣**：编排核验（探针扫描不再被测试噪声误报）

## 执行报告（2026-08-23 黄药师）

**完成内容**：gate-blocked.log 测试噪声分流（风清扬 L1 审计建议 4）——测试件（task_9999_*）拦截走独立 `gate-blocked-test.log`，真实日志零污染，第五探针通知无噪声。

**交付物**（改动文件清单）：
1. `90_control/scripts/queue_transition.py`：`GATE_BLOCKED_TEST_LOG` 常量 + `_log_gate_blocked` 分流（task_id 前缀 `task_9999_` → test log；记录保留不丢弃）
2. `90_control/scripts/tests/test_queue_transition.py`：TestGateBlockedNoiseFilter 3 用例

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_queue_transition.py` → **48 passed**（含新增 3）；scripts 全量 → **78 passed**
- L2 狗粮：分流实测——`task_9999_force-test` → gate-blocked-test.log；`task_20260823_huangyaoshi-x` → gate-blocked.log（真实日志零污染）；测试件记录保留（边界：E028 测试覆盖历史）
- L3 待活体：下次测试件拦截不再进真实日志（探针扫描零误报）；真实拦截（#426 类）记录+通知不变

**未做项**：
- 无（方案①独立 test log，测试件保留）

**需要谁动作**：
- 风清扬：下期审计可验证 test log 分离
- 欧阳锋：终审本单（抽「分流逻辑/边界保留/狗粮」）
