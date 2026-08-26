---
id: 542
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T17:23:02.060369+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/scripts/
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
