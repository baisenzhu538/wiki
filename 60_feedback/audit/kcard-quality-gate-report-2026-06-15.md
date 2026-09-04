# KDO 卡片质量门禁报告

**扫描时间**：2026-06-21  
**扫描范围**：30_wiki 全库 2934 张卡片  
**锚定评分**：2/5 — 草稿
**P0 阻塞问题卡片**：432 张  
**P1 修复问题卡片**：966 张  
**完全干净卡片**：1685 张  
**YAML 解析错误**：3 张  

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
| `agent-specs\agent-spec-zhu-boss.md` | 缺少 trust_level |
| `cases\case-daxin-team-content-training-camp.md` | 缺少 trust_level |
| `cases\case-daxin-vikki-community-contrast.md` | 缺少 trust_level |
| `cases\case-feishu-minutes-extraction-attempt.md` | author 为空 |
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
| `cases\case-toc-online-education-trust-metrics.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-truman-roi-decision-spring-festival-class.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-wechat-5291b61bc722d90d.md` | 缺少 id; author 为空; 缺少 confidence; 缺少 trust_level |
| `cases\case-wechat-6725b942182f6277.md` | 缺少 id; author 为空; 缺少 confidence; 缺少 trust_level |
| `cases\case-wechat-AWyGiJIRgc.md` | 缺少 id; author 为空; 缺少 confidence; 缺少 trust_level |
| `cases\case-wechat-article_4dd7be7cd82f7e80.md` | 缺少 id; author 为空; 缺少 confidence; 缺少 trust_level |
| `cases\case-wechat-dy_7666832665312982138.md` | 缺少 id; author 为空; 缺少 confidence; 缺少 trust_level |
| `cases\case-wechat-f4faadff37c0b43b.md` | 缺少 id; author 为空; 缺少 confidence; 缺少 trust_level |
| `cases\case-wechat-tt_7666646931699367986.md` | 缺少 id; author 为空; 缺少 confidence; 缺少 trust_level |
| `cases\case-yitang-burger-franchise-key-path.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-du-kids-education-sabc.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-false-causality-collection.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-farm-machinery-matching.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-fupanying-five-years-1000-hypotheses.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-homework-six-owners.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-innovative-metrics-collection.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-laowenqi-huixiao-10x.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-magic-number-collection.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-marathon-ten-seasons.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-meituan-red-dot.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-panhonghai-entertainment.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-shao-kaoyan-gmv.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-shipinhao-ads-l1-l6.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-subtraction-decisions-three.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-three-industry-formula-demos.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-tob-devboard-price-coupling.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-vicky-short-video.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-wang-mcn-funnel.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-wechat-monthly-price-value.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-wenxiaozhang-driving-school.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-womenswear-formula-three-versions.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-woqingke-referral-15-to-40.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-xingangwan-chess-room.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-zhanglei-comic-booth.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-yitang-zhanglei-gacha-points.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-一堂自身转化实践.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-优秀案例逐字稿合集.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-优秀触点案例合集.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-优秀转化率复盘合集.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-作业率20到50.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-入职率50到80-100.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-全会员出圈率1.5翻倍.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-六杯奶茶推荐率近100.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-动力篇案例库.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-基本功-认知篇案例集.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-小米发布会拆解.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-我请客推荐率5到40.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-教研加微信率40到100.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-春萍-刘伟tob销售标准化.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-春萍-温校长校园代理.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-春萍-花总AI研发.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-晓莉学而思引流课.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-棋牌室办卡率1到5.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-组合篇案例库.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-视频号加微信率44到85.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-跆拳道黑带卡.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-邹韵涛-中小企业高级管理辅导班专题培训会.md` | status=enriched 但 reviewed_by=pending |
| `cases\case-一堂-阻力篇案例库.md` | status=enriched 但 reviewed_by=pending |
| `concept-card-index-latest.md` | YAML 解析错误: None |
| `concepts\ai单元模型口述蒋老师.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\ai数据理解第一课.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\ai时代判断力口述-3.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\concept-mcp-protocol.md` | source_refs 为空 |
| `concepts\concept-open-source-knowledge-usage-boundary.md` | 缺少 trust_level |
| `concepts\concept-smart-medicine-cabinet-supply-chain-validation.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\concept-strategy-evolution-cycle.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-AI时代基本功变与不变.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-三类目标策略.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-假设飞轮.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-关键路径与乘法杠杆.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-参数即假设与递归嵌套.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-参数耦合与动态公式.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-双目标法.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-基本功-刻意练习四要素.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-基本功-段位体系.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-基本功定义.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-相关不等于因果.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-脱离成本.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-魔法数字.md` | status=enriched 但 reviewed_by=pending |
| `concepts\concept-一堂-黑盒到白盒.md` | status=enriched 但 reviewed_by=pending |
| `concepts\ec工业化规范手册-v2.8.0.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\rust-borrowing-references.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\rust-concurrency-send-sync.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\rust-domain-overview.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\rust-error-handling.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\rust-lifetimes.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\rust-ownership-basics.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\rust-smart-pointers.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\rust-traits-generics.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\smart-medicine-cabinet-distribution.md` | 缺少 confidence |
| `concepts\supply-chain-beverage.md` | source_refs 为空 |
| `concepts\web-scraping-三剑客-scrapling-crawl4ai-firecrawl.md` | source_refs 为空 |
| `concepts\yt-ai-startup-20-risky-hypotheses.md` | author 为空; 缺少 trust_level |
| `concepts\yt-ai-trend-12-signals.md` | author 为空; 缺少 trust_level |
| `concepts\yt-barrier-analysis-cheat-sheet.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\yt-business-formula-parameter-iceberg.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-business-formula-six-level-logic.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-business-formula-ten-paradigms.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-customer-acquisition-toolkit.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\yt-demand-analysis-hiking-map.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\yt-entrepreneur-259-milestone.md` | author 为空; status=enriched 但 reviewed_by=pending; 缺少 trust_level |
| `concepts\yt-entrepreneur-barriers.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-business-growth.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-channel-exploration.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-concentration-analysis.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-fundraising.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-industrial-production.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-industry-forecast.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-opportunity-selection.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-pragmatic-startup.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-product-core.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-research-camp.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-scientific-method.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-spin-selling.md` | author 为空; 缺少 trust_level |
| `concepts\yt-entrepreneur-truth-seeking.md` | author 为空; 缺少 trust_level |
| `concepts\yt-foresight-model-taxonomy.md` | author 为空; 缺少 trust_level |
| `concepts\yt-growth-cycle-model.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\yt-model-deep-review-iceberg.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-deliberate-practice-growth.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-ipo-complete-checklist.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-liberate-thinking-layers.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-management-map.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-muse-ai-framework.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-prediction-model.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-product-core-metrics.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-product-excellence.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-questioning-practice-canvas.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-scientific-questioning-map.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-truman-career-routes.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-truman-five-step-growth.md` | author 为空; 缺少 trust_level |
| `concepts\yt-model-y-organization.md` | author 为空; 缺少 trust_level |
| `concepts\yt-note-deliberate-practice-four-elements.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-personal-checklist-notes.md` | author 为空; 缺少 trust_level |
| `concepts\yt-personal-deliberate-practice.md` | author 为空; 缺少 trust_level |
| `concepts\yt-personal-inspiration-flash.md` | author 为空; 缺少 trust_level |
| `concepts\yt-personal-knowledge-management.md` | 缺少 trust_level |
| `concepts\yt-personal-product-design.md` | author 为空; 缺少 trust_level |
| `concepts\yt-personal-thinking-models.md` | author 为空; 缺少 trust_level |
| `concepts\yt-personal-verbatim-script.md` | author 为空; 缺少 trust_level |
| `concepts\yt-personal-y-model-practice.md` | author 为空; 缺少 trust_level |
| `concepts\yt-product-kernel-cultivation.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\yt-scale-economy-weapon-library.md` | author 为空; 缺少 trust_level |
| `concepts\yt-skill-storyline-contrast-analysis.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-skill-storyline-key-elements.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-skill-storyline-problem-solving.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-skill-storyline-target-tradeoff.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-skill-storyline-timeline.md` | status=enriched 但 reviewed_by=pending |
| `concepts\yt-unit-model-three-tools.md` | author 为空; status=enriched 但 reviewed_by=pending; 缺少 confidence; 缺少 trust_level |
| `concepts\人机协作决策-双三角模型.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\诊所o2o外卖平台业务深度调研报告.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `concepts\鑫港湾his系统分阶段整改报告.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `cross-domain-patterns\README.md` | id (cross-domain-patterns-index) 与文件名 (README) 不一致; 缺少 confidence; 缺少 trust_level |
| `dark-knowledges\dk-ai-design-pitfalls.md` | source_refs 为空; author 为空; 缺少 confidence |
| `dark-knowledges\dk-digest-registration-gap.md` | YAML 解析错误: while parsing a block mapping
  in "<unicode string>", line 33, column 3:
    - signal: 卡文件存在（ls 能看见）但 grep 不到任何 ... 
      ^
expected <block end>, but found '<scalar>'
  in "<unicode string>", line 35, column 20:
      implication: "存在"不等于"注册"——2026-08-23 周检实测 12 张核心卡 ... 
                       ^ |
