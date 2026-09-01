# Skill 健康雷达（SKILL-HEALTH）

> #598 扫描生成物（生成时间 2026-09-02 05:14，共 76 个 skill）。
> 8 维口径 = 建议书_20260901_skill健康度勘察与检测方法论 §三；溯源 darwin-skill 9 维 rubric + skill-architecture-design 五维量化。
> 档位：≥6/8 🟢 健康；4-5/8 🟡 亚健康（补短板即可）；≤3/8 🔴 不健康（路由/内容至少一项阻塞）。
> **结构层 triage，不替代实测**（test-prompts 效果实测=建议书动作8 缓议）；生成物勿手改，
> 重跑 `python 40_outputs/code/scripts/scan_skills_registry.py` 刷新。

**总览：🟢 7 / 🟡 45 / 🔴 24（共 76）**

| skill | 档位 | 得分 | A触发 | B描述 | C失败 | D边界 | E来源 | F三写 | G克制 | H步骤 | 主文件行数 |
|:--|:--|--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|--:|
| `nine-character-ai-collaboration` | 🟢 | 8/8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90 |
| `research-core` | 🟢 | 8/8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 204 |
| `skill-architecture-design` | 🟢 | 8/8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 103 |
| `agent-self-iteration` | 🟢 | 6/8 | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 125 |
| `kdo-self-attack` | 🟢 | 6/8 | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 170 |
| `knowledge-collision` | 🟢 | 6/8 | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 158 |
| `task-orchestration` | 🟢 | 6/8 | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 118 |
| `ai-collaboration-dev` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 82 |
| `ai-collaboration-gan` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 77 |
| `ai-collaboration-harness` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 93 |
| `beikai-multimodal-pipeline` | 🟡 | 5/8 | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | 839 |
| `content-production-polish` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 221 |
| `content-production-positioning` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 80 |
| `decision-prediction` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 108 |
| `demand-analysis-synthetic` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 257 |
| `nine-layer-deep-dig` | 🟡 | 5/8 | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | 72 |
| `research-ci-framework` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 123 |
| `self-evolution` | 🟡 | 5/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 113 |
| `stage-3-tooling` | 🟡 | 5/8 | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | 63 |
| `agent-migration-health-check` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 110 |
| `ai-collaboration-bitcoe` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 65 |
| `ai-collaboration-ooda` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 73 |
| `content-production` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 70 |
| `content-production-draft` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 86 |
| `decision` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 53 |
| `decision-bias` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 100 |
| `decision-hygiene` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 110 |
| `decision-y-model` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 101 |
| `deep-debug` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | 444 |
| `five-step-barrier` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 65 |
| `five-step-demand` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 60 |
| `five-step-product` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 63 |
| `hermes-multi-bot-feishu-setup` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | 358 |
| `multi-page-article-capture` | 🟡 | 4/8 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | 395 |
| `presenton-ppt-generator` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 277 |
| `research` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | 33 |
| `research-cross-validation` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 51 |
| `research-expert-interview` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 48 |
| `research-financial-report` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 57 |
| `research-industry-report` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 56 |
| `research-multi-agent` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 135 |
| `research-quality-gate` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 96 |
| `research-sats` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 104 |
| `research-web-scraping` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 54 |
| `six-layer-cross-validation` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | 52 |
| `strategy` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 49 |
| `strategy-brm` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 96 |
| `strategy-lifecycle` | 🟡 | 4/8 | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | 67 |
| `strategy-workshop` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 144 |
| `visual-asset-analysis` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 110 |
| `visual-polish` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 134 |
| `vlm-image-describe-pipeline` | 🟡 | 4/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | 544 |
| `ai-collaboration` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 58 |
| `comfyui-local` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | 331 |
| `cosyvoice-tts` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | 327 |
| `demand-analysis` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 65 |
| `demand-analysis-blindspot` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 96 |
| `demand-analysis-evaluate` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 93 |
| `demand-analysis-iceberg` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 115 |
| `domain-iteration` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 60 |
| `drawio-mcp-diagrams` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 213 |
| `feishu-publish` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 79 |
| `five-step` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 60 |
| `five-step-business-model` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 62 |
| `five-step-growth` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 60 |
| `pre-ship-check` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 101 |
| `research-alt-data` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 91 |
| `research-google-dorking` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 80 |
| `research-media-verification` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 92 |
| `research-osint` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 55 |
| `stage-1-diagnose` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 67 |
| `stage-2-skeleton` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 63 |
| `stage-4-validate` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 57 |
| `stage-5-assetize` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 62 |
| `strategy-diagnose` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 67 |
| `wan-video-generation` | 🔴 | 3/8 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | 289 |

## 短板聚合（非 🟢 的共性欠账，修复优先级参考）

- B 描述信息量≥80字+场景：缺 68 个——`agent-migration-health-check`、`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-dev`、`ai-collaboration-gan`、`ai-collaboration-harness`、`ai-collaboration-ooda`、`beikai-multimodal-pipeline`、`comfyui-local`、`content-production`…
- C 失败模式编码：缺 65 个——`agent-migration-health-check`、`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-dev`、`ai-collaboration-gan`、`ai-collaboration-harness`、`ai-collaboration-ooda`、`comfyui-local`、`content-production`、`content-production-draft`…
- D 边界与反例：缺 42 个——`agent-migration-health-check`、`ai-collaboration`、`content-production`、`content-production-draft`、`cosyvoice-tts`、`demand-analysis`、`demand-analysis-blindspot`、`demand-analysis-evaluate`、`demand-analysis-iceberg`、`domain-iteration`…
- E 来源可追溯：缺 68 个——`agent-migration-health-check`、`ai-collaboration`、`ai-collaboration-bitcoe`、`ai-collaboration-dev`、`ai-collaboration-gan`、`ai-collaboration-harness`、`ai-collaboration-ooda`、`beikai-multimodal-pipeline`、`comfyui-local`、`content-production`…
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

