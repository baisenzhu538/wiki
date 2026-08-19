---
id: tool-author-targeted-collect
title: 博主定向采集（方式二·抖音侧）：作者视频列表+点赞 → 下载 → 转写 → 知识化
type: tool
status: draft
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-08-19
updated_at: 2026-08-19
domain:
- knowledge-management
- ai-collaboration
- infrastructure
aliases:
- 博主定向采集
- 给我拉一圈
- 作者视频列表
- 抖音采集
- douyin author videos
discoverable_by:
- 博主 定向 采集
- 作者 全部视频 列表
- 高赞视频 拉取
- 抖音 视频列表
- 给我拉一圈
author: 黄药师
reviewed_by: 待审
source_refs:
- 40_outputs/capabilities/skills/author-targeted-collect/SKILL.md
- 40_outputs/code/scripts/douyin_user_videos.py
- 40_outputs/code/scripts/douyin_cookie_extract.py
- 70_product/projects/proj_20260816_wechat-collect-顶层文档.md
related:
- tool-kdo-wechat-serendipity-collect
- tool-cangjie-skill
- tool-yizhan-shendeng
tags:
- audience:all-agents
- scene:execution
- method:automation
- content-format:tool
quality_labels:
- actionable
- validated
- cited
diagnostic_signals:
- signal: 用户说"调研某博主/把某博主的高赞视频拉下来/给我拉一圈"
  lens: 视频号无作者列表公开接口——走抖音同号绕路（蝉妈妈 sec_uid → CDP 列表 → cookie → yt-dlp）
  follow_up: 按 40_outputs/capabilities/skills/author-targeted-collect/SKILL.md 四步执行
---

# 博主定向采集（方式二·抖音侧）

> 楚门"这个小导演不错，给我拉一圈"的落地。与方式一（偶遇采集）互补：方式一守株待兔，方式二主动出击。
> 实测：大李书房一盏灯 27 条视频 + 点赞全抓到，Top3 全链入仓（2026-08-19）。

## 链路

```
博主名 → 蝉妈妈 open 页 HTML（拿 sec_uid）
→ douyin_user_videos.py（CDP 无头 Edge 渲染主页 → 全量视频列表+点赞数）
→ 按赞排序选代表作 → douyin_cookie_extract.py（CDP 提匿名新鲜 cookie）
→ yt-dlp 下载 → WSL GPU 转写 → LLM 三层次知识化 → wechat_promote.py 转正
（自动触发 L1 增量索引——入库即可检索）
```

## 关键组件

| 组件 | 路径 | 作用 |
|:--|:--|:--|
| 列表抓取 | `kdo-tools/douyin_user_videos.py` | CDP 渲染作者主页，输出标题/点赞/aweme_id（6 次滚动全量加载） |
| Cookie 提取 | `kdo-tools/douyin_cookie_extract.py` | 匿名新鲜 cookie（yt-dlp 的 fresh-cookie 墙必须） |
| 下载 | yt-dlp + cookies.txt | 实测 25MB/3s |
| 转写/知识化/转正 | 复用偶遇管线三件套 | 命名 `src_wechat_dy_<aweme_id>` |

## 边界

- 视频号侧无作者列表接口（实测：服务报 unsupported channels url）——抖音同号绕路是 intentional design
- 抓取结果需清洗 Baiduspider 推荐位污染（非作者视频）
- 知识卡标题用平台元数据，不信 tiny 转写稿专名
- 仅个人学习用途
