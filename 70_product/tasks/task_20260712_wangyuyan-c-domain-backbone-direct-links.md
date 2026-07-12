---
assignee: kimi
status: in_progress
updated_at: '2026-07-12T06:29:49.899274+00:00'
reviewed_by: pending
---
# 任务 #162：C 域骨干直连（任务 A，欧阳锋建议书落地）

> 编排：王语嫣 | 生产：老顽童 | 终审：欧阳锋
> 优先级：P1（半天量级；与 #161 不重叠——#161 修 C 域卡出链，本任务修外部 hub→C 域入链主干）
> 建议书：`60_feedback/tasks/task_20260712_ouyangfeng-cdomain-crosslink-backbone-proposal.md`（先读）
> 诊断：6 个外部 hub 卡对 C 域出链全部为 0（grep 坐实）；入向跨域 112 边仅覆盖 21/56 卡，35 张 C 域卡外部完全不可达。桥接卡是图的边缘节点，不等于骨干直连。

## 交付：候选边 ~12-18 条双向 related + 2 处占位死链摘除

**A. 骨干直连候选边**（#161 已 reviewed，织掉部分域外桥——**执行前对 #161 已织边全量 grep，本清单按缺口实况缩减，只补缺的方向**）：

| 候选边 | 语义依据 |
|---|---|
| `framework-一堂-苦练基本功-总纲` ↔ `framework-一堂-业务公式拆解-总纲` | 两域号称「同一套 OS 两个对象」，总纲互不相识（最刺眼缺口） |
| `framework-一堂-基本功-九层金字塔` → 参数冰山/六层逻辑 | 同构映射 |
| `framework-一堂-基本功-四字诀拆建推练` → C 域总纲 | 拆建推练 ↔ 梳理-建公式-探参数-探逻辑-假设管理 |
| `concept-yihang-dual-triangle-core` ↔ C 域总纲 | 六顶点定位 |
| `yt-decision-y-model` ↔ C 域总纲 | 关键假设层操作化 |
| `system-yitang-Y-model-os` → C 域总纲 | Agent OS 底座对接 |
| ABCD 模型卡 ↔ C 域总纲 | ABCD→C 已有 4 边，查 C→ABCD 是否缺 |

**B. 占位死链摘除**（#161 终审裁定 2 并入本任务，顺手件）：`yt-management-business-formula` L31-32 related 里 `pending_unknown ×2` 占位死链——**摘**，一行级修复。同卡 3 条导航边（方法论总图/course-map/course-catalog）已经终审裁定为合法导航边，**不动**。

## 边界与纪律（欧阳锋写死，逐条执行）

1. **执行前逐边 grep 双向确认缺口方向，只补缺的方向，不重复建边**
2. 只动 related + 必要的 Synthesis 一行，不重写既有卡正文（#155 起老规矩）
3. **关系型边不得进豁免清单**——本批直连全是关系型边（同时是对黄药师 #159 扩豁免的红线重申）
4. 全称量词申报（「全部双向闭合」）须附 grep 输出原文
5. 与 #161 并行时按边清单去重：#161 管 C 域卡→域外出链，本任务管 hub→C 域入链；疑似重叠的边以 grep 缺口方向为准

## 验收点（欧阳锋用）

1. 每边双向，grep 两卡 related 互见（附输出原文）
2. 触碰文件逐件 pre-submit PASS
3. lint 增量（T5 回卷后）零新增债
4. 申报集=实动集（协议 2 扫窗自查）
