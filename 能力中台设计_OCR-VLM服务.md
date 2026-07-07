# OCR+VLM 能力中台设计方案

> 目标：让 Claude、Kimi Code CLI、Codex、Hermes 都能调用同一套 OCR+VLM 能力，支持 Windows 本机和 WSL2 混合部署。

---

## 一、核心架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                     OCR + VLM 能力中台                               │
│                                                                      │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────────────────┐   │
│  │  REST API   │   │  MCP Server │   │       CLI 工具          │   │
│  │  (FastAPI)  │   │ (for Claude)│   │  (for Kimi/Hermes脚本)  │   │
│  └──────┬──────┘   └──────┬──────┘   └───────────┬─────────────┘   │
│         └──────────────────┼──────────────────────┘                 │
│                            ↓                                        │
│                 ┌─────────────────────┐                             │
│                 │    OCR/VLM Core     │                             │
│                 │  (MiniMax API 调用)  │                             │
│                 └──────────┬──────────┘                             │
│                            ↓                                        │
│                 ┌─────────────────────┐                             │
│                 │     Wiki 存储层      │                             │
│                 │ (Windows 路径映射)   │                             │
│                 └─────────────────────┘                             │
└─────────────────────────────────────────────────────────────────────┘
        ↑                      ↑                      ↑
   Kimi Code CLI          Claude Desktop          Hermes / Codex
   (HTTP / CLI)           (MCP 协议)              (HTTP / CLI)
```

---

## 二、为什么这样设计

| 需求 | 方案 | 原因 |
|------|------|------|
| 多 Agent 共用 | REST API | 所有 Agent 都能发 HTTP 请求 |
| Claude 深度集成 | MCP Server | Claude 官方推荐的标准工具协议 |
| 脚本/自动化 | CLI 工具 | Kimi Code CLI、Hermes 可以直接跑 |
| Windows + WSL 都能跑 | 路径抽象层 + 本地网络 | 用 `pathlib` + `localhost` 抹平差异 |
| 结果统一存储 | Wiki 目录 | 所有 Agent 都能读共享知识库 |

---

## 三、部署位置选择

### 方案 A：服务跑在 Windows 本机（推荐）

**原因**：
- 图片和 wiki 文件都在 Windows 侧
- WSL 访问 Windows 文件通过 `/mnt/c/` 有性能损耗
- Kimi Code CLI 运行在 Windows 环境，直接调用本机服务最快

**访问方式**：
- Windows 本机：`http://localhost:8765`
- WSL2：`http://localhost:8765`（WSL2 与 Windows 共享 localhost）
- 其他机器：`http://<Windows_IP>:8765`（如需局域网访问）

### 方案 B：服务跑在 WSL2 里

**适用场景**：
- 你的主要开发环境在 WSL
- Hermes 或其他 Agent 常驻 WSL

**访问方式**：
- WSL2 内部：`http://localhost:8765`
- Windows 侧：`http://localhost:8765`（WSL2 自动映射）
- 文件写入：通过 `/mnt/c/Users/Administrator/Desktop/wiki/...` 写回 Windows

**注意**：WSL2 的 localhost 共享是自动的，但文件 I/O 跨系统比 Windows 本机慢。

### 推荐

**Windows 本机部署为主**，WSL 里的 Agent 通过 `localhost` 调用。

---

## 四、各 Agent 怎么接入

### 1. Kimi Code CLI

**方式一：调用 REST API**

```bash
curl -X POST "http://localhost:8765/ocr_vlm" \
  -F "file=@/c/Users/Administrator/Desktop/wiki/00_inbox/test.png" \
  -H "X-API-Key: your_local_api_key"
```

**方式二：调用 CLI 工具**

```bash
python -m vlm_hub process --image "path/to/image.png"
```

### 2. Claude Desktop / Claude Code

通过 MCP Server 接入：

```json
{
  "mcpServers": {
    "ocr_vlm_hub": {
      "command": "python",
      "args": [
        "-m",
        "vlm_hub.mcp_server",
        "--api-url",
        "http://localhost:8765"
      ],
      "env": {
        "LOCAL_API_KEY": "your_local_api_key"
      }
    }
  }
}
```

接入后，Claude 对话中可以直接说：

> "请用 ocr_vlm 识别这张图片"

### 3. Hermes

取决于 Hermes 的实现：
- 如果是 Python Agent：直接 import `vlm_hub.client`
- 如果是 HTTP 服务：调用 `http://localhost:8765/ocr_vlm`
- 如果是 Node.js：用 axios/fetch 调 REST API

### 4. Codex

Codex 的接入方式取决于它的插件机制：
- 如果 Codex 支持 MCP：直接接 MCP Server
- 如果 Codex 支持 HTTP tools：调用 REST API
- 如果 Codex 只能本地命令：调用 CLI 工具

**Codex 目前最可能的方式**：通过自定义 tool 调用本地 CLI 或 HTTP API。

---

## 五、API 设计

### Endpoint 1：文件上传识别

```http
POST /ocr_vlm
Content-Type: multipart/form-data

file: <binary image>
prompt_type: "default" | "codex" | "course" | "custom"
custom_prompt: "可选，自定义提示词"
save_to_wiki: true
wiki_path: "00_inbox/某个文件夹"
```

**Response**：

