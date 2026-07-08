"""python -m cap_hub list —— 能力中台入口。"""

import sys

if len(sys.argv) > 1 and sys.argv[1] == "list":
    from cap_hub.registry import print_list
    print_list()
else:
    print("用法：python -m cap_hub list")
    print("      列出所有可用能力（工具 + 说明书 + Agent 配置）")
