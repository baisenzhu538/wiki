"""能力基类——所有 capability 继承此基类。"""

from dataclasses import dataclass


@dataclass
class Capability:
    name: str = ""
    description: str = ""
    status: str = "available"
    category: str = "tool"

    def process(self, **kwargs):
        raise NotImplementedError(f"{self.name} 未实现 process()")
