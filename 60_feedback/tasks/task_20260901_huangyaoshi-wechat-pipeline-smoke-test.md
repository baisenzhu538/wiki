---
id: '585'
title: wechat 采集管线 smoke 测试最小护栏（扣分点2：管线修复无自动化回归断言）
type: task
status: reviewed
priority: P2
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
reviewed_by: 欧阳锋
review_date: '2026-08-31'
grade: A
source_refs:
- 60_feedback/tasks/task_20260831_huangyaoshi-wechat-pipeline-llm-fix.md
- kdo-tools/wechat_knowledge.py
related: '#584'
instance: huangyaoshi
updated_at: '2026-08-31T19:24:21.933210+00:00'
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

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（欧阳锋 2026-09-01）

**结论：PASS / A**

### 验收核验（规格对照法，全部欧阳锋独立复跑，非采信执行报告）

| # | 验收项 | 证据 | 状态 |
|:--|:--|:--|:--|
| 1 | 绿跑：一条命令 exit code 即结论 | 亲跑 `cd kdo-tools && python test_wechat_knowledge_smoke.py` → 6/6 通过，EXIT=0，断言明细逐条输出 | ✅ |
| 2 | pytest 单文件兼容 | 亲跑 `python -m pytest kdo-tools/test_wechat_knowledge_smoke.py -q` → 6 passed in 0.11s | ✅ |
| 3 | 红绿自证（测试自身有效性） | 亲跑 monkeypatch `SKELETON_MARKERS=('<!--',)` 模拟泛匹配回归 → 3/6 红 EXIT=1，红项=`test_skeleton_marker_exact_match`（完整卡误判为骨架）+`test_skip_complete_card_no_llm_call`（完整卡仍调 LLM 1 次）+`test_skeleton_card_triggers_rerun`——断言精确命中 #584 两修复点，报错文案与执行报告声称逐字一致 | ✅ |
| 4 | 样例独立性（不碰真库） | 断言用例全落 tempfile 临时目录（红跑输出实证 `%TEMP%\tmp*` 路径），真库 00_inbox/wechat-collect/ 零触碰；LLM 调用全 mock（绿跑中 llm_summarize 均为桩返回，零网络零 key） | ✅ |
| 5 | 主逻辑零改动（边界②） | `git diff HEAD -- kdo-tools/wechat_knowledge.py kdo-tools/wechat_promote.py` 空输出——wechat_knowledge / wechat_promote 两主逻辑文件工作区无脏改动 | ✅ |
| 6 | 双副本覆盖（任务单第 4 条） | 亲读 40_outputs/code/scripts/wechat_knowledge.py：runpy 转发桩指向 `kdo-tools/wechat_knowledge.py` 同一真身（L18 `_CANON` 路径解析逐行核对），桩=真身同码，对真身测即对桩测——执行报告「参数化路径无必要」的边界声明成立 | ✅ |
| 7 | 基建登记（§3.19 纪律） | `90_control/infrastructure-inventory.md` L131 已登记 smoke 脚本一行，交付面与差集一致 | ✅ |

### 审查意见

- **加分项**：施工期自抓样例缺陷（GOOD_CARD 196 字 < MIN_BODY_CHARS 200 被 promote 门禁反向拦截）并如实写进执行报告——红绿自证不是事后补做，测试先抓了自己的样例问题，这是测试有效性最硬的实证。
- **口径确认**：`_content_issues` 纯函数直测不跑 promote_case 全链路，符合任务单边界①（只测判定逻辑，不测 LLM 输出质量/不碰真库目录态）——非偷工。
- 扣分点无阻断项。对比 #584（A-）本单交付面更小且六断言全部实证可复跑，给 **A**。

**终审落点**：task_20260901_huangyaoshi-wechat-pipeline-smoke-test.md（本节）；队列流转由 queue_transition.py review 完成。
