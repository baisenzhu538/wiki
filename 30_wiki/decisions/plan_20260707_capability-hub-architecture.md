---
id: plan_20260707_capability-hub-architecture
title: 能力中台架构方案——多 Agent 共享能力层
type: decision
status: draft
domain:
- agent-infrastructure
- capability-hub
author: 黄药师
created_at: 2026-07-07
confidence: 0.85
trust_level: high
related:
- "[[framework-yihang-dual-triangle-weapon-library]]"
- "[[framework-yihang-fde-ai-native-org]]"
---

# 能力中台架构方案

> **一句话**：让任何 Agent——无论跑在 Claude Code、Kimi Code、Codex、Hermes，无论通过飞书还是微信——都能用同一行代码调用 OCR、VLM、搜索等共享能力。API Key 写死在能力模块里，Agent 不需要知道自己用的是 MiniMax 还是 PaddleOCR。

---

## 一、审美：什么叫"好"？

按双三角模型，先定标准再谈实现。

### 标准 1：一行注册，即刻可用

```
# Agent 使用 VLM 能力的唯一姿势
from capability_hub.vlm import process
result = process("path/to/image.png")
```

不需要配置 API Key、不需要知道用的是哪个模型、不需要管路径是 Windows 还是 WSL。能力模块内部搞定一切。

**反模式**：Agent 每次调用前要设置环境变量、找 API Key、处理路径转换。

### 标准 2：能力和 Agent 解耦

```
Agent（飞书）──┐
Agent（微信）──┼──→ capability_hub（注册表）──→ VLM/OCR/搜索/...
Agent（Claude）─┘
```

Agent 不知道自己调用的能力跑在什么模型上。今天用 MiniMax-M3，明天换 GPT-5，Agent 代码一行不改。

**反模式**：Agent 代码里硬编码了模型名、API endpoint。

### 标准 3：自描述 + 可发现

```
$ python -m capability_hub list

  vlm      图片识别（MiniMax-M3）    可用 ✅
  ocr      文字提取（PaddleOCR v5）  可用 ✅
  search   统一检索                  规划中 🟡
```

任何 Agent 启动时可以问一句"现在有什么能力可用？"

**反模式**：能力存在但 Agent 不知道——就像王语嫣不知道 OSCAR 已经存在。

### 标准 4：零运维

没有需要启动的服务。没有需要监控的进程。没有端口冲突。能力 = Python 模块，import 即用。

**反模式**：洪七公休假，FastAPI 服务挂了，所有 Agent 的 OCR 能力全挂。

### 标准 5：输出统一存 wiki

无论哪个 Agent 调的、从哪个平台调的，结果都存入 wiki 约定目录。Agent A 识别的图片，Agent B 可以通过 `kdo query` 搜到。

**反模式**：每个 Agent 把结果存在自己的临时目录，换个 Agent 就找不到。

---

## 二、体系：怎么建？

### 2.1 目录结构

```
wiki/
├── _capability_hub/           ← 能力中台
│   ├── registry.py            ← 能力注册表（自发现）
│   ├── base.py                ← 能力基类（每个能力继承它）
│   ├── config.py              ← 统一配置（API Keys 写在这里）
│   │
│   ├── vlm/                   ← VLM 图片识别
│   │   ├── __init__.py        ← 注册：registry.register(VLMCapability)
│   │   └── core.py            ← MiniMax API 调用逻辑
│   │
│   ├── ocr/                   ← OCR 文字提取（未来）
│   ├── pdf/                   ← PDF 解析（未来）
│   ├── search/                ← 统一检索（未来）
│   └── TEMPLATE.md            ← 新增能力的模板
│
├── _vlm_output/               ← VLM 结果存储
├── _ocr_output/               ← OCR 结果存储
└── kdo-tools/                 ← 现有工具（不变）
```

### 2.2 注册机制

每个能力是一个 Python 类，继承 `base.Capability`，在 `__init__.py` 中自注册：

```python
# _capability_hub/vlm/__init__.py
from capability_hub.registry import register
from capability_hub.vlm.core import VLMCapability

register(VLMCapability())
```

Agent 发现能力：

```python
from capability_hub.registry import list_capabilities
for cap in list_capabilities():
    print(cap.name, cap.description, cap.status)
```

Agent 调用能力：

```python
from capability_hub.registry import get
result = get("vlm").process(image_path="...", prompt_type="codex")
```

### 2.3 API Key 内嵌

所有外部 API 的 Key 统一写在 `_capability_hub/config.py`：

```python
# _capability_hub/config.py
MINIMAX_API_KEY = "sk-xxx"       # VLM
PADDLEOCR_HOME = "C:\\..."       # OCR（本地，无需 Key）
MINERU_PATH = "/home/.../mineru" # PDF
```

