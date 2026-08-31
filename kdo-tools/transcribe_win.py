#!/usr/bin/env python3
"""Windows 原生转写脚本（wechat-collect 管线，2026-08-31 从 WSL 迁出）。

用法: python transcribe_win.py <video_or_audio_path> <output_md_path>
模型: C:/Users/Administrator/wechat-collect/models/ 下的 faster-whisper-tiny
背景: 五绝已全量迁移 Windows 侧，WSL 已废除；wsl.exe 间歇性僵死曾把王语嫣
      的 turn 卡死 180s+（2026-08-31 21:28 实证）。管线拔掉 WSL 依赖。
"""
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODEL_DIR = Path(r"C:/Users/Administrator/wechat-collect/models")


def pick_model():
    """优先完整可用的模型（tiny 已就绪；small 残缺时跳过）。"""
    tiny_dir = MODEL_DIR / "faster-whisper-tiny"
    small_dir = MODEL_DIR / "faster-whisper-small"
    if small_dir.exists() and (small_dir / "model.bin").exists():
        return "small", str(small_dir)
    if tiny_dir.exists() and (tiny_dir / "model.bin").exists():
        return "tiny", str(tiny_dir)
    return "tiny", "tiny"


def transcribe(video_path: str, output_md: str) -> int:
    t0 = time.time()
    print(f"[transcribe] 输入: {video_path}")
    from faster_whisper import WhisperModel

    name, model_path = pick_model()
    model = WhisperModel(model_path, device="cpu", compute_type="int8")
    print(f"[transcribe] 模型 {name} 加载完成 (device=cpu)，开始转写...")

    segments, info = model.transcribe(video_path, language="zh", vad_filter=True)
    lines = []
    for seg in segments:
        ts = f"[{int(seg.start//60):02d}:{int(seg.start%60):02d}] "
        lines.append(f"{ts}{seg.text.strip()}")
        print(f"  {ts}{seg.text.strip()}", flush=True)

    md = f"# 逐字稿\n\n> 源: {video_path} | 模型: {name} | 设备: cpu | 时长: {info.duration:.0f}s | 耗时: {time.time()-t0:.0f}s\n\n" + "\n".join(lines) + "\n"
    Path(output_md).write_text(md, encoding="utf-8")
    print(f"[transcribe] ✅ 完成 -> {output_md} ({len(lines)} 段, {time.time()-t0:.0f}s)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python transcribe_win.py <video> <output_md>")
        sys.exit(1)
    sys.exit(transcribe(sys.argv[1], sys.argv[2]))
