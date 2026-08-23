---
id: 443
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T03:29:41.802001+00:00'
---
# #443 探针可领取通知按 assignee 路由（#421 演进）

- **任务号**：#443
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（#442 立项实证：huangyaoshi 单被通知给 laowantong，黄药师无直达通知；老朱 2026-08-23 指令入队）
- **立项**：2026-08-23 王语嫣（基建任务编排——编排双轨：知识卡片编排 + 基础设施任务编排，本单属后者）

## 任务目标

可领取探针的通知按任务 assignee 路由到正确的接收角色，消除「基建单通知错人」：#442（assignee=huangyaoshi）落队时，探针把「📥 可领取 1 单：#442」发给了 laowantong（2026-08-23 11:16 实证）——黄药师收不到直达通知，老顽童收到无关噪音。

## 缺陷定位（已核实，两处）

1. **路由硬编码**：`kdo-tools/conveyor_probe.py` L245-247 —— `if queue_sig["new_queued"]: ... messages["laowantong"] = ...`，不读队列行 assignee。
2. **通道缺口**：`kdo-tools/.feishu_webhooks.json` 只配了 wangyuyan / laowantong / ouyangfeng 三个角色——无 huangyaoshi 通道，路由修了也无 webhook 可投递。

## 范围

1. **按 assignee 路由**：可领取通知读队列行（或任务单 frontmatter）assignee，经映射表路由：
   - `huangyaoshi` → 黄药师通道
   - `laowantong` / `hermes` / `kimi`（老顽童各实例名，E020 实例分布口径）→ laowantong 通道
   - `wangyuyan` → wangyuyan 通道
   - **未知/缺省 assignee → 回落 laowantong**（保守默认，不静默丢弃）
   - 一单一条按角色聚合，同批多单不同 assignee 拆分投递
2. **补 huangyaoshi 通道**：`.feishu_webhooks.json` 增加黄药师 webhook（key 由黄药师自行配置；**通道缺失时按探针既有行为 dry-run 打印，不阻塞、不误报失败**——与 #421 「配置驱动、缺失降级」设计一致）
3. **映射表写在代码常量或配置**，带注释说明实例名↔角色对应，防下个实例加入时再撞
4. **测试**：+路由用例（huangyaoshi 单→黄药师通道；laowantong/hermes 单→laowantong；未知 assignee→默认回落不崩；通道缺失→dry-run 降级）

## 验证

- dry-run 断言：构造不同 assignee 的 queued 任务，检查 messages 按 role 分桶正确。
- 活体：#443 本单或下一张 huangyaoshi 单落队时，通知到达黄药师通道（本单验收用 #442/#443 状态变化实测）。
- 回归：`pytest kdo-tools/tests/test_conveyor_probe.py` 全过 + 新增用例；夜间静默/幂等/登记逻辑不回归。

## 边界

- 不动 #421 已审设计：单扫描器纪律（检出→登记→通知同源）、幂等、夜间静默、只通知不领取不裁决不流转（F-033 边界）全部保持。
- 不改 REVIEW-PENDING（通知 ouyangfeng）与 PROPOSAL-PENDING（通知 wangyuyan）两条既有路由——它们目标正确，无实证缺陷。
- 交付五字段（F-034）+ 审查意见落盘（F-035）+ commit 入档。

## 关联

- 实证：#442 立项后探针输出「✅ 通知 laowantong：📥 KDO 可领取 1 单：#442」（assignee=huangyaoshi）
- 母单：#421 传送带探针（reviewed，冻结不动，本单为演进）
- 同族：E020 实例名/角色名双口径；F-033 探针闭环演进线
