---
id: tool-demand-agent-l4-case-match
title: Agent做L4：案例库自动检索匹配——用历史摩擦点作为推演起点
type: tool
status: reviewed
confidence: 0.88
trust_level: high
domain:
- yitang
- five-step-method
source_refs:
- 60_feedback/diagnosis/diag_20260621_冰山策略增强_外部探索.md
- src_unknown
created_at: '2026-06-21'
updated_at: '2026-06-29'
author: 黄药师
reviewed_by: 欧阳锋
related:
- '[[tool-demand-iceberg-l4-job-map]]'
- '[[framework-multi-agent-research-architecture]]'
- business-research-skill-oscar-13-weapon-system
- framework-一堂五步法-泛产品设计
- '[[case-demand-milkshake-jtbd]]'
- '[[case-demand-ai-fitness-four-forces]]'
- '[[case-demand-elderly-smart-device]]'
- '[[case-demand-equestrian-three-tasks]]'
- '[[case-demand-financial-literacy]]'
- '[[case-demand-indonesia-insurance]]'
- '[[case-demand-pharma-bigdata]]'
- '[[case-demand-restaurant-hiring]]'
- '[[case-demand-rural-5g]]'
- '[[case-demand-silver-parenting]]'
- '[[case-demand-tier4-housekeeping]]'
- '[[case-demand-travel-agent]]'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---
# Agent 做 L4：案例库自动检索匹配

> 人的 L4 凭经验填 8 步表。Agent 不做从零推演——先检索案例库中相似任务的 8 步地图，用历史摩擦点作为推演起点。

## 核心流程

```
业务方向（一句话）
  ↓
Step 1: 关键词提取 → 检索案例库
  ↓
Step 2: 匹配最相似的 3-5 个案例
  ↓
Step 3: 提取共性摩擦点 → 注入推演上下文
  ↓
Step 4: Persona Agent 以历史摩擦点为起点推演（而非从零开始）
```

## Step 1: 关键词提取 + 案例检索

```python
# 从业务方向提取关键词
business = "社区生鲜配送服务"
keywords = ["生鲜", "配送", "社区", "零售", "食品", "O2O"]

# 检索 30_wiki/cases/ 下的需求案例
matches = []
for case in list_cases("30_wiki/cases/"):
    text = read(case)
    score = sum(1 for kw in keywords if kw in text.lower())
    if score > 0:
        matches.append((case, score))
matches.sort(key=lambda x: x[1], reverse=True)
```

## Step 2: 匹配最相似的 3-5 个案例

**可用的需求案例库（13 张）**：

| 案例 | 行业 | 核心教训 |
|:--|:--|:--|
| `case-demand-milkshake-jtbd` | 快餐 | 经典JTBD——用户"雇佣"奶昔是为了让早上的通勤不那么无聊 |
| `case-demand-ai-fitness-four-forces` | AI健身 | 四种力量博弈——用户想健身但焦虑隐私/习惯不去健身房 |
| `case-demand-elderly-smart-device` | 老年智能设备 | USP 模型中的用户边界——功能强≠老人会用 |
| `case-demand-equestrian-three-tasks` | 马术 | 功能/情感/社交三层任务的完美展演——不只骑马，是彰显身份 |
| `case-demand-financial-literacy` | 教育 | 刚性误判——家长说"很重要"但不付费 |
| `case-demand-indonesia-insurance` | 保险 | 场景错配——印尼寿险在错误场景推广 |
| `case-demand-pharma-bigdata` | 医药 | 评估三角形实战——大数据私有化在创新药的切入机会判断 |
| `case-demand-restaurant-hiring` | 餐饮 | 频次高估——麦家小馆以为天天招人，实际季度 |
| `case-demand-rural-5g` | 通信 | 普遍性误判——偏远县域5G，人口基数太小 |
| `case-demand-silver-parenting` | 养老 | 冰山模型完整应用——银发育儿的六层深挖 |
| `case-demand-tier4-housekeeping` | 家政 | 天花板误判——四线城市的家政市场远小于预估 |
| `case-demand-travel-agent` | 旅游 | 隐性需求被忽略——旅行攻略Agent没发现用户真正要的是"安全感" |
| `case-yitang-jtbd-story-formula` | 通用 | JTBD 故事公式——从用户故事中提取需求的标准模板 |

