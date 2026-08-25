---
id: 524
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T06:16:33.057325+00:00'
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

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：kdo_search 消费端契约四件套（`kdo-tools/mcp/tools.py` 渲染/排序层）：①**status/confidence 外露+⚠️ 前缀**：结果新增 `confidence` 字段（frontmatter 直读）；`_display_title`——draft/pending_review 标题加 `⚠️ ` 前缀（#380【未审】符号升级为 ⚠️ 且覆盖 pending_review，status 字段原样保留可机读）；②**来源层标注**：`_source_layer_label`——无 status 且非 30_wiki 的命中标注 `[skills]`（路径含 skills 段）/`[raw]`（10_raw）/`[outputs]`（40_outputs）等顶层目录别名；③**排序加权**：`_apply_status_weights` 在 `_filter_by_trust` 后、`_sort_by_layer` 前对 score 加权（reviewed×1.25/draft×0.7/pending_review×0.8/其他×1.0）——层优先级不动（框架层仍在前），层内按加权分重排，**降权不剔除**（红线 4）；加权轻读 frontmatter 前 4KB（`_quick_status`，文件不可读 fail-open 权重 1.0）；④回归 10 例。预声明 code_files 中 server.py 实际零改动（工具层全在 tools.py，server 仅转发）——差 1 件记录在案。

**交付物**：
- `kdo-tools/mcp/tools.py`（三 helper + search() 接线 + confidence/source_layer 字段）
- `kdo-tools/tests/test_mcp_server.py`（新：10 例回归）

**验证**：
- L1 单测 10 例全过：⚠️ 前缀三分支（draft/pending_review/reviewed）、来源层四分支（[raw]/[skills]/30_wiki 无标/有 status 无标）、加权混合语料（等分 reviewed>无 status>draft，全部保留不剔除）、pending_review 权重介于 draft 与净卡之间、文件不可读 fail-open；全量基线 **120 passed**（110+10，零退步）
- L2 狗粮（验收演示 query「OpenClaw 和 Hermes 区别」前后对照，HEAD 版=before）：before——pending_review 卡（Agent 白皮书五要素）**零标记**且与 draft 并列 0.148 排第 5-6、darwin-skill 命中标题泄漏 frontmatter 无标注、无 confidence；after——⚠️ 覆盖 draft+pending_review、confidence 全外露、[skills] 标注生效、pending_review 0.148→0.118 与 draft 0.148→0.104 双双降权后移、4 张 reviewed 稳占头部 ✅
- L3 待活体：小昭下轮消费端会话不再把 draft 当答案吃（⚠️ 可见）

**边界**：索引/召回算法（RRF/GraphRAG/BM25/MOC）零改动 ✅；kdo_read 未动 ✅；层优先级语义未动（加权只在层内）✅；【未审】→⚠️ 是显示符号升级（status 字段不变，机读兼容）。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉——消费端契约已上线（⚠️=未终审，[raw]/[skills]=非卡来源层）；小昭侧下次消费可见新标注。
