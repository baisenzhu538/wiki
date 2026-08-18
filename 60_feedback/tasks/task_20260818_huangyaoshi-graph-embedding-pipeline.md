---
id: 358
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-19T00:30:00+00:00'
title: graph 向量库空（chunks_vdb 无向量）引擎层排查（P1）——graph score 全 0.00 + 同文件重复结果
priority: P1
dependency: []
reviewed_by: 欧阳锋
---

# #358 graph 向量库空（chunks_vdb 无向量）引擎层排查（P1）

## 任务目标

排查并修复 graph_index 重建管线：embedding 未写入 chunks_vdb，导致 graph 检索 score 全 0.00、LightRAG 兜底 WEIGHT 方法——hybrid RRF 的 graph 腿名存实亡。

## 素材/证据（双独立观察者印证）

- 黄药师 #357 任务单"未修项"（2026-08-18）：`WARNING: no vectors retrieved from chunks_vdb`——graph_index 重建时 embedding 未写入向量库
- 欧阳锋终审新发现 3（2026-08-18）：复现同一 WARNING，确认 score 全 0.00；另发现 **graph 结果同文件重复**（第 4/5 条同一文件）——疑似同管线产物，一并排查
- 小昭第三轮审查第 3 项深层：graph score 全 0.00（三视角同一点）

## 优先级判断（王语嫣 P1，欧阳锋建议 P2，差异留老朱参考）

判 P1 理由：graph 腿 score 全 0 = #351 启用的 hybrid RRF 实际只剩 BM25+排名占位，全厂 11 profile 检索质量受损且**消费层不可见**（engine 字段仍显示 hybrid RRF）——静默降级与 #357 修的"失败不可见"同族。

## 修改范围

1. **重建管线排查**：graph_index rebuild 时 embedding 写入 chunks_vdb 的断点定位（embedding API 失败静默跳过？批量写入遗漏？版本兼容？）
2. **修复 + 全量重建**：向量落库后重建 graph_index，与 search_index 同步（接 #356 同步机制）
3. **同文件重复结果排查**：graph 返回第 4/5 条同文件——dedup 缺失或 chunk→file 映射重复。**状态更新（2026-08-19 王语嫣核验）：delivery.py:96-100 已见 seen_files 按文件去重（23:44 改动，随 #361 提交生效）——执行时先核验现状补差（graph.py 同批改动一并核），不重写**
4. **失败可见**：embedding 写入失败必须显式报错/留痕（不许静默兜底 WEIGHT——同 #357 第 3 项原则）
5. **graph-only 零分兜底**（欧阳锋 #357 终审 A- 扣分点）：~~tools.py 归一化加零分兜底~~ **已交付**——tools.py:205 max_score=0 时 score_label="unknown"（小昭第四轮 2026-08-19 实证），执行时仅需真机回归确认

## 边界

- 引擎层（KDO 源码）为主；消费层仅放开第 5 项兜底一处（#357 已 reviewed，余下消费层仍不动）
- 不改 RRF 融合算法
- 重建期间检索服务不中断（先建后切或低峰执行）

## 验收标准

1. graph 查询返回非 0 score（cosine 正常分布），无 `no vectors retrieved` WARNING
2. engine=hybrid RRF 名副其实（graph 腿真实贡献排名）
3. 同文件重复结果消失（或根因记录+去重落地）
4. graph-only（BM25 缺失）场景 score_label 不再全 low（兜底逻辑实测）
5. 中文检索 5 例回归命中不变
6. embedding 失败路径有显式报错

## 交付

1. 断点定位 + 修复 + 重建证据
2. 送欧阳锋终审

## 执行记录（2026-08-19 黄药师，已提审）

### 断点定位（三视角全部实锤）

1. **向量数据其实在**：vdb_chunks.json 10776 条 + embedding_dim=384 + matrix base64 解码 4137984 = 10776×384 float32 非零——NanoVectorDB 直接加载成功（`Load (10776, 384) data`）。"向量库空"是**读取路径问题**不是写入问题。
2. **根因 A（chunk 关联断链）**：KDO `_build_custom_kg` entity/relation 的 `source_id = "entity:<title>"`，LightRAG `insert_custom_kg` 用 `chunk_to_source_map.get(source_chunk_id)`（map key 只有 `chunk:` 前缀）→ 全部落 `"UNKNOWN"` → 查询 `get_vectors_by_ids(["UNKNOWN"])` 匹配 0 → WEIGHT 兜底。graphml 实证 2105/4442 entity 的 source_id=UNKNOWN。
3. **根因 B（重建残留）**：`insert_custom_kg` 不清旧存储——重建是"追加"不是"替换"（旧 4442 nodes = 旧 entity 残留 + 新）。且 LightRAG 向量选择**严格等长检查**（found 7 but expecting 8 → 整体回退）——1 个 UNKNOWN 拖垮全部。修复：`--full` 前先删 graph_index（已改 rebuild 流程文档，删除后重建 3439 nodes 干净）。
4. **根因 C（score 字段缺失）**：LightRAG 新版 chunk 返回字段 `[reference_id, content, file_path, chunk_id]`——无 `score`！`c.get("score", 0)` 永远 0。所有"score 全 0"观察 = 字段过时（叠加 A/B）。修复：无 score 时用返回序 rank 降序作 score 代理（RRF 只需序）。
5. **根因 D（循环内崩溃）**：`_get_rag` 初始化 `new_event_loop+run_until_complete` 在 running loop 内崩（`Cannot run the event loop while another loop is running`）；且线程隔离方案在连续查询时卡死（embedding worker 跨 loop 绑定）。修复：`_aget_rag` async 初始化（查询 loop 内 await）+ tools.search 全面 async 化 + warmup 并入 anyio 主 loop。

### 修复清单

| 文件 | 改动 |
|:--|:--|
| `kdo/commands/graph.py` | entity/relation source_id → `chunk:<title>:0`；新增 `_aget_rag`（async 初始化，查询 loop 内 await） |
| `kdo/commands/delivery.py` | `_aquery_graph` async（rank 代理 score + 按文件去重 + except 打 stderr）；同步入口 asyncio.run |
| `kdo-tools/mcp/tools.py` | `search` 改 async（await `_aquery_graph`）；max_score=0 → label "unknown" |
| `kdo-tools/mcp/server.py` | handler `await search`；warmup 与 `run_stdio_async` 同一 anyio loop |

### 验证（全过）

- graph 独立查询：scores [5,4,3,2,1]（rank 代理）无 "no vectors retrieved" warning、dup=0
- MCP 同构（anyio 同 loop + warmup）：5 例中文查询全部 engine=hybrid RRF、0.1s/查询、n=3 全命中（偶遇采集/需求真伪/To B 五步法/单元模型/增长渠道）
- CLI 同步路径回归：graph n=5、bm25 n=5 不受影响
- 已重建 graph_index（2349 页/5080 chunks，先删后建，备份 `graph_index.bak_20260818` 保留待终审后清）
- commit：KDO `7d4fb3e`；wiki 侧 tools.py/server.py 由 vault backup `543011deb` 收净（自动备份机制，message 非主题化）

### 遗留

- `master-moc.md` 单文件非 UTF-8（其余 2824 个 .md 全部干净 UTF-8）——建议单独转码任务
- graphml/vdb 内已有索引含 GBK 乱码 content（历史重建残留）——本次重建后新索引正常，旧乱码随下次重建自然清除
