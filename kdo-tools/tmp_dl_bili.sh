#!/bin/bash
# 批量下载 B站视频音频
set -x
YTDLP="/c/Program Files/Python312/Scripts/yt-dlp.exe"
OUTDIR="C:/Users/Administrator/Desktop/wiki/00_inbox/video_audio"
mkdir -p "$OUTDIR"

VURLS=(
  "https://www.bilibili.com/video/BV1JsgQzWEuD/"    # DOC3 SPIN创始人
  "https://www.bilibili.com/video/BV1ug411i7bH/"    # DOC4-1 芝大演讲
  "https://www.bilibili.com/video/BV1kp4y1v7p9/"    # DOC4-2 TED
  "https://www.bilibili.com/video/BV1rp4y1e76Y/"    # DOC4-3 芝加哥2017
  "https://www.bilibili.com/video/BV1wb9XBXEGb/"    # DOC4-4 耶鲁对话
)

for url in "${VURLS[@]}"; do
  "$YTDLP" -f "ba/b" -x --audio-format mp3 --audio-quality 5 \
    -o "$OUTDIR/%(id)s.%(ext)s" "$url" 2>&1 | tail -3
done
echo "ALL_DOWNLOAD_DONE"
ls -la "$OUTDIR" | tail -10
