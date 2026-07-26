---
id: task_20260726_wangyuyan-bfm-yb-insights
task_id: 205
assignee: 飞书老顽童
status: queued
created_at: 2026-07-26
updated_at: 2026-07-26
domain: system
priority: P1
source: 00_inbox/半肥猫月白老朱线下聚会/
---

# 半肥猫+月白线下聚会 · 暗知识卡片化

## 任务目标

从半肥猫+月白+老朱线下聚会录音中提取可复用方法论，产出4张新卡+2张已有卡注入。不打断#204。

## 素材

| 文件 | 路径 |
|:--|:--|
| 交流录音 | `00_inbox/半肥猫月白老朱线下聚会/AI应用研讨-半肥猫月白老朱-交流录音.txt` |
| 事后笔记 | `00_inbox/半肥猫月白老朱线下聚会/AI应用研讨-半肥猫月白老朱-事后笔记.txt` |

## 卡片规格

### 新卡（2张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 1 | tool-yb-cross-quadrant-prompt-framework | tool | 十字象限提示词结构化框架 | 月白三轴框架：X轴短词(探索风格)↔长词(稳定要素) / Y轴精准(数据/指令/物理属性)↔模糊(参考图) / Z轴艺术↔商业。每象限适用场景+典型提示词模板。核心原则："结构化足够好，没有幻觉，几乎可以无限接近"(L726-728) |
| 2 | dk-bfm-compression-path | dk | 压缩路径：从万字规范到40条铁规 | 半肥猫+老朱案例：1000字→30万字→40条铁规。15天完成5-6人半年工作。三步压缩法：穷举(迭代至30万字)→合并(去重聚类)→提炼(40条可记忆铁规)。暗知识注入：半肥猫"AI不受压迫→回到本质"(L6476-6484)。与KDO建模方法论完全同构 |
| 3 | concept-ai-co-learning | concept | AI共学模式：人+AI共学课程→固化知识→产生Skill | 老朱口述(L6752-6756)："我跟AI一起在学课程，把知识固化，不断交互来问，在里面产生skill"。核心模式：不是人教AI也不是AI教人——是双向共学，AI做"脚手架"放大人的学习效率。桥接#204协作双目标哲学+协作底层哲学(#202) |
| 4 | dk-ai-cross-domain-inference | dk | AI跨域自发推导：碎片中拼出完整框架 | 老朱"汗毛竖起"案例(L6820-6842)：AI从其他课程碎片中自动推导出业务公式。验证KDO跨域桥接底层机制——AI本质上在做"底层自洽→上层推导"。桥接闪电模型(#201)+协作底层哲学(#202) |

### 已有卡注入（等#204完成后执行，不打断老顽童）

| 目标卡 | 注入内容 | 时机 |
|:--|:--|:--|
| `concept-structured-naming-as-infrastructure` (#204产出) | 新增§"月白十字象限"——命名只是结构化的一个维度，提示词结构化是另一维度，同一哲学 | #204 reviewed后 |
| `framework-kdo-modeling-methodology` | 新增§"外部验证：半肥猫的压缩路径"——1000字→30万字→40条铁规=KDO pitfalls→组件库的独立验证 | 随时 |

## 暗知识清单（必须嵌入对应卡）

| 暗知识 | 锚点 | 去向 |
|:--|:--|:--|
| "agent无非就是加了一堆规则的对话框" | L1004-1010 | dk卡 |
| "结构化足够好，没有幻觉，几乎可以无限接近" | L726-728 | tool卡 |
| "设计师非常害怕摩擦——一有摩擦力创作就受影响" | L2114-2116 | tool卡·When NOT to Use |
| "AI品味取决于操作者审美和给的标准" | L662-672 | dk卡 |
| "你的命名，我的建筑"——命名是被逼出来的 | L2046-2072 | 注入#204 concept卡 |

**合计：4新卡 + 2注入**（2026-07-26飞书王语嫣迭代：2→4张，+AI共学模式+AI跨域自发推导）

## 验收标准

1. source_refs引用录音行号
2. tool卡必须含：三轴完整图示+四象限场景+每种场景的提示词模板
3. dk卡必须含：三步压缩法+与KDO建模方法论的同构对照
4. related ≥5且≥2跨域（链接月白命名卡+建模方法论+KDO组件库）
5. 提交前跑`kdo pre-submit`

## 边界

- **不覆盖**：中药行业讨论（非KDO域）
- **不覆盖**：国内外市场环境对比
- **不单独建域**：归入system域，工具层补充
- **不打断#204**：#204产出后再执行已有卡注入

## 建议标签（按 #206 Phase 2 规范）

| 卡片 | 建议标签 |
|:--|:--|
| tool-yb-cross-quadrant-prompt-framework | `method:thinking-tool` `audience:designer` `scene:execute` `source-person:月白` |
| dk-bfm-compression-path | `method:modeling` `audience:builder` `scene:reference` `source-person:半肥猫` `source-person:老朱` |
| concept-ai-co-learning | `method:collaboration` `audience:builder` `scene:diagnose` `source-person:老朱` |
| dk-ai-cross-domain-inference | `method:reasoning` `audience:builder` `scene:reference` `value-tier:macro` |

**合计：4张新卡 + 2张已有卡注入**
