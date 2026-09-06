---
id: task_20260907_huangyaoshi-dk-graph-index-gap
title: "graph_index 补录 dark-knowledges 族 332 张（0/332 实证——dk 卡图检索通道系统性失明，检索失明第三层根因）"
seq: 671
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 欧阳锋建议书 diag_20260907_ouyangfeng-dark-knowledges-graph-index-gap（0/332 path_map 实证）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T19:09:57.699655+00:00'
evidence: logs/dk-graph-coverage-evidence-20260907.log
---

# #671 graph_index 补录 dk 族（黄药师）

## 实证（欧阳锋 #668 终审时独立复测发现）
graph_state.json path_map 含 frameworks/concepts/cases/tools/decisions 等，但 **dark-knowledges 0/332**——dk 卡在 kdo query 的 graph 检索通道系统性失明（hybrid RRF 的 graph 分量缺失使 dk 语义排序沉底；BM25 分量有命中但被稀释）。

## 修法
1. graph_index 构建脚本排查 dark-knowledges 目录被排除的原因（glob 漏/过滤规则误伤）
2. 补录 332 张 dk 入 graph index
3. **防复发**：索引覆盖率检查进 channel_health 或独立探针（30_wiki 各子目录卡数 vs 索引内数，缺口>0 报警）

## 验收
path_map dk 命中 332/332；kdo query 抽 5 张 dk 标题均召回；探针上线；回归不红。

## kdo query 检索记录（宪法第六条 #669）

| 查询词 | 命中数 | 日期 |
|:--|:--|:--|
| `kdo query "dark-knowledges 暗知识 卡片图索引 graph index 覆盖" --limit 8` | 7 | 2026-09-07 |
| `kdo query "AI 预言的保质期" --limit 10`（dk 标题召回实测） | 本卡命中 [0.03] | 2026-09-07 |
| `kdo query "压力激发：灵感在压力下产生" --limit 10`（同上） | 本卡命中 [0.03] | 2026-09-07 |
| `kdo query "Agent 并行设计系统：五 Agent 同时做图 + 设计规范=能力复制介质" --limit 10`（同上） | 本卡命中 [0.02] | 2026-09-07 |
| `kdo query "「暗知识：Feature不是学会的，是用会的」" --limit 10`（同上） | 本卡命中 [0.03] | 2026-09-07 |
| `kdo query "王欢暗知识：Spec 陷阱——过度拆解会锁死 AI 上限" --limit 10`（同上） | 本卡命中 [0.03] | 2026-09-07 |
| `kdo query "过早细化陷阱：在验证前追求完美" --limit 30`（第 6 张，top10 外靠后） | 本卡命中 [0.02] | 2026-09-07 |

## 根因（附锚点）

**【实证】** 修复前 `kdo/commands/graph.py:333-342` `_collect_all_wiki_pages` 硬编码 9 子目录白名单（concepts/frameworks/tools/cases/systems/entities/decisions/projects/queries）——`30_wiki/dark-knowledges`（332 张）与 `30_wiki/dk`（57 张）均不在名单。非 glob 漏、非过滤误伤：**新目录上线后从未回填构建白名单**（新域 9 步清单管 index 注册，没覆盖 graph 构建白名单这个暗点）。锚点：KDO 仓 commit `78e6551` diff（白名单→动态扫描）。

## 执行报告

**交付物**：`Knowledge Delivery OS 0.0.1/kdo/commands/graph.py` 动态扫描修复（KDO 仓 commit 78e6551）+ `90_control/scripts/graph-index-coverage-probe.py` 防复发探针 + `kdo-tools/run-kdo-health.cmd` 挂载 + `Knowledge Delivery OS 0.0.1/tests/test_graph.py` 3 例 + `.kdo/graph_index` 全量重建（2941 页）+ 佐证包 `logs/dk-graph-coverage-evidence-20260907.log`

**完成内容**：dk 族 332+57 张全入 graph 索引；根因=构建白名单漏目录（【实证】锚点见上）；白名单改全子目录动态扫描（治根因：任何新目录免改码即检索）；覆盖率探针上线并接入每日 02:07 健康节拍（kdo-health-daily）

**验证**：①path_map dark-knowledges **332/332**【实证】（graph_state.json 2928 条总映射）②kdo query 抽 6 张 dk 标题实测：**5/6 进 top10、6/6 进 top30**（第 6 张仅排序靠后非未入索引，limit 30 实测命中）【实证】③探针实跑：dk 族 gap=0，同时捕获库内 13 张历史标题撞车卡（见边界）④回归 **633 passed 1 skipped**（与 #669 基线一致）+ 新增 3 例 passed【实证】

**边界**：探针暴露 **13 张历史标题撞车卡**【实证】（path_map 按 title 键、后者覆盖前者；实证例：`dk/dk-research-triangulation-stop-rule.md` 与 `skills/skill-research-triangulation-stop-rule.md` 同 title）——撞名卡实体在图里存在（检索可用），丢的只是溯源映射；改名属内容侧变更，黄药师不改内容。撞车未清前探针每日报 13 张缺口（有意保留的压力信号，非误报）。另：dk 排序分值普遍低（0.02-0.03）是哈希向量+RRF 的全库现象，非 dk 专属，不在本单范围

**需要谁动作**：欧阳锋终审本单；王语嫣为「13 张标题撞车卡改名」立项（清单：`python 90_control/scripts/graph-index-coverage-probe.py` 输出 title-collision victims 节）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 5 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
