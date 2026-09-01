# -*- coding: utf-8 -*-
"""下载 faster-whisper small 模型（CTranslate2 格式）"""
import os, sys

os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
from faster_whisper.utils import download_model

out = r"C:\Users\Administrator\wechat-collect\models\faster-whisper-small"
print("Downloading faster-whisper small...", flush=True)
try:
    path = download_model("small", output_dir=out, local_files_only=False)
    print("MODEL_PATH:", path, flush=True)
    # 检查 model.bin
    for root, dirs, files in os.walk(out):
        for f in files:
            if f == "model.bin":
                full = os.path.join(root, f)
                print("FOUND model.bin:", full, os.path.getsize(full), flush=True)
    print("DOWNLOAD_DONE", flush=True)
except Exception as e:
    print("DOWNLOAD_ERR:", str(e)[:500], flush=True)
    sys.exit(1)
