# Storyboard: Knowledge Delivery OS 快速上手指南：把散落知识变成可交付资产

## Style Guide

- **Color palette:** `--color-primary: #E5A028` (amber) / `--color-accent: #FFFFFF` (white) / `--color-bg: #0A0A0A` (near-black) / `--color-text: #F5F5F5` (off-white) / `--color-muted: #888888` (gray)
- **Font:** JetBrains Mono (terminal/code), Inter (body text), Noto Sans SC (Chinese)
- **Animation language:** Clean reveals, no bounce, 0.3s ease transitions. Elements snap into place. Terminal cursors blink at 530ms intervals.
- **Aspect ratio:** 1920×1080
- **Brand elements:** KDO logo (minimalist block letters) top-left corner from Frame 2 onwards. Recurring motif: the "funnel" shape representing the 9-step pipeline.

> Style reference: KDO brand language — Bauhaus simplicity, black/white/amber, terminal aesthetics, structured whitespace.
> AVOID: generic "tech" aesthetic (blue/purple gradients on dark bg).

---

## Frame Map

| Frame # | Segment | Speaking Point | Visual Type | Description | Duration |
|---------|---------|---------------|-------------|-------------|----------|
| 1 | 1 | — | Title Card | 黑底。KDO logo 居中，淡入。下方副标题："快速上手指南"。最底部一行小字："Knowledge Delivery OS"。 | 5s |
| 2 | 1 | "你收藏了 200 篇文章" | Text Reveal | 黑底。白色数字从左到右逐字打出。先出 "200"，然后 "篇文章"。数字用 amber 高亮。 | 3s |
| 3 | 1 | "写了 50 篇笔记" | Text Reveal | 上一行向上移动。新一行打出 "50 篇笔记"。数字同样 amber。 | 3s |
| 4 | 1 | "参加了 10 个课程" | Text Reveal | 再添一行 "10 个课程"。三行文字垂直居中对齐。 | 3s |
| 5 | 1 | "然后呢？" | Text Reveal | 上面三行突然变成灰色。屏幕中央只剩"然后呢？"闪烁。字体放大。背景轻微噪点。 | 5s |
| 6 | 1 | "信息过载不是问题" | Metaphor Illustration | 左侧出现一排文件图标，逐个变灰、破碎、消失。右侧同时显示"信息过载不是问题。信息变不成可用的东西，才是问题。" | 10s |
| 7 | 1 | "今天这个视频" | Text Reveal | 黑底。淡入主题文字："把散落知识，变成可交付的资产"。字与字之间有短暂的出现间隔。 | 6s |
| 8 | 1 | "KDO" | Logo Reveal | KDO 品牌名从噪点中显现。字母一个一个出现，每个字母带有轻微的机械噪点效果。 | 5s |
| 9 | 2 | "大多数人的知识管理" | Comparison Split | 左半屏显示一排应用图标（印象笔记、Notion、Obsidian）。右半屏黑底，中央打出公式："收集 + 分类 = 死胡同"。 | 8s |
| 10 | 2 | "这叫信息管理" | Text Reveal | 屏幕中央大字："信息管理 ≠ 知识管理"。等号被一条红线划掉。 | 5s |
| 11 | 2 | "真正的知识管理" | Flow Diagram | 屏幕出现一个循环图：输入 → 加工 → 交付 → 反馈 → 改进 → 输入。箭头逐个高亮。 | 10s |
| 12 | 2 | "KDO 把这个闭环工程化了" | Flow Diagram | 循环图消失。出现 9 个圆角方块，横向排列。每个方块代表一步。方块依次高亮，显示名称。 | 15s |
| 13 | 2 | "每一步对应一种认知操作" | Text Reveal | 黑底白字。文字从上到下划入："捕获 → 注册 → 编译 → 路由 → 生产 → 验证 → 交付 → 反馈 → 改进"。 | 8s |
| 14 | 2 | "这些操作你本来就在做" | Text Reveal | 屏幕中央一句话："只是你没意识到，它们是一条流水线。" | 5s |
| 15 | 2 | "KDO 的价值" | Text Reveal | 两行文字出现：第一行"显性化、标准化"。第二行"可追踪、可复查"。 | 5s |
| 16 | 3 | "KDO 不是什么" | Text Reveal | 列表式文字逐条出现："不是笔记应用" / "不是知识库" / "不是又一个让你记东西的工具"。每行带有小型红色叉号。 | 8s |
| 17 | 3 | "KDO 是一条流水线" | Flow Diagram | 屏幕中央出现漏斗动画。顶部倒入各种格式的文件图标。漏斗内部 9 个发光节点依次闪烁。漏斗底部输出三类产物图标。 | 12s |
| 18 | 3 | "三种产出" | Flow Diagram | 漏斗消失。三个大方块平行展开："文章" / "代码" / "能力"。每个方块下方拉出一条虚线，指向顶部一个“来源”标签。 | 10s |
| 19 | 3 | "9 步流程之一：capture" | Terminal Demo | 终端界面。命令行输入 `kdo capture <url>`，回车后显示"已捕获飞书文档至 inbox"。光标闪烁。 | 8s |
| 20 | 3 | "之二：ingest" | Terminal Demo | 上一屏继续。输入 `kdo ingest`，显示"注册成功，wiki_id: xxx"。 | 7s |
| 21 | 3 | "之三：enrich" | Terminal Demo | 输入 `kdo enrich`，显示三步编译进度条：浓缩 → 批判 → 对标，依次变绿。 | 10s |
| 22 | 3 | "之四五六：route/produce/validate" | Terminal Demo | 三个命令快速展示：`kdo route` → `kdo produce` → `kdo validate`。每个命令带有简短的返回信息。 | 12s |
| 23 | 3 | "之七八九：ship/feedback/improve" | Terminal Demo | 后三个命令快速展示：`kdo ship` → `kdo feedback` → `kdo improve`。最后一行显示"状态: shipped"。 | 10s |
| 24 | 3 | "每一步都是可选的" | Text Reveal | 屏幕中央大字："可以只用 3 步。也可以用满 9 步。" | 5s |
| 25 | 3 | "三层产物和溯源链" | Flow Diagram | 横向时间线动画。从左到右：source → wiki → artifact。每个节点都可以点击展开详情。中间节点的箭头上写着"编译"。 | 10s |
| 26 | 3 | "一键追溯" | Terminal Demo | 小型终端截图。显示 `kdo trace <article_id>` 的返回结果，列出原始文档、wiki 页面、编译记录。 | 8s |
| 27 | 4 | "从飞书到 KDO" | Comparison Split | 左右分屏。左侧标题"传统做法"，显示飞书文档图标 → 分享链接 → 空白。右侧标题"KDO 做法"，显示同样的飞书文档，然后连接 7 个 CLI 命令节点，最终输出一篇文章 + green checkmark。 | 15s |
| 28 | 4 | "传统做法写完就结束" | Text Reveal | 屏幕中央大字："文档写完 = 结束 → 文档写完 = 开始" | 5s |
| 29 | 5 | "KDO 和 Obsidian 的关系" | Comparison Split | 左右分屏。左侧：Obsidian 图谱界面，温和绿色调，标签"花园"。右侧：终端 CLI 界面，琥珀色文字，标签"工厂"。两者之间有光带流动。 | 12s |
| 30 | 5 | "花园和工厂" | Metaphor Illustration | 左侧是一个简约的花园插画。右侧是一个工厂流水线插画。中间有一条传送带连接。 | 10s |
| 31 | 5 | "适合谁" | Text Reveal | 屏幕分为两栏。左栏标题"适合"，列出四个条件。右栏标题"不适合"，列出三个条件。 | 10s |
| 32 | 5 | "信息过载不是问题" | Text Reveal | 黑底。白字大字出现："信息变不成资产，才是问题。" | 5s |
| 33 | 5 | "结束语" | CTA Card | 黑底。KDO logo 居中。下方一行小字："让你的知识值得被交付。" | 6s |
| 34 | 5 | "—" | End Screen | 屏幕淡出至黑。底部小字：二维码 / 官方文档链接 / 版权信息。 | 4s |

