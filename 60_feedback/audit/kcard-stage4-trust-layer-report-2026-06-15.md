# 30_wiki 阶段 4 可信度分层审查报告

**报告日期**：2026-06-15  
**审查角色**：王语嫣  
**覆盖范围**：30_wiki 全库 1339 张卡片  
**本阶段目标**：识别 confidence/trust_level/reviewed_by 等可信度元数据问题，批量修正可规则化的问题。

---

## 一、问题统计

| 问题类型 | 数量 | 是否可批量自动处理 |
|---|---|---|
| 正文已批准但 reviewed_by 仍为 pending | 68 | 部分可（需确认 reviewer） |
| confidence ≥ 0.90 但 source < 2 | 13 | 可 |
| 缺失 confidence | 968 | 可（按 status/source 填充默认值） |
| 缺失 trust_level | 1095 | 可（按 status/source 填充默认值） |
| confidence ≥ 0.85 但 trust_level 为 low/medium-low | 0 | 可 |
| 日期字段不一致 | 517 | 需人工复核 |

---

## 二、正文已批准但 reviewed_by 仍为 pending

| 文件 | 检测到的批准人 | 当前 status | 建议操作 |
|---|---|---|---|
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-course-to-skill.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kdo-flywheel.md` | 欧阳锋 | stable | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c1-cjk-regex-silent-fail.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c11-hongqigong-skip-review.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c2-dual-status-machine.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c3-txt-ingest-skip.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c4-selfcheck-superseded.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c5-todo-false-positive.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c6-large-source-overflow.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c7-auto-backup-conflict.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c9-batch-trigger-garbage.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f1-regex-on-cjk.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f10-broken-source-refs.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f11-encyclopedia-style.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f12-builder-context-deadlock.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f13-handwritten-yaml-parser.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f14-accuracy-measurement-mismatch.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f2-txt-ingest-skip.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f3-state-json-race-condition.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f4-wrong-workdir.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f5-stale-feedback-ref.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f6-cjk-skeleton-corruption.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f7-surface-translation.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f8-phony-wikilink.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f9-generic-critique.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p1-model-switch-env.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p10-oral-ban.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p11-regex-cutoff.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p13-token-burn.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p14-zombie.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p15-unverified.md` | 欧阳锋 |  | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p16-validate-reads-state-json.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p17-accuracy-gap.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p18-yaml-parser.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p19-quote-yaml.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p2-tmux-cache.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p20-bigram-fail.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p3-auth-cache.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p4-batch-format-empty.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p5-cc-connect-config.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p6-session-resume-fail.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p7-ocr-skip.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p8-toolkit-forget.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p9-glob-miss.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\data-curator-role-division.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\fix-data-curator-parse-bug.md` | 欧阳锋 | pending | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\high-density-composite-compilation-strategy.md` | 黄药师 | revised | 更新 reviewed_by 为 黄药师，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-data-alignment-response.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-extractor-upgrade-report.md` | 老顽童 | draft | 更新 reviewed_by 为 老顽童，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-tagging-and-scope-proposal.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\kdo-15-dimension-label-spec.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\kdo-ec-industrialization-migration-proposal.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\label-accuracy-standard-alignment.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\labeling-final-consolidation.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\labeling-research-alignment.md` | 老顽童 | draft | 更新 reviewed_by 为 老顽童，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\ouyangfeng-data-alignment-response.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\ouyangfeng-labeling-research-review.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-deep-synthesis-infrastructure.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-kdo-flywheel-infrastructure.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\sprint-6-cli-gap-proposal.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\three-party-data-alignment.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\七件事集团.md` | 欧阳锋 | stable | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-decision-abcd-model.md` | 欧阳锋 | enriched | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\agent-native-card-design.md` | 欧阳锋 | active | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\graph-rag-retrieval-layer.md` | 欧阳锋 | stable | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\kdo-watch-health-check-layer.md` | 欧阳锋 | proposed | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\sprint-2-gate-enrich-evidence.md` | 欧阳锋 | draft | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\一堂方法论体系总图.md` | 欧阳锋 |  | 更新 reviewed_by 为 欧阳锋，status 视情况改为 approved/reviewed |

---

## 三、高置信低来源卡片

| 文件 | confidence | source 数量 | status | 建议操作 |
|---|---|---|---|---|
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-personal-growth-map-creation.md` | 0.9 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-ai-info-literacy.md` | 0.9 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-decision-hygiene.md` | 0.9 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI对话上下文隔离.md` | 0.9 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-three-virtues.md` | 0.9 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-scale-economy-weapon-library.md` | 0.9 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\framework-logic-cleanliness-five-levels.md` | 0.9 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\model-quality-four-levels.md` | 0.92 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\sales-pitch-bias-patterns.md` | 0.92 | 1 | enriched | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\smart-device-foodservice-automation.md` | 0.95 | 1 | enriched | 下调 confidence 至 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\skill-note-keyword-bolding.md` | 0.9 | 1 | draft | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\skill-note-layer-constraint.md` | 0.92 | 1 | draft | 下调 confidence 至 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\skill-note-one-line-one-point.md` | 0.95 | 1 | draft | 下调 confidence 至 0.85 |

---

## 四、缺失 confidence 的卡片

