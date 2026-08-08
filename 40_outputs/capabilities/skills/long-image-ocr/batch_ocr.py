#!/usr/bin/env python3
"""Batch OCR+VLM for a directory of images.
Usage: python3 batch_ocr.py <src_dir> [out_dir]
- src_dir: directory containing .png images
- out_dir: defaults to src_dir (must be user-visible, NOT /tmp/)
- Reads API key from /home/dministrator/.mmkey_b64 (fallback /tmp/.mmkey_b64)
- Uses MiniMax-M3 (not abab6.5s-chat)
- Auto-splits images >800px tall into 600px chunks
- Produces per-image markdown files with raw VLM text
- Resume-safe: skips images that already have OCR_*.md output
"""
import base64 as b64mod, json, os, subprocess, sys, time, urllib.request

# Config
MODEL = "MiniMax-M3"
CHUNK_H = 600
DIRECT_THRESHOLD = 800  # images <= this height go straight to VLM

KEY_CANDIDATES = [
    "/home/dministrator/.mmkey_b64",  # primary (home dir survives /tmp cleanup)
    "/tmp/.mmkey_b64",                # fallback
]

def load_key():
    for path in KEY_CANDIDATES:
        if os.path.exists(path):
            with open(path) as f:
                return b64mod.b64decode(f.read().strip()).decode().strip()
    raise FileNotFoundError(f"No API key file in {KEY_CANDIDATES}. Ask user for base64 key.")

def get_dims(path):
    out = subprocess.check_output(
        ["ffprobe","-v","error","-show_entries","stream=width,height","-of","csv=p=0",path],
        timeout=10, text=True
    ).strip()
    w, h = out.split(",")
    return int(w), int(h)

def split_image(src, w, h, workdir):
    if h <= DIRECT_THRESHOLD:
        return [src]
    n = max(1, (h + CHUNK_H - 1) // CHUNK_H)
    chunks = []
    for i in range(n):
        top = i * CHUNK_H
        bot = min((i + 1) * CHUNK_H, h)
        out = os.path.join(workdir, f"_chunk_{i}.png")
        subprocess.run(
            ["ffmpeg","-y","-i",src,"-vf",f"crop={w}:{bot-top}:0:{top}","-frames:v","1",out],
            capture_output=True, timeout=10
        )
        chunks.append(out)
    return chunks

def call_vlm(img_path, label, key):
    with open(img_path, "rb") as f:
        enc = b64mod.b64encode(f.read()).decode()
    body = json.dumps({
        "model": MODEL,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": f"Transcribe ALL text in this image. Label: {label}"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{enc}"}}
            ]
        }]
    }).encode()
    req = urllib.request.Request(
        "https://api.minimaxi.com/v1/text/chatcompletion_v2",
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        result = json.loads(r.read())
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    return json.dumps(result, ensure_ascii=False)[:500]

def main():
    src_dir = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else src_dir
    os.makedirs(out_dir, exist_ok=True)

    key = load_key()
    pngs = sorted([f for f in os.listdir(src_dir) if f.lower().endswith('.png')])

    # Resume: skip images that already have OCR output
    todo = []
    for fname in pngs:
        out_md = os.path.join(out_dir, f"OCR_{os.path.splitext(fname)[0]}.md")
        if not os.path.exists(out_md):
            todo.append(fname)
    print(f"Total {len(pngs)}, already done {len(pngs)-len(todo)}, to process {len(todo)}", flush=True)

    stats = {"total": 0, "ok": 0, "fail": 0}

    for fi, fname in enumerate(todo):
        path = os.path.join(src_dir, fname)
        w, h = get_dims(path)
        kb = os.path.getsize(path) / 1024
        chunks = split_image(path, w, h, out_dir)

        print(f"[{fi+1}/{len(todo)}] {fname} ({w}x{h}, {kb:.0f}KB) -> {len(chunks)} chunks", flush=True)

        out_md = os.path.join(out_dir, f"OCR_{os.path.splitext(fname)[0]}.md")
        with open(out_md, "w") as f:
            f.write(f"# {fname}\n> {w}×{h} | {len(chunks)} chunks | Model: {MODEL}\n\n")

            for ci, cp in enumerate(chunks):
                label = f"{fname} c{ci+1}/{len(chunks)}"
                ckb = os.path.getsize(cp) / 1024
                print(f"  c{ci+1} {ckb:.0f}KB...", end=" ", flush=True)

                try:
                    txt = call_vlm(cp, label, key)
                    ok = "无法查看" not in txt and "cannot" not in txt.lower() and len(txt) > 30
                except Exception as e:
                    txt = f"[ERROR] {e}"
                    ok = False

                print("OK" if ok else "FAIL", flush=True)
                stats["total"] += 1
                if ok: stats["ok"] += 1
                else: stats["fail"] += 1

                f.write(f"## Chunk {ci+1} {'✅' if ok else '❌'}\n\n{txt}\n\n---\n\n")

                time.sleep(0.3)

        # Clean up temp chunks
        for cp in chunks:
            if cp != path and os.path.exists(cp):
                os.remove(cp)

    print(f"\nDone: {stats['ok']}/{stats['total']} OK ({stats['ok']*100//max(stats['total'],1)}%)", flush=True)

if __name__ == "__main__":
    main()
