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
source_refs:
- 00_inbox/人机协作双三角/codex/_vlm_output/整合笔记_Codex六大神级Skill.md
- 能力中台设计_OCR-VLM服务.md（洪七公建议书）
related:
- "[[framework-yihang-dual-triangle-weapon-library]]"
- "[[framework-yihang-fde-ai-native-org]]"
- "[[plan_20260701_kdo-multi-repo-architecture]]"
---

# 能力中台架构方案

> **一句话**：KDO 从"知识处理"阶段进入"Agent 军团"阶段后，需要一个标准化的能力中台——让所有 Agent（无论跑在 Claude Code、Kimi Code、Codex 还是 Hermes）都能调用同一套 OCR、VLM、搜索等共享能力。

## 一、为什么需要能力中台

### 当前状态

```
洪七公（Windows/Hermes）
  ├── run_vlm_codex.py       ← 只有他能用
  ├── run_vlm_xxx.py         ← 散落各处
  └── ocr-paddle.cjs         ← Node.js，其他 Agent 不懂

其他 Agent
  └── 想用 OCR/VLM？→ 找洪七公 → 手动处理
```

### 目标状态

```
任何 Agent（Windows/WSL，Claude/Kimi/Codex/Hermes）
  → python -m capability_hub.vlm process --image <path>
  → python -m capability_hub.ocr process --image <path>
  → 结果统一存回 wiki，所有 Agent 可读
```

### 触发条件

- 项目管理域 Agent 即将上线（用户 2026-07-07）
- 未来会有更多域 Agent（销售、内容、设计……）
- 每个 Agent 都可能需要 OCR/VLM/搜索等基础能力
- 不能每个 Agent 都去重复造轮子

## 二、架构设计

### 核心原则

1. **CLI 优先**：每个能力首先是一个标准 CLI 工具——任何能跑 Python 的 Agent 都能调用
2. **MCP 加持**：Claude Code 通过 MCP Server 获得原生工具集成
3. **Python API**：Hermes/脚本可以直接 import 核心模块
4. **统一输出**：结果存入 wiki 约定目录，所有 Agent 可检索
5. **零外部依赖**：纯 Python 标准库 + 已有依赖（MiniMax SDK、PaddleOCR 等）

### 目录结构

```
wiki/
├── _capability_hub/           ← 能力中台代码
│   ├── README.md              ← 架构标准 + 如何添加新能力
│   ├── vlm/                   ← VLM 图片识别（MiniMax）
│   │   ├── __init__.py
│   │   ├── core.py            ← 业务逻辑
│   │   ├── cli.py             ← CLI：python -m capability_hub.vlm process
│   │   └── mcp_server.py      ← MCP Server（Claude 集成）
│   ├── ocr/                   ← OCR 文字提取（PaddleOCR）— 未来
│   ├── pdf/                   ← PDF 解析（MinerU）— 未来
│   ├── search/                ← 统一检索 — 未来
│   └── TEMPLATE.md            ← 新增能力的模板
│
├── _vlm_output/               ← VLM 识别结果（已有）
├── _ocr_output/               ← OCR 提取结果（已有）
└── kdo-tools/                 ← 现有工具脚本（保持不变）
    ├── vlm.py                 ← CLI 入口（薄封装 → capability_hub.vlm）
    ├── daily-context-save.py
    ├── review-check.py
    └── ...
```

### Agent 接入矩阵

| Agent | 运行环境 | 接入方式 |
|:---|:---|:---|
| 黄药师 | Claude Code（Windows/WSL） | `python -m capability_hub.vlm` + MCP Server |
| 王语嫣 | Kimi Code CLI（Windows） | `python -m capability_hub.vlm` |
| 老顽童 | Claude Code / Hermes / Kimi | `python -m capability_hub.vlm` |
| 欧阳锋 | Kimi Code CLI（Windows） | `python -m capability_hub.vlm` |
| 洪七公 | Hermes（WSL/飞书） | `python -m capability_hub.vlm` + Python import |
| 段王爷 | Hermes（WSL/飞书） | `python -m capability_hub.vlm` |
| 销售参谋 | Claude Code | `python -m capability_hub.vlm` |
| **未来 Agent** | 任意环境 | `python -m capability_hub.<capability>` |

