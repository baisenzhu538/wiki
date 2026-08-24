---
id: diag_20260824_wangyuyan-zijing-product-level-prep-report
title: KDO 产物级 DAG 落地准备报告（#497 调研产出——供产品化排任务直接使用）
type: diagnosis/preparation
author: 王语嫣
created_at: '2026-08-24'
status: draft
audience: 老朱（产品化拍板）
related:
  - diag_20260823_zijing-ag-dag-upgrade-9layer-landing
  - diag_20260823_zijing-ag-architecture-deep-dive
  - diag_20260823_zijing-ag-product-outline-study
  - F-049（停车场：5 吸收点产品化挂起，本报告为其产物级部分的准备）
---

# KDO 产物级 DAG 落地准备报告（#497）

> 老朱 08-24 指令：「做一项调研，借鉴紫鲸产物级的内容，先做准备工作」。本报告=准备产物：紫鲸产物级机制提炼 → KDO 现状对账（实测）→ 落地准备清单（可直接拆任务）。产品化仍等老朱想清楚后从停车场 F-049 排。

## 一、紫鲸产物级机制（3 份调研提炼）

| 机制 | 紫鲸做法 | KDO 借鉴价值 |
|:--|:--|:--|
| 产物形态 | 8 业务角色产出=结构化对象（画像/诊断/调研/能力 4 类关键产出），非对话文本 | 关键产出落结构化模板，下游可机读 |
| result_id | 产物带 result_id，跨 session 稳定（服务端存） | KDO 需自定持久化位置（落 vault frontmatter，不引独立 DB——9 层方案 L8 边界 2） |
| 产物复用 | 同一 script 喂 3 个内容形态；下游 agent 取上游 result_id 消费 | 跨任务产物复用（同一批卡→多文章/多课程） |
| 编排门禁 | 13 工具=8 业务角色+3 内容形态+2 编排门禁 | MANIFEST 门禁链（F-049 改进 5，仅对外正式交付物） |
| 单元模型 | 产物级 DAG（result_id 邻接表）无任务状态机 | KDO 已有任务状态机——互补叠加，不是替换（9 层 L1） |

## 二、KDO 现状对账（2026-08-24 实测）

| 对账点 | KDO 现状 | 差距 |
|:--|:--|:--|
| 任务依赖 | frontmatter `depends_on` 已落地（F-047/#472：task_20260823_huangyaoshi-role-routes.md 等已在用） | 任务级依赖有了，**产物级复用无显式机制**（同批卡→多文章缺 result_id 链） |
| 产物类型 | 卡类型轴已成熟（concept/framework/case/tool/dk/agent-spec/article/diagnosis/review/delivery） | output_kind 可直接复用此轴，**不新增维度**（9 层 L9 第二步） |
| 交付物模板 | `40_outputs/capabilities/templates` + skills 各 templates（#307 6 模板机制，业务 agent 交付物模板） | 模板机制在，缺 result_id 字段接入 |
| 索引基建 | `.kdo/search_index.json`（4111 文档/54 万 token 全文索引）+ state.sqlite + doc_mtimes/doc_lengths | **确证两个障碍（2026-08-24 探针实测）**：①frontmatter 自定义字段（result_id 等）不入索引——索引器只提取 title/aliases/tags/discoverable_by 四字段，正文从 frontmatter 后开始；②**下划线被分词拆分**（`card_20260824_x`→card/20260824/x 多 token），连字符保留完整（aliases 实证）。⇒ 按完整 result_id 精确查询**不可行**，需索引器补字段提取（9 层 F4：确证需改造，非待验证） |
| 流转协议 | queue_transition 状态机 + Manual edits forbidden | result_id 字段需脚本化流转（不手改）——queue_transition/parse_queue 兼容改造（9 层 L3/L6） |
| 冻结纪律 | #449 §6.1/§6.2 + L10 机械化（#502 立项中） | 产物文件=已落盘即冻结——result_id 落盘后不可改，与冻结兼容 |
| 跨任务复用先例 | 半肥猫 #465(A 档卡)→#466(B 档手册)→#467(C 档案例) 同素材链 | **天然试点场景**（9 层 L9 第四步试点 2） |

