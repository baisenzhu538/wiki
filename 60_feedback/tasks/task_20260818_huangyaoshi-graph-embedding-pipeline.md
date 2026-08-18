---
id: 358
assignee: huangyaoshi
status: queued
updated_at: '2026-08-18T15:30:00+00:00'
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
