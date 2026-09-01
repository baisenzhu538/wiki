# Agent × Skill 挂载矩阵（MOUNT-MATRIX）

> #588 扫描生成物（生成时间 2026-09-01 14:34）。**登记制：文件引用即挂载**（含历史引用，
> 与「实际运行时可用」可能有出入——引用面是登记真相源）。生成物勿手改，
> 重跑 `python 40_outputs/code/scripts/scan_skills_registry.py` 刷新；挂载变更走 #587 Skills 助理。

## 一、挂载单元清单（谁挂了什么）

| 挂载单元 | 层 | 挂载 skill 数 | skill 清单 |
|:--|:--|--:|:--|
| agent-spec-hongqigong-multimodal | agent-spec | 9 | `beikai-multimodal-pipeline`、`comfyui-local`、`content-production-polish`、`cosyvoice-tts`、`drawio-mcp-diagrams`、`multi-page-article-capture`、`presenton-ppt-generator`、`vlm-image-describe-pipeline`、`wan-video-generation` |
| agent-spec-huangyaoshi-builder | agent-spec | 4 | `agent-self-iteration`、`deep-debug`、`domain-iteration`、`kdo-self-attack` |
| agent-spec-duanwangye-publisher | agent-spec | 2 | `content-production-polish`、`feishu-publish` |
| agent-spec-ouyangfeng-reviewer | agent-spec | 2 | `kdo-self-attack`、`six-layer-cross-validation` |
| agent-spec-laowantong-producer | agent-spec | 1 | `content-production` |
| agent-spec-skills-assistant | agent-spec | 1 | `deep-debug` |
| agent-spec-fengqingyang-observer | agent-spec | 0 | （无 skill 引用） |
| agent-spec-wangyuyan-orchestrator | agent-spec | 0 | （无 skill 引用） |
| agent-spec-zhu-ai-coach | agent-spec | 0 | （无 skill 引用） |
| agent-spec-zhu-boss | agent-spec | 0 | （无 skill 引用） |
| research-explosion-partner | agents实例 | 2 | `content-production`、`stage-1-diagnose` |
| coaching-leadership-assistant | agents实例 | 1 | `content-production-polish` |
| skills-assistant | agents实例 | 1 | `deep-debug` |
| agent-basic-skills-coach | agents实例 | 0 | （无 skill 引用） |
| coaching-leadership-coach | agents实例 | 0 | （无 skill 引用） |
| hongqigong | agents实例 | 0 | （无 skill 引用） |
| laowantong | agents实例 | 0 | （无 skill 引用） |
| meeting-assistant | agents实例 | 0 | （无 skill 引用） |
| ouyangfeng | agents实例 | 0 | （无 skill 引用） |
| sales-dialogue-assistant | agents实例 | 0 | （无 skill 引用） |
| wangyuyan | agents实例 | 0 | （无 skill 引用） |
| 王语嫣 | 角色路由(role-routes) | 9 | `knowledge-collision`、`research-cross-validation`、`research-expert-interview`、`stage-1-diagnose`、`stage-2-skeleton`、`stage-3-tooling`、`stage-4-validate`、`stage-5-assetize`、`task-orchestration` |
| 洪七公 | 角色路由(role-routes) | 8 | `beikai-multimodal-pipeline`、`comfyui-local`、`cosyvoice-tts`、`drawio-mcp-diagrams`、`visual-asset-analysis`、`visual-polish`、`vlm-image-describe-pipeline`、`wan-video-generation` |
| 老顽童 | 角色路由(role-routes) | 7 | `content-production`、`content-production-draft`、`content-production-polish`、`content-production-positioning`、`domain-iteration`、`kdo-self-attack`、`multi-page-article-capture` |
| 黄药师 | 角色路由(role-routes) | 5 | `agent-self-iteration`、`domain-iteration`、`kdo-self-attack`、`nine-layer-deep-dig`、`self-evolution` |
| 欧阳锋 | 角色路由(role-routes) | 5 | `kdo-self-attack`、`pre-ship-check`、`research-cross-validation`、`self-evolution`、`six-layer-cross-validation` |
| 段王爷 | 角色路由(role-routes) | 3 | `feishu-publish`、`pre-ship-check`、`presenton-ppt-generator` |

## 二、skill 对照表（状态三档：已挂载/单点挂载/无主）