## 三、落地准备清单（产品化时直接拆任务）

### 契约层（王语嫣起草→老朱拍板）
1. `result_id` 命名：`<output_kind>-<YYYYMMDD>-<short>`（如 `card-20260824-zijing-prep`）——**用连字符不用下划线**（2026-08-24 探针实测：下划线被分词拆分，连字符保留完整；修正 9 层方案 L9 原建议的 `card_20260823_xxx` 下划线命名）
2. `output_kind` 取值：复用现有卡类型轴（10 类），不新增
3. `upstream_result_ids`：frontmatter 列表字段，软依赖可选（不强制 downstream 邻接表，避 F6）

### 基建层（黄药师，复用 #453/#479 模式，排队不抢线）
4. queue_transition/parse_queue 兼容三字段（yaml.safe_load，禁正则 E017）
5. lint 扩展：result_id 命名校验（连字符格式）+ output_kind 合法集校验
6. **索引器补 result_id 字段提取**（最大风险 F4，**必做非待验证**——2026-08-24 探针确证：frontmatter 自定义字段不入索引 + 下划线拆分）：`search_index.py` `_index_doc` 加 result_id 加权入索引（仿 aliases 路径）+ 单测 + 全量回归（4111 文档 doc_count 不变）

### 试点层（2 单狗粮）
7. 试点 1：落地单自举（该单自己带 result_id + output_kind=diagnosis）
8. 试点 2：半肥猫 #465→#466→#467 链——#466/#467 的 upstream_result_ids 取 #465 卡 result_id

### 观察层（2 周 L3）
9. 观察点：result_id 消费次数（无人消费=H1 证伪）/ upstream 写错率 / 与 wikilink 重复度
10. 重评触发信号（9 层 L9 已列 5 条，任一触发回 L2 重审）

### 边界（不做清单，9 层 L9 已定）
- 不引独立 result_id DB / 不照搬紫鲸远程 MCP / 不做 pack_only 双形态 / 不做 gateway 自动路由 / 不强制造 downstream

## 四、准备期探针——已完成（2026-08-24）

**探针实测**（2 张对照测试卡：正常/损坏 frontmatter，各带 result_id marker + 唯一正文词 → 全量索引 4113 → 查 4 类 marker → 清理恢复 4111）：

| 查询词 | 结果 | 原因 |
|:--|:--|:--|
| frontmatter result_id（正常卡） | ❌ MISS | frontmatter 非提取字段不入索引 |
| frontmatter result_id（损坏卡） | ❌ MISS | 同上 + 下划线拆分 |
| aliases marker | ✅ HIT | aliases 3x 加权入索引，连字符保留 |
| 正文下划线 marker | ❌ 完整词 MISS | 下划线被分词拆成多 token |

**探针结论**：①frontmatter 自定义字段（result_id）不入索引——索引器必须补字段提取（黄药师小单，必做）；②result_id 命名规范用连字符（下划线搜不到完整串）；③现有 `kdo query` 语义检索不受影响（只影响"按 result_id 精确取物"新机制）。

## 五、待老朱拍板（产品化时）

1. result_id 持久化：落 vault frontmatter（推荐，T2 轻量）vs 独立 DB（T3，否决——真相源冲突）
2. output_kind 复用现有类型轴（推荐）vs 新增维度
3. 试点场景确认（半肥猫链）
4. 索引命中率探针是否提前做（建议：是）

---

*王语嫣 · 2026-08-24 · #497 调研产出 · 基于紫鲸 3 份调研 + 9 层方案 L8/L9 + KDO 现状实测 · F-049 产品化准备件*
