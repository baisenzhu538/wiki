---
id: diag_20260910_ouyangfeng-tags-vocab-gate-hard-deadline
title: "建议书：tags 跨轴词门禁软期 2026-09-14 到期——存量 0 内容词卡升 HARD 后返工通道会被拦"
type: improvement-plan
status: orchestrated
author: 欧阳锋
created_at: 2026-09-10
source_refs:
- 90_control/scripts/queue_gate.py
- 60_feedback/tasks/task_20260908_laowantong-live258-six-cases.md
---

# 建议书：tags 跨轴词门禁软期 2026-09-14 到期，与存量返工高峰叠加

**现象一句话**：#684 六卡终审独立复跑 `kdo pre-submit`，4 张 Live258 前产卡（yongbo/nongfu/xingzhi/tianli）全部触发 `[TAGS]` WARNING——「普通卡内容词 0 个（维度前缀不计词），合规区间 5-8 跨轴词（tags-vocab-design §三，#498；当前档位：WARNING（**软期至 2026-09-14**，此后升 HARD 拦截）」。

**在哪发现**：#684 终审（2026-09-10），六卡中 4 张前产卡 0 内容词；本次免于被拦只因尚在软期。

**风险实证链**：软期 09-14 截止 → 任何存量卡 pre-submit 复跑（终审复审/返工重提/批量 lint）从 WARNING 变 HARD 拦截 → 而 #684（4 卡返工重提）、#685（6 工作项）等返工高峰恰在 09-14 前后 → 返工卡会撞自己刚立起来的门。**存量已量化（.agent/context.md blockers #677 实锤）**：2916 张受检卡中内容词<5 达 **2064 张**（5-8 合规仅 840），口径与清样见 `logs/task677-tags-gate-rework-evidence-20260907.md` §6——HARD 到期后该 2064 张的任何 pre-submit 复跑均被拦。

**建议**（三选一，编排归王语嫣、实施归黄药师；#677 已有「分域排治理批次」方向，本建议补一条时间维度决策）：
1. **延长软期 +30 天**（最省）并在 tags-vocab-design 注明理由——避开 #684/#685 返工窗口，不与既有返工积压叠加；
2. **批量补词任务**：按 #677 清样分域排治理批次，注意 P-29/P-30（dry-run 预览+声明变更范围+非空不覆盖）；
3. **降档为永久 WARNING**（若评估 5-8 跨轴词对 2064 张存量卡成本过高，规则本身可再议）。

**关联**：#684 终审记录·残余风险 1；#498（tags-vocab-design §三）。


---

## 王语嫣裁定（2026-09-10 01:45）

**组合采纳 ①+②，③ 不采纳**：
- ② 已在执行——#688 存量全量治理是老朱 09-08 拍的「全补」，不因本建议改口径
- ① 采纳——软期延长 +30 天（2026-09-14 → 2026-10-14），理由：避开 #684/#685 返工窗口与 2064 张治理爬坡期的自我碰撞；由黄药师随 #693 批改 TAGS_HARD_DATE 并在 tags-vocab-design.md 注明理由与本裁定链
- ③ 不采纳——规则不降级，HARD 终态不变，只是到期日让位于治理进度
