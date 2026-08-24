---
id: 501
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-24T14:45:28.077681+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-24'
---

# #501 角色待办收件箱泛化（探针通知双通道——CLI 实例不再盲区）

- **任务号**：#501
- **状态**：queued
- **assignee**：huangyaoshi（conveyor_probe 扩展+入口挂载；王语嫣编排；欧阳锋终审）
- **优先级**：P1（治编排者盲区——#499 FAIL 打回通知丢失实证：飞书+CLI 均未达，编排者靠用户提醒才发现）
- **立项**：2026-08-24 王语嫣（黄药师建议书 `diag_20260824_huangyaoshi-role-todos-inbox.md` 裁定采纳）

## 背景

探针通知=飞书单一通道，任何角色的 CLI 实例收不到——#499 FAIL 打回通知丢失（飞书+CLI 均未达，编排者靠用户提醒才发现）；欧阳锋双实例（在家 CLI/在外飞书）同族实证。根因：通知只有"推"（飞书）没有"拉"（CLI 收件箱）。F-036 已建 `_append_role_todo` 模式 + `90_control/ouyangfeng-todos.md` 雏形 + `todos-wangyuyan.md` 手动补录 #499 首例——模式验证可行，未泛化。

## 任务

1. **conveyor_probe 通知全角色落盘**：`90_control/todos/<role>.md` 追加式待办（复用 F-036 `_append_role_todo`，通知循环统一落盘，幂等沿用 state 去重）——飞书（在外实例）+ 待办文件（CLI 实例收件箱）双通道全覆盖
2. **CAPSULE_STARTUP 各角色入口**挂"启动读 todos/<role>.md"
3. **故障窗口补偿**：探针运行间隔异常（>2×周期）时提示补扫（增量机制本身可补，只要 state 未被消费——dry-run 已修）
4. 存量已手动补录（#499 打回/欧阳锋 F-036）作首例，验收时核对

## 验证（验证分层）

- L1：conveyor_probe 通知事件同时落盘 todos/<role>.md（state 幂等去重，重跑不重复追加）
- L2 狗粮：制造一次终审/建议书事件，CLI 侧读 todos 文件可查（非飞书侧）
- L3 待活体：下一次角色流转事件（提审/打回/建议书）CLI 实例不再靠用户提醒

## 边界

- **不新增扫描器**（复用 conveyor_probe 现有通知循环）
- **不动 #462 飞书推送**（在外实例照常）
- 待办文件追加式留痕；清理/完成标注由各角色自管（或后续立项）
- 与 F-036 门禁互补：门禁管"发现必须给落点"，收件箱管"通知必须送达"

## 关联

- 黄药师建议书 `diag_20260824_huangyaoshi-role-todos-inbox.md`
- #462（探针流转完成信号——飞书通道，本单补 CLI 通道）
- F-036（agent复盘 git 化 + `_append_role_todo` 模式源）
- #499 打回事件（本单触发实证）

## 需要谁动作

- **黄药师**：conveyor_probe 扩展 + CAPSULE_STARTUP 挂载
- **王语嫣**：验收 CLI 收件箱效果（下次流转事件）
- **欧阳锋**：终审本单

## 执行报告（2026-08-24 黄药师）

**完成内容**：角色待办收件箱泛化（D-002 采纳落地）——探针通知全角色落盘 todos/<role>.md（CLI 实例收件箱）+ CAPSULE_STARTUP 入口 + 故障窗口补偿。

**交付物**（改动文件清单）：
1. `kdo-tools/conveyor_probe.py`：`_append_role_todo` 泛化（全角色 → `90_control/todos/<role>.md` 追加式）；main 通知循环统一落盘（deduped 消息、非 dry-run）；故障窗口补偿（last_run_ts 间隔 >20min 提示补扫）
2. `90_control/todos/`（新目录）：ouyangfeng.md + wangyuyan.md（存量迁移，含 #499 打回/欧阳锋 F-036 首例）
3. `.kdo/CAPSULE_STARTUP.md`：§2 加"角色待办收件箱"共享提示（各角色启动读 todos/<role>.md）
4. `kdo-tools/tests/test_conveyor_probe.py`：2 用例（全角色落盘/追加式）

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_conveyor_probe.py` → **21 passed**（含新增 2）；kdo-tools 全量 → **75 passed**
- L2 狗粮：探针 dry-run 冒烟（夜间静默 3 条进待补发=设计路径正常）；todos/ 落盘生效（wangyuyan/ouyangfeng 文件在，含存量 #499 首例）
- L3 待活体：下一次角色流转事件（提审/打回/建议书）CLI 实例读 todos 文件即见，不再靠用户提醒

**未做项**：
- 待办清理/完成标注由各角色自管（任务书边界，后续可立项）
- 飞书推送不动（#462 在外实例照常）

**需要谁动作**：
- 各角色：启动读 `90_control/todos/<role>.md`（CAPSULE_STARTUP 已挂提示）
- 欧阳锋：终审本单（抽「全角色落盘/幂等/迁移/入口」）

---

## 终审记录（欧阳锋 · 2026-08-24）

**结论：PASS / A-**

**版本对齐三问**（代码类）：① 入仓：531b78b1b（4 files 45+/11-）在 HEAD 链 ② 生效：单测独立复现 + todos/ 落盘实存 ③ 对齐：审查对象=当前源码

**O0 逐条溯源**：
1. **`_append_role_todo` 泛化** ✅（conveyor_probe.py L427）：全角色 → `90_control/todos/<role>.md` 追加式（文件头初始化 + OSError 兜底）——复用 F-036 模式
2. **main 通知循环落盘** ✅（L572）：通知事件统一写 todos（deduped 消息、非 dry-run）
3. **故障窗口补偿** ✅（L511-515）：last_run_ts 间隔 >1200s 提示补扫（增量机制补扫 + dry-run 不消费 state——#499 首例丢失根因已修）
4. **todos/ 迁移首例** ✅：ouyangfeng.md/wangyuyan.md 实存，含 #499 打回手动补录首例（F-036 提醒行——20:58/21:05 两则）
5. **CAPSULE_STARTUP 挂载** ✅：§2"角色待办收件箱（#501，各角色启动必读）"
6. **测试独立复现** ✅：`pytest tests/test_conveyor_probe.py` → **21 passed**（与报告一致）
7. **边界** ✅：不动 #462 飞书推送；不新增扫描器（复用通知循环）；待办清理各角色自管

**发现问题**：🔵 无实质缺陷——观察项：双实例待办语义（ouyangfeng-todos.md vs todos/ouyangfeng.md 两处文件并存——STARTUP §2 已注明口径，演进中）

**魔鬼代言人**：3 个月后最可能出问题——todos/<role>.md 只增不清（长期积累噪音）；或角色不在 ASSIGNEE_ROLE 映射内时落盘失败（OSError 兜底有但静默）——建议后续立项清理/完成标注

**存在性核查**（本意见书负向断言证据）：
- 「泛化实现」→ 核查：conveyor_probe.py L427 源码（追加式+兜底）
- 「21 passed」→ 核查：pytest 独立复跑
- 「迁移首例」→ 核查：todos/ouyangfeng.md 内容（#499 打回补录）
- 「STARTUP 挂载」→ 核查：.kdo/CAPSULE_STARTUP.md §2

**残余风险**：todos 长期只增不清（L3 观察）；两文件并存口径演进。

*欧阳锋 · 2026-08-24 · A-*
