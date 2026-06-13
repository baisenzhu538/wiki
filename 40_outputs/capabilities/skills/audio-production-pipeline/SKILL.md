---
name: audio-production-pipeline
title: 音频生产管线 — TTS / 配音 / 音乐 / 音频后期工作流
type: capability/skill
status: stable
description: >
  把文字内容（文章/卡片/脚本）转化为音频资产的完整管线：
  TTS（edge-tts 免费、ElevenLabs 高真实感）、AI 音乐生成（Suno/Udio）、
  音频编辑与增强（Descript/Adobe Podcast）。含工具选型、成本、输出规范。
triggers:
  - 需要把文章转成播客/音频
  - 需要为视频生成配音
  - 需要生成背景音乐/BGM
  - 需要清理/增强已有录音
source_refs:
  - "DIY AI (2026). Best AI Voice and Audio Tools in 2026. https://diyai.io/ai-tools/audio-generation/best-ai-audio-tools/"
  - "Cyberscap (2025). Best Free AI Text-to-Speech Tools in 2025-2026."
  - "edge-tts. https://github.com/rany2/edge-tts"
tags:
  - audio
  - tts
  - text-to-speech
  - music-generation
  - podcast
  - voiceover
---

# 音频生产管线

## 1. 一句话定位

把 wiki 里的 **文字内容** 变成 **可发布的音频资产**：TTS 配音、AI 音乐、音频后期。

---

## 2. 工具选型矩阵

### 2.1 TTS（文本转语音）

| 工具 | 成本 | 质量 | 中文 | 本地/云端 | 最佳场景 |
|:---|:---|:---:|:---:|:---:|:---|
| **edge-tts** | 免费 | ⭐⭐⭐ | ⭐⭐⭐ | 云端（Edge 语音） | **无 API key 快速配音首选** |
| **ElevenLabs** | 付费 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | API | 高真实感播客/有声书 |
| **Fish Audio** | 付费/免费 tier | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | API | 中文表达、角色语音 |
| **Play.ht** | 付费 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | API | 多语言配音/配音 |
| **Coqui TTS** | 开源 | ⭐⭐⭐ | ⭐⭐⭐ | 本地 | 技术团队自建 |
| **GPT-SoVITS** | 开源 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 本地 | 声音克隆 |
| **CosyVoice / F5-TTS** | 开源 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 本地 | 中文 TTS、声音克隆 |

### 2.2 AI 音乐生成

| 工具 | 成本 | 质量 | 商用 | 最佳场景 |
|:---|:---|:---:|:---:|:---|
| **Suno** | 付费/免费 tier | ⭐⭐⭐⭐ | 需确认授权 | 带人声的完整歌曲 |
| **Udio** | 付费/免费 tier | ⭐⭐⭐⭐ | 需确认授权 | 音乐动机/BGM 草图 |
| **AudioLDM 2** | 开源 | ⭐⭐⭐ | 自主 | 文本生成通用音频 |
| **Amphion** | 开源 | ⭐⭐⭐ | 自主 | 研究/音乐生成 |

### 2.3 音频编辑/增强

| 工具 | 成本 | 功能 | 最佳场景 |
|:---|:---|:---|:---|
| **Descript** | 付费 | 文字编辑音频、overdub、降噪 | 播客后期 |
| **Adobe Podcast Enhancer** | 免费 | 一键降噪、去混响 | 快速修复录音 |
| **ffmpeg** | 开源 | 剪辑、合并、转码、标准化 | 批量音频处理 |
| **Demucs** | 开源 | 人声/伴奏分离 | 混音/采样 |

---

## 3. edge-tts — 本地免费首选

### 3.1 安装

```bash
pip install edge-tts
```

### 3.2 基本使用

```bash
# 列出中文语音
edge-tts --list-voices | grep zh

# 生成音频
edge-tts --voice zh-CN-XiaoxiaoNeural --text "你好，这是测试" --write-media output.mp3

# 生成音频 + 字幕
edge-tts --voice zh-CN-XiaoxiaoNeural --text "你好，这是测试" --write-media output.mp3 --write-subtitles output.srt
```

