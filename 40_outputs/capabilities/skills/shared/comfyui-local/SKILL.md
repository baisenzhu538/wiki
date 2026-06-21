---
name: comfyui-local
description: "ComfyUI 本地多模态 AI 编排中枢。节点式可视化工作流引擎，统一管理图片生成、视频生成、音频合成、3D渲染。支持 API 批量自动化、ComfyHub 社区工作流复用。GPL v3 开源。"
version: 1.0.0
category: creative
metadata:
  hermes:
    tags: [comfyui, workflow, orchestration, image-generation, video-generation, audio, multimodal, automation]
    related_skills:
      - beikai-multimodal-pipeline
      - stable-diffusion-image-generation
      - wan-video-generation
      - vlm-image-describe-pipeline
  env:
    COMFYUI_DIR: "ComfyUI 安装目录"
    COMFYUI_PORT: "服务端口（默认 8188）"
---

# ComfyUI — 多模态 AI 编排中枢

> "散装工具打到头也就是降龙十八掌前三招。ComfyUI 是把刀架，把 Wan 2.2、FLUX.2、CosyVoice 全挂上去，一招连环——这才叫十八掌齐发。" — 洪七公

## 定位

北丐多模态武器库的**统一中枢**，替代散装的独立工具链：

```
旧架构（散装）:
  hyperframes → 视频
  Edge TTS → 音频
  image_gen → 图片
  baoyu-infographic → 信息图
  excalidraw → 手绘图
  (各工具独立调用，无法串联)

新架构（ComfyUI 中枢）:
  ComfyUI ──┬── FLUX.2 → 文生图（替换 stable-diffusion）
            ├── Wan 2.2 → 文生视频/图生视频
            ├── LTX-2.3 → 快速视频+音频
            ├── CosyVoice 3.0 → TTS节点
            ├── Qwen-Image → 图片编辑
            └── Tripo3D → 3D生成
  (一个 API，一条工作流，全链路自动化)
```

## 技术规格

| 维度 | 数值 |
|:--|:--|
| 类型 | 节点式可视化 AI 工作流引擎 |
| 最新版本 | v0.25.1（2026-06-16） |
| 许可证 | GPL v3（开源免费） |
| 后端 | Python + PyTorch + aiohttp |
| 前端 | Web UI（浏览器访问） |
| API | REST + WebSocket |
| 默认端口 | 8188 |
| GPU 需求 | NVIDIA CUDA（推荐 RTX 3060 12GB+） |
| CPU 模式 | 支持但极慢（不推荐生产） |
| 官网 | https://comfy.org |
| GitHub | comfyanonymous/ComfyUI |

## 核心能力

### 支持的模态（2026年）

| 模态 | 节点/模型 | 用途 |
|:--|:--|:--|
| **文生图** | FLUX.2, SDXL, Z-Image-Turbo, Ideogram 4 | 高质量图片生成 |
| **图生图** | Qwen-Image-Edit, Nano Banana 2 | 图片编辑/修复 |
| **文生视频** | Wan 2.2, HunyuanVideo, Kling V3, Seedance 2.0 | AI 视频生成 |
| **图生视频** | LTX-2.3, CogVideoX | 图片转视频 |
| **音频** | Stable Audio 3.0, CosyVoice | 音乐/TTS |
| **3D** | Tripo3D, Gaussian Splat | 3D模型生成 |
| **视频后处理** | RTX Video Super Resolution, LatentSync | 4K升频/唇形同步 |
| **LLM集成** | Gemini Text 节点 | 文本生成+图像 |

### App View vs Node View

```yaml
App View（简易模式）:
  - 输入文本提示 → 一键生成
  - 适合快速原型
  - 2026年新增

Node View（专业模式）:
  - 节点式可视化工作流
  - 分支/循环/条件逻辑
  - 适合批量自动化
```

## 安装

### 硬件前提
```bash
# 检查 GPU
nvidia-smi

# 需要: NVIDIA GPU + CUDA 11.8+ + ≥12GB VRAM（推荐24GB）
```

### 一键安装

```bash
# 1. 克隆
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动
python main.py
# → http://localhost:8188
```

### ComfyUI Manager（推荐）
```bash
cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
# 重启 ComfyUI，UI 中会出现 Manager 按钮
# 通过 Manager 一键安装模型和自定义节点
```

## 关键工作流

### 工作流 1：文章→配图→视频（北丐主流水线）

```
[文本输入] → [LLM 分段] → [FLUX.2 生成配图]
    → [Wan 2.2 图生视频] → [CosyVoice TTS 配音]
    → [LatentSync 唇形同步] → [FFmpeg 合并输出]
```

### 工作流 2：批量信息图生成

```
[CSV 数据] → [循环节点] → [FLUX.2 + ControlNet]
    → [RTX Upscale 4K] → [批量保存 PNG]
```

### 工作流 3：声音克隆 + 视频

```
[参考音频] → [CosyVoice 声音克隆]
[文本脚本] → [CosyVoice TTS] → [音频输出]
[图片素材] → [Wan 2.2 动画] → [视频输出]
    → [LatentSync 音视频对齐] → [成品 MP4]
```

## API 自动化

### REST API 核心端点

