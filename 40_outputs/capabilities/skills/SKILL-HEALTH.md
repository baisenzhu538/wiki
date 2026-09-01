# Skill 健康雷达（SKILL-HEALTH）

> #598 扫描生成物（生成时间 2026-09-02 01:33，共 76 个 skill）。
> 8 维口径 = 建议书_20260901_skill健康度勘察与检测方法论 §三；溯源 darwin-skill 9 维 rubric + skill-architecture-design 五维量化。
> 档位：≥6/8 🟢 健康；4-5/8 🟡 亚健康（补短板即可）；≤3/8 🔴 不健康（路由/内容至少一项阻塞）。
> **结构层 triage，不替代实测**（test-prompts 效果实测=建议书动作8 缓议）；生成物勿手改，
> 重跑 `python 40_outputs/code/scripts/scan_skills_registry.py` 刷新。

**总览：🟢 3 / 🟡 5 / 🔴 68（共 76）**

| skill | 档位 | 得分 | A触发 | B描述 | C失败 | D边界 | E来源 | F三写 | G克制 | H步骤 | 主文件行数 |
|:--|:--|--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|--:|
| `nine-character-ai-collaboration` | 🟢 | 8/8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90 |
| `research-core` | 🟢 | 8/8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 204 |
| `skill-architecture-design` | 🟢 | 8/8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 103 |
| `agent-self-iteration` | 🟡 | 4/8 | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | 125 |
| `deep-debug` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | 444 |
| `kdo-self-attack` | 🟡 | 4/8 | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | 170 |
| `knowledge-collision` | 🟡 | 4/8 | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 158 |
| `task-orchestration` | 🟡 | 4/8 | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 118 |
| `ai-collaboration-dev` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 82 |
| `ai-collaboration-gan` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 77 |
| `ai-collaboration-harness` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 93 |
| `beikai-multimodal-pipeline` | 🔴 | 3/8 | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | 839 |
| `content-production-polish` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 221 |
| `content-production-positioning` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 80 |
| `decision-prediction` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 108 |
| `demand-analysis-synthetic` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 257 |
| `nine-layer-deep-dig` | 🔴 | 3/8 | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | 72 |
| `research-ci-framework` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 123 |
| `self-evolution` | 🔴 | 3/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | 113 |
| `stage-3-tooling` | 🔴 | 3/8 | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | 63 |
| `agent-migration-health-check` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 110 |
| `ai-collaboration-bitcoe` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 65 |
| `ai-collaboration-ooda` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 73 |
| `content-production` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 70 |
| `content-production-draft` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 86 |
| `decision` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 53 |
| `decision-bias` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 100 |
| `decision-hygiene` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 110 |
| `decision-y-model` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 101 |
| `five-step-barrier` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 65 |
| `five-step-demand` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 60 |
| `five-step-product` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 63 |
| `hermes-multi-bot-feishu-setup` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | 358 |
| `multi-page-article-capture` | 🔴 | 2/8 | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 395 |
| `presenton-ppt-generator` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 277 |
| `research` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | 33 |
| `research-cross-validation` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 51 |
| `research-expert-interview` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 48 |
| `research-financial-report` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 57 |
| `research-industry-report` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 56 |
| `research-multi-agent` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 135 |
| `research-quality-gate` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 96 |
| `research-sats` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 104 |
| `research-web-scraping` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 54 |
| `six-layer-cross-validation` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | 52 |
| `strategy` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 49 |
| `strategy-brm` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 96 |
| `strategy-lifecycle` | 🔴 | 2/8 | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | 67 |
| `strategy-workshop` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 144 |
| `visual-asset-analysis` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 110 |
| `visual-polish` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 134 |
| `vlm-image-describe-pipeline` | 🔴 | 2/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | 544 |
| `ai-collaboration` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 58 |
| `comfyui-local` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 331 |
| `cosyvoice-tts` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 327 |
| `demand-analysis` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 65 |
| `demand-analysis-blindspot` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 96 |
| `demand-analysis-evaluate` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 93 |
| `demand-analysis-iceberg` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 115 |
| `domain-iteration` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 60 |
| `drawio-mcp-diagrams` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 213 |
| `feishu-publish` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 79 |
| `five-step` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 60 |
| `five-step-business-model` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 62 |
| `five-step-growth` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 60 |
| `pre-ship-check` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 101 |
| `research-alt-data` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 91 |
| `research-google-dorking` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 80 |
| `research-media-verification` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 92 |
| `research-osint` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 55 |
| `stage-1-diagnose` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 67 |
| `stage-2-skeleton` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 63 |
| `stage-4-validate` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 57 |
| `stage-5-assetize` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 62 |
| `strategy-diagnose` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 67 |
| `wan-video-generation` | 🔴 | 1/8 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | 289 |

