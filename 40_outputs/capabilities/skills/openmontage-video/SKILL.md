---
name: openmontage-video
version: "1.0.0"
allowed-tools:
  - Bash
  - Read
  - Write
description: |
  AI视频工厂——一句话需求→完整MP4视频。12条专业管道、85+工具、7阶段自动化。
  触发词：做视频、生成视频、制作视频、产品宣传片、科普视频、口播、数字人、
  视频剪辑、AI视频、视频制作、宣传片、字幕视频。
status: published
owner: huangyaoshi
---

# OpenMontage 视频工厂

将 KDO 知识卡片转化为专业视频。洪七公主导。

## 前置

```bash
git clone https://github.com/noah-1106/openmontage-zh-mcp.git
cd openmontage-zh-mcp && pip install -e .
```

## 12 条管道

| 管道 | 用途 |
|:---|:---|
| `animated-explainer` | 科普/教学/知识点（默认，最成熟） |
| `cinematic` | 预告片/品牌/电影感 |
| `animation` | 动效/社交/快节奏 |
| `documentary-montage` | 纪录片/素材剪辑 |
| `screen-demo` | 录屏/软件教程 |
| `talking-head` | 真人出镜/演讲/Vlog |
| `clip-factory` | 长视频拆短视频 |
| `podcast-repurpose` | 播客/音频转视频 |
| `character-animation` | 卡通/角色/IP动画 |
| `avatar-spokesperson` | 数字人/口播 |
| `localization-dub` | 多语言/字幕翻译 |
| `hybrid` | 实拍+AI混合 |

## 工作流

```
KDO卡片(脚本素材) → kdo video montage init → OpenMontage pipeline → MP4交付
```

## 成本

| 类型 | 零成本 | 低成本 | 标准 | 高成本 |
|:---|:---|:---|:---|:---|
| 60秒解说 | $0 | $0.15-0.50 | $1-1.50 | $3+ |
| 30秒预告 | $0 | $0.30-0.80 | $1-2 | $3+ |

默认零成本路径：Piper配音 + 免费图库 + Remotion渲染。
