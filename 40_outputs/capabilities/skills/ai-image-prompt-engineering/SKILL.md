---
name: ai-image-prompt-engineering
title: AI 图像生成 Prompt 工程 — 从混沌关键词到可控视觉输出
type: capability/skill
status: draft
description: >
  2026 年 Midjourney、Stable Diffusion、DALL-E、Flux、Ideogram 等图像生成工具的
  prompt 工程框架：结构化公式、模型差异、token 加权、负面提示、迭代工作流。
triggers:
  - 需要用 Midjourney/SD/DALL-E/Flux 生成图片
  - 图片生成结果不稳定、风格不一致
  - 需要把自然语言需求翻译成高质量图像 prompt
  - 需要建立团队级 prompt 模板库
source_refs:
  - "AIML Insights (2026). Best Prompts for Image Generation in 2026. https://aimlinsights.com/prompts-for-image-generation/"
  - "LetsEnhance (2026). How to write AI image prompts like a pro. https://letsenhance.io/blog/article/ai-text-prompt-guide/"
  - "PromptArch (2026). Prompt Engineering Best Practices for 2026. https://promptarch.ai/blog/prompt-engineering-best-practices-2026"
tags:
  - ai-image-generation
  - prompt-engineering
  - midjourney
  - stable-diffusion
  - dall-e
  - flux
---

# AI 图像生成 Prompt 工程

## 1. 一句话定位

把 "我要一张图" 变成 **可重复、可调试、可团队协作** 的 prompt 生产系统。

---

## 2. 通用 Prompt 结构公式

### 2.1 五维公式

```text
[主体 Subject] + [环境 Environment] + [光影 Lighting] + [构图/镜头 Composition/Camera] + [风格/质感 Style/Texture]
```

**示例对比**：

| 版本 | Prompt | 问题 |
|:---|:---|:---|
| 差 | "一只猫" | 信息不足，模型自由发挥 |
| 好 | "A majestic Bengal tiger stalking through a lush tropical rainforest, dappled sunlight filtering through the canopy, rich greens contrasting with orange fur, lower-left third composition, National Geographic wildlife photography, ultra-detailed" | 每个维度都有控制 |

### 2.2 六维扩展版（专业输出）

```text
[主体] + [动作/姿态] + [环境] + [光影] + [色彩] + [镜头/构图] + [风格参考] + [质量词]
```

---

## 3. 各维度常用词库

### 3.1 主体（Subject）

- 人物：`professional business portrait`, `candid street photography`, `three-quarter view`
- 产品：`luxury product shot on marble surface`, `floating wireless earbuds`
- 场景：`cozy coffee shop interior`, `futuristic neon cityscape`

### 3.2 光影（Lighting）

| 效果 | Prompt 词 |
|:---|:---|
| 柔和自然光 | `soft diffused lighting`, `overcast`, `golden hour` |
| 戏剧化 | `chiaroscuro`, `dramatic shadows`, `Rembrandt lighting` |
| 产品感 | `studio lighting`, `softbox`, `rim light` |
| 氛围感 | `volumetric lighting`, `god rays`, `cinematic lighting` |

### 3.3 构图/镜头（Composition/Camera）

| 效果 | Prompt 词 |
|:---|:---|
| 特写 | `close-up`, `macro shot`, `chest-up framing` |
| 远景 | `wide shot`, `full body`, `environmental portrait` |
| 角度 | `low angle`, `bird's eye view`, `top-down`, `isometric` |
| 景深 | `shallow depth of field`, `bokeh`, `sharp focus on subject` |
| 镜头 | `35mm lens`, `85mm portrait lens`, `16mm wide-angle` |

### 3.4 风格/质感（Style/Texture）

| 风格 | Prompt 词 |
|:---|:---|
| 写实 | `photorealistic`, `hyperrealistic`, `lifelike` |
| 电影感 | `cinematic color grading`, `film grain`, `anamorphic` |
| 插画 | `illustrative`, `painterly`, `vector art` |
| 极简 | `minimalist`, `clean lines`, `negative space` |
| 高级编辑感 | `editorial style`, `museum quality`, `refined aesthetic` |

---

## 4. 模型差异与适配

### 4.1 Midjourney V7/V8

- **偏好**：短、高信号、逗号分隔的短语
- **参数**：`--ar 16:9`, `--style raw`, `--sref <url>`, `--no`
- **技巧**：
  - 用 `--style raw` 减少默认美化
  - 负面词用 `--no watermark, blurry, extra fingers`
  - 风格引用用 `--sref`

