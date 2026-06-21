---
name: presenton-ppt-generator
description: "Presenton 开源 AI PPT 生成器。Docker 一键部署，支持 Ollama 本地 LLM，AI 将 PPTX/PDF 转为可复用模板，输出 PPTX + PDF。完全自托管，数据不出机器。替换手写 python-pptx 流程。"
version: 1.0.0
category: creative
metadata:
  hermes:
    tags: [ppt, presentation, slides, docker, ollama, ai, open-source, self-hosted]
    related_skills:
      - beikai-multimodal-pipeline
      - markdown-to-ppt-pipeline
      - baoyu-infographic
      - cosyvoice-tts
---

# Presenton — 开源 AI PPT 生成器

> "python-pptx 手写 PPT？那叫搬砖。Presenton 一句话出二十页，模板复用、品牌锁定——叫花子终于能体面地交付了。" — 洪七公

## 定位

北丐文档武器的**自动化升级**，替换手写 python-pptx：

| 维度 | markdown-to-ppt-pipeline（旧） | Presenton（新） |
|:--|:--|:--|
| 生成方式 | python-pptx 手写代码 | **AI 模板 + 自然语言** |
| 模板复用 | 每次重新设计 | ✅ AI 模板转换器 |
| LLM 依赖 | 需外部 API | **Ollama 本地 / 任意 API** |
| 数据安全 | 本地 | **完全自托管** |
| 输出格式 | PPTX | PPTX + PDF |
| API | 无 | ✅ REST API |
| 品牌一致性 | 手动调整 | ✅ 模板锁定品牌 |
| 部署 | Python 脚本 | **Docker 一键** |
| 许可证 | 自写 | 开源 |

## 技术规格

| 维度 | 数值 |
|:--|:--|
| 类型 | 开源 AI 演示文稿生成器 |
| 部署 | Docker 单容器 |
| LLM 后端 | Ollama / OpenAI / Anthropic / 任意兼容 API |
| 图像生成 | 可接入 FLUX.2 / Stable Diffusion |
| 模板系统 | AI 转换现有 PPTX/PDF 为可复用模板 |
| 输出 | PPTX（完全可编辑）+ PDF |
| API | REST API（可嵌入 SaaS 产品） |
| 白标 | 支持 |
| 离线 | ✅ 完全离线（Ollama 模式） |

## 安装

### Docker 一键部署（推荐）

```bash
# 基础版
docker run -it --name presenton \
  -p 5000:80 \
  -v "./app_data:/app/app_data" \
  ghcr.io/presenton/presenton:latest

# 访问 http://localhost:5000
```

### 配合 Ollama（完全本地）

```bash
# 先启动 Ollama
ollama serve

# 拉取模型
ollama pull qwen3:14b

# 启动 Presenton（挂载 Ollama）
docker run -it --name presenton \
  -p 5000:80 \
  -v "./app_data:/app/app_data" \
  -e LLM_PROVIDER=ollama \
  -e OLLAMA_HOST=http://host.docker.internal:11434 \
  -e LLM_MODEL=qwen3:14b \
  ghcr.io/presenton/presenton:latest
```

### 离线/气隙部署

```bash
# 金融/政企等需合规场景
docker run -it --name presenton \
  -p 5000:80 \
  -v "./app_data:/app/app_data" \
  -e LLM_PROVIDER=ollama \
  --network none \
  ghcr.io/presenton/presenton:latest
```

## 快速使用

### Web UI 生成

```
1. 打开 http://localhost:5000
2. 输入主题："2026年Q2多模态AI工具链全景报告"
3. 选择品牌模板
4. 点击生成 → 下载 PPTX
```

### API 编程生成

```python
import requests

PRESENTON = "http://localhost:5000"

def generate_ppt(topic: str, template: str = "default") -> str:
    """生成 PPT，返回下载链接"""
    resp = requests.post(f"{PRESENTON}/api/generate", json={
        "topic": topic,
        "template": template,
        "slide_count": 12,
        "language": "zh",
        "include_charts": True,
        "style": "professional"
    })
    data = resp.json()
    return data["download_url"]

def generate_batch(topics: list[str]) -> list[str]:
    """批量生成"""
    urls = []
    for topic in topics:
        url = generate_ppt(topic)
        urls.append(url)
        print(f"✅ {topic[:30]}... → {url}")
    return urls

# 示例
topics = [
    "KDO 知识交付系统技术架构",
    "多模态 AI 工具链选型报告",
    "2026年开源 AI 生态全景",
]
urls = generate_batch(topics)
for url in urls:
    # 下载 PPTX
    r = requests.get(f"{PRESENTON}{url}")
    with open(url.split("/")[-1], "wb") as f:
        f.write(r.content)
```