## Step 3: 提取共性摩擦点

从匹配的案例中提取：
1. **用户的崩溃环节**——在哪一步最想放弃？
2. **为什么现有方案不 work**——土办法在哪一步最不靠谱？
3. **评估三角形误判**——哪些案例在普遍性/频次/刚性上踩过坑？

**提取格式**：
```
匹配案例：case-demand-elderly-smart-device
崩溃环节：L4 执行步骤——"老人打开App后不知道点哪里"
现有方案为什么不work：子女远程教，但老人记不住
踩过的坑：刚性误判——老人说"想学"但不练

匹配案例：case-demand-tier4-housekeeping
崩溃环节：L4 定位步骤——"找不到靠谱的阿姨"
现有方案为什么不work：熟人介绍质量不稳定
踩过的坑：天花板误判——四线城市的付费意愿远低于预估
```

## Step 4: 注入推演上下文

将提取的共性摩擦点作为 Persona Agent 推演的起点：

```
Persona Agent 推演 Prompt 增加：
"以下是类似场景下真实用户最痛苦的环节（来自案例库）：
  1. [摩擦点1]
  2. [摩擦点2]
  3. [摩擦点3]
请在你的推演中优先检查这些环节是否也会出现——如果出现，详细描述；如果没有，说明为什么你的场景不同。"
```

## Agent 执行指令

```python
def case_retrieve_and_inject(business_idea, persona_prompts):
    """案例检索 + 推演注入"""
    # 1. 提取关键词
    keywords = extract_keywords(business_idea)
    
    # 2. 检索案例库
    matches = search_cases(keywords, limit=5)
    
    # 3. 提取共性摩擦点
    friction_points = []
    for case in matches:
        fp = extract_section(case, "核心教训")
        friction_points.append(fp)
    
    # 4. 注入 Persona Prompt
    context = "以下是类似场景下真实用户最痛苦的环节：\n"
    for i, fp in enumerate(friction_points, 1):
        context += f"  {i}. {fp}\n"
    context += "请在你的推演中优先检查这些环节。"
    
    for prompt in persona_prompts:
        prompt["system"] += f"\n\n{context}"
    
    return persona_prompts
```

## 失败模式

| 失败 | 症状 | 修复 |
|:--|:--|:--|
| 案例匹配不相关 | 检索到的案例行业/场景差异太大 | 扩展关键词或降低匹配阈值 |
| 历史摩擦点不适用 | 注入的摩擦点在当前场景未出现 | Persona 应说明"为什么不适用"而非硬套 |
| 案例太少 | 关键词匹配 <2 个案例 | 用 `kdo query` 语义搜索补充 |

---

*黄药师 · 2026-06-21 · Agent 原生策略 A-3*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设"历史摩擦点可以作为当前推演的有效起点"，但摩擦点的可迁移性高度依赖"场景同构性"——如果场景的底层逻辑不同（如 2B vs 2C、高频 vs 低频），历史摩擦点不仅无益，还可能误导推演方向。
- **边界**：在快速变化的新兴领域（如 AI Agent 生态），6 个月前的案例可能已经过时——历史摩擦点反映的是"旧环境"的约束，而当前环境可能已经完全不同。
- **反例**：一个从"外卖配送"案例中提取的"骑手崩溃环节"被注入到"企业级 SaaS 推演"中——完全无关的摩擦点会浪费推演时间并产生虚假关联。

**Allen Newell**（卡内基梅隆大学计算机科学教授，图灵奖得主）会质疑：案例注入的本质是"用先验知识约束搜索空间"——这在求解明确问题（如国际象棋）时有效，但在"需求探索"这种开放性问题中，先验约束可能变成"认知锁死"。真正的需求洞察往往来自"预期之外的发现"，而历史摩擦点的注入会让 Persona Agent 只关注"已知模式"——它不会问"还有什么我们没想到的"，而是问"历史摩擦点有没有出现"。
