---
id: 524
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-25T06:08:12.753344+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/mcp/server.py
- kdo-tools/tests/test_mcp_server.py
---

# #524 kdo_search 消费端契约：结果标注 status + draft 警示 + 非卡来源层标注 + reviewed 排序加权

- **任务号**：#524
- **状态**：queued
- **assignee**：huangyaoshi（kdo MCP server 检索结果渲染/排序层；欧阳锋终审）
- **优先级**：P1（消费端正在把 draft 当答案吃——全库 draft 1110+ 张，检索层零标注=唯一可立刻压风险的杠杆）
- **立项**：2026-08-25 王语嫣（老朱授权「根据洞察自行编排入列」；依据=`60_feedback/analysis/2026-08-25-xiaozhao-consumer-side-kb-usage.md` 证据 1/2/3/11——小昭消费端实况）

## 背景

消费端实况（小昭 08-24 会话）：kdo_search 语义层有效（捞出 Grep 漏掉的关键卡），但结果①不标 status——捞到的核心卡是 draft/待审，消费端自警「不看 status 容易把草稿当定论」；②混入非卡片（SKILL.md/README 无 status、10_raw 原始素材 type=unknown）；③头部结果 score 并列仅沾边，最相关卡被略过。draft 存量短期消化不完，检索层标注是止血杠杆。

## 任务

1. **status 标注**：kdo_search 每条结果显式输出 `status`/`confidence` 字段；`status: draft` 或 `pending_review` 的卡片标题前加 ⚠️ 前缀（消费端一眼可辨）
2. **来源层标注**：无 status 字段的命中（40_outputs skills、10_raw 素材等）标注来源层（如 `[skills]`/`[raw]`），不与 30_wiki 卡片混淆
3. **排序加权**：reviewed 卡排序权重上调，draft/pending_review 降权（不剔除——有些 query 只有 draft 命中，剔除=召回损失；降权+标注即可）
4. **回归测试**：构造混合语料（reviewed/draft/无 status 三类）验证标注与排序；既有测试全绿

## 边界

- 不动索引/召回算法本身（RRF/GraphRAG/BM25/MOC 不动），只动结果渲染与排序权重——红线 4：误拦优先不误伤，降权不剔除
- 不改 kdo_read（读卡层行为不变）
- 施工前读最新 HEAD（charter §3.16）；与 #519-#523 无文件区冲突（探针/l1_capture 不相交）

## 验收

- 同一 query（建议复用「OpenClaw 和 Hermes 区别」）演示：draft 卡带 ⚠️、skills/raw 命中带来源层标注、reviewed 卡排序前移（附前后对照输出）
- 混合语料回归测试通过，既有测试全绿
- 欧阳锋终审
