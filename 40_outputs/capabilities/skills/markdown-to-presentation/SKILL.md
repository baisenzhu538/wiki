---
name: markdown-to-presentation
title: Markdown → 演示文稿 — Marp / Slidev / reveal.js 选型与工作流
type: capability/skill
status: stable
description: >
  把 Markdown 知识卡片/文章转换为可演示幻灯片的工具链：
  Marp（最简 PPT 导出）、Slidev（开发者友好）、reveal.js（最灵活网页幻灯片）。
  含安装、主题、导出 PDF/PPTX/HTML 的完整工作流。
triggers:
  - 需要把 Markdown 文章转成 PPT/幻灯片
  - 需要技术分享/演讲的视觉资产
  - 需要选择 Markdown 幻灯片工具
  - 需要批量生成演示文稿
source_refs:
  - "Marp. Markdown Presentation Ecosystem. https://marp.app/"
  - "Slidev. Presentation Slides for Developers. https://sli.dev/"
  - "reveal.js. The HTML Presentation Framework. https://revealjs.com/"
tags:
  - markdown
  - presentation
  - ppt
  - slides
  - marp
  - slidev
  - revealjs
---

# Markdown → 演示文稿

## 1. 一句话定位

把 wiki 里的 **Markdown 知识卡片/文章** 快速变成 **可演讲、可导出、可分享的幻灯片**。

---

## 2. 工具选型矩阵

| 工具 | 上手难度 | 导出格式 | 主题定制 | 动画/交互 | 最佳场景 |
|:---|:---:|:---:|:---:|:---:|:---|
| **Marp** | ⭐ 极低 | PDF, PPTX, HTML | CSS 主题 | 基础 | **快速导出 PPT/PDF** |
| **Slidev** | ⭐⭐ 低 | PDF, SPA, PPTX（插件） | Vue 组件 + 主题 | 丰富 | **技术分享、代码演示** |
| **reveal.js** | ⭐⭐⭐ 中 | PDF, HTML, PPTX（有限） | CSS + JS | 非常丰富 | **高度定制网页幻灯片** |
| **mdx-deck** | ⭐⭐⭐ 中 | HTML | React 组件 | 丰富 | React 开发者 |

---

## 3. Marp — 最快上手

### 3.1 安装

```bash
# VS Code 插件（推荐）
# 安装 Marp for VS Code

# CLI 版
npm install -g @marp-team/marp-cli
```

### 3.2 基本语法

```markdown
---
marp: true
theme: default
paginate: true
---

# 标题页

副标题在这里

---

# 第二页

- 要点一
- 要点二
- 要点三

---

# 第三页

![bg right:40%](image.png)

左侧文字，右侧图片
```

### 3.3 常用指令

| 指令 | 作用 |
|:---|:---|
| `<!-- _class: lead -->` | 标题页样式 |
| `![bg](image.png)` | 全页背景图 |
| `![bg right:40%](image.png)` | 右侧 40% 背景 |
| `<!-- paginate: true -->` | 显示页码 |
| `<!-- footer: "备注" -->` | 页脚 |

### 3.4 导出

```bash
# PDF
marp slide.md --pdf

# PPTX
marp slide.md --pptx

# HTML
marp slide.md --html
```

> ✅ **Marp 本地验证通过**（2026-06-14，Windows）：
> - `npm install -g @marp-team/marp-cli` 安装成功（v4.4.0）
> - 已将文章 `你的知识，睡了吗？` 转为幻灯片并导出 PDF
> - 源文件：`40_outputs/content/presentations/kdo-quickstart-slides/slides.md`
> - 输出：`40_outputs/content/presentations/kdo-quickstart-slides/slides.pdf`

---

## 4. Slidev — 开发者首选

### 4.1 安装

```bash
npm init slidev
# 或
npx slidev
```

### 4.2 基本语法

```markdown
---
# 封面
subtitle: 副标题
---

# 第一页

- 要点
- 要点

---

# 代码页

```python
print("Hello Slidev")
```

---

# 图片页

<img src="./image.png" class="rounded shadow" />
```

### 4.3 优势

- 原生支持代码高亮、代码片段聚焦
- 内置演讲者模式、演讲录制
- 可写 Vue 组件扩展
- 一键部署为 SPA

### 4.4 导出

```bash
# PDF
npx slidev export

# SPA
npx slidev build
```

---

## 5. reveal.js — 最灵活

### 5.1 安装

```bash
npm install reveal.js
```

### 5.2 基本结构

```html
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="dist/reveal.css">
    <link rel="stylesheet" href="dist/theme/black.css">
  </head>
  <body>
    <div class="reveal">
      <div class="slides">
        <section>Slide 1</section>
        <section>Slide 2</section>
        <section data-markdown>
          <textarea data-template>
            ## Markdown Slide
            - point 1
            - point 2
          </textarea>
        </section>
      </div>
    </div>
    <script src="dist/reveal.js"></script>
    <script>Reveal.initialize();</script>
  </body>
</html>
```

### 5.3 优势

- 最成熟，插件生态丰富
- 支持 Markdown、嵌套幻灯片、动画
- 可高度定制 CSS/JS

---

## 6. KDO 集成工作流

### 6.1 文章 → 幻灯片（Marp 推荐）

1. 从 `40_outputs/content/articles/` 选一篇文章
2. 用 `kdo query` 确认核心论点覆盖
3. 按 "一页一个论点" 拆 Markdown
4. 加 Marp frontmatter 和分页 `---`
5. 导出 PDF/PPTX
6. 存到 `40_outputs/content/presentations/`

### 6.2 知识卡片 → 演讲幻灯片

```markdown
---
marp: true
theme: default
---

# [[concept-name]]

> 核心洞察的一句话

---

## Claims

- 论点 1
- 论点 2
- 论点 3

---

## Action Triggers

| 场景 | 动作 | 指标 |
|:---|:---|:---|
| ... | ... | ... |
```

---

## 7. 输出目录规范

根据 `90_control/AGENTS.md`，洪七公的演示产出固定放到：

```
40_outputs/content/presentations/
├── <project-name>/
│   ├── slides.md          # 源文件
│   ├── slides.pdf         # 导出 PDF
│   ├── slides.pptx        # 导出 PPTX（可选）
│   ├── theme.css          # 自定义主题
│   └── assets/            # 图片素材
```

---

## 8. 与现有 skills 的关系

- `ai-image-prompt-engineering`：生成幻灯片配图
- `visual-prompt-system`：统一视觉风格
- 本 skill：把文字内容结构化为演示

---

## 9. 快速启动模板

**Marp 模板**：`40_outputs/capabilities/templates/checklist-proposal.md` 已有一个 checklist 模板，可扩展为幻灯片模板。

新建幻灯片的最小模板：

```markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #fff
---

<!-- _class: lead -->

# 标题

副标题 | 演讲者 | 日期

---

# 今天讲什么

1. 问题背景
2. 核心框架
3. 案例应用
4. 行动建议

---

# 问题背景

![bg right:40%](https://example.com/image.png)

- 痛点一
- 痛点二
- 痛点三

---

# 谢谢

Q&A
```

---

## 10. 下一步待建设

- [ ] 创建 2-3 个品牌主题 CSS（Marp）
- [ ] 建立 `presentations/` 目录下的项目模板
- [ ] 把一篇已有文章转成 Slidev 演示并导出
- [ ] 测试 Marp CLI 在 Windows/WSL 下的可用性
