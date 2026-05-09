---
title: "黄药师 2026-05-08 工作审查"
reviewer: 欧阳锋
created_at: "2026-05-09"
status: open
---
# 黄药师 2026-05-08 工作审查

## 审查范围

| # | 文件 | 当前评级 |
|---|------|:------:|
| 1 | [[yt-entrepreneur-five-step-method.md]] | **D** |
| 2 | [[yt-entrepreneur-scientific-method.md]] | **D** |
| 3 | [[yt-entrepreneur-fundraising.md]] | **D** |
| 4 | [[yt-management-scientific-hiring.md]] | **B+** |
| 5 | [[yt-management-goal-management.md]] | **B+** |

附带：[[health_2026-05-08.md]] 健康巡检

---

## 一、模式 A：三步编译法的三种失败形态（3 张 D 级卡）

以 `five-step-method` 为典型标本，逐段诊断：

### 失败形态 1：Source_refs 为空 — 溯源断裂（F-KDO-010）

```yaml
source_refs: []
```

前端写着 `> 来源：一堂课程体系`，但 `source_refs` 是空数组。读者无法验证 Condense 内容是从哪个源文件提取的。EC 手册 CF-012「所有声明必须可追溯到不可变源」— P0 违规。

### 失败形态 2：Condense 是模板填充，不是浓缩

```markdown
### 核心定位
一堂五步法在一堂知识地图中的位置：预判阶段/核心框架。

### 关键概念
- 本课程属于一堂「预判阶段/核心框架」模块
- 一堂课程强调「科学创业」方法论
```

全是目录级信息（"这门课在哪里"），没有课程级内容（"这门课教了什么"）。三步编译法的 Condense 要求提取**该课程特有的核心结论**——比如五步法中每一"步"的判定标准和常见错误——而不是描述它在课程树里的坐标。

### 失败形态 3：Critique 是复制粘贴

三张模式 A 卡的 Critique 段是同一段话改了几个字：

> 「本卡片内容基于一堂课程体系和目录提取……默会知识未能完全转化」

真正的 Critique 必须**针对该课程的具体主张**提出质疑——比如五步法中"关键假设优先"这个原则，在什么情况下是错的？是否有创业公司因为跳过需求验证直接做增长反而成功的反例？

### 失败形态 4：Synthesis Self-link

`scientific-method.md` 的 Synthesis 段 wikilink 了自己：

```markdown
- [[yt-entrepreneur-scientific-method]] — 科学理念，底层世界观
```

这是 F-KDO-009（虚假关联）的变体。

---

## 二、模式 B：接近合格，仅缺 source_refs（2 张 B+ 级卡）

`scientific-hiring` 和 `goal-management` 两张卡的三步编译质量明显高于模式 A：

- Condense 有实质内容：STAR 追问法、行为面试层级、OKR 脱钩绩效策略
- Critique 有针对性：文化匹配→similarity bias；脱钩绩效→KPI 文化冲突
- Synthesis 有跨学科锚点：McClelland、Google Project Aristotle、卡尼曼

**唯一缺陷**：`source_refs: []` 仍为空。补上即可升 A。

---

## 三、附带：健康巡检异常

来自 [[health_2026-05-08.md]]：

| 异常 | 数量 | 说明 |
|------|:----:|------|
| 孤立页面 | 26 | 其中 ~18 个 yt-* 概念卡无任何入链 — 最小修复：链入 [[yt-system-course-catalog]] |
| 重复页面 | 3 | `kdo_product_design_agent_final` ≈ `obsidian-kdo-内容产出工作流`（dist=10），建议合并 |
| TODO 残留 | 0 | ✅ 干净 |

---

## 四、修复清单（按优先级）

| 优先级 | 动作 | 涉及文件 |
|:------:|------|------|
| **P0** | 三张模式 A 卡退回 draft，重写三步编译 | five-step-method, scientific-method, fundraising |
| **P0** | 五张卡全部补 `source_refs` | 全部 5 张 |
| **P1** | 修复 scientific-method 的 self-link | scientific-method |
| **P2** | 18 个 yt-* 孤立页面链入 course-catalog 或 map index | 见巡检报告 |

---

## 五、修复规范

退回 draft 的操作：
```yaml
status: draft          # 从 enriched 改回
# 删除 reviewed_by 和 review_date 字段
```

重写三步编译的底线（与 EC 迁移提案决策记录一致）：
1. **Condense**：从源材料提取 ≥3 条该课程独有的核心结论，不是目录改写
2. **Critique**：≥1 条质疑必须**指名具体假设或边界**（EC 决策第 2 条）
3. **Synthesis**：每个 wikilink 指向不同页面，不自指
4. **source_refs**：指向 `00_inbox/` 中的实际源文件路径

---

*修完通知我复审。三张模式 A 卡是 Sprint 1 L1 Lint 扩展上线前必须清掉的债务——`source_refs` 为空的卡在 Lint 扩展后会直接报 P0。*