| 文件 | status | source 数量 | 当前 trust_level | 建议 confidence |
|---|---|---|---|---|
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-ether-online-acquisition.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-jh-yitang-vs-sqlhelper.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-milktea-five-step.md` | reviewed | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-shampoo-product-kernel.md` | reviewed | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-treadmill-demand-analysis.md` | reviewed | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-ai-partner.md` | draft | 4 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-motivation-map-12-versions.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-poker-deck-roi.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-prd-checklist-evolution.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-AI高考志愿-kernel-mismatch.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-无人餐厅-hypothesis-failure.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-陈贤敏汉堡-hypothesis-validation.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-conversion-hacker-skill.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-course-to-skill.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-from-assignment-to-tool.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-skill-ab-test.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-广冷电子-hx-smj.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-ai-workspace-chaos.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-focus-prompt-design.md` | draft | 4 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-from-zip-to-five-layers.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-skill-market-problem-validation.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-skills-market.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-ui-design-constraint-evolution.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\2026-05-17-深夜感想.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-collaboration-mindset-shift.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-landing-scene-selection.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-learning-closed-loop.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-native-五层进阶从答案到效率到作品到产品到系统.md` | “enriched” | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-俱乐部人和-ai-协作-五层结构.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-俱乐部人和-ai-协作-参考案例对比一堂-vs-sql-helper.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc文创案例设计课leo文创ip从0到1全流程.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc设计基础01ai生图原理与提示词基本功.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc设计师实操培训01口喷设计范式与电商ai设计全流程.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aima-ai思维卡-外部链接归档.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai数据理解第一课.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai时代判断力口述.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\business-analysis.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\business-research-skill-oscar-13-weapon-system.md` | enriched | 0 | high | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-mckinsey-issue-tree.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-mckinsey-mece.md` | draft | 3 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-business-prediction.md` | deprecated | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-hypothesis-driven-business-methodology.md` | reviewed | 5 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-kernel-iteration.md` | reviewed | 1 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-kernel-validation.md` | reviewed | 1 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-key-assumptions.md` | reviewed | 1 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-product-kernel.md` | reviewed | 3 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-半肥猫-ai-learning-toolification-methodology.md` | draft | 3 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-纪浩-ai-collaboration-five-layer.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-纪浩-ai-collaboration-methodology.md` | draft | 3 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\contingency-decision-making.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\course-to-skill-conversion.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\data-labeling-best-practices-report.md` | draft | 4 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\deepseek-v4-在知识管理系统中的应用.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\design-ai-image-generation.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ec工业化规范手册-v2.8.0.md` | enriched | 1 | high | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\EC工业化规范手册.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\find-old-do-small.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\graph-rag.md` | enriched | 0 | medium | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\HIS系统开发实现方案-架构师指南.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\HIS系统深度调研.md` | reviewed | 1 | medium | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kdo-flywheel.md` | stable | 0 | (empty) | 0.9 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kdo-yaml-frontmatter-safety.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kdo_product_design_agent_final.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kimi-深度调研集群方法论-deep-research-swarm.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\knowledge-delivery-os-快速体验指南-飞书云文档.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\knowledge-error-self-exposure.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\learning-thinking.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\meta-prompt-eng.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\obsidian-kdo-内容产出工作流-产品设计大纲.md` | superseded | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ai俱乐部-人和ai协作-纪浩-五层结构-图片01.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ocr_screenshot2.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ocr_snipaste_2026-05-15_21-39-40.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-screenshot1.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-screenshot2.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-truman的个人成长五步法.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-truman的选择两条职业成长路线.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-truman自用的ai-featureset.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-提问工程化.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-提问进化路线图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai清单体笔记系统故事线-truman-图片01.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai清单体笔记训练段位图-truman-图片02.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-tcpr模型-皇冠模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-y模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-全景图muse模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-双三角模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-提问刻意练习画布.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo-全景策略.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo完整清单.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学提问刻意练习.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-表达力火箭模型-执行武器库.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-表达力火箭模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-解放思想.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香十指模型-超级武器库.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香基本功-十指模型修炼地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香基本功.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-课程清单.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-人机协作-双三角模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-创业必修-课程清单.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-abcd策略模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-tcpr底层网络协议.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-修炼地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-动态预测.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单sku模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单商圈模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单城市模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单客户模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单履约模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单柜子模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单用户模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单订单模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单销售模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单门店模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-基准值.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-壁垒预判.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-外部对抗地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-多模型情况.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-学练用.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄01.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄02.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-扭蛋机案例.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找全成本实操难点.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找单元模型实操难点.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找基准值实操难点.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-斧子尺子梯子.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-斧子尺子梯子详解.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-最简单元模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-段位专家.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-示例.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-示例01.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-规模对抗实操难点.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-规模经济对抗武器库.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-象限分析法.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-个人地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-个人地图_conv.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-创业地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-创业地图_conv.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-管理地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-管理地图_conv.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-案例拆解-课程清单.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-泛产品设计-十年苦练30招.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例01.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例02.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例03.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例04.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi高阶训练全景图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-x型y型决策习惯对比.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-一堂双三角磨合追求-从入门到无限进步.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-人机协作决策.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-关键假设abcd模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-关键训练清单重要.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-决策三角形.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-发现决策.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-商业模式-完整财务公式决策.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-个人.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-企业.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-团队.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l1优先级定性.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l2部分定量.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l3定量公式.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l4-案例01.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l4严格财务公式.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-你的业务是一次抽样实验.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-决策经验值.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例01.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例02.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例03.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例04.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例05.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例06.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-稀缺机会窗口.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-稀缺资源清单.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-项目方案评估三角形.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-高度-两种典型的思考习惯.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-高水平共识曲线重要.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-管理必修-课程清单.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-高阶体系探索营-三种咨询可能性.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂doc-单元模型-十大单元模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型-科学成事道理.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型steps策略集.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型实操工作流.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂个人地图高潜力成长者修炼全景图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂五步法-产品内核画布.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂五步法画布.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂产品内核-十大典型指标.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂刻意练习十年成长指数.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂提炼过的因果模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂最佳转化率动力曲线图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计-十年修炼爬山地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计-多出牌多练习.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计36计-全套地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂深度复盘冰山图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂转化率-10大容易浪费的触点.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂进步大地图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂进步大地图_compressed.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-优秀泛产品设计者的自我修养.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-婚礼操盘-用户和场景.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-婚礼规划.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-审美提升的层级.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004746_32_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004751_33_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004755_34_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004758_35_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004801_37_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004802_38_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004804_39_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004806_40_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004811_41_32.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践建模.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践收集.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践池子.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-美好作品想象.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美工具箱指南.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-一堂五步法.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-动力阻力.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-场景推演.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-多视角思考.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-峰终定律.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-惊喜公式.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-用户分层.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-用户视角.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-行业分析画布.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-需求挖掘.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-项目背景分析.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-roi分析.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-业务建模.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-低成本测试mvp.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-假设拆解.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-内核和边界.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-努力仿真.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-十倍速验证.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-善用佳软.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-复盘迭代.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-攻坚会.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-灵感闪现.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-管理三段论.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-解放思想.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-设计原则.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-逻辑mece.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-酝酿式打磨.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-里程碑拆解.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-风险管理.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-需求工具箱指南.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计的应用场景示意图.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计者的三大自我修养.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计者的自我修养.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计落地工具篇指南.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计落地篇.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-萃取总结.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-顶级产品追求的方向-乔布斯.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-项目背景问题思考的8个维度.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-预判模型.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\paddleocr-skill.md` | enriched | 0 | high | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\pilot-atomic-chunk-comparison.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\prd-as-ai-instruction.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\product-ux.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\research_methodology.md` | superseded | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-1视角升级思考法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-ai-workspace-setup.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-evidence-check.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-four-elements-validation.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-info-literacy-three-layer.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-landing-five-steps.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-narrative-test.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-old-small-checklist.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-oral-spray-input.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-parallel-validation.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-prd-for-ai.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-problem-question-check.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-problem-validation.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-purpose-bias-check.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-research-five-steps.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-scene-four-elements.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-system-redundancy.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-voice-input-doubao.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai辅助学习.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-cognitive-bias-12-check.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-decision-delay-intuition.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-decision-outside-view.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-first-principles-assumption-classify.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-mece体系框架法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-react行动推理循环.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI场景探索STAR模型.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI工具选型决策.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI时代IPO模型重构.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI时代提示词优化法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI能力分层学习路径.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI辅助思考伙伴养成.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI输出审慎判断与交付确认.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-Feature特性层训练法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-Skill全生命周期管理.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-XY-Problem识别与真实问题定位.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-上下文质量管理（AI协作）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-个人判断力系统建设（达克效应应对）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-人在环渐进自动化策略.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-低质量动作识别与拒绝.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-信息输入持续补全（防AI错误累积）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-判断力产品化与系统赋能.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-双三角模型应用.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-复杂项目AI落地稳定性保障.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-多Agent通信协作方案.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-开源模型与商业模型融合方案.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-技术社区严肃提问法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-提示词优化底层方法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-数学题与语文题区分法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-本地记忆与云端记忆管理.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-知识库最佳实践构建.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-短视频自动化上传工作流.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-科学提问法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-职场异步协作提问法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-语义对齐沟通法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-问题定义澄清法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-business-prediction-15-char.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-five-step-validation.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-hypothesis-validation-three-axe.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-kernel-three-questions.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-product-kernel-add-subtract.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-product-kernel-canvas.md` | draft | 3 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-spectrum-positioning.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-三层目标对齐法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-三阶追问法穷尽决策要素.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-专家访谈十步法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-专家访谈学习.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-专题笔记整理.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-专题笔记脑图整理法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-主动摘要压缩上下文.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-人生红点战略对齐.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-从案例中学习.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-从案例中学习正反案例法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-代入场景推演要素法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-任务拆解为工作流.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-体系框架构建.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-使用优先级快筛卡锁定核心矛盾.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-使用概念辨析卡区分易混淆概念.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-六维窗口期扫描法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-分享输出检验法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-分层标注重点信息.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-创始人二当家分工协作模式.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-制作行业化要素检查清单.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-动手建模提炼.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-动手建模法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-区分获客渠道计算单元roi.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-ai-research-validation.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-course-to-skill-workflow.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-优先使用官方权威信源做证据.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-判断课程是否值得做成Skill.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-动态读取-向量化管理迭代知识.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-告诉AI当前日期限制数据时效.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-将学习成果沉淀为PRD文档.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-按语义切分文档做向量化.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-清洗资料为Markdown格式喂给AI.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-用AI做结构化用户调研.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-用Skill做对比测试验证效果.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-用YAML格式做知识库原子化标签.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-设计Skill的评分规则与风险边界.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-课程Skill化的八步工作流.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-边学边练边沉淀的AI学习法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-追问AI证据并标注信源.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-飞书多维表格-自建机器人做团队数据协同.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-反向提示获取优化建议.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-反向教学深化理解.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-反向记录整理思路.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-反向采访挖掘深度.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-四层联系建立法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-城市合伙人模式复制能力.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-增强数据供给.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-复盘推演法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-复盘推演练习.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-多模型对比抽卡.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-多源输入法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-多轮确认防偏差.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-对标借鉴他人决策维度.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-寻找学习教练法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-封装可复用skill.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-将未中标成本纳入循环计算真实投标成本.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-应用人员降级公式实现标准化.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-建立知识联系.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-建立策略-要素映射表设计对抗策略.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-快招品牌总部模拟调研.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-思维链显化推理.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-思维验证交叉检验.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-执行对标研究三步法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-按分阶练习路径渐进掌握方法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-按图索骥改良外部模板.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-按月份摊销收入成本做计划.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-推行分层标准化策略.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-提升笔记练习频次的方法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-提示词结构化迭代.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-敏捷发布快速迭代搭建体系.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-数据分层供给.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-80分效率设计策略.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-A-B双轨反推模式选择.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC产品白底图制作.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC人群画像驱动详情页规划.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC反向拆解法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC文字大小精确控制.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC模型选型决策法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC橱窗陈列设计流程.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC海报信息优先级排序法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC生成人物证件照.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC设计作业复盘法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC餐饮海报优化一抽流.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI一句话改图尺寸.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI人物特征精准描述法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI去字-稿定设计加字工作流.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI去文字-稿定设计快速出图法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI图片印刷落地预处理.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI图片去文字处理.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI图片风格逆向提取（抄图法）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI图生图尺寸快速转换.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI对话式海报修改（免PS）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI对话情绪管理法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI工艺图人工复核法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI平台算法咨询法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI归纳共性描述法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI抽卡效率控制法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI提示词精准约束法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI改图指令精细化.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI智价比评估决策.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI模型选择决策法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI模型选择策略.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI海报快速生成法（15分钟无PS）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生图与图生图决策法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成IP表情包.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成图小字控制法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成图片排版控制-尺寸优先法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成棉花娃娃形象.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成电商白底图.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI电商图人工过审处理.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI精准替换产品技巧.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI自动生成多语种专业名词提示词.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计-质价比-决策框架.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计三段式里程碑流程.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计严苛批评法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计反馈萃取法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计底层逻辑：从设计到作图到改图.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计落地文件标准生成.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计里程碑拆解法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI课程内容深度梳理法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI质价比评估方法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI逆向反推描述法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI需求拆解咨询法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI高清重绘去模糊.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-PPT全AI生成工作流.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-PPT内容框架AIGC生成法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-PPT风格锁定工作流.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-PS图层规范管理.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-RGB转CMYK印刷预检.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-RGB转CMYK色彩校准法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-Token效价比决策公式.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-Token效价比决策法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-Token智甲比控制法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-一抽流改图法（自然语言精准许愿法）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-一抽流长提示词写作法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-三步作业反馈法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-产品反光修复术.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-产品替换式场景合成法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-产品白底图标准化制作.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-产品风格选择：测而非定.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-价格带视觉策略匹配.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-供应商信息对齐清单法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-像素图高清重绘修复法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-光影灰度控制能力构建.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-关键要素提取改图法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-具体化优点萃取与复用.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-分层自洽海报生成法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-分步迭代改图法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-创作与执行双模式切换.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-包材工艺参数核对法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-卖点可视化海报设计法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-印刷DPI标准设置.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-叙事性场景海报构建.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-口喷作图工作流.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-口喷式AIGC设计法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-口喷式设计工作流.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-口述作图法（口喷设计）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-后台数据AI诊断法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-商业项目AI模型选型决策.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-图像信息逆向解析训练.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-图片逆向反推提示词法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-图片逆向提示词提取.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-图生图产品替换与场景合成.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-圈图指定修改法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-基于基础形象做动作延展（1到10）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-基于白底图做动作延展.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-基于需求拆解找设计参考.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-多窗口并行工作法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-多语种专业名词提示词策略.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-多语言提示词精准法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-多语言提示词降幻觉法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-官方提示词最佳实践迁移.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-实物包装产业链实践.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-实物包装落地训练法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-审美刻意练习法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-封面情绪转化法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-小红书双重搜索法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-小红书封面趋势判断法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-小红书平台内容策略：从美图经济到沙雕梗图.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-工厂对接信息清单制作.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-左手Cubox右手里程碑学习法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-左脑画面描述训练法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-强约束画面尺寸比例.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-微信公众号封面AI设计-尺寸强约束法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-手机外设计逻辑切换法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-手绘草稿AI转化工作流.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-批量生成多视角素材.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-找AI要平台专属方法（模型对抗法）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-控制产品画面尺寸比例.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-提示词优化：信息流海报文字修复.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-提示词长度控制法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文件命名与图层命名规范.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文件命名与存档规范（口述暗示）.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文件命名与平台适配规范.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文创产品AI设计到生产的卡点预判.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文创材质成本调研与精益选择.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文创材质调研与精益选择.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-新媒体平台流量逻辑-问平台亲儿子AI法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-新媒体热点物料快速迭代法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-新手设计师基本功训练法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-普通人AI快速上手法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-普通人AI设计80分法则.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-智能扩图-拓图双方案.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-替换大法改图.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-最佳实践素材收集法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-服务体验类去AI感设计.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-未知领域审美建构法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-模型性价比选型决策.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-模型识别与边界测试法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-正向反馈强化AI生成.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-泛产品设计能力迁移法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-海报二维码快速替换法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-海报文字错误修复法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-灵感画布建立法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-烧Token快速积累体感.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-用AIGC做设计专家批评复盘.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-用一堂方法论找最佳实践并拉满执行.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商场景图三类分类法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商场景图三类构建法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商白底图生成与场景图匹配.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商白底图生成与高清处理.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商白底图生成与高清重绘.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商详情页起承转合架构法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-眼高手低训练法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-眼高手低转化法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-短视频封面-音量战争-设计法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-短视频封面一秒吸睛法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-短视频封面高亮吸睛法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-社群直播海报利益点提炼法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-竞品图精益替换法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-精准共用提示词撰写.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-精准提示词撰写法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-精准提示词消除模型幻觉.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-精准改图提示词写法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-纳米级抄大师训练法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-线下实体门店设计真实体感验证.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-线下门店设计复杂度评估.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-背景消除与分辨率修复.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-色块分区控制法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-薅AIGC羊毛资源法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-行业配色快速确定法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-表情包风格筛选与确定.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-视角替换专用提示法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计参考图精准定位法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计基本功回归法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计师AI工具习惯切换.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计师AI资产四类型沉淀.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计文件八要素命名法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计素材脱敏处理规范.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计能力蒸馏封装法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计需求口头化表达法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计项目MVP拆解法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计项目里程碑拆解法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-课程资料文件命名规范.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-课程问题预埋法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-资深设计师AI工具切换法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-跨境电商产品图替换法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-醒图人脸精修法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-里程碑思维-找对标优先于做设计.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-里程碑思维拆解设计流程.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-风格不变局部调整.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-风格探索试错法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-餐饮海报AB测试法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-餐饮类线下设计调性把控.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-个人IP的重新定义与输出策略.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-内容创作中的观察训练法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-判断工作价值的交易成本视角.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-短视频-脱口秀创作：从-风格-自然-的无效建议中解脱.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-销售闭环验证：从0到1的重新定义.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-阅读重读机制：与书籍的-因缘-相遇.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-面对过去错误的平静心法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-模型匹配调度.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-模型组合调用.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-保持系统冗余.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-利用叙事驱动决策.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-利用基因漂变视角.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-区分风险与不确定性.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-接受发散性世界观.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-构建自利叙事.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-用感性维度构建溢价.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-练习坦然说不知道.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-警惕概率虚妄安全感.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-警惕错误归因.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别关键偶然因素.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别数据折磨陷阱.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别模型局限性.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别自证预言陷阱.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别超级传播者风险.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别饥饿效应.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-避免原生家庭万能归因.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-降低故事逻辑要求.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-深度分层学习.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-清单小抄制作.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-清单小抄工具箱法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-清单式笔记法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-渐进式披露上下文.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-现场建模式萃取笔记.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-用topdown方式整理内化笔记.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-用旗舰店替代纯招商投入.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-用清单体记备忘笔记.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-知识库团队管理.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-知识树存储记忆法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-稀缺资源机会成本比对法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-立即实践转化法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-Agent开工检查单制作法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-Agent技能市场设计法.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI使用边界管理法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI工作空间与导诊台设计法.md` | draft | 3 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI工具脚本化约束.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-Do-first-PDCA渐进迭代法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-problem-validation-four-checks.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-Problem与Question区分法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-任务交付物标准化.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-低成本输出验证法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-处理AI生成代码运行异常.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-多视角切换思考法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-新手心态启动法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-日志驱动排查法.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-案例池构建法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-真需求四要素验证法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-线上问题应急值守.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-评估AI从零写UI的可行性.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-识别AI不可维护代码.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-里程碑验证法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-问题导向备课法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-项目启动五问法.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-自我反馈修正笔记姿势.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-自我反馈检验.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-获取他人反馈优化笔记.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-设定管理杠杆率指标评估效率.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-设计对抗效果追踪看板.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-费曼学习法三句话提炼.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-费曼学习法实践讲香课题.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-费曼简单提炼法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-辩证讨论法.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-辩证讨论深化.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-逐字稿练习演讲.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-通过综合案例沙盘走通全流程.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-通过请吃饭获取行业内部资料.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-遵循规模前倾原则设计组织架构.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-采用滚动预测机制.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-项目复盘基本功.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AIGC项目ROI评估.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI任务拆解提升控制度.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI搜索公网数据增强（合规边界）.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI答疑运营风格适配.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI能力团队复制.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地前置条件验证.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地四阶段验证法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地场景筛选-四有新人法则.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地场景识别-拆工作流找场景.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地场景识别与拆分.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地能力内化训练.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地认知速成-最佳实践学习法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI项目上线-先平行再独行.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI项目需求拆解筛选.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-RPA数据整合法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-业务问题AI化拆解-餐饮设计案例法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-中国企业AI落地五步法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-低置信度样本黄金漏斗处理.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-公寓获客自跑通原则.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-关键假设识别与验证.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-减少输入噪音法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-判断标准快速产出法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-工作流优先于AIGC的决策方法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-工作流拆解找场景.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-平台模式验证法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-成为首位F工程师.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-数字员工FD拆解落地.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-数据存储架构选择.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-数据标注正确法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-时间序列大模型场景识别.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-最小场景优先落地法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-深度沉浸需求挖掘.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-痛点驱动的数字化.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-知识库-回答技巧双建设.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-视频转化关键要素标注校验.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-销售智能体体系搭建路径.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-隐性知识萃取与模型化.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-隐私安全分层解决.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-需求创造验证法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-风口痛点识别法.md` | needs-review | 0 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\sprint-2-门禁举证验收.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\structured-ai-workspace.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\tinyfish-agentic-web-infrastructure.md` | enriched | 0 | high | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\tools-workflows.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\truman-perspective-skill.md` | enriched | 0 | high | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\voice-input-doubao.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\web-scraping-三剑客-scrapling-crawl4ai-firecrawl.md` | enriched | 0 | high | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\writing-content.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown.md` | enriched | 1 | medium | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yitang-course-map.md` | stable | 0 | (empty) | 0.9 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yitang-huazong-ama-by-industry.md` | stable | 1 | (empty) | 0.9 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yitang-huazong-ama-summary.md` | stable | 1 | (empty) | 0.9 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-case-mandatory-cases.md` | reviewed | 0 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-basic-skills.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-company-culture.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-conversion-hacking.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-finance-basics.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-founder-role.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-goal-management.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-leadership-levels.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-onboarding.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-partnership-equity.md` | enriched | 0 | medium | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-project-management.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-decision.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-hiring.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-meetings.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-strategy-meeting.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-team-knowledge.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-deliberate-practice-four-elements.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-action-camp-launch.md` | reviewed | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-weaponry-course.md` | reviewed | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-p-role-prompt-design.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-contrast-analysis.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-key-elements.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-problem-solving.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-target-tradeoff.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-timeline.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-system-course-catalog.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-system-course-map-lecture.md` | reviewed | 0 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-equity-checklist.md` | redirect | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-onboarding-90day.md` | redirect | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-project-health-radar.md` | redirect | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-overview.md` | reviewed | 5 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\互联网医院模式深度调研报告.md` | enriched | 1 | high | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\人机协作决策-双三角模型.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\保达云诊所深度调研报告.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\在设计小伙伴的反馈还挺好的.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\存储策略.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\学会提问在信息洪流中锻造批判性思维的利刃.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\开源HIS系统代码深度分析报告.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\数据标注维度最佳实践调研报告.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\紫鲸ai_智能体工作流平台_深度分析与产品设计.md` | superseded | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\紫鲸ai智能体工作流平台.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\老朱的水感-2026年5月.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\街顺app全面调研报告.md` | reviewed | 1 | medium | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\视觉prompt三层操作系统-srom-visual-os.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\诊所o2o外卖平台业务深度调研报告.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\轻量级诊所HIS调研全清单.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\那今天不会.md` | enriched | 1 | (empty) | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\鑫港湾his系统分阶段整改报告.md` | enriched | 1 | high | 0.8 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ai-entrepreneur-technical-blindspot.md` | draft | 3 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ai-judgment-human-responsibility.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ai-judgment-programmer-paradox.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c1-cjk-regex-silent-fail.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c10-batch-tool-no-dry-run.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c11-hongqigong-skip-review.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c2-dual-status-machine.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c3-txt-ingest-skip.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c4-selfcheck-superseded.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c5-todo-false-positive.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c6-large-source-overflow.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c7-auto-backup-conflict.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c8-format-complete-mind-empty.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c9-batch-trigger-garbage.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ef-001-sn74lvc2g07-open-drain.md` |  | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ef-002-bom-version-async.md` |  | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ef-003-hand-soldering-bom-divergence.md` |  | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ef-004-missing-diagnostic-firmware.md` |  | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f1-regex-on-cjk.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f10-broken-source-refs.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f11-encyclopedia-style.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f12-builder-context-deadlock.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f13-handwritten-yaml-parser.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f14-accuracy-measurement-mismatch.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f2-txt-ingest-skip.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f3-state-json-race-condition.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f4-wrong-workdir.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f5-stale-feedback-ref.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f6-cjk-skeleton-corruption.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f7-surface-translation.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f8-phony-wikilink.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f9-generic-critique.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-foresight-tier-skip-illusion.md` | draft | 3 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-jh-llm-time-blindness.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-lz-ai-native-organization.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-lz-code-is-disposable.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-mckinsey-hypothesis-driven-pitfalls.md` | enriched | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-modeling-ai-self-retrospection.md` | draft | 2 | high | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-modeling-timely-review-session-window.md` | draft | 2 | high | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-my-ai-landing-three-barriers.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-note-maximum-common-divisor.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-note-rookie-disaster-veteran-heaven.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-note-surplus-brainpower.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p1-model-switch-env.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p10-oral-ban.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p11-regex-cutoff.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p13-token-burn.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p14-zombie.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p15-unverified.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p16-validate-reads-state-json.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p17-accuracy-gap.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p18-yaml-parser.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p19-quote-yaml.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p2-tmux-cache.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p20-bigram-fail.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p3-auth-cache.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p4-batch-format-empty.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p5-cc-connect-config.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p6-session-resume-fail.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p7-ocr-skip.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p8-toolkit-forget.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p9-glob-miss.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-pseudo-demand-trap.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-signal-cluster-illusion.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-truman-document-is-real-project-is-fake.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-truman-iteration-to-aesthetic-ceiling.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-truman-knowledge-extraction-three-schools.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb1-aigc-mvp-before-ps.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb10-theory-moat-designer.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb11-visual-book-reverse.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb12-ai-image-analysis-replace-training.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb13-zero-shot-style-transfer.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb14-multi-image-commonality.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb15-reverse-image-description.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb16-ecommerce-product-image-vs-lucky-draw.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb17-product-lifestyle-photography.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb18-small-shop-image-mismatch.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb19-visual-strategy-price-match.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb2-llm-muddy-clear-muddy.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb20-ai-eye-high-principle.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb21-ecommerce-pricing-independent-model.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb22-visual-presentation-scene-match.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb23-ai-pre-screen-three-minutes.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb24-ai-poster-de-ai-feeling.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb25-solution-driven-visual-design.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb26-chinese-food-photography-props.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb27-pseudo-layer-evasion.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb28-prompt-expiration-management.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb29-prompt-migrate-copy-first.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb3-diffusion-stepwise-vs-human-holistic.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb30-ecommerce-channel-version.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb31-style-first-controlnet.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb32-doubao-size-composition.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb4-nano-banana-style-reproduction.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb5-style-asset-archive.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb6-midjourney-chinese-text-fix.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb7-design-demand-80-10-10.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb8-file-naming-eight-elements.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb9-cubox-deployment-failure.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yitang-business-formula-plus-times-trap.md` | reviewed | 3 | high | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-一堂-wishful-thinking-kills-startups.md` | draft | 3 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-atomic-no-standard.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-real-business-is-the-engine.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-silky-answer-warning.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-silky-answers-are-dangerous.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-skill-rejection-value.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-ai-cant-design-structure.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-constraint-beats-talent.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-logs-fastest-ignored.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-newbie-can-validate.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-novice-mindset-advantage.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-pdca-starts-from-do.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-problem-vs-question.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-simple-complex-routing.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\yt-note-ai-p-role-not-c-role.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\yt-note-p-c-role-boundary-realworld.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\yt-note-three-level-evolution.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\agent-ecosystem-design.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\data-curator-role-division.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\fix-dark-knowledge-extractor-llm.md` | pending | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\fix-data-curator-parse-bug.md` | pending | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\gold-standard-manual-labels.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\high-density-composite-compilation-strategy.md` | revised | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-data-alignment-response.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-extractor-upgrade-report.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-tagging-and-scope-proposal.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\kdo-15-dimension-label-spec.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\kdo-ec-industrialization-migration-proposal.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\kdo-priority-checklist.md` | draft | 0 | high | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\kdo-protocol-implementation-roadmap.md` | draft | 0 | high | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\label-accuracy-standard-alignment.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\labeling-final-consolidation.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\labeling-research-alignment.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\ouyangfeng-data-alignment-response.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\ouyangfeng-labeling-research-review.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_05858800-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_47264869-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_8001399c-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_85a84b92-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_8ecb74e3-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_97170532-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_ca61cdd7-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_e1e150b9-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260503_f3e9a2b1-improvement-plan.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260531_data-curator-v1.1.md` | superseded | 1 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260531_data-curator-v1.3.md` | draft | 4 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260531_data-curator-v1.md` | superseded | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-ai-domain-mastery-pipeline.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-deep-synthesis-infrastructure.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-graph-rag-star-fix.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-kdo-flywheel-infrastructure.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-prompt-injection-infrastructure.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-yaml-frontmatter-standardization.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\sprint-6-cli-gap-proposal.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\three-party-data-alignment.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\truman-ai-partner-design-analysis.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\Kimi-月之暗面.md` | reviewed | 0 | medium | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\YC-Y-Combinator.md` | reviewed | 0 | high | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\一堂.md` | stable | 0 | (empty) | 0.9 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\七件事集团.md` | stable | 4 | medium | 0.9 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\紫鲸AI.md` | reviewed | 0 | medium | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\鑫港湾.md` | reviewed | 0 | medium | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-maister-trusted-advisor.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-mckinsey-7s.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-mckinsey-hypothesis-driven.md` | enriched | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-mckinsey-mece.md` | enriched | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-minto-pyramid-principle.md` | draft | 2 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-decision-abcd-model.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-unit-model-ladder.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-unit-model-overview.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\projects\互联网医院项目.md` | active | 0 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\projects\诊所O2O项目.md` | active | 0 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\projects\鑫港湾HIS项目.md` | active | 0 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\agent-external-brain-design.md` | enriched | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\agent-native-card-design.md` | active | 0 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\graph-rag-retrieval-layer.md` | stable | 0 | (empty) | 0.9 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\kdo-batch-produce-req014.md` | proposed | 0 | (empty) | 0.65 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\kdo-protocol.md` | draft | 0 | medium | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\kdo-watch-health-check-layer.md` | proposed | 0 | (empty) | 0.65 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\obsidian-git-sync-protocol.md` | draft | 0 | high | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\sprint-2-gate-enrich-evidence.md` | draft | 0 | (empty) | 0.6 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\workflow-knowledge-collision.md` | active | 0 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\一堂方法论体系总图.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\concept-mckinsey-issue-tree.md` | enriched | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\concept-toyota-5-whys.md` | enriched | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-ai-workspace-setup.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-evidence-check.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-landing-five-steps.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-narrative-test.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-old-small-checklist.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-parallel-validation.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-prd-for-ai.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-problem-validation.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-purpose-bias-check.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-question-problem-checklist.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-system-redundancy.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-voice-input-doubao.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\skill-mckinsey-hypothesis-driven-workflow.md` | enriched | 2 | (empty) | 0.85 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-ai-ppt-maker.md` | draft | 1 | (empty) | 0.7 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-ai-assisted.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-benchmark.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-construction.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-dynamic.md` |  | 0 | (empty) | 0.75 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-selection.md` |  | 0 | (empty) | 0.75 |

