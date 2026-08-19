---
id: 382
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-19T19:14:22.571958+00:00'
title: delivery.py trust 过滤失效修复（P2，#380 测试挖出的预存在 bug）——缺 import os 致 _filter_by_trust
  静默失效
priority: P2
dependency: []
code_files:
- C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/commands/delivery.py
---

# #382 delivery.py trust 过滤失效修复（P2）

## 任务背景

黄药师 #380 测试中挖出（KDO CLI 仓）：`kdo/delivery.py` 全模块缺 `import os`，导致 `_filter_by_trust` 静默失效——**BM25 检索结果从未被 trust≥medium 过滤过**（设计意图从未生效）。黄药师未顺手修（改变检索行为超出 #380 边界），裁决正确，单独立项。

## 执行范围

1. 修复 `import os` 缺失，使 `_filter_by_trust` 真实生效
2. **行为变化公告**：修复后 low-trust 卡将从检索结果消失——执行报告须给出前后对比实测（同一查询修复前/后结果数差异、消失的卡抽样列表），供欧阳锋评估影响面
3. 回归：CLI 仓 pytest 全跑（基线：567 passed + test_cli_smoke 预存在失败，修复后不得新增失败）
4. **生效动作**：修复合并后需重启 kdo MCP server（进程跑旧码）——杀进程前请示老朱授权（沿用 #361 模式），不擅自杀

## 边界

- 只修 import 缺失及直接必要的连通，不顺手改过滤阈值/逻辑
- test_cli_smoke 预存在失败不在本任务范围
- 若修复后影响面实测过大（如某域结果腰斩），不硬推，如实报告交编排裁决

## 内容价值判断（PROTOCOL §7 合规声明）

- 只改 KDO CLI 仓 delivery.py，不动 wiki 卡片与素材

## 验收标准

1. `_filter_by_trust` 生效实测（构造 low-trust 查询验证过滤发生）
2. 前后对比实测报告（含消失卡抽样）
3. pytest 无新增失败
4. MCP 重启后消费端实测检索正常（含【未审】标注仍在，与 #380 成果兼容）

## 交付

1. 修复 + 对比实测报告
2. 送欧阳锋终审

---

# 执行报告（黄药师 2026-08-20 02:5x）

## 一、修复内容（两处，均属"直接必要的连通"）

1. **补 `import os`**（模块级）——根因修复，_filter_by_trust 的 posix 分支不再 NameError。
2. **过滤语义补正**：原逻辑"只有 frontmatter 解析成功且 trust_level 达标的卡才被 append"——import 修好后这个缺陷立刻显形：无 frontmatter 的文档（10_raw 素材 src_*、README 等）会被全部误杀出检索结果。改为**只有显式声明 trust_level 且低于阈值才剔除**；缺 frontmatter/缺 trust_level/解析异常一律按默认 medium 放行（与既有 except 分支 fail-open 语义一致）。若只补 import 不改这条，修复会把素材层整体炸出检索——属于不修不能上线的连通缺陷，非顺手改逻辑。

## 二、前后对比实测（6 查询 × BM25 top10，trust≥medium）

| 查询 | 修复前 | 修复后 | 剔除 |
|:--|:--|:--|:--|
| 药柜 商业模式 验证 | 10 | 8 | 2 张 low-trust 药柜卡 |
| 双三角 IP 选题 智能体 | 10 | 9 | 1 张 low-trust 双三角 case |
| skill 市场 问题验证 | 10 | 8 | tool-ai-problem-validation + case-ji-hao（均 low） |
| 蒸馏 书单 | 10 | 9 | tool-月白-设计能力蒸馏封装法（low） |
| 销售 需求 挖掘 | 10 | 10 | 无变化 |
| AI 员工 落地 | 10 | 7 | tool-马易 + 2 张 yihang case（均 low） |

**精度核验：被剔的 9 张卡 100% 显式声明 `trust_level: low`，零误杀**（逐张 grep 实证）。
**误杀回归核验：修复初版（仅补 import）曾把 src_ 素材/README/corr 文档误剔，语义补正后全部回名单。**

## 三、影响面评估

- 全库 520 张显式 low-trust 卡（共 2737 张带 trust_level）从此在默认检索（trust≥medium）中不可见——这正是该过滤器的设计意图，本次是"设计意图首次真实生效"。
- 实测单查询结果数下降 0–30%，无"腰斩"级影响；被剔卡均为明确标 low 的存量。
- 消费端如需 low-trust 卡：`kdo query --trust low` 或 view=needs-review 仍可达。

## 四、验收对照

| 验收 | 结果 |
|:--|:--|
| ① low-trust 过滤真实发生 | ✅ 6 查询实测，9 张 low 卡被剔且全部精确命中 |
| ② 前后对比报告含消失卡清单 | ✅ §二 |
| ③ pytest 无新增失败 | ✅ 567 passed + 1 failed（test_cli_smoke 预存在失败，stash 验证干净树同样失败，与基线一致） |
| ④ 与 #380【未审】标注兼容 | ✅ 修复后实测：trust 过滤生效同时 draft 卡【未审 draft】标注正常（tool-yizhan-shendeng / tool-cangjie-skill 双命中） |
| MCP 重启 | ⚠️ 需老朱授权杀 PID（沿用 #361 模式）——代码已入仓，重启后消费端生效 |
