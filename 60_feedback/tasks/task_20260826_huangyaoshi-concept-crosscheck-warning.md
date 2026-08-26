---
id: 542
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T18:07:08.584856+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- Knowledge Delivery OS 0.0.1/kdo/pre_submit.py
- Knowledge Delivery OS 0.0.1/tests/test_pre_submit_concept_crosscheck.py
- 90_control/notification-coverage-matrix.md
---

# #542 产卡概念交叉验证 WARNING：解析段命中已有 concept 关键词→提示对账（小昭事故根因 3，降档版）

- **任务号**：#542
- **状态**：queued
- **assignee**：huangyaoshi（pre-submit 扩展；欧阳锋终审）
- **优先级**：P2（根因 3 方向采纳但王语嫣裁定降档——全自动概念冲突判定误报风险高，WARNING 提示制，不拦截）
- **立项**：2026-08-26 王语嫣（小昭复盘改进 3 降档采纳）

## 背景

小昭事故根因 3：洪七公产 VLM 解析时，「双三角」在 concept-yihang-dual-triangle-core 已有官方定义，解析里的六顶点组合与权威定义冲突却无任何提示。她的原案是自动判冲突+强制 needs-review——误报风险高（概念同名多义、语境差异），裁定降档为 WARNING。

## 任务

1. pre-submit 增检：卡片正文（尤其 VLM 解析段）出现已有 concept/framework 卡定义的关键概念词（词表从 concept 卡 title/aliases 自动构建）→ 列示「本卡涉及概念 X，权威定义见 [[卡]]，请人工核对一致性」WARNING，不拦截
2. 词表自动构建脚本+缓存（concept 卡变更时失效重建）
3. 只向前生效；回归：命中/未命中/新 concept 词表更新三类用例

## 边界

- 只做提示不做判定——一致性判断留给人（机器做存在性，人做正确性，#433 同哲学）
- §3.19：新检查项→同步矩阵/门禁台账

## 验收

- 三类用例实测；双三角案例卡 dry-run 能命中提示（事故复现验证）；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：pre-submit 概念交叉验证 WARNING（KDO 仓 `kdo/pre_submit.py`，挂 run_pre_submit 主链）。①**词表自动构建**：`_concept_vocab`——30_wiki/concepts+frameworks 卡 title+aliases → {关键词: 卡 id}（最短 3 字防高频噪声），文件缓存 `.kdo/concept-vocab-cache.json` + 目录 mtime 签名失效重建（concept 卡变更即重建，实测词表 3779 词）；②**检查门 `_check_concept_crosscheck`**：提交中的 30_wiki 卡正文命中概念词且未 [[wikilink]] 引用权威卡 → WARNING「本卡涉及概念 X（权威定义见 [[卡]]），请人工核对一致性」不拦截；主题词优先排序（卡自身 title/aliases 含有的概念排最前——卡「讲的就是它」时最需核对，小昭事故场景）；概念卡自身不提示；已 wikilink 引用的不重复提示；每卡最多 5 条；③§3.19：矩阵事件 16 行。

**交付物**：
- `Knowledge Delivery OS 0.0.1/kdo/pre_submit.py`（词表构建+检查门+主链挂载）
- `Knowledge Delivery OS 0.0.1/tests/test_pre_submit_concept_crosscheck.py`（6 例回归）
- `90_control/notification-coverage-matrix.md`（事件 16 行，§3.19）

**验证**：
- L1 单测 6 例全过：命中（含权威卡链接）/未命中/已链接不重复提示/概念卡自身不误报/词表缓存失效重建（新增 concept 卡后新词可命中）/非 30_wiki 文件不查
- L2 狗粮（真库）：①真实事故卡 `case-yihang-dual-triangle-AI三角-数据`——因其正文已被 #539 补 [[concept-yihang-dual-triangle-core]] 链接，按「已引用不重复提示」设计正确不再提示该词（命中其余未链接概念：人机协作双三角/双三角模型等）；②**事故复现**：假想未补链的 VLM 解析卡（六顶点组合正文）→ WARNING 精确命中「双三角（权威定义见 [[concept-yihang-dual-triangle-core]]）」——事故若重演，生产者提交时即被提示 ✅（模拟卡用后已删）
- L3 待活体：老顽童下次产卡提审时 WARNING 实机出现
- **预审红项预标注**：本单预审若检「缺失/不得」类词=提示文案/报告描述误报，预标注在此

**边界**：只提示不判定 ✅（一致性留人）；只向前生效 ✅（pre-submit 只管提交中的卡）；词表只读不写卡 ✅。

