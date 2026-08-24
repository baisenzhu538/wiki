---
id: 503
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-24T15:52:49.988735+00:00'
version: v0.2
instance: huangyaoshi
code_files:
  - 90_control/scripts/queue_transition.py
  - 90_control/scripts/queue_gate.py
  - 90_control/scripts/tests/test_queue_transition.py
---

# #503 claim 口径族根治（写入口径 + claimed 锁匹配）

- **任务号**：#503
- **状态**：queued
- **assignee**：huangyaoshi（改 claim 写入口径+锁匹配+回归用例；王语嫣编排；欧阳锋终审）
- **优先级**：P1（系统性问题：①任何角色用 kimi 实例 claim 任务，frontmatter assignee 被错写 laowantong；②claimed 锁匹配失效——老顽童 in_progress 不阻塞自己）
- **立项**：2026-08-24 王语嫣（#497 claim 实测发现 + 老朱 08-24 报"老顽童串行任务"锁诊断洞A；拍板 #503+洞A 合并执行）

## 背景

`queue_transition.py:473` `INSTANCE_ROLE_MAP = {"hermes": "laowantong", "kimi": "laowantong"}`——**kimi 被映射为 laowantong**，但实际角色实例分布（#445 映射）：王语嫣=kimi、欧阳锋=kimi、老顽童=hermes。kimi 是多角色共用实例（CLI 名），**按 instance 反推 assignee 在 kimi 上是系统性错误**。

claim 写入（action_claim → apply_updates）`assignee=_role_of(instance)` 把任务单 assignee 覆盖为 instance 反推角色——#444 口径（assignee=角色名+instance 另存）的正确语义应是：claim 不改 assignee（保持队列行/任务单原值），instance 字段记录执行实例。

**洞A（老朱 08-24 实证并入）**：`queue_gate.py can_claim` 的"同一实例 claimed 阻塞"检查 `instance in r.get("assignee")`——#444 起 assignee 写角色名，hermes/kimi 实例名永远匹配不上 laowantong（`"hermes" in "laowantong" = False`）→ **老顽童 in_progress 任务从不阻塞自己，可无限并行 claim**。其他角色（实例名=角色名同形）不受影响——bug 只坑 laowantong。流水线实证：08-24 22:23-23:00 老顽童提审 4 单（#499/#500/#498/#495）不等审查，#498 等审期间提审 #495。

## 任务

1. **claim 写入口径修正**：claim 时 assignee **保持任务单/队列行原值**（不按 instance 反推），只更新 status=in_progress + instance=<执行实例>
2. **INSTANCE_ROLE_MAP 处理**：移除 `kimi: laowantong`（多角色共用实例不可反推角色；hermes 是否保留待确认——hermes 目前是老顽童专属？若也是多角色则一并移除，统一"claim 不改 assignee"语义）
3. **回归用例**：王语嫣(kimi) claim 王语嫣单 → assignee 保持 wangyuyan；老顽童(hermes) claim 老顽童单 → assignee 保持 laowantong；A 角色 claim B 角色单（非法场景）→ can_claim 拒绝或 assignee 保持 B
4. **存量修正**：#497 frontmatter 已手工修正 assignee=wangyuyan（本单实证），其他任务单如被同样误写则复扫修正
5. **claimed 锁匹配修复（洞A）**：can_claim 的 claimed 阻塞检查弃用 `instance in assignee` 子串匹配，改按执行者维度判定——取 claimed 行的执行实例（status `claimed-<instance>` 前缀或独立字段）与当前 instance 比较；老顽童多实例（hermes/kimi）并行风险可加角色归一（INSTANCE_ROLE_MAP 将实例归一为角色再比）。语义目标：**同一执行者同一时刻最多一个 in_progress**
6. **半套修改排查（元凶 commit 读侧验证）**：根因=#444 commit `9d414dd62`（08-23 12:05）改 claim 写入口径（assignee=角色名）时**未同步读侧**（can_claim 锁匹配仍按实例名）→ 静默失效。排查 #444 触碰的写入口径是否还有**其他读侧消费点**未同步：grep 全链 `assignee` 消费处（find_blockers/can_claim/next_claimable/队列行解析），确认无同类"写侧改了读侧没改"的遗留

## 验证（验证分层）