> ✅ **本地验证通过**（2026-06-14）：在 Windows Python 3.12 环境，`pip install edge-tts` 后可直接使用。已生成测试文件：
> - `40_outputs/content/audio/test-edge-tts.mp3`
> - `40_outputs/content/audio/test-edge-tts.srt`

### 3.3 Python 批量脚本

```python
import edge_tts, asyncio

async def main():
    communicate = edge_tts.Communicate("你好，世界", "zh-CN-XiaoxiaoNeural")
    await communicate.save("hello.mp3")

asyncio.run(main())
```

### 3.4 参数调节

| 参数 | 说明 | 示例 |
|:---|:---|:---|
| `--rate` | 语速 | `-50%` 慢速，`+50%` 快速 |
| `--volume` | 音量 | `-50%` 小声，`+50%` 大声 |
| `--pitch` | 音调 | `+50Hz` 提高 |

---

## 4. ElevenLabs — 高真实感

### 4.1 特点

- 最自然的语音合成
- 支持声音克隆
- 支持多语言
- 需要 API key

### 4.2 Python 示例

```python
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="your-api-key")

audio = client.text_to_speech.convert(
    voice_id="21m00Tcm4TlvDq8ikWAM",
    output_format="mp3_22050_32",
    text="Hello, this is a test.",
    model_id="eleven_multilingual_v2",
    voice_settings=VoiceSettings(stability=0.5, similarity_boost=0.5)
)
```

---

## 5. Suno / Udio — AI 音乐

### 5.1 Suno

```text
Prompt 格式：
[风格描述], [情绪], [乐器], [用途]

示例：
Upbeat lo-fi hip hop, relaxed study vibe, soft piano and vinyl crackle, instrumental background music
```

### 5.2 Udio

更适合快速生成音乐动机和 BGM 草图。

### 5.3 商用注意

- 免费 tier 通常不可商用
- 付费 tier 需仔细阅读授权条款
- 建议保留生成记录和授权截图

---

## 6. KDO 音频工作流

### 6.1 文章 → 播客

1. 从 `40_outputs/content/articles/` 选文章
2. 用 `kdo clean-transcript` 把书面语改成口语化脚本
3. 拆分脚本为 3-5 分钟段落
4. edge-tts 批量生成音频
5. ffmpeg 合并音频 + 加片头片尾
6. 导出到 `40_outputs/content/audio/`

### 6.2 视频配音

1. 从视频脚本提取旁白
2. edge-tts / ElevenLabs 生成配音
3. ffmpeg 对齐音画
4. 生成字幕 SRT

### 6.3 输出目录规范

```
40_outputs/content/audio/
├── podcasts/
│   └── <episode-name>/
│       ├── script.md
│       ├── audio.mp3
│       └── subtitles.srt
├── voiceovers/
│   └── <project-name>/
│       ├── narration.mp3
│       └── subtitles.srt
└── music/
    └── <project-name>/
        ├── bgm.mp3
        └── license.txt
```

---

## 7. ffmpeg 常用音频命令

```bash
# 合并多个音频
ffmpeg -i "concat:file1.mp3|file2.mp3|file3.mp3" -acodec copy output.mp3

# 音频标准化
ffmpeg -i input.mp3 -af "loudnorm=I=-16:TP=-1.5:LRA=11" output.mp3

# 添加片头音乐并淡出
ffmpeg -i narration.mp3 -i intro.mp3 -filter_complex "[1:a]afade=t=out:st=3:d=2[intro];[0:a][intro]concat=n=2:v=0:a=1" output.mp3

# 转 WAV
ffmpeg -i input.mp3 -ar 44100 -ac 2 output.wav
```

---

## 8. 与现有 skills 的关系

- `kdo video` 管线：本 skill 提供 TTS 配音部分
- `image-ocr` / `document-parsing-toolkit`：提取脚本素材
- 本 skill：把文字转成可发布的音频

---

## 9. 下一步待建设

- [ ] 在本地验证 edge-tts 安装和中文语音
- [ ] 创建播客脚本模板
- [ ] 用 ffmpeg 建立音频合并/标准化脚本
- [ ] 测试 ElevenLabs API 中文效果
- [ ] 建立音频资产命名规范
