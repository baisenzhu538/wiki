# Storyboard: Knowledge Delivery OS 快速上手指南：把散落知识变成可交付资产

## Style Guide

- **Color palette:** `--color-primary: #E5A028` (amber) / `--color-accent: #FFFFFF` (white) / `--color-bg: #0A0A0A` (near-black) / `--color-text: #F5F5F5` (off-white) / `--color-muted: #888888` (gray) / `--color-danger: #EF4444` (red) / `--color-success: #4ADE80` (green)
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
| 1 | 1 | — | Title Card | 黑底。KDO logo 居中淡入。下方副标题："快速上手指南"。最底部一行小字："Knowledge Delivery OS"。 | 5s |
| 2 | 1 | "你是不是这样的人？" | Text Reveal | 黑底。白色问号从屏幕中央放大出现。然后缩小移至左上角。 | 3s |
| 3 | 1 | "收藏夹里躺着 200 多篇" | Text Reveal | 数字通讯式出现："200+" 用 amber 闪烁，后跟"篇文章"。然后"一半以上没点开过第二次"以灰色小字出现在下方。 | 4s |
| 4 | 1 | "50 多篇笔记" | Text Reveal | 上一行向上移，新行出现："50+ 篇笔记" + "最近三个月没回头看过"。 | 4s |
| 5 | 1 | "10 几个课" | Text Reveal | 再添一行："10+ 个课程" + "开了个头没继续"。三行数据居中对齐。 | 4s |
| 6 | 1 | "713 块钱、1200 小时" | Text Reveal | 屏幕出现两个大数字："713 块" 和 "1200+ 小时"，数字通讯式跳动。然后数字逐个变暗。 | 5s |
| 7 | 1 | "换来的是什么？" | Text Reveal | 三行数据变灰。中央闪烁："然后呢？"。 | 4s |
| 8 | 1 | "老板周一要方案" | Metaphor Illustration | 快闪场景：日历显示"周一"、钟表倒计时、收藏夹图标。配上旁白："翻了三个小时，拼不齐一段"。 | 8s |
| 9 | 1 | "信息变不成资产" | Text Reveal | 金句出现："信息过载不是问题。信息变不成可以买单的资产，才是问题。" | 6s |
| 10 | 1 | "KDO" | Logo Reveal | KDO 品牌名从噪点中显现。字母一个一个出现，带机械噪点效果。 | 5s |
| 11 | 2 | "你不是不努力" | Text Reveal | 黑底大字："你不是不努力。你是努力停在了错误的地方。" 第二句用 amber 高亮。 | 6s |
| 12 | 2 | "只做两件事" | Text Reveal | 屏幕出现"收集 + 分类"，然后被一条红线划掉，改成"收集 + 分类 = 死胡同"。 | 5s |
| 13 | 2 | "印象笔记/Notion/Obsidian" | Comparison Split | 三个应用名称依次出现，每个名称下方有一行小字描述“失败现状"。例如：印象笔记 → "标签打了永远不看" | 10s |
| 14 | 2 | "消费行为 vs 生产行为" | Text Reveal | 左右对比：左侧红色"消费行为"，右侧琥珀色"生产行为"。中间有一条箭头指向右侧。 | 5s |
| 15 | 2 | "真正的知识管理" | Flow Diagram | 屏幕出现循环图：输入 → 加工 → 交付 → 反馈 → 改进 → 输入。箭头逐个高亮。 | 8s |
| 16 | 2 | "KDO 工程化了这个闭环" | Flow Diagram | 循环图变形为水平流水线。出现 9 个圆角方块，每个方块代表一个工序。方块依次高亮并显示名称。 | 12s |
| 17 | 2 | "有了 KDO，你做得更清晰" | Text Reveal | 屏幕中央大字："不是做得更多。是做得更清晰。" | 5s |
| 18 | 3 | "KDO 不是什么" | Text Reveal | 列表式文字逐条出现："不是笔记软件" / "不是知识库" / "不是让你存更多的工具"。每行带红色叉号。 | 8s |
| 19 | 3 | "KDO 是一条流水线" | Flow Diagram | 屏幕中央出现漏斗动画。顶部倒入飞书文档图标、网页图标、聊天记录图标。漏斗内部 9 个发光节点依次闪烁。漏斗底部输出三个方块。 | 10s |
| 20 | 3 | "三种产出" | Flow Diagram | 漏斗消失。三个大方块平行展开："文竩" / "代码" / "能力"。每个方块下方拉出虚线连接到顶部“来源”标签。 | 8s |
| 21 | 3 | "三个月后一键追溯" | Terminal Demo | 终端截图。显示 `kdo trace <article_id>` 返回结果，列出原始文档、编译记录、交付版本。 | 8s |
| 22 | 3 | "不是存得更多，是产得更清晰" | Text Reveal | 金句出现："不是“存得更多”，是“产得更清晰”。" | 5s |
| 23 | 3 | "9 步流程之一：capture" | Terminal Demo | 终端界面。命令行输入 `kdo capture <url>`，回车后显示"已捕获飞书文档至 inbox"。光标闪烁。 | 6s |
| 24 | 3 | "之二：ingest" | Terminal Demo | 上一屏继续。输入 `kdo ingest`，显示"注册成功，wiki_id: xxx"。 | 5s |
| 25 | 3 | "之三：enrich" | Terminal Demo | 输入 `kdo enrich`，显示三步编译进度条：浓缩 → 批判 → 对标，依次变绿。 | 8s |
| 26 | 3 | "生肉 → 粥 → 菜" | Metaphor Illustration | 三帧快闪动画：左侧是一块生肉（灰色），中间是一碗粥（淡色），右侧是一盘菜（琥珀色高亮）。三者之间有箭头连接。 | 8s |
| 27 | 3 | "之四五六：route/produce/validate" | Terminal Demo | 三个命令快速展示：`kdo route` → `kdo produce` → `kdo validate`。每个命令带简短返回。 | 10s |
| 28 | 3 | "之七八九：ship/feedback/improve" | Terminal Demo | 后三个命令快速展示：`kdo ship` → `kdo feedback` → `kdo improve`。最后一行显示"状态: shipped"。 | 8s |
| 29 | 3 | "每一步都是可选的" | Text Reveal | 屏幕中央大字："可以只用 3 步。也可以用满 9 步。" | 4s |
| 30 | 4 | "传统做法" | Comparison Split | 左右分屏。左侧标题"传统做法"，一个墓碑图标出现在屏幕上，上面写着"谷歌分析.docx"。右侧标题"KDO 做法"，显示从飞书文档开始的流水线，7 个 CLI 节点序列通过。 | 12s |
| 31 | 4 | "传统做法 vs KDO" | Comparison Split | 左侧墓碑上长出青草，右侧节点之间有动态流光效果。最终右侧输出一篇文竩和一个绿色 checkmark。 | 8s |
| 32 | 4 | "文档写完就是墓碑" | Text Reveal | 屏幕中央大字："传统做法，文档写完就是墓碑。KDO 的做法，文档写完才是开始。" | 5s |
| 33 | 5 | "KDO 和 Obsidian 的关系" | Comparison Split | 左右分屏。左侧：Obsidian 图谱界面，温和绿色调，标签"花园"。右侧：终端 CLI 界面，琥珀色文字，标签"厨房"。两者之间有浅橙色传送带，光流流动。 | 10s |
| 34 | 5 | "花园与厨房" | Metaphor Illustration | 左侧是简约花园插画，有花朵和枝叶。右侧是简约厨房插画，有锅和灶台。中间有传送带连接，上面有果实在流动。 | 8s |
| 35 | 5 | "适合谁" | Text Reveal | 屏幕分为两栏。左栏标题"适合"，列出四个条件。右栏标题"不适合"，列出三个条件。 | 8s |
| 36 | 5 | "信息过载不是问题" | Text Reveal | 黑底。白色大字出现："信息变不成资产，才是问题。" | 4s |
| 37 | 5 | "结束语" | CTA Card | 黑底。KDO logo 居中。下方一行小字："让你的知识值得被交付。" | 5s |
| 38 | 5 | "—" | End Screen | 屏幕淡出至黑。底部小字：二维码 / 官方文档链接 / 版权信息。 | 4s |

