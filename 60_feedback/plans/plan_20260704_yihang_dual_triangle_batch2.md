# 一行双三角第二批卡片生产计划

> 制定时间：2026-07-04
> 制定人：王语嫣
> 关联目标：完成一行双三角方法论第一版知识卡生产并制度化飞轮运行

---

## 一、计划背景

第一批 12 张核心卡已全部通过 `kdo pre-submit`（实际交付 14 张，含 2 张基于新输入洪七公飞书洞察的补充卡）。

第二批聚焦：**个人/专家级案例补充 + 边缘暗知识深挖**，让双三角知识库从「组织变革」延伸到「个人跃迁」和「高阶数据策略」。

---

## 二、第二批 4 张卡片清单

| 序号 | ID | 类型 | 标题 | 核心暗知识 | 素材来源 | 预计字数 |
|:---|:---|:---|:---|:---|:---|:---:|
| 1 | case-yihang-dual-triangle-tianmo-design-delivery | case | 一行双三角案例：天末4天商业级室内设计交付 | 审美可一夜之间建立；拆变量逐层稳定；零容错部分人工做 | 00_inbox/人机协作双三角/_processed/天末的案例口述_text.md；天末的双三角模型.jpg | 6000 |
| 2 | case-yihang-dual-triangle-ahao-product-selection | case | 一行双三角案例：阿豪电商选品函数替代模型 | 能写成函数的判断不要交给大模型；用白纸外包/临时合伙人解决组织资源缺口 | 00_inbox/人机协作双三角/_processed/阿豪案例的口述_page*.vlm.md；阿豪的双三角模型.jpg | 6000 |
| 3 | case-yihang-dual-triangle-huazao-synthetic-data | case | 一行双三角案例：花总让AI先造数据破解工业级难题 | 数据稀缺时用仿真/合成数据破局；跨行业速解依赖快速学习上限 | 00_inbox/人机协作双三角/_processed/一堂双三角-跨行业速解工业级难题_vlm.md | 5500 |
| 4 | case-yihang-dual-triangle-chentian-knowledge-agent | case | 一行双三角案例：陈天从知识管理到多Agent系统 | 知识管理的核心不是存而是用；从人驱动到AI驱动；多Agent枕戈以待 | 00_inbox/人机协作双三角/_processed/陈天同学案例口述_text.md | 6000 |

---

## 三、每张卡的内容规格

沿用第一批 case 卡结构：

```markdown
---
frontmatter (id/type/title/status/author/reviewed_by/confidence/trust_level/...)
---

# 标题

> 一句话定义

## 一、背景
## 二、决策与行动
### 人类三角
### AI 三角
### 关键动作链
## 三、结果
## 四、可迁移洞察（3-5 条）
## 五、Critique（内部局限 + 外部攻击）
## 六、Synthesis（关联已有卡）
## 七、Action Triggers
```

---

## 四、产出依赖

- 依赖第一批 `concept-yihang-dual-triangle-core.md` 已通过 pre-submit
- 依赖 `method-dual-triangle-flywheel-engine.md` 已完整化
- 依赖 `tool-yihang-dual-triangle-canvas.md` 已定义画布结构

---

## 五、验收标准

1. 4 张卡全部通过 `kdo pre-submit`
2. 每张卡至少提炼 3 条带原文依据的暗知识
3. 每张卡明确关联第一批核心模型/方法卡
4. 全部纳入王语嫣飞轮日志追踪

---

## 六、风险

| 风险 | 应对 |
|:---|:---|
| 口述稿 OCR 质量影响暗知识提取 | 多页对照，不确定处标注待复核 |
| 案例之间暗知识重复 | 每张卡聚焦不同维度：审美/函数/数据/知识管理 |
| 第二批超时 | 单张控制在 6000 字以内，优先保证结构和暗知识 |
