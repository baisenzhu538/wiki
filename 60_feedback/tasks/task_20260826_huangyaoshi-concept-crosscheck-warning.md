---
id: 542
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T17:37:38.581282+00:00'
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