```python
import json, urllib.request, websocket

COMFYUI = "http://localhost:8188"

def queue_prompt(workflow: dict) -> str:
    """提交工作流，返回 prompt_id"""
    req = urllib.request.Request(
        f"{COMFYUI}/prompt",
        data=json.dumps({"prompt": workflow}).encode(),
        headers={"Content-Type": "application/json"}
    )
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp["prompt_id"]

def get_history(prompt_id: str) -> dict:
    """获取执行结果"""
    resp = json.loads(urllib.request.urlopen(f"{COMFYUI}/history/{prompt_id}").read())
    return resp[prompt_id]

def wait_for_result(prompt_id: str, ws_url: str = "ws://localhost:8188/ws") -> dict:
    """WebSocket 监听执行完成"""
    ws = websocket.WebSocket()
    ws.connect(ws_url)
    while True:
        msg = json.loads(ws.recv())
        if msg["type"] == "executed" and msg["data"]["prompt_id"] == prompt_id:
            ws.close()
            return get_history(prompt_id)
```

### 批量处理脚本

```python
"""批量文生图"""
import json, base64, urllib.request
from pathlib import Path

# 加载预定义工作流
with open("workflow_text2img.json") as f:
    workflow = json.load(f)

prompts = [
    "洪七公在华山之巅打出降龙十八掌",
    "北丐多模态渲染流水线全景图",
    "KDO 知识管理系统架构图",
]

for i, prompt in enumerate(prompts):
    # 修改工作流中的 prompt 节点
    for node in workflow.values():
        if node.get("class_type") == "CLIPTextEncode":
            node["inputs"]["text"] = prompt
    
    # 提交
    req = urllib.request.Request(
        "http://localhost:8188/prompt",
        data=json.dumps({"prompt": workflow}).encode(),
        headers={"Content-Type": "application/json"}
    )
    prompt_id = json.loads(urllib.request.urlopen(req).read())["prompt_id"]
    print(f"[{i+1}/{len(prompts)}] {prompt[:30]}... → {prompt_id}")
```

### ComfyHub 工作流复用

```
# 社区高质量工作流（直接拖入 ComfyUI 使用）
https://comfy.org/workflows
  - 热门: Seedance 2.0 视频生成
  - 热门: FLUX.2 + LoRA 角色生成
  - 热门: Wan 2.2 文生视频
  - 热门: LTX 2.3 Lipdub + Voice Clone
```

## 集成到北丐流水线

### 决策：何时用 ComfyUI vs 单工具

```
任务类型
│
├── 单一模态（纯图片/纯音频）
│   └── 直接用单工具（image_gen / CosyVoice）
│
├── 多模态串行（图+音+视频）
│   └── ⭐ ComfyUI 编排
│
├── 批量处理（100+ 张）
│   └── ⭐ ComfyUI API + 队列
│
└── 交互式调试
    └── ComfyUI Web UI
```

### 与现有工具对比

| 能力 | 旧方案 | ComfyUI 方案 |
|:--|:--|:--|
| 文生图 | stable-diffusion ❌ 不可用 | FLUX.2 ✅ |
| 图生视频 | 无 | Wan 2.2 / LTX-2.3 ✅ |
| 批量自动化 | 各脚本独立 | 统一 API ✅ |
| 工作流复用 | 无 | ComfyHub 社区 ✅ |
| 4K 升频 | ffmpeg 软升 | RTX VSR 硬升 ✅ |

## 性能基准

| 任务 | GPU | 速度 |
|:--|:--|:--|
| FLUX.2 1024² 文生图 | RTX 4090 | ~3秒/张 |
| Wan 2.2 5秒视频 | RTX 4090 | ~4-8分钟 |
| LTX-2.3 5秒视频+音频 | RTX 4090 | ~4-11秒 |
| RTX VSR 720p→4K | RTX 4090 | ~实时 |

## 常见坑点

### Pitfall 1: GPU 内存不足
```bash
# 启动时限制 VRAM
python main.py --lowvram        # 适合 6-8GB
python main.py --novram         # CPU only（极慢）
python main.py --reserve-vram 2.0  # 保留 2GB
```

### Pitfall 2: 自定义节点缺失
报 `Cannot import module` → ComfyUI Manager 安装缺失节点：
```bash
cd custom_nodes && git clone <缺失节点仓库>
```

### Pitfall 3: 模型下载
ComfyUI 不自带模型，需手动下载到 `models/` 目录：
```
models/
├── checkpoints/     # SDXL, FLUX.2 (.safetensors)
├── vae/             # VAE 模型
├── diffusion_models/ # Wan 2.2, LTX-2.3
├── upscale_models/  # 4K 升频模型
└── tts/             # CosyVoice 模型
```

### Pitfall 4: WSL2 GPU 直通
WSL2 需要 Windows 端安装 NVIDIA 驱动 + WSL CUDA 支持：
```powershell
# Windows 端
wsl --update
wsl --shutdown
# 重进 WSL 后 nvidia-smi 应可用
```

### Pitfall 5: API 并发限制
ComfyUI 默认单任务队列。批量任务用队列模式，不要并发提交。

### Pitfall 6: 工作流 JSON 结构
工作流 JSON 的 node ID 必须是字符串数字。从 UI 导出工作流时保持格式不变。

## 验证清单

- [ ] `python main.py` 启动无报错
- [ ] 浏览器打开 `http://localhost:8188` 看到 UI
- [ ] 加载示例工作流 → 执行 → 成功生成
- [ ] API `/prompt` 端点返回 prompt_id
- [ ] WebSocket 连接 `ws://localhost:8188/ws` 正常
- [ ] ComfyUI Manager 可安装缺失节点

## 参考资料

- 官网: https://comfy.org
- GitHub: https://github.com/comfyanonymous/ComfyUI
- 工作流市场: https://comfy.org/workflows
- API 文档: https://docs.comfy.org
- ComfyUI Manager: https://github.com/ltdrdata/ComfyUI-Manager
