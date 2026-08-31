---
id: '585'
title: wechat 采集管线 smoke 测试最小护栏（扣分点2：管线修复无自动化回归断言）
type: task
status: queued
priority: P2
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
source_refs:
- 60_feedback/tasks/task_20260831_huangyaoshi-wechat-pipeline-llm-fix.md
- kdo-tools/wechat_knowledge.py
related: '#584'
---

# #585 wechat 管线 smoke 测试最小护栏

## 背景

#584 终审 PASS A-（欧阳锋 2026-09-01），扣分点 2：「无自动化回归护栏：管线修复验证全靠手工实跑（py_compile 通过但无测试断言），下次改动仍无机器兜底——记停车场（O 系列），另立项最小 smoke 测试单」。本单即该最小 smoke 测试单，欧阳锋终审时明示要求立项，编排层落地。

## 任务

1. 构造最小样例文件集（临时目录，不碰真库）：
   - 含 `<!-- LLM 总结失败，请重试 -->` 骨架标记的卡（应触发 `_needs_rerun` 重跑判定）
   - 已知识化完整卡（应被 skip 判定跳过，且 LLM 不被调用——skip 前置已由 #584 根治，此处固化断言）
   - 空骨架/无标记边界件
2. 断言项（smoke 级，不追求覆盖率）：
   - skip 判定：完整卡被跳过、骨架卡被重跑（#584 L158-164 前置逻辑回归）
   - 骨架标记精确匹配：SKELETON_MARKERS 命中/不命中（`<!--` 泛匹配误判不复发）
   - E040/内容校验联动：失败占位产出会被 #380 校验拦截（可用桩替代真 LLM 调用）
3. 一条命令可跑：`python kdo-tools/test_wechat_knowledge_smoke.py`（或 pytest 单文件），exit code 即结论，输出断言明细
4. 注册副本（40_outputs/code/scripts/）同步机制落定后（#584 待办③），smoke 须能对双副本分别跑（参数化路径即可，不强求）

## 验证

- smoke 全绿 + 故意破坏一处（如临时改回泛匹配）验证测试能红（测试自身的有效性核验）
- 不依赖网络/LLM key：LLM 调用全部 mock/桩化

## 边界

- 只测管线判定逻辑，不测 LLM 输出质量（那是 #380 内容校验的域）
- 不动 wechat_knowledge.py 主逻辑（发现 bug 另立 bugfix 单，不在本单内顺手修）
- P2 优先级，排在黄药师在册基建单之后，不插队

## 关联

- #584（母单，终审扣分点 2 出处）
- #380（偶遇管线 promote 校验，拦截层先例）
- #522（E040 交付物入仓门禁，交付纪律）

## 需要谁动作

- 黄药师：施工（smoke 脚本+断言+红绿验证）
- 欧阳锋：终审
