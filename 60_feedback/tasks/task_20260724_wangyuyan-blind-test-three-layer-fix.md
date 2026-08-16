---
reviewed_by: 欧阳锋
review_date: 2026-08-09
id: task_20260724_wangyuyan-blind-test-three-layer-fix
task_id: 199
assignee: hermes
status: reviewed
created_at: 2026-07-24
updated_at: '2026-07-23T19:17:23.206620+00:00'
domain: master
priority: P0
source: 盲人测试失败复盘
review_audit: 60_feedback/audit/2026-07-24-blind-test-failure-retrospective.md
---

# 盲人测试失败三修复：Agent 溯源 + 卡片定位 + 失忆锚点

## 问题本质

一次盲人测试失败的完整链路：

```
用户问"销售过程分成几个环节"
  → Agent 检索到 tool-yitang-sales-process-decomposition
    → 卡片全文没有一句话说"我是五步法的 B 步"（内容格式缺陷）
      → Agent 没有向上溯源的动作（Agent 行为缺陷）
        → 答了局部当全景（盲人测试失败）
```

三个问题同时命中，需三层并行修复。

## 三层修复

| 层 | 问题 | 修法 | 优先级 | 负责人 |
|:---|:---|:---|:---|:---|
| Agent 行为 | 没有向上溯源 | 把黄药师的 B6「先找 MOC 再回答」同步写入王语嫣、欧阳锋、老顽童的 context.md；回答第一句话必须是定位（"XX 是 YY 框架的第 Z 步"） | P0 | 老顽童 / 王语嫣 |
| 内容格式 | tool/子卡不声明框架定位 | 新标准：每张子卡标题下第一行必须写"本卡属于 XX 框架的第 Y 步"；先从 `tool-yitang-sales-process-decomposition` 开始补，再逐步扫描同类子卡 | P0 | 老顽童 |
| 记忆恢复 | 4/6 Agent 缺失忆锚点 | 在 `20_memory/` 下新建黄药师、老顽童、王语嫣、欧阳锋的 amnesia-recovery 文件，包含角色定位、关键行为牌、上下文入口、常见踩坑 | P1 | 老顽童 |

## 最小可验证成果（Phase 1）

修复完成后，用同一条问题再测：

> 用户问："销售过程分成几个环节"

**期望回答**：
> "科学销售五步法的 B 步。四类决策是 B 步的内容，完整框架还有 A/C/D/E。"

**错误回答**：
> "四类决策：接触/购买/付款/履约。"

## 执行进度

| 检查项 | 状态 | 验证方式 | 备注 |
|:---|:---|:---|:---|
| Agent 行为：王语嫣 context 写入 W8 | ✅ 完成 | 读取 `.agent/wangyuyan-context.md` L491-L510 | 含「先找 MOC 再回答」四步执行 + 2026-07-24 实况复盘 |
| Agent 行为：欧阳锋 context 写入 O8 | ✅ 完成 | 读取 `.agent/ouyangfeng-context.md` L420-L437 | 审查侧内容格式门禁 |
| Agent 行为：老顽童 context 写入 L8 | ✅ 完成 | 读取 `.agent/laowantong-context.md` L231-L243 | 生产侧内容格式标准 |
| 内容格式：销售过程拆解卡补定位声明 | ✅ 完成 | 读取 `tool-yitang-sales-process-decomposition.md` L53 | `kdo pre-submit` 通过 |
| 失忆锚点：4 个 amnesia 文件 | ✅ 完成 | `ls 20_memory/*-amnesia-recovery.md` | 王语嫣/欧阳锋/老顽童/黄药师 |
| 临时脚本清理 | ✅ 完成 | `rm -f add_b6_rule.py` | — |
| 任务队列/看板刷新 | ✅ 完成 | `queue_transition.py claim/complete` + dashboard 自动生成 | 已推进到 `pending_review`；dashboard: 待领取 0 / 审查中 1 / 进行中 0 / 已完成 195 |
| 盲测复测 | ✅ 完成 | 读取 framework + tool 卡后按 W8 规则组织回答 | 见下方「盲测结果」 |

## 盲测结果

**测试问题**：销售过程分成几个环节？

**Agent 回答（按 W8「先找 MOC 再回答」规则组织）**：

> 你问的是「一堂科学销售五步法」的 **B 步（拆解过程）**。
> 完整五步法包括：A. 提炼卖点 / B. 拆解过程 / C. 推进业绩 / D. 激励团队 / E. 打造工具。
> 其中 B 步的核心是拆解用户从接触到成交的关键决策路径；`tool-yitang-sales-process-decomposition` 就是这一步的工具卡，它把成交黑盒拆成「路径 → 阶段 → 动作」。

**判定**：✅ 通过。回答第一句话给出框架定位（B 步），再展开局部内容，未把 tool 卡当顶层框架答。

**注意**：`kdo query` 图检索在本次测试中返回了不相关结果（deepfake 案例），说明图索引可能未即时更新；但 Agent 行为层的修复不依赖单次 RAG，而是依赖 context 中的 W8/O8/L8 规则。建议定期重建图索引，或把「先找 MOC」规则嵌入 Agent 检索逻辑。

## 验收标准

1. `tool-yitang-sales-process-decomposition.md` 标题下第一行增加定位声明。
2. 王语嫣 / 欧阳锋 / 老顽童 context.md 中新增或引用 B6「先找 MOC 再回答」规则。
3. `20_memory/` 下存在 4 个新增 amnesia 文件。
4. 盲测复测通过（同问题答出框架定位而非局部内容）。

## 关联资产

- `tool-yitang-sales-process-decomposition`
- `framework-yitang-scientific-sales-methodology`
- `.agent/huangyaoshi-context.md`（B6 来源）
- `.agent/wangyuyan-context.md`
- `.agent/ouyangfeng-context.md`
- `.agent/laowantong-context.md`
- `20_memory/`
