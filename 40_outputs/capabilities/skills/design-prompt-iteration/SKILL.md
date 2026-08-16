---
name: design-prompt-iteration
type: capability/skill
status: published
description: 人（审美判断）+ Agent（prompt 翻译）的协作协议。设计师描述视觉问题，agent 翻译为 AI 图像工具的 prompt 修改——agent
  不看图不改图，只做自然语言→prompt token 的精确转换。触发词：prompt 迭代、改 prompt、设计不满意、光影/构图/色彩/质感调整。
---
# Design Prompt Iteration

## Purpose

人（审美判断）+ Agent（prompt 翻译）的协作协议。设计师描述视觉问题，agent 将其翻译为 AI 图像工具的 prompt 修改。agent 不看图、不改图——只做"自然语言 → prompt token"的精确转换。

## When to Use

- 设计师跑完一轮 AI 出图后，对结果有具体不满
- 需要迭代 prompt 的某个方向（光影/构图/色彩/质感）
- 想在不破坏其他变量前提下微调某个维度

## When NOT to Use

- 设计师说"不好看"但说不出哪里不好 → 先帮设计师拆解"哪里不好"，再走协议
- 需要判断 SOTA 哪个模型效果更好 → 这是人的审美判断
- 需要图片修改（调色/合成/剪裁） → 这是 Photoshop 的工作

---

## Protocol

### Input Format

设计师按以下格式提交反馈：

```
━━━━ 原始 prompt ━━━━
[上轮使用的完整 prompt]
━━━━ 使用工具 ━━━━
[Midjourney / Stable Diffusion / ComfyUI / DALL-E]
━━━━ 反馈 ━━━━
画面内容：[姿势/动作/对象/关系]
光影/氛围：[光方向/强度/色温/氛围词]
构图/景别：[镜头距离/角度/画面比例/负空间]
色彩/质感：[色板方向/材质/表面]
参考：[Eagle 路径或图片描述]
```

四个维度选填，只填要改的。不填 = 本轮不动。

### Output

agent 返回：

1. **修改后的完整 prompt**（只动反馈涉及的词，其余保留）
2. **修改说明**：每个改动对应哪个反馈维度
3. **风险提醒**（如有）：某些改动可能影响未提及的维度

---

## Translation Guide

### 画面内容 → Prompt

| 设计师说 | 翻译为 |
|---------|------|
| 人物太正面 | `three-quarter view`, `profile view`, `looking away` |
| 姿态僵硬 | `relaxed posture`, `natural stance`, `candid moment`, `mid-gesture` |
| 人物太少 | `group of N`, `crowd scene`, `multiple subjects` |
| 要加动作 | `holding X`, `reaching for X`, `interacting with X` |
| 关系太远 | `intimate framing`, `close proximity`, `touching shoulders` |

### 光影/氛围 → Prompt

| 设计师说 | 翻译为 |
|---------|------|
| 光影太硬 | `soft diffused lighting`, `overcast`, `bounced light`, `fill light` |
| 太暗 | `bright exposure`, `high key lighting`, `airy atmosphere` |
| 不够戏剧化 | `chiaroscuro`, `dramatic shadows`, `single light source`, `Rembrandt lighting` |
| 要晨光 | `golden hour`, `low angle sunlight`, `warm directional light` |
| 背景太亮喧宾夺主 | `dark atmospheric background`, `negative fill`, `subject spotlight` |
| 太平 | `volumetric lighting`, `god rays`, `rim light`, `edge light separation` |

### 构图/景别 → Prompt

| 设计师说 | 翻译为 |
|---------|------|
| 太远 | `close-up`, `intimate portrait`, `chest-up framing` |
| 太近 | `wide shot`, `full body`, `environmental portrait` |
| 构图太紧 | `negative space`, `wide composition`, `breathing room` |
| 要俯视 | `bird's eye view`, `top-down`, `overhead shot` |
| 要仰视 | `low angle`, `heroic perspective`, `looking up` |
| 主体太小 | `subject dominant`, `foreground emphasis`, `shallow depth of field` |

### 色彩/质感 → Prompt

| 设计师说 | 翻译为 |
|---------|------|
| 太艳 | `muted color palette`, `desaturated tones`, `subdued colors` |
| 太灰 | `vibrant`, `rich saturation`, `colorful`, `bold colors` |
| 太暖 | `cool color temperature`, `blue shift`, `teal and cyan tones` |
| 太冷 | `warm color temperature`, `golden tones`, `amber and orange` |
| 像塑料 | `photorealistic textures`, `material definition`, `surface detail` |
| 要电影感 | `cinematic color grading`, `teal and orange`, `film grain` |

### 风格泛化

| 设计师说 | 翻译为 |
|---------|------|
| 太写实 | `stylized`, `illustrative`, `painterly`, `abstract elements` |
| 太卡通 | `photorealistic`, `hyperrealistic`, `lifelike` |
| 要极简 | `minimalist`, `clean lines`, `negative space`, `essential forms` |
| 不够高级 | `refined aesthetic`, `editorial style`, `museum quality`, `curated` |

---

## Example

### Input

```
━━━━ 原始 prompt ━━━━
front-facing business portrait, bright white background,
full body shot, corporate lighting, blue suit, smiling
━━━━ 使用工具 ━━━━
Midjourney v7
━━━━ 反馈 ━━━━
画面内容：太正面 → 换成侧身45度，视线偏左
光影/氛围：背景太亮喧宾夺主
构图/景别：太远 → 推到胸口以上
色彩/质感：（不动）
参考：Eagle #品牌参考/SaaS/BrandX-about-page
━━━━
```

### Output

**修改后的 prompt**：
```
three-quarter view business portrait, gaze directed left,
chest-up framing, dark atmospheric background with subtle rim light,
corporate attire, navy suit, natural expression
--ar 4:5 --style raw
```

**修改说明**：
| 维度 | 原词 | 改为 | 对应反馈 |
|------|------|------|--------|
| 画面内容 | `front-facing` | `three-quarter view, gaze directed left` | 侧身45度 |
| 光影 | `bright white background` | `dark atmospheric background with subtle rim light` | 不喧宾夺主 |
| 构图 | `full body shot` | `chest-up framing` | 胸口以上 |
| 色彩 | （保留） | — | 不动 |

**风险提醒**：
- `dark atmospheric background` 如果环境光不够，人物可能融进背景。加了 `rim light` 做边缘分离。
- 头像近景可能丢失衣着细节。如果需要保留 → 回退到 waist-up。

---

## Tool-Specific Notes

### Midjourney
- 加 `--style raw` 减少 MJ 默认美化偏差
- 负面 prompt 用 `--no`（如 `--no smiling, full body`）
- 长宽比用 `--ar`，不是 SD 的 `--width --height`

### Stable Diffusion / ComfyUI
- 负面 prompt 单独一个字段
- 构图更多靠分辨率+CFG 而非 token
- 人物姿态可配合 ControlNet 精确控制

### DALL-E
- 不支持负向 prompt
- 写"不要 XX"不如写"要 YY"
- 对风格词敏感度低于 MJ/SD