| skill | 状态 | 已挂载单元 | 可挂建议 |
|:--|:--|:--|:--|
| `agent-self-iteration` | 已挂载 | 黄药师、agent-spec-huangyaoshi-builder | — |
| `beikai-multimodal-pipeline` | 已挂载 | 洪七公、agent-spec-hongqigong-multimodal | — |
| `comfyui-local` | 已挂载 | 洪七公、agent-spec-hongqigong-multimodal | — |
| `content-production` | 已挂载 | 老顽童、agent-spec-laowantong-producer、research-explosion-partner | — |
| `content-production-draft` | 已挂载 | 老顽童 | — |
| `content-production-polish` | 已挂载 | 老顽童、agent-spec-duanwangye-publisher、agent-spec-hongqigong-multimodal、coaching-leadership-assistant | — |
| `content-production-positioning` | 已挂载 | 老顽童 | — |
| `cosyvoice-tts` | 已挂载 | 洪七公、agent-spec-hongqigong-multimodal | — |
| `deep-debug` | 已挂载 | agent-spec-huangyaoshi-builder、agent-spec-skills-assistant、skills-assistant | — |
| `domain-iteration` | 已挂载 | 黄药师、老顽童、agent-spec-huangyaoshi-builder | — |
| `drawio-mcp-diagrams` | 已挂载 | 洪七公、agent-spec-hongqigong-multimodal | — |
| `feishu-publish` | 已挂载 | 段王爷、agent-spec-duanwangye-publisher | — |
| `kdo-self-attack` | 已挂载 | 黄药师、老顽童、欧阳锋、agent-spec-huangyaoshi-builder、agent-spec-ouyangfeng-reviewer | — |
| `knowledge-collision` | 已挂载 | 王语嫣 | — |
| `multi-page-article-capture` | 已挂载 | 老顽童、agent-spec-hongqigong-multimodal | — |
| `nine-layer-deep-dig` | 已挂载 | 黄药师 | — |
| `pre-ship-check` | 已挂载 | 欧阳锋、段王爷 | — |
| `presenton-ppt-generator` | 已挂载 | 段王爷、agent-spec-hongqigong-multimodal | — |
| `research-cross-validation` | 已挂载 | 王语嫣、欧阳锋 | — |
| `research-expert-interview` | 已挂载 | 王语嫣 | — |
| `self-evolution` | 已挂载 | 黄药师、欧阳锋 | — |
| `six-layer-cross-validation` | 已挂载 | 欧阳锋、agent-spec-ouyangfeng-reviewer | — |
| `stage-1-diagnose` | 已挂载 | 王语嫣、research-explosion-partner | — |
| `stage-2-skeleton` | 已挂载 | 王语嫣 | — |
| `stage-3-tooling` | 已挂载 | 王语嫣 | — |
| `stage-4-validate` | 已挂载 | 王语嫣 | — |
| `stage-5-assetize` | 已挂载 | 王语嫣 | — |
| `task-orchestration` | 已挂载 | 王语嫣 | — |
| `visual-asset-analysis` | 已挂载 | 洪七公 | — |
| `visual-polish` | 已挂载 | 洪七公 | — |
| `vlm-image-describe-pipeline` | 已挂载 | 洪七公、agent-spec-hongqigong-multimodal | — |
| `wan-video-generation` | 已挂载 | 洪七公、agent-spec-hongqigong-multimodal | — |
| `agent-migration-health-check` | 无主 | （无） | 欧阳锋 |
| `ai-collaboration` | 无主 | （无） | 待议 |
| `ai-collaboration-bitcoe` | 无主 | （无） | 待议 |
| `ai-collaboration-dev` | 无主 | （无） | 待议 |
| `ai-collaboration-gan` | 无主 | （无） | 待议 |
| `ai-collaboration-harness` | 无主 | （无） | 待议 |
| `ai-collaboration-ooda` | 无主 | （无） | 待议 |
| `decision` | 无主 | （无） | 王语嫣 |
| `decision-bias` | 无主 | （无） | 王语嫣 |
| `decision-hygiene` | 无主 | （无） | 王语嫣 |
| `decision-prediction` | 无主 | （无） | 王语嫣 |
| `decision-y-model` | 无主 | （无） | 王语嫣 |
| `demand-analysis` | 无主 | （无） | 王语嫣 |
| `demand-analysis-blindspot` | 无主 | （无） | 王语嫣 |
| `demand-analysis-evaluate` | 无主 | （无） | 王语嫣 |
| `demand-analysis-iceberg` | 无主 | （无） | 王语嫣 |
| `demand-analysis-synthetic` | 无主 | （无） | 王语嫣 |
| `five-step` | 无主 | （无） | 王语嫣 |
| `five-step-barrier` | 无主 | （无） | 王语嫣 |
| `five-step-business-model` | 无主 | （无） | 王语嫣 |
| `five-step-demand` | 无主 | （无） | 王语嫣 |
| `five-step-growth` | 无主 | （无） | 王语嫣 |
| `five-step-product` | 无主 | （无） | 王语嫣 |
| `hermes-multi-bot-feishu-setup` | 无主 | （无） | 黄药师 |
| `nine-character-ai-collaboration` | 无主 | （无） | 待议 |
| `research` | 无主 | （无） | 王语嫣 |
| `research-alt-data` | 无主 | （无） | 王语嫣 |
| `research-ci-framework` | 无主 | （无） | 王语嫣 |
| `research-financial-report` | 无主 | （无） | 王语嫣 |
| `research-google-dorking` | 无主 | （无） | 王语嫣 |
| `research-industry-report` | 无主 | （无） | 王语嫣 |
| `research-media-verification` | 无主 | （无） | 王语嫣 |
| `research-multi-agent` | 无主 | （无） | 王语嫣 |
| `research-osint` | 无主 | （无） | 王语嫣 |
| `research-quality-gate` | 无主 | （无） | 王语嫣 |
| `research-sats` | 无主 | （无） | 王语嫣 |
| `research-web-scraping` | 无主 | （无） | 王语嫣 |
| `skill-architecture-design` | 无主 | （无） | 洪七公 |
| `strategy` | 无主 | （无） | 王语嫣 |
| `strategy-brm` | 无主 | （无） | 王语嫣 |
| `strategy-diagnose` | 无主 | （无） | 王语嫣 |
| `strategy-lifecycle` | 无主 | （无） | 王语嫣 |
| `strategy-workshop` | 无主 | （无） | 王语嫣 |

