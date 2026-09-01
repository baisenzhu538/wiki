# -*- coding: utf-8 -*-
"""批量生成视频逐字稿 delivery manifest"""
import os, json, datetime

BASE = r"C:\Users\Administrator\Desktop\wiki\50_delivery\published"
DOCS = [
    ("del_20260901_spin_video", "art_20260901_spin_video", "尼尔·雷克汉姆：联结销售与营销（SPIN创始人）-视频逐字稿",
     "https://yitang.top/fs-doc/d942dd39331738382bd8ecf0ffacbceb/YTJgdq3idoRKwExETDqc5JlfnNd",
     "https://www.bilibili.com/video/BV1JsgQzWEuD/", "KoxHdJSiToPfdLxZ62PcAsNCnFf",
     "00_inbox/video_transcripts_small/BV1JsgQzWEuD-逐字稿.md", 16120, "L1 doc + B站视频 yt-dlp 下载 → faster-whisper-small 转写"),
    ("del_20260901_ted_video", "art_20260901_ted_video", "大卫·布鲁克斯：当代文化的3个主流谎言（TED）-视频逐字稿",
     "https://yitanger.feishu.cn/wiki/KzXwwSWmMiAKJzkPnIBcvTpdnhf",
     "https://www.bilibili.com/video/BV1kp4y1v7p9/", "C7iNdl04eoNzALxF6TqcadOnnTc",
     "00_inbox/video_transcripts_small/TED-大卫布鲁克斯-3个主流谎言-逐字稿.md", 53392, "L1 doc + B站视频 yt-dlp 下载 → faster-whisper-small 转写（3段合集合并）"),
    ("del_20260901_chicago2017_video", "art_20260901_chicago2017_video", "大卫·布鲁克斯：2017芝加哥大学毕业演讲-视频逐字稿",
     "https://yitanger.feishu.cn/wiki/KzXwwSWmMiAKJzkPnIBcvTpdnhf",
     "https://www.bilibili.com/video/BV1rp4y1e76Y/", "HvDZd7YcBocZmJxVLI9cEZp8nMb",
     "00_inbox/video_transcripts_small/BV1rp4y1e76Y-逐字稿.md", 33008, "L1 doc + B站视频 yt-dlp 下载 → faster-whisper-small 转写"),
    ("del_20260901_uchicago_video", "art_20260901_uchicago_video", "大卫·布鲁克斯：芝大毕业演讲（求知是有代价的）-视频逐字稿",
     "https://yitanger.feishu.cn/wiki/KzXwwSWmMiAKJzkPnIBcvTpdnhf",
     "https://www.bilibili.com/video/BV1ug411i7bH/", "St1zdcJZ6oINqtxUwppcSLpan7g",
     "00_inbox/video_transcripts_small/BV1ug411i7bH-逐字稿.md", 32353, "L1 doc + B站视频 yt-dlp 下载 → faster-whisper-small 转写"),
    ("del_20260901_yale_video", "art_20260901_yale_video", "大卫·布鲁克斯：耶鲁对话——如何爱上一个人-视频逐字稿",
     "https://yitanger.feishu.cn/wiki/KzXwwSWmMiAKJzkPnIBcvTpdnhf",
     "https://www.bilibili.com/video/BV1wb9XBXEGb/", "ZaqudvIzeocTcXxcnytc4bpDnzb",
     "00_inbox/video_transcripts_small/BV1wb9XBXEGb-逐字稿.md", 63046, "L1 doc + B站视频 yt-dlp 下载 → faster-whisper-small 转写"),
]

for del_id, art_id, title, source_url, video_url, doc_id, local_copy, chars, method in DOCS:
    d = os.path.join(BASE, del_id)
    os.makedirs(d, exist_ok=True)
    manifest = f"""---
delivery_id: "{del_id}"
artifact_id: "{art_id}"
channel: "feishu_doc"
shipped_at: "2026-09-01T02:20:00+08:00"
feedback_status: "无反馈"
source_url: "{source_url}"
video_url: "{video_url}"
extraction_method: "{method}"
doc_id: "{doc_id}"
url: "https://yitanger.feishu.cn/docx/{doc_id}"
local_copy: "{local_copy}"
permission: "anyone_readable"
---

# Delivery Manifest: {del_id}

## Artifact Info

- title: {title}
- chars: {chars}
- verify: 转写结果已存本地，发布零失败

## Extraction

- source: B站视频（作业Candy文档引用）
- method: yt-dlp 下载音频 → faster-whisper-small (CPU int8) 转写 → 时间戳逐字稿

## Publishing

- permission: anyone_readable
- url: https://yitanger.feishu.cn/docx/{doc_id}
"""
    with open(os.path.join(d, "manifest.yaml"), "w", encoding="utf-8") as f:
        f.write(manifest)
    print("WROTE:", del_id)
print("ALL_MANIFESTS_DONE")
