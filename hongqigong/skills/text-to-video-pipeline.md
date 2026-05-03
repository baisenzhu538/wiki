# Text-to-Video Pipeline

## Overview

将黄药师产出的文字内容（`40_outputs/content/articles/`）render 成带配音的视频，输出到对应目录。

## Pipeline

```
articles/*.md
    ↓ 提取文字内容
HTML 编排（HyperFrames）
    ↓ render
MP4 视频（无声）
    ↓ 配音合成
MP4 视频（带配音）
    ↓
40_outputs/content/videos/
```

## Steps

### Step 1: 读取 article

从 `40_outputs/content/articles/` pickup 待 render 的文章。
读取 frontmatter 中的 target_user、title、source_refs。

### Step 2: 确定风格模板

根据 document type 选择 HyperFrames 模板：
- tutorial → 步骤编号突出、进度感强
- concept → 大标题 + 图文并排
- report → 数据可视化占位
- infographic → 信息密度高、分栏

风格参考：如果 article 中有 visual_style 指定，使用指定的；否则使用默认知识类风格。

### Step 3: 编写 HTML composition

使用 HyperFrames 框架，编写 index.html。
必须包含：
- 标题动画（开场）
- 核心内容逐段展示
- 数据/引用高亮
- 结束画面

### Step 4: 生成配音

使用飞书 TTS 或其他可用 TTS 方案，将文章正文转为语音。

### Step 5: Render

```bash
cd /path/to/hyperframes-project
npx hyperframes lint
npx hyperframes inspect
npx hyperframes render --quality draft --output preview.mp4
# 人工确认后
npx hyperframes render --quality production --output final.mp4
```

### Step 6: 合成配音

使用 FFmpeg 将 MP4 视频和配音音频合成为最终视频。

### Step 7: 输出

将最终视频保存到 `40_outputs/content/videos/`，文件名格式：
`{原article名}_{timestamp}.mp4`

## Known Issues

- HyperFrames 在中国大陆可能无法自动下载 Chrome，需要预先配置 `HYPERFRAMES_BROWSER_PATH`
- TTS 配音需要确认飞书 TTS API 的可用性和配额
