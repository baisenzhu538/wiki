---
id: 517
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-25T02:37:24.667268+00:00'
version: v0.1
instance: huangyaoshi
---

# #517 pre-submit 补「正文 src_unknown 占位」检查项（新卡 ERROR / 存量 WARNING / 只向前生效）

- **任务号**：#517
- **状态**：queued
- **assignee**：huangyaoshi（kdo pre-submit 门禁扩展；欧阳锋终审）
- **优先级**：P1（门禁盲区实证：22,871 行/1,524 张卡正文 src_unknown，pre-submit 零拦截还附安慰语）
- **立项**：2026-08-25 王语嫣（欧阳锋建议书 `diag_20260825_ouyangfeng-src-unknown-body-gate.md` R1 裁定采纳）

## 背景

graph-rag 域 11 处 src_unknown 是单卡缺陷，但背后现象是基建类：**正文 src_unknown 占位存量 22,871 行 / 1,524 张卡（超半数卡）**，`kdo pre-submit` 对此零拦截（PASS 还附「修得干净」安慰语——误判成本方向反了：机器少拦+安慰语=漏放还安抚，违反 charter §3.17 红线 4 误判成本不对称）。欧阳锋 R1 口径：WARNING 起步、新卡 ERROR、只向前生效。

## 任务

1. `kdo pre-submit` 新增检查项「正文 src_unknown 占位」：
   - **新卡（created_at ≥ 本门禁上线日）**：ERROR（拦截）
   - **存量卡**：WARNING（不拦截，计数输出）
   - 只向前生效，存量不回扫拦截（存量治理由 #518 分批承接）
2. 检查范围=正文（frontmatter 的 source_refs 已有既有检查，本项查正文占位符 `src_unknown` 及同族占位写法——占位词表欧阳锋建议书/既有 lint 词表对齐）
3. 回归用例：含正文占位的测试卡新卡 ERROR、存量 WARNING；不含占位不误报
4. 安慰语口径顺带核：门禁输出不得在存在 WARNING 时附「修得干净」类全清措辞（§3.11 归零声明纪律同族）

## 验证（验证分层）

- L1：单测——新卡占位 ERROR / 存量 WARNING / 清洁卡 PASS 三分支
- L2 狗粮：拿 1,524 张存量清单抽查若干跑 pre-submit，WARNING 计数与实测一致
- L3 待活体：下一张含占位新卡被当场拦下（不再带安慰语漏放）

## 边界

- 只加检查项，不动存量卡内容（治理归 #518）
- 占位词表先小后大（#433 词表演进先例）
- 本单是门禁层；审查侧过渡口径（R3：门禁上线前欧阳锋见正文占位即 FAIL）已同步生效，不依赖本单

## 关联

- 欧阳锋建议书 R1（存量实测 22,871 行/1,524 卡）
- #498 复审观察项重分类（触发源）；#426 分批模式（#518 参照）
- charter §3.17 红线 4（误判成本不对称）/ §3.11（归零声明纪律）

## 需要谁动作

- **黄药师**：pre-submit 检查项 + 回归
- **欧阳锋**：终审本单；过渡口径（见占位即 FAIL）已生效