| `dark-knowledges\dk-mcp-pythonpath-pollution.md` | author 为空 |
| `dark-knowledges\dk-modeling-ai-without-judgment.md` | source_refs 为空 |
| `dark-knowledges\dk-modeling-business-visual-logic-match.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `dark-knowledges\dk-modeling-counterexample-driven.md` | source_refs 为空 |
| `dark-knowledges\dk-modeling-essence-predictive.md` | source_refs 为空 |
| `dark-knowledges\dk-modeling-model-arsenal-paradigms.md` | source_refs 为空 |
| `dark-knowledges\dk-modeling-radar-model-not-result.md` | source_refs 为空 |
| `dark-knowledges\dk-modeling-unit-pairs-milestone.md` | source_refs 为空 |
| `dark-knowledges\dk-wanghuan-paced-sales-decision.md` | source_refs 为空 |
| `dark-knowledges\dk-wanghuan-spec-trap.md` | source_refs 为空 |
| `dark-knowledges\dk-yb1-aigc-mvp-before-ps.md` | source_refs 为空 |
| `dark-knowledges\dk-yb5-style-asset-archive.md` | source_refs 为空 |
| `dark-knowledges\dk-yb9-cubox-deployment-failure.md` | source_refs 为空 |
| `dark-knowledges\dk-yitang-Y-model-pitfalls.md` | source_refs 为空 |
| `dark-knowledges\dk-yitang-business-formula-a-missing-syndrome.md` | status=enriched 但 reviewed_by=pending |
| `dark-knowledges\dk-yitang-business-formula-cd-loop-undo-key.md` | status=enriched 但 reviewed_by=pending |
| `dark-knowledges\dk-yitang-business-formula-l1-site-blindness.md` | status=enriched 但 reviewed_by=pending |
| `dark-knowledges\dk-yitang-business-formula-logic-l5-l6.md` | status=enriched 但 reviewed_by=pending |
| `dark-knowledges\dk-yitang-business-formula-pseudo-causality-two-masks.md` | status=enriched 但 reviewed_by=pending |
| `dark-knowledges\dk-yitang-sales-common-pitfalls.md` | source_refs 为空; author 为空; 缺少 confidence |
| `dark-knowledges\yt-note-ai-p-role-not-c-role.md` | author 为空 |
| `dark-knowledges\yt-note-p-c-role-boundary-realworld.md` | author 为空 |
| `dark-knowledges\yt-note-three-level-evolution.md` | author 为空 |
| `decisions\kdo-protocol-implementation-roadmap.md` | 缺少 confidence |
| `decisions\modeling-capability-for-kdo.md` | source_refs 为空 |
| `decisions\plan_20260621_skill-iteration-standard.md` | 缺少 trust_level |
| `decisions\plan_20260701_kdo-multi-repo-architecture.md` | 缺少 confidence; 缺少 trust_level |
| `domains\ai-collaboration-domain-digest.md` | status=enriched 但 reviewed_by=pending |
| `domains\business-formula-domain-digest.md` | status=enriched 但 reviewed_by=pending |
| `domains\conversion-rate-domain-digest.md` | status=enriched 但 reviewed_by=pending |
| `domains\decision-science-domain-digest.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `domains\lean-startup-domain-digest.md` | status=enriched 但 reviewed_by=pending |
| `domains\management-domain-digest.md` | source_refs 为空; status=enriched 但 reviewed_by=pending |
| `domains\yitang-domain-digest.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\concept-minto-pyramid-principle.md` | source_refs 为空 |
| `frameworks\framework-ai-deconstruction-methodology.md` | source_refs 为空 |
| `frameworks\framework-ai-native-organization-two-modes.md` | source_refs 为空 |
| `frameworks\framework-ai2041-critical-reading-os.md` | source_refs 为空 |
| `frameworks\framework-brand-three-degree.md` | source_refs 为空; 缺少 trust_level |
| `frameworks\framework-business-formula-dual-triangle-bridge.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\framework-business-formula-fundamentals-bridge.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\framework-business-formula-y-model-bridge.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\framework-ci-operating-model.md` | author 为空 |
| `frameworks\framework-community-knowledge-production-failure-modes.md` | source_refs 为空; 缺少 trust_level |
| `frameworks\framework-content-business-six-step.md` | source_refs 为空; 缺少 trust_level |
| `frameworks\framework-course-milestone-model.md` | source_refs 为空 |
| `frameworks\framework-decision-cognitive-bias-map.md` | source_refs 为空 |
| `frameworks\framework-decision-quality-checklist.md` | source_refs 为空 |
| `frameworks\framework-deep-work-iceberg.md` | source_refs 为空 |
| `frameworks\framework-demand-ceiling-four-lines.md` | source_refs 为空 |
| `frameworks\framework-demand-iceberg.md` | source_refs 为空 |
| `frameworks\framework-demand-lean-bridge.md` | source_refs 为空 |
| `frameworks\framework-five-step-lean-interface.md` | source_refs 为空 |
| `frameworks\framework-founder-ip-three-positioning.md` | source_refs 为空; 缺少 trust_level |
| `frameworks\framework-lean-abcd-model.md` | source_refs 为空 |
| `frameworks\framework-lean-false-model.md` | source_refs 为空 |
| `frameworks\framework-lean-pivot-decision.md` | source_refs 为空 |
| `frameworks\framework-lean-systematic-test-curve.md` | source_refs 为空 |
| `frameworks\framework-lean-tenx-formula.md` | source_refs 为空 |
| `frameworks\framework-logic-cleanliness-five-levels.md` | source_refs 为空 |
| `frameworks\framework-multi-agent-research-architecture.md` | author 为空 |
| `frameworks\framework-ouyangfeng-review-methodology.md` | source_refs 为空 |
| `frameworks\framework-pan-product-organization.md` | source_refs 为空 |
| `frameworks\framework-strategy-ansoff.md` | source_refs 为空 |
| `frameworks\framework-strategy-basics-01-core.md` | source_refs 为空 |
| `frameworks\framework-strategy-basics-02-insight.md` | source_refs 为空 |
| `frameworks\framework-strategy-basics-03-layout.md` | source_refs 为空 |
| `frameworks\framework-strategy-basics-05-change.md` | source_refs 为空 |
| `frameworks\framework-strategy-blm.md` | source_refs 为空 |
| `frameworks\framework-strategy-business-design.md` | source_refs 为空 |
| `frameworks\framework-strategy-five-basics.md` | source_refs 为空 |
| `frameworks\framework-strategy-five-forces.md` | source_refs 为空 |
| `frameworks\framework-strategy-kai-innovation-directions.md` | source_refs 为空 |
| `frameworks\framework-strategy-lean-validation.md` | source_refs 为空 |
| `frameworks\framework-strategy-mckinsey-7s.md` | source_refs 为空 |
| `frameworks\framework-strategy-pyramid.md` | source_refs 为空 |
| `frameworks\framework-strategy-six-stages.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\framework-strategy-three-horizons.md` | source_refs 为空 |
| `frameworks\framework-structured-analytic-techniques.md` | author 为空 |
| `frameworks\framework-taste-as-judgment-system.md` | source_refs 为空 |
| `frameworks\framework-time-management-dual-loop-matrix.md` | source_refs 为空 |
| `frameworks\framework-time-management-matrix.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-actor-director-mode.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-ai-five-level-ladder.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-bitcoe-prompt-framework.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-five-criteria-first-product.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-gan-three-roles.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-harness-seven-stages.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-ooda-loop.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-say-think-do-toolchain.md` | source_refs 为空 |
| `frameworks\framework-wanghuan-task-product-system.md` | source_refs 为空 |
| `frameworks\framework-yihang-AI-native-dual-triangle-kernel.md` | source_refs 为空 |
| `frameworks\framework-yihang-knowledge-data-decoupling.md` | source_refs 为空 |
| `frameworks\framework-yitang-channel-exploration-4step.md` | source_refs 为空 |
| `frameworks\framework-yitang-channel-industrialization.md` | source_refs 为空 |
| `frameworks\framework-yitang-channel-partnership-map.md` | source_refs 为空 |
| `frameworks\framework-yitang-channel-unit-economics.md` | source_refs 为空 |
| `frameworks\framework-yitang-five-step-to-time-management.md` | source_refs 为空 |
| `frameworks\framework-yitang-growth-flywheel.md` | source_refs 为空 |
| `frameworks\framework-yitang-jiefang-sixiang.md` | source_refs 为空 |
| `frameworks\framework-yitang-shishi-qiushi.md` | source_refs 为空 |
| `frameworks\framework-一堂-基本功-九层金字塔.md` | source_refs 为空; status=enriched 但 reviewed_by=pending |
| `frameworks\framework-一堂-基本功-四字诀拆建推练.md` | source_refs 为空; status=enriched 但 reviewed_by=pending |
| `frameworks\framework-一堂-基本功-四类工作四化.md` | source_refs 为空; status=enriched 但 reviewed_by=pending |
| `frameworks\framework-一堂-苦练基本功-总纲.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\framework-一堂五步法-增长周期.md` | source_refs 为空 |
| `frameworks\framework-一堂五步法-壁垒.md` | source_refs 为空 |
| `frameworks\framework-一堂五步法-泛产品设计.md` | source_refs 为空 |
| `frameworks\framework-一堂五步法.md` | source_refs 为空 |
| `frameworks\framework-个人成长五步法.md` | source_refs 为空 |
| `frameworks\framework-单元模型-外部对抗地图.md` | source_refs 为空 |
| `frameworks\yt-business-formula-abc-model.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\yt-business-formula-hypothesis-management-playbook.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\yt-business-formula-peahd-roles.md` | status=enriched 但 reviewed_by=pending |
| `frameworks\yt-business-formula-three-stage-workflow.md` | status=enriched 但 reviewed_by=pending |
| `index.md` | source_refs 为空; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `links\index.md` | source_refs 为空; author 为空; 缺少 confidence; 缺少 trust_level; 缺少 domain |
| `operations\runbook-agent-spec-to-runtime.md` | 缺少 confidence; 缺少 trust_level |
| `personal-os\README.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `personal-os\opc-ai-sales-agent-architecture.md` | 缺少 confidence; 缺少 trust_level |
| `personal-os\wangyuyan-working-protocols.md` | source_refs 为空; author 为空; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-codebase-ai-orchestration.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-domain-index.md` | source_refs 为空; author 为空; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-feedback-patterns.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-future-directions.md` | source_refs 为空; author 为空; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-lessons-learned.md` | author 为空; status=enriched 但 reviewed_by=pending; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-network-resources.md` | source_refs 为空; author 为空; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-project-board.md` | source_refs 为空; author 为空; status=enriched 但 reviewed_by=pending; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-strategic-conclusions.md` | author 为空; status=enriched 但 reviewed_by=pending; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-time-os.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `personal-os\zhu-weekly-reflections.md` | source_refs 为空; author 为空; 缺少 confidence; 缺少 trust_level |
| `projects\互联网医院项目.md` | status=enriched 但 reviewed_by=pending |
| `projects\广冷电子_HX-SMJ_红外光栅故障分析报告.md` | YAML 解析错误: None |
| `projects\诊所O2O项目.md` | status=enriched 但 reviewed_by=pending |
| `projects\鑫港湾HIS项目.md` | status=enriched 但 reviewed_by=pending |
| `systems\obsidian-git-sync-protocol.md` | 缺少 confidence |
| `systems\system-kdo-quality-labels.md` | status=enriched 但 reviewed_by=pending; 缺少 trust_level |
| `systems\workflow-knowledge-collision.md` | status=enriched 但 reviewed_by=pending |
| `tools\agent-spec-coaching-leadership-assistant.md` | id (spec-coaching-leadership-assistant) 与文件名 (agent-spec-coaching-leadership-assistant) 不一致; 缺少 domain |
| `tools\agent-spec-meeting-assistant.md` | id (spec-meeting-assistant) 与文件名 (agent-spec-meeting-assistant) 不一致; 缺少 domain |
| `tools\tool-agent-crawl4ai.md` | source_refs 为空 |
| `tools\tool-agent-firecrawl.md` | source_refs 为空 |
| `tools\tool-agent-research-pipeline.md` | author 为空 |
| `tools\tool-agent-research-supervisor.md` | author 为空 |
| `tools\tool-agent-research-swarm.md` | author 为空 |
| `tools\tool-agent-spec-business-formula-parameter-miner.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-ci-define-phase.md` | author 为空 |
| `tools\tool-ci-implement-phase.md` | author 为空 |
| `tools\tool-demand-agent-auto-verify.md` | source_refs 为空 |
| `tools\tool-demand-agent-multi-hypothesis.md` | source_refs 为空 |
| `tools\tool-demand-agent-signal-substitute.md` | source_refs 为空 |
| `tools\tool-demand-agent-signals.md` | source_refs 为空 |
| `tools\tool-devils-advocacy.md` | author 为空 |
| `tools\tool-geo-ai-search-visibility-playbook.md` | status=enriched 但 reviewed_by=pending |
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
| `tools\tool-shortvideo-six-dimension-deconstruction.md` | 缺少 trust_level |
| `tools\tool-strategy-12-word-test.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-activity-scope.md` | source_refs 为空 |
| `tools\tool-strategy-competition-traps.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-control-points.md` | source_refs 为空 |
| `tools\tool-strategy-four-layers.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-four-moves.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-gap-analysis.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-logistics-cost-planning.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-market-opportunity-matrix.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-nine-problems.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-pareto.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-risk-management.md` | source_refs 为空 |
| `tools\tool-strategy-sentence-formula.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-three-horizons.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-value-capture.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-strategy-value-proposition.md` | source_refs 为空 |
| `tools\tool-yitang-ai-assisted-analysis.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-ai-assisted-organize.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-ai-monitoring-alert.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-ai-report-drafting.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-amazon-bestseller.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-anonymous-product-testing.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-anonymous-roundtable.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-app-store-data.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-app-store-review.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-baidu-index.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-behavioral-observation.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-bidding-analysis.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-bp-analysis.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-business-formula-l5-mining-and-verification.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-business-registration-check.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-channel-agent-interview.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-channel-partnership-design.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-yitang-practice-20hour-starter.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `tools\tool-yitang-project-weapon-library-v1-8.md` | source_refs 为空 |
| `tools\tool-yitang-research-normalize-summary.md` | source_refs 为空 |
| `tools\tool-一堂-business-prediction-15-char.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `tools\tool-一堂-five-step-validation.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `tools\tool-一堂-基本功-三环六维自检.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-一堂-基本功-建模七法.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-一堂-基本功-拆解四法.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-一堂-基本功-推动七式.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-一堂-基本功-练习二十法.md` | status=enriched 但 reviewed_by=pending |
| `tools\tool-使用一页纸速查卡快速调用框架.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `tools\tool-场景推演.md` | source_refs 为空 |
| `tools\tool-审美工具箱.md` | source_refs 为空 |
| `tools\tool-泛产品落地-内核和边界.md` | source_refs 为空 |
| `tools\tool-泛产品落地-善用佳软.md` | source_refs 为空 |
| `tools\tool-泛产品落地-灵感闪现.md` | source_refs 为空 |
| `tools\tool-用户分层.md` | source_refs 为空 |
| `tools\tool-用户视角.md` | source_refs 为空 |
| `tools\tool-纪浩-AI对话上下文隔离.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `tools\tool-行业分析画布.md` | source_refs 为空 |
| `tools\tool-需求挖掘.md` | source_refs 为空 |
| `tools\tool-项目背景分析.md` | source_refs 为空 |
| `tools\tool-马易-业务为先的AI中台建设.md` | author 为空; 缺少 confidence; 缺少 trust_level |
| `tools\yt-pitch-metaphor.md` | source_refs 为空 |
| `tools\yt-pitch-quantification.md` | source_refs 为空 |
| `tools\yt-pitch-storytelling.md` | source_refs 为空 |
| `tools\yt-tool-business-formula-18-moves.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-business-formula-causality-toolkit.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-business-formula-expert-interview-10.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-business-formula-format-spec.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-business-formula-gongjianhui.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-business-formula-hypothesis-pool.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-business-formula-inspiration-5.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-business-formula-metrics-checklist.md` | source_refs 为空; author 为空; status=enriched 但 reviewed_by=pending; 缺少 confidence; 缺少 trust_level |
| `tools\yt-tool-business-formula-parameter-arsenal.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-business-formula-quant-space-3d.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-equity-checklist.md` | source_refs 为空 |
| `tools\yt-tool-onboarding-90day.md` | source_refs 为空 |
| `tools\yt-tool-project-health-radar.md` | source_refs 为空 |
| `tools\yt-tool-strategy-workshop.md` | source_refs 为空 |
| `tools\yt-tool-unit-model-ai-assisted.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-unit-model-benchmark.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-unit-model-construction.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-unit-model-dynamic.md` | status=enriched 但 reviewed_by=pending |
| `tools\yt-tool-unit-model-selection.md` | status=enriched 但 reviewed_by=pending |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `agent-specs\agent-spec-duanwangye-publisher.md` | type 值异常: agent-spec; dangling 链接: content-production-polish; status=draft 但 confidence=0.9 |
| `agent-specs\agent-spec-fengqingyang-observer.md` | type 值异常: agent-spec |
| `agent-specs\agent-spec-hongqigong-multimodal.md` | type 值异常: agent-spec; dangling 链接: content-production-polish; status=draft 但 confidence=0.9 |
| `agent-specs\agent-spec-huangyaoshi-builder.md` | type 值异常: agent-spec |
| `agent-specs\agent-spec-laowantong-producer.md` | type 值异常: agent-spec; status=draft 但 confidence=0.9 |
| `agent-specs\agent-spec-ouyangfeng-reviewer.md` | type 值异常: agent-spec |
| `agent-specs\agent-spec-skills-assistant.md` | type 值异常: agent-spec |
| `agent-specs\agent-spec-wangyuyan-orchestrator.md` | type 值异常: agent-spec |
| `agent-specs\agent-spec-zhu-ai-coach.md` | type 值异常: agent-spec; dangling 链接: user-insight-profile; status=draft 但 confidence=0.85 |
| `agent-specs\agent-spec-zhu-boss.md` | type 值异常: agent-spec |
| `bridges\bridge-christensen-reverse-mapping.md` | type 值异常: bridge; dangling 链接: yt-panproduct-execution-roi-analysis, yt-panproduct-execution-low-cost-mvp |
| `bridges\bridge-coaching-leadership-feature-layered.md` | type 值异常: bridge |
| `bridges\bridge-dual-track-feature-system.md` | type 值异常: bridge; trust_level=high 但 source 仅 1 个 |
| `bridges\bridge-how-to-know-person-to-business.md` | type 值异常: bridge; dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `bridges\bridge-lightning-agent-evolution.md` | type 值异常: bridge |
| `bridges\bridge-meeting-leadership-coaching.md` | type 值异常: bridge |
| `bridges\bridge-panproduct-kids-translation.md` | type 值异常: bridge |
| `bridges\bridge-two-feature-systems.md` | type 值异常: bridge |
| `bridges\bridge-yitang-seek-truth-liberate-thought.md` | type 值异常: bridge; status=draft 但 confidence=0.9 |
| `bridges\bridge-个人复盘×知识管理W-Z-K-P.md` | type 值异常: bridge; trust_level=high 但 source 仅 1 个 |
| `cases\case-20260829-zhanlue-dingding-l3-extraction.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9 |
| `cases\case-252-quality-gate-pilot.md` | status=draft 但 confidence=0.9 |
| `cases\case-ai-agent-milestone-design.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-ai-search-commerce-platform-hedge.md` | dangling 链接: AI 搜索与电商平台, 平台履约能力护城河, 购物即娱乐案例 |
| `cases\case-aodaye-archery-reinvention.md` | status=draft 但 confidence=0.85 |
| `cases\case-candy-problem-os-vpn.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-coaching-dialogue-three-versions.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-decision-ai-assisted-vs-human.md` | dangling 链接: framework-decision-cognitive-bias-map|认知偏差地图, concept-AI时代双三角竞争力|AI 时代双三角竞争力, dk-decision-when-to-defer|何时应该推迟决策, framework-decision-quality-checklist|决策质量六问检查表 |
| `cases\case-demand-b2b-enterprise-erp.md` | dangling 链接: yt-tob-demand-metrics|To B 需求测算双指标, framework-demand-validation-pipeline|需求验证流水线, framework-demand-iceberg|需求洞察冰山模型, yt-demand-decision-chain|ToB决策链需求分析 |
| `cases\case-demand-b2c-consumer-insight.md` | dangling 链接: yt-demand-motivation-resistance|需求动机与阻力分析, dk-demand-signal-vs-noise|需求信号与噪音的区分, case-demand-milkshake-jtbd|JTBD 方法, yt-demand-peak-end-rule|峰终定律, framework-demand-usp-model|USP 模型 |
| `cases\case-demand-financial-literacy.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-milkshake-jtbd.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-pharma-bigdata.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-restaurant-hiring.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-rural-5g.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-demand-silver-parenting.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-beauty-ecommerce-channel.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-catering-chain-benchmark.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-crossborder-ecommerce-opportunity.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-grab-industry-cognition.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-doris-outbound-travel-community.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-feishu-live259-l3-extraction.md` | confidence=0.95 但 source 仅 1 个 |
| `cases\case-feishu-minutes-extraction-attempt.md` | status=draft 但 confidence=0.85 |
| `cases\case-five-step-fake-vs-real-barriers.md` | dangling 链接: 假的壁垒, 一堂五步法 |
| `cases\case-five-step-growth-first-lever.md` | dangling 链接: 一堂五步法 |
| `cases\case-friend-circle-aigc-transformation.md` | status 值异常: pending_review |
| `cases\case-fuzeyu-ai-koubo-tool-dev.md` | status=draft 但 confidence=0.85 |
| `cases\case-investment-claim-fact-check.md` | status 值异常: pending_review |
| `cases\case-kinda-digital-employees-fullview.md` | confidence=0.9 但 source 仅 1 个 |
| `cases\case-laozhu-hongqigong-human-ai-partner-evolution.md` | dangling 链接: administrator, Copilot到Partner, desktop, 人机协作跃迁, 老朱洪七公诊断 |
| `cases\case-lean-building-in-vacuum.md` | dangling 链接: framework-lean-false-model|FALSE 模型, framework-lean-six-wastes|六宗罪 |
| `cases\case-liutao-douyin-team-leader-9m.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-liutao-electric-bike-localization.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-meeting-roi-awakening.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-modeling-abstraction-reliability-ladder.md` | dangling 链接: 高阶建模, 建模能力培训, 抽象建模 |
| `cases\case-modeling-ai-image-workflow.md` | status=draft 但 confidence=0.85 |
| `cases\case-modeling-essence-levels.md` | dangling 链接: 高阶建模, 本质建模, 建模能力培训 |
| `cases\case-modeling-gongjianhui-facilitation.md` | status=draft 但 confidence=0.85 |
| `cases\case-modeling-process-sop-examples.md` | dangling 链接: 高阶建模, 建模能力培训, 流程建模 |
| `cases\case-morfei-semiconductor.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-neworiental-prospectus-marketing.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-popmart-prospectus-pricing.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-proya-betaine-skincare-benchmark.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-qinpeng-hardware-ai-amplification.md` | dangling 链接: yt-panproduct-execution-low-cost-mvp |
| `cases\case-shuishui-business-insight.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-failure-04-appliance.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-failure-09-boeing.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-longzhong-plan.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-11-third-place.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-12-zero-loss.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-practice-ranpeng-milk-powder.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-revival-14-gucci.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-shell-oil.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-strategy-wuxi-suntech.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-truman-ai-image-workflow-evolution.md` | dangling 链接: 10_raw/sources/feature-periodic-table-v0.8.json; confidence=0.92 但 source 仅 1 个; status=draft 但 confidence=0.92; trust_level=high 但 source 仅 1 个 |
| `cases\case-truman-ai-native-research-flow.md` | status 值异常: pending_review |
| `cases\case-truman-investment-daily-report.md` | dangling 链接: 10_raw/sources/feature-periodic-table-v0.8.json; confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `cases\case-truman-roi-decision-spring-festival-class.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-truman-sales-report-structure.md` | dangling 链接: 建模能力培训 |
| `cases\case-truman-temperature-parameter.md` | dangling 链接: 10_raw/sources/feature-periodic-table-v0.8.json; confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `cases\case-wangfei-newyear-event-diagnosis.md` | dangling 链接: five-step-domain-digest|五步法, framework-yitang-shishi-qiushi|实事求是, dk-sponsor-three-tier-pricing|赞助商三层定价法, tool-private-board-facilitation-sop|私董会七步法; status=draft 但 confidence=0.85 |
| `cases\case-wenxiaobao-campus-bilateral-network.md` | status=draft 但 confidence=0.85 |
| `cases\case-wudi-innovation-contest-value.md` | status=draft 但 confidence=0.85 |
| `cases\case-yihang-dual-triangle-AI三角-场景.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-AI三角-基本功.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-AI三角-数据.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-AI可以落地的场景假设.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-AI场景.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-AI基本功.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-AI数据.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-D-engineer-upward-communication.md` | dangling 链接: D同学案例, 红蓝军沟通法, 人机协作双三角, 同学的案例口述 |
| `cases\case-yihang-dual-triangle-ahao-product-selection.md` | dangling 链接: 阿豪案例, 阿豪案例的口述, 人机协作双三角, 电商选品案例 |
| `cases\case-yihang-dual-triangle-beike-ai-outbound.md` | dangling 链接: AI外呼案例, 组织贝壳找房案例口述, 人机协作双三角, 贝壳找房案例 |
| `cases\case-yihang-dual-triangle-chentian-knowledge-agent.md` | dangling 链接: 陈天同学案例口述, 陈天案例, 知识管理案例, 人机协作双三角 |
| `cases\case-yihang-dual-triangle-hardware-patent-rule-explicit.md` | dangling 链接: 专利落地案例, 硬件公司专利案例, 规则显性化案例, 人机协作双三角 |
| `cases\case-yihang-dual-triangle-hotel-tag-sandbox.md` | dangling 链接: 标签审核案例, 边缘切入案例, 沙盒练兵案例, 人机协作双三角, 酒店标签案例 |
| `cases\case-yihang-dual-triangle-huazao-synthetic-data.md` | dangling 链接: 花总案例, 一堂双三角, 合成数据案例, 人机协作双三角 |
| `cases\case-yihang-dual-triangle-tianmo-design-delivery.md` | dangling 链接: 天末案例, 人机协作双三角, 设计交付案例, 天末的双三角模型 |
| `cases\case-yihang-dual-triangle-truman-feishu-to-slide-ppt-evolution.md` | dangling 链接: PPT 迭代案例, Truman 飞书 To slide, annotations |
| `cases\case-yihang-dual-triangle-一堂DOC-20260704025752.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-AI企业经营数据分析.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-AI时代的竞争力武器库.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-AI落地五部曲.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-一个引擎-三阶六变.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-人生红点教练parther探索.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-作业洞察和特别表白.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-十年爬山地图.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-双三角预判画布.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-清单版画布.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-画布案例1.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-画布案例2.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-一堂双三角-解释版画布.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-人创造力.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-人审美.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-人类三角-创造力.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-人类三角-审美.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-人类三角-练体系.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-人练体系.md` | source_refs 为空 |
| `cases\case-yihang-dual-triangle-双三角-竞争力武器库.md` | source_refs 为空 |
| `cases\case-yitang-2022-annual-lessons.md` | dangling 链接: yt-management-project-management|科学项目管理（概念）, framework-yitang-project-breakdown|项目拆解框架, framework-yitang-project-execution|项目执行框架, workflow-yitang-project-four-step-loop|项目四步闭环工作流, framework-yitang-project-retrospective|复盘十六字原则 |
| `cases\case-yitang-4-leaps-innovation-evolution.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-ai-time-management-coach.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-beauty-device-overseas-sales.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-competitor-pricing-intelligence.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-consumer-offline-channel-decision.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-copywriting-time-decomposition.md` | dangling 链接: concept-time-block-energy-fit, tool-time-audit-matrix |
| `cases\case-yitang-doorstep-nail-service-context.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-eason-truth-delivery-audit.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-elderly-home-roleplay.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-fake-interview-intelligence.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-hardware-factory-photo.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-jiangxiang-huawei-matext-launch.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-jiangxiang-tianmu-balcony.md` | confidence=0.92 但 source 仅 1 个 |
| `cases\case-yitang-jtbd-story-formula.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-leadership-culture.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-leo-website-redesign.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-lianjia-site-selection-industrialization.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-luckin-field-research.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-mahjong-machine-fake-order.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-model-asset-inventory.md` | dangling 链接: 建模能力培训 |
| `cases\case-yitang-model-valuation-flywheel.md` | dangling 链接: 建模能力培训 |
| `cases\case-yitang-pet-fostering-user-research.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-sales-transformation-jubensha-saas.md` | dangling 链接: tool-yitang-sales-toolkit-radar|销售武器库六维雷达图, tool-yitang-sales-performance-management|业绩管理三步法, tool-yitang-sales-process-decomposition|销售过程拆解三步法, tool-yitang-customer-segmentation-4step|用户分层四步法, framework-yitang-scientific-sales-five-step|科学销售五步法 |
| `cases\case-yitang-sales-transformation-meirongyuan.md` | dangling 链接: framework-yitang-nine-layer-deep-dig|九层深挖, framework-yitang-channel-exploration-4step|渠道探索四步法, tool-yitang-sales-toolkit-radar|销售武器库六维雷达图, tool-yitang-sales-performance-management|业绩管理三步法, tool-yitang-sales-process-decomposition|销售过程拆解三步法 |
| `cases\case-yitang-sales-transformation-tuliaogongsi.md` | dangling 链接: master-decision-hygiene|决策卫生, framework-yitang-nine-layer-deep-dig|九层深挖, dk-yitang-sales-common-pitfalls|销售常见陷阱, tool-yitang-sales-performance-management|业绩管理三步法, tool-yitang-customer-segmentation-4step|用户分层四步法 |
| `cases\case-yitang-sanjieke-benchmark-failure.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-shishi-qiushi-pitfall-1-subjective-speculation.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-shishi-qiushi-pitfall-10-over-abstraction.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-shishi-qiushi-pitfall-2-ignore-facts.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-shishi-qiushi-pitfall-3-overgeneralization.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-shishi-qiushi-pitfall-4-no-quantification.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-shishi-qiushi-pitfall-5-over-prediction.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-shishi-qiushi-pitfall-6-deny-patterns.md` | status=draft 但 confidence=0.85 |
| `cases\case-yitang-shishi-qiushi-pitfall-7-underestimate-patterns.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-shishi-qiushi-pitfall-8-wrong-analogy.md` | status=draft 但 confidence=0.88 |
| `cases\case-yitang-shishi-qiushi-pitfall-9-methodology-superstition.md` | status=draft 但 confidence=0.85 |
| `cases\case-yitang-ski-project-user-as-expert.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-supplier-security-guard.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-track-selection-research.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-travel-receipt-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-weekly-modeling-engine.md` | dangling 链接: 建模能力培训 |
| `cases\case-yitang-yai-conversion-rate-visit-rate.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-yai-scientific-decision-life-direction.md` | dangling 链接: agent-一堂-科学决策教练; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-ymodel-ai-business-dialogue.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-ymodel-b2b-sales-conversion.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-ymodel-children-reading-retention.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-ymodel-vicki-cross-domain-transfer.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `cases\case-yitang-ymodel-watermelon-challenge.md` | status=draft 但 confidence=0.88; trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglan-amusement-park-undercover.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglei-furniture-overseas-market-selection.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhanglei-nursing-home-family.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-zhu-disruptive-innovation-practice.md` | dangling 链接: user-insight-profile; status=draft 但 confidence=0.85 |
| `cases\case-zhu-foresight-timing-pattern.md` | dangling 链接: framework-yitang-thought-liberation-lightning|闪电模型, user-insight-profile, framework-christensen-disruptive-innovation|Christensen框架 |
| `cases\case-一堂-A加社失败归因→一堂诞生.md` | confidence=0.95 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-一堂-教材品控事故.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-一堂-春萍-刘伟tob销售标准化.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-一堂-春萍-温校长校园代理.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-一堂-春萍-花总AI研发.md` | trust_level=high 但 source 仅 1 个 |
| `cases\case-一堂-迷你访谈五周迭代.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `cases\case-利润-巨米OPC利润前置对照.md` | status=draft 但 confidence=0.85 |
| `cases\case-利润-白牌珠宝流量上瘾症.md` | status=draft 但 confidence=0.85 |
| `cases\case-利润-苹果智能手机利润垄断.md` | status=draft 但 confidence=0.88 |
| `cases\case-利润-通用汽车份额追逐失败.md` | status=draft 但 confidence=0.85 |
| `cases\case-千惠供应链复盘.md` | status=draft 但 confidence=0.95 |
| `cases\case-莹莹-before-after复盘.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\2026-05-17-深夜感想.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\ai-hackathon-pitches.md` | dangling 链接: 价值投资大师项目, 一堂武智院, 内容营销路演 |
| `concepts\ai-native-im-multi-agent.md` | source_refs 中的 src ID 未注册: src_20260614_c5115d2c |
| `concepts\ai-tool-learning-curve.md` | dangling 链接: AI工具学习五阶段, Truman 学习曲线, 角色给我的诊断, 元能力-刻意练习, 循序渐进学习曲线; trust_level=high 但 source 仅 1 个 |
| `concepts\ai-tool-learning-workbook.md` | dangling 链接: ai-tool-learning-curve|AI 工具循序渐进学习曲线, yai-counsel-role|YAI 咨询模式, productization-judgment|产品化判断, practice-card-decomposition|练习卡片拆解, fixed-routine-design|固定套路设计 |
| `concepts\ai-virtual-coach-prompt.md` | dangling 链接: timely-feedback-loop|反馈闭环, four-questions-feedback|四问法自我反馈, ai-tool-learning-curve|AI 工具循序渐进学习曲线, productization-judgment|产品化判断, yai-counsel-role|YAI 咨询模式 |
| `concepts\ai-俱乐部人和-ai-协作-五层结构.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作; source_refs 中的 src ID 未注册: src_20260609_8e64b361 |
| `concepts\ai-俱乐部人和-ai-协作-参考案例对比一堂-vs-sql-helper.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作; source_refs 中的 src ID 未注册: src_20260609_dade3353 |
| `concepts\ai单元模型口述蒋老师.md` | dangling 链接: tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作, tool-yitang-research-unit-model|单元模型 |
| `concepts\ai数据理解第一课.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\ai时代判断力口述-3.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\ai时代判断力口述.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\business-analysis.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\business-validation-models-collaboration.md` | dangling 链接: 一起引擎, 刘长胜, 外卖对接方案讨论 |
| `concepts\challenge-point-design.md` | dangling 链接: 拉伸区设计, 元能力-刻意练习, 挑战点, 角色给我的诊断; trust_level=high 但 source 仅 1 个 |
| `concepts\comfort-zone-expansion.md` | dangling 链接: deliberate-repetition|刻意重复, productization-judgment|产品化判断, deliberate-practice-four-elements|刻意练习四要素, yt-management-team-knowledge|团队知识管理, fixed-routine-design|固定套路设计 |
| `concepts\completion-criteria-design.md` | dangling 链接: 学会的定义, 元能力-刻意练习, 角色给我的诊断, 完成标准; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-AI知识库-KDO传承溯源.md` | status=draft 但 confidence=0.9 |
| `concepts\concept-AI知识库-原子化拆分.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-AI知识库-四关键词.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-aducit-six-step.md` | status=draft 但 confidence=0.9 |
| `concepts\concept-agent-as-token-consumer.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-ai-co-learning.md` | dangling 链接: framework-kdo-modeling-methodology|KDO建模方法论 |
| `concepts\concept-ai-video-wanggan-componentization.md` | status=draft 但 confidence=0.9 |
| `concepts\concept-brooks-three-lies-culture.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-candy-ai-as-collaborator.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-changing-others-as-self-compensation.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-christensen-jtbd-link.md` | dangling 链接: yt-panproduct-execution-low-cost-mvp |
| `concepts\concept-christensen-rpv-model.md` | dangling 链接: framework-decision-science-triangle |
| `concepts\concept-five-step-growth-to-barrier-transition.md` | dangling 链接: 一堂五步法 |
| `concepts\concept-harness-cattle-not-pets.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-harness-scoring-anchors.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-jevons-paradox-in-ai.md` | dangling 链接: AI 时代杰文斯悖论, 杰文斯悖论, Jevons paradox in AI |
| `concepts\concept-kdo-agent-design-principles.md` | dangling 链接: framework-一堂-TCPR皇冠模型 |
| `concepts\concept-kdo-feature-registry.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-kdo-review-workflow.md` | dangling 链接: <code>kdo pre-submit</code>, framework-kdo-self-attack|KDO 知识自攻击, ec工业化规范手册-v2.8.0|EC 工业化规范手册, framework-kdo-self-attack|KDO 知识自攻击, ec工业化规范手册-v2.8.0|EC 工业化规范手册 |
| `concepts\concept-mcp-protocol.md` | trust_level=high 但 source 仅 0 个 |
| `concepts\concept-meta-skill-layering.md` | status 值异常: pending_review |
| `concepts\concept-oral-spray-vs-typing-dialectics.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-pain-treats-pain.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-pleasure-pain-balance.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-qinpeng-ai-as-amplifier.md` | confidence=0.99 但 source 仅 1 个 |
| `concepts\concept-qinpeng-knowledge-base-conversion.md` | confidence=0.9 但 source 仅 1 个 |
| `concepts\concept-smart-medicine-cabinet-consumer-acceptance.md` | source_refs 中的 src ID 未注册: src_20260613_b0cac5a3, src_20260613_c5f5a7ce |
| `concepts\concept-smart-medicine-cabinet-digital-pharmacy-diagnosis.md` | source_refs 中的 src ID 未注册: src_20260613_98aa19d4 |
| `concepts\concept-smart-medicine-cabinet-giants-why-not-clinic-cabinet.md` | source_refs 中的 src ID 未注册: src_20260613_7cfd7b89, src_20260613_9a2b289e |
| `concepts\concept-smart-medicine-cabinet-international-models.md` | source_refs 中的 src ID 未注册: src_20260613_f23b86fa, src_20260613_c5f5a7ce |
| `concepts\concept-smart-medicine-cabinet-platform-cooperation-validation.md` | source_refs 中的 src ID 未注册: src_20260613_945a21d7 |
| `concepts\concept-spatial-narrative-design.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-strategy-evolution-cycle.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-strategy-framework-landscape.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-token-capital.md` | dangling 链接: AI 时代资本结构, 第三种资本结构, token capital |
| `concepts\concept-token-per-watt.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-truman-18-component-cards.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-truman-feature-four-scenarios.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-truman-feature-six-stages.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yihang-data-pack-ethics.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yihang-dual-triangle-core.md` | dangling 链接: 一行双三角, MUSE模型, 人机协作模型, agent-spec-yitang-dual-triangle-cross-domain-diagnostician, 缪斯模型; status=draft 但 confidence=0.88 |
| `concepts\concept-yihang-human-in-the-loop-dual-triangle.md` | dangling 链接: HITL双三角, 人在环双三角关系, annotations |
| `concepts\concept-yihang-methodology-production-pipeline.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yihang-research-driven-company.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yitang-ai-research-10-assumptions.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yitang-case-jiejiaxiuzhen.md` | dangling 链接: framework-yitang-content-polish, concept-yitang-case-soul-selection; status=draft 但 confidence=0.9 |
| `concepts\concept-yitang-education-formula.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-yitang-ideal-research-goal.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-yitang-layered-self-consistency.md` | status=draft 但 confidence=0.88 |
| `concepts\concept-一堂-AI时代基本功变与不变.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\concept-一堂-Agent基本功修炼.md` | status=draft 但 confidence=0.86 |
| `concepts\concept-一堂-business-prediction.md` | dangling 链接: 机会预判, business prediction, 商业预判课, 15字诀, 商业预判 |
| `concepts\concept-一堂-key-assumptions.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-一堂-product-kernel.md` | dangling 链接: 最小解决方案, 产品内核, product kernel |
| `concepts\concept-一堂-基本功-刻意练习四要素.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\concept-利润-真正利润定义.md` | status=draft 但 confidence=0.9 |
| `concepts\concept-利润-风险报偿本质.md` | status=draft 但 confidence=0.88 |
| `concepts\concept-定价-价格杠杆.md` | status=draft 但 confidence=0.88 |
| `concepts\concept-目标-北极星型vs探索型.md` | status=draft 但 confidence=0.88 |
| `concepts\concept-目标管理组织四阶段.md` | status=draft 但 confidence=0.85 |
| `concepts\concept-讲香-卖点直给到价值感.md` | dangling 链接: agent-一堂-个人表达力教练 |
| `concepts\deepseek-v4-在知识管理系统中的应用.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\deliberate-practice-four-elements.md` | dangling 链接: 元能力-刻意练习, 四要素诊断, 关于刻意练习的对话, 刻意练习四要素 |
| `concepts\deliberate-repetition.md` | dangling 链接: productization-judgment|产品化判断, deliberate-practice-four-elements|刻意练习四要素, yai-counsel-role|YAI 咨询模式, practice-card-decomposition|练习卡片拆解, fixed-routine-design|固定套路设计 |
| `concepts\fd-forward-deployment.md` | source_refs 中的 src ID 未注册: src_20260614_ab09af1c |
| `concepts\finance-legal-business-operations.md` | dangling 链接: 系统费用沟通, 进项税处理沟通, 企业高新技术与专精特新资质申报规划 |
| `concepts\fixed-routine-design.md` | dangling 链接: ai-tool-learning-curve|AI 工具循序渐进学习曲线, ai-tool-learning-curve|AI 工具学习曲线, productization-judgment|产品化判断, deliberate-practice-four-elements|刻意练习四要素, yai-counsel-role|YAI 咨询模式 |
| `concepts\four-questions-feedback.md` | dangling 链接: 自我反馈四问法, 元能力-刻意练习, 角色给我的诊断, 四问法; trust_level=high 但 source 仅 1 个 |
| `concepts\graph-rag.md` | source_refs 中的 src ID 未注册: src_20260502_7d7c1b7c |
| `concepts\learning-thinking.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, ai-collaboration-mindset-shift|AI协作 |
| `concepts\meta-prompt-eng.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\practice-card-decomposition.md` | dangling 链接: ai-tool-learning-curve|AI 工具循序渐进学习曲线, deliberate-repetition|刻意重复, productization-judgment|产品化判断, yai-counsel-role|YAI 咨询模式, fixed-routine-design|固定套路设计 |
| `concepts\product-business-strategy.md` | dangling 链接: 项目问题沟通, 产品方向选择讨论, 市场分析讨论 |
| `concepts\product-ux.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\productization-judgment.md` | dangling 链接: 工具产品化评估, 元能力-刻意练习, 产品化判断, 角色给我的诊断; trust_level=high 但 source 仅 1 个 |
| `concepts\smart-medicine-cabinet-national-policy-redlines.md` | source_refs 中的 src ID 未注册: src_20260613_26c69f98, src_20260613_6ed8df4b |
| `concepts\smart-medicine-cabinet-o2o-cost-structure.md` | source_refs 中的 src ID 未注册: src_20260613_26c69f98, src_20260613_6ed8df4b, src_20260613_c5f5a7ce |
| `concepts\smart-medicine-cabinet-regional-policy-map.md` | source_refs 中的 src ID 未注册: src_20260613_26c69f98, src_20260613_6ed8df4b |
| `concepts\sprint-2-门禁举证验收.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\timely-feedback-loop.md` | dangling 链接: yai-counsel-role|YAI 咨询模式, deliberate-practice-four-elements|刻意练习四要素, productization-judgment|产品化判断, fixed-routine-design|固定套路设计, four-questions-feedback|四问法自我反馈 |
| `concepts\tools-workflows.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\writing-content.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\yai-counsel-role.md` | dangling 链接: C角色咨询法, YAI C角色, 角色给我的诊断, 刻意练习方法论, 元能力-刻意练习; trust_level=high 但 source 仅 1 个 |
| `concepts\yai-tcp-teacher-role.md` | dangling 链接: 刻意练习方法论, T角色咨询法, ai-consultation-mindset-shift, 关于刻意练习的对话, YAI TCPR; trust_level=high 但 source 仅 1 个 |
| `concepts\yitang-methodology-system.md` | dangling 链接: 九层宝塔模型, 业务公式拆解培训, 世总会 |
| `concepts\yitang-qualitative-to-quantitative.md` | source_refs 中的 src ID 未注册: src_20260614_606a631d, src_20260614_6d9f7671, src_20260616_b1e25c49 |
| `concepts\yt-ai-startup-20-risky-hypotheses.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-business-formula-l6-essence-formulas.md` | source_refs 中的 src ID 未注册: src_20260613_6b939d2b, src_20260613_6edbf0af, src_20260613_a8bcfd38 |
| `concepts\yt-case-mandatory-cases.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\yt-concept-ai-guard-brain.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-concept-weapon-arsenal.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-decision-y-model.md` | dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach, agent-spec-yitang-Y-model-cross-domain-coach |
| `concepts\yt-entrepreneur-industry-forecast.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-entrepreneur-product-core.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-entrepreneur-scientific-method.md` | source_refs 中的 src ID 未注册: src_20260614_faa8021d |
| `concepts\yt-entrepreneur-unit-model.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-foresight-addition-subtraction.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-foresight-ten-fatal-flaws.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-management-founder-role.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-management-goal-management.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-aesthetic-progression.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-conversion-optimization.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-deep-review-iceberg.md` | source_refs 中的 src ID 未注册: src_20260522_c92a36ba |
| `concepts\yt-model-deliberate-practice-growth.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-dual-triangle-competitiveness.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-entrepreneur-map.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-five-step-canvas.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-ipo-complete-checklist.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-ipo-learning-strategy.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-muse-ai-framework.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-pan-product-aesthetic-toolkit.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-personal-map.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-personal-pitch-toolkit.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-prediction-model.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-product-core-metrics.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-product-excellence.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-progress-map.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-prompt-engineering.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `concepts\yt-model-questioning-practice-canvas.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-scientific-questioning-map.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-truman-career-routes.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-truman-five-step-growth.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-model-y-organization.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-note-deliberate-practice-four-elements.md` | dangling 链接: yt-note-expert-interview-modeling|专家访谈建模, deliberate-practice-four-elements|刻意练习四要素, yt-note-ai-human-division|AI 与人的笔记分工, yt-note-checklist-concept|清单体笔记概念 |
| `concepts\yt-personal-checklist-notes.md` | status=draft 但 confidence=0.85 |
| `concepts\yt-personal-deep-review.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-personal-deliberate-practice.md` | source_refs 中的 src ID 未注册: src_20260609_e13d29d9 |
| `concepts\yt-personal-ipo-learning.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-pitch-aphorism.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-pitch-colloquialization.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-pitch-conflict.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-pitch-emotionalization.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-pitch-materialization.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-pitch-scenarization.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-pitch-sublimation.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-prompt-engineering-andrew-ng.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-research-action-camp-launch.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\yt-research-weaponry-course.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\yt-three-dimension-opportunity-matrix.md` | dangling 链接: 机会预判, 三维排列组合 |
| `concepts\yt-tob-sales-unit-model.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-tool-best-practice-learning.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-tool-fab-persuasion.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-tool-mental-model-refinement.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\yt-tool-y-model-ruler.md` | trust_level=high 但 source 仅 1 个 |
| `concepts\互联网医院模式深度调研报告.md` | source_refs 中的 src ID 未注册: src_20260501_9962715b |
| `concepts\人机协作决策-双三角模型.md` | source_refs 为空 |
| `concepts\在设计小伙伴的反馈还挺好的.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\存储策略.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\学会提问在信息洪流中锻造批判性思维的利刃.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\数据标注维度最佳实践调研报告.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\老朱的水感-2026年5月.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\视觉prompt三层操作系统-srom-visual-os.md` | dangling 链接: tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作, tool-yitang-research-unit-model|单元模型 |
| `concepts\诊所o2o外卖平台业务深度调研报告.md` | source_refs 为空 |
| `concepts\那今天不会.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `concepts\鑫港湾his系统分阶段整改报告.md` | dangling 链接: tool-yitang-research-unit-model|单元模型, tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作 |
| `cross-domain-patterns\README.md` | source_refs 为空 |
| `cross-domain-patterns\pattern-hypothesis-validation.md` | type 值异常: pattern-index; source_refs 为空; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 0 个 |
| `cross-domain-patterns\pattern-layered-matching.md` | type 值异常: pattern-index; source_refs 为空; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 0 个 |
| `cross-domain-patterns\pattern-tool-vs-model.md` | type 值异常: pattern-index; source_refs 为空; trust_level=high 但 source 仅 0 个 |
| `dark-knowledges\dk-AI知识库-隐性知识显性化60分原则.md` | status=draft 但 confidence=0.85 |
| `dark-knowledges\dk-P42-agent-fact-check-gap.md` | dangling 链接: dk-P15-false-completion-report（计划卡，未产出） |
| `dark-knowledges\dk-aesthetic-redline-doc.md` | status 值异常: pending_review |
| `dark-knowledges\dk-agent-access-kdo-pitfalls.md` | status=draft 但 confidence=0.9 |
| `dark-knowledges\dk-agent-parallel-design-system.md` | status 值异常: pending_review |
| `dark-knowledges\dk-agent-promise-verification.md` | status=draft 但 confidence=0.87; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-agreeableness-double-edged.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-ai-builder-illusion.md` | dangling 链接: 做出来不是从 0 到 1, builder 幻觉, AI  builder 幻觉 |
| `dark-knowledges\dk-ai-capability-illusion.md` | status 值异常: pending_review; confidence=0.9 但 source 仅 1 个 |
| `dark-knowledges\dk-ai-collaboration-degradation-spiral.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-ai-cross-domain-inference.md` | dangling 链接: framework-kdo-modeling-methodology|KDO 建模方法论, dk-bfm-compression-path|压缩路径 |
| `dark-knowledges\dk-ai-efficiency-and-management-radius.md` | status 值异常: pending_review |
| `dark-knowledges\dk-ai-memory-four-layers.md` | status=draft 但 confidence=0.88; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-ai-self-evolution-prompt.md` | status 值异常: pending_review |
| `dark-knowledges\dk-ai-video-common-pitfalls.md` | status=draft 但 confidence=0.9 |
| `dark-knowledges\dk-analogy-blinds-search.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-anti-human-ux-is-feature.md` | status 值异常: pending_review |
| `dark-knowledges\dk-best-datasource-is-floor.md` | status 值异常: pending_review; confidence=0.9 但 source 仅 1 个 |
| `dark-knowledges\dk-bfm-compression-path.md` | status=draft 但 confidence=0.85 |
| `dark-knowledges\dk-brooks-cost-of-knowing.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-coaching-boundary-conditions.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-coaching-monkey-theory.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-collection-vs-assets.md` | status 值异常: pending_review |
| `dark-knowledges\dk-context-patching-recipe.md` | status 值异常: pending_review |
| `dark-knowledges\dk-decision-when-to-defer.md` | dangling 链接: framework-decision-cognitive-bias-map|认知偏差地图, concept-稀缺机会窗口|稀缺机会窗口, master-decision-hygiene|决策卫生五步法, framework-decision-quality-checklist|决策质量六问检查表, dk-你的业务是一次抽样实验|你的业务是一次抽样实验 |
| `dark-knowledges\dk-delivery-path-type-bug.md` | confidence=0.9 但 source 仅 1 个 |
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
| `dark-knowledges\dk-demand-signal-vs-noise.md` | dangling 链接: yt-demand-fake-demand-detection|伪需求识别：7个危险信号, framework-decision-cognitive-bias-map|认知偏差地图, yt-demand-early-validation|需求早期验证, framework-demand-validation-pipeline|需求验证流水线, case-demand-b2c-consumer-insight|ToC 消费洞察驱动需求案例 |
| `dark-knowledges\dk-demand-switching-cost.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-doc-explosion-slowdown.md` | status 值异常: pending_review |
| `dark-knowledges\dk-doc-numbering-business-logic.md` | status 值异常: pending_review |
| `dark-knowledges\dk-emotional-value-high-bar.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-emotional-value-premium.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-feature-not-learned-but-used.md` | confidence=0.92 但 source 仅 1 个; status=draft 但 confidence=0.92; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-feature-registry-count-drift.md` | status=draft 但 confidence=0.88 |
| `dark-knowledges\dk-future-backward-knowledge-tree.md` | status 值异常: pending_review |
| `dark-knowledges\dk-key-hypothesis-still-hope.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-koupen-500-vs-5000.md` | status=draft 但 confidence=0.85 |
| `dark-knowledges\dk-koupen-decision-tiering-compromise.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-leadership-trust-coin-sensitivity.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-let-ai-learn-for-me.md` | status 值异常: pending_review |
| `dark-knowledges\dk-market-info-gap-to-product-strategy.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-mckinsey-hypothesis-driven-pitfalls.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-mcp-pythonpath-pollution.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9 |
| `dark-knowledges\dk-modeling-ai-without-judgment.md` | trust_level=high 但 source 仅 0 个 |
| `dark-knowledges\dk-modeling-counterexample-driven.md` | trust_level=high 但 source 仅 0 个 |
| `dark-knowledges\dk-modeling-essence-predictive.md` | confidence=0.9 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `dark-knowledges\dk-modeling-jump-step-cost.md` | status=draft 但 confidence=0.88 |
| `dark-knowledges\dk-modeling-question-scaffold-not-answer.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-my-ai-landing-three-barriers.md` | source_refs 为空 |
| `dark-knowledges\dk-narrative-choice-theory.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-occhams-knife-tool-migration.md` | status 值异常: pending_review |
| `dark-knowledges\dk-one-sentence-handover.md` | confidence=0.9 但 source 仅 1 个 |
| `dark-knowledges\dk-oral-spray-newcomer-blockers.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-post-hoc-framework-vs-messy-reality.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-process-is-scar-tissue.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-project-manager-agent-failure.md` | status 值异常: pending_review; confidence=0.9 但 source 仅 1 个 |
| `dark-knowledges\dk-publish-collapse-to-iterate.md` | status=draft 但 confidence=0.85 |
| `dark-knowledges\dk-research-ai-no-time-concept.md` | confidence=0.9 但 source 仅 1 个 |
| `dark-knowledges\dk-rule-not-system-capability.md` | status 值异常: pending_review; confidence=0.9 但 source 仅 1 个 |
| `dark-knowledges\dk-shoulu-yixia-culture.md` | status 值异常: pending_review |
| `dark-knowledges\dk-skill-market-agent-self-install.md` | source_refs 中的 src ID 未注册: src_20260606_6ea91aa8 |
| `dark-knowledges\dk-skill-seven-elements-upgrade.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-sponsor-three-tier-pricing.md` | dangling 链接: five-step-domain-digest|五步法, business-formula-domain-digest|业务公式, case-wangfei-newyear-event-diagnosis|王非跨年案例, business-formula-domain-digest|业务公式域; status=draft 但 confidence=0.85 |
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
| `dark-knowledges\dk-three-context-formula.md` | confidence=0.9 但 source 仅 1 个 |
| `dark-knowledges\dk-token-economy-critical-reading.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-tool-adoption-by-force.md` | confidence=0.9 但 source 仅 1 个 |
| `dark-knowledges\dk-tool-as-phased-validator.md` | dangling 链接: skill-note-one-line-one-point; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-unit-model-reverse-calc.md` | status=draft 但 confidence=0.85 |
| `dark-knowledges\dk-y-model-communication.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yihang-ai-false-certainty.md` | status=draft 但 confidence=0.9 |
| `dark-knowledges\dk-yihang-canvas-preparation-three-principles.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yihang-dual-triangle-commitment-confidence.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yihang-dual-triangle-strategic-bet.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yihang-multi-ai-cross-validation.md` | status=draft 但 confidence=0.88; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yihang-non-expert-judgment.md` | status=draft 但 confidence=0.88 |
| `dark-knowledges\dk-yihang-report-book-learner.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yihang-scientific-community-moat.md` | status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yihang-technical-domain-aesthetic.md` | status=draft 但 confidence=0.88; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yitang-Y-model-pitfalls.md` | trust_level=high 但 source 仅 0 个 |
| `dark-knowledges\dk-yitang-case-before-after.md` | status=draft 但 confidence=0.88 |
| `dark-knowledges\dk-yitang-case-crafting-pitfalls.md` | status=draft 但 confidence=0.88 |
| `dark-knowledges\dk-yitang-fact-three-questions-trust-tiers.md` | trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-yitang-innovation-failure-modes.md` | status=draft 但 confidence=0.87 |
| `dark-knowledges\dk-利润-创始人利润耻感.md` | status=draft 但 confidence=0.87 |
| `dark-knowledges\dk-利润-利润敏感度非对称性.md` | status=draft 但 confidence=0.88; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-利润-定价恐惧三段式反问.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-利润-平台驱动本质是现金流驱动.md` | status=draft 但 confidence=0.86; trust_level=high 但 source 仅 1 个 |
| `dark-knowledges\dk-利润-资本游戏与真实商业分界线.md` | status=draft 但 confidence=0.87 |
| `dark-knowledges\dk-实事求是目标管理双原则.md` | status=draft 但 confidence=0.88 |
| `dark-knowledges\dk-目标管理四大病.md` | status=draft 但 confidence=0.9 |
| `dark-knowledges\dk-管控vs协同执行策略.md` | status=draft 但 confidence=0.87 |
| `decisions\huangyaoshi-tagging-and-scope-proposal.md` | source_refs 中的 src ID 未注册: src_20260528_4277c6be |
| `decisions\kdo-15-dimension-label-spec.md` | source_refs 中的 src ID 未注册: src_20260606_6dad71f1 |
| `decisions\kdo-ec-industrialization-migration-proposal.md` | source_refs 中的 src ID 未注册: src_20260503_dadc7838, src_20260503_feab72b2 |
| `decisions\modeling-capability-for-kdo.md` | trust_level=high 但 source 仅 0 个 |
| `decisions\plan_20260501_05858800-improvement-plan.md` | source_refs 中的 src ID 未注册: src_20260501_58b6edef |
| `decisions\plan_20260501_47264869-improvement-plan.md` | source_refs 中的 src ID 未注册: src_20260501_58b6edef |
| `decisions\plan_20260501_8001399c-improvement-plan.md` | source_refs 中的 src ID 未注册: src_20260501_58b6edef |
| `decisions\plan_20260501_85a84b92-improvement-plan.md` | source_refs 中的 src ID 未注册: src_20260501_58b6edef |
| `decisions\plan_20260501_8ecb74e3-improvement-plan.md` | source_refs 中的 src ID 未注册: src_20260501_58b6edef |
| `decisions\plan_20260501_97170532-improvement-plan.md` | source_refs 中的 src ID 未注册: src_20260501_58b6edef |
| `decisions\plan_20260501_ca61cdd7-improvement-plan.md` | source_refs 中的 src ID 未注册: src_20260501_58b6edef |
| `decisions\plan_20260501_e1e150b9-improvement-plan.md` | source_refs 中的 src ID 未注册: src_20260501_58b6edef |
| `decisions\plan_20260621_crawl4ai-firecrawl-evaluation.md` | status=draft 但 confidence=0.85 |
| `decisions\plan_20260621_domain-index-infrastructure.md` | dangling 链接: <code>check-source-refs.py</code>, <code>track-production-progress.py</code> |
| `decisions\plan_20260701_kdo-multi-repo-architecture.md` | dangling 链接: plan-kdo-infrastructure-disaster-prevention, kdo-system-manual |
| `decisions\plan_20260707_capability-hub-architecture.md` | source_refs 为空; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 0 个 |
| `dk\dk-disruptive-innovation-insight-vs-survey.md` | dangling 链接: yt-panproduct-execution-low-cost-mvp |
| `dk\dk-feishu-bot-slow-session-hygiene.md` | dangling 链接: framework-hermes-multi-bot-feishu-setup |
| `dk\dk-jiejiaxiuzhen-ai-reestablish.md` | status=draft 但 confidence=0.85 |
| `dk\dk-meeting-asset-harvest.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-meeting-borrow-false-repair-true.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-meeting-rederive.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-meeting-roi-first.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-multithread-whack-a-mole.md` | status=draft 但 confidence=0.85 |
| `dk\dk-project-skill-agent-loop.md` | status=draft 但 confidence=0.85 |
| `dk\dk-qinpeng-three-corrections.md` | dangling 链接: yt-panproduct-execution-roi-analysis, yt-panproduct-execution-low-cost-mvp |
| `dk\dk-roi-three-step-decision.md` | status=draft 但 confidence=0.88 |
| `dk\dk-yitang-digging-belief.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-expert-interview-5-traps.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-formula-unmeasurable-metrics.md` | status=draft 但 confidence=0.85 |
| `dk\dk-yitang-public-info-is-enough.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-ai-hallucination.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-cost-value-match.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-desperate-effort.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-goal-before-efficiency.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-source-freshness.md` | trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-research-starter-vs-veteran.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `dk\dk-yitang-survivor-bias-in-research.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `domains\ai-collaboration-domain-digest.md` | trust_level=high 但 source 仅 1 个 |
| `domains\business-formula-domain-digest.md` | dangling 链接: agent-一堂-业务公式教练, agent-一堂-业务公式教练 |
| `domains\conversion-rate-domain-digest.md` | dangling 链接: case-一堂-棋牌室办卡率1到5|棋牌室办卡率, case-一堂-六杯奶茶推荐率近100|六杯奶茶, case-一堂-一堂自身转化实践|一堂自身转化实践, case-一堂-全会员出圈率1.5翻倍|全会员出圈率, case-一堂-作业率20到50|作业率 20%→50% |
| `domains\decision-science-domain-digest.md` | dangling 链接: dk-决策经验值|决策经验值——老手和新手的隐性差距, concept-AI时代双三角竞争力|AI时代双三角竞争力, case-科学决策-深度案例06|电话外呼的ROI分析, concept-最佳实践建模|最佳实践建模, tool-场景推演|场景推演 |
| `domains\design-moc.md` | status=draft 但 confidence=0.85 |
| `domains\domain-demand-analysis-index.md` | dangling 链接: yt-demand-b2b-vs-b2c|ToB vs ToC需求分析差异, dk-demand-switching-cost|新体验-旧体验-切换成本=产品价值, tool-demand-assessment-triangle|需求评估三角形, yt-demand-hierarchy-model|需求层次模型, tool-需求挖掘|需求挖掘; trust_level=high 但 source 仅 1 个 |
| `domains\human-ai-collaboration-double-triangle.md` | source_refs 为空 |
| `domains\human-insights-domain-digest.md` | dangling 链接: framework-big-five-personality - concept-pleasure-pain-balance - framework-dopamine-recovery - tool-self-binding-three-strategies - concept-pain-treats-pain |
| `domains\innovation-domain-digest.md` | type 值异常: digest; source_refs 为空; confidence=0.9 但 source 仅 0 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 0 个 |
| `domains\kdo-moc.md` | dangling 链接: kdo-charter-v0.1-draft; status=draft 但 confidence=0.85 |
| `domains\management-domain-digest.md` | confidence=0.9 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `domains\master-moc.md` | trust_level 值异常: observed |
| `domains\product-moc.md` | status=draft 但 confidence=0.85 |
| `domains\retrospective-moc.md` | status=draft 但 confidence=0.85 |
| `domains\sales-domain-digest.md` | status=draft 但 confidence=0.9 |
| `domains\strategy-domain-digest.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `domains\yitang-domain-digest.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `entities\Kimi-月之暗面.md` | source_refs 中的 src ID 未注册: src_20260503_52ae08ba |
| `entities\YC-Y-Combinator.md` | source_refs 中的 src ID 未注册: src_20260430_8cc84e5b |
| `entities\一堂.md` | source_refs 中的 src ID 未注册: src_20260613_6b939d2b |
| `entities\七件事集团.md` | dangling 链接: case-qishijian-smart-medicine-cabinet; confidence=0.9 但 source 仅 1 个 |
| `entities\紫鲸AI.md` | source_refs 中的 src ID 未注册: src_20260428_29929c1f |
| `entities\鑫港湾.md` | source_refs 中的 src ID 未注册: src_20260503_52ae08ba |
| `frameworks\ai-complex-communication.md` | source_refs 中的 src ID 未注册: src_20260614_d79b42d1 |
| `frameworks\ai-methodology-tools.md` | dangling 链接: 何老师, 场景落地方法分享, 工具使用分享 |
| `frameworks\beverage-foodservice-channel.md` | source_refs 中的 src ID 未注册: src_20260614_8a0317f1, src_20260614_16c4bf0d, src_20260614_d6ab6fb6 |
| `frameworks\bridge-利润-单元模型-定价闭环.md` | status=draft 但 confidence=0.88 |
| `frameworks\bridge-利润-需求冰山-价值定价.md` | status=draft 但 confidence=0.85 |
| `frameworks\concept-mckinsey-hypothesis-driven.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-AI知识库-Workflow六要素.md` | status=draft 但 confidence=0.9 |
| `frameworks\framework-AI知识库-五维标注深挖法.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-AI知识库-五阶段演进.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-AI知识库-分库与映射表.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-AI知识库-加卡片加标签双原则.md` | status=draft 但 confidence=0.9 |
| `frameworks\framework-AI知识库-四象限资产.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-AI知识库-知识卡片公式.md` | status=draft 但 confidence=0.9 |
| `frameworks\framework-TCPR底层网络协议.md` | dangling 链接: agent-os |
| `frameworks\framework-TCPR皇冠模型.md` | dangling 链接: agent-os, agent-os |
| `frameworks\framework-agent-card-execution-pattern.md` | dangling 链接: agent-os |
| `frameworks\framework-ai-video-production-aesthetics-first.md` | source_refs 为空; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-christensen-disruptive-innovation.md` | dangling 链接: yt-panproduct-execution-roi-analysis, yt-panproduct-execution-low-cost-mvp |
| `frameworks\framework-christensen-value-network.md` | dangling 链接: framework-yitang-five-step-barrier |
| `frameworks\framework-coaching-leadership-core.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-decision-cognitive-bias-map.md` | dangling 链接: master-cognitive-bias-checklist|认知偏差检查清单, dk-决策经验值|决策经验值, framework-decision-quality-checklist|决策质量六问检查表, concept-X型Y型决策习惯|X型 vs Y型决策习惯; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-decision-quality-checklist.md` | dangling 链接: yt-decision-abcd-model|关键假设 ABCD 模型, master-decision-hygiene|决策卫生五步法; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-demand-ceiling-four-lines.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-demand-iceberg.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-demand-usp-model.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-demand-validation-pipeline.md` | dangling 链接: dk-demand-signal-vs-noise|需求信号与噪音的区分, tool-lean-fake-product|假产品, yt-demand-early-validation|需求早期验证, framework-demand-lean-bridge|需求判断与精益验证的衔接, yt-demand-hierarchy-model|需求层次模型; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-dopamine-recovery.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-education-protracted-war.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-fact-rule-insight.md` | status 值异常: pending_review; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-five-step-lean-interface.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-kdo-mcp-server.md` | source_refs 为空; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-kdo-modeling-methodology.md` | source_refs 为空; confidence=0.9 但 source 仅 0 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-knowledge-naming-systems-comparison.md` | status 值异常: pending_review |
| `frameworks\framework-leadership-coin-model.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-leadership-five-ladders.md` | confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-lean-abcd-model.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-lean-false-model.md` | confidence=0.9 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-lean-four-principles.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-lean-pivot-decision.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-lean-product-kernel.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-lean-systematic-test-curve.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-lean-tenx-formula.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-lemon-market-new-brand-trust.md` | status 值异常: pending_review |
| `frameworks\framework-meeting-iceberg-canvas.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-modeling-relation-exploration.md` | source_refs 为空; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-muse-ai-full-map-v1.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-openclaw-vs-harness-selection.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-oral-spray-cultivation-map.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-ouyangfeng-review-methodology.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-ansoff.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-basics-01-core.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-basics-02-insight.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-basics-03-layout.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-basics-04-system.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-basics-05-change.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-blm.md` | confidence=0.95 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-business-design.md` | confidence=0.95 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-conviction.md` | status=draft 但 confidence=0.88 |
| `frameworks\framework-strategy-five-basics.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-five-forces.md` | confidence=0.95 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-kai-innovation-directions.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-lean-validation.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-mckinsey-7s.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-pyramid.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-strategy-six-stages.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-strategy-three-horizons.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-token-economy-three-layer.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-truman-feature-layered-system.md` | status=draft 但 confidence=0.93 |
| `frameworks\framework-truman-feature-thinking-core.md` | status=draft 但 confidence=0.95 |
| `frameworks\framework-visual-analysis-four-dimensions.md` | confidence=0.9 但 source 仅 1 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-yihang-AI-native-dual-triangle-kernel.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yihang-aesthetic-judgment-training.md` | source_refs 为空; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yihang-ai-implementation-consultant.md` | source_refs 为空 |
| `frameworks\framework-yihang-dual-triangle-ai-landing-five-steps.md` | source_refs 为空; dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yihang-dual-triangle-ten-year-map.md` | source_refs 为空; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yihang-dual-triangle-three-stages-six-changes.md` | source_refs 为空; status=draft 但 confidence=0.86; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yihang-dual-triangle-weapon-library.md` | source_refs 为空; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yihang-fde-ai-native-org.md` | source_refs 为空; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yihang-knowledge-data-decoupling.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yitang-case-crafting-four-step.md` | source_refs 为空; confidence=0.9 但 source 仅 0 个; status=draft 但 confidence=0.9; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yitang-channel-industrialization.md` | dangling 链接: concept-yitang-channel-lean-validation-bridge|渠道精益验证, framework-yitang-growth-flywheel|增长飞轮, framework-yitang-channel-exploration-4step|渠道探索四步法, framework-yitang-channel-unit-economics|渠道单元经济模型 |
| `frameworks\framework-yitang-deliberate-practice-1plus4.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-yitang-five-step-to-time-management.md` | dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach |
| `frameworks\framework-yitang-jiefang-sixiang.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yitang-research-weapon-supplement-2026.md` | status=draft 但 confidence=0.88 |
| `frameworks\framework-yitang-scientific-sales-five-step.md` | dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach, agent-spec-yitang-Y-model-cross-domain-coach |
| `frameworks\framework-yitang-shishi-qiushi.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-yitang-thought-liberation-lightning.md` | status=draft 但 confidence=0.88 |
| `frameworks\framework-yitang-y-model-cross-domain-fusion.md` | dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach, agent-spec-yitang-Y-model-cross-domain-coach; status=draft 但 confidence=0.85 |
| `frameworks\framework-yitang-y-model-dual-triangle-synergy.md` | dangling 链接: 双三角迭代发动机, agent-spec-yitang-dual-triangle-cross-domain-diagnostician, Y模型双三角协同, annotations |
| `frameworks\framework-一堂-个人表达力.md` | dangling 链接: agent-一堂-个人表达力教练 |
| `frameworks\framework-一堂-关键假设-三板斧.md` | source_refs 为空; status=draft 但 confidence=0.86; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-关键假设.md` | source_refs 为空; dangling 链接: agent-一堂-关键假设教练, agent-一堂五步法教练; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-动力三曲线.md` | source_refs 为空; status=draft 但 confidence=0.87; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-十指模型.md` | source_refs 为空; status=draft 但 confidence=0.86; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-四象限复盘法.md` | confidence=0.95 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-一堂-团队复盘四阶段12策略.md` | dangling 链接: framework-一堂-刻意练习 |
| `frameworks\framework-一堂-基本功-九层金字塔.md` | confidence=0.9 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-基本功-四字诀拆建推练.md` | dangling 链接: agent-一堂-基本功教练; confidence=0.9 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-基本功-四类工作四化.md` | dangling 链接: case-一堂-春萍-温校长校园代理|温校长, case-一堂-春萍-花总AI研发|花总, case-一堂-春萍-刘伟tob销售标准化|刘伟; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-复盘本质与三要素.md` | confidence=0.95 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-一堂-影响力36计.md` | source_refs 为空; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-机会预判.md` | source_refs 为空; dangling 链接: agent-一堂-机会预判教练; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-表达力火箭模型.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\framework-一堂-触点本质论.md` | source_refs 为空; status=draft 但 confidence=0.87; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-转化基本功七个自我修养.md` | source_refs 为空; status=draft 但 confidence=0.87; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-转化率提升六步法.md` | source_refs 为空; status=draft 但 confidence=0.86; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-转化率黑客-总纲.md` | source_refs 为空; dangling 链接: conversion-rate-domain-digest|D 域, business-formula-domain-digest|C 域, decision-science-domain-digest|B 域, five-step-domain-digest|A 域; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-转化率黑客爬山地图.md` | source_refs 为空; status=draft 但 confidence=0.87; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂-阻力方法论骨架.md` | source_refs 为空; status=draft 但 confidence=0.87; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂五步法-增长周期.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂五步法-壁垒.md` | trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂五步法-泛产品设计.md` | dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-一堂五步法.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `frameworks\framework-利润-利润优先经营框架.md` | status=draft 但 confidence=0.85 |
| `frameworks\framework-目标三层拆解.md` | status=draft 但 confidence=0.87 |
| `frameworks\framework-科学决策三角形.md` | dangling 链接: agent-一堂-科学决策教练 |
| `frameworks\smart-device-foodservice-automation.md` | source_refs 中的 src ID 未注册: src_20260614_909802bd |
| `frameworks\yt-decision-y-model-philosophical-roots.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\yt-lean-false-model-ai.md` | dangling 链接: 精益方法论培训 |
| `frameworks\yt-tob-barriers.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\yt-tob-demand-metrics.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\yt-tob-growth-channel.md` | trust_level=high 但 source 仅 1 个 |
| `frameworks\yt-unit-model-overview.md` | dangling 链接: tool-demand-iceberg-l1-user|需求冰山, learning-thinking|学习方法论, ai-collaboration-mindset-shift|AI协作, tool-yitang-research-unit-model|单元模型 |
| `index.md` | dangling 链接: tools/yt-tool-business-formula-inspiration-5|灵感闪现五字诀：压 / 看 / 聚 / 拆 / 再, tools/tool-yitang-weapon-insider-intelligence|武器库策略5：内部人情报——员工/离职员工的信息价值, tools/tool-yitang-project-risk-discovery|项目常见风险发现七维度清单, cases/case-yihang-dual-triangle-beike-ai-outbound|一行双三角案例：贝壳找房110个场景的AI外呼, tools/tool-水水-构建自利叙事|技能：构建自利叙事 |
| `knowledges\knowledge-demand-2b-dictionary.md` | type 值异常: knowledge |
| `knowledges\knowledge-demand-2c-dictionary.md` | type 值异常: knowledge |
| `links\index.md` | dangling 链接: concepts/concept-ai-co-learning, dk-demand-switching-cost|新体验-旧体验-切换成本=产品价值, operations/runbook-agent-spec-to-runtime, business-formula-domain-digest|C 域, agent-一堂五步法教练 |
| `methods\method-anthropic-skill-design-patterns.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-arui-business-scenario-3step-decomposition.md` | type 值异常: method |
| `methods\method-course-creation-eleven-steps.md` | type 值异常: method |
| `methods\method-dual-triangle-flywheel-engine.md` | type 值异常: method |
| `methods\method-dual-triangle-human-ai-division.md` | type 值异常: method |
| `methods\method-judge-skill-meta-evaluation.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-kdo-agent-design-meta.md` | type 值异常: method |
| `methods\method-kdo-agent-distillation.md` | type 值异常: method |
| `methods\method-kdo-external-exploration-sop.md` | type 值异常: method |
| `methods\method-kdo-inbox-annotation.md` | type 值异常: method |
| `methods\method-key-assumption-abcd.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-obsidian-ai-collaboration.md` | type 值异常: method |
| `methods\method-obsidian-km-camp.md` | type 值异常: method |
| `methods\method-shizhi-jiangxiang-ten-strategies.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-spin-linking-sales-marketing.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-storytelling-with-numbers.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-yihang-aesthetic-fast-build.md` | type 值异常: method |
| `methods\method-yihang-agent-hr-role.md` | type 值异常: method; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `methods\method-yihang-ai-self-xray-iteration.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-yihang-dual-triangle-ai-review.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-yihang-dual-triangle-deliberate-practice.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-yihang-dual-triangle-team-assembly.md` | type 值异常: method; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 1 个 |
| `methods\method-yihang-human-self-distillation.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-yihang-knowledge-battle-station.md` | type 值异常: method; trust_level=high 但 source 仅 1 个 |
| `methods\method-yihang-knowledge-versioning.md` | type 值异常: method; status=draft 但 confidence=0.85; trust_level=high 但 source 仅 1 个 |
| `methods\method-yitang-jiangxiang-audience-value-routing.md` | type 值异常: method |
| `methods\method-yitang-micro-innovation.md` | type 值异常: method |
| `methods\method-yitang-y-model-engine-cycle.md` | type 值异常: method; dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach |
| `methods\method-yitang-y-model-structured-form.md` | type 值异常: method |
| `methods\method-一堂-教练对话引擎协议.md` | type 值异常: method; dangling 链接: agent-一堂-科学决策教练, agent-一堂-业务公式教练; status=draft 但 confidence=0.85 |
| `operations\runbook-agent-spec-to-runtime.md` | type 值异常: doc; dangling 链接: agent-spec-yitang-dual-triangle-cross-domain-diagnostician, agent-spec-yitang-dual-triangle-cross-domain-diagnostician |
| `personal-os\zhu-codebase-ai-orchestration.md` | dangling 链接: user-insight-profile |
| `personal-os\zhu-future-directions.md` | dangling 链接: user-insight-profile |
| `personal-os\zhu-lessons-learned.md` | dangling 链接: user-insight-profile |
| `personal-os\zhu-network-resources.md` | dangling 链接: user-insight-profile |
| `personal-os\zhu-time-os.md` | dangling 链接: user-preferences, operating-principles, user-insight-profile |
| `principles\principle-yitang-y-model-boundary.md` | type 值异常: principle; status=draft 但 confidence=0.9 |
| `principles\principle-yitang-y-model-dual-posture.md` | type 值异常: principle; status=draft 但 confidence=0.85 |
| `prompt-methodology\prompt-demand-ai-coach.md` | type 值异常: prompt-methodology; confidence=0.92 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `skills\feishu-docx-pagination-extraction.md` | confidence=0.95 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `skills\skill-demand-analysis.md` | dangling 链接: agent-spec-demand-iceberg-coach |
| `skills\skill-duanwangye-feishu-publishing.md` | confidence=0.95 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `skills\skill-duanwangye-kdo-pipeline.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `skills\skill-duanwangye-prezi.md` | status=draft 但 confidence=0.85 |
| `skills\skill-duanwangye-wechat-extraction.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `skills\skill-feishu-doc-l3-extraction.md` | confidence=0.95 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `systems\agent-external-brain-design.md` | source_refs 中的 src ID 未注册: src_20260503_52ae08ba |
| `systems\agent-native-card-design.md` | dangling 链接: tool-agent-spec-yitang-Y-model-coach - dk-agent-promise-verification; source_refs 中的 src ID 未注册: src_20260503_52ae08ba |
| `systems\graph-rag-retrieval-layer.md` | source_refs 中的 src ID 未注册: src_20260502_7d7c1b7c, src_20260503_9bfe6913 |
| `systems\system-kdo-quality-framework.md` | status=draft 但 confidence=0.85 |
| `systems\system-yitang-Y-model-os.md` | dangling 链接: agent-os, agent-spec-yitang-Y-model-cross-domain-coach |
| `tools\agent-spec-basic-skills-coach.md` | type 值异常: agent-spec |
| `tools\agent-spec-coaching-leadership-assistant.md` | type 值异常: agent-spec |
| `tools\agent-spec-codex-teammate.md` | type 值异常: agent-spec |
| `tools\agent-spec-dual-triangle-canvas-filler.md` | type 值异常: agent-spec; dangling 链接: administrator, desktop, 双三角挖掘师, 对话教练版 Agent, 画布填充 Agent |
| `tools\agent-spec-meeting-assistant.md` | type 值异常: agent-spec; dangling 链接: agent-spec-coaching-leadership-coach |
| `tools\agent-spec-project-management-assistant.md` | type 值异常: agent-spec; dangling 链接: 管项目Agent, 项目管理教练, 项目对话教练 |
| `tools\agent-spec-research-explosion-partner.md` | type 值异常: agent-spec |
| `tools\agent-spec-复盘教练.md` | type 值异常: agent-spec; status=draft 但 confidence=0.88; trust_level=high 但 source 仅 1 个 |
| `tools\smart-medicine-cabinet-financial-model.md` | source_refs 中的 src ID 未注册: src_20260613_26c69f98, src_20260613_6ed8df4b, src_20260613_b0cac5a3 |
| `tools\smart-medicine-cabinet-fraud-detection.md` | source_refs 中的 src ID 未注册: src_20260613_26c69f98, src_20260613_6ed8df4b, src_20260613_59270720 |
| `tools\tool-IPO学习-输入处理输出工具箱导航.md` | dangling 链接: agent-个人学习方法教练 |
| `tools\tool-OGSM目标管理工具.md` | status=draft 但 confidence=0.85 |
| `tools\tool-Truman-双三角模型应用.md` | source_refs 为空 |
| `tools\tool-Y模型STEPS策略集.md` | dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach, dk-yitang-Y-model-pitfalls|六大陷阱, agent-spec-yitang-Y-model-cross-domain-coach, method-yitang-y-model-engine-cycle|Y模型引擎循环, agent-spec-yitang-Y-model-cross-domain-coach|跨域 Coach Agent |
| `tools\tool-Y模型实操工作流.md` | dangling 链接: agent-spec-yitang-Y-model-cross-domain-coach, dk-yitang-Y-model-pitfalls|六大陷阱, framework-yitang-scientific-sales-five-step|科学销售, agent-spec-yitang-Y-model-cross-domain-coach, tool-yitang-Y-model-application|Y模型应用工作流 |
| `tools\tool-agent-crawl4ai.md` | trust_level=high 但 source 仅 0 个 |
| `tools\tool-agent-firecrawl.md` | trust_level=high 但 source 仅 0 个 |
| `tools\tool-agent-native-overview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-agent-spec-business-formula-parameter-miner.md` | type 值异常: tool-agent-spec |
| `tools\tool-agent-spec-yitang-Y-model-coach.md` | type 值异常: tool-agent-spec |
| `tools\tool-agent-spec-yitang-ability-migration-diagnosis.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-aesthetic-radar-modeling.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-beautiful-work-imagination.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-card-dealing-guide.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-customer-segmentation.md` | type 值异常: tool-agent-spec; dangling 链接: 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-customer-segmentation__SaaS_线索分级.md|SaaS 5 条线索分级, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-customer-segmentation__医药零售_B2B_线索分级_v1.1.md, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-customer-segmentation__医药零售_B2B_线索分级.md|医药零售 B2B 5 条线索分级 |
| `tools\tool-agent-spec-yitang-daily-weekly-meeting-host.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-incentive-design.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-kernel-add-subtract-diagnosis.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-kernel-canvas-autofill.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-kernel-case-matching.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-kernel-failure-mode-diagnosis.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-kernel-iteration-direction.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-kernel-three-questions.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-kernel-verification-ladder.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-lead-funnel-health.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-objection-handler.md` | type 值异常: tool-agent-spec; dangling 链接: 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-objection-handler__智能药柜价格异议.md|智能药柜价格异议, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-objection-handler__剧本杀_SaaS_时机异议.md|剧本杀 SaaS 时机异议 |
| `tools\tool-agent-spec-yitang-opening-3min.md` | type 值异常: tool-agent-spec; dangling 链接: 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-opening-3min__首条消息给连锁药店采购总监.md|首条消息给连锁药店采购总监, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-opening-3min__首通电话攻略给_SaaS_潜在客户.md|首通电话攻略给 SaaS 潜在客户 |
| `tools\tool-agent-spec-yitang-payment-collection-risk.md` | type 值异常: agent-spec; status=draft 但 confidence=0.85 |
| `tools\tool-agent-spec-yitang-project-background-analysis.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-sales-performance-monitor.md` | type 值异常: tool-agent-spec; dangling 链接: 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-sales-performance-monitor__美容院连锁月度_Pipeline_复盘.md|美容院连锁月度 Pipeline 5 客户复盘, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-sales-performance-monitor__智能药柜月度_Pipeline_复盘.md|智能药柜月度 Pipeline 10 客户复盘, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-sales-performance-monitor__智能药柜月度_Pipeline_复盘_v1.1.md |
| `tools\tool-agent-spec-yitang-sales-process-tracker.md` | type 值异常: tool-agent-spec; dangling 链接: 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-sales-process-tracker__剧本杀_SaaS_多轮推进.md|剧本杀 SaaS 多轮推进, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-sales-process-tracker__智能药柜多轮推进.md|智能药柜多轮推进 |
| `tools\tool-agent-spec-yitang-sales-toolkit-gap.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-scenario-walkthrough.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-self-motivation.md` | type 值异常: tool-agent-spec; dangling 链接: 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-self-motivation__月度目标超前_+_防松懈.md|月度目标超前 + 防松懈, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-self-motivation__周目标落后_+_倦怠.md|周目标落后 + 倦怠 |
| `tools\tool-agent-spec-yitang-three-second-opening-scripts.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-user-perspective-training.md` | type 值异常: agent-spec |
| `tools\tool-agent-spec-yitang-value-proposition.md` | type 值异常: tool-agent-spec; dangling 链接: 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-value-proposition__智能药柜卖给连锁药店.md|智能药柜卖给连锁药店, 60_feedback/agent-traces/2026-07-02/tool-agent-spec-yitang-value-proposition__剧本杀_SaaS_卖给桌游吧.md|剧本杀 SaaS 卖给桌游吧 |
| `tools\tool-agent-white-paper-five-elements.md` | status 值异常: pending_review; confidence=0.9 但 source 仅 1 个 |
| `tools\tool-agent-whitepaper-full-lifecycle-template.md` | dangling 链接: agent-whitepaper-template |
| `tools\tool-ai-adapted-workflow-design.md` | status 值异常: pending_review; confidence=0.9 但 source 仅 1 个 |
| `tools\tool-ai-agent-feature-comparison.md` | status 值异常: pending_review |
| `tools\tool-ai-customer-quality-audit.md` | status=draft 但 confidence=0.85 |
| `tools\tool-ai-feature-inventory.md` | status=draft 但 confidence=0.88 |
| `tools\tool-ai-koupen-training-partner-design.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-ai-video-cost-optimization.md` | status=draft 但 confidence=0.87 |
| `tools\tool-ai-video-market-gap-assessment.md` | status=draft 但 confidence=0.87 |
| `tools\tool-anti-ai-bs-three-moves.md` | status 值异常: pending_review; confidence=0.9 但 source 仅 1 个 |
| `tools\tool-author-targeted-collect.md` | status=draft 但 confidence=0.85 |
| `tools\tool-candy-oral-polish.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-candy-positioning-canvas.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-cangjie-skill.md` | status=draft 但 confidence=0.9 |
| `tools\tool-clinic-cabinet-legal-contract-guide.md` | source_refs 中的 src ID 未注册: src_20260613_f3aecb2d, src_20260613_9a2b289e |
| `tools\tool-coaching-communication-four-layers.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-cross-city-replication-test.md` | status=draft 但 confidence=0.85 |
| `tools\tool-darwin-skill.md` | status=draft 但 confidence=0.9 |
| `tools\tool-decision-narrative-method.md` | status=draft 但 confidence=0.85 |
| `tools\tool-demand-agent-auto-verify.md` | trust_level=high 但 source 仅 0 个 |
| `tools\tool-demand-agent-case-match.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-agent-multi-hypothesis.md` | trust_level=high 但 source 仅 0 个 |
| `tools\tool-demand-agent-signal-substitute.md` | trust_level=high 但 source 仅 0 个 |
| `tools\tool-demand-agent-signals.md` | trust_level=high 但 source 仅 0 个 |
| `tools\tool-demand-assessment-triangle.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-blindspot-checklist.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-four-forces.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l2-scenario.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l3-core-job.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l4-job-map.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l5-forces.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-demand-iceberg-l6-hypothesis.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-four-line-review.md` | status=draft 但 confidence=0.85 |
| `tools\tool-harness-adversarial-tester.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-incentive-28-principle.md` | status=draft 但 confidence=0.85 |
| `tools\tool-jargon-to-value-translator.md` | status=draft 但 confidence=0.85 |
| `tools\tool-kdo-agent-production-checklist.md` | dangling 链接: framework-建模四步法; status=draft 但 confidence=0.88 |
| `tools\tool-leadership-consensus-goal-escalation.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-leadership-exit-consulting.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-leadership-three-stubborn-subordinates.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-lean-premium-service.md` | dangling 链接: tool-lean-stealth-service|偷偷服务 |
| `tools\tool-local-search-repo-datasource-engineering.md` | status 值异常: pending_review |
| `tools\tool-meeting-basic-principles.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-mot-research-method.md` | status=draft 但 confidence=0.85 |
| `tools\tool-open-closed-problem-classifier.md` | dangling 链接: 开放封闭问题分类器, AI 任务形态判断器, open-closed-problem-classifier |
| `tools\tool-openmontage-video-factory.md` | dangling 链接: hongqigong-profile |
| `tools\tool-oral-spray-into-doc-not-chatbox.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-platform-requirement-eight-sections.md` | status 值异常: pending_review |
| `tools\tool-presentation-quality-gate-pipeline.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-private-board-facilitation-sop.md` | dangling 链接: framework-kdo-modeling-methodology|KDO 建模方法论, private-board-facilitation-sop; status=draft 但 confidence=0.85 |
| `tools\tool-prompt-iceberg-demand-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-prompt-jtbd-scenario-coach.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-prompt-usp-quick-scan.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-self-binding-three-strategies.md` | status=draft 但 confidence=0.85 |
| `tools\tool-smart-medicine-cabinet-compliance-checklist.md` | source_refs 中的 src ID 未注册: src_20260613_2286ccfb |
| `tools\tool-strategy-12-word-test.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-activity-scope.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `tools\tool-strategy-capability-matrix.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-competition-traps.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-control-points.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `tools\tool-strategy-five-see-three-set.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-four-layers.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-four-moves.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-gap-analysis.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-map.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-nine-problems.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-pareto.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-risk-management.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `tools\tool-strategy-sentence-formula.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-three-horizons.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-strategy-value-proposition.md` | confidence=0.92 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `tools\tool-three-ring-capability-filter.md` | dangling 链接: manage, 能力准入, capability filter, 三环过滤器, task_20260708_huangyaoshi-capability-hub-phase1; status=draft 但 confidence=0.85 |
| `tools\tool-token-economy-mvp-five-steps.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-trr-maturity-scale.md` | status=draft 但 confidence=0.85 |
| `tools\tool-value-teaching-three-stage.md` | status=draft 但 confidence=0.85 |
| `tools\tool-versioned-iteration.md` | status=draft 但 confidence=0.85 |
| `tools\tool-yb-cross-quadrant-prompt-framework.md` | dangling 链接: framework-kdo-modeling-methodology|KDO 建模方法论; status=draft 但 confidence=0.85 |
| `tools\tool-yihang-agent-config-7steps.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yihang-dual-triangle-canvas.md` | dangling 链接: 一行双三角画布, 一堂双三角, 双三角画布, dual-triangle-canvas, 人机协作双三角; status=draft 但 confidence=0.88 |
| `tools\tool-yihang-dual-triangle-oral-spray.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yihang-dual-triangle-xray-deconstruct.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-assisted-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-assisted-organize.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-monitoring-alert.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ai-report-drafting.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-amazon-bestseller.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-anonymous-product-testing.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-app-store-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-app-store-review.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-baidu-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-behavioral-observation.md` | dangling 链接: tool-yitang-field-research|实地调研/蹲店, tool-yitang-user-interview-5steps|用户访谈五步法, concept-yitang-facts-first|事实优先, framework-yitang-research-weapon-system|调研武器系统; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-bidding-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-bp-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-business-registration-check.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-case-fact-review-checklist.md` | status=draft 但 confidence=0.9 |
| `tools\tool-yitang-case-storyline-selector.md` | status=draft 但 confidence=0.88 |
| `tools\tool-yitang-channel-agent-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-comparable-company-selection.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-competitor-financial-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-conference-networking.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-court-record-search.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-database-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-dialectical-modeling.md` | status=draft 但 confidence=0.85 |
| `tools\tool-yitang-douyin-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-dual-guardrail-system.md` | status=draft 但 confidence=0.87 |
| `tools\tool-yitang-dual-triangle-agent-handoff-protocol.md` | dangling 链接: agent-spec-yitang-dual-triangle-cross-domain-diagnostician, agent-spec-demand-iceberg-coach, agent-spec-yitang-dual-triangle-cross-domain-diagnostician |
| `tools\tool-yitang-dual-triangle-domain-registry.md` | dangling 链接: agent-spec-yitang-dual-triangle-cross-domain-diagnostician, agent-spec-yitang-dual-triangle-cross-domain-diagnostician; status=draft 但 confidence=0.85 |
| `tools\tool-yitang-dual-triangle-scenario-router.md` | dangling 链接: agent-spec-yitang-dual-triangle-cross-domain-diagnostician, agent-spec-yitang-dual-triangle-cross-domain-diagnostician, agent-spec-demand-iceberg-coach; status=draft 但 confidence=0.85 |
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
| `tools\tool-yitang-payment-collection-playbook.md` | dangling 链接: payment-collection-playbook |
| `tools\tool-yitang-pc-web-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-people-network-database.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-change-decision.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-change-identification.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-comm-frequency.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-comm-matrix.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-communication-plan.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-cost-estimation.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-gap-analysis.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-progress-tracking.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-proposal-checklist.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-resource-escalation.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-retro-goal-types.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-retro-value-mining.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-risk-discovery.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-risk-response.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-unblock-techniques.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-project-weapon-library-v1-8.md` | confidence=0.95 但 source 仅 0 个; trust_level=high 但 source 仅 0 个 |
| `tools\tool-yitang-public-information-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-public-sentiment-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-quantity-bold-matrix.md` | status=draft 但 confidence=0.85 |
| `tools\tool-yitang-recruit-user-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-retrospective-canvas.md` | dangling 链接: retrospective-canvas |
| `tools\tool-yitang-review-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-securities-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-shareholder-analysis.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-signup-statistics.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-social-media-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-social-media-monitoring.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-stock-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-supplier-interview.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-supply-chain-research.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-ten-layer-interpretation.md` | status=draft 但 confidence=0.85 |
| `tools\tool-yitang-trend-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weapon-media-search.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weapon-third-party-database.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-web-scraping-research.md` | confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-wechat-group-infiltration.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-wechat-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-weibo-index.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yitang-xiaohongshu-data.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-yizhan-shendeng.md` | status=draft 但 confidence=0.85 |
| `tools\tool-zhu-ai-deliberate-practice-roadmap.md` | status=draft 但 confidence=0.88 |
| `tools\tool-一堂-ABACC叙事法.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-FAB说服法.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-五大转化率范式.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-五种挖触点.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-伏笔式消除法.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-减法排序四招.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-制作仿真三要点.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-动嘴动手动钱成本纪律.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-名利权情动力法.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-心理激励优先机制.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-提假设四大类策略.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-经典故事线框架库.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-表达力火箭模型-执行武器库.md` | dangling 链接: agent-一堂-个人表达力教练 |
| `tools\tool-一堂-讲香双策略.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-阻力三句话心法.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-阻力挖掘方式.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂-马毅阻力消除四部曲.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂五步法-ToB-十八式-checklist.md` | dangling 链接: agent-一堂五步法教练 |
| `tools\tool-一堂五步法-换档检查清单.md` | dangling 链接: agent-一堂五步法教练; confidence=0.9 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |
| `tools\tool-一堂五步法-段位升级三部曲.md` | dangling 链接: agent-一堂五步法教练 |
| `tools\tool-个人学习方法-修炼闭环自检清单.md` | dangling 链接: agent-个人学习方法教练 |
| `tools\tool-团队复盘引导清单.md` | confidence=0.92 但 source 仅 1 个; status=draft 但 confidence=0.92; trust_level=high 但 source 仅 1 个 |
| `tools\tool-月白-MOC.md` | status 值异常: pending_review |
| `tools\tool-月白-设计文件八要素命名法.md` | dangling 链接: concept-structured-naming-as-infrastructure|于陆的命名哲学 |
| `tools\tool-水水-管理决策权重偏差.md` | trust_level=high 但 source 仅 1 个 |
| `tools\tool-泛产品设计-出牌指南.md` | dangling 链接: yt-model-pan-product-climbing-map|十年爬山地图, yt-model-pan-product-execution-toolkit|执行工具箱, yt-model-pan-product-aesthetic-toolkit|审美工具箱, yt-model-pan-product-demand-toolkit|泛产品设计·需求工具箱（13 张卡牌）, yt-model-pan-product-36-strategies|36 计总图 |
| `tools\tool-泛产品设计-需求可行性四字诀.md` | dangling 链接: tool-泛产品设计-出牌指南|L1 出牌序列, yt-model-pan-product-demand-toolkit|需求工具箱, yt-personal-pan-product-practice|个人泛产品设计实操, yt-entrepreneur-five-step-method|一堂五步法, tool-泛产品设计-出牌指南|出牌指南 |
| `tools\yt-business-model-canvas.md` | dangling 链接: business-model-canvas |
| `tools\yt-demand-segmentation-canvas.md` | dangling 链接: demand-segmentation-canvas |
| `tools\yt-pitch-metaphor.md` | trust_level=high 但 source 仅 0 个 |
| `tools\yt-pitch-quantification.md` | trust_level=high 但 source 仅 0 个 |
| `tools\yt-pitch-storytelling.md` | trust_level=high 但 source 仅 0 个 |
| `tools\yt-product-kernel-canvas.md` | dangling 链接: business-model-canvas, demand-segmentation-canvas, product-kernel-canvas |
| `tools\yt-tool-unit-model-benchmark.md` | dangling 链接: tool-demand-iceberg-l1-user|需求冰山, tool-yitang-research-unit-model|单元模型, ai-collaboration-mindset-shift|AI协作, learning-thinking|学习方法论 |
| `tools\yt-tool-unit-model-construction.md` | dangling 链接: tool-demand-iceberg-l1-user|需求冰山, tool-yitang-research-unit-model|单元模型, ai-collaboration-mindset-shift|AI协作, learning-thinking|学习方法论 |
| `tools\yt-tool-unit-model-dynamic.md` | dangling 链接: tool-demand-iceberg-l1-user|需求冰山, tool-yitang-research-unit-model|单元模型, ai-collaboration-mindset-shift|AI协作, learning-thinking|学习方法论 |
| `tools\yt-tool-unit-model-selection.md` | dangling 链接: tool-demand-iceberg-l1-user|需求冰山, tool-yitang-research-unit-model|单元模型, ai-collaboration-mindset-shift|AI协作, learning-thinking|学习方法论 |
| `workflows\workflow-cross-agent-fact-dispute.md` | type 值异常: workflow; dangling 链接: dk-P15-false-completion-report（计划卡，未产出） |
| `workflows\workflow-kdo-agent-production-pipeline.md` | type 值异常: workflow |
| `workflows\workflow-yitang-project-four-step-loop.md` | type 值异常: workflow |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。