### 调用示例

```bash
# CLI 方式（所有 Agent 通用）
python -m capability_hub.vlm process --image "00_inbox/test.png" --prompt-type codex

# Python API（脚本/Hermes）
from capability_hub.vlm.core import process_image
result = process_image("path/to/image.png", prompt_type="codex")

# MCP（Claude Code 原生）
# 在对话中直接说"用 VLM 识别这张图片"
```

## 三、实施计划

### Phase 1：VLM 能力上线（现在做，~1 天）

| # | 动作 | 产出 |
|:--|:---|:---|
| 1 | 创建 `_capability_hub/` 目录 + README 架构标准 | 架构文档 |
| 2 | 从现有脚本提取 MiniMax VLM 核心逻辑 → `vlm/core.py` | 核心模块 |
| 3 | 写 `vlm/cli.py`——标准 CLI 接口 | CLI 工具 |
| 4 | 写 `vlm/mcp_server.py`——Claude MCP 集成 | MCP Server |
| 5 | 用 Kimi Code CLI 路径测试一遍 | 跨平台验证 |
| 6 | 旧脚本 `run_vlm_*.py` 改为调用新模块（薄封装） | 向后兼容 |

### Phase 2：其他能力 + REST API（停车场）

| # | 任务 | 触发条件 | 优先级 |
|:--|:---|:---|:--|
| P-17 | OCR 能力中台化（PaddleOCR 封装） | 第二个 Agent 需要 OCR | P2 |
| P-18 | PDF 能力中台化（MinerU 封装） | Agent 需要批量解析 PDF | P2 |
| P-19 | 统一检索能力（kdo query 中台化） | Agent 不能跑 kdo CLI | P2 |
| P-20 | REST API 层（FastAPI） | Agent > 10 或需要并发 | P2 |
| P-21 | 异步任务队列 + 批量处理 | 日均调用 > 50 次 | P3 |
| P-22 | 用量统计 + 成本监控 | 月 API 费 > ¥100 | P3 |

### 不做的事（明确排除）

- **不建持久服务**（Phase 1）——CLI + MCP 已经覆盖所有调用场景，REST API 等需求驱动再做
- **不做路径抽象层**——`capability_hub` 代码在 wiki 目录下，Windows 和 WSL 各自用各自的路径（`C:\...` vs `/mnt/c/...`），不搞自动检测
- **不迁移现有 OCR 管线**（PaddleOCR）——洪七公已经在用，稳定运行，先不改

## 四、与洪七公建议书的差异

| | 洪七公方案 | 本方案 |
|:---|:---|:---|
| 核心理念 | 能力中台 ✅ | 相同 ✅ |
| 目录位置 | `_capability_hub/vlm_hub/` | `_capability_hub/vlm/` |
| 标准接口 | REST API + MCP + CLI | CLI 优先 + MCP + Python API |
| REST API | Phase 1 就做 | Phase 2（需求驱动） |
| 持久服务 | FastAPI 需要启动/监控 | 不做——零运维 |
| 路径抽象 | 自动检测 Windows/WSL | 各 Agent 用各自路径 |
| OCR 迁移 | 纳入中台 | 暂不迁移（稳定运行中） |
| 实施周期 | 4 阶段 1-2 周 | Phase 1：1 天 |

**核心差异**：洪七公的方案是对的——能力中台方向正确。但 Phase 1 不需要 REST API 和持久服务。CLI + MCP 已经让所有 Agent 都能调用了，REST API 等 Agent 数量和调用频率真的上去之后再加——那时候加一层 FastAPI 是水到渠成，现在加是提前背负运维债务。
