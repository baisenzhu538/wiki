---
id: 559
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T02:05:00+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
---

# #559 profile 配置巡检 + manual 残留止血 + SOUL 真相源指针

- **任务号**：#559
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（止血项当下实证：huangyaoshi/laowantong 两 profile 仍 manual）
- **立项**：2026-08-27 王语嫣（飞书欧阳锋洞察报告 P1-1/P1-3 裁定——「知道≠生效」：段王爷 dk 卡 08-09 沉淀修复方案，ouyangfeng profile 08-26 才修，且**只修了一个**——半套修改实证）

## 任务

1. **止血**：全部 hermes profile 核查 `approvals.mode`——manual 一律改 smart（08-27 实测残留：huangyaoshi、laowantong 两个；其他逐个复核）
2. **配置巡检**：挂 kdo-health-daily（日级）——各 profile 的 approvals.mode / timeout / allowlist 与基线核对，漂移即报（落 health-check 报告）
3. **SOUL.md 防漂移**：各 profile SOUL.md 角色定义行加注「以 `90_control/kdo-charter-v0.1-draft.md` §2.6 为准」——单一真相源指针（charter §3.11 / B2-2）

## 边界

- 只动 hermes profiles 配置层，不动各角色 .agent context（那是 wiki 侧真相源，已对齐）
- 巡检只报漂移不自动改（配置变更留人）

## 验收

- 全 profile approvals.mode=smart 实测；巡检首跑落盘；SOUL.md 指针全 profile 覆盖；欧阳锋终审
