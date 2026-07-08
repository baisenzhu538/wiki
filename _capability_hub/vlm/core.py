"""VLM 图片识别能力——MiniMax M3 引擎。

提取自洪七公 run_vlm_codex.py。
"""

import base64
from pathlib import Path

from anthropic import Anthropic

from ..base import Capability
from ..config import MINIMAX_API_KEY, MINIMAX_BASE_URL, MINIMAX_MODEL, WIKI_ROOT

DEFAULT_PROMPT = """你是一位专业的 OCR + 内容理解专家。请对这张图片进行以下处理：

1. **完整 OCR**：尽可能准确地识别图片中的所有文字，保持原文的段落和结构。
2. **内容理解**：简要说明这张图片的核心主题或核心观点（2-3 句话）。
3. **结构化输出**：如果图片是思维导图、框架图、流程图、表格或课程笔记，请用 Markdown 还原其结构。
4. **关键概念提取**：列出图片中出现的 3-7 个关键概念或术语。
5. **一句话总结**：用一句话总结这张图片最有价值的信息。

请用中文输出，格式如下：

## 原文识别
[OCR 原文]

## 核心主题
[2-3 句话]

## 结构化内容
[Markdown 结构]

## 关键概念
-
-

## 一句话总结
[一句话]
"""


def _resolve_path(image_path: str) -> Path:
    """解析图片路径。相对路径相对于 WIKI_ROOT。"""
    p = Path(image_path)
    if p.is_absolute():
        return p
    return WIKI_ROOT / p


def _encode_image(image_path: Path) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def _media_type(image_path: Path) -> str:
    ext = image_path.suffix.lower()
    if ext in (".png",):
        return "image/png"
    if ext in (".gif",):
        return "image/gif"
    if ext in (".webp",):
        return "image/webp"
    return "image/jpeg"


def process(image_path: str, prompt: str = "", save: bool = True) -> dict:
    """识别单张图片，返回 {path, content, model}。

    用法：
        from capability_hub.vlm import process
        result = process("00_inbox/test.png")
        print(result["content"])
    """
    path = _resolve_path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"图片不存在：{path}")

    if not MINIMAX_API_KEY:
        raise RuntimeError("MINIMAX_API_KEY 未配置，请检查 _capability_hub/config.py")

    client = Anthropic(api_key=MINIMAX_API_KEY, base_url=MINIMAX_BASE_URL)
    base64_image = _encode_image(path)
    mt = _media_type(path)

    response = client.messages.create(
        model=MINIMAX_MODEL,
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {"type": "base64", "media_type": mt, "data": base64_image},
                },
                {"type": "text", "text": prompt or DEFAULT_PROMPT},
            ],
        }],
    )

    content = response.content[0].text

    if save:
        output_dir = WIKI_ROOT / "_vlm_output"
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / f"{path.stem}_vlm.md"
        output_path.write_text(
            f"# VLM 识别结果：{path.name}\n\n{content}",
            encoding="utf-8",
        )

    return {
        "path": str(path),
        "content": content,
        "model": MINIMAX_MODEL,
        "saved": save,
    }


class VLMCapability(Capability):
    name = "vlm"
    description = "图片识别（MiniMax-M3）——OCR + 内容理解 + 结构化输出"
    category = "tool"

    def process(self, image_path: str = "", prompt: str = "", save: bool = True, **kwargs):
        return process(image_path=image_path, prompt=prompt, save=save)
