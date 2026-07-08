"""VLM 图片识别能力——自注册到能力中台。"""

from ..registry import register
from .core import VLMCapability, process

register(VLMCapability(
    name="vlm",
    description="图片识别（MiniMax-M3）——OCR + 内容理解 + 结构化输出",
    category="tool",
))
