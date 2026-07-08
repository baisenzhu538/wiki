"""能力中台配置——API Keys 统一管理，Agent 零配置。"""

import os
from pathlib import Path

MINIMAX_API_KEY = ""
MINIMAX_BASE_URL = "https://api.minimaxi.com/anthropic"
MINIMAX_MODEL = "MiniMax-M3"

PADDLEOCR_HOME = r"C:\Users\Administrator\ocr-pipeline"
MINERU_PATH = "/home/dministrator/.local/bin/mineru"

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", r"C:\Users\Administrator\Desktop\wiki"))


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