```json
{
  "success": true,
  "file_id": "uuid",
  "original_name": "test.png",
  "output_path": "C:/Users/Administrator/Desktop/wiki/_vlm_output/test_vlm.md",
  "content": "## 原文识别\n...",
  "model": "MiniMax-M3",
  "tokens_used": 1234,
  "cost": 0.002
}
```

### Endpoint 2：本地文件路径识别

```http
POST /ocr_vlm/path
Content-Type: application/json

{
  "file_path": "C:/Users/Administrator/Desktop/wiki/00_inbox/test.png",
  "save_to_wiki": true
}
```

### Endpoint 3：批量识别

```http
POST /ocr_vlm/batch
Content-Type: application/json

{
  "folder_path": "C:/Users/Administrator/Desktop/wiki/00_inbox/人机协作双三角/codex",
  "save_to_wiki": true
}
```

### Endpoint 4：健康检查

```http
GET /health
```

---

## 六、数据流设计

```
Agent 上传图片 / 指定路径
        ↓
能力中台接收请求
        ↓
读取图片 → Base64 编码
        ↓
调用 MiniMax API（统一用 Anthropic SDK）
        ↓
获得识别结果
        ↓
写入 wiki/_vlm_output/{filename}_vlm.md
        ↓
返回结果给 Agent
        ↓
Agent 可以进一步调用整合 Agent 生成综合笔记
```

---

## 七、跨平台路径处理

核心代码：

```python
from pathlib import Path

def resolve_wiki_path(relative_path: str) -> Path:
    """统一解析 Windows 和 WSL 下的 wiki 路径"""
    base = Path("/mnt/c/Users/Administrator/Desktop/wiki")
    if not base.exists():
        base = Path("C:/Users/Administrator/Desktop/wiki")
    return base / relative_path
```

更健壮的方案：把 wiki 根目录配置成环境变量 `WIKI_ROOT`，服务启动时自动检测。

```python
import os
from pathlib import Path

def get_wiki_root() -> Path:
    if os.getenv("WIKI_ROOT"):
        return Path(os.getenv("WIKI_ROOT"))
    
    candidates = [
        Path("C:/Users/Administrator/Desktop/wiki"),
        Path("/mnt/c/Users/Administrator/Desktop/wiki"),
        Path.home() / "Desktop" / "wiki",
    ]
    for c in candidates:
        if c.exists():
            return c
    raise FileNotFoundError("Wiki root not found")
```

---

## 八、目录结构建议

```
C:/Users/Administrator/Desktop/wiki/
├── _vlm_output/                    ← 所有 VLM 识别结果统一存这里
│   ├── 2026-07-07/
│   │   ├── test_vlm.md
│   │   └── ...
│   └── ...
├── _capability_hub/                ← 能力中台代码
│   ├── vlm_hub/
│   │   ├── __init__.py
│   │   ├── server.py               ← FastAPI 服务
│   │   ├── mcp_server.py           ← Claude MCP Server
│   │   ├── client.py               ← 通用客户端
│   │   ├── cli.py                  ← 命令行工具
│   │   ├── core.py                 ← MiniMax VLM 调用核心
│   │   └── config.py               ← 配置管理
│   ├── requirements.txt
│   ├── start_server.bat            ← Windows 启动脚本
│   ├── start_server.sh             ← WSL 启动脚本
│   └── README.md
└── ...
```

---

## 九、安全与权限

| 风险 | 方案 |
|------|------|
| API Key 泄露 | 本地服务用本地 API Key，与 MiniMax Key 分离；MiniMax Key 存在 `.env` |
| 外部访问 | 默认只监听 `127.0.0.1`，不开放公网 |
| 文件越界 | 服务只接受 wiki 目录下的路径，拒绝 `../` 等越界路径 |
| 大文件上传 | 限制单文件 20MB，超时 120 秒 |

---

## 十、实施路线图

### 第一阶段：MVP（1-2 天）

1. 写 `vlm_hub/server.py`：一个 FastAPI 服务，支持单文件上传识别
2. 写 `vlm_hub/cli.py`：命令行工具
3. 在 Windows 本机跑起来
4. 用 Kimi Code CLI 调通一次

### 第二阶段：Claude 接入（2-3 天）

1. 写 `vlm_hub/mcp_server.py`
2. 配置 Claude Desktop 的 MCP
3. 测试 Claude 直接调用识别图片

### 第三阶段：批量与整合（1 周）

1. 加批量识别接口 `/ocr_vlm/batch`
2. 加"识别 + 自动整合笔记"接口
3. 把历史识别脚本迁移到中台
4. 写使用文档

### 第四阶段：扩展能力（长期）

1. 把其他能力也接进来：数据分析、PDF 处理、视频理解
2. 加任务队列，支持异步大文件
3. 加用量统计和成本监控

---

## 十一、对现有脚本的处理

你现在已经有：
- `wiki/00_inbox/人机协作双三角/codex/run_vlm_codex.py`
- 各种 `_processed/run_vlm_xxx.py`

**迁移策略**：
- 保留现有脚本作为"单机版"
- 新的中台版写好后，让旧脚本可选地调用中台 API
- 最终逐步统一到 `_capability_hub/vlm_hub/`

---

## 十二、一句话总结

> 能力中台 = 一个跑在 Windows 本机的 FastAPI 本地服务 + 一个给 Claude 用的 MCP Server + 统一的 wiki 存储。所有 Agent 通过 `localhost:8765` 调用同一套 OCR+VLM，结果统一存回 wiki，实现跨 Windows/WSL、跨 Agent 的能力共享。