**Visual types:** Title Card / Text Reveal / Flow Diagram / Terminal Demo / Comparison Split / Metaphor Illustration / CTA Card / Logo Reveal / End Screen

---

## Timing Summary

| Segment | Frames | Total Duration |
|---------|--------|---------------|
| 1 (Hook) | 1–8 | ~45s |
| 2 (知识流水线) | 9–15 | ~120s |
| 3 (KDO 是什么) | 16–26 | ~200s |
| 4 (典型工作流) | 27–28 | ~90s |
| 5 (Closing) | 29–34 | ~55s |
| **Total** | **34 frames** | **~8–10 min** |

---

## Production Notes

### Frame 6 — 文件破碎效果
- 使用简单的几何图形代表文件（矩形、圆角矩形），不需要真实文件图标
- 碎裂效果用几个三角形组成，渐变透明
- 关键词："变不成可用的东西"用 amber 色

### Frame 17 — 漏斗动画
- 漏斗形状不需要精确几何，简化为一个倒置的三角形/梯形
- 9 个发光节点用小圆点表示，从上到下依次点亮
- 三类产物图标简化为三个小方块，带有简单符号（文/码/⚡）

### Frame 19–23 — 终端演示
- 终端背景色：#0A0A0A
- 命令提示符：`$` 或 `➜`，用 amber 色
- 用户输入：白色
- 系统输出：灰色
- 字体：JetBrains Mono 14px 等宽
- 光标：南海壶形块光标，闪烁频率 530ms

### Frame 27 — 左右分屏对比
- 左侧使用飞书的品牌色（蓝色）作为点缀，但不要太多，避免破坏 KDO 黑白琥珀调
- 右侧 CLI 节点用圆角矩形框住，框内是命令名称
- 最终 checkmark 用亮绿色（#4ADE80），与整体 amber 调形成对比

### Frame 29 — 花园与工厂
- 花园侧使用柔和的自然色调（浅绿、米白），但不要太鲜艳
- 工厂侧保持 KDO 的黑白琥珀
- 中间传送带用淡色（半透明 amber）

---

## Asset Checklist

- [ ] KDO logo 横版 + 竖版 (SVG, 白色/琥珀色双版本)
- [ ] 终端背景纹理（可选，可用纯色代替）
- [ ] 飞书文档图标简化版（用于 Frame 27，避免真实 logo 版权问题）
- [ ] Obsidian 图谱界面模拟截图（用于 Frame 29）
- [ ] 简约花园插画（用于 Frame 30，可用简单几何形状代替）
- [ ] 简约工厂插画（用于 Frame 30，可用简单几何形状代替）
