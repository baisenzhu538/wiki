---
id: task_20260802_wangyuyan-christensen-related-backfill
task_id: 216
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
created_at: 2026-08-02
domain: strategy
priority: P1
source: 30_wiki/bridges/bridge-christensen-reverse-mapping.md
diagnosis: 60_feedback/diagnosis/diag_20260802_创新者的窘境_秦鹏拆书.md
updated_at: '2026-08-09T12:23:04.318910+00:00'
---

# #216 Christensen卡组 related补链（验收#7 TODO清零）

## 任务背景

#213（秦鹏拆书，14张卡）已终审PASS/A-，但**验收#7（related ≥5且≥2跨域）仍有TODO**：9张卡related只有2-4个真链接，未达≥5标准，且部分卡跨域不足（如`dk-qinpeng-three-corrections`的3个related只有1个跨域）。

**欧阳锋终审记录原文**："related<5×9补链留TODO（验收#7，建议王语嫣编排）"。

## 补链依据：bridge-christensen-reverse-mapping（#213产物）

`bridges/bridge-christensen-reverse-mapping.md` 已提供完整的四列映射表（引用文件→引用概念→原著位置→回填判定），是本次补链的钥匙：

### 映射表中已识别的可回填目标

| 引用文件 | 引用概念 | 原著位置 | 回填判定 |
|:--|:--|:--|:--|
| `yt-panproduct-execution-roi-analysis` | ROI是破坏性创新杀手 | Ch.7 | 🟡 P0 建议补原著锚点 |
| `yt-panproduct-execution-low-cost-mvp` | 破坏性创新无法被现有客户验证 | Ch.8 | 🟡 P0 |
| `tool-马易-风口痛点识别法` | 追逐风口=延续性创新 | Ch.2 | 🟢 建议确认来源标注 |
| `tool-遵循规模前倾原则设计组织架构` | Christensen批评规模前倾 | Ch.5 | 🟢 引用合理 |
| `tool-水水-保持系统冗余` | 冗余在经济下行被削减 | Ch.9 | 🔴 引用点不够精确 |
| `yt-product-kernel-mvp-design` | 产品内核↔破坏性创新 | Ch.6 | 🟡 建议阐明映射 |
| `yt-tool-unit-model-selection` | 破坏性创新对单元模型影响 | Ch.2+7 | 🟡 |
| `yt-tool-strategy-workshop` | 价值网络对战略影响 | Ch.2 | 🟡 |
| `yt-demand-quantitative-estimation` | 破坏性创新市场规模不可预测 | Ch.7 | 🟢 |
| `yt-demand-level-assessment` | 需求层次与价值网络 | Ch.2 | 🟢 |
| `case-demand-milkshake-jtbd` | JTBD | 《解答》Ch.3 | 🟢 |

## 补链目标（9张卡 → ≥5 related且≥2跨域）

### 需补链的9张卡与建议链接

| # | 卡 | 当前related | 建议补充（来自bridge映射表） | 达成 |
|:--|:--|:--|:--|:--|
| 1 | dk-qinpeng-three-corrections | 3 | +`yt-panproduct-execution-low-cost-mvp`（已有？查）+`tool-马易-风口痛点识别法`+`tool-遵循规模前倾原则设计组织架构` | ≥5，跨域 |
| 2 | dk-disruptive-innovation-insight-vs-survey | 3 | +`yt-demand-quantitative-estimation`+`yt-demand-level-assessment`+`tool-马易-风口痛点识别法` | ≥5，跨域 |
| 3 | case-feishu-disruptive-innovation | 3 | +`yt-tool-strategy-workshop`+`tool-遵循规模前倾原则设计组织架构`+`case-english-teacher-ai-agent` | ≥5，跨域 |
| 4 | case-english-teacher-ai-agent | 4 | +`yt-product-kernel-mvp-design`+`dk-ai-as-last-step-not-first`（#214产物）+`tool-qinpeng-ai-intelligent-service` | ≥5，跨域 |
| 5 | case-qinpeng-hardware-ai-amplification | 3 | +`tool-遵循规模前倾原则设计组织架构`+`yt-demand-quantitative-estimation`+`dk-ai-as-last-step-not-first` | ≥5，跨域 |
| 6 | dk-christensen-empirical-criticisms | 2 | +`framework-christensen-value-network`+`case-demand-milkshake-jtbd`+`concept-christensen-jtbd-link` | ≥5，跨域 |
| 7 | concept-christensen-jtbd-link | 3 | +`case-demand-milkshake-jtbd`+`framework-christensen-disruptive-innovation`+`tool-马易-风口痛点识别法` | ≥5，跨域 |
| 8 | concept-qinpeng-ai-as-amplifier | 4 | +`tool-马易-风口痛点识别法`+`ai-landing-scene-selection`+`dk-ai-as-last-step-not-first` | ≥5，跨域 |
| 9 | concept-qinpeng-knowledge-base-conversion | 4 | +`tool-马易-风口痛点识别法`+`tool-遵循规模前倾原则设计组织架构`+`framework-christensen-disruptive-innovation` | ≥5，跨域 |

## 验收标准

1. 9张卡每张 related ≥5 且 ≥2跨域（strategy/产品域/决策域/AI协作域）
2. 补链目标**必须真实存在**（生产前用`kdo query`或文件查找验证，禁止补死链）
3. 优先用bridge映射表中的深度引用文件（roi-analysis/low-cost-mvp/马易/规模前倾/水水冗余）
4. `dk-christensen-empirical-criticisms` 和 `concept-christensen-jtbd-link` 必须链接到bridge映射表提到的外部卡
5. 补链后跑 `kdo lint` 确认无死链新增
6. 提交前跑 `kdo pre-submit`，附输出

## 边界

- **只补related字段，不改正文内容**——#213内容已终审PASS，不得触碰
- 补链对象是30_wiki中真实存在的卡
- 参考 `bridge-christensen-reverse-mapping` 的P1建议（`yt-product-kernel-mvp-design` 阐明映射关系）
- 优先级P1——不阻塞主线，但TODO需清零
