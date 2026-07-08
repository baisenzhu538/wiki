"""能力基类——所有 capability 继承此基类。"""

from dataclasses import dataclass, field


@dataclass
class Capability:
    """能力定义。每个子类必须提供 name 和 description。"""

    name: str = ""
    description: str = ""
    status: str = "available"  # available | planned | deprecated
    category: str = "tool"     # tool | manual | agent_config

    def process(self, **kwargs):
        """子类重写此方法。"""
        raise NotImplementedError(f"{self.name} 未实现 process()")
