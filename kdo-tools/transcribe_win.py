#!/usr/bin/env python3
"""Windows 原生转写脚本（wechat-collect 管线，2026-08-31 从 WSL 迁出）。

用法:
  python transcribe_win.py <video_or_audio_path> <output_md_path> [--model small|medium|tiny]
                           [--prompt "术语1、术语2"]
默认: small（CPU int8）

#634 转写质量升级（2026-09-04）背景：
- tiny 中文政策/课程类不可用——414 号文视频实测整段乱码（工信部→公秦部、首购首用→
  手锅手用），同族乱码批（09-02「失碎冲鞋/征留」）即 tiny 产物。
- small 裸跑偶发关键名词错转（工信部→公刑部、首购首用→手购所用）；加 --prompt 术语
  注入后专名大部修复，但长音频尾段提示衰减 + 可能引入数字漂移（对照实测：2027→2020）。
- 政策/课程/专名密集内容验收标准=关键名词零错转 → 建议 --model medium（或 medium+prompt）。
  414 号文对照实测（CPU int8）：tiny 34s 乱码 / small 120s 专名错 /
  small+prompt 152s 专名大部修复 / medium 待 #634 实测数字。

模型目录: C:/Users/Administrator/wechat-collect/models/（faster-whisper-tiny/small/medium）
下载指引（HF 直连不通时走镜像，2026-09-04 实测 hf-mirror 约 90MB/s）:
  HF_ENDPOINT=https://hf-mirror.com python -m huggingface_hub.commands.huggingface_cli \
    download Systran/faster-whisper-medium --local-dir C:/Users/Administrator/wechat-collect/models/faster-whisper-medium
"""
import argparse
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODEL_DIR = Path(r"C:/Users/Administrator/wechat-collect/models")
# model.bin 最小可信尺寸（完整包 ~80% 阈值；缺/小=下载中断或残缺——残缺模型加载不报错但出烂稿）
MODEL_MIN_BYTES = {
    "tiny": 60_000_000,
    "small": 400_000_000,
    "medium": 1_200_000_000,
}
DEFAULT_MODEL = "small"


def check_import() -> None:
    """转写前置自检（#634：faster_whisper 曾无痕失踪——pip 日志/会话记录均无，根因不可考）。

    import 失败即报 + 修复指引，不静默不裸崩。
    """
    try:
        import faster_whisper  # noqa: F401
    except ImportError as e:
        print("[transcribe] ❌ faster_whisper 不可用——环境漂移（曾无痕失踪，根因不可考）", file=sys.stderr)
        print("[transcribe]    修复: python -m pip install faster-whisper==1.2.1", file=sys.stderr)
        print(f"[transcribe]    原始错误: {e}", file=sys.stderr)
        sys.exit(2)


def resolve_model(requested: str = DEFAULT_MODEL) -> str:
    """解析模型路径；目标模型残缺（model.bin 缺失/过小）→ 明确报错，禁止静默降级。

    静默降级 = 低质量稿入库污染检索面（#634 事故本质），宁失败不可将就。
    """
    if requested not in MODEL_MIN_BYTES:
        print(f"[transcribe] ❌ 未知模型: {requested}（可选: {'/'.join(MODEL_MIN_BYTES)}）", file=sys.stderr)
        sys.exit(2)
    d = MODEL_DIR / f"faster-whisper-{requested}"
    b = d / "model.bin"
    if not b.exists() or b.stat().st_size < MODEL_MIN_BYTES[requested]:
        print(f"[transcribe] ❌ 模型 {requested} 不可用: {b}", file=sys.stderr)
        print(f"[transcribe]    当前: {'缺失' if not b.exists() else f'仅 {b.stat().st_size} 字节（疑似残缺下载）'}", file=sys.stderr)
        print("[transcribe]    下载: HF_ENDPOINT=https://hf-mirror.com python -m huggingface_hub.commands.huggingface_cli "
              f"download Systran/faster-whisper-{requested} --local-dir {d}", file=sys.stderr)
        sys.exit(2)
    return str(d)


def transcribe(video_path: str, output_md: str, model_name: str = DEFAULT_MODEL, prompt: str = "") -> int:
    t0 = time.time()
    check_import()
    print(f"[transcribe] 输入: {video_path} | 模型: {model_name}{' +prompt' if prompt else ''}")
    from faster_whisper import WhisperModel

    model_path = resolve_model(model_name)
    import faster_whisper as fw

    model = WhisperModel(model_path, device="cpu", compute_type="int8")
    print(f"[transcribe] {model_name} 加载完成 (device=cpu, faster-whisper {fw.__version__})，开始转写...")

    kwargs = {"vad_filter": True}
    if prompt:
        kwargs["initial_prompt"] = prompt
    segments, info = model.transcribe(video_path, language="zh", **kwargs)
    lines = []
    for seg in segments:
        ts = f"[{int(seg.start//60):02d}:{int(seg.start%60):02d}] "
        lines.append(f"{ts}{seg.text.strip()}")
        print(f"  {ts}{seg.text.strip()}", flush=True)

    # 环境指纹入头（#634：引擎版本留痕——下次"上次能跑这次不能"可对照，不再无痕漂移）
    md = (f"# 逐字稿\n\n> 源: {video_path} | 模型: {model_name} | 设备: cpu "
          f"| 引擎: faster-whisper {fw.__version__}"
          f"{' | 术语提示: 开' if prompt else ''}"
          f" | 时长: {info.duration:.0f}s | 耗时: {time.time()-t0:.0f}s\n\n"
          + "\n".join(lines) + "\n")
    Path(output_md).write_text(md, encoding="utf-8")
    print(f"[transcribe] ✅ 完成 -> {output_md} ({len(lines)} 段, {time.time()-t0:.0f}s)")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Windows 原生 faster-whisper 转写（CPU int8）")
    ap.add_argument("video", help="视频/音频路径")
    ap.add_argument("output", help="输出 .md 路径")
    ap.add_argument("--model", default=DEFAULT_MODEL, choices=sorted(MODEL_MIN_BYTES),
                    help=f"转写模型（默认 {DEFAULT_MODEL}；政策/课程/专名密集内容建议 medium）")
    ap.add_argument("--prompt", default="", help="术语提示（initial_prompt，中文专名拼写强化，顿号分隔）")
    args = ap.parse_args()
    sys.exit(transcribe(args.video, args.output, args.model, args.prompt))
