---
id: 420
assignee: wangyuyan
status: queued
updated_at: '2026-08-22T17:05:00+08:00'
---
# #420 工厂停车场收口（6 份 → 单一 control/parking-lot.md）

- **任务号**：#420
- **状态**：queued
- **assignee**：wangyuyan（编排执行；黄药师配合脚本）
- **优先级**：P1
- **立项**：2026-08-22 王语嫣（会诊 B4-4 拍板；风清扬 §14.5 方案）

## 任务目标

6 份旧停车场（parking-lot-{huangyaoshi,ouyangfeng,wangyuyan}.md + 30_wiki/projects/parking-lot.md + laowantong/parking-lot.md + .agent/parking-lot-laowantong.md）合并为单一 `control/parking-lot.md`（90_control 未重排前暂落 90_control/parking-lot.md）。

## 动作（按风清扬 §14.5 方案）

1. 抽离 A 类（工厂自迭代）条目约 50 条 → 8 主题收敛 → F-xxx 统一编号
2. 生命周期状态机：待讨论→会诊→拍板→入 production-queue→已关闭
3. 清账：已闭环项归档（P-28/P-30/P-31/P2-DYN-01/O-8/O-13/O-14 等已落地仍挂账的）；被会诊拍板吸收的关闭；重复登记去重（P-5/P-9 多库、P-32/P2-DYN-02 skill 漂移、O-15/O-16 MCP、LW-PL-003/PL-013/O-14 lint 债等）
4. 残留工具名按 B4-2 口径处理
5. B 类（领域生产）/C 类（业务项目）不进工厂停车场

## 验收

- 单一停车场落盘，F-xxx 编号无重复；旧 6 份标记 DEPRECATED 指向新址
- 清账明细（每条：原编号→处置）附执行报告
- 欧阳锋终审抽"去重正确性"；commit 入档
