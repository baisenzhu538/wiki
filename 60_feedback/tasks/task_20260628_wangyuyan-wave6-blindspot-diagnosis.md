---
id: task_20260628_wangyuyan-wave6-blindspot-diagnosis
type: task
status: queued
assignee: 王语嫣
priority: P2
created_at: 2026-06-28
updated_at: 2026-06-28
reviewer: 欧阳锋
source_refs:
- .agent/kb-evolution-direction.md
- 60_feedback/methods/method-dialogue-driven-kb-evolution.md
- 60_feedback/auto/kb-evolution-signals-weekly.md
---

# Wave 6 新盲区探索诊断

## 目标

在 wave5（CI 框架 / SATs / 多智能体架构）完成并入库后，识别下一批值得建设的新盲区，产出诊断报告并拆分为可入队的生产任务。

## 输入

1. `.agent/kb-evolution-direction.md` — 长期方向
2. `60_feedback/methods/method-dialogue-driven-kb-evolution.md` — 五环模型
3. `60_feedback/methods/method-systematic-dialogue-kb-evolution-hybrid.md` — 冷热混合模型
4. `60_feedback/auto/kb-evolution-signals-weekly.md` — 系统扫描周报（如已生成）
5. 当前队列状态：`production-queue.md`

## 诊断步骤

1. **读周报**：查看最近一次 `kb-evolution-signals-weekly` 报告，找出高密度未覆盖主题、跨域桥接机会、孤立概念簇。
2. **对话回顾**：回顾近期用户与 Agent 的对话记录（尤其是一堂五步法、AI 协作、商业预判、产品内核、渠道增长之外的域），识别反复出现但未卡片化的概念。
3. **盲区候选清单**：列出 3-5 个候选盲区，每个给一句话商业价值和与现有域的桥接关系。
4. **优先级排序**：按以下维度打分（1-5）：
   - 与用户长期目标的关联度
   - 与现有卡片的桥接潜力
   - 素材可获取性
   - 生产可行性（2-3 天内可出首批卡）
5. **选定 1-2 个盲区**，写 `diag_20260628_wangyuyan-wave6-<主题>.md`，含：
   - 盲区定义
   - 为什么现在建
   - 建议建设的 3-5 张卡片（id / type / title / 关键问题）
   - 依赖与风险
   - 建议 assignee

## 输出

- 诊断报告：`60_feedback/diags/diag_20260628_wangyuyan-wave6-<主题>.md`
- 入队建议：在 `production-queue.md` 末尾新增 wave6 任务条目（状态 `queued`）
- 不直接生产卡片，只负责诊断和任务拆分

## 时间窗口

建议在 lint Batch 2 进行期间（约 1-2 天）完成诊断，以便老顽童在 Batch 2 收尾后无缝衔接 wave6 生产。
