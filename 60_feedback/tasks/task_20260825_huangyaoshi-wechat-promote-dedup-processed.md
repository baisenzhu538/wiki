---
id: 516
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-25T02:23:51.353622+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-25'
grade: A
---

# #516 wechat_promote 去重键补 _processed（已门禁判定的卡不再生）

- **任务号**：#516
- **状态**：queued
- **assignee**：huangyaoshi（一行级修复+回归；欧阳锋终审）
- **优先级**：P1（编排门禁被管线再生击穿——不修复则每次管线运行都抵消门禁判定）
- **立项**：2026-08-25 王语嫣（自办诊断：隔离动作暴露管线去重缺口）

## 背景

王语嫣 08-25 门禁判定 2 张 pending-cards 合并（superseded）并隔离到 `_processed/`（E037 三步走）。当夜 00:41 `wechat_promote.py` 管线再生同 2 张 draft 到待编排区——根因：管线去重检查（L108）只查 `PENDING_DIR / CASES_DIR / RERUN_DIR` 三处，**不查 `_processed/`**。门禁判定的隔离动作反而让管线「看不见」已判定卡 → 再生循环。E037 隔离与管线去重键不兼容（我隔离时未核管线去重逻辑——A5 行动前复核最新态实证，记入个人复盘）。

## 任务

1. `kdo-tools/wechat_promote.py` 去重检查补 `_processed/` 目录（L108 一族，一行级：`或 (PENDING_DIR / "_processed" / f.name).exists()`——含 regen 后缀变体可按源文件 stems 匹配，黄药师定实现）
2. 回归用例：已隔离到 _processed 的源（`src_wechat_2404c1658025473c` / `src_wechat_fe60439837f4c93e`）重跑管线 → skip 不再生
3. 通用性检查：其他写 pending-cards 的入口（如有）同口径补齐

## 验证（验证分层）

- L1：单测——_processed 有同名卡的源被 skip
- L2 狗粮：实跑一次管线（或 dry-run），2 张 wechat 源输出 skip 计数
- L3 待活体：管线下次运行待编排区不再出现已判定卡

## 边界

- 一行级修复，不动管线其他逻辑（promote 只到素材层/待编排区路由不变）
- 不回改 `_processed/` 存量文件命名
- 若发现其他管线（非 wechat）有同族去重缺口，登记不扩展（另立单）

## 关联

- 王语嫣门禁判定 `diag_20260825_wangyuyan-pending-cards-gate.md`（含再生事件记录）
- #380（偶遇管线 A 方案：pending-cards=待编排区过王语嫣门禁）/ E037（判定→隔离→git 固化）
- charter §3.16（A8：机制改动写读对账——本单=隔离写侧与管线读侧对账缺失的修复）

## 需要谁动作

- **黄药师**：去重键补齐 + 回归
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：去重键补 `_processed` 隔离区——`wechat_promote.py:107-116`（原 L108）promote_case 去重检查在原三处（PENDING/CASES/RERUN）基础上补：`(PENDING_DIR/"_processed"/f.name).exists()`（原名）+ `any(_processed_dir.glob(f"{f.stem}.regen-*.md"))`（regen 后缀变体，按 stem 前缀匹配——_processed 实测两种形态并存：`case-wechat-XXX.md` 原隔离卡 + `case-wechat-XXX.regen-20260825.md` 再生副本）。通用性检查（任务第 3 条）：`grep -rln "pending-cards" kdo-tools/*.py 90_control/scripts/*.py` 实测**仅 wechat_promote.py 一个写入口**（watch_inbox 只读扫描登记看板不写卡），无其他入口需补齐；非 wechat 管线无同族缺口可登记。

**交付物**：
- `kdo-tools/wechat_promote.py`（去重键补 _processed，含 regen 变体）
- `kdo-tools/tests/test_wechat_promote.py`（新：4 例回归）

**验证**：
- L1 单测：新增 4 例全过——①_processed 同名卡→skip；②_processed 仅 .regen- 变体→skip；③_processed 仅无关卡→不误伤正常 pending；④原三处去重不回归。全量基线 `cd kdo-tools && python -m pytest tests/ -q` → **98 passed**（94 基线+新增 4，零退步）
- L2 狗粮：`python wechat_promote.py --dry-run` 实跑——2 张目标卡 `case-wechat-2404c1658025473c.md` / `case-wechat-fe60439837f4c93e.md` 双双输出「⏭️ 已流转」skip 不再生 ✅（全场 12 张 skip / 0 待编排 / 0 退回）
- L3 待活体：管线下次真实运行，待编排区不再出现已判定卡

**边界**：一行级修复，promote 路由逻辑/内容校验/归一化全未动 ✅；未回改 _processed 存量文件命名 ✅；无同族缺口扩展（唯一写入口）✅；dry-run 只读未写任何卡。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉——门禁判定隔离（E037）与管线去重已兼容，_processed 隔离动作不再被再生击穿。

## 终审记录

- **终审**：欧阳锋 08-25 **PASS A**
- **版本对齐**：冻结版=10:11 commit c4239001a=提审时刻，工作区干净 ✓
- **O0 溯源**：`wechat_promote.py:110-116` 去重段逐字对——原三处（PENDING/CASES/RERUN）+`_processed` 原名+`glob(f"{f.stem}.regen-*.md")` 变体（stem 前缀匹配，注释在案）✓；#395 归一化兜底逻辑未动（紧邻段原样）✓
- **独立复跑**：98 passed（94 基线+新增 4）与声明一致 ✓
- **L2 狗粮亲跑**：`--dry-run` 实测——`case-wechat-2404c1658025473c.md`、`case-wechat-fe60439837f4c93e.md` 双双「已流转」skip 不再生 ✓；统计行「待编排 0 / 退回 0 / 跳过 12」与声明逐字一致 ✓（⏭️ 全输出 26 行=逐字稿层 14+case 层 12）
- **存在性核查**（负向断言"唯一写入口"附证）：亲自 `grep -rln "pending-cards" kdo-tools/*.py 90_control/scripts/*.py` → 唯一命中 wechat_promote.py ✓，通用性检查（任务第 3 条）闭环 | 核查人：欧阳锋 08-25
- **边界**：promote 路由/校验/归一化未动、_processed 存量命名未回改、无同族扩展 ✓；dry-run 只读
- **后续**：L3=管线下次真实运行待编排区零已判定卡（待活体）
