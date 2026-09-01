#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量 B站视频 → 逐字稿：faster-whisper 转写"""
import os, sys, time, glob

AUDIO_DIR = r"C:\Users\Administrator\Desktop\wiki\00_inbox\video_audio"
OUT_DIR = r"C:\Users\Administrator\Desktop\wiki\00_inbox\video_transcripts"
MODEL_DIR = r"C:\Users\Administrator\wechat-collect\models\faster-whisper-small"
os.makedirs(OUT_DIR, exist_ok=True)

from faster_whisper import WhisperModel
print("Loading model...", flush=True)
model = WhisperModel(MODEL_DIR, device="cpu", compute_type="int8")
print("Model loaded", flush=True)

files = sorted(glob.glob(os.path.join(AUDIO_DIR, "*.mp3")))
print("Files:", files, flush=True)

for f in files:
    vid = os.path.basename(f).replace(".mp3", "")
    out_md = os.path.join(OUT_DIR, f"{vid}-逐字稿.md")
    if os.path.exists(out_md):
        print(f"SKIP {vid} (already)", flush=True)
        continue
    print(f"=== Transcribing {vid} ({os.path.getsize(f)//1024//1024}MB) ===", flush=True)
    t0 = time.time()
    segments, info = model.transcribe(
        f,
        beam_size=5,
        vad_filter=True,
        language=None,  # 自动检测
    )
    print(f"  lang={info.language} prob={info.language_probability:.2f} dur={info.duration:.0f}s", flush=True)
    lines = []
    lines.append(f"# {vid} 视频逐字稿")
    lines.append("")
    lines.append(f"> 转写工具：faster-whisper-small | 语言：{info.language} | 时长：{int(info.duration//60)}分{int(info.duration%60)}秒")
    lines.append("")
    lines.append("---")
    lines.append("")
    for seg in segments:
        ts = f"[{int(seg.start//60):02d}:{int(seg.start%60):02d}]"
        lines.append(f"{ts} {seg.text.strip()}")
        lines.append("")
    md = "\n".join(lines)
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  SAVED {out_md} chars={len(md)} elapsed={int(time.time()-t0)}s", flush=True)

print("ALL_TRANSCRIPTION_DONE", flush=True)
