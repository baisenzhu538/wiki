# 能力中台——环境配置

> 新电脑/新 Agent 接入能力中台，只需要做一次以下步骤。

## 1. 前置条件

```bash
pip install anthropic
```

## 2. API Key

在 wiki 根目录创建 `.env` 文件（git 不会提交它，每台电脑需要单独创建）：

```
MINIMAX_API_KEY=sk-你的MiniMax密钥
```

`cap_hub/config.py` 启动时自动从 `.env` 加载，Agent 不需要传 Key。

## 3. 路径（Windows / WSL 自动兼容）

`cap_hub/config.py` 自动检测 wiki 根目录：

```
Windows: C:\Users\Administrator\Desktop\wiki
WSL:     /mnt/c/Users/Administrator/Desktop/wiki
```

如果 wiki 不在默认路径，设 `WIKI_ROOT` 环境变量：

```bash
# Windows
set WIKI_ROOT=D:\my-wiki

# WSL
export WIKI_ROOT=/mnt/d/my-wiki
```

## 4. 验证

```bash
cd <wiki根目录>
python -m cap_hub list
```

预期输出：1 个可调用工具（vlm）、192 frameworks、8 workflows、101 skills、3 个 agent-spec。

## 5. Agent 调用示例

```python
# 任何 Agent，任何平台——同一行代码
from cap_hub.vlm import process
result = process("00_inbox/test.png")
print(result["content"])
```
