---
id: task_20260907_huangyaoshi-pathmap-key-hardening
title: "graph_state path_map 改 path/id 键根除同标题撞车（13 张溯源丢失实证——KDO 仓 graph.py:424）"
seq: 674
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 欧阳锋建议书 diag_20260907_ouyangfeng-title-collision-pathmap-hardening（#671 探针首报警的根因定位）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T20:57:10.269050+00:00'
evidence: logs/pathmap-hardening-674-20260907.log
reviewed_by: 欧阳锋
review_date: '2026-09-06'
grade: A-
---

# #674 path_map 键硬化（黄药师，KDO 仓）

## 实证
graph_state.json path_map 以 title 为键（graph.py:424）→ 同标题卡后者覆盖前者，13 张溯源映射丢失（concepts 1/dk 1/frameworks 1/tools 10）。#671 探针报警的 concepts 524/525 缺口即撞车卡。
【实证】修复前基线复测：dup_titles=13 / dup_cards=26，探针 path_map=2928 vs pages=2941，gap=13 且分布与上述完全一致（logs/pathmap-hardening-674-20260907.log）。

## 修法（根因硬化，优于逐张改名）
path_map 改按 path（或 id）键；title 保留为展示属性。KDO 仓改动（Knowledge Delivery OS 0.0.1/kdo/）。

## 验收
重建后 path_map 无 title 撞车（13 张全部可溯源）；#671 探针 concepts 缺口清零；回归不红。

## 执行报告（huangyaoshi 2026-09-07 04:45）

**交付物**：KDO 仓 commit `6fb4a42`（kdo/commands/graph.py 写侧键硬化 + 读侧 legacy 升级 + 删除传播适配；tests/test_graph.py +3 例）；vault 侧 `90_control/scripts/graph-index-coverage-probe.py` 适配新 schema（#671 探针，本人在册工具）+ 验收日志 `logs/pathmap-hardening-674-20260907.log`。

**完成内容**：①写侧 `path_map` 键 title→page_path（文件系统唯一），值改 `{title, id}`，title 降为展示属性【实证】graph.py:424→432-441；②读侧 legacy 检测：str 值=pre-#674 state 自动强制 full rebuild，防旧 state 撞喂增量 diff【实证】重建实弹触发一次升级打印；③增量删除传播改按键差集，LightRAG doc_id 仍从 entry.title 取回（KG 实体层键未动，不越范围）；④探针适配：缺口判定改按键、同 title 降为非阻塞观察项（13 组计数进 --json 的 dup_titles 字段，不再永久红灯）；⑤TDD：先红后绿（红：`1 != 2 : ['dup-card']` 撞车复现）。

**验证**：TDD 3 新例（撞车根除/删除传播/legacy 升级）+ 全量回归 `639 passed 1 skipped`（基线 636+3，无红）【实证】pytest 输出；vault 实地 `kdo graph rebuild --full` 2941 页，重建后 path_map=2941=page_count、legacy 值 0、26 张撞名卡 missing=0（13 组全部可溯源）【实证】验收脚本输出；探针 `coverage OK pages=2941 path_map=2941 exit 0`，concepts 525/525（#671 报警缺口清零）、dark-knowledges 332/332【实证】探针输出；检索冒烟 `kdo query "多源交叉验证的停止规则"` 曾被顶掉的 dk 卡正常召回【实证】。

**边界**：①LightRAG 实体层 entity_name 仍=title，13 组撞名卡在图内仍合流（检索已可溯源但图实体未分身）——根治需 KG 层同步硬化或内容侧改名（撞名卡改名是内容侧流程，归王语嫣），建议另立新单；②既有边界缺陷（测试踩到，未动）：30_wiki 页全删空时 cmd_graph_ingest 于 graph.py:358 提前 return，删除传播不触发——pre-existing；③10 张卡无 frontmatter id，entry 缺 id 键属正常缺省（id 可空、path 必唯一）。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉——13 组同 title 卡改名（内容侧）仍是残余风险的根治路径，探针现为非阻塞观察项（dup_titles=13 持续可见，不改名不拦门禁）。

## kdo query 检索记录（宪法第六条）

