# KDO 卡片质量门禁报告

**扫描时间**：2026-06-21  
**扫描范围**：30_wiki 全库 1971 张卡片  
**锚定评分**：2/5 — 草稿
**P0 阻塞问题卡片**：204 张  
**P1 修复问题卡片**：415 张  
**完全干净卡片**：1370 张  
**YAML 解析错误**：96 张  

---

## 锚定评分标准（Harness 1-5 + 取较低值）

| 分 | 标签 | 标准 |
|---|---|---|
| 5 | 可发布 | P0=0, P1<2%, 零CRITICAL |
| 4 | 可靠 | P0<1%, source_refs 真实 |
| 3 | 可用 | P0<5%, 骨架完整 |
| 2 | 草稿 | 需大量修复 |
| 1 | 不可用 | P0≥15% 或违反铁律 |

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `_dogfood_dk.md` | id (dogfood-dk-indent) 与文件名 (_dogfood_dk) 不一致; 缺少 title; author 为空; 缺少 confidence; 缺少 trust_level |
| `_dogfood_dk2.md` | id (dogfood-dk-missing) 与文件名 (_dogfood_dk2) 不一致; 缺少 title; author 为空; 缺少 confidence; 缺少 trust_level |
| `_test_pa.md` | YAML 解析错误: None |
| `cases\case-strategy-failure-04-appliance.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-failure-05-it.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-failure-06-phone-n.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-failure-07-phone-l.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-failure-08-video.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-failure-09-boeing.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-fangte-disney.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-lekai-film.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-li-ka-shing.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-longzhong-plan.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-m-brand-profit-model.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-practice-10-turnaround.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-practice-11-third-place.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-practice-12-zero-loss.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-practice-ranpeng-milk-powder.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-retailer-activity-scope.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-revival-13-bestore.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-shell-oil.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-snack-export-opportunity.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-walmart-vs-costco-pyramid.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-wuxi-suntech.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-strategy-xiaobear.md` | status=enriched 但 reviewed_by=pending |
| `concept-card-index-latest.md` | YAML 解析错误: None |
| `concepts\ai-native-im-multi-agent.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: ai-native-im-multi-agent
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 17, column 1:
    - src_20260614_c5115d2c-龙虾-AI原生I ... 
    ^ |
| `concepts\ai-native-五层进阶从答案到效率到作品到产品到系统.md` | source_refs 为空 |
| `concepts\ai-俱乐部人和-ai-协作-五层结构.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    title: "AI 俱乐部·人和 AI 协作 — 五层结构"
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 14, column 1:
    - src_20260609_8e64b361-ai-俱乐部人和 ... 
    ^ |
| `concepts\ai-俱乐部人和-ai-协作-参考案例对比一堂-vs-sql-helper.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    title: "AI 俱乐部·人和 AI 协作 — 参考案例对比 ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 14, column 1:
    - src_20260609_dade3353-ai-俱乐部人和 ... 
    ^ |
| `concepts\ai单元模型口述蒋老师.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\ai数据理解第一课.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\ai时代判断力口述-3.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\concept-smart-medicine-cabinet-consumer-acceptance.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    id: concept-smart-medicine-cabin ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 15, column 1:
    - src_20260613_b0cac5a3-corr_202 ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-digital-pharmacy-diagnosis.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    id: concept-smart-medicine-cabin ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 10, column 1:
    - src_20260613_98aa19d4-itingnao ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-giants-why-not-clinic-cabinet.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    id: concept-smart-medicine-cabin ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 14, column 1:
    - src_20260613_7cfd7b89-corr_202 ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-international-models.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    id: concept-smart-medicine-cabin ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 14, column 1:
    - src_20260613_f23b86fa-corr_202 ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-platform-cooperation-validation.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    id: concept-smart-medicine-cabin ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 13, column 1:
    - src_20260613_945a21d7-itingnao ... 
    ^ |
| `concepts\concept-smart-medicine-cabinet-supply-chain-validation.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\concept-strategy-evolution-cycle.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: concept-strategy-evolution-cycle
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 13, column 1:
    - src_unknown
    ^ |
| `concepts\concept-yitang-channel-lean-validation-bridge.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    id: concept-yitang-channel-lean- ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 19, column 1:
    - 00_inbox/一堂五步法之增长/truman-渠道探索方 ... 
    ^ |
| `concepts\concept-一堂-key-assumptions.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\concept-纪浩-ai-collaboration-five-layer.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    id: concept-纪浩-ai-collaboration- ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 13, column 1:
    - 10_raw/sources/src_20260619_e1 ... 
    ^ |
| `concepts\ec工业化规范手册-v2.8.0.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\fd-forward-deployment.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    id: fd-forward-deployment
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 15, column 1:
    - src_20260614_ab09af1c-多人-FD模式解析
    ^ |
| `concepts\graph-rag.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    id: graph-rag
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 1:
    - src_20260502_7d7c1b7c-kimi-深度调 ... 
    ^ |
| `concepts\smart-medicine-cabinet-distribution.md` | 缺少 confidence |
| `concepts\smart-medicine-cabinet-national-policy-redlines.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: smart-medicine-cabinet-natio ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 16, column 1:
    - src_20260613_26c69f98-corr_202 ... 
    ^ |
| `concepts\smart-medicine-cabinet-o2o-cost-structure.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: smart-medicine-cabinet-o2o-c ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 18, column 1:
    - src_20260613_26c69f98-corr_202 ... 
    ^ |
| `concepts\smart-medicine-cabinet-regional-policy-map.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: smart-medicine-cabinet-regio ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 16, column 1:
    - src_20260613_26c69f98-corr_202 ... 
    ^ |
| `concepts\truman-perspective-skill.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\web-scraping-三剑客-scrapling-crawl4ai-firecrawl.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    id: web-scraping-三剑客-scrapling-c ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 19, column 1:
    - src_20260502_7d7c1b7c-kimi-深度调 ... 
    ^ |
| `concepts\yitang-qualitative-to-quantitative.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    id: yitang-qualitative-to-quanti ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - src_20260614_606a631d-张磊-精益方法论培训
    ^ |
| `concepts\yt-ai-startup-20-risky-hypotheses.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 23, column 1:
    - src_20260614_086550ab-刘长胜@136- ... 
    ^ |
| `concepts\yt-ai-trend-12-signals.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 23, column 1:
    - src_20260614_82a4fdb9-凯文凯利-必然趋势分享
    ^ |
| `concepts\yt-barrier-analysis-cheat-sheet.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\yt-business-formula-l6-essence-formulas.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: yt-business-formula-l6-essen ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 17, column 1:
    - src_20260613_6b939d2b-yitang-b ... 
    ^ |
| `concepts\yt-business-formula-ten-paradigms.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: yt-business-formula-ten-para ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 16, column 1:
    - src_20260613_6edbf0af-yitang-b ... 
    ^ |
| `concepts\yt-customer-acquisition-toolkit.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\yt-demand-analysis-hiking-map.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\yt-entrepreneur-259-milestone.md` | 缺少 title; 缺少 type; author 为空; status=enriched 但 reviewed_by=pending; 缺少 trust_level |
| `concepts\yt-entrepreneur-barriers.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 1:
    - src_20260614_8f80cb0f-一堂-课程地图精华串讲
    ^ |
| `concepts\yt-entrepreneur-business-growth.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 1:
    - src_20260614_720e62a1-theme-pe ... 
    ^ |
| `concepts\yt-entrepreneur-channel-exploration.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 1:
    - src_20260614_8f80cb0f-一堂-课程地图精华串讲
    ^ |
| `concepts\yt-entrepreneur-concentration-analysis.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 1:
    - src_20260522_9d98d526-business ... 
    ^ |
| `concepts\yt-entrepreneur-fundraising.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 24, column 1:
    - src_20260614_8f80cb0f-一堂-课程地图精华串讲
    ^ |
| `concepts\yt-entrepreneur-industrial-production.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 1:
    - src_20260614_8f80cb0f-一堂-课程地图精华串讲
    ^ |
| `concepts\yt-entrepreneur-industry-forecast.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 28, column 1:
    - src_20260614_b9fbfc2b-theme-in ... 
    ^ |
| `concepts\yt-entrepreneur-opportunity-selection.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 1:
    - src_20260614_8f80cb0f-一堂-课程地图精华串讲
    ^ |
