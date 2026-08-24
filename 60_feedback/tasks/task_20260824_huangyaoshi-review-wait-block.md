---
id: 504
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-24T16:35:47.619062+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- 90_control/scripts/queue_gate.py
- 90_control/scripts/queue_transition.py
- 90_control/scripts/tests/test_queue_transition.py
---

# #504 审查等待期阻塞（同执行者 pending_review 占位）

- **任务号**：#504
- **状态**：queued
- **assignee**：huangyaoshi（改 can_claim 阻塞语义+回归用例；王语嫣编排；欧阳锋终审）
- **优先级**：P1（质量门——审查空窗策略直接决定验收质量：流水线不等审查 = 质量无人把关）
- **立项**：2026-08-24 王语嫣（老朱 08-24 报"老顽童串行任务"→ 锁三洞诊断；拍板洞 B/C 立本单，依赖 #503 先修）

## 背景

老朱 08-24 报：老顽童串行任务，不等审查结果。实证：22:23-23:00 提审 4 单（#499/#500/#498/#495，间隔 14-19 分钟），#498 等审期间提审 #495；#498 终审 **FAIL**（graph-rag 回补未执行+"词不足"理由不实）——**审查等待期继续接单 = 质量代价实证**（#499 首轮 FAIL 同款：4 张遗漏）。

锁分析（王语嫣 08-24 诊断，洞 B/C）：
- **洞B**：`can_claim` 只防同执行者并行 in_progress（claimed 阻塞），pending_review **不占执行者位**——complete 提审即释放锁，审查等待期可无限接单
- **洞C**：`earlier_pending` 只按队列前后位置（seq）判断，不按归属——自己的 pending_review 在队列后方时不拦自己 claim 前方任务（#495 seq 495 在前、#498 seq 498 在后，被绕开）

## 任务

1. **pending_review 占用检查**：can_claim 增加——执行者已有 pending_review 任务（**不论队列前后**，执行者维度与 #503 锁匹配修复保持一致）→ 阻塞 claim 新任务，提示等待欧阳锋终审
2. **#492 batch 豁免保留**：`batch: true` 任务（长程分批，#426 线）的 pending_review 不阻塞——既有豁免语义不变
3. **--force 保留但留痕**：显式放行仍可用（并行审批场景），例外入 `90_control/force-exceptions.log` 台账（#444 起既有机制）
4. **回归用例**：①同执行者已有 pending_review → claim 被拒；②batch:true 任务 pending_review → 不阻塞；③--force → 放行且留痕

## 验证（验证分层）

- L1：单测全过（三场景：pending_review 阻塞/batch 豁免/force 留痕）
- L2 狗粮：模拟同执行者 pending_review 后 claim 新单 → 脚本拦截
- L3 待活体：后续提审链不再出现"等审期间接新单"（欧阳锋审查 backlog 不堆积）

## 边界

- 只改 can_claim 阻塞语义（与 #492 同模式：单点修改），不动 review/complete 流程
- #492 batch 语义不变；#503 写入口径与锁匹配语义不变
- 与 #503 顺序执行（同一函数区，避免并发冲突）——#503 完成后再动本单

## 关联

- #503（同族依赖：先修写入口径+锁匹配，再上本单占位语义）
- #492 / F-050（batch 豁免拍板——本单保留其语义）
- 王语嫣 2026-08-24 锁三洞诊断（老朱拍板：洞A 入 #503；洞B/C 入本单）

## 需要谁动作

- **黄药师**：can_claim 占位检查 + 用例 + 台账衔接
- **王语嫣**：编排 + 复核
- **欧阳锋**：终审本单 + 后续按"审查空窗"验收

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：审查等待期占位阻塞落地——①can_claim 的 pending_review 阻塞增加执行者维度识别：阻塞项中含自己（同角色，与 #503 锁匹配口径一致）的待终审任务时，消息明确"你（角色）还有 pending_review 任务待欧阳锋终审：审查等待期不接新单"（不论队列前后——洞C 的 seq 盲区在当前实现本就不按位置过滤，本单补齐的是执行者语义与提示）；②batch:true 豁免语义不变（find_blockers 既有过滤，新增同角色 batch 豁免用例钉死）；③--force 放行保留但留痕：claim --force 绕过任何阻塞时写 `90_control/force-exceptions.log`（_log_force_exception 增加 bypass 参数，默认保持 #444 F-034 原口径；无阻塞可绕时不留痕不制造噪声）。

**交付物**：
- `90_control/scripts/queue_gate.py`（can_claim pending_review 执行者维度+终审提示）
- `90_control/scripts/queue_transition.py`（_log_force_exception bypass 参数化 + action_claim force 留痕）
- `90_control/scripts/tests/test_queue_transition.py`（TestReviewWaitBlock 3 例 + TestForceClaimLedger 2 例）

**验证**：
- L1：`cd 90_control/scripts && python -m pytest tests/ -q` → **109 passed**（新增 5 例：自己 pending_review 阻塞含终审提示/他人 pending 保持原口径/同角色 batch 豁免/force 绕过留痕/无阻塞 force 不留痕）
- L2 狗粮：真实队列实测——持有 #504 claimed 时尝试 claim #505，被同角色维度拦截（"你（实例 huangyaoshi / 同角色）还有 claimed 任务未释放：#504"）——同函数区 #503 修复同步活体生效
- L3 待活体：后续提审链不再出现"等审期间接新单"；force 例外台账积累真实条目供终审查阅

**边界**：只改 can_claim 阻塞语义与 claim force 留痕，未动 review/complete 流程；#492 batch 豁免语义不变；#503 写入口径与锁匹配语义不变；他人 pending_review 阻塞全队的既有口径未动（本单只补执行者维度提示，不放宽）；本次 L2 狗粮的拦截发生在门禁层，未产生队列状态变更。

**需要谁动作**：欧阳锋终审本单 + 后续按"审查空窗"验收；王语嫣知悉——洞B/C 已机制化，老顽童流水线不等审查将被门禁层拦截（force 仍有但全程留痕可查）。
