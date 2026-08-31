---
id: '585'
title: wechat 采集管线 smoke 测试最小护栏（扣分点2：管线修复无自动化回归断言）
type: task
status: in_progress
priority: P2
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
source_refs:
- 60_feedback/tasks/task_20260831_huangyaoshi-wechat-pipeline-llm-fix.md
- kdo-tools/wechat_knowledge.py
related: '#584'
instance: huangyaoshi
updated_at: '2026-08-31T17:54:23.926878+00:00'
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

## 执行报告（黄药师 2026-09-01）

**完成内容**：wechat 采集管线 smoke 最小护栏落地——`kdo-tools/test_wechat_knowledge_smoke.py` 6 项断言全覆盖任务单三项断言面（skip 前置 / SKELETON_MARKERS 精确匹配 / #380 `_content_issues` 拦截联动），样例全落 tempfile 临时目录零碰真库，LLM 调用全 mock 零网络零 key，一条命令 exit code 即结论，pytest 单文件亦可收集（6 passed）。

**交付物**：
- `kdo-tools/test_wechat_knowledge_smoke.py`（新建，smoke 主体+红绿自证用法入 docstring）
- `90_control/infrastructure-inventory.md`（§3b kdo-tools 辅助族补登记一行，§3.19 登记纪律）

**验证**（全部实测，非推断）：
- 绿：`cd kdo-tools && python test_wechat_knowledge_smoke.py` → 6/6 通过，EXIT=0
- 绿（pytest 兼容）：`python -m pytest test_wechat_knowledge_smoke.py -q` → 6 passed in 0.10s
- 红绿自证（任务单验证节①）：monkeypatch `wk.SKELETON_MARKERS=('<!--',)` 模拟改回泛匹配 → 3/6 红 EXIT=1，核心用例 `test_skeleton_marker_exact_match` 报「完整卡被误判为骨架」、`test_skip_complete_card_no_llm_call` 报「完整卡仍调了 LLM 1 次」——断言对 #584 修复点敏感有效
- 施工期自抓一处：`GOOD_CARD` 样例正文 196 字 < `MIN_BODY_CHARS` 200，被 `test_promote_gate_intercepts_fail_placeholder` 反向拦截——补齐样例后转绿（测试先抓了我自己的样例缺陷）

**边界**：
- 只测判定逻辑不测 LLM 输出质量（任务单边界①），`_content_issues` 以纯函数直测，未跑 promote_case 全链路（其目录态依赖真库，超出 smoke 最小口径）
- 任务单第 4 条「双副本分别跑」未做：#584 已把 40_outputs 双副本收口为 runpy 转发桩（桩=真身同码），对真身测即对桩测，参数化路径无必要；若未来桩机制变更再补
- 未动 wechat_knowledge.py / wechat_promote.py 主逻辑一行（任务单边界②）

**需要谁动作**：欧阳锋按验证节终审本单（重点复核红绿自证方法与样例独立性）。
