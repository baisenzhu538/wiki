---
name: research-media-verification
description: OSINT媒体验证链——反向图片搜索→元数据提取→时间/天气/阴影验证
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [媒体验证, 反向搜索, ExifTool, GPS, 照片真伪]
    related_skills: [research]
---

# 媒体验证链

OSINT 媒体验证——反向图片搜索→元数据提取→时间/天气/阴影验证。验证一张图是否"如其所说"。

## Constraints

<hard_limits>
- 仅验证公开图片，不得提取他人私密照片的元数据
- GPS 坐标如涉及个人隐私 → 脱敏处理
</hard_limits>

## 四步验证链

### Step 1: 反向图片搜索——这张图最早出现在哪里？

| 引擎 | URL | 特点 |
|:--|:--|:--|
| **Google Images** | `images.google.com` | 覆盖面最广 |
| **TinEye** | `tineye.com` | 按时间排序，适合溯源 |
| **Yandex** | `yandex.com/images` | 人脸识别最强 |
| **Bing Images** | `bing.com/images` | 补充 Google 盲区 |

**判断**：如果图片在声称的时间之前就已出现 → 造假。

### Step 2: 元数据提取——图片里藏了什么？

```bash
exiftool image.jpg
```

关键字段：
| 字段 | 含义 | 验证什么 |
|:--|:--|:--|
| `GPS Latitude/Longitude` | 拍摄地点 | 与声称地点一致？ |
| `Date/Time Original` | 拍摄时间 | 与声称时间一致？ |
| `Camera Model Name` | 拍摄设备 | 与声称设备一致？ |
| `Software` | 编辑软件 | 被 PS 过？ |

### Step 3: 天气/阴影验证

| 技术 | 工具 | 验证什么 |
|:--|:--|:--|
| **SunCalc** | `suncalc.org` | 阴影方向与声称时间/地点是否一致 |
| **天气预报历史** | `wunderground.com/history` | 声称日期天气与实际是否一致 |
| **Chronolocation** | 综合交叉 | 多因素时间定位 |

### Step 4: 综合判断

| 真实性 | 信号 |
|:--|:--|
| 🔵 高度可信 | 四步全部一致 |
| 🟡 存疑 | 元数据缺失+反向搜索无结果 |
| 🔴 造假 | 反向搜索发现更早出现 / GPS 不一致 / 编辑软件痕迹 |

## 执行流程

```
输入：图片 URL 或文件路径
  ↓
Step 1: 四引擎反向搜索 → 最早出现时间
  ↓
Step 2: exiftool 提取元数据
  ↓
Step 3: (如有GPS/时间) SunCalc + 天气历史交叉验证
  ↓
Step 4: 综合评估 → 输出真实性报告
```

## 相关 wiki 卡片
- `tool-media-verification-overview`
- `tool-reverse-image-search`
- `tool-metadata-extraction`
- `research-cross-validation` — 交叉验证（互补）
