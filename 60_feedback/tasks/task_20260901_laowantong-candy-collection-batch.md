---
id: "585"
title: "学习candy合集+两天inbox素材批量产卡（翻译→调研→六层交叉→九层深挖→产卡入库）"
type: production
status: claimed
priority: P0
assignee: 老顽童
created_by: 王语嫣
created_at: 2026-09-01
updated_at: 2026-09-01
source_refs:
- 00_inbox/学习candy合集/
- 00_inbox/video_transcripts/
---

# #585 学习candy合集批量产卡任务（老朱 09-01 凌晨直令）

## 任务来源

老朱直令：candy 合集 + 两天进 inbox 的素材，按一堂调研方法论全网调研、六层交叉、九层深挖，产知识卡/skill/workflow/agent 入库，明早汇报。

## 素材清单与分域方案（王语嫣编排判定）

| 素材 | 域 | 产出形态 | 备注 |
|---|---|---|---|
| Live257 十指讲香模型（拆书《用数字讲故事》） | decision | 概念卡+方法卡（数字转换四原则） | 2240 行，含拆书完整正文 |
| Live260 AI口喷基本功（Truman 双 Partner 原文） | ai-collaboration | dk卡+case卡 | ⚠️传播限制「仅限内部不要外传」——落卡必须标注，正文脱敏引用 |
| AI×知识管理探索营（10篇Obsidian文档开源） | kdo | 方法卡+情报卡（外部参照） | 586 行 |
| 大卫·布鲁克斯 TED 3个谎言 | strategy（个人成长/价值观） | 概念卡 | **先翻译再产卡** |
| 大卫·布鲁克斯 芝大毕业演讲 | decision（求知方法论） | 概念卡+dk卡 | **先翻译再产卡** |
| 尼尔·雷克汉姆 SPIN 访谈 | sales | 方法卡（与 #320 SPIN 卡组互链） | **先翻译再产卡** |
| Jovida 调研报告×2 | ai-collaboration | case卡（AI Life Agent 竞品对标） | 已是中文调研稿 |
| WAIC 顶层思考 + MUSE DataPack | strategy | 框架卡（MUSE 四层模型）+概念卡 | 顶层文与 DataPack 交叉引用 |
| deep-debug 技能 | kdo/skill | **直接 skill 化**（40_outputs/capabilities/skills/shared/） | 已是 skill 格式，验收后注册 |
| 高阶 Skill 设计指南 | kdo | 方法卡+tool卡（与 skill 体系互链） | Anthropic 官方案例拆解 |
| 龙虾团队 OPT | strategy/management | 框架卡（One Person Team） | 产品设想稿 |
| Agent 大学 | ai-collaboration | 概念卡+情报卡 | 产品设想稿 |
| Eason 文化审计 DataPack | management | 方法卡（实事求是方法论） | ⚠️CHO 私有密级——只产方法论卡，人物细节脱敏 |
| BV 视频逐字稿 7 件 | sales/decision | 已由 01:14 值守拍诊断（英文 ASR 质量差）——SPIN 访谈与 candy 版重复，其余按 #585b 处置 | 撞车件不重复产卡 |

## 生产顺序（Wave 结构）

- **Wave 0（翻译）**：3 篇英文稿→中译版落 `00_inbox/学习candy合集/translations/`（指令见 90_control/parking-lot/tmp-translate-instruction-20260901.md）
- **Wave 1（高价值优先）**：Live257 数字讲故事 / Live260 口喷（脱敏）/ 高阶Skill设计指南 / MUSE 框架卡
- **Wave 2**：布鲁克斯×2 / SPIN 方法卡 / 龙虾OPT / Agent大学 / deep-debug skill 化
- **Wave 3**：Jovida case / 探索营方法卡 / Eason 方法论（脱敏）

## 生产规范（老朱直令要求）

1. **全网调研**：每个主题产卡前用 kdo-tools/web_search.py 搜外部验证源（框架卡必带「外部验证」节，老朱 08-09 铁律）
2. **六层交叉验证**：核心结论 ≥2 独立来源，逐条标 L1-L6 层级（research-cross-validation skill）
3. **九层深挖**：暗知识单层挖（决策代价/学习顿悟/反直觉），一卡一事细粒度
4. **终稿形态**：知识卡落 `30_wiki/`（concepts/frameworks/methods/cases/tools 按性质），skill 落 `40_outputs/capabilities/skills/shared/`，workflow 落 `40_outputs/capabilities/workflows/`——按内容性质归位，不硬塞
5. **frontmatter 全字段**：domain/aliases/discoverable_by/source_refs/related 一个不少（Agent 可发现性设计）
6. **传播限制**：Live260 与 Eason 两件必须标注密级+脱敏

## 验收标准

- 卡片数 ≥15（每素材 ≥1 卡，高价值素材 2-3 卡）
- 每张卡有 ≥1 外部验证源（概念/框架卡）
- 翻译件 3 篇落盘且行数对齐
- skill 化 ≥1 件（deep-debug）
- 全部 complete 提审，欧阳锋终审

## 执行报告

（完工后填写：交付物清单/验证输出/未做项/需要谁动作）
