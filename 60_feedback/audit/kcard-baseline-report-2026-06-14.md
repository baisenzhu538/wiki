# 30_wiki 知识卡基线扫描报告

> 生成时间：2026-06-15 01:05:14
> 扫描范围：`30_wiki/` 下所有 `.md` 文件
> 总卡片数：1320

## 一、整体概况

| 指标 | 数量 | 占比 |
|---|---|---|
| 总卡片数 | 1320 | 100% |
| draft 状态 | 617 | 46.7% |
| enriched 状态 | 537 | 40.7% |
| stable 状态 | 11 | 0.8% |
| 无 source_refs | 219 | 16.6% |
| 无 author | 0 | 0.0% |
| 无 reviewed_by | 47 | 3.6% |
| 空壳/微小文件 | 0 | 0.0% |
| 高置信低信任 | 152 | 11.5% |

## 二、问题标签分布

| 问题标签 | 数量 | 占比 |
|---|---|---|
| no-trust-level | 1095 | 83.0% |
| no-confidence | 972 | 73.6% |
| draft | 617 | 46.7% |
| no-source | 219 | 16.6% |
| high-conf-low-trust | 152 | 11.5% |
| high-conf-no-trust | 150 | 11.4% |
| no-reviewer | 47 | 3.6% |
| no-title | 28 | 2.1% |
| no-status | 21 | 1.6% |
| no-type | 16 | 1.2% |
| theme-source | 5 | 0.4% |

## 三、按目录问题分布

| 目录 | draft | no-source | no-author | no-reviewer | empty-or-tiny | high-conf-low-trust |
|---|---|---|---|---|---|---|
| cases | 20 | 0 | 0 | 0 | 0 | 12 |
| concepts | 427 | 153 | 0 | 41 | 0 | 125 |
| dark-knowledges | 112 | 4 | 0 | 0 | 0 | 2 |
| decisions | 34 | 36 | 0 | 0 | 0 | 0 |
| entities | 0 | 5 | 0 | 0 | 0 | 0 |
| frameworks | 3 | 3 | 0 | 0 | 0 | 1 |
| projects | 0 | 3 | 0 | 0 | 0 | 0 |
| systems | 3 | 10 | 0 | 0 | 0 | 0 |
| tools | 18 | 5 | 0 | 6 | 0 | 12 |

## 四、Author 分布（前 30）

| Author | 数量 |
|---|---|
| legacy | 1217 |
| 老顽童 | 54 |
| 王语嫣 | 22 |
| 孔阳 | 11 |
| 黄药师 | 7 |
| 黄药师（基于 Truman 口述提取） | 4 |
| 审查者欧阳锋 | 2 |
| 黄药师（Builder） | 1 |
| 黄药师 (Builder) | 1 |
| 周伯通 | 1 |

## 五、Reviewer 分布（前 30）

| Reviewer | 数量 |
|---|---|
| pending | 931 |
| 黄药师 | 154 |
| 老顽童 | 97 |
| (no reviewer) | 47 |
| laowantong | 33 |
| 周伯通 | 15 |
| ['黄药师', 'laowantong'] | 12 |
| 洪七公 | 10 |
| 老顷童（精修） | 7 |
| Claude | 7 |
| 黄药师（Builder体验Producer） | 3 |
| 欧阳锋 | 2 |
| 老顷童 | 2 |

## 六、Domain 分布（前 50）

| Domain | 数量 |
|---|---|
| yitang | 517 |
| design | 230 |
| master | 106 |
| ai-collaboration | 96 |
| ai-saas | 54 |
| product | 45 |
| healthcare | 43 |
| business-strategy | 36 |
| modeling | 25 |
| ai | 25 |
| learning-methodology | 18 |
| entrepreneur | 17 |
| personal-growth | 15 |
| personal | 14 |
| consulting | 10 |
| note-taking | 8 |
| education | 6 |
| pharmaceutical-retail | 6 |
| ['ai-saas'] | 6 |
| AI | 6 |
| kdo | 6 |
| 决策 | 5 |
| skill-engineering | 4 |
| management | 4 |
| ['master'] | 4 |
| ['healthcare'] | 4 |
| agent-infrastructure | 3 |
| policy-compliance | 3 |
| learning | 3 |
| SaaS | 3 |
| execution | 2 |
| e-commerce | 2 |
| product-design | 2 |
| decision-making | 2 |
| product-strategy | 2 |
| risk-warning | 2 |
| ['yitang'] | 2 |
| structured-thinking | 2 |
| 产品 | 2 |
| 信息素养 | 2 |
| 落地 | 2 |
| 认知 | 2 |
| 分销系统 | 2 |
| financial-model | 2 |
| 私域电商 | 2 |
| decision-science | 2 |
| personal-life | 1 |
| strategy | 1 |
| entrepreneurship | 1 |
| essence | 1 |

## 七、高危卡片清单（示例）

以下卡片同时存在多个高危问题标签，需优先处理：

| 文件路径 | 状态 | Author | Reviewer | Source数 | Confidence | Trust | 问题标签 |
|---|---|---|---|---|---|---|---|
| 30_wiki/concepts/master-ai-info-literacy.md | enriched | legacy | (空) | 1 | 0.9 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-antifragile-checklist.md | enriched | legacy | (空) | 1 | 0.88 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-cognitive-bias-checklist.md | enriched | legacy | (空) | 1 | 0.85 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-decision-hygiene.md | enriched | legacy | (空) | 1 | 0.9 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-first-principles.md | enriched | legacy | (空) | 1 | 0.85 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/master-systems-thinking.md | enriched | legacy | (空) | 1 | 0.85 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/concepts/yt-entrepreneur-industry-forecast.md | enriched | legacy | (空) | 2 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-entrepreneur-key-hypotheses.md | enriched | legacy | (空) | 2 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-entrepreneur-product-core.md | enriched | legacy | (空) | 6 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-research-competitor-toolkit.md | reviewed | legacy | (空) | 2 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-research-expert-interview.md | reviewed | legacy | (空) | 2 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-research-hypothesis-test.md | reviewed | legacy | (空) | 2 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-research-industry-canvas.md | reviewed | legacy | (空) | 2 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-research-intelligence-map.md | reviewed | legacy | (空) | 1 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-research-osl-framework.md | reviewed | legacy | (空) | 2 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/concepts/yt-tool-product-core-canvas.md | enriched | legacy | (空) | 3 | 0.85 | medium | no-reviewer;high-conf-low-trust |
| 30_wiki/tools/yt-pitch-metaphor.md | enriched | legacy | (空) | 2 | 0.85 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/tools/yt-pitch-quantification.md | enriched | legacy | (空) | 2 | 0.85 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |
| 30_wiki/tools/yt-pitch-storytelling.md | enriched | legacy | (空) | 2 | 0.85 | (空) | no-reviewer;high-conf-low-trust;high-conf-no-trust;no-trust-level |

> 注：完整清单见 `kcard-inventory-2026-06-14.csv`，共 19 张高危卡片。

## 八、下一步建议

1. **阶段 1 元数据治理**：先为无 author/reviewer/id 的卡片补全基础字段；
2. **阶段 2 高危清理**：优先处理 `empty-or-tiny`、`no-source` + `no-author` + `no-reviewer` 的卡片；
3. **阶段 3 作者审查**：从老顽童、黄药师等关键作者开始；
4. **阶段 4/5 分层与 domain 审查**：按可信度和业务域抽样深入。