| `concepts\yt-entrepreneur-pragmatic-startup.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 1:
    - src_20260614_8f80cb0f-一堂-课程地图精华串讲
    ^ |
| `concepts\yt-entrepreneur-product-core.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 29, column 1:
    - src_20260614_0e6fd2e7-theme-pr ... 
    ^ |
| `concepts\yt-entrepreneur-research-camp.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 21, column 1:
    - src_20260510_2ba8671c-创业-调研行动营口述01
    ^ |
| `concepts\yt-entrepreneur-scientific-method.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 24, column 1:
    - src_20260614_faa8021d-Y模型探索营-第二节课
    ^ |
| `concepts\yt-entrepreneur-spin-selling.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 22, column 1:
    - src_20260510_349a66fd-读书会-spin销售法
    ^ |
| `concepts\yt-entrepreneur-truth-seeking.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 1:
    - src_20260614_8f80cb0f-一堂-课程地图精华串讲
    ^ |
| `concepts\yt-foresight-model-taxonomy.md` | 缺少 title; 缺少 type; author 为空; 缺少 trust_level |
| `concepts\yt-growth-cycle-model.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\yt-model-deep-review-iceberg.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - src_20260522_c92a36ba-ocr-一堂深度 ... 
    ^ |
| `concepts\yt-model-deliberate-practice-growth.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - src_20260522_e6cf558a-ocr-一堂刻意 ... 
    ^ |
| `concepts\yt-model-ipo-complete-checklist.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 22, column 1:
    - src_20260609_e3a27299-ocr-一堂-个 ... 
    ^ |
| `concepts\yt-model-liberate-thinking-layers.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - src_20260613_96e45c45-qishijia ... 
    ^ |
| `concepts\yt-model-management-map.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 23, column 1:
    - src_20260613_96e45c45-qishijia ... 
    ^ |
| `concepts\yt-model-muse-ai-framework.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 21, column 1:
    - src_20260510_62b2cfa1-一堂人工智能全景 ... 
    ^ |
| `concepts\yt-model-prediction-model.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 22, column 1:
    - src_20260522_e71d89ff-ocr-预判模型
    ^ |
| `concepts\yt-model-product-core-metrics.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - src_20260510_5ef61f8f-一堂产品内核十大典型指标
    ^ |
| `concepts\yt-model-product-excellence.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 22, column 1:
    - src_20260522_ea933690-ocr-顶级产品 ... 
    ^ |
| `concepts\yt-model-questioning-practice-canvas.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - src_20260510_e4a6ef49-提问刻意练习提升 ... 
    ^ |
| `concepts\yt-model-scientific-questioning-map.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - src_20260609_e13d29d9-ocr-一堂-个 ... 
    ^ |
| `concepts\yt-model-truman-career-routes.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 21, column 1:
    - src_20260522_9cbdf4fd-ocr-trum ... 
    ^ |
| `concepts\yt-model-truman-five-step-growth.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 21, column 1:
    - src_20260522_074c72ae-ocr-trum ... 
    ^ |
| `concepts\yt-model-y-organization.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 21, column 1:
    - src_20260613_96e45c45-qishijia ... 
    ^ |
| `concepts\yt-note-deliberate-practice-four-elements.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-personal-checklist-notes.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 31, column 1:
    - src_20260609_a7f2ae2e-ocr-一堂-a ... 
    ^ |
| `concepts\yt-personal-deliberate-practice.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 1:
    - src_20260609_e13d29d9-ocr-一堂-个 ... 
    ^ |
| `concepts\yt-personal-inspiration-flash.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 1:
    - src_20260522_e861d61d-ocr-泛产品设 ... 
    ^ |
| `concepts\yt-personal-knowledge-management.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 1:
    - src_20260505_7766e197-deepseek ... 
    ^ |
| `concepts\yt-personal-product-design.md` | 缺少 title; 缺少 type; author 为空; 缺少 trust_level |
| `concepts\yt-personal-thinking-models.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 25, column 1:
    - src_20260614_1be3d76f-一堂-思维模型案例分享
    ^ |
| `concepts\yt-personal-time-management.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 1:
    - src_20260614_720e62a1-theme-pe ... 
    ^ |
| `concepts\yt-personal-verbatim-script.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 27, column 1:
    - src_20260614_720e62a1-theme-pe ... 
    ^ |
| `concepts\yt-personal-y-model-practice.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 24, column 1:
    - src_20260614_842be4c9-一堂-Y模型实操探索营
    ^ |
| `concepts\yt-product-kernel-cultivation.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\yt-scale-economy-weapon-library.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    domain:
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 22, column 1:
    - src_20260611_79848c35-一堂-一堂五步法 ... 
    ^ |
| `concepts\yt-unit-model-three-tools.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\互联网医院模式深度调研报告.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    id: 互联网医院模式深度调研报告
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 12, column 1:
    - src_20260501_9962715b-互联网医院模式深 ... 
    ^ |
