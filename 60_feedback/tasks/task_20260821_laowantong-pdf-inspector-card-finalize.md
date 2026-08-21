---
id: 407
assignee: hermes
status: reviewed
updated_at: '2026-08-21T20:15:22.560430+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-21'
grade: A-
---
# #407 PDF-Inspector 外部建议稿核验入库（tool 卡精做）

- **任务号**：#407
- **状态**：queued
- **assignee**：laowantong
- **优先级**：P2
- **立项**：2026-08-21 王语嫣（门禁判定：`60_feedback/diagnosis/diag_20260821_wangyuyan-pdf-inspector-gate.md`）
- **来源**：`00_inbox/pending-cards/tool-pdf-inspector.md`（**小昭外部 agent 建议稿**，08-21 22:51 写入，author 虚标"老顽童"——E018 变体；老朱亲自规范小昭，本单只处理卡片入库链）+ 源素材 `00_inbox/wechat-collect/src_wechat_fe60439837f4c93e.md`（40s 短视频逐字稿）

## 背景

Firecrawl PDF-Inspector（纯 Rust、MIT）：先分类（10–50ms 判断 text_based/scanned/image_based/mixed）再路由，原生文本 PDF 本地直提不走 OCR。与库内 `mineru-pdf-parsing-setup` 互补（MinerU 管扫描件/复杂版面）。黄药师 08-21 已狗粮实测：5 份 KDO 真实 PDF 5/5 通过（conf 0.875–1.0，0.2–0.42s/份，中文无乱码，混合页正确标出 pages_needing_ocr）。

小昭产物按"外部建议稿"对待：内容可采，但**必须 KDO 生产链核验 + 欧阳锋真实终审**后才算入库（08-19 铁律）。

## 动作清单

1. **官方源核验（三方法轻量版）**：逐一核验卡内超源数字，全部来自官方源（GitHub firecrawl/pdf-inspector、PyPI、Firecrawl blog）才算过：
   - 200 PDF 0.47s（opendataloader-bench 语料）
   - 54% PDF 自带文本层统计
   - 文本直提 ~150ms / 分类 10–50ms
   - heading 识别 0.788 vs liteparse 0.811
   - 核验结果回填卡片（标 verified 或修正数字）；核不到的删除或标注存疑
2. **author 字段修正**：`author: 老顽童` → 如实标注（建议 `author: 小昭（外部建议稿），老顽童核验入库`；最终口径以老朱对小昭的规范为准，终审时欧阳锋裁定）
3. **定位声明**：正文开头补定位句——本卡是 KDO PDF 进料 classify-then-route 路由的"快速通道"工具卡，与 `mineru-pdf-parsing-setup` 互补（#199 门禁规则）
4. **双向回链**：`30_wiki/tools/mineru-pdf-parsing-setup.md` related 加反向链 `[[tool-pdf-inspector]]`（只增不改，#384/E017 模式）；`tool-agent-crawl4ai` 如相关同加
5. **入正式层**：卡片从 `00_inbox/pending-cards/` 移入 `30_wiki/tools/tool-pdf-inspector.md`（git mv，E037 固化）
6. **pre-submit + commit 入档**：`kdo pre-submit` 目标卡 0 ERROR，附输出；完成后走 queue_transition 提审

## 验收标准

- 官方源核验逐项有结论（verified / 修正 / 存疑删除），卡面不留未核数字
- author 如实、status 流转走脚本、pre-submit 附输出
- 双向回链完成且 0 死链
- 欧阳锋终审：重点抽"核验真实性"（官方源是否真含这些数字）+ "author 口径"

## 内容价值判断（#375 处置类门禁补充）

- **本任务素材**：`00_inbox/pending-cards/tool-pdf-inspector.md`（小昭外部建议稿，7.7KB）——已通读全文（先读完整内容再下结论，B5 牌）：结构完整、含黄药师一手狗粮实测、source_refs 三官方源，**判定为有价值素材，去向=核验后入正式层**（git mv 至 `30_wiki/tools/`，非删除）
- **源素材**：`00_inbox/wechat-collect/src_wechat_fe60439837f4c93e.md`（40s 视频逐字稿）——原位保留不动
- **case 卡**：`00_inbox/pending-cards/case-wechat-fe60439837f4c93e.md`——王语嫣门禁已判 superseded（并入 tool 卡），本任务不处理，只读确认
- **处置原则**：本任务**无任何删除动作**；卡内数字核验不通过的条目按「标注存疑/修正」处理，不删卡。素材默认消化/归档原位保留，**删除须逐件老朱亲批**（PROTOCOL §7）

## 边界

- 不动 case 卡（已由王语嫣门禁判定合并 superseded，诊断见上）
- 不动 MinerU 卡正文内容，只加 related
- 不替小昭定性、不改小昭侧任何东西（老朱规范）
- 卡内黄药师实测段落保留原样（那是本厂一手实测）

## 终审记录（2026-08-22 欧阳锋 · PASS A-）

**O0 溯源核验**（source_refs 官方源逐一打开）：
- PyPI 官方 description（GitHub README 镜像）：0.470s ✅ / 54% ✅ / ~10–50ms ✅ / 0.788vs0.811 ✅ / under 200ms ✅ / Rust ✅ —— 卡面数字核验标注真实
- "200 个 PDF" ✅ 官方 benchmark 原文 "corpus (200 PDFs)"（opendataloader-bench）；视频逐字稿"2.8 秒"与官方 0.470s 不一致，核验以官方源为准修正——**核验真实性正证据**
- "单依赖 lopdf" 🟡 部分准确：Cargo.toml 确认 lopdf 存在（native 构建），但实际依赖 ~10 个 crate，且 WASM 版无 lopdf（用 ttf-parser）——表述过强，TODO 小修

**其他检查**：author 如实标注小昭（外部建议稿）✅ / 定位声明 ✅ / 双向回链 mineru+crawl4ai 0 死链 ✅ / pre-submit 0 issues ✅ / reviewed_by: pending 占位合规（E018）✅

**遗留 TODO**：
1. 对比表"依赖 | 纯 Rust，单依赖 lopdf"表述修正为"核心解析依赖 lopdf（native），依赖轻量"——并入下批小修（非阻断）
2. 观察：任务单 review_date 08-21（queue_transition UTC 口径）vs 卡片 08-22（review_mark 本地口径）差一天——known 时区口径，统一留待脚本层修（记 #357 家族）
