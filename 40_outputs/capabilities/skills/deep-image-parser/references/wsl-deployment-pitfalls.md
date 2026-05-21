# Deep Image Parser 部署坎坑记录

## 发现日期
2026-05-22

## 璯境
- WSL2 (Ubuntu) on Windows 11
- Python 3.11.15
- uv 0.11.7

---

## 坑 1：MinerU (magic-pdf) pip 安装反复超时

### 现象
```
uv pip install magic-pdf
# → error: Request failed after 4 retries in 124.7s
# → Caused by: Failed to fetch: `https://pypi.org/simple/brotli/`
# → Caused by: operation timed out

pip install --timeout 300 --index-url https://pypi.tuna.tsinghua.edu.cn/simple magic-pdf
# → [命令超时]
```

### 尝试记录
1. pip 默认超时 → 失败
2. pip --timeout 300 → 失败
3. uv pip install → 失败（依赖下载量大，网络不稳）
4. 清华镜像源 → 仍然超时

### 根因
magic-pdf 依赖链极重：torch + transformers + 多个 CV 库，
下载量达数 GB。WSL 网络环境不稳定时无法完成。

### 解决：降级决策
**不再反复尝试同一个坑**，直接切换策略：
- 主引擎：多模态 AI 视觉分析（零安装，即开即用）
- Fallback：本地 PaddleOCR.js（已部署）
- 未来等网络环境改善后再安装 MinerU

---

## 坑 2：双重 Python 环境陷阱

### 现象
系统 pip 调用的是 Python 3.10，而 venv 中是 Python 3.11。

### 根源
直接运行 `pip install` 可能走到系统 Python，而非 venv。

### 解决
始终先 activate venv：
```bash
source /home/dministrator/.hermes/hermes-agent/venv/bin/activate
python --version  # 确认 3.11
```

---

## 坑 3：PaddleOCR.js 轻量版 vs 深度需求的能力差距

### 现象
对同一张图片（Truman的个人成长五步法.png）：
- PaddleOCR.js 输出：525 字节，乱码严重，表格结构全丢
- 多模态AI输出：完整结构化 Markdown，表格、视觉标记、逻辑关系全部还原

### 根源
PaddleOCR.js（ONNX Runtime）只是基础文字检测+识别，
没有表格结构、公式理解、布局分析能力。

### 解决
对于含有表格/公式/密集文字/视觉标记的图片，
必须使用深度理解引擎。

---

## 通用原则

1. **困难先调研，不要反复试错**
   - 尝试1-2次后仍失败 → 立即切换方案，不要头铁

2. **本地安装前先确认网络环境**
   - 大型 ML 包（torch/transformers等）需要稳定高速网络
   - 下载量 >1GB 时先用 `pip index versions` 查看包大小再决定

3. **混合引擎是最佳实践**
   - 不要过度依赖单一引擎
   - API 主 + 本地 fallback = 可靠性最高

4. **用真图验证**
   - 任何 OCR/vision 引擎都必须用实际素材验证，不能只看文档
