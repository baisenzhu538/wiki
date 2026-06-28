---

id: tool-media-verification-overview
title: 媒体验证技术总览：判断"对方说的是不是真的"
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.85
trust_level: high
language: zh-CN
domain:
- yitang
- research
source_refs:
- src_unknown
- src_unknown
related:
  - [[yitang-domain-digest]]
  - [[yitang-research-domain-digest]]
  - [[pending_unknown]]
  - [[pending_unknown]]
  - [[pending_unknown]]
updated_at: '2026-06-29'
---

# 媒体验证技术总览

> 竞对声称"我们的产品在XX市场大获成功"、照片里"热火朝天的生产线"、视频里"人山人海的门店"——这些是真的还是演的？媒体验证技术用客观证据说话。

## 六大验证技术

| # | 技术 | 难度 | 适用场景 | 核心原理 |
|:---:|:---|:---:|:---|:---|
| 1 | **反向图片搜索** | ⭐ | 验证图片是否原创/从哪来的 | 在Google/TinEye/Yandex搜图片来源 |
| 2 | **元数据提取** | ⭐⭐ | 验证文件的时间/地点/作者 | ExifTool提取GPS/时间/设备信息 |
| 3 | **Chronolocation** | ⭐⭐⭐ | 验证视频/照片的拍摄时间 | 画面中的钟表/手机时间/电视节目/日照角度 |
| 4 | **Geolocation** | ⭐⭐⭐⭐ | 验证照片/视频的拍摄地点 | 画面中的地标/招牌/车牌/植被/建筑风格 |
| 5 | **天气验证** | ⭐⭐⭐ | 验证"在某时某地拍摄"的声明 | Wolfram Alpha历史天气 vs 画面中的天气/阴影 |
| 6 | **影子/太阳位置** | ⭐⭐⭐⭐ | 验证拍摄时间和大致纬度 | SunCalc输入日期地点→比对画面中的阴影方向和长度 |

## 实战流水线

```
竞对发布"工厂满负荷运转"的照片
  ↓
① 反向图片搜索 → 确认图片是原创还是图库照片
  ↓
② 元数据提取 → GPS显示拍摄地点、时间显示日期
  ↓
③ Geolocation → 画面中的工厂招牌/周边建筑匹配GPS坐标
  ↓
④ 天气验证 → 该日期该地点的天气（阴天?晴天?）和画面一致?
  ↓
⑤ Chronolocation → 画面中的时钟/日照角度与拍摄时间一致?
  ↓
⑥ 结论：照片真实/照片存疑/照片伪造
```

## Agent执行指令

```bash
# 天气验证 (Wolfram Alpha API)
curl "https://api.wolframalpha.com/v1/query?appid=KEY&input=weather+2024-03-15+Shanghai&format=plaintext"

# 太阳位置验证 (SunCalc)
# https://www.suncalc.org - 输入日期+地点→看太阳高度角和方位角→比对照片阴影

# ExifTool提取元数据
exiftool -GPSPosition -DateTimeOriginal -Make -Model image.jpg
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 元数据被清除 | 提取不到任何信息 | 这是常态（大公司会脱敏），不能作为"可疑"的证据 |
| 单一验证不充分 | 天气对上了但地点不对 | 必须多技术交叉验证——单技术不能下结论 |
| 技术难度过高 | Geolocation需要专业知识 | 先从简单的开始（反向搜索+元数据），再逐步深入 |

## 适用边界

- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*