## 三、可挂未挂清单（无主 + 单点挂载，actionable）

- ℹ️ 角色路由另引用 3 个**根目录 legacy skill**（不在 shared/ 73 登记面，未计入上表）：`anti-ai-bs-three-moves`、`author-targeted-collect`、`distill-own-skill`——是否迁入 shared 归 Skills 助理裁定

- **无主 skill：43 个**（任何登记处零引用——先判定归属或明确废弃）
- **单点挂载：0 个**（仅 1 单元引用——评估是否值得推广挂载）
- **已挂载：32 个**

### 无主 skill 归属建议（关键词启发式，机械可审计；落地由 Skills 助理登记）

- `agent-migration-health-check` → 建议 欧阳锋
- `ai-collaboration` → 建议 待议
- `ai-collaboration-bitcoe` → 建议 待议
- `ai-collaboration-dev` → 建议 待议
- `ai-collaboration-gan` → 建议 待议
- `ai-collaboration-harness` → 建议 待议
- `ai-collaboration-ooda` → 建议 待议
- `decision` → 建议 王语嫣
- `decision-bias` → 建议 王语嫣
- `decision-hygiene` → 建议 王语嫣
- `decision-prediction` → 建议 王语嫣
- `decision-y-model` → 建议 王语嫣
- `demand-analysis` → 建议 王语嫣
- `demand-analysis-blindspot` → 建议 王语嫣
- `demand-analysis-evaluate` → 建议 王语嫣
- `demand-analysis-iceberg` → 建议 王语嫣
- `demand-analysis-synthetic` → 建议 王语嫣
- `five-step` → 建议 王语嫣
- `five-step-barrier` → 建议 王语嫣
- `five-step-business-model` → 建议 王语嫣
- `five-step-demand` → 建议 王语嫣
- `five-step-growth` → 建议 王语嫣
- `five-step-product` → 建议 王语嫣
- `hermes-multi-bot-feishu-setup` → 建议 黄药师
- `nine-character-ai-collaboration` → 建议 待议
- `research` → 建议 王语嫣
- `research-alt-data` → 建议 王语嫣
- `research-ci-framework` → 建议 王语嫣
- `research-financial-report` → 建议 王语嫣
- `research-google-dorking` → 建议 王语嫣
- `research-industry-report` → 建议 王语嫣
- `research-media-verification` → 建议 王语嫣
- `research-multi-agent` → 建议 王语嫣
- `research-osint` → 建议 王语嫣
- `research-quality-gate` → 建议 王语嫣
- `research-sats` → 建议 王语嫣
- `research-web-scraping` → 建议 王语嫣
- `skill-architecture-design` → 建议 洪七公
- `strategy` → 建议 王语嫣
- `strategy-brm` → 建议 王语嫣
- `strategy-diagnose` → 建议 王语嫣
- `strategy-lifecycle` → 建议 王语嫣
- `strategy-workshop` → 建议 王语嫣

## 四、挂载纪律（#587 SPEC §六 口径）

- agent-spec 模板增补「已挂载skills」标准节，格式：`- skill-name: 用途一句话`（见 workflow-kdo-agent-production-pipeline Step 1/2）
- 挂载变更 = 三写一致：spec 节 / 本矩阵（重跑刷新）/ skill manifest 适用agent
- 挂载变更同步：王语嫣（编排视图）+ 黄药师（基建视图）；登记维护归 Skills 助理