### 模板 AI 转换

```bash
# 把现有的 PPTX 转为可复用模板
curl -X POST http://localhost:5000/api/templates/convert \
  -F "file=@brand_template.pptx" \
  -F "name=公司品牌模板"

# 之后生成 PPT 时指定模板
# template: "公司品牌模板"
```

## 集成到北丐流水线

### KDO 知识卡片 → PPT

```
KDO Markdown 卡片
│
├── 1. Markdown 内容提取（标题/要点/数据）
├── 2. Presenton API 生成 PPT
│      - 模板: "KDO知识卡片模板"
│      - LLM: 本地 Ollama
│      - 图表: 自动生成
├── 3. 下载 PPTX
└── 4. 存入 40_outputs/content/presentations/
```

### 批量报告生成

```python
"""从 00_inbox 目录批量生成 PPT 报告"""
from pathlib import Path
import requests

def batch_from_markdown(inbox_dir: str, output_dir: str):
    for md_file in Path(inbox_dir).glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        title = md_file.stem
        
        resp = requests.post("http://localhost:5000/api/generate", json={
            "topic": title,
            "content": content[:5000],  # 前 5000 字
            "template": "knowledge_report",
            "slide_count": 10,
            "language": "zh"
        })
        
        url = resp.json()["download_url"]
        pptx = requests.get(f"http://localhost:5000{url}").content
        output_path = Path(output_dir) / f"{title}.pptx"
        output_path.write_bytes(pptx)
        print(f"✅ {title}")
```

## 对比决策

| 需求 | 用 Presenton | 用 python-pptx 手写 |
|:--|:--|:--|
| 一次性 PPT | ✅ 快速 | ❌ 太慢 |
| 精确像素排版 | ❌ AI 不可控 | ✅ |
| 品牌模板固化 | ✅ 一次转换 | ❌ 每次手写 |
| 批量 100+ 份 | ✅ API 批量 | ❌ 调试噩梦 |
| 数据图表 | ✅ 自动生成 | 🟡 pandas+pptx |
| 离线合规 | ✅ Docker 本地 | ✅ |
| 嵌入 SaaS | ✅ REST API | ❌ 无 API |

## 与其他工具配合

```
成品交付套餐:
  信息图 ← baoyu-infographic
  架构图 ← Draw.io MCP
  手绘图 ← excalidraw
  配图   ← FLUX.2 (ComfyUI)
  PPT    ← Presenton
  视频   ← Wan 2.2 + hyperframes
  配音   ← CosyVoice 3.0
```

## 常见坑点

### Pitfall 1: Docker 权限
```bash
# 如果报 permission denied
sudo usermod -aG docker $USER
newgrp docker
```

### Pitfall 2: Ollama 连接失败
Docker 内访问宿主 Ollama：
```bash
# Linux
-e OLLAMA_HOST=http://host.docker.internal:11434

# WSL2
-e OLLAMA_HOST=http://172.17.0.1:11434
```

### Pitfall 3: 模板转换质量
AI 模板转换依赖原始 PPTX 结构清晰。复杂的动画/母版可能丢失。

### Pitfall 4: PPTX 中文兼容
生成后建议用 WPS/LibreOffice 检查中文排版（微软 PowerPoint 最佳）。

### Pitfall 5: 大规模批量限流
单实例并发生成约 2-3 个/分钟。如需更高吞吐，多实例 + 队列。

## 验证清单

- [ ] Docker 容器正常启动
- [ ] Web UI 可访问 http://localhost:5000
- [ ] 输入主题生成 PPTX 成功
- [ ] API `/api/generate` 返回下载链接
- [ ] 模板 AI 转换可用
- [ ] Ollama 本地 LLM 模式正常

## 参考资料

- 官网: https://presenton.ai
- Docker: https://github.com/presenton/presenton/pkgs/container/presenton
- 文档: https://docs.presenton.ai
- 模板创建: https://docs.presenton.ai/create-presentation-template-with-ai
