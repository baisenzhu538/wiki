# Feishu Publish Workflow

## Overview

将 40_outputs/ 中的成品（articles/videos/images）发布到指定飞书渠道，并记录交付结果。

## Pre-flight Check

发布前必须确认：
1. 素材完整（标题/摘要/thumbnail/元数据）
2. 渠道匹配 target_user
3. 周伯通已批准发布

## Steps

### Step 1: 读取成品信息

从 `40_outputs/content/{type}/` pickup 待发布的成品。
读取 frontmatter 中的：
- target_user：目标读者
- delivery_channel：指定渠道
- source_refs：来源追溯

### Step 2: 格式化素材

根据渠道要求格式化：
- 飞书文档：Markdown → 富文本
- 飞书消息：标题 + 摘要 + 链接
- 视频：上传到飞书云盘或视频服务

### Step 3: 发布

使用 send_message 或飞书 API 发到指定渠道。
记录发布时间和渠道。

### Step 4: 记录交付

在 `50_delivery/published/` 创建记录文件：
```
del_{timestamp}_{artifact_id}.md
```

包含：
- artifact_id
- 发布渠道
- 发布时间
- 发布链接（如有）
- target_user
- 预期反馈时间

### Step 5: 追踪反馈

发布后定期检查：
- 飞书消息的回复/评论
- 转发数据
- 用户反应

将有效反馈录入 `60_feedback/`。

## Feedback Classification

| 类型 | 判断标准 | 动作 |
|------|---------|------|
| 内容错误 | 事实性错误、过时数据 | 通知周伯通，回流给黄药师 |
| 表达不清 | 目标用户反馈看不懂 | 通知周伯通，评估改写 |
| 渠道不匹配 | 受众反馈"不是我要的" | 通知周伯通，重新选渠道 |
| 噪音 | 无实质内容的反应 | 记录，不触发行动 |

## Pitfalls

- 不在没有完整元数据时发布
- 不擅自更换渠道（必须经过周伯通确认）
- 不遗漏发布后的追踪
