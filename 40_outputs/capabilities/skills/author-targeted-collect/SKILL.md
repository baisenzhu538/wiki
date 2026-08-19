---
name: author-targeted-collect
description: 博主定向采集（方式二·抖音侧）——"这个小导演不错，给我拉一圈"：给定博主名/主页，抓取其全部视频列表（含点赞数），按赞排序挑代表作，yt-dlp 下载 → WSL GPU 转写 → LLM 三层次知识化 → 转正入仓。当用户说"调研某博主/把某博主的高赞视频拉下来/定向采集某作者"时使用。视频号作者列表无公开接口，走抖音同号绕路。
agent_created: true
---

# 博主定向采集（方式二·抖音侧）

> 楚门"给我拉一圈"机制的落地。缘起：视频号无作者视频列表公开接口（下载服务只解析单链接，实测实证），
> 同一博主内容通常视频号/抖音同步分发——抖音侧列表可抓，等价可用。
> 实测：大李书房一盏灯 27 条全抓，Top3 全链入仓（2026-08-19）。

## 工作流程

### 1. 定位博主抖音账号

- 已知博主名 → 搜索引擎找蝉妈妈 open 数据页（`chanmama.com/open/authorRank/...`）
- 抓该页原始 HTML，正则提取 `douyin.com/user/MS4w...`（sec_uid）和 `share/user/<uid>`
- 有现成 sec_uid 直接跳到下一步

### 2. 抓作者视频列表（含点赞数）

```bash
python kdo-tools/douyin_user_videos.py <sec_uid>   # CDP 无头 Edge 渲染主页 → JSON
```

- 原理：CDP 驱动无头 Edge（端口 9223，独立 profile `edge-debug-profile-dy`，不碰用户浏览器）
- 6 次滚动触发全量加载；输出 title/likes/aweme_id/url
- ⚠️ 结果清洗：去掉 `?source=Baiduspider` 的推荐位污染条目（非作者视频）

### 3. 按赞排序选代表作 → 下载

```bash
python kdo-tools/douyin_cookie_extract.py   # CDP 提匿名新鲜 cookie → cookies.txt
yt-dlp --cookies cookies.txt -o "<目录>/%(id)s.%(ext)s" https://www.douyin.com/video/<aweme_id>
```

- 抖音需要 fresh cookies（不必登录），yt-dlp 裸跑会报 "Fresh cookies needed"
- cookie 文件是凭证：**永不入 git**（.gitignore 已含）

### 4. 转写 → 知识化 → 转正（复用偶遇管线）

```bash
wsl -e bash -c "python3 /home/dministrator/wechat-collect/transcribe.py <mp4> <out.md>"   # GPU 转写
python kdo-tools/wechat_knowledge.py <out.md>    # LLM 三层次（事实/规律/洞察）
python kdo-tools/wechat_promote.py               # 转正 10_raw + 30_wiki（自动触发增量索引）
```

- 命名约定：`src_wechat_dy_<aweme_id>.md`（dy 前缀标识抖音来源，复用 promote 正则）
- 知识卡标题用平台元数据修正——**不信 tiny 转写稿的专名**

## 边界与注意

- 仅个人学习用途，不传播下载内容
- 抖音主页结构会变——抓不到列表时先小样本诊断（看页面 title/DOM），别盲目重试
- cookie 约短期有效，失效重跑 `douyin_cookie_extract.py`
- 视频号侧如未来开放作者列表接口，优先切回视频号（与偶遇管线同源）

## 关联

- 偶遇采集（方式一）：`wechat-serendipity-collect` skill / `tool-kdo-wechat-serendipity-collect`
- 顶层文档：`70_product/projects/proj_20260816_wechat-collect-顶层文档.md`（§零 楚门两种方式对齐）
- 蒸馏后续：采来的视频可用 `cangjie-skill` / `yizhan-shendeng` 继续蒸成技能包