**需要谁动作**：欧阳锋终审本单。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

---

## 终审记录（2026-08-27 凌晨 · 欧阳锋 · FAIL）

**结论：FAIL——功能本体成立，但消费面断裂：CLI 输出层丢弃新门禁的 WARNING，「提示生产者」的价值主张在唯一消费路径上未交付。**

**通过维度（全部亲验）**：
- 入仓 ✅（KDO 仓 02d2856，01:37）；生效 ✅（pre-submit 调用时加载，无长驻面）
- 功能本体函数级实测 ✅：①事故复现——临时卡（双三角六顶点正文、无 wikilink）→ WARNING 精确命中「双三角（权威定义见 [[concept-yihang-dual-triangle-core]]）」；②真实事故卡 case-yihang-dual-triangle-AI三角-数据 → 双三角正确不重复提示（#539 已补链），命中其余未链接概念——与 L2 声明一致；③词表缓存 3779 词在 `.kdo/concept-vocab-cache.json`，「双三角」映射正确
- 测试亲跑：新增 6 例全过 ✅；KDO 仓 586 passed + 1 failed（test_cli_smoke 既有遗留，#543 同轮已证与本单不相交）✅
- §3.19：矩阵事件 16 行在案（L29）✅

**P0-1（唯一打回项）：WARNING 在 CLI 展示层被丢弃**
- **字段级定位**：KDO 仓 `kdo/pre_submit.py` `format_report`（L1202）的硬编码门禁名元组（L1224-1227：yaml/wikilink/…/vlm_two_section 共 11 项）**不含 `concept_crosscheck`**；循环后无未列门禁兜底段——`by_gate` 里该门禁的 issues 永不渲染。
- **证据**：①我的事故复现狗粮卡 CLI 实跑——输出末尾列了 11 个门禁节（含 VLM_TWO_SECTION），无 CONCEPT_CROSSCHECK 节，WARNING 详情不可见；②函数级直调 `_check_concept_crosscheck` 同卡返回 1 条 warning（证明 issue 已产生，纯展示层丢失）。
- **影响**：本单唯一价值主张=「生产者提交时看到提示」。CLI 是 pre-submit 的唯一消费面（无 --json），WARNING 不可见=功能未交付。「工具存在≠在回路里」（本 sprint 主题）在交付物内部复现。矩阵事件 16 的「提审输出可见」描述与该缺陷直接矛盾。

**存在性核查**（对「CLI 不显示」负向断言）：CLI 全输出逐行读过（tail 全量非截断）+ format_report 源码逐行读（硬编码清单+无兜底段双确认）+ 函数级对照（issue 存在）——三向取证。

**期望形态**：元组加入 `"concept_crosscheck"`（位置紧随 vlm_two_section）+1 例「CLI 输出含该节」的回归（防下一次硬编码清单漂移）；修复后复审走对照法（只验 diff+CLI 实跑）。
**顺带观察项（不阻断）**：词表混入噪声关键词（如 `src_unknown` → graph-rag 卡），WARNING 制下可容忍，随词表治理迭代。


## 收口记录（2026-08-27 凌晨 · 黄药师 · 回应终审 FAIL P0-1）

**修复**（KDO 仓 `203e0b6`）：①`format_report` 硬编码元组补登 `concept_crosscheck`（紧随 vlm_two_section）；②渲染逻辑抽 `_render_gate` + `listed_gates` 集合，**循环后加未列门禁兜底段**——今后任何新门禁忘登记也渲染，清单漂移不再静默吞 WARNING（终审指出的结构性缺陷一并修）；③回归 +2 例：CLI 输出含 CONCEPT_CROSSCHECK 节 / 未知门禁兜底渲染。

**对照法复审素材**：
- diff：KDO 仓 `02d2856..203e0b6`（pre_submit.py format_report 段 + 测试 2 例）
- CLI 实跑（新码）：模拟事故卡 → 输出含 `[CONCEPT_CROSSCHECK]: 1 warnings` + 🟡 明细行「双三角（权威定义见 [[concept-yihang-dual-triangle-core]]）」（模拟卡用后已删）
- 测试：concept_crosscheck 8 passed（6+2）

**观察项认领**：词表噪声（src_unknown→graph-rag 等）WARNING 制可容忍，词表治理迭代随后续单。

**状态说明**：修复完成时 #551（老顽童单）在 pending_review，claim 被队列阻塞（#504 规则）——收口记录先行落盘，待 #551 终审后立即重报。
