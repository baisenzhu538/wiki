---
id: task_20260705_wangyuyan-canvas-agent-spec-v3-upgrade
type: task
status: done
assignee: 王语嫣
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-05
updated_at: 2026-07-05
source_refs:
- 60_feedback/diagnosis/diag_20260705_yai-agent-distillation.md
- 60_feedback/diagnosis/diag_20260705_yai-agent-distillation-v2.md
- 00_inbox/人机协作双三角/YAI双三角agent对话记录.md
- 00_inbox/人机协作双三角/一堂双三角partner的对话记录20260705.md
related:
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[tool-yihang-dual-triangle-canvas]]'
---

# 任务 #111：画布 Agent agent-spec v3 升级——注入 YAI 蒸馏方法论

## 来源

两轮 YAI Partner 对话蒸馏提取的 13 个 Agent 能力模式。

## 升级内容

### 第一轮蒸馏注入（7 项）

1. **六要素状态标记体系**：已确认/有方向/偏薄/暂放 四态 + 状态变化追踪
2. **三级优先级框架**：主挖角/副挖角/贯穿约束/暂放，每级有不同深挖轮数
3. **0-10 信心打分 + 保底策略**：≤5 分自动触发最小实践版本建议
4. **追问升级链**："我能验证"→"其他AI能接手"→"3年后还能接手"
5. **备忘录输出 9 节标准格式**
6. **画布版本管理**：v0.1 → v0.4 增量更新模式
7. **里程碑计划自动生成**：M1-M6 模板

### 第二轮蒸馏注入（6 项）

8. **创造力主动推演**：其他五角够密时，基于上下文主动推演 2-4 个方向
9. **场景边界重校准**：识别"用户改变了前提条件"→停→确认→广播
10. **限时数据源标记**：有时间窗口的数据源自动触发优先级重组
11. **诚实边界声明**：信息不在上下文时，给框架不给判断（TCPR C 角色）
12. **3年视角审美审计**："未来的人会骂什么"→倒推现在做什么
13. **里程碑→日级执行脚本**：当用户问"这周能跑吗"，自动压缩到日级

## 产出

- `agent-spec-dual-triangle-canvas-filler.md` v2 → v3
- 升级理由 + 每项能力的具体追问模板和触发条件

## 验收

- agent-spec v3 包含全部 13 项能力模式
- 每项有触发条件 + 追问模板
- `kdo pre-submit` PASS
- 欧阳锋终审通过
