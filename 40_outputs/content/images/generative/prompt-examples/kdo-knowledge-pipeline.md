---
title: KDO 知识流水线 — AI 图像生成 Prompt 示例
created_at: 2026-06-14
type: prompt-example
generator: midjourney-v8
aspect_ratio: 16:9
---

# KDO 知识流水线 — AI 图像生成 Prompt 示例

## 需求描述

为 KDO（Knowledge Delivery OS）创作一张概念图：把"知识从 raw input 到 delivered asset"的流转过程可视化。

## 五维拆解

| 维度 | 内容 |
|:---|:---|
| **主体** | 一条现代化的知识生产线 / 流水线 |
| **环境** | 悬浮在数字空间中的模块化工厂，背景是干净的浅灰蓝 |
| **光影** | 柔和的环境光 + 节点处的科技蓝光 |
| **构图** | 等轴测视角（isometric），从左到右展示流程 |
| **风格** | 极简科技插画，扁平化 + 微立体，信息图风格 |

## 最终 Prompt（Midjourney V8）

```text
A clean isometric knowledge delivery pipeline floating in a soft digital space, modular factory stations connected by glowing conveyor belts, raw notes and documents entering from the left, processed cards and articles moving through capture/compile/produce/validate/ship stages, final deliverables exiting as polished assets on the right, soft ambient lighting with subtle tech-blue node glows, minimalist tech illustration style, flat design with micro-3D depth, light gray-blue background, infographic aesthetic, crisp vector-like edges, no text, no watermark --ar 16:9 --style raw --no people, hands, blurry, low quality
```

## 执行方式

### Midjourney

1. 复制上方 prompt 到 Discord `/imagine`
2. 等待生成 4 张变体
3. 选最符合的一张 Upscale
4. 如需调整：单独改 `soft digital space` → `dark futuristic lab`，或 `isometric` → `top-down`

### Stable Diffusion / ComfyUI

```text
正向：
(isometric knowledge delivery pipeline:1.3), modular factory stations, glowing conveyor belts, documents and notes transforming into polished assets, soft ambient lighting, tech-blue glows, minimalist tech illustration, flat design with micro-3D, light gray-blue background, infographic style, crisp vector edges, no text

负向：
people, hands, text, watermark, blurry, low quality, deformed, extra fingers, photorealistic
```

### Flux

```text
Clean isometric illustration of a knowledge delivery pipeline. Modular stations process raw notes into polished assets. Soft blue glows. Minimalist tech style. Light background. No text. 16:9.
```

### DALL-E 3 / GPT Image

```text
Create a clean isometric illustration of a knowledge delivery pipeline. On the left, raw notes and documents enter a modular factory. The documents flow through several stations connected by glowing conveyor belts. On the right, polished articles and assets exit the pipeline. Use a minimalist tech illustration style with soft blue lighting, light gray-blue background, and no text or labels.
```

## 为什么这样写

- `isometric`：统一透视，适合流程图/概念图
- `modular factory stations`：明确主体是模块化的工作站
- `glowing conveyor belts`：表达流动和连接
- `soft ambient lighting with tech-blue node glows`：控制光影，避免死黑
- `--style raw`：减少 MJ 默认艺术化，更贴近信息图
- 负面词排除 `people, hands, text, watermark`：避免常见污染

## 迭代建议

| 轮次 | 修改 | 预期效果 |
|:---|:---|:---|
| V1 → V2 | 改 `light gray-blue` → `deep navy` | 深色科技风 |
| V2 → V3 | 加 `data particles flowing between stations` | 增强数据流动感 |
| V3 → V4 | 改 `isometric` → `top-down view` | 俯视图，更像系统架构图 |
