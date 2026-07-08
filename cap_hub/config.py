"""能力中台配置——API Keys 统一管理，Agent 零配置。"""

import os
from pathlib import Path

MINIMAX_API_KEY = ""
MINIMAX_BASE_URL = "https://api.minimaxi.com/anthropic"
MINIMAX_MODEL = "MiniMax-M3"

PADDLEOCR_HOME = r"C:\Users\Administrator\ocr-pipeline"
MINERU_PATH = "/home/dministrator/.local/bin/mineru"


def _detect_wiki_root() -> Path:
    """自动检测 WSL / Windows 下的 wiki 根目录。"""
    if env := os.environ.get("WIKI_ROOT"):
        p = Path(env)
        if p.exists():
            return p

    candidates = [
        Path("/mnt/c/Users/Administrator/Desktop/wiki"),          # WSL
        Path(r"C:\Users\Administrator\Desktop\wiki"),              # Windows
        Path.home() / "Desktop" / "wiki",
    ]
    for c in candidates:
        if c.exists():
            return c

    return candidates[0]  # 兜底：第一个候选


WIKI_ROOT = _detect_wiki_root()


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
