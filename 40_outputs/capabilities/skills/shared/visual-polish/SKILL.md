---
name: visual-polish
description: "Polish AI-generated visual assets to remove AI-feel and template-feel. The visual parallel to content-production-polish — checks images, diagrams, slides, and charts for common AI artifacts. Use when 洪七公 or any agent produces AI-generated visuals that look 'too AI' — '去AI味', 'visual polish', 'make it look human-made', '这个图太AI了'. Routes through 洪七公."
version: 1.0.0
author: 黄药师
status: enriched
reviewed_by: 待审
updated_at: 2026-07-21
metadata:
  hermes:
    tags: [visual, polish, de-ai, design, image, quality]
    related_skills:
      - content-production-polish
      - visual-asset-analysis
      - comfyui-local
      - drawio-mcp-diagrams
      - presenton-ppt-generator
    caller: [hongqigong, huangyaoshi, laowantong]
---

# 视觉去 AI 味检查

> 文字有 AI 味，图片也有。文字润色有 Vikki 讲人话，视觉润色有洪七公讲人眼。
> 本 skill 是 `content-production-polish` 的视觉侧对称——不讲人话，讲人眼。

## 核心标准

好的视觉资产让人看不出是 AI 做的。坏的视觉资产一看就知道"这是 AI 跑的"。六个维度：

### 1. 模板感（Template Smell）

**症状**：AI 生成的图表/PPT 有强烈的"模板套上去"的感觉——所有元素太整齐、太对称、太完美。

| 检查项 | 标准 | 修复 |
|------|------|------|
| 对称性 | 不完全对称——真实设计有微妙的不对称 | 偏移一个元素 5-10px |
| 圆角 | 不全是同一圆角半径——真实设计混合圆角 | 主卡片 8px，内部元素 4px |
| 间距 | 不全是 8px 倍数——真实设计有"差不多"的间距 | 随机 ±2px 微调 |
| 对齐 | 不完全网格化——真实设计有刻意的错位 | 一个元素故意不对齐 |

### 2. 配色 AI 感（AI Color Palette）

**症状**：AI 默认配色——高饱和渐变、紫橙配色、霓虹色调。

| 检查项 | 标准 | 修复 |
|------|------|------|
| 饱和度 | ≤70%，不刺眼 | 降饱和 10-15% |
| 渐变 | 不用彩虹渐变 | 单色相渐变（同色深浅） |
| 配色数量 | 3-5 色，不用 10+ 色盘 | 减少到主色+辅色+强调色 |
| 色盲友好 | 不用红绿做唯一区分 | 加纹理/形状/标签 |

### 3. 构图 AI 感（AI Composition）

**症状**：中心对称构图、元素漂浮感、缺少视觉锚点。

| 检查项 | 标准 | 修复 |
|------|------|------|
| 视觉锚点 | 有明确的视觉重心（≠画面中心） | 用三分法重新定位焦点 |
| 负空间 | 有呼吸感，不塞满 | 裁掉 15% 的次要元素 |
| 前景/背景 | 有层次感，不扁平 | 加阴影/模糊/大小对比 |
| 引导线 | 有隐含的视觉引导 | 加一条对角线或箭头 |

### 4. 细节 AI 感（AI Artifacts）

**症状**：AI 生图的经典 bug——手指畸形、文字乱码、纹理重复、边缘模糊。

| 检查项 | 标准 | 修复 |
|------|------|------|
| 人物 | 手指/眼睛/耳朵正常 | 重绘异常部位 or 裁剪 |
| 文字 | 图中文字可读（非乱码） | 用 Photoshop/Canva 替换文字层 |
| 纹理 | 不重复、不模糊 | 局部重绘 or 叠真实纹理 |
| 边缘 | 主体边缘清晰 | 修边 or 加描边 |

### 5. 信息图 AI 感（AI Infographic）

**症状**：信息图看起来"像模板"——图标太通用、布局太平均、缺少品牌感。

| 检查项 | 标准 | 修复 |
|------|------|------|
| 图标 | 不全是 Noun Project 通用图标 | 混用手绘/自定义图标 |
| 数据可视化 | 图表类型匹配数据（不用饼图表示时间序列） | 换正确的图表类型 |
| 标注 | 有直接标注而非图例 | 关键数据点加 inline 标注 |
| 品牌感 | 有一致的设计语言 | 统一字体/配色/图标风格 |

### 6. PPT AI 感（AI Slide Deck）

**症状**：AI 生成的 PPT——每页结构完全相同、标题位置不变、图片大小统一。

| 检查项 | 标准 | 修复 |
|------|------|------|
| 页面节奏 | 不重复同一布局连续 3 页 | 交替全 bleed/左右分栏/三列 |
| 标题位置 | 不总是在左上角 | 隔页换位置 |
| 图片大小 | 不全屏/半屏/1/3 屏交替 | 打破统一尺寸 |
| 过渡 | 有视觉连续性（颜色/形状/主题延续） | 加跨页元素 |

---

## 调用流程

```
洪七公产出视觉资产
  → visual-polish 六维检查
    → 逐维标注问题 + 修复建议
      → 修复 → 再查 → 通过
        → 交段王爷发布
```

## 快速诊断（替代完整六维）

如果只需要快速判断"这张图有没有 AI 味"，看三个信号：

1. **配色**：是不是紫橙渐变？→ AI
2. **构图**：是不是完美中心对称？→ AI
3. **细节**：文字是不是乱码/手指是不是畸形？→ AI

三个全中 = 🔴 AI 味重，建议全面检查。两个中 = 🟡 可发但有改进空间。一个或零 = 🟢 可发。

## When NOT to Use

| 场景 | 原因 |
|------|------|
| 非 AI 生成的手工设计 | 不需要去 AI 味——但要检查是否符合 VA 四维法 |
| 纯数据图表（Matplotlib/ggplot） | 这些本来就不应该"像人做的" |
| 工程截图/代码截图 | 不是视觉资产，是证据 |
| 紧急产出（用户说"不管直接发"） | 尊重 override |

## 参考

- `shared/content-production-polish/SKILL.md` — 文字侧去 AI 味（对称 skill）
- `framework-visual-analysis-four-dimensions` — VA 四维法（互补：VA 分析"设计师怎么想的"，visual-polish 分析"AI 怎么露馅的"）
- `agent-spec-hongqigong-multimodal` — 洪七公武器库
