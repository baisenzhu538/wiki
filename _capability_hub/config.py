"""能力中台配置——API Keys 统一管理，Agent 零配置。

所有外部 API 的 Key 写在这里。Agent 永远不需要传 Key。
换 Key 时改一处，所有 Agent 自动生效。
"""

import os
from pathlib import Path

# === MiniMax VLM ===
MINIMAX_API_KEY = ""
MINIMAX_BASE_URL = "https://api.minimaxi.com/anthropic"
MINIMAX_MODEL = "MiniMax-M3"

# === PaddleOCR（本地，无需 Key）===
PADDLEOCR_HOME = r"C:\Users\Administrator\ocr-pipeline"

# === MinerU PDF 解析 ===
MINERU_PATH = "/home/dministrator/.local/bin/mineru"

# === Wiki 根目录 ===
WIKI_ROOT = Path(os.environ.get(
    "WIKI_ROOT",
    r"C:\Users\Administrator\Desktop\wiki"
))

# 启动时自动从 .env 加载 MiniMax Key
def _load_api_keys():
    global MINIMAX_API_KEY
    env_path = WIKI_ROOT / ".env"
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("MINIMAX_API_KEY="):
                    MINIMAX_API_KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break

_load_api_keys()
