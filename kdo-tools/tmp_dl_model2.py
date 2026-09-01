# -*- coding: utf-8 -*-
"""通过 hf-mirror 下载 faster-whisper small 模型"""
import os, sys

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
from huggingface_hub import snapshot_download

out = r"C:\Users\Administrator\wechat-collect\models\faster-whisper-small"
print("Downloading via hf-mirror...", flush=True)
try:
    path = snapshot_download("Systran/faster-whisper-small", local_dir=out)
    print("MODEL_PATH:", path, flush=True)
    for root, dirs, files in os.walk(out):
        for f in files:
            if f == "model.bin":
                full = os.path.join(root, f)
                print("FOUND model.bin:", full, os.path.getsize(full), flush=True)
    print("DOWNLOAD_DONE", flush=True)
except Exception as e:
    print("DOWNLOAD_ERR:", str(e)[:800], flush=True)
    sys.exit(1)