- L1：单测全过（四场景：同角色 claim 保持/跨角色 claim 拒绝/instance 记录正确/老顽童 hermes 已有 claimed 时再 claim 被拒）
- L2 狗粮：王语嫣用 kimi claim 一张测试单，assignee 不再被改写
- L3 待活体：后续 claim 事件 assignee 不再漂移

## 边界

- 只改 claim 写入路径，不动 queue_transition 其他命令（complete/review 等）
- #444 口径（assignee=角色名）维持——修的是"claim 时按 instance 反推覆盖"这个实现缺陷
- 存量 assignee=实例名的任务单不回改（#444 兼容口径）

## 关联

- #497（本 bug 实测现场）
- #444（assignee=角色名+instance 另存口径）
- #445（角色实例分布映射）
- E034/E038（执行状态核实纪律——本次发现=claim 后核 frontmatter）
- 王语嫣 2026-08-24 锁诊断（老朱拍板：洞A 并入本单；洞B/C 另立 #504）
- **元凶 commit**：`9d414dd62`（#444，08-23 12:05）——改写侧（assignee=角色名）未改读侧（锁匹配），静默失效只坑 laowantong（其他角色实例名=角色名同形不受影响）

## 需要谁动作

- **黄药师**：claim 写入口径修正 + INSTANCE_ROLE_MAP 清理 + 回归用例
- **王语嫣**：复扫存量误写 assignee 任务单
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：claim 口径族根治——①claim 不再按 instance 反推覆盖 assignee（保持任务单/队列行原值，只写 status=in_progress + instance）；②INSTANCE_ROLE_MAP 移除 `kimi: laowantong`（kimi=王语嫣/欧阳锋/老顽童共用实例，#445，不可反推；hermes=老顽童专属保留）；③claimed 锁匹配洞A 根治——弃用 `instance in assignee` 子串匹配（#444 写侧改角色名后静默失效，"hermes" in "laowantong"=False → 老顽童可无限并行），改双维度判定：status 前缀 claimed-<instance> 同实例 + claimed 行 assignee 与本次任务 assignee 同角色；④半套修改排查：grep 全链 assignee 消费点（queue_gate/queue_transition/audit_queue_integrity/conveyor_probe/generate-dashboard/myqueue），唯一"写侧改了读侧没改"遗留即 can_claim:166 元凶点，其余为展示/路由兼容层（conveyor_probe ASSIGNEE_ROLE 的 kimi→laowantong 条目仅影响存量实例名行的通知路由回落，记观察项）；⑤存量复扫：frontmatter 与队列行 assignee 不一致 11 条——10 条为 #444 前存量实例名口径（豁免不回改），1 条 role-special-zhu 方向相反且已 reviewed（观察项）；#497 误写模式残留 0 条（#497 本单已手工修正确认 assignee=wangyuyan/instance=kimi）。

**交付物**：
- `90_control/scripts/queue_transition.py`（INSTANCE_ROLE_MAP 去 kimi + action_claim 写入口径修正）
- `90_control/scripts/queue_gate.py`（can_claim claimed 锁匹配双维度重写）
- `90_control/scripts/tests/test_queue_transition.py`（test_role_of_instance_mapping 更新 + TestClaimAssigneePreserved 3 例 + TestClaimedLockMatching 4 例）

**验证**：
- L1：`cd 90_control/scripts && python -m pytest tests/ -q` → **104 passed**（含新增 7 例：kimi claim 保持 wangyuyan / hermes claim 保持 laowantong / 跨角色 claim 保持原值 / 同角色多实例阻塞 / 同实例阻塞 / 不同角色不阻塞 / 存量实例名兼容阻塞）
- L2 狗粮：TestClaimAssigneePreserved 以 action_claim 真实函数+隔离队列跑通 #497 实证场景（kimi claim 王语嫣单 → assignee 不再被改写）
- 存量复扫脚本 `_tmp/scan_503_stale_assignee.py` 实测输出 11 条不一致逐条定性（见上）
- L3 待活体：后续 claim 事件 assignee 不再漂移；老顽童 in_progress 真实阻塞后续 claim

**边界**：只改 claim 写入路径与 can_claim 锁匹配，未动 complete/review/cancel 流程；#444 assignee=角色名口径维持；存量 assignee=实例名任务单不回改；conveyor_probe 通知路由的 kimi 条目未动（观察项——存量行消亡后自然失效，改动会扩大本单范围）；pending_review 占位（洞B/C）归 #504 不在本单。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉存量复扫结论（bug 模式残留 0，无需复扫动作）；#504 待本单终审后领取执行。
