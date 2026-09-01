#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量转写（small 模型，覆盖 tiny 结果）"""
import os, sys, time, glob

AUDIO_DIR = r"C:\Users\Administrator\Desktop\wiki\00_inbox\video_audio"
OUT_DIR = r"C:\Users\Administrator\Desktop\wiki\00_inbox\video_transcripts_small"
MODEL_DIR = r"C:\Users\Administrator\wechat-collect\models\faster-whisper-small"
os.makedirs(OUT_DIR, exist_ok=True)

os.environ['http_proxy'] = 'http://127.0.0.1:7897'
os.environ['https_proxy'] = 'http://127.0.0.1:7897'

from faster_whisper import WhisperModel
print("Loading small model...", flush=True)
model = WhisperModel(MODEL_DIR, device="cpu", compute_type="int8")
print("Model loaded", flush=True)

files = sorted(glob.glob(os.path.join(AUDIO_DIR, "*.mp3")))
print("Files:", [os.path.basename(f) for f in files], flush=True)

for f in files:
    vid = os.path.basename(f).replace(".mp3", "")
    out_md = os.path.join(OUT_DIR, f"{vid}-逐字稿.md")
    if os.path.exists(out_md):
        print(f"SKIP {vid} (already)", flush=True)
        continue
    print(f"=== Transcribing {vid} ({os.path.getsize(f)//1024//1024}MB) ===", flush=True)
    t0 = time.time()
    segments, info = model.transcribe(f, beam_size=5, vad_filter=True, language=None)
    print(f"  lang={info.language} prob={info.language_probability:.2f} dur={info.duration:.0f}s", flush=True)
    lines = [f"# {vid} 视频逐字稿", "",
             f"> 转写工具：faster-whisper-small | 语言：{info.language} | 时长：{int(info.duration//60)}分{int(info.duration%60)}秒", "",
             "---", ""]
    for seg in segments:
        ts = f"[{int(seg.start//60):02d}:{int(seg.start%60):02d}]"
        lines.append(f"{ts} {seg.text.strip()}")
        lines.append("")
    md = "\n".join(lines)
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"  SAVED {out_md} chars={len(md)} elapsed={int(time.time()-t0)}s", flush=True)

print("ALL_TRANSCRIPTION_DONE", flush=True)
