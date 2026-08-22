# GEO 战略卡一致性核对（2026-08-22）

## 背景
把这组结论与 KDO 知识库现有卡片对照，看是否有冲突、是否被覆盖：
1. SEO→GEO 范式转移：旧 SEO 的"多站/站群"投机玩法在 GEO 时代被 AI 去重识别而失效；正统"权威集中 + 内容质量"主线被强化。
2. 一服多域架构对 GEO **技术中性**：架构本身不加分不减分，关键在用法（正经多品牌各自独立 vs 相似站群伪装）。
3. 垂直/精准 = topical authority + 可被 AI 引用：把"垂直"定义为"成为某话题 AI 最想引用的来源"，而非窄。

## 一、核对对象（kdo_search 命中 + 读原文）
| 卡片 | 类型/状态 | 路径 |
|---|---|---|
| 渠道经济学：获客成本优化 | framework / enriched / conf 0.92 | 30_wiki/frameworks/yt-business-model-channel-economics.md |
| 品牌三度 | framework / reviewed / conf 0.85 | 30_wiki/frameworks/framework-brand-three-degree.md |
| 飞书文档发布引擎 SKILL | skill / enriched / 欧阳锋审 | 40_outputs/capabilities/skills/shared/feishu-publish/SKILL.md |
| GEO业务-最佳实践讨论 | raw source / ingested | 10_raw/sources/src_20260614_45ab8b35-GEO业务-最佳实践讨论.md |
| 产业 AI 落地案例集 | concept / reviewed | 30_wiki/concepts/industry-ai-cases.md（列 GEO 为营销服务） |

## 二、一致性结论：**无冲突，三处印证**
| 对话结论 | KDO 对应卡 | 判定 |
|---|---|---|
| 权威集中、不要摊薄到多个弱域名 | 渠道经济学：「获客渠道不是越多越好，而是需要优化组合」「渠道之间可能互相蚕食」 | ✅ 一致 |
| GEO 重权威/可信/可被引用，而非数量 | 品牌三度：「网红追求流量，创始人 IP 追求信任」「只做知名度不做美誉度会塌」 | ✅ 一致（信任/美誉度 ≈ GEO 的 authority/trust 信号） |
| 内容上 GEO 吃结构、吃可被引用 | 飞书发布 SKILL 已内置「GEO优化：标题关键词、结构化摘要、可引用片段」✅ | ✅ 一致，且 KDO 已落地，领先于对话结论 |

**粒度说明（非冲突）**：渠道经济学是"渠道组合"视角（付费/SEO/口碑…），把 SEO/内容列为单一渠道（low CAC / high LTV / high 可规模化），未具体下钻到"SEO 渠道内部的多域名 vs 单域名"。这与"内容渠道内集中权威"是互补粒度，不矛盾。

## 三、覆盖缺口（GAP）
KDO **没有**一张专属 GEO 战略卡覆盖以下三点：
- **G1** SEO→GEO 范式转移（多站群失效 / 权威集中被强化）。
- **G2** 一服多域架构对 GEO 技术中性（架构不加分不减分，关键在用法）。
- **G3** 垂直/精准 = topical authority + 可被 AI 引用。
- **原始材料未蒸馏**：`src_20260614_45ab8b35-GEO业务-最佳实践讨论.md` 把 GEO 当作"客户委托的投放业务（结果付费）"，仍停在 ingested source，未升为知识卡。

## 四、建议
- **A**：新增一张概念/框架卡（如 `concept-geo-paradigm-shift` 或 `framework-geo-content-strategy`），覆盖 G1–G3，并挂接 feishu-publish SKILL 的 GEO 能力作为"已落地实践"。
- **B**：把 raw source 蒸馏进该卡（说明 KDO 把 GEO 当作客户投放业务线，与"内容可被 AI 引用"战略互补）。
- **C**：走工厂流水线：notify 欧阳锋分发 → 老顽童/小昭建卡 → 欧阳锋终审。

## 五、本次核对动作记录
- 检索：kdo_search ×5（GEO / SEO多域名站群 / 内容策略垂直 / 答案引擎GEO优化 / GEO token 兜底）。
- 读卡：渠道经济学、品牌三度、飞书发布 SKILL 全文；raw source 与 industry-ai-cases 摘要。
- 结论：现有卡与对话结论**不冲突**，三处印证；缺一张 GEO 范式专属卡（G1–G3）。