## 短板聚合（非 🟢 的共性欠账，修复优先级参考）

- A 触发词可路由：缺 72 个——`agent-migration-health-check`、`agent-self-iteration`、`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-dev`、`ai-collaboration-gan`、`ai-collaboration-harness`、`ai-collaboration-ooda`、`beikai-multimodal-pipeline`、`comfyui-local`…
- B 描述信息量≥80字+场景：缺 70 个——`agent-migration-health-check`、`agent-self-iteration`、`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-dev`、`ai-collaboration-gan`、`ai-collaboration-harness`、`ai-collaboration-ooda`、`beikai-multimodal-pipeline`、`comfyui-local`…
- C 失败模式编码：缺 67 个——`agent-migration-health-check`、`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-dev`、`ai-collaboration-gan`、`ai-collaboration-harness`、`ai-collaboration-ooda`、`comfyui-local`、`content-production`、`content-production-draft`…
- D 边界与反例：缺 42 个——`agent-migration-health-check`、`ai-collaboration`、`content-production`、`content-production-draft`、`cosyvoice-tts`、`demand-analysis`、`demand-analysis-blindspot`、`demand-analysis-evaluate`、`demand-analysis-iceberg`、`domain-iteration`…
- E 来源可追溯：缺 72 个——`agent-migration-health-check`、`agent-self-iteration`、`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-dev`、`ai-collaboration-gan`、`ai-collaboration-harness`、`ai-collaboration-ooda`、`beikai-multimodal-pipeline`、`comfyui-local`…
- F 三写一致(manifest)：缺 72 个——`agent-migration-health-check`、`agent-self-iteration`、`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-dev`、`ai-collaboration-gan`、`ai-collaboration-harness`、`ai-collaboration-ooda`、`beikai-multimodal-pipeline`、`comfyui-local`…
- G 主文件克制≤300行：缺 7 个——`beikai-multimodal-pipeline`、`comfyui-local`、`cosyvoice-tts`、`deep-debug`、`hermes-multi-bot-feishu-setup`、`multi-page-article-capture`、`vlm-image-describe-pipeline`
- H 操作可执行(编号步骤)：缺 38 个——`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-ooda`、`comfyui-local`、`decision`、`decision-bias`、`decision-hygiene`、`decision-y-model`、`demand-analysis`、`demand-analysis-blindspot`…

## 维度判定说明（机械规则，与建议书 §三对齐）

- A：manifest/frontmatter `trigger.natural_language` 非空
- B：`description` ≥80 字符且含触发场景语汇（触发/适用/何时用/场景…）
- C：正文含「失败模式/踩坑/故障表/常见错误」任一面
- D：正文含「适用边界/不适用/不要/禁止/反例/误区」任一语义段
- E：`adapted_from` 非空（frontmatter 或 manifest）
- F：`manifest.yaml` 存在（挂载同步面见 MOUNT-MATRIX）
- G：SKILL.md ≤300 行（300-500 护栏预警不计分，>500 超护栏）
- H：正文有编号步骤（`1.`/`步骤 N`）或加粗操作条目

