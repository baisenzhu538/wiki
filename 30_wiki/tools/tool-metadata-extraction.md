---

id: tool-metadata-extraction
title: 元数据提取：从文件中提取隐藏信息
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain: [yitang, research]
source_refs:
- web: ExifTool official docs
- web: OSINT metadata analysis techniques
related:
  - '[[tool-media-verification-overview]]'
  - '[[tool-reverse-image-search]]'
  - '[[tool-osint-maltego]]'
  - "[[tool-osint-overview]]"
  - "[[tool-reverse-image-search]]"
---

# 元数据提取

> 竞对发的每一张图片、每一份PDF、每一个Office文件——里面都可能嵌着作者、时间、GPS坐标、软件版本。元数据是"不注意就会泄露"的信息层。

## ExifTool：文件元数据之王

| 文件类型 | 能提取什么 |
|:---|:---|
| 照片（JPEG/RAW） | 拍摄时间、GPS坐标、相机型号、镜头参数 |
| PDF | 作者、创建时间、修改时间、使用的软件 |
| Office文档 | 作者、公司名、编辑历史、修订记录 |
| 视频 | 拍摄时间、设备型号、编码参数 |

## Agent执行指令

```bash
# 安装
sudo apt install exiftool   # Linux
brew install exiftool        # macOS

# 提取图片元数据
exiftool image.jpg
# 关键字段: GPS Position, Date/Time Original, Camera Model Name

# 批量提取目录下所有文件
exiftool -r /path/to/files/ > metadata_report.txt

# 只提取特定字段
exiftool -GPSPosition -DateTimeOriginal image.jpg

# 从PDF提取作者信息
exiftool document.pdf | grep -E "Author|Creator|Producer"
```

## 实战场景

| 场景 | 发现 |
|:---|:---|
| 竞对发的产品照片 | GPS坐标暴露了拍摄地点（工厂/办公室位置） |
| 竞对发的PDF白皮书 | 作者字段暴露了真正的作者（可能是外包/顾问） |
| 竞对官网的团队照片 | 拍摄时间暴露了团队合影的真实时间（可能是多年前的） |
| 竞对泄露的内部文档 | 元数据里的公司名/部门名确认了来源 |

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 元数据被清除 | 很多公司上传前会清除元数据 | 这是好习惯——说明他们安全意识强 |
| GPS不精确 | GPS坐标偏差几百米 | 结合地图手动确认 |
| 过度解读 | 把"软件默认作者名"当成真实作者 | 区分"用户设定"和"软件默认"的字段 |

## 适用边界

- **适用**：验证竞对材料的时间/地点/来源真实性
- **不适用**：经过专业脱敏处理的文件（元数据已清除）
- **成本**：完全免费（ExifTool开源）

---

*卡片类型：tool | 审核状态：待审*
