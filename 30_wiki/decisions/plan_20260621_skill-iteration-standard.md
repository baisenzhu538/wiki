---
id: plan_20260621_skill-iteration-standard
title: 知识卡片 → Claude Code Skill 迭代标准与全库扫描方案
type: improvement-plan
status: approved
domain:
  - master
  - kdo
source_refs:
  - .claude/skills/research/SKILL.md
  - .claude/skills/research-osint/SKILL.md
  - .claude/skills/research-cross-validation/SKILL.md
  - .claude/skills/research-web-scraping/SKILL.md
  - .claude/skills/research-financial-report/SKILL.md
  - .claude/skills/research-industry-report/SKILL.md
  - .claude/skills/research-expert-interview/SKILL.md
created_at: "2026-06-21"
author: 欧阳锋
reviewed_by: 欧阳锋
confidence: 0.90
related:
  - "[[framework-yitang-oscar-research]]"
  - "[[framework-yitang-18-strategy-cards]]"
  - "[[yitang-research-domain-digest]]"
---

# 知识卡片 → Claude Code Skill 迭代标准

> 审查对象：黄药师迭代的 7 个 research-* Skill
> 审查人：欧阳锋 · 2026-06-21
> 状态：✅ 批准，纳入 KDO 基础设施标准

---

## 一、黄药师 Skill 迭代审查结论

### 1.1 总体评价

黄药师以调研域 82 张卡片为原料，产出了 7 个 Claude Code Skill，整体质量 **B+/A-**。所有 Skill 满足：

- ✅ Hard constraints 安全边界明确
- ✅ 可执行步骤（Agent 可直接照做）
- ✅ wiki 卡片引用链（知识可溯源）
- ✅ 决策树/工具矩阵（选择路径清晰）

### 1.2 逐卡评级

| Skill | 评级 | 亮点 | 改进建议（不阻塞） |
|:------|:----:|:-----|:-----------------|
| `research`（总入口） | **A-** | 意图分类→路由→执行完整链 | 嵌入降龙十八掌决策树 |
| `research-osint` | **A** | 工具矩阵+CLI/API/费用+武器库桥接表 | — |
| `research-cross-validation` | **A-** | 六层框架+多重身份元模式+输出模板 | — |
| `research-web-scraping` | **A** | 需求→决策树→工具速查+合规CheckList | — |
| `research-financial-report` | **B+** | 步骤清晰案例实 | 补"创业三阶段报告策略" |
| `research-industry-report` | **B+** | 搜索七技+可信度分级 | 补 Doris 六要素画布 |
| `research-expert-interview` | **B+** | 十步法+5大陷阱 | 补"按专家类型变换提问" |

### 1.3 最大亮点：OSINT 武器库桥接表

OSINT Skill 中的 "与一堂武器库的桥接" 表格将新工具与已有的 18 掌一一对应：

```
第12掌"穷尽手段" → SpiderFoot 自动 200+ 源
第15掌"交叉验证" → ExifTool 技术验证
第10掌"按图索骥" → Sherlock 跨 300 平台
```

这种桥接让已有卡片的知识不浪费，新工具直接锚定在用户已有的认知框架上。**列为 Skill 迭代的标准模式。**

---

## 二、全知识库 Skill 化扫描方案

### 2.1 什么域适合 Skill 化

| ✅ 适合 | ❌ 不适合 |
|:--------|:----------|
| 有明确执行步骤的方法框架 | 纯概念/定义类知识 |
| Agent 可自主完成的操作流程 | 需要人类主观判断的领域 |
| 有决策树/工具矩阵的结构化知识 | 大量案例的集合 |
| 跨会话重复使用的操作手册 | 一次性内容产出 |

### 2.2 触发条件（三项均满足）

```
域 Skill 化触发条件：
1. 域内卡片 ≥20 张（知识规模足够）
2. 有 ≥1 张框架卡定义可重复的执行流程（有方法可包装）
3. 有 ≥2 个独立案例验证流程有效性（方法已被验证）
```

### 2.3 候选域优先级

| 优先级 | 域 | 卡片数 | 满足触发条件 | 建议 Skill 数量 |
|:------|:---|:------:|:-----------:|:--------------:|
| **P0** | Y 模型决策框架 | ~66 | ✅ | 3-4 个（决策总入口/假设验证/单元模型分析） |
| **P1** | AI 协作方法论 | ~20 | ✅ | 2-3 个（人机分工/五级能力/Agent 编排） |
| **P1** | 对抗思维/红队思考 | ~10 | ⚠️ 案例不足 | 待案例补充后 |
| **P2** | 管理工具箱 | ~8 | ❌ 卡片不足 | 暂缓 |
| **P2** | AIGC 设计域 | ~5 | ❌ 卡片不足 | 暂缓 |

### 2.4 执行方式

不是一次性全库扫描。各域生产者在自己的 Wave 计划末尾评估"本域是否满足 Skill 化条件"，满足则通知黄药师做工程实现。Skill 化是每个域的**收尾阶段**，不是独立的大扫除任务。

**标准流程**：
```
域卡片生产完成 → 评估触发条件 → 满足 → 黄药师写 Skill → 欧阳锋审核 → 发布
```

---

## 三、Skill 质量标准（参考调研域实践）

每个 Skill 必须包含：

| 要素 | 说明 | 调研域示例 |
|:-----|:-----|:-----------|
| frontmatter | name, version, allowed-tools, description, 触发词 | 已全部实现 |
| Hard constraints | 安全/合规边界，禁止操作 | SpiderFoot 不得攻击目标系统 |
| 执行步骤 | Agent 可照做的分步指令 | 黄金十步法每步一个动作 |
| 决策树/工具矩阵 | 什么场景选什么工具 | OSINT 决策树七分支 |
| wiki 卡片引用链 | 每步引用对应卡片 | 每个 Skill 末尾有相关卡片表 |
| Agent 调用方式 | CLI 命令/API endpoint/MCP | Firecrawl: `pip install firecrawl-py` |

**可选但鼓励**：
- 桥接表：新工具与已有框架的对应关系（如 OSINT 桥接表）
- 输出模板：标准化输出格式（如验证矩阵）
- 参考案例：具体场景的案例链接

---

## 四、指令

- **黄药师**：7 个 research-* Skill 通过审查，可继续维护。Y 模型决策域的 Skill 化列为下一优先级
- **老顽童/王语嫣**：各自产出的域在 Wave 计划末尾评估是否满足 Skill 化触发条件。满足则通知黄药师
- **全员**：新 Skill 放在 `.claude/skills/<name>/SKILL.md`，不要放在 vault 内的 `40_outputs/capabilities/skills/`（后者是给人类读的文档，前者是 Agent 可调用的 Skill）