**Visual types:** Title Card / Text Reveal / Flow Diagram / Terminal Demo / Comparison Split / Metaphor Illustration / CTA Card / Logo Reveal / End Screen

---

## Timing Summary

| Segment | Frames | Total Duration |
|---------|--------|---------------|
| 1 (Hook) | 1–10 | ~50s |
| 2 (知识流水线) | 11–17 | ~115s |
| 3 (KDO 是什么) | 18–29 | ~195s |
| 4 (典型工作流) | 30–32 | ~85s |
| 5 (Closing) | 33–38 | ~60s |
| **Total** | **38 frames** | **~8–10 min** |

---

## Production Notes

### Frame 3–6 — 数据通讯式跳动
- 数字出现方式参考电影《社交网络》开头的数据爆炸效果，但更极简
- "200+" / "50+" / "10+" 用 amber 色，其余文字用白色
- 数字变暗时加上轻微的破碎效果（几个小三角形分离）

### Frame 8 — 老板要方案场景
- 快闪式场景，不需要真实人物
- 日历、钟表、收藏夹三个元素简化为几何图形
- 倒计时动画增加紧迫感

### Frame 13 — 三大应用失败现状
- 不使用真实 App logo，用简单几何图形代替（矩形代表文档，圆角矩形代表笔记）
- 每个图形下方的失败现状用小字，灰色，带有自嘲感

### Frame 19 — 漏斗动画
- 漏斗形状简化为倒置梯形
- 9 个发光节点用小圆点，从上到下依次点亮，节点之间有流动光线
- 三类产物简化为三个小方块：文（文档图标）/码（代码符号）/⚡（能力）

### Frame 26 — 生肉→粥→菜
- 三帧快闪，每帧占屏幕三分之一
- 左侧是灰色生肉块，中间是白色粥碗，右侧是 amber 色菜盘
- 箭头用浅灰色虚线
- 这个比喻可能需要找设计师细化或用简约插画风格

### Frame 30–31 — 墓碑 vs 流水线
- 左侧墓碑用简单几何形状，灰色，上面写 .docx
- 墓碑上长青草用简单的绿色线条表示
- 右侧节点用圆角矩形框住，框内是命令名称
- 最终 checkmark 用亮绿色 #4ADE80

### Frame 33–34 — 花园与厨房
- 花园侧使用柔和自然色调（浅绿、米白），但不要太鲜艳
- 厨房侧保持 KDO 黑白琥珀
- 传送带用半透明 amber
- 最后合并时两者渐入 KDO logo

---

## Asset Checklist

- [ ] KDO logo 横版 + 竖版 (SVG, 白色/琥珀色双版本)
- [ ] 终端背景纹理（可选，可用纯色代替）
- [ ] 飞书文档图标简化版（用于 Frame 30）
- [ ] Obsidian 图谱界面模拟截图（用于 Frame 33）
- [ ] 简约花园插画 / 厨房插画（用于 Frame 34，可用简单几何形状代替）
- [ ] 墓碑图标简化版（用于 Frame 30）
- [ ] 生肉/粥/菜插画（用于 Frame 26，可用简约几何形状）