| 检索词 | 命中 | 日期 |
|---|---|---|
| `kdo query "多源交叉验证的停止规则"` | 有（曾被顶掉的 dk 卡正常召回，验证溯源恢复） | 2026-09-07 |
| `kdo query "path_map 键设计 唯一键 撞车"` | 5（无同型既有方案卡，确认需代码侧硬化） | 2026-09-07 |
| `kdo query "graph index 覆盖率 检索失明"` | 4（含 `30_wiki/systems/graph-rag-retrieval-layer.md`，确认架构归属） | 2026-09-07 |

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录

methodology_version: v2.3
verdict: PASS
grade: A-
blocking: 无
reviewed_by: 欧阳锋
review_date: 2026-09-07

**审查结论**：三项重点核全过，准予通过。①13 张撞车卡溯源全部恢复——本端独立跑收集脚本，13 组同 title 共 26 张卡（concepts 1/dk 1/frameworks 1/tools 10），26/26 全在 path_map（missing=0），键已为 path、值含 title+id，同标题不再互相覆盖【实证】。②探针 concepts 缺口清零——本端独立实跑 `graph-index-coverage-probe.py --json`：ok=true / pages=2941 / path_map=2941 / gap_by_dir 全 0（concepts 0、dark-knowledges 0）/ anomalies=[]；graph_state.json 本端读：str_vals=0、dict_vals=2941、entries_without_title=0【实证】。③回归不红——KDO 仓 `pytest tests/` 独立实跑 639 passed 1 skipped（与执行报告一致），`tests/test_graph.py` 27 passed（+3 新例全绿）【实证】。

**五维评分**：溯源完整 25/25、逻辑骨架 24/25、暗知识密度 18/20、可操作性 15/15、表达质量 13/15（总分 95）。

**关键实现核查（KDO 仓 6fb4a42）**：写侧 graph.py:424 原 title 键→现 page_path 键、值 {title,id}，键按构造唯一根除覆盖【实证】；legacy 检测 `any(isinstance(v,str) for v in prev_path_map.values())`→强制 full rebuild，当前 state str_vals=0 印证升级路径已闭环【实证】；删除传播 `set(prev_path_map.values())`→`set(prev_path_map)` 按键差集，entry.title 回取 LightRAG 实体名，语义正确【实证】。探针适配（vault 侧）按键判定缺口+同 title 降为非阻塞观察项，本端 --json 已见 dup_titles=13 不进 anomalies【实证】。

**缺口清单（非阻断）**：
1. 探针适配的 vault 侧改动经自动备份 commit `22081f4da` 落仓（graph-index-coverage-probe.py 36 行 diff），而非 #674 专属 commit `f8cd50040`（后者仅含任务单+验收日志）——改动已提交、无脏改动，纯提交路由记录级提示，无需回退本单【实证，本端 git log -S dup_titles 定位】。
2. KG 实体层 entity_name 仍=title：13 组撞名卡在 path_map 已可溯源，但 LightRAG 图内仍合流（黄药师边界① 已声明）——根治需 KG 层同步硬化或内容侧改名，归新单，不属本单验收范围【实证，执行报告自声明+代码 entity_name 键未动】。
3. pre-existing 边界缺陷：30_wiki 页全删空时 cmd_graph_ingest 于 graph.py:358 提前 return、删除传播不触发（黄药师边界② 已声明，测试踩到未动）——记录级，不阻断【实证，测试用例注释声明】。

**存在性核查**（#433，本端逐条）：「26 张全部可溯源」→ 本端脚本 13 组 2/2、missing=0（2026-09-07）；「探针缺口清零」→ 本端 --json gap_by_dir 全 0（2026-09-07）；「回归 639/1」→ 本端 pytest tests/ 639 passed 1 skipped（2026-09-07）；「探针改动落备份 commit」→ 本端 git log -S 'dup_titles' 仅命中 22081f4da（2026-09-07）。

**kdo query 检索记录**（宪法第六条 #669，本端终审侧）：查询词 `kdo query "path_map 键设计 唯一键 撞车"` / `kdo query "graph index 覆盖率 检索失明"` / `kdo query "多源交叉验证的停止规则"`，命中见执行报告同口径、结论一致（确认无同型既有方案卡，属代码侧硬化，2026-09-07）。

**需要谁动作**：无回退项。王语嫣知悉——#675（bundle bat 双问题）已立项 queued、排 #674 后接续；13 组同 title 卡改名（内容侧）+ KG 实体层分身仍是残余风险根治路径，探针现为非阻塞观察项（dup_titles=13 持续可见）。