### 4.2 Stable Diffusion 3.5 / ComfyUI

- **偏好**：结构化、加权关键词
- **语法**：`(blue sky:1.5)` 增加权重，`(blurry:0.5)` 降低权重
- **技巧**：
  - 负面 prompt 单独字段
  - 配合 ControlNet 控制姿态/构图
  - 用 LoRA 固定风格/人物

### 4.3 DALL-E 3 / GPT Image

- **偏好**：自然语言段落、多轮对话修改
- **限制**：不支持负面 prompt
- **技巧**：
  - 说"要 YY"而不是"不要 XX"
  - 适合风格迁移和概念图

### 4.4 Flux

- **偏好**：短而精确的 prompt
- **特点**：文字渲染能力较强
- **技巧**：明确主体和场景，避免过度堆砌

### 4.5 Ideogram

- **优势**：字体/文字渲染
- **场景**：Logo、海报、带文字的设计

---

## 5. Token 加权与负面提示

### 5.1 Token 加权

| 平台 | 语法 | 示例 |
|:---|:---|:---|
| Midjourney | `::` | `blue sky::2 mountain::1` |
| Stable Diffusion | `()` / `()` + `:` | `(blue sky:1.5)` |
| ComfyUI | 同上 | 同上 |

### 5.2 负面提示（Negative Prompt）

**通用负面词库**：

```text
watermark, signature, text, blurry, low quality, deformed, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, ugly, duplicate, morbid, mutilated
```

**平台差异**：
- Midjourney：用 `--no`
- SD/ComfyUI：独立 negative prompt 字段
- DALL-E：不支持，改用正面描述排除

---

## 6. 迭代工作流

```
Step 1: 写初版结构化 prompt（五维公式）
Step 2: 生成 4 张变体，观察失败模式
Step 3: 每次只改一个维度（光影/构图/色彩/主体）
Step 4: 固定满意的维度，微调剩余维度
Step 5: 上采样/精修（upscale + inpaint）
```

**迭代原则**：
- 一次只改一个变量
- 记录每轮修改和结果
- 用 seed 固定可复现

---

## 7. 团队 Prompt 模板库

建议按场景沉淀模板：

```
prompts/
├── product-shot.md        # 产品图
├── portrait.md            # 人像
├── social-media-poster.md # 社媒海报
├── illustration.md        # 插画
├── concept-diagram.md     # 概念图
└── brand-style-<name>.md  # 品牌视觉宪章
```

每个模板包含：
- 固定维度词
- 可变占位符
- 平台参数
- 参考案例

---

## 8. 与现有 skills 的关系

- `design-prompt-iteration`：人给反馈 → agent 翻译为 prompt 修改
- `visual-prompt-system`：SROM Visual OS，含品牌宪章+拼贴海报模板
- 本 skill：通用图像 prompt 工程方法论

---

## 9. 示例：从产品需求到最终 Prompt

**需求**：给一款高端护肤品拍电商主图

**需求拆解**：
- 主体：深蓝色玻璃瓶精华液
- 环境：大理石台面 + 水波纹
- 光影：柔和晨光、无硬阴影
- 构图：俯视 45°、产品居中
- 风格：高端商业摄影

**Midjourney Prompt**：

```text
Luxury cobalt blue glass serum bottle on white marble surface, clear water ripples around the base, soft morning diffused light, no harsh shadows, top-down 45-degree angle, product-centered composition, premium skincare commercial photography, ultra-detailed, photorealistic --ar 4:5 --style raw --no watermark, text, hands
```

### 更多示例

- **KDO 知识流水线概念图**：`40_outputs/content/images/generative/prompt-examples/kdo-knowledge-pipeline.md`
  - 含 Midjourney / SD / Flux / DALL-E 三平台适配版本
  - 含迭代建议

---

## 10. 常见错误

| 错误 | 后果 | 修正 |
|:---|:---|:---|
| 只写 "beautiful" "high quality" | 模型忽略，输出平庸 | 替换为具体维度描述 |
| 一次改多个变量 | 不知道哪个变量生效 | 每次只改一个维度 |
| 负面词写 "不要 XX" | DALL-E 不理解 | 改写为正面描述 |
| 忽视平台差异 | 同一个 prompt 在不同平台效果差很多 | 按平台调整语法和长度 |
| 不用参考图 | 风格不可控 | 用 `--sref` / IPAdapter / 风格模板 |