| `concepts\人机协作决策-双三角模型.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\诊所o2o外卖平台业务深度调研报告.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `concepts\鑫港湾his系统分阶段整改报告.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `dark-knowledges\dk-f13-handwritten-yaml-parser.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 33, column 5:
      - signal: "批量修改 frontmatter 的脚本使用字 ... 
        ^
expected <block end>, but found '<scalar>'
  in "<unicode string>", line 33, column 57:
     ... atter 的脚本使用字符串替换、正则或 `.split(\\"---
                                         ^ |
| `dark-knowledges\dk-modeling-business-visual-logic-match.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `dark-knowledges\dk-p15-unverified.md` | YAML 解析错误: None |
| `dark-knowledges\dk-skill-market-agent-self-install.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: dk-skill-market-agent-self-i ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 14, column 1:
    - src_20260606_6ea91aa8-纪浩-AI协作方 ... 
    ^ |
| `dark-knowledges\yt-note-ai-p-role-not-c-role.md` | author 为空 |
| `dark-knowledges\yt-note-p-c-role-boundary-realworld.md` | author 为空 |
| `dark-knowledges\yt-note-three-level-evolution.md` | author 为空 |
| `decisions\kdo-protocol-implementation-roadmap.md` | 缺少 confidence |
| `decisions\modeling-capability-for-kdo.md` | source_refs 为空 |
| `decisions\plan_20260621_skill-iteration-standard.md` | 缺少 trust_level |
| `domains\ai-collaboration-domain-digest.md` | status=enriched 但 reviewed_by=pending |
| `domains\decision-science-domain-digest.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `domains\lean-startup-domain-digest.md` | status=enriched 但 reviewed_by=pending |
| `domains\yitang-domain-digest.md` | status=enriched 但 reviewed_by=pending |
| `entities\Kimi-月之暗面.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    title: Kimi（月之暗面）
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 39, column 1:
    - src_20260503_52ae08ba-kdo_prod ... 
    ^ |
| `entities\YC-Y-Combinator.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    title: Y Combinator
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 39, column 1:
    - src_20260430_8cc84e5b-yc-放出一套a ... 
    ^ |
| `entities\一堂.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    title: 一堂
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 21, column 1:
    - src_20260613_6b939d2b-yitang-b ... 
    ^ |
| `entities\紫鲸AI.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    title: 紫鲸AI
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 36, column 1:
    - src_20260428_29929c1f-紫鲸ai智能体工作流平台
    ^ |
| `entities\鑫港湾.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    title: 鑫港湾
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 39, column 1:
    - src_20260503_52ae08ba-kdo_prod ... 
    ^ |
| `frameworks\ai-complex-communication.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: ai-complex-communication
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 17, column 1:
    - src_20260614_d79b42d1-D同学-AI技术落地案例
    ^ |
| `frameworks\beverage-foodservice-channel.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: beverage-foodservice-channel
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - src_20260614_8a0317f1-产品-市场分析讨论
    ^ |
| `frameworks\concept-mckinsey-hypothesis-driven.md` | source_refs 为空 |
| `frameworks\framework-ci-operating-model.md` | author 为空 |
| `frameworks\framework-multi-agent-research-architecture.md` | author 为空 |
| `frameworks\framework-strategy-brm.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    id: framework-strategy-brm
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 19, column 1:
    - 00_inbox/战略专题/引擎点火20260110 战略破 ... 
    ^ |
| `frameworks\framework-strategy-six-stages.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\framework-structured-analytic-techniques.md` | author 为空 |
| `frameworks\framework-yitang-channel-unit-economics.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
    id: framework-yitang-channel-uni ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 20, column 1:
    - 00_inbox/一堂五步法之增长/truman-渠道探索方 ... 
    ^ |
| `frameworks\smart-device-foodservice-automation.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: smart-device-foodservice-aut ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 17, column 1:
    - src_20260614_909802bd-智能设备-外卖对 ... 
    ^ |
| `frameworks\yt-business-formula-qualitative-metrics-library.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `frameworks\yt-tob-growth-channel.md` | source_refs 为空 |
| `frameworks\yt-tob-solution-model.md` | source_refs 为空 |
| `index.md` | YAML 解析错误: None |
| `links\index.md` | YAML 解析错误: None |
| `systems\agent-external-brain-design.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    title: Agent 外挂大脑设计
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 14, column 1:
    - src_20260503_52ae08ba-kdo_prod ... 
    ^ |
| `systems\agent-native-card-design.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    id: agent-native-card-design
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 15, column 1:
    - src_20260503_52ae08ba-kdo_prod ... 
    ^ |
| `systems\graph-rag-retrieval-layer.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 4, column 1:
    title: Graph RAG 检索层技术说明
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 18, column 1:
    - src_20260502_7d7c1b7c-kimi-深度调 ... 
    ^ |
| `systems\kdo-protocol.md` | confidence 非数字: 0.6# KDO Protocol — AI-Agent Operating Contract |
| `systems\obsidian-git-sync-protocol.md` | 缺少 confidence |
| `tools\smart-medicine-cabinet-financial-model.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: smart-medicine-cabinet-finan ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 18, column 1:
    - src_20260613_26c69f98-corr_202 ... 
    ^ |
| `tools\smart-medicine-cabinet-fraud-detection.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 5, column 1:
    id: smart-medicine-cabinet-fraud ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 18, column 1:
    - src_20260613_26c69f98-corr_202 ... 
    ^ |
| `tools\tool-agent-research-pipeline.md` | author 为空 |
| `tools\tool-agent-research-supervisor.md` | author 为空 |
| `tools\tool-agent-research-swarm.md` | author 为空 |
| `tools\tool-ai-landing-five-steps.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: tool-ai-landing-five-steps
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 15, column 1:
    - src_20260606_ef4877d0-所以90的核心问题
    ^ |
| `tools\tool-ai-research-five-steps.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: tool-ai-research-five-steps
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 15, column 1:
    - src_20260606_90b44191-没有人呀现在
    ^ |
| `tools\tool-ai-scene-four-elements.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: tool-ai-scene-four-elements
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 15, column 1:
    - src_20260606_ef4877d0-所以90的核心问题
    ^ |
| `tools\tool-ci-define-phase.md` | author 为空 |
| `tools\tool-ci-implement-phase.md` | author 为空 |
| `tools\tool-devils-advocacy.md` | author 为空 |
| `tools\tool-indicators-signposts.md` | author 为空 |
| `tools\tool-key-assumptions-check.md` | author 为空 |
| `tools\tool-lean-ai-accelerated-validation.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-cut-features.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-fake-marketing.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-fake-product.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-human-replace-rnd.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-human-replace-system.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-leverage-competitor.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-leverage-resources.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-leverage-tools.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-leverage-traffic.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-minimum-test-volume.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-minimum-version.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-premium-service.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-presell.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-product-kernel-metrics.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-lean-stealth-service.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-red-team-analysis.md` | author 为空 |
| `tools\tool-smart-medicine-cabinet-site-selection-guide.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    id: tool-smart-medicine-cabinet- ... 
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 15, column 1:
    - src_20260613_59270720-corr_202 ... 
    ^ |
| `tools\tool-strategy-12-word-test.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: tool-strategy-12-word-test
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 14, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-competition-traps.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    id: tool-strategy-competition-traps
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 15, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-five-see-three-set.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    id: tool-strategy-five-see-three-set
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 18, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-four-layers.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: tool-strategy-four-layers
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 13, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-four-moves.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: tool-strategy-four-moves
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 13, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-gap-analysis.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    id: tool-strategy-gap-analysis
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 18, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-logistics-cost-planning.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-market-opportunity-matrix.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-nine-problems.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    id: tool-strategy-nine-problems
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 18, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-pareto.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: tool-strategy-pareto
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 16, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-sentence-formula.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 2, column 1:
    id: tool-strategy-sentence-formula
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 13, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-three-horizons.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 3, column 1:
    id: tool-strategy-three-horizons
    ^
expected <block end>, but found '-'
  in "<unicode string>", line 18, column 1:
    - src_unknown
    ^ |
| `tools\tool-strategy-value-capture.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-channel-partnership-design.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-practice-20hour-starter.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `tools\tool-一堂-business-prediction-15-char.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `tools\tool-一堂-five-step-validation.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `tools\tool-使用一页纸速查卡快速调用框架.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `tools\tool-纪浩-AI对话上下文隔离.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `tools\tool-马易-业务为先的AI中台建设.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `tools\yt-tool-business-formula-metrics-checklist.md` | 缺少 id; 缺少 title; 缺少 type; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `tools\yt-tool-unit-model-ai-assisted.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-unit-model-benchmark.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-unit-model-construction.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-unit-model-dynamic.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-unit-model-selection.md` | status=enriched 但 reviewed_by=pending |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `cases\case-ai-agent-milestone-design.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-ai-assisted-review.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-ban-fei-mao-from-assignment-to-tool.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-candy-problem-os-vpn.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-泛产品设计-用户卡片-场景推演, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; trust_level=high 但 source 仅 1 个 |
| `cases\case-child-drawing-rhyme.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-course-milestone-model.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-decision-ai-assisted-vs-human.md` | dangling 链接: concept-AI时代双三角竞争力|AI 时代双三角竞争力, framework-decision-cognitive-bias-map|认知偏差地图, dk-decision-when-to-defer|何时应该推迟决策, framework-decision-quality-checklist|决策质量六问检查表 |
| `cases\case-deepfake-market-misuse.md` | dangling 链接: ocr-泛产品设计-落地卡片-风险管理 |
| `cases\case-demand-ai-fitness-four-forces.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-demand-b2b-enterprise-erp.md` | dangling 链接: framework-demand-validation-pipeline|需求验证流水线, yt-tob-demand-metrics|To B 需求测算双指标, yt-demand-decision-chain|ToB决策链需求分析, framework-demand-iceberg|需求洞察冰山模型 |
| `cases\case-demand-b2c-consumer-insight.md` | dangling 链接: framework-demand-usp-model|USP 模型, case-demand-milkshake-jtbd|JTBD 方法, yt-demand-motivation-resistance|需求动机与阻力分析, yt-demand-peak-end-rule|峰终定律, dk-demand-signal-vs-noise|需求信号与噪音的区分 |
| `cases\case-demand-dialer.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-demand-elderly-smart-device.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-深度-案例02, ocr-一堂-科学决策-深度-案例04, ocr-一堂-案例拆解-课程清单 |
| `cases\case-demand-equestrian-three-tasks.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-demand-financial-literacy.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-indonesia-insurance.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-demand-milkshake-jtbd.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-pharma-bigdata.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-restaurant-hiring.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-rural-5g.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-silver-parenting.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-tier4-housekeeping.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-地图-创业地图_conv, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-doris-beauty-ecommerce-channel.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-catering-chain-benchmark.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-crossborder-ecommerce-opportunity.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-grab-industry-cognition.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-outbound-travel-community.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-essence-entrepreneurship.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-essence-humanity-trap.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-ether-online-acquisition.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-guang-leng-dian-zi-hx-smj.md` | dangling 链接: ocr-项目背景问题思考的8个维度, ocr-泛产品设计-用户卡片-项目背景分析, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-jh-yitang-vs-sqlhelper.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-lean-building-in-vacuum.md` | dangling 链接: framework-lean-false-model|FALSE 模型, framework-lean-six-wastes|六宗罪 |
| `cases\case-liutao-douyin-team-leader-9m.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-liutao-electric-bike-localization.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-modeling-abstraction-reliability-ladder.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-modeling-abstraction-yitang-models.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-modeling-essence-levels.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-modeling-essence-schools.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-modeling-process-livestream-prep.md` | dangling 链接: ocr-truman的选择两条职业成长路线 |
| `cases\case-modeling-process-livestream-roles.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-modeling-process-sop-evolution.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂y模型steps策略集, ocr-一堂-ai学习-提问工程化, ocr-一堂-个人修炼-讲香十指模型-超级武器库 |
| `cases\case-modeling-process-sop-examples.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-neworiental-prospectus-marketing.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-nine-pm-livestream-survey.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-personal-map-modeling.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂个人地图高潜力成长者修炼全景图, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-popmart-prospectus-pricing.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-proya-betaine-skincare-benchmark.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-failure-01-cosmetics.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-strategy-failure-02-supermarket.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-strategy-failure-03-cleaning.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-strategy-failure-04-appliance.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-failure-09-boeing.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-strategy-model-selection-quiz.md` | dangling 链接: ocr-一堂-个人修炼-科学提问刻意练习, ocr-一堂刻意练习十年成长指数, ocr-一堂-个人修炼-提问刻意练习画布 |
| `cases\case-strategy-practice-10-turnaround.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-strategy-practice-11-third-place.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-12-zero-loss.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-ranpeng-crossborder.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-strategy-revival-13-bestore.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-strategy-revival-14-gucci.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单; confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-shell-oil.md` | dangling 链接: ocr-一堂-单元模型-动态预测 |
| `cases\case-strategy-snack-business-design.md` | dangling 链接: ocr-一堂-单元模型-示例01, ocr-一堂-单元模型-示例 |
| `cases\case-thousand-people-square.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂y模型steps策略集, ocr-一堂-ai学习-提问工程化, ocr-一堂-科学决策-x型y型决策习惯对比 |
| `cases\case-toc-content-platform-correlation-trap.md` | dangling 链接: 紫鲸ai_智能体工作流平台_深度分析与产品设计 |
| `cases\case-truman-ai-skill-engineering-guide.md` | dangling 链接: ocr-一堂-高阶体系探索营-三种咨询可能性 |
| `cases\case-truman-motivation-map-12-versions.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计-用户卡片-场景推演 |
| `cases\case-truman-prd-checklist-evolution.md` | dangling 链接: ocr-truman的选择两条职业成长路线 |
| `cases\case-truman-sales-report-structure.md` | dangling 链接: ocr-truman的选择两条职业成长路线 |
| `cases\case-unit-model-gashapon.md` | dangling 链接: ocr-一堂-单元模型-扭蛋机案例 |
| `cases\case-yi-tang-ai-gao-kao-zhi-yuan-kernel-mismatch.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-yitang-ai-time-management-coach.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-beauty-device-overseas-sales.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-competitor-pricing-intelligence.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-consumer-offline-channel-decision.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-doorstep-nail-service-context.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-double-triangle-confidence.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-人机协作-双三角模型, ocr-一堂-科学决策-深度-案例04, ocr-一堂-个人修炼-双三角模型, ocr-一堂-科学决策-深度-案例02 |
| `cases\case-yitang-elderly-home-roleplay.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-fake-interview-intelligence.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-hardware-factory-photo.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-jtbd-story-formula.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-luckin-field-research.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-mahjong-machine-fake-order.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-model-asset-inventory.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-yitang-model-valuation-flywheel.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-yitang-pet-fostering-user-research.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-radar-chart-selection.md` | dangling 链接: ocr-truman的选择两条职业成长路线 |
| `cases\case-yitang-sanjieke-benchmark-failure.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-ski-project-user-as-expert.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-supplier-security-guard.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-tob-grinding-machine.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04 |
| `cases\case-yitang-track-selection-research.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-travel-receipt-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglan-amusement-park-undercover.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglei-furniture-overseas-market-selection.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglei-nursing-home-family.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhangyang-anchor-sop-three-locks.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02, ocr-一堂-案例拆解-课程清单 |
| `cases\case-一堂-陈贤敏汉堡-hypothesis-validation.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-关键假设abcd模型, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-深度-案例04, ocr-一堂-科学决策-深度-案例02 |
| `cases\case-纪浩-focus-prompt-design.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计-用户卡片-场景推演, ocr-泛产品设计落地篇 |
| `cases\yt-product-kernel-shampoo-case.md` | dangling 链接: ocr-一堂五步法-产品内核画布, ocr-一堂产品内核-十大典型指标 |
| `concepts\2026-05-17-深夜感想.md` | dangling 链接: ocr-一堂-单元模型-找全成本实操难点, ocr-一堂-单元模型-找基准值实操难点 |
| `concepts\ai-tool-learning-curve.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\ai-tool-learning-workbook.md` | dangling 链接: productization-judgment|产品化判断, yai-tcp-teacher-role|YAI 教师角色, yai-counsel-role|YAI 咨询模式, practice-card-decomposition|练习卡片拆解, fixed-routine-design|固定套路设计 |
| `concepts\ai-virtual-coach-prompt.md` | dangling 链接: productization-judgment|产品化判断, timely-feedback-loop|反馈闭环, yai-tcp-teacher-role|YAI 教师角色, four-questions-feedback|四问法自我反馈, timely-feedback-loop|及时反馈闭环 |
| `concepts\aima-ai思维卡-外部链接归档.md` | dangling 链接: ocr-一堂y模型-科学成事道理, ocr-ocr_snipaste_2026-05-15_21-39-40, ocr-ocr_screenshot2, ocr-一堂-地图-创业地图_conv, ocr-truman的个人成长五步法 |
| `concepts\business-analysis.md` | dangling 链接: ocr-一堂-单元模型-找基准值实操难点 |
| `concepts\challenge-point-design.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\comfort-zone-expansion.md` | dangling 链接: productization-judgment|产品化判断, deliberate-practice-four-elements|刻意练习四要素, yt-management-team-knowledge|团队知识管理, yai-tcp-teacher-role|YAI 教师角色, timely-feedback-loop|及时反馈闭环 |
| `concepts\completion-criteria-design.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-ai-native-organization-five-steps.md` | dangling 链接: ocr-一堂y模型steps策略集 |
| `concepts\concept-candy-ai-as-collaborator.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-harness-cattle-not-pets.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-harness-scoring-anchors.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-kdo-review-workflow.md` | dangling 链接: <code>kdo pre-submit</code>, <code>kdo lint</code>, ec工业化规范手册-v2.8.0|EC 工业化规范手册, ec工业化规范手册-v2.8.0|EC 工业化规范手册, framework-kdo-self-attack|KDO 知识自攻击 |
| `concepts\concept-strategy-2024-2026-supplement.md` | dangling 链接: ocr-一堂-科学决策-深度-你的业务是一次抽样实验, ocr-一堂-科学决策-宽度-个人, ocr-一堂-科学决策-稀缺资源清单, ocr-一堂-科学决策-x型y型决策习惯对比, ocr-一堂-科学决策-宽度-团队 |
| `concepts\concept-strategy-framework-landscape.md` | dangling 链接: ocr-一堂-科学决策-roi高阶训练全景图, ocr-一堂-个人修炼-全景图muse模型, ocr-一堂个人地图高潜力成长者修炼全景图; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-streaming-extraction-pattern.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\concept-thousand-people-square.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂-单元模型-对抗小抄01, ocr-一堂y模型steps策略集, ocr-一堂-人机协作-双三角模型 |
| `concepts\concept-wanghuan-ai-native-definition.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-泛产品设计-审美工具箱指南, ocr-泛产品设计落地工具篇指南 |
| `concepts\concept-wanghuan-tacit-knowledge-examples.md` | dangling 链接: ocr-一堂-单元模型-单销售模型 |
| `concepts\concept-yitang-ai-research-10-assumptions.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yitang-ideal-research-goal.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-一堂-kernel-iteration.md` | trust_level 值异常: medium# 产品内核迭代：从静态到动态的五方向演化 |
| `concepts\concept-一堂-kernel-validation.md` | trust_level 值异常: medium# 产品内核验证：三维度评估 + 六策略验证 |
| `concepts\concept-一堂-product-kernel.md` | trust_level 值异常: high# 产品内核：用户愿意选择你的最小解决方案 |
| `concepts\concept-最简单元模型.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂-单元模型-单履约模型, ocr-一堂-单元模型-对抗小抄01, ocr-一堂-单元模型-单商圈模型, ocr-一堂-单元模型-规模经济对抗武器库 |
| `concepts\deepseek-v4-在知识管理系统中的应用.md` | dangling 链接: ocr-泛产品设计的应用场景示意图 |
| `concepts\deliberate-repetition.md` | dangling 链接: productization-judgment|产品化判断, deliberate-practice-four-elements|刻意练习四要素, comfort-zone-expansion|舒适区扩展, yai-tcp-teacher-role|YAI 教师角色, timely-feedback-loop|及时反馈闭环 |
| `concepts\design-ai-image-generation.md` | dangling 链接: yt-panproduct-execution-design-principles |
| `concepts\fixed-routine-design.md` | dangling 链接: productization-judgment|产品化判断, deliberate-practice-four-elements|刻意练习四要素, comfort-zone-expansion|舒适区扩展, timely-feedback-loop|及时反馈闭环, yai-counsel-role|YAI 咨询模式 |
| `concepts\four-questions-feedback.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\kdo-yaml-frontmatter-safety.md` | dangling 链接: ocr-泛产品设计-审美工具箱指南, obsidian-kdo-内容产出工作流-产品设计大纲 |
| `concepts\kdo_product_design_agent_final.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计-用户卡片-场景推演, ocr-泛产品设计-落地卡片-低成本测试mvp, ocr-泛产品设计落地篇 |
| `concepts\knowledge-delivery-os-快速体验指南-飞书云文档.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-泛产品设计-审美工具箱指南 |
| `concepts\learning-thinking.md` | dangling 链接: yt-panproduct-execution-liberate-thinking |
| `concepts\paddleocr-skill.md` | dangling 链接: ocr-微信图片_20260507004806_40_32, ocr-微信图片_20260507004801_37_32, ocr-微信图片_20260507004811_41_32, ocr-微信图片_20260507004758_35_32 |
| `concepts\pilot-atomic-chunk-comparison.md` | dangling 链接: ocr-一堂-科学决策-稀缺机会窗口 |
| `concepts\practice-card-decomposition.md` | dangling 链接: productization-judgment|产品化判断, yai-tcp-teacher-role|YAI 教师角色, timely-feedback-loop|及时反馈闭环, deliberate-repetition|刻意重复, yai-counsel-role|YAI 咨询模式 |
| `concepts\product-business-strategy.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计-用户卡片-惊喜公式, ocr-泛产品设计-落地卡片-低成本测试mvp, ocr-泛产品设计落地篇 |
| `concepts\productization-judgment.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\supply-chain-beverage.md` | dangling 链接: ocr-一堂-单元模型-找全成本实操难点, ocr-泛产品设计-落地卡片-低成本测试mvp |
| `concepts\timely-feedback-loop.md` | dangling 链接: four-questions-feedback|四问法, productization-judgment|产品化判断, deliberate-practice-four-elements|刻意练习四要素, ai-virtual-coach-prompt|AI 虚拟教练提示词, yt-growth-data-driven-decision|数据驱动决策 |
| `concepts\tools-workflows.md` | dangling 链接: yt-panproduct-execution-good-tools |
| `concepts\yai-counsel-role.md` | dangling 链接: 刻意练习方法论; trust_level=high 但 source 仅 1 个 |
| `concepts\yai-tcp-teacher-role.md` | dangling 链接: 咨询对话框架, ai-consultation-mindset-shift, 刻意练习方法论; trust_level=high 但 source 仅 1 个 |
| `concepts\yitang-huazong-ama-summary.md` | dangling 链接: ocr-一堂-科学决策-人机协作决策, ocr-一堂-人机协作-双三角模型, ocr-一堂-个人修炼-双三角模型 |
| `concepts\yitang-methodology-system.md` | dangling 链接: ocr-一堂进步大地图, ocr-一堂进步大地图_compressed, ocr-一堂-科学决策-一堂双三角磨合追求-从入门到无限进步 |
| `concepts\yt-barrier-network-effects-deep.md` | dangling 链接: ocr-一堂-科学决策-深度-你的业务是一次抽样实验, ocr-一堂-科学决策-深度-l4-案例01, ocr-一堂-科学决策-深度-l4严格财务公式, ocr-一堂-科学决策-深度-案例04, ocr-一堂深度复盘冰山图 |
| `concepts\yt-barrier-offensive-strategy.md` | dangling 链接: ocr-一堂-单元模型-壁垒预判 |
| `concepts\yt-barrier-scale-economies.md` | dangling 链接: ocr-一堂-单元模型-规模经济对抗武器库 |
| `concepts\yt-business-model-cash-flow.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\yt-business-model-competitive-moat.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\yt-business-model-definition.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\yt-business-model-freemium.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\yt-business-model-partnership.md` | dangling 链接: ocr-一堂-单元模型-abcd策略模型, ocr-一堂y模型steps策略集, ocr-一堂-个人修炼-科学学习ipo-全景策略 |
| `concepts\yt-business-model-subscription.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\yt-decision-depth-ladder.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-泛产品设计-审美工具箱指南, ocr-泛产品设计落地工具篇指南 |
| `concepts\yt-decision-width-method.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-泛产品设计-审美工具箱指南, ocr-一堂-科学决策-稀缺资源清单, ocr-一堂-科学决策-关键训练清单重要, ocr-一堂-ai清单体笔记系统故事线-truman-图片01 |
| `concepts\yt-demand-peak-end-rule.md` | dangling 链接: ocr-泛产品设计-用户卡片-峰终定律 |
| `concepts\yt-entrepreneur-unit-model.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-foresight-deliverables-four-levels.md` | dangling 链接: ocr-一堂-科学决策-关键假设abcd模型, plan_20260531_data-curator-v1, plan_20260531_data-curator-v1.1 |
| `concepts\yt-growth-market-led-growth.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\yt-growth-product-led-growth.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\yt-growth-sales-led-growth.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `concepts\yt-growth-user-onboarding.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-泛产品设计-落地卡片-低成本测试mvp, ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计-用户卡片-场景推演 |
| `concepts\yt-model-agent-architecture.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂-单元模型-对抗小抄01, ocr-一堂y模型steps策略集, ocr-一堂-人机协作-双三角模型 |
| `concepts\yt-model-prompt-engineering.md` | confidence=0.9 但 source 仅 1 个 |
| `concepts\yt-note-deliberate-practice-four-elements.md` | dangling 链接: deliberate-practice-four-elements|刻意练习四要素, yt-note-checklist-concept|清单体笔记概念, yt-note-ai-human-division|AI 与人的笔记分工, yt-note-expert-interview-modeling|专家访谈建模 |
| `concepts\yt-product-kernel-add-subtract.md` | dangling 链接: ocr-一堂五步法-产品内核画布, ocr-一堂产品内核-十大典型指标 |
| `concepts\yt-product-kernel-definition.md` | dangling 链接: ocr-一堂-科学决策-项目方案评估三角形, ocr-一堂产品内核-十大典型指标 |
| `concepts\yt-product-kernel-key-conversion.md` | dangling 链接: ocr-一堂五步法-产品内核画布, ocr-一堂产品内核-十大典型指标 |
| `concepts\yt-product-kernel-user-perspective.md` | dangling 链接: ocr-泛产品设计-用户卡片-用户视角 |
| `concepts\yt-skill-checklist-as-ai-protocol.md` | dangling 链接: ocr-一堂-ai学习-提问工程化 |
| `concepts\yt-tob-sales-unit-model.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-tool-best-practice-learning.md` | dangling 链接: ocr-泛产品设计-审美卡片-最佳实践池子, ocr-泛产品设计-审美卡片-最佳实践建模, ocr-泛产品设计-审美卡片-最佳实践收集 |
| `concepts\yt-tool-mental-model-refinement.md` | dangling 链接: ocr-一堂提炼过的因果模型 |
| `concepts\yt-tool-peas-agent-analysis.md` | dangling 链接: ocr-一堂-ai清单体笔记系统故事线-truman-图片01 |
| `concepts\人机协作决策-双三角模型.md` | source_refs 为空 |
| `concepts\在设计小伙伴的反馈还挺好的.md` | dangling 链接: ocr-一堂-人机协作-双三角模型, ocr-一堂-单元模型-找全成本实操难点 |
| `concepts\开源HIS系统代码深度分析报告.md` | dangling 链接: 紫鲸ai_智能体工作流平台_深度分析与产品设计 |
| `concepts\紫鲸ai智能体工作流平台.md` | dangling 链接: 紫鲸ai_智能体工作流平台_深度分析与产品设计 |
| `concepts\老朱的水感-2026年5月.md` | dangling 链接: ocr-一堂-单元模型-找全成本实操难点 |
| `concepts\诊所o2o外卖平台业务深度调研报告.md` | source_refs 为空 |
| `concepts\那今天不会.md` | dangling 链接: ocr-一堂-单元模型-abcd策略模型, ocr-一堂-单元模型-示例 |
| `dark-knowledges\dk-c3-txt-ingest-skip.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-c7-auto-backup-conflict.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-decision-when-to-defer.md` | dangling 链接: dk-你的业务是一次抽样实验|你的业务是一次抽样实验, framework-decision-cognitive-bias-map|认知偏差地图, framework-decision-quality-checklist|决策质量六问检查表, concept-稀缺机会窗口|稀缺机会窗口, master-decision-hygiene|决策卫生五步法 |
| `dark-knowledges\dk-demand-feature-stacking.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-hidden-need.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-misjudgment-rate.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-dialer.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-financial-literacy.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-indonesia-insurance.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-restaurant-hiring.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-rural-5g.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-tier4-housekeeping.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-pitfall-travel-agent.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-premature-solution.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-demand-signal-vs-noise.md` | dangling 链接: yt-research-user-jtbd|用户 JTBD 调研方法, yt-demand-early-validation|需求早期验证, framework-decision-cognitive-bias-map|认知偏差地图, framework-demand-validation-pipeline|需求验证流水线, yt-demand-market-size-pitfalls|市场规模估算的5个陷阱 |
| `dark-knowledges\dk-demand-switching-cost.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-f1-regex-on-cjk.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f10-broken-source-refs.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f11-encyclopedia-style.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f14-accuracy-measurement-mismatch.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f2-txt-ingest-skip.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f4-wrong-workdir.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f5-stale-feedback-ref.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f6-cjk-skeleton-corruption.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f7-surface-translation.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f8-phony-wikilink.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-f9-generic-critique.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-infrastructure-guardrails-over-checklist.md` | dangling 链接: ocr-一堂-科学决策-稀缺资源清单, ocr-一堂-科学决策-关键训练清单重要, ocr-一堂-ai清单体笔记系统故事线-truman-图片01, ocr-一堂-案例拆解-课程清单 |
| `dark-knowledges\dk-modeling-ai-self-retrospection.md` | dangling 链接: ocr-一堂-科学决策-稀缺资源清单, ocr-一堂-科学决策-关键训练清单重要, ocr-一堂-ai清单体笔记系统故事线-truman-图片01, ocr-一堂-案例拆解-课程清单 |
| `dark-knowledges\dk-modeling-checklist-formatting-rules.md` | dangling 链接: ocr-一堂-科学决策-深度-l1优先级定性 |
| `dark-knowledges\dk-modeling-expert-consensus-five-percent.md` | dangling 链接: ocr-一堂-科学决策-高水平共识曲线重要, ocr-泛产品设计-落地卡片-灵感闪现 |
| `dark-knowledges\dk-modeling-unit-pairs-milestone.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂-单元模型-对抗小抄01, ocr-一堂y模型steps策略集, ocr-一堂-人机协作-双三角模型 |
| `dark-knowledges\dk-p11-regex-cutoff.md` | trust_level 值异常: medium# p-11：validator `section_content` regex 在 `###` 处截断——所有文章 word count 失效 |
| `dark-knowledges\dk-p14-zombie.md` | dangling 链接: obsidian-kdo-内容产出工作流-产品设计大纲 |
| `dark-knowledges\dk-p17-accuracy-gap.md` | dangling 链接: ocr-项目背景问题思考的8个维度 |
| `dark-knowledges\dk-p20-bigram-fail.md` | dangling 链接: ocr-screenshot2 |
| `dark-knowledges\dk-p4-batch-format-empty.md` | dangling 链接: ocr-泛产品设计-落地卡片-努力仿真, ocr-泛产品设计-落地卡片-十倍速验证, ocr-泛产品设计-用户卡片-动力阻力, ocr-泛产品设计-审美卡片-最佳实践建模, ocr-泛产品设计-落地卡片-攻坚会 |
| `dark-knowledges\dk-p7-ocr-skip.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型steps策略集, ocr-一堂-ai学习-提问工程化, ocr-一堂-人机协作-双三角模型, ocr-泛产品设计-落地卡片-攻坚会 |
| `dark-knowledges\dk-strategy-01-not-goal-setting.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-02-three-paradoxes.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-03-advantage-temporary.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-04-consulting-trap.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-05-positioning-trap.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-06-dividend-to-strategy.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-07-strategy-vs-dividend.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-08-not-local-optimum.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-longzhong-four-failures.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-strategy-three-must-do-moments.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-tool-as-phased-validator.md` | dangling 链接: skill-note-one-line-one-point |
| `dark-knowledges\dk-yb1-aigc-mvp-before-ps.md` | dangling 链接: yt-panproduct-execution-low-cost-mvp |
| `dark-knowledges\dk-yb18-small-shop-image-mismatch.md` | dangling 链接: ocr-一堂-单元模型-单客户模型 |
| `dark-knowledges\dk-yitang-business-formula-plus-times-trap.md` | dangling 链接: ocr-泛产品设计-落地卡片-里程碑拆解, ocr-一堂-案例拆解-课程清单 |
| `dark-knowledges\yt-note-three-level-evolution.md` | dangling 链接: ocr-一堂-ai清单体笔记系统故事线-truman-图片01 |
| `decisions\fix-data-curator-parse-bug.md` | dangling 链接: ocr-微信图片_20260507004751_33_32 |
| `decisions\huangyaoshi-data-alignment-response.md` | trust_level 值异常: low# 黄药师对齐回应：对欧阳锋补充的意见 + 4 个分歧 |
| `decisions\labeling-final-consolidation.md` | trust_level 值异常: low# 数据标注方案最终汇总 — 三方调研 + 黄药师独立判断 |
| `decisions\modeling-capability-for-kdo.md` | dangling 链接: ocr-一堂-科学决策-稀缺资源清单, ocr-一堂-科学决策-x型y型决策习惯对比, ocr-一堂-科学决策-宽度-团队, ocr-一堂-科学决策-roi决策评估画布, ocr-一堂-科学决策-深度-l1优先级定性; trust_level=high 但 source 仅 0 个 |
| `decisions\plan_20260621_domain-index-infrastructure.md` | status 值异常: approved; dangling 链接: <code>check-source-refs.py</code>, <code>track-production-progress.py</code> |
| `decisions\plan_20260621_skill-iteration-standard.md` | status 值异常: approved |
| `decisions\sprint-6-cli-gap-proposal.md` | trust_level 值异常: low# sprint 6 cli 缺口修复提案 |
| `dk\dk-research-decision-first-mapping.md` | dangling 链接: ocr-一堂-科学决策-深度-你的业务是一次抽样实验, ocr-一堂-科学决策-宽度-个人, ocr-一堂-科学决策-稀缺资源清单, ocr-一堂-科学决策-x型y型决策习惯对比, ocr-一堂-科学决策-宽度-团队 |
| `dk\dk-yitang-digging-belief.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-expert-interview-5-traps.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-public-info-is-enough.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-ai-hallucination.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-cost-value-match.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-desperate-effort.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-goal-before-efficiency.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-source-freshness.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-starter-vs-veteran.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-survivor-bias-in-research.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-单元模型-对抗小抄.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂-单元模型-单履约模型, ocr-一堂-单元模型-对抗小抄01, ocr-一堂-单元模型-规模经济对抗武器库, ocr-一堂-单元模型-段位专家 |
| `dk\dk-单元模型-找全成本实操难点.md` | dangling 链接: ocr-一堂-单元模型-规模对抗实操难点, ocr-一堂-单元模型-找全成本实操难点, ocr-一堂-单元模型-找基准值实操难点, ocr-一堂-单元模型-找单元模型实操难点 |
| `dk\dk-单元模型-找单元模型实操难点.md` | dangling 链接: ocr-一堂-单元模型-找单元模型实操难点 |
| `dk\dk-单元模型-找基准值实操难点.md` | dangling 链接: ocr-一堂-单元模型-规模对抗实操难点, ocr-一堂-单元模型-找全成本实操难点, ocr-一堂-单元模型-找基准值实操难点, ocr-一堂-单元模型-找单元模型实操难点 |
| `dk\dk-单元模型-规模对抗实操难点.md` | dangling 链接: ocr-一堂-单元模型-规模对抗实操难点, ocr-一堂-单元模型-找全成本实操难点, ocr-一堂-单元模型-找基准值实操难点, ocr-一堂-单元模型-找单元模型实操难点 |
| `domains\ai-collaboration-domain-digest.md` | trust_level=high 但 source 仅 1 个 |
| `domains\decision-science-domain-digest.md` | dangling 链接: ocr-一堂-科学决策-深度-你的业务是一次抽样实验, concept-美好作品想象|美好作品想象, framework-个人成长五步法|个人成长五步法, tool-提问刻意练习画布|提问刻意练习画布, concept-AI时代双三角竞争力|AI 时代双三角竞争力 |
| `domains\domain-demand-analysis-index.md` | dangling 链接: yt-demand-competitive-displacement|需求替代陷阱, yt-research-user-jtbd|用户 JTBD 调研方法, yt-five-step-method-complete|五步法完整地图, yt-demand-early-validation|需求早期验证, yt-demand-peak-end-rule|峰终定律在需求分析中的应用; trust_level=high 但 source 仅 1 个 |
| `domains\five-step-domain-digest.md` | dangling 链接: ocr-泛产品设计-用户卡片-一堂五步法, ocr-一堂五步法-产品内核画布, ocr-一堂五步法画布 |
| `domains\strategy-domain-digest.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `domains\yitang-domain-digest.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `entities\七件事集团.md` | dangling 链接: case-qishijian-smart-medicine-cabinet; confidence=0.9 但 source 仅 1 个 |
| `frameworks\business-formula-to-kdo-card-quality.md` | dangling 链接: ocr-一堂-科学决策-关键假设abcd模型, ocr-一堂-单元模型-abcd策略模型, obsidian-kdo-内容产出工作流-产品设计大纲 |
| `frameworks\framework-TCPR底层网络协议.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂-单元模型-对抗小抄01, ocr-一堂y模型steps策略集, ocr-一堂-人机协作-双三角模型 |
| `frameworks\framework-candy-transcript-workflow.md` | dangling 链接: ocr-泛产品设计-用户卡片-一堂五步法, ocr-一堂五步法画布, ocr-truman的个人成长五步法; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-decision-cognitive-bias-map.md` | dangling 链接: master-cognitive-bias-checklist|认知偏差检查清单, concept-X型Y型决策习惯|X型 vs Y型决策习惯, framework-decision-quality-checklist|决策质量六问检查表, dk-决策经验值|决策经验值; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-decision-quality-checklist.md` | dangling 链接: yt-decision-abcd-model|关键假设 ABCD 模型, master-decision-hygiene|决策卫生五步法; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-demand-opportunity-spectrum.md` | dangling 链接: ocr-一堂-单元模型-壁垒预判, ocr-预判模型; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-demand-usp-model.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型steps策略集, ocr-一堂-单元模型-对抗小抄02; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-demand-validation-pipeline.md` | dangling 链接: yt-demand-early-validation|需求早期验证, dk-demand-signal-vs-noise|需求信号与噪音的区分, tool-lean-fake-product|假产品, framework-demand-lean-bridge|需求判断与精益验证的衔接, framework-decision-quality-checklist|决策质量六问检查表; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-ouyangfeng-review-methodology.md` | status=draft 但 confidence=0.88 |
| `frameworks\framework-strategy-ansoff.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计-用户卡片-场景推演, ocr-泛产品设计-落地卡片-低成本测试mvp, ocr-泛产品设计落地篇 |
| `frameworks\framework-strategy-basics-01-core.md` | dangling 链接: yt-panproduct-execution-core-and-boundary; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-basics-02-insight.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂y模型steps策略集, ocr-一堂-人机协作-双三角模型, ocr-一堂-个人修炼-讲香十指模型-超级武器库; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-basics-04-system.md` | dangling 链接: ocr-一堂-高阶体系探索营-三种咨询可能性; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-basics-05-change.md` | dangling 链接: ocr-一堂-高阶体系探索营-三种咨询可能性; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-five-basics.md` | dangling 链接: ocr-一堂-高阶体系探索营-三种咨询可能性; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-mckinsey-7s.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂-单元模型-对抗小抄01, ocr-一堂y模型steps策略集, ocr-一堂-人机协作-双三角模型 |
| `frameworks\framework-strategy-six-stages.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-three-horizons.md` | dangling 链接: ocr-一堂-管理必修-课程清单, ocr-一堂-地图-管理地图_conv |
| `frameworks\framework-wanghuan-task-product-system.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计-用户卡片-场景推演, ocr-泛产品设计-落地卡片-低成本测试mvp, ocr-泛产品设计落地篇 |
| `frameworks\framework-yitang-channel-industrialization.md` | dangling 链接: framework-yitang-channel-exploration-4step|渠道探索四步法, concept-yitang-channel-lean-validation-bridge|渠道精益验证, framework-yitang-growth-flywheel|增长飞轮, framework-yitang-channel-unit-economics|渠道单元经济模型 |
| `frameworks\framework-yitang-research-weapon-supplement-2026.md` | status=draft 但 confidence=0.88 |
| `frameworks\framework-单元模型-外部对抗地图.md` | dangling 链接: ocr-一堂进步大地图, ocr-一堂-单元模型-外部对抗地图, ocr-一堂-地图-管理地图, ocr-一堂-个人修炼-讲香基本功-十指模型修炼地图, ocr-一堂个人地图高潜力成长者修炼全景图 |
| `frameworks\model-quality-four-levels.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂y模型steps策略集, ocr-一堂-人机协作-双三角模型, ocr-一堂-个人修炼-讲香十指模型-超级武器库 |
| `frameworks\modeling-personal-practice-loop.md` | dangling 链接: ocr-一堂-个人修炼-科学学习ipo模型, ocr-一堂-个人修炼-科学提问刻意练习, ocr-一堂-个人修炼-讲香基本功-十指模型修炼地图, ocr-一堂刻意练习十年成长指数, ocr-一堂-个人修炼-讲香十指模型-超级武器库 |
| `frameworks\modeling-to-kdo-toolchain.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计落地篇 |
| `frameworks\xingangwan-pharma-business-formulas.md` | dangling 链接: ocr-一堂-科学决策-深度-l4严格财务公式, ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `frameworks\yt-barrier-moat-building.md` | dangling 链接: ocr-一堂-ai学习-提问进化路线图 |
| `frameworks\yt-business-formula-business-pattern-selector.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `frameworks\yt-business-model-scalability.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-roi决策评估画布-案例04, ocr-一堂-科学决策-商业模式-完整财务公式决策, ocr-一堂-科学决策-roi决策评估画布 |
| `frameworks\yt-five-step-method-complete.md` | dangling 链接: ocr-一堂-单元模型-壁垒预判 |
| `frameworks\yt-growth-to-barrier.md` | dangling 链接: ocr-一堂-单元模型-壁垒预判 |
| `frameworks\yt-product-kernel-hypothesis-test.md` | dangling 链接: ocr-泛产品设计-落地卡片-低成本测试mvp |
| `frameworks\yt-product-kernel-iteration.md` | dangling 链接: ocr-泛产品设计-落地卡片-复盘迭代, ocr-顶级产品追求的方向-乔布斯, ocr-一堂产品内核-十大典型指标 |
| `frameworks\yt-product-kernel-six-levels.md` | dangling 链接: ocr-一堂五步法-产品内核画布, ocr-一堂产品内核-十大典型指标 |
| `frameworks\yt-product-kernel-to-business-model.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `frameworks\yt-product-kernel-validation.md` | dangling 链接: ocr-泛产品设计-落地卡片-十倍速验证, ocr-一堂产品内核-十大典型指标 |
| `frameworks\yt-tob-barriers.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\yt-tob-unit-model.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂-单元模型-单履约模型, ocr-一堂-单元模型-对抗小抄01, ocr-一堂-单元模型-外部对抗地图, ocr-一堂-单元模型-单商圈模型 |
| `frameworks\yt-unit-model-overview.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂-单元模型-单履约模型, ocr-一堂-单元模型-对抗小抄01, ocr-一堂-单元模型-外部对抗地图, ocr-一堂-单元模型-单商圈模型 |
| `projects\互联网医院项目.md` | trust_level 值异常: medium# 互联网医院项目 |
| `projects\诊所O2O项目.md` | trust_level 值异常: medium# 诊所o2o项目 |
| `projects\鑫港湾HIS项目.md` | trust_level 值异常: medium# 鑫港湾his项目 |
| `prompt-methodology\prompt-demand-ai-coach.md` | type 值异常: prompt-methodology; confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `skills\feishu-docx-pagination-extraction.md` | dangling 链接: ocr-一堂-科学决策-商业模式-完整财务公式决策 |
| `system\pending_unknown.md` | status 值异常: placeholder; trust_level 值异常: placeholder |
| `systems\一堂方法论体系总图.md` | dangling 链接: ocr-一堂进步大地图, ocr-一堂-个人修炼-课程清单 |
| `tools\sk-ai-old-small-checklist.md` | dangling 链接: ocr-一堂-科学决策-稀缺资源清单, ocr-一堂-科学决策-关键训练清单重要, ocr-一堂-ai清单体笔记系统故事线-truman-图片01, ocr-一堂-案例拆解-课程清单 |
| `tools\tool-ai-skill-engineering-guide.md` | dangling 链接: ocr-一堂-科学决策-roi高阶训练全景图, ocr-一堂-高阶体系探索营-三种咨询可能性 |
| `tools\tool-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, ocr-泛产品设计-用户卡片-场景推演 |
| `tools\tool-candy-oral-polish.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-candy-positioning-canvas.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-canvas-weapon-library-modeling.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂五步法画布, ocr-一堂-ai清单体笔记系统故事线-truman-图片01, ocr-一堂-个人修炼-提问刻意练习画布, ocr-一堂-科学决策-roi决策评估画布 |
| `tools\tool-checklist-cheatsheet-modeling.md` | dangling 链接: ocr-一堂-科学决策-稀缺资源清单, ocr-一堂-科学决策-关键训练清单重要, ocr-一堂-ai清单体笔记系统故事线-truman-图片01, ocr-一堂-案例拆解-课程清单 |
| `tools\tool-demand-agent-auto-verify.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-agent-case-match.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-agent-multi-hypothesis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-agent-signal-substitute.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-assessment-triangle.md` | dangling 链接: ocr-一堂-科学决策-项目方案评估三角形, ocr-一堂-科学决策-决策三角形; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-blindspot-checklist.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-four-forces.md` | dangling 链接: ocr-泛产品设计-审美卡片-最佳实践建模, ocr-泛产品设计-落地卡片-业务建模; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l2-scenario.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-项目背景问题思考的8个维度; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l3-core-job.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l4-job-map.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l5-forces.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l6-hypothesis.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-harness-adversarial-tester.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-iceberg-triangle-modeling.md` | dangling 链接: ocr-一堂深度复盘冰山图 |
| `tools\tool-lean-premium-service.md` | dangling 链接: tool-lean-stealth-service|偷偷服务 |
| `tools\tool-mece体系框架法.md` | dangling 链接: yt-panproduct-execution-logic-mece, ocr-泛产品设计-落地卡片-逻辑mece |
| `tools\tool-openmontage-video-factory.md` | dangling 链接: hongqigong-profile |
| `tools\tool-prompt-iceberg-demand-analysis.md` | dangling 链接: ocr-一堂深度复盘冰山图; trust_level=high 但 source 仅 1 个 |
| `tools\tool-prompt-jtbd-scenario-coach.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-prompt-usp-quick-scan.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-blue-ocean-canvas.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-泛产品设计-审美工具箱指南, ocr-一堂五步法画布, ocr-一堂-个人修炼-提问刻意练习画布 |
| `tools\tool-strategy-business-summary.md` | dangling 链接: ocr-泛产品设计-落地卡片-努力仿真, ocr-泛产品设计-用户卡片-动力阻力, ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-设计原则, ocr-泛产品设计-落地卡片-roi分析 |
| `tools\tool-strategy-capability-matrix.md` | dangling 链接: ocr-一堂-单元模型-象限分析法; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-control-points.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂y模型-科学成事道理, ocr-一堂-单元模型-对抗小抄01, ocr-一堂y模型steps策略集, ocr-一堂-人机协作-双三角模型 |
| `tools\tool-strategy-customer-selection.md` | dangling 链接: ocr-泛产品设计-用户卡片-场景推演 |
| `tools\tool-strategy-industry-chain-analysis.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-泛产品设计-审美工具箱指南, ocr-泛产品设计落地工具篇指南 |
| `tools\tool-strategy-map.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-risk-management.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-泛产品设计-审美工具箱指南 |
| `tools\tool-yitang-ai-assisted-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-assisted-organize.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-monitoring-alert.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-report-drafting.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-amazon-bestseller.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-anonymous-product-testing.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-app-store-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-app-store-review.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-baidu-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-behavioral-observation.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-bidding-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-bp-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-business-registration-check.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-channel-agent-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-comparable-company-selection.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-competitor-financial-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-conference-networking.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-court-record-search.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-database-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-douyin-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-employee-directory.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-executive-speech-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-expert-network-platform.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-financing-intelligence.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-forum-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-government-data-search.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-hardware-product-disassembly.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-in-home-experience-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-industry-report-search.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ipo-annual-report-cheat-sheet.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-news-monitoring.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-online-product-experience.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-partner-data-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-patent-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-pc-web-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-people-network-database.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-public-information-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-public-sentiment-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-recruit-user-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-review-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-securities-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-shareholder-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-signup-statistics.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-social-media-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-social-media-monitoring.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-stock-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-supplier-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-supply-chain-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-trend-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weapon-media-search.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weapon-third-party-database.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-wechat-group-infiltration.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-wechat-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weibo-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-xiaohongshu-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-从案例中学习正反案例法.md` | dangling 链接: ocr-一堂-个人修炼-科学学习ipo模型, ocr-一堂-ai学习-提问工程化, ocr-一堂-ai学习-提问进化路线图 |
| `tools\tool-单元模型-单商圈.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂-单元模型-单履约模型, ocr-一堂-单元模型-对抗小抄01, ocr-一堂-单元模型-规模经济对抗武器库, ocr-一堂-单元模型-段位专家 |
| `tools\tool-单元模型-单城市.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂-单元模型-单履约模型, ocr-一堂-单元模型-对抗小抄01, ocr-一堂-单元模型-规模经济对抗武器库, ocr-一堂-单元模型-段位专家 |
| `tools\tool-单元模型-壁垒预判.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂-单元模型-单履约模型, ocr-一堂-单元模型-对抗小抄01, ocr-一堂-单元模型-单商圈模型, ocr-一堂-单元模型-规模经济对抗武器库 |
| `tools\tool-单元模型-象限分析法.md` | dangling 链接: ocr-一堂-单元模型-单用户模型, ocr-一堂-单元模型-单履约模型, ocr-一堂-单元模型-对抗小抄01, ocr-一堂-单元模型-规模经济对抗武器库, ocr-一堂-单元模型-段位专家 |
| `tools\yt-business-model-canvas.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂五步法画布, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-roi决策评估画布-案例04, ocr-一堂-个人修炼-提问刻意练习画布 |
| `tools\yt-demand-segmentation-canvas.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-泛产品设计-审美工具箱指南, ocr-一堂五步法画布, ocr-一堂-科学决策-roi决策评估画布-案例01 |
| `tools\yt-growth-a-b-testing.md` | dangling 链接: ocr-泛产品设计-落地卡片-低成本测试mvp |
| `tools\yt-growth-channel-roi.md` | dangling 链接: ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-一堂-科学决策-roi高阶训练全景图, ocr-一堂-科学决策-roi决策评估画布-案例01, ocr-一堂-科学决策-roi决策评估画布-案例04, ocr-泛产品设计-落地卡片-roi分析 |
| `tools\yt-product-kernel-canvas.md` | dangling 链接: ocr-泛产品设计-需求工具箱指南, ocr-一堂-科学决策-roi决策评估画布-案例02, ocr-泛产品设计-审美工具箱指南, ocr-一堂五步法画布, ocr-一堂-科学决策-roi决策评估画布-案例01 |
| `tools\yt-product-kernel-mvp-design.md` | dangling 链接: ocr-泛产品设计-落地卡片-攻坚会, ocr-泛产品设计-落地卡片-roi分析, yt-panproduct-execution-low-cost-mvp, ocr-泛产品设计-用户卡片-场景推演 |
| `tools\yt-product-kernel-ten-metrics.md` | dangling 链接: ocr-一堂五步法-产品内核画布, ocr-一堂产品内核-十大典型指标 |
| `tools\yt-tob-customer-sabc.md` | dangling 链接: ocr-一堂-单元模型-单客户模型 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。