Agent 永远不需要传 API Key。换 Key 时改一处，所有 Agent 自动生效。

### 2.4 跨平台路径

能力模块接受相对路径（相对于 wiki 根目录），内部自动解析：

```python
# Agent 调用（Windows、WSL 都这样写）
result = process("00_inbox/test.png")

# 能力内部自动解析为绝对路径
# Windows: C:/Users/Administrator/Desktop/wiki/00_inbox/test.png
# WSL:     /mnt/c/Users/Administrator/Desktop/wiki/00_inbox/test.png
```

不做自动检测——各平台 Agent 启动时设一次 `WIKI_ROOT` 环境变量即可。

### 2.5 Agent 接入一览

| Agent | 运行环境 | 调用方式 | 需要做什么 |
|:---|:---|:---|:---|
| 黄药师 | Claude Code（Windows/WSL） | `from capability_hub.vlm import process` | 无——已在 wiki 目录 |
| 王语嫣 | Kimi Code CLI（Windows） | 同上 | `sys.path` 已含 wiki 根目录 |
| 老顽童 | 多平台 | 同上 | 同上 |
| 欧阳锋 | Kimi Code CLI（Windows） | 同上 | 同上 |
| 洪七公 | Hermes（WSL → 飞书） | 同上 | Hermes venv 需装 MiniMax SDK |
| 段王爷 | Hermes（WSL → 飞书） | 同上 | 同上 |
| 销售参谋 | Claude Code | 同上 | 无 |
| **未来微信 Agent** | 微信机器人（Python） | 同上 | `pip install` 依赖包 |
| **未来项目管理 Agent** | 待定 | 同上 | `sys.path` 指向 wiki |

所有 Agent 的调用代码完全一样。区别只在环境配置（一次性）。

---

## 三、实施：什么时候做什么？

### Phase 1：现在做（0.5-1 天）——让 VLM 能力上线

| # | 动作 | 产出 |
|:--|:---|:---|
| 1 | 建 `_capability_hub/` 目录结构 + `registry.py` + `base.py` + `config.py` | 中台骨架 |
| 2 | 从现有脚本提取 MiniMax VLM 逻辑 → `vlm/core.py` | VLM 核心模块 |
| 3 | `vlm/__init__.py` 自注册 | 注册表可发现 VLM 能力 |
| 4 | 写 `python -m capability_hub list` | 能力列表命令 |
| 5 | 用多个路径测试（Windows 绝对路径 + WSL 相对路径） | 跨平台验证 |
| 6 | 旧 `run_vlm_*.py` 脚本改为调用新模块 | 向后兼容 |

### Phase 2：停车场——其他能力 + 增强

| # | 任务 | 触发条件 | 优先级 |
|:--|:---|:---|:--|
| P-17 | OCR 能力中台化（PaddleOCR → `_capability_hub/ocr/`） | 第二个 Agent 需要 OCR | P2 |
| P-18 | PDF 能力中台化（MinerU → `_capability_hub/pdf/`） | Agent 需要批量解析 PDF | P2 |
| P-19 | 搜索能力中台化（`kdo query` → `_capability_hub/search/`） | Agent 不能跑 kdo CLI 的环境 | P2 |
| P-20 | MCP Server 封装（每个能力可选地暴露为 MCP 工具） | Claude Code 需要原生集成 | P2 |
| P-21 | 用量统计 + 成本监控 | 月 API 费 > ¥100 | P3 |
| P-22 | 异步批处理（任务队列） | 日均调用 > 50 次 | P3 |

### 不做的事

- **不做 REST API / 持久服务**（Phase 1）——Python import 已经覆盖所有 Agent 的调用场景。将来如果出现"不能跑 Python 但需要调能力"的 Agent（如纯 Node.js 微信机器人），再加一层 HTTP 封装。
- **不做路径自动检测**——各 Agent 启动时设 `WIKI_ROOT` 环境变量，比自动检测更可靠。

---

## 四、与洪七公建议书的关系

洪七公的判断是对的——需要一个中台。差异在执行节奏：

| | 洪七公方案 | 本方案 |
|:---|:---|:---|
| 方向 | 能力中台 | 相同 ✅ |
| Phase 1 做什么 | FastAPI + MCP + CLI 三件套 | 注册表 + 自描述模块 |
| API Key 管理 | Agent 传 `X-API-Key` header | 写死在 `config.py`——Agent 零配置 |
| Agent 发现能力 | 看文档 | `python -m capability_hub list` |
| 运维负担 | 需要启动/监控 FastAPI 服务 | 零——纯 Python import |
| REST API | 上来就建 | 等出现"不能跑 Python 的 Agent"再加 |
