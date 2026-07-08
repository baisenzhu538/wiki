"""VLM 图片识别能力——自注册到能力中台。"""

from ..registry import register
from .core import VLMCapability, process

register(VLMCapability())