---

## 五、缺失 trust_level 的卡片

| 文件 | status | source 数量 | 当前 confidence | 建议 trust_level |
|---|---|---|---|---|
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-ether-online-acquisition.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-five-step-fake-vs-real-barriers.md` | enriched | 3 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-five-step-growth-first-lever.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-gudong-tea-shop-foresight.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-jh-yitang-vs-sqlhelper.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-milktea-five-step.md` | reviewed | 2 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-shampoo-product-kernel.md` | reviewed | 2 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-treadmill-demand-analysis.md` | reviewed | 2 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-ai-partner.md` | draft | 4 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-motivation-map-12-versions.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-poker-deck-roi.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-prd-checklist-evolution.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-truman-yitang-foresight.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-xiaolong-ecommerce-foresight.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-AI高考志愿-kernel-mismatch.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-无人餐厅-hypothesis-failure.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-陈贤敏汉堡-hypothesis-validation.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-conversion-hacker-skill.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-course-to-skill.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-from-assignment-to-tool.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-半肥猫-skill-ab-test.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-广冷电子-hx-smj.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-ai-workspace-chaos.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-focus-prompt-design.md` | draft | 4 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-from-zip-to-five-layers.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-skill-market-problem-validation.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-skills-market.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-纪浩-ui-design-constraint-evolution.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\2026-05-17-深夜感想.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-collaboration-mindset-shift.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-landing-scene-selection.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-learning-closed-loop.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-native-五层进阶从答案到效率到作品到产品到系统.md` | “enriched” | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-俱乐部人和-ai-协作-五层结构.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-俱乐部人和-ai-协作-参考案例对比一堂-vs-sql-helper.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc文创案例设计课leo文创ip从0到1全流程.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc设计基础01ai生图原理与提示词基本功.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc设计师实操培训01口喷设计范式与电商ai设计全流程.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aima-ai思维卡-外部链接归档.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai单元模型口述蒋老师.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai数据理解第一课.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai时代判断力口述-3.md` | enriched | 1 | 0.75 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai时代判断力口述.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\anthropic-官方发布创始人手册打造-ai-原生初创公司.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\business-analysis.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-ai-native-organization-five-steps.md` | draft | 1 | 0.8 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-five-step-growth-to-barrier-transition.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-mckinsey-issue-tree.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-mckinsey-mece.md` | draft | 3 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-business-prediction.md` | deprecated | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-hypothesis-driven-business-methodology.md` | reviewed | 5 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-kernel-iteration.md` | reviewed | 1 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-kernel-validation.md` | reviewed | 1 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-key-assumptions.md` | reviewed | 1 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-product-kernel.md` | reviewed | 3 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-半肥猫-ai-learning-toolification-methodology.md` | draft | 3 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-纪浩-ai-collaboration-five-layer.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-纪浩-ai-collaboration-methodology.md` | draft | 3 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\contingency-decision-making.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\course-to-skill-conversion.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\data-labeling-best-practices-report.md` | draft | 4 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\deepseek-v4-在知识管理系统中的应用.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\design-ai-image-generation.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\EC工业化规范手册.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\find-old-do-small.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\HIS系统开发实现方案-架构师指南.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kdo-flywheel.md` | stable | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kdo-yaml-frontmatter-safety.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kdo_product_design_agent_final.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kimi-深度调研集群方法论-deep-research-swarm.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\knowledge-delivery-os-快速体验指南-飞书云文档.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\knowledge-error-self-exposure.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\learning-thinking.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-ai-info-literacy.md` | enriched | 1 | 0.9 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-antifragile-checklist.md` | enriched | 0 | 0.88 | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-cognitive-bias-checklist.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-decision-hygiene.md` | enriched | 1 | 0.9 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-first-principles.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-knowledge-compound.md` | enriched | 0 | 0.82 | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\master-systems-thinking.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\meta-prompt-eng.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\obsidian-kdo-内容产出工作流-产品设计大纲.md` | superseded | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ai俱乐部-人和ai协作-纪浩-五层结构-图片01.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ocr_screenshot2.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ocr_snipaste_2026-05-15_21-39-40.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-screenshot1.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-screenshot2.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-truman的个人成长五步法.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-truman的选择两条职业成长路线.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-truman自用的ai-featureset.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-提问工程化.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-提问进化路线图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai清单体笔记系统故事线-truman-图片01.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai清单体笔记训练段位图-truman-图片02.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-tcpr模型-皇冠模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-y模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-全景图muse模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-双三角模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-提问刻意练习画布.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo-全景策略.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo完整清单.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学提问刻意练习.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-表达力火箭模型-执行武器库.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-表达力火箭模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-解放思想.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香十指模型-超级武器库.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香基本功-十指模型修炼地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香基本功.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-课程清单.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-人机协作-双三角模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-创业必修-课程清单.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-abcd策略模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-tcpr底层网络协议.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-修炼地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-动态预测.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单sku模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单商圈模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单城市模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单客户模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单履约模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单柜子模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单用户模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单订单模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单销售模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单门店模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-基准值.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-壁垒预判.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-外部对抗地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-多模型情况.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-学练用.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄01.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄02.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-扭蛋机案例.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找全成本实操难点.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找单元模型实操难点.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找基准值实操难点.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-斧子尺子梯子.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-斧子尺子梯子详解.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-最简单元模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-段位专家.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-示例.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-示例01.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-规模对抗实操难点.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-规模经济对抗武器库.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-象限分析法.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-个人地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-个人地图_conv.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-创业地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-创业地图_conv.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-管理地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-管理地图_conv.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-案例拆解-课程清单.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-泛产品设计-十年苦练30招.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例01.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例02.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例03.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例04.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi高阶训练全景图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-x型y型决策习惯对比.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-一堂双三角磨合追求-从入门到无限进步.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-人机协作决策.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-关键假设abcd模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-关键训练清单重要.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-决策三角形.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-发现决策.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-商业模式-完整财务公式决策.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-个人.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-企业.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-团队.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l1优先级定性.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l2部分定量.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l3定量公式.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l4-案例01.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l4严格财务公式.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-你的业务是一次抽样实验.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-决策经验值.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例01.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例02.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例03.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例04.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例05.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例06.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-稀缺机会窗口.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-稀缺资源清单.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-项目方案评估三角形.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-高度-两种典型的思考习惯.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-高水平共识曲线重要.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-管理必修-课程清单.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-高阶体系探索营-三种咨询可能性.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂doc-单元模型-十大单元模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型-科学成事道理.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型steps策略集.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型实操工作流.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂个人地图高潜力成长者修炼全景图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂五步法-产品内核画布.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂五步法画布.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂产品内核-十大典型指标.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂刻意练习十年成长指数.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂提炼过的因果模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂最佳转化率动力曲线图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计-十年修炼爬山地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计-多出牌多练习.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计36计-全套地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂深度复盘冰山图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂转化率-10大容易浪费的触点.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂进步大地图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂进步大地图_compressed.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-优秀泛产品设计者的自我修养.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-婚礼操盘-用户和场景.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-婚礼规划.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-审美提升的层级.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004746_32_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004751_33_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004755_34_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004758_35_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004801_37_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004802_38_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004804_39_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004806_40_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004811_41_32.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践建模.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践收集.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践池子.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-美好作品想象.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美工具箱指南.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-一堂五步法.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-动力阻力.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-场景推演.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-多视角思考.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-峰终定律.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-惊喜公式.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-用户分层.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-用户视角.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-行业分析画布.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-需求挖掘.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-项目背景分析.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-roi分析.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-业务建模.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-低成本测试mvp.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-假设拆解.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-内核和边界.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-努力仿真.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-十倍速验证.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-善用佳软.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-复盘迭代.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-攻坚会.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-灵感闪现.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-管理三段论.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-解放思想.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-设计原则.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-逻辑mece.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-酝酿式打磨.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-里程碑拆解.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-风险管理.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-需求工具箱指南.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计的应用场景示意图.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计者的三大自我修养.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计者的自我修养.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计落地工具篇指南.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计落地篇.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-萃取总结.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-顶级产品追求的方向-乔布斯.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-项目背景问题思考的8个维度.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-预判模型.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\pilot-atomic-chunk-comparison.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\prd-as-ai-instruction.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\product-ux.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\research_methodology.md` | superseded | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-1视角升级思考法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-ai-workspace-setup.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-evidence-check.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-four-elements-validation.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-info-literacy-three-layer.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-landing-five-steps.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-narrative-test.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-old-small-checklist.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-oral-spray-input.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-parallel-validation.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-prd-for-ai.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-problem-question-check.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-problem-validation.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-purpose-bias-check.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-research-five-steps.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-scene-four-elements.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-system-redundancy.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-voice-input-doubao.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai辅助学习.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-cognitive-bias-12-check.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-decision-delay-intuition.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-decision-outside-view.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-first-principles-assumption-classify.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-mece体系框架法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-react行动推理循环.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI场景探索STAR模型.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI工具选型决策.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI时代IPO模型重构.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI时代提示词优化法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI能力分层学习路径.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI辅助思考伙伴养成.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-AI输出审慎判断与交付确认.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-Feature特性层训练法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-Skill全生命周期管理.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-XY-Problem识别与真实问题定位.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-上下文质量管理（AI协作）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-个人判断力系统建设（达克效应应对）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-人在环渐进自动化策略.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-低质量动作识别与拒绝.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-信息输入持续补全（防AI错误累积）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-判断力产品化与系统赋能.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-双三角模型应用.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-复杂项目AI落地稳定性保障.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-多Agent通信协作方案.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-开源模型与商业模型融合方案.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-技术社区严肃提问法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-提示词优化底层方法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-数学题与语文题区分法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-本地记忆与云端记忆管理.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-知识库最佳实践构建.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-短视频自动化上传工作流.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-科学提问法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-职场异步协作提问法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-语义对齐沟通法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-Truman-问题定义澄清法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-business-prediction-15-char.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-five-step-validation.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-hypothesis-validation-three-axe.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-kernel-three-questions.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-product-kernel-add-subtract.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-product-kernel-canvas.md` | draft | 3 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-spectrum-positioning.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-三层目标对齐法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-三阶追问法穷尽决策要素.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-专家访谈十步法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-专家访谈学习.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-专题笔记整理.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-专题笔记脑图整理法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-主动摘要压缩上下文.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-人生红点战略对齐.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-从案例中学习.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-从案例中学习正反案例法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-代入场景推演要素法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-任务拆解为工作流.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-体系框架构建.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-使用一页纸速查卡快速调用框架.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-使用优先级快筛卡锁定核心矛盾.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-使用概念辨析卡区分易混淆概念.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-六维窗口期扫描法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-分享输出检验法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-分层标注重点信息.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-创始人二当家分工协作模式.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-制作行业化要素检查清单.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-动手建模提炼.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-动手建模法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-区分获客渠道计算单元roi.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-ai-research-validation.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-course-to-skill-workflow.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-优先使用官方权威信源做证据.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-判断课程是否值得做成Skill.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-动态读取-向量化管理迭代知识.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-告诉AI当前日期限制数据时效.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-将学习成果沉淀为PRD文档.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-按语义切分文档做向量化.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-清洗资料为Markdown格式喂给AI.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-用AI做结构化用户调研.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-用Skill做对比测试验证效果.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-用YAML格式做知识库原子化标签.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-设计Skill的评分规则与风险边界.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-课程Skill化的八步工作流.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-边学边练边沉淀的AI学习法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-追问AI证据并标注信源.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-半肥猫-飞书多维表格-自建机器人做团队数据协同.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-反向提示获取优化建议.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-反向教学深化理解.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-反向记录整理思路.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-反向采访挖掘深度.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-四层联系建立法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-城市合伙人模式复制能力.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-增强数据供给.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-复盘推演法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-复盘推演练习.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-多模型对比抽卡.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-多源输入法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-多轮确认防偏差.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-对标借鉴他人决策维度.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-寻找学习教练法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-封装可复用skill.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-将未中标成本纳入循环计算真实投标成本.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-应用人员降级公式实现标准化.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-建立知识联系.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-建立策略-要素映射表设计对抗策略.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-快招品牌总部模拟调研.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-思维链显化推理.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-思维验证交叉检验.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-执行对标研究三步法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-按分阶练习路径渐进掌握方法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-按图索骥改良外部模板.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-按月份摊销收入成本做计划.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-推行分层标准化策略.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-提升笔记练习频次的方法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-提升笔记阅读舒适度.md` | draft | 1 | 0.84 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-提示词结构化迭代.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-敏捷发布快速迭代搭建体系.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-数据分层供给.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-80分效率设计策略.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-A-B双轨反推模式选择.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC产品白底图制作.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC人群画像驱动详情页规划.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC反向拆解法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC文字大小精确控制.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC模型选型决策法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC橱窗陈列设计流程.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC海报信息优先级排序法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC生成人物证件照.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC设计作业复盘法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AIGC餐饮海报优化一抽流.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI一句话改图尺寸.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI人物特征精准描述法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI去字-稿定设计加字工作流.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI去文字-稿定设计快速出图法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI图片印刷落地预处理.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI图片去文字处理.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI图片风格逆向提取（抄图法）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI图生图尺寸快速转换.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI对话式海报修改（免PS）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI对话情绪管理法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI工艺图人工复核法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI平台算法咨询法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI归纳共性描述法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI抽卡效率控制法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI提示词精准约束法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI改图指令精细化.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI智价比评估决策.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI模型选择决策法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI模型选择策略.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI海报快速生成法（15分钟无PS）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生图与图生图决策法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成IP表情包.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成图小字控制法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成图片排版控制-尺寸优先法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成棉花娃娃形象.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI生成电商白底图.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI电商图人工过审处理.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI精准替换产品技巧.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI自动生成多语种专业名词提示词.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计-质价比-决策框架.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计三段式里程碑流程.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计严苛批评法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计反馈萃取法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计底层逻辑：从设计到作图到改图.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计落地文件标准生成.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI设计里程碑拆解法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI课程内容深度梳理法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI质价比评估方法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI逆向反推描述法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI需求拆解咨询法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-AI高清重绘去模糊.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-PPT全AI生成工作流.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-PPT内容框架AIGC生成法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-PPT风格锁定工作流.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-PS图层规范管理.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-RGB转CMYK印刷预检.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-RGB转CMYK色彩校准法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-Token效价比决策公式.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-Token效价比决策法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-Token智甲比控制法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-一抽流改图法（自然语言精准许愿法）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-一抽流长提示词写作法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-三步作业反馈法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-产品反光修复术.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-产品替换式场景合成法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-产品白底图标准化制作.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-产品风格选择：测而非定.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-价格带视觉策略匹配.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-供应商信息对齐清单法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-像素图高清重绘修复法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-光影灰度控制能力构建.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-关键要素提取改图法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-具体化优点萃取与复用.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-分层自洽海报生成法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-分步迭代改图法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-创作与执行双模式切换.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-包材工艺参数核对法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-卖点可视化海报设计法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-印刷DPI标准设置.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-叙事性场景海报构建.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-口喷作图工作流.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-口喷式AIGC设计法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-口喷式设计工作流.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-口述作图法（口喷设计）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-后台数据AI诊断法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-商业项目AI模型选型决策.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-图像信息逆向解析训练.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-图片逆向反推提示词法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-图片逆向提示词提取.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-图生图产品替换与场景合成.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-圈图指定修改法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-基于基础形象做动作延展（1到10）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-基于白底图做动作延展.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-基于需求拆解找设计参考.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-多窗口并行工作法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-多语种专业名词提示词策略.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-多语言提示词精准法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-多语言提示词降幻觉法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-官方提示词最佳实践迁移.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-实物包装产业链实践.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-实物包装落地训练法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-审美刻意练习法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-封面情绪转化法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-小红书双重搜索法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-小红书封面趋势判断法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-小红书平台内容策略：从美图经济到沙雕梗图.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-工厂对接信息清单制作.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-左手Cubox右手里程碑学习法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-左脑画面描述训练法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-强约束画面尺寸比例.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-微信公众号封面AI设计-尺寸强约束法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-手机外设计逻辑切换法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-手绘草稿AI转化工作流.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-批量生成多视角素材.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-找AI要平台专属方法（模型对抗法）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-控制产品画面尺寸比例.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-提示词优化：信息流海报文字修复.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-提示词长度控制法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文件命名与图层命名规范.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文件命名与存档规范（口述暗示）.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文件命名与平台适配规范.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文创产品AI设计到生产的卡点预判.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文创材质成本调研与精益选择.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-文创材质调研与精益选择.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-新媒体平台流量逻辑-问平台亲儿子AI法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-新媒体热点物料快速迭代法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-新手设计师基本功训练法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-普通人AI快速上手法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-普通人AI设计80分法则.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-智能扩图-拓图双方案.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-替换大法改图.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-最佳实践素材收集法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-服务体验类去AI感设计.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-未知领域审美建构法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-模型性价比选型决策.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-模型识别与边界测试法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-正向反馈强化AI生成.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-泛产品设计能力迁移法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-海报二维码快速替换法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-海报文字错误修复法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-灵感画布建立法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-烧Token快速积累体感.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-用AIGC做设计专家批评复盘.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-用一堂方法论找最佳实践并拉满执行.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商场景图三类分类法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商场景图三类构建法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商白底图生成与场景图匹配.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商白底图生成与高清处理.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商白底图生成与高清重绘.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-电商详情页起承转合架构法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-眼高手低训练法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-眼高手低转化法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-短视频封面-音量战争-设计法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-短视频封面一秒吸睛法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-短视频封面高亮吸睛法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-社群直播海报利益点提炼法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-竞品图精益替换法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-精准共用提示词撰写.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-精准提示词撰写法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-精准提示词消除模型幻觉.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-精准改图提示词写法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-纳米级抄大师训练法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-线下实体门店设计真实体感验证.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-线下门店设计复杂度评估.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-背景消除与分辨率修复.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-色块分区控制法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-薅AIGC羊毛资源法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-行业配色快速确定法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-表情包风格筛选与确定.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-视角替换专用提示法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计参考图精准定位法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计基本功回归法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计师AI工具习惯切换.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计师AI资产四类型沉淀.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计文件八要素命名法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计素材脱敏处理规范.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计能力蒸馏封装法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计需求口头化表达法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计项目MVP拆解法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-设计项目里程碑拆解法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-课程资料文件命名规范.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-课程问题预埋法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-资深设计师AI工具切换法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-跨境电商产品图替换法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-醒图人脸精修法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-里程碑思维-找对标优先于做设计.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-里程碑思维拆解设计流程.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-风格不变局部调整.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-风格探索试错法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-餐饮海报AB测试法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-月白-餐饮类线下设计调性把控.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-个人IP的重新定义与输出策略.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-内容创作中的观察训练法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-判断工作价值的交易成本视角.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-短视频-脱口秀创作：从-风格-自然-的无效建议中解脱.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-销售闭环验证：从0到1的重新定义.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-阅读重读机制：与书籍的-因缘-相遇.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-李诞-面对过去错误的平静心法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-模型匹配调度.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-模型组合调用.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-保持系统冗余.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-利用叙事驱动决策.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-利用基因漂变视角.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-区分风险与不确定性.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-接受发散性世界观.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-构建自利叙事.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-用感性维度构建溢价.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-管理决策权重偏差.md` | enriched | 0 | 0.85 | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-练习坦然说不知道.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-警惕概率虚妄安全感.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-警惕错误归因.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别关键偶然因素.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别数据折磨陷阱.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别模型局限性.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别自证预言陷阱.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别超级传播者风险.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-识别饥饿效应.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-避免原生家庭万能归因.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-降低故事逻辑要求.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-深度分层学习.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-清单小抄制作.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-清单小抄工具箱法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-清单式笔记法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-渐进式披露上下文.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-现场建模式萃取笔记.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-用topdown方式整理内化笔记.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-用旗舰店替代纯招商投入.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-用清单体记备忘笔记.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-知识库团队管理.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-知识树存储记忆法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-稀缺资源机会成本比对法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-立即实践转化法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-Agent开工检查单制作法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-Agent技能市场设计法.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI使用边界管理法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI对话上下文隔离.md` | enriched | 1 | 0.9 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI工作空间与导诊台设计法.md` | draft | 3 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI工具脚本化约束.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-Do-first-PDCA渐进迭代法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-problem-validation-four-checks.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-Problem与Question区分法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-任务交付物标准化.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-低成本输出验证法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-处理AI生成代码运行异常.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-多视角切换思考法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-新手心态启动法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-日志驱动排查法.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-案例池构建法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-真需求四要素验证法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-线上问题应急值守.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-评估AI从零写UI的可行性.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-识别AI不可维护代码.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-里程碑验证法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-问题导向备课法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-项目启动五问法.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-自我反馈修正笔记姿势.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-自我反馈检验.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-获取他人反馈优化笔记.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-设定管理杠杆率指标评估效率.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-设计对抗效果追踪看板.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-费曼学习法三句话提炼.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-费曼学习法实践讲香课题.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-费曼简单提炼法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-辩证讨论法.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-辩证讨论深化.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-逐字稿练习演讲.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-通过综合案例沙盘走通全流程.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-通过请吃饭获取行业内部资料.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-遵循规模前倾原则设计组织架构.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-采用滚动预测机制.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-问题驱动式深度思考笔记.md` | draft | 1 | 0.86 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-项目复盘基本功.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AIGC项目ROI评估.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI任务拆解提升控制度.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI搜索公网数据增强（合规边界）.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI答疑运营风格适配.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI能力团队复制.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地前置条件验证.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地四阶段验证法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地场景筛选-四有新人法则.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地场景识别-拆工作流找场景.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地场景识别与拆分.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地能力内化训练.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI落地认知速成-最佳实践学习法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI项目上线-先平行再独行.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AI项目需求拆解筛选.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-RPA数据整合法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-业务为先的AI中台建设.md` | enriched | 0 | 0.85 | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-业务问题AI化拆解-餐饮设计案例法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-中国企业AI落地五步法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-低置信度样本黄金漏斗处理.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-公寓获客自跑通原则.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-关键假设识别与验证.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-减少输入噪音法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-判断标准快速产出法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-工作流优先于AIGC的决策方法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-工作流拆解找场景.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-平台模式验证法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-成为首位F工程师.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-数字员工FD拆解落地.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-数据存储架构选择.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-数据标注正确法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-时间序列大模型场景识别.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-最小场景优先落地法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-深度沉浸需求挖掘.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-痛点驱动的数字化.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-知识库-回答技巧双建设.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-视频转化关键要素标注校验.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-销售智能体体系搭建路径.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-隐性知识萃取与模型化.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-隐私安全分层解决.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-需求创造验证法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-风口痛点识别法.md` | needs-review | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\sprint-2-门禁举证验收.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\structured-ai-workspace.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\tools-workflows.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\voice-input-doubao.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\writing-content.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yitang-course-map.md` | stable | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yitang-huazong-ama-by-industry.md` | stable | 1 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yitang-huazong-ama-summary.md` | stable | 1 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-case-mandatory-cases.md` | reviewed | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-composite-pan-product-methodology.md` | enriched | 5 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-concept-ai-guard-brain.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-concept-context-engineering.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-concept-weapon-arsenal.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-research-camp.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-spin-selling.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-15-char-mantra.md` | enriched | 4 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-ab-steady-state.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-addition-subtraction.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-deliverables-four-levels.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-probability-engineering.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-ten-fatal-flaws.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-basic-skills.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-company-culture.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-conversion-hacking.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-finance-basics.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-founder-role.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-goal-management.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-leadership-levels.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-onboarding.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-project-management.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-decision.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-hiring.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-meetings.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-strategy-meeting.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-team-knowledge.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-aesthetic-progression.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-conversion-optimization.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-deep-review-iceberg.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-deliberate-practice-growth.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-dual-triangle-competitiveness.md` | enriched | 4 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-entrepreneur-map.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-five-step-canvas.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-ipo-complete-checklist.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-ipo-learning-strategy.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-liberate-thinking-layers.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-management-map.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-muse-ai-framework.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-36-strategies.md` | enriched | 4 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-aesthetic-toolkit.md` | enriched | 6 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-climbing-map.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-demand-toolkit.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-execution-toolkit.md` | enriched | 3 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-three-virtues.md` | enriched | 1 | 0.9 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-personal-map.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-personal-pitch-toolkit.md` | enriched | 3 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-prediction-model.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-product-core-metrics.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-product-excellence.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-progress-map.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-prompt-engineering.md` | enriched | 3 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-questioning-practice-canvas.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-scientific-questioning-map.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-truman-career-routes.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-truman-five-step-growth.md` | enriched | 3 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-y-organization.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-ai-human-division.md` | draft | 2 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-checklist-concept.md` | draft | 3 | 0.88 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-deliberate-practice-four-elements.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-expert-interview-modeling.md` | draft | 2 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-extensive-research-input.md` | draft | 1 | 0.84 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-fact-pattern-insight.md` | draft | 1 | 0.86 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-l4-internalization.md` | draft | 1 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-l6-extraction.md` | draft | 1 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-problem-solving-capability.md` | draft | 1 | 0.88 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-aesthetic-collection.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-aesthetic-imagination.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-aesthetic-modeling.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-aesthetic-pool.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-five-step-method.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-industry-canvas.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-motivation-resistance.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-multi-perspective.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-need-discovery.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-peak-end-rule.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-project-background.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-scenario-walkthrough.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-surprise-formula.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-user-perspective.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-user-segmentation.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-10x-validation.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-business-modeling.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-core-and-boundary.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-design-principles.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-good-tools.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-hypothesis-decomposition.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-idea-spark.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-incubation-polish.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-liberate-thinking.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-logic-mece.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-low-cost-mvp.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-management-trilogy.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-milestone-breakdown.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-realistic-simulation.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-review-iteration.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-risk-management.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-roi-analysis.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-war-room.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-deep-review.md` | enriched | 2 | 0.8 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-ipo-learning.md` | enriched | 2 | 0.8 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-knowledge-extraction.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-02.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-aesthetics.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-concepts.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-exploration.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-practice.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-tools.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-thinking-models.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-y-model-exploration-2.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-y-model-practice.md` | enriched | 1 | 0.8 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-aphorism.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-colloquialization.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-conflict.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-emotionalization.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-materialization.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-metaphor.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-quantification.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-scenarization.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-storytelling.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-sublimation.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-anti-flattery.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-brainstorming.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-engineering-andrew-ng.md` | enriched | 4 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-iterative-prompting.md` | enriched | 2 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-writing-workflow.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-action-camp-launch.md` | reviewed | 2 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-mindset.md` | draft | 1 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-user-jtbd.md` | draft | 1 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-weaponry-course.md` | reviewed | 2 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-checklist-as-ai-protocol.md` | draft | 1 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-p-role-prompt-design.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-contrast-analysis.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-key-elements.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-problem-solving.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-target-tradeoff.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-timeline.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-system-course-catalog.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-system-course-map-lecture.md` | reviewed | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-best-practice-learning.md` | enriched | 1 | 0.88 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-equity-checklist.md` | redirect | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-fab-persuasion.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-foresight-canvas.md` | enriched | 5 | 0.9 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-mental-model-refinement.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-onboarding-90day.md` | redirect | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-project-health-radar.md` | redirect | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-y-model-ruler.md` | enriched | 1 | 0.85 | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-overview.md` | reviewed | 5 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\人机协作决策-双三角模型.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\保达云诊所深度调研报告.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\在设计小伙伴的反馈还挺好的.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\存储策略.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\学会提问在信息洪流中锻造批判性思维的利刃.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\开源HIS系统代码深度分析报告.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\数据标注维度最佳实践调研报告.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\紫鲸ai_智能体工作流平台_深度分析与产品设计.md` | superseded | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\紫鲸ai智能体工作流平台.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\老朱的水感-2026年5月.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\视觉prompt三层操作系统-srom-visual-os.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\诊所o2o外卖平台业务深度调研报告.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\轻量级诊所HIS调研全清单.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\那今天不会.md` | enriched | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ai-entrepreneur-technical-blindspot.md` | draft | 3 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ai-judgment-human-responsibility.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ai-judgment-programmer-paradox.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c1-cjk-regex-silent-fail.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c10-batch-tool-no-dry-run.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c11-hongqigong-skip-review.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c2-dual-status-machine.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c3-txt-ingest-skip.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c4-selfcheck-superseded.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c5-todo-false-positive.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c6-large-source-overflow.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c7-auto-backup-conflict.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c8-format-complete-mind-empty.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-c9-batch-trigger-garbage.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ef-001-sn74lvc2g07-open-drain.md` |  | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ef-002-bom-version-async.md` |  | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ef-003-hand-soldering-bom-divergence.md` |  | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-ef-004-missing-diagnostic-firmware.md` |  | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f1-regex-on-cjk.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f10-broken-source-refs.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f11-encyclopedia-style.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f12-builder-context-deadlock.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f13-handwritten-yaml-parser.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f14-accuracy-measurement-mismatch.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f2-txt-ingest-skip.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f3-state-json-race-condition.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f4-wrong-workdir.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f5-stale-feedback-ref.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f6-cjk-skeleton-corruption.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f7-surface-translation.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f8-phony-wikilink.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-f9-generic-critique.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-foresight-source-material-blindness.md` | enriched | 2 | 0.95 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-foresight-tier-skip-illusion.md` | draft | 3 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-jh-llm-time-blindness.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-lz-ai-native-organization.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-lz-code-is-disposable.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-mckinsey-hypothesis-driven-pitfalls.md` | enriched | 2 | (empty) | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-my-ai-landing-three-barriers.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-note-maximum-common-divisor.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-note-rookie-disaster-veteran-heaven.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-note-surplus-brainpower.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p1-model-switch-env.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p10-oral-ban.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p11-regex-cutoff.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p13-token-burn.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p14-zombie.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p15-unverified.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p16-validate-reads-state-json.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p17-accuracy-gap.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p18-yaml-parser.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p19-quote-yaml.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p2-tmux-cache.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p20-bigram-fail.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p3-auth-cache.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p4-batch-format-empty.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p5-cc-connect-config.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p6-session-resume-fail.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p7-ocr-skip.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p8-toolkit-forget.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-p9-glob-miss.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-pseudo-demand-trap.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-signal-cluster-illusion.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-truman-document-is-real-project-is-fake.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-truman-flag-note-taking.md` | draft | 1 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-truman-iteration-to-aesthetic-ceiling.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-truman-knowledge-extraction-three-schools.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb1-aigc-mvp-before-ps.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb10-theory-moat-designer.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb11-visual-book-reverse.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb12-ai-image-analysis-replace-training.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb13-zero-shot-style-transfer.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb14-multi-image-commonality.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb15-reverse-image-description.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb16-ecommerce-product-image-vs-lucky-draw.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb17-product-lifestyle-photography.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb18-small-shop-image-mismatch.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb19-visual-strategy-price-match.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb2-llm-muddy-clear-muddy.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb20-ai-eye-high-principle.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb21-ecommerce-pricing-independent-model.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb22-visual-presentation-scene-match.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb23-ai-pre-screen-three-minutes.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb24-ai-poster-de-ai-feeling.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb25-solution-driven-visual-design.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb26-chinese-food-photography-props.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb27-pseudo-layer-evasion.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb28-prompt-expiration-management.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb29-prompt-migrate-copy-first.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb3-diffusion-stepwise-vs-human-holistic.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb30-ecommerce-channel-version.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb31-style-first-controlnet.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb32-doubao-size-composition.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb4-nano-banana-style-reproduction.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb5-style-asset-archive.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb6-midjourney-chinese-text-fix.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb7-design-demand-80-10-10.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb8-file-naming-eight-elements.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb9-cubox-deployment-failure.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-一堂-wishful-thinking-kills-startups.md` | draft | 3 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-atomic-no-standard.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-real-business-is-the-engine.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-silky-answer-warning.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-silky-answers-are-dangerous.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-半肥猫-skill-rejection-value.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-ai-cant-design-structure.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-constraint-beats-talent.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-logs-fastest-ignored.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-newbie-can-validate.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-novice-mindset-advantage.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-pdca-starts-from-do.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-problem-vs-question.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-纪浩-simple-complex-routing.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\yt-note-ai-p-role-not-c-role.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\yt-note-p-c-role-boundary-realworld.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\yt-note-three-level-evolution.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\agent-ecosystem-design.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\data-curator-role-division.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\fix-dark-knowledge-extractor-llm.md` | pending | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\fix-data-curator-parse-bug.md` | pending | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\gold-standard-manual-labels.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\high-density-composite-compilation-strategy.md` | revised | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-data-alignment-response.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-extractor-upgrade-report.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\huangyaoshi-tagging-and-scope-proposal.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\kdo-15-dimension-label-spec.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\kdo-ec-industrialization-migration-proposal.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\label-accuracy-standard-alignment.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\labeling-final-consolidation.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\labeling-research-alignment.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\modeling-capability-for-kdo.md` | stable | 2 | 0.78 | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\ouyangfeng-data-alignment-response.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\ouyangfeng-labeling-research-review.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_05858800-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_47264869-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_8001399c-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_85a84b92-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_8ecb74e3-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_97170532-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_ca61cdd7-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260501_e1e150b9-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260503_f3e9a2b1-improvement-plan.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260531_data-curator-v1.1.md` | superseded | 1 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260531_data-curator-v1.3.md` | draft | 4 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\plan_20260531_data-curator-v1.md` | superseded | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-ai-domain-mastery-pipeline.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-deep-synthesis-infrastructure.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-graph-rag-star-fix.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-kdo-flywheel-infrastructure.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-prompt-injection-infrastructure.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\proposal-yaml-frontmatter-standardization.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\sprint-6-cli-gap-proposal.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\three-party-data-alignment.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\truman-ai-partner-design-analysis.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\一堂.md` | stable | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-maister-trusted-advisor.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-mckinsey-7s.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-mckinsey-hypothesis-driven.md` | enriched | 2 | (empty) | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-mckinsey-mece.md` | enriched | 2 | (empty) | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-minto-pyramid-principle.md` | draft | 2 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-decision-abcd-model.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-unit-model-ladder.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-unit-model-overview.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\projects\互联网医院项目.md` | active | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\projects\诊所O2O项目.md` | active | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\projects\鑫港湾HIS项目.md` | active | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\agent-external-brain-design.md` | enriched | 0 | (empty) | medium-low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\agent-native-card-design.md` | active | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\graph-rag-retrieval-layer.md` | stable | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\kdo-batch-produce-req014.md` | proposed | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\kdo-watch-health-check-layer.md` | proposed | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\sprint-2-gate-enrich-evidence.md` | draft | 0 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\workflow-knowledge-collision.md` | active | 0 | (empty) | high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\一堂方法论体系总图.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\concept-mckinsey-issue-tree.md` | enriched | 2 | (empty) | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\concept-toyota-5-whys.md` | enriched | 2 | (empty) | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-ai-workspace-setup.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-evidence-check.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-landing-five-steps.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-narrative-test.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-old-small-checklist.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-parallel-validation.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-prd-for-ai.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-problem-validation.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-purpose-bias-check.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-question-problem-checklist.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-system-redundancy.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\sk-ai-voice-input-doubao.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\skill-mckinsey-hypothesis-driven-workflow.md` | enriched | 2 | (empty) | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\skill-note-keyword-bolding.md` | draft | 1 | 0.9 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\skill-note-layer-constraint.md` | draft | 1 | 0.92 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\skill-note-one-line-one-point.md` | draft | 1 | 0.95 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-note-five-levels-training.md` | draft | 2 | 0.88 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-note-live-field-skill.md` | draft | 2 | 0.85 | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-pitch-metaphor.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-pitch-quantification.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-pitch-storytelling.md` | enriched | 2 | 0.85 | medium-high |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-ai-ppt-maker.md` | draft | 1 | (empty) | low |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-ai-assisted.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-benchmark.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-construction.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-dynamic.md` |  | 0 | (empty) | medium |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-tool-unit-model-selection.md` |  | 0 | (empty) | medium |

---

## 六、高置信低信任卡片

未发现此类问题。

---

## 七、日期字段不一致卡片

| 文件 | 日期字段 | 建议操作 |
|---|---|---|
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-jh-yitang-vs-sqlhelper.md` | created_at=2026-06-09, updated_at=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-AI高考志愿-kernel-mismatch.md` | created_at=2026-06-08, updated_at=2026-06-09 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-无人餐厅-hypothesis-failure.md` | created_at=2026-06-08, updated_at=2026-06-09 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-一堂-陈贤敏汉堡-hypothesis-validation.md` | created_at=2026-06-08, updated_at=2026-06-09 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\2026-05-17-深夜感想.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-hackathon-pitches.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-native-五层进阶从答案到效率到作品到产品到系统.md` | created_at=“2026-05-23T17:29:50+00:00”, updated_at=“2026-05-24T00:00:00+00:00” | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-short-drama-ice-fire-scripting-compass.md` | created_at=2026-06-13, updated_at=2026-06-14, review_date=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-俱乐部人和-ai-协作-五层结构.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:22:09+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai-俱乐部人和-ai-协作-参考案例对比一堂-vs-sql-helper.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:22:37+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc文创案例设计课leo文创ip从0到1全流程.md` | created_at=2026-05-28, updated_at=2026-06-12 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc设计基础01ai生图原理与提示词基本功.md` | created_at=2026-05-28, updated_at=2026-06-12 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aigc设计师实操培训01口喷设计范式与电商ai设计全流程.md` | created_at=2026-05-28, updated_at=2026-06-12 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\aima-ai思维卡-外部链接归档.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ai时代判断力口述.md` | created_at=2026-05-25, updated_at=2026-05-28 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\business-validation-models-collaboration.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-business-prediction.md` | created_at=2026-06-09, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-一堂-hypothesis-driven-business-methodology.md` | created_at=2026-06-08, updated_at=2026-06-09 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-半肥猫-ai-learning-toolification-methodology.md` | created_at=2026-06-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-纪浩-ai-collaboration-methodology.md` | created_at=2026-06-07, updated_at=2026-06-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\design-ai-image-generation.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\finance-legal-business-operations.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\graph-rag.md` | created_at=2026-05-03, updated_at=2026-05-03, review_date=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\industry-ai-cases.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\kimi-深度调研集群方法论-deep-research-swarm.md` | created_at=2026-05-01, updated_at=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\knowledge-delivery-os-快速体验指南-飞书云文档.md` | created_at=2026-04-30, updated_at=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\learning-thinking.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\obsidian-kdo-内容产出工作流-产品设计大纲.md` | created_at=2026-05-01, updated_at=2026-05-03 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ai俱乐部-人和ai协作-纪浩-五层结构-图片01.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:23:11+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ai俱乐部-人和ai协作-纪浩-参考案例-图片02.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:23:54+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ocr_screenshot2.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-ocr_snipaste_2026-05-15_21-39-40.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-screenshot1.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-screenshot2.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-truman的个人成长五步法.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-truman的选择两条职业成长路线.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-truman自用的ai-featureset.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:25:32+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-提问工程化.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:26:18+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai学习-提问进化路线图.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:26:53+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai清单体笔记系统故事线-truman-图片01.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:27:45+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-ai清单体笔记训练段位图-truman-图片02.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:28:40+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-tcpr模型-皇冠模型.md` | created_at=2026-06-09T14:03:49+00:00, updated_at=2026-06-09T14:29:37+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-y模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-全景图muse模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-双三角模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-提问刻意练习画布.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo-全景策略.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo完整清单.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学学习ipo模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-科学提问刻意练习.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-表达力火箭模型-执行武器库.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-表达力火箭模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-解放思想.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香十指模型-超级武器库.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香基本功-十指模型修炼地图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-讲香基本功.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-个人修炼-课程清单.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-人机协作-双三角模型.md` | created_at=2026-06-09T14:04:55+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-创业必修-课程清单.md` | created_at=2026-06-09T14:04:55+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-abcd策略模型.md` | created_at=2026-06-09T14:04:55+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-tcpr底层网络协议.md` | created_at=2026-06-09T14:04:55+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-修炼地图.md` | created_at=2026-06-09T14:04:55+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-动态预测.md` | created_at=2026-06-09T14:04:55+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单sku模型.md` | created_at=2026-06-09T14:04:55+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单商圈模型.md` | created_at=2026-06-09T14:04:55+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单城市模型.md` | created_at=2026-06-09T14:04:56+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单客户模型.md` | created_at=2026-06-09T14:04:56+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单履约模型.md` | created_at=2026-06-09T14:04:56+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单柜子模型.md` | created_at=2026-06-09T14:04:56+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单用户模型.md` | created_at=2026-06-09T14:04:56+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单订单模型.md` | created_at=2026-06-09T14:04:56+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单销售模型.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-单门店模型.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-基准值.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-壁垒预判.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-外部对抗地图.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-多模型情况.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-学练用.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄01.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-对抗小抄02.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-扭蛋机案例.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找全成本实操难点.md` | created_at=2026-06-09T14:05:27+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找单元模型实操难点.md` | created_at=2026-06-09T14:05:28+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-找基准值实操难点.md` | created_at=2026-06-09T14:05:28+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-斧子尺子梯子.md` | created_at=2026-06-09T14:05:28+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-斧子尺子梯子详解.md` | created_at=2026-06-09T14:05:28+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-最简单元模型.md` | created_at=2026-06-09T14:05:28+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-段位专家.md` | created_at=2026-06-09T14:05:28+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-示例.md` | created_at=2026-06-09T14:05:28+00:00, updated_at=2026-06-09T15:52:58+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-示例01.md` | created_at=2026-06-09T14:05:28+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-规模对抗实操难点.md` | created_at=2026-06-09T14:05:51+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-规模经济对抗武器库.md` | created_at=2026-06-09T14:05:51+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-单元模型-象限分析法.md` | created_at=2026-06-09T14:05:51+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-个人地图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-个人地图_conv.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-创业地图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-创业地图_conv.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-管理地图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-地图-管理地图_conv.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-案例拆解-课程清单.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-泛产品设计-十年苦练30招.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例01.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例02.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例03.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布-案例04.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi决策评估画布.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-roi高阶训练全景图.md` | created_at=2026-06-09T14:05:51+00:00, updated_at=2026-06-09T15:52:58+00:00 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-x型y型决策习惯对比.md` | created_at=2026-06-09T14:05:51+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-一堂双三角磨合追求-从入门到无限进步.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-人机协作决策.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-关键假设abcd模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-关键训练清单重要.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-决策三角形.md` | created_at=2026-06-09T14:05:51+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-发现决策.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-商业模式-完整财务公式决策.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-个人.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-企业.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-宽度-团队.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l1优先级定性.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l2部分定量.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l3定量公式.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l4-案例01.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-l4严格财务公式.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-你的业务是一次抽样实验.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-决策经验值.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例01.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例02.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例03.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例04.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例05.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-深度-案例06.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-稀缺机会窗口.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-稀缺资源清单.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-项目方案评估三角形.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-高度-两种典型的思考习惯.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-科学决策-高水平共识曲线重要.md` | created_at=2026-06-09T14:05:52+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-管理必修-课程清单.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂-高阶体系探索营-三种咨询可能性.md` | created_at=2026-06-09T14:05:52+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂doc-单元模型-十大单元模型.md` | created_at=2026-06-09T14:05:52+00:00, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型-科学成事道理.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型steps策略集.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂y模型实操工作流.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂个人地图高潜力成长者修炼全景图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂五步法-产品内核画布.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂五步法画布.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂产品内核-十大典型指标.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂刻意练习十年成长指数.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂提炼过的因果模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂最佳转化率动力曲线图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计-十年修炼爬山地图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计-多出牌多练习.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂泛产品设计36计-全套地图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂深度复盘冰山图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂转化率-10大容易浪费的触点.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂进步大地图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-一堂进步大地图_compressed.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-优秀泛产品设计者的自我修养.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-婚礼操盘-用户和场景.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-婚礼规划.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-审美提升的层级.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004746_32_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004751_33_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004755_34_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004758_35_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004801_37_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004802_38_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004804_39_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004806_40_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-微信图片_20260507004811_41_32.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践建模.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践收集.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-最佳实践池子.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美卡片-美好作品想象.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-审美工具箱指南.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-一堂五步法.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-动力阻力.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-场景推演.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-多视角思考.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-峰终定律.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-惊喜公式.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-用户分层.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-用户视角.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-行业分析画布.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-需求挖掘.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-用户卡片-项目背景分析.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-roi分析.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-业务建模.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-低成本测试mvp.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-假设拆解.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-内核和边界.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-努力仿真.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-十倍速验证.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-善用佳软.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-复盘迭代.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-攻坚会.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-灵感闪现.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-管理三段论.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-解放思想.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-设计原则.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-逻辑mece.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-酝酿式打磨.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-里程碑拆解.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-落地卡片-风险管理.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计-需求工具箱指南.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计的应用场景示意图.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计者的三大自我修养.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计者的自我修养.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计落地工具篇指南.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-泛产品设计落地篇.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-萃取总结.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-顶级产品追求的方向-乔布斯.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-项目背景问题思考的8个维度.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\ocr-预判模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\personal-growth-complex-systems.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\product-business-strategy.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-ai-problem-question-check.md` | created_at=2026-06-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-一堂-product-kernel-canvas.md` | created_at=2026-06-08, updated_at=2026-06-09 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-使用一页纸速查卡快速调用框架.md` | created_at=2026-06-09, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-分享输出检验法.md` | created_at=2026-06-09, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-水水-管理决策权重偏差.md` | created_at=2026-06-07, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-立即实践转化法.md` | created_at=2026-06-09, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-纪浩-AI对话上下文隔离.md` | created_at=2026-06-07, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-AIGC项目ROI评估.md` | created_at=2026-06-07, updated_at=2026-06-12 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-业务为先的AI中台建设.md` | created_at=2026-06-07, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-工作流优先于AIGC的决策方法.md` | created_at=2026-06-07, updated_at=2026-06-12 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\supply-chain-beverage.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\tools-workflows.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\writing-content.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown.md` | created_at=2026-04-29, updated_at=2026-05-04, review_date=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yitang-methodology-system.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-ai-startup-20-risky-hypotheses.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-ai-trend-12-signals.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-barrier-analysis-cheat-sheet.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-barrier-identification-skill.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-business-analysis-cognitive-biases.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-business-formula-parameter-iceberg.md` | created_at=2026-06-14, updated_at=2026-06-15, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-business-formula-ten-paradigms.md` | created_at=2026-06-14, updated_at=2026-06-15, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-case-mandatory-cases.md` | created_at=2026-05-05, updated_at=2026-06-13, review_date=2026-05-06 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-composite-pan-product-methodology.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-concept-ai-guard-brain.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-concept-context-engineering.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-concept-p-type-l-type.md` | created_at=2026-06-06, updated_at=2026-06-13, review_date=2026-06-06 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-concept-peas-insight.md` | created_at=2026-05-18, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-concept-weapon-arsenal.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-customer-acquisition-toolkit.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-ai-partner.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-canvas.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-consensus-iceberg.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-depth-ladder.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-full-process.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-habit-shift.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-height-toolkit.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-review.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-width-method.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-decision-y-model.md` | created_at=2026-05-17, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-demand-analysis-hiking-map.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-259-milestone.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-barriers.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-business-growth.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-channel-exploration.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-concentration-analysis.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-five-step-method.md` | created_at=2026-05-06, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-fundraising.md` | created_at=2026-05-06, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-growth-flywheel.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-industrial-production.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-industry-forecast.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-key-hypotheses.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-06-06 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-lean-validation.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-liberate-thinking.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-needs-analysis.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-07 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-opportunity-selection.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-pragmatic-startup.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-product-core.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-06-06 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-research-camp.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-research-cognition.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-scientific-method.md` | created_at=2026-05-06, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-spin-selling.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-truth-seeking.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-unit-model.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-five-step-common-pitfalls.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-five-step-implementation.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-five-step-level-blindspots.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-five-step-method.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-15-char-mantra.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-ab-steady-state.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-addition-subtraction.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-business-spectrum.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-deliverables-four-levels.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-model-taxonomy.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-probability-engineering.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-ten-fatal-flaws.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-growth-cycle-model.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-basic-skills.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-business-formula.md` | created_at=2026-06-15, updated_at=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-company-culture.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-conversion-hacking.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-finance-basics.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-founder-role.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-goal-management.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-leadership-levels.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-onboarding.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-partnership-equity.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-project-management.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-decision.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-hiring.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-scientific-meetings.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-strategy-meeting.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-team-knowledge.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-management-toolkit-overview.md` | created_at=2026-05-19, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-market-size-estimation.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-aesthetic-progression.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-agent-architecture.md` | created_at=2026-05-15, updated_at=2026-06-13, review_date=2026-05-15 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-cognitive-upgrade-framework.md` | created_at=2026-05-15, updated_at=2026-06-13, review_date=2026-05-15 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-conversion-optimization.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-deep-review-iceberg.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-deliberate-practice-growth.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-dual-triangle-competitiveness.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-entrepreneur-map.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-five-step-canvas.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-ipo-complete-checklist.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-ipo-learning-strategy.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-liberate-thinking-layers.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-management-map.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-muse-ai-framework.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-36-strategies.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-aesthetic-toolkit.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-climbing-map.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-demand-toolkit.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-execution-toolkit.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-pan-product-three-virtues.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-personal-map.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-personal-pitch-toolkit.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-prediction-model.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-product-core-metrics.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-product-excellence.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-progress-map.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-prompt-engineering.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-questioning-practice-canvas.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-scientific-questioning-map.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-truman-career-routes.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-truman-five-step-growth.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-y-organization.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-ai-human-division.md` | created_at=2026-06-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-checklist-concept.md` | created_at=2026-06-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-deliberate-practice-four-elements.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-expert-interview-modeling.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-extensive-research-input.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-fact-pattern-insight.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-l4-internalization.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-l6-extraction.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-note-problem-solving-capability.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-aesthetic-collection.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-aesthetic-imagination.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-aesthetic-modeling.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-aesthetic-pool.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-five-step-method.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-industry-canvas.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-motivation-resistance.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-multi-perspective.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-need-discovery.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-peak-end-rule.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-project-background.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-scenario-walkthrough.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-surprise-formula.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-user-perspective.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-user-segmentation.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-10x-validation.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-business-modeling.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-core-and-boundary.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-design-principles.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-good-tools.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-hypothesis-decomposition.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-idea-spark.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-incubation-polish.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-liberate-thinking.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-logic-mece.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-low-cost-mvp.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-management-trilogy.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-milestone-breakdown.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-realistic-simulation.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-review-iteration.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-risk-management.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-roi-analysis.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-war-room.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-ai-capability.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-ai-thinking-card.md` | created_at=2026-05-15, updated_at=2026-06-13, review_date=2026-05-15 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-checklist-notes.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-deep-review.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-07 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-deliberate-practice.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-inspiration-flash.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-ipo-learning.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-07 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-knowledge-extraction.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-knowledge-management.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-02.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-aesthetics.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-concepts.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-exploration.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-practice.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-pan-product-tools.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-product-design.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-scientific-expression.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-thinking-models.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-time-management.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-verbatim-script.md` | created_at=2026-05-06, updated_at=2026-06-13, review_date=2026-05-08 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-y-model-exploration-2.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-y-model-practice.md` | created_at=2026-05-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-aphorism.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-colloquialization.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-conflict.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-emotionalization.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-materialization.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-metaphor.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-quantification.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-scenarization.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-storytelling.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-sublimation.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-product-kernel-cultivation.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-product-ten-metrics.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-anti-flattery.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-brainstorming.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-engineering-andrew-ng.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-iterative-prompting.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-prompt-writing-workflow.md` | created_at=2026-05-13, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-action-camp-launch.md` | created_at=2026-05-05, updated_at=2026-06-13, review_date=2026-05-06 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-competitor-toolkit.md` | created_at=2026-05-18, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-expert-interview.md` | created_at=2026-05-18, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-hypothesis-test.md` | created_at=2026-05-18, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-industry-canvas.md` | created_at=2026-05-18, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-intelligence-map.md` | created_at=2026-05-18, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-mindset.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-osl-framework.md` | created_at=2026-05-18, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-user-jtbd.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-weaponry-course.md` | created_at=2026-05-05, updated_at=2026-06-13, review_date=2026-05-06 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-scale-economy-weapon-library.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-checklist-as-ai-protocol.md` | created_at=2026-06-10, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-p-role-prompt-design.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-contrast-analysis.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-key-elements.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-problem-solving.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-target-tradeoff.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-skill-storyline-timeline.md` | created_at=2026-06-15, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-system-course-catalog.md` | created_at=2026-05-07, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-system-course-map-lecture.md` | created_at=2026-05-05, updated_at=2026-06-13, review_date=2026-05-06 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-three-dimension-opportunity-matrix.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-best-practice-learning.md` | created_at=2026-06-06, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-equity-checklist.md` | created_at=2026-05-31, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-fab-persuasion.md` | created_at=2026-06-06, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-foresight-canvas.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-hiring-scorecard.md` | created_at=2026-05-19, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-knowledge-extraction.md` | created_at=2026-05-19, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-meeting-designer.md` | created_at=2026-05-19, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-mental-model-refinement.md` | created_at=2026-06-06, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-okr-cycle.md` | created_at=2026-05-19, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-onboarding-90day.md` | created_at=2026-05-31, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-peas-agent-analysis.md` | created_at=2026-05-15, updated_at=2026-06-13, review_date=2026-05-15 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-product-core-canvas.md` | created_at=2026-06-06, updated_at=2026-06-13, review_date=2026-06-06 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-project-health-radar.md` | created_at=2026-05-31, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-strategy-workshop.md` | created_at=2026-05-19, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-y-model-ruler.md` | created_at=2026-06-06, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-ai-assisted.md` | created_at=2026-05-24, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-benchmark.md` | created_at=2026-05-24, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-build.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-concept.md` | created_at=2026-06-11, updated_at=2026-06-13, review_date=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-construction.md` | created_at=2026-05-24, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-dynamic.md` | created_at=2026-05-24, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-ladder.md` | created_at=2026-05-24, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-overview.md` | created_at=2026-05-24, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-selection.md` | created_at=2026-05-24, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-unit-model-three-tools.md` | created_at=2026-06-10, updated_at=2026-06-13, review_date=2026-06-10 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\互联网医院模式深度调研报告.md` | created_at=2026-04-30, updated_at=2026-05-04, review_date=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\人机协作决策-双三角模型.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\在设计小伙伴的反馈还挺好的.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\存储策略.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\学会提问在信息洪流中锻造批判性思维的利刃.md` | created_at=2026-05-23, updated_at=2026-05-24 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\紫鲸ai_智能体工作流平台_深度分析与产品设计.md` | created_at=2026-04-30, updated_at=2026-05-03 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\老朱的水感-2026年5月.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\街顺app全面调研报告.md` | created_at=2026-04-26, updated_at=2026-05-03, review_date=2026-05-03 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\视觉prompt三层操作系统-srom-visual-os.md` | created_at=2026-05-21, updated_at=2026-06-12 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\诊所o2o外卖平台业务深度调研报告.md` | created_at=2026-04-30, updated_at=2026-05-03 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\那今天不会.md` | created_at=2026-05-21, updated_at=2026-05-22 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\鑫港湾his系统分阶段整改报告.md` | created_at=2026-04-28, updated_at=2026-05-03, review_date=2026-05-03 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-modeling-ai-without-judgment.md` | created_at=2026-06-14, updated_at=2026-06-15, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-modeling-counterexample-driven.md` | created_at=2026-06-14, updated_at=2026-06-15, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-modeling-essence-predictive.md` | created_at=2026-06-14, updated_at=2026-06-15, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-modeling-sop-execution-locks.md` | created_at=2026-06-14, updated_at=2026-06-15, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb1-aigc-mvp-before-ps.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb10-theory-moat-designer.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb18-small-shop-image-mismatch.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb19-visual-strategy-price-match.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb20-ai-eye-high-principle.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb21-ecommerce-pricing-independent-model.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb5-style-asset-archive.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb7-design-demand-80-10-10.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-yb9-cubox-deployment-failure.md` | created_at=2026-06-04, updated_at=2026-06-11 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\dark-knowledges\dk-一堂-wishful-thinking-kills-startups.md` | created_at=2026-06-08, updated_at=2026-06-09 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\modeling-capability-for-kdo.md` | created_at=2026-06-15, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\truman-ai-partner-design-analysis.md` | date=2026-06-07, created_at=2026-06-15 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\Kimi-月之暗面.md` | created_at=2026-05-03, updated_at=2026-05-03, review_date=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\YC-Y-Combinator.md` | created_at=2026-05-03, updated_at=2026-05-03, review_date=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\紫鲸AI.md` | created_at=2026-05-03, updated_at=2026-05-03, review_date=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\鑫港湾.md` | created_at=2026-05-03, updated_at=2026-05-03, review_date=2026-05-04 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\ai-methodology-tools.md` | created_at=2026-06-14, updated_at=2026-06-14T16:09:18+00:00, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\ai-short-drama-ice-fire-dissection-compass.md` | created_at=2026-06-13, updated_at=2026-06-14, review_date=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\concept-mckinsey-hypothesis-driven.md` | created_at=2026-06-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-business-formula-abc-model.md` | created_at=2026-06-14, updated_at=2026-06-15, review_date=2026-06-14 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-unit-model-ladder.md` | date=2026-05-24, created_at=2026-06-15 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\frameworks\yt-unit-model-overview.md` | date=2026-05-24, created_at=2026-06-15 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\systems\kdo-protocol.md` | created_at=2026-05-02, updated_at=2026-05-04, review_date=2026-05-03 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\ai-short-drama-conflict-three-axes.md` | created_at=2026-06-13, updated_at=2026-06-14, review_date=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\ai-short-drama-framework-three-axes.md` | created_at=2026-06-13, updated_at=2026-06-14, review_date=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\ai-short-drama-plot-three-axes.md` | created_at=2026-06-13, updated_at=2026-06-14, review_date=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\ai-short-drama-script-planning-three-axes.md` | created_at=2026-06-13, updated_at=2026-06-14, review_date=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\concept-toyota-5-whys.md` | created_at=2026-06-11, updated_at=2026-06-13 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-pitch-metaphor.md` | created_at=2026-05-13, updated_at=2026-05-28 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-pitch-quantification.md` | created_at=2026-05-13, updated_at=2026-05-28 | 人工复核 |
| `C:\Users\Administrator\Desktop\wiki\30_wiki\tools\yt-pitch-storytelling.md` | created_at=2026-05-13, updated_at=2026-05-28 | 人工复核 |

---

## 八、批量处理规则

### 8.1 自动下调规则
- confidence ≥ 0.95 且 source < 2 → 0.85
- confidence 0.90–0.94 且 source < 2 → 0.80
- confidence ≥ 0.85 且 trust_level 为 low/medium-low → 0.80

### 8.2 默认值填充规则
| status | source 数量 | confidence | trust_level |
|---|---|---|---|
| draft | 0 | 0.60 | low |
| draft | ≥1 | 0.70 | medium-low |
| proposed | 任意 | 0.65 | low |
| enriched | 0 | 0.75 | medium-low |
| enriched | 1 | 0.80 | medium |
| enriched | ≥2 | 0.85 | medium-high |
| reviewed | 任意 | 0.85 | high |
| stable | 任意 | 0.90 | high |
| needs-review | 任意 | 0.70 | medium-low |

### 8.3 已批准卡片更新规则
- 正文检测到 reviewer + 批准关键词，且当前 reviewed_by=pending → 更新 reviewed_by 为检测到的 reviewer
- 若 status 为 draft/proposed → 同时更新为 reviewed（最终是否 approved 需人工确认）