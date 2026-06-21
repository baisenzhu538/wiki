---
name: cosyvoice-tts
description: "CosyVoice 3.0 中文TTS与声音克隆引擎。阿里巴巴 FunAudioLLM 开源，支持9语言+18方言，零样本声音复刻，150ms流式延迟。Apache 2.0 许可证。替换 Edge TTS 的主战武器。"
version: 1.0.0
category: creative
metadata:
  hermes:
    tags: [tts, voice-cloning, chinese, multilingual, audio, cosyvoice, alibaba]
    related_skills:
      - beikai-multimodal-pipeline
      - text-to-audio-pipeline
      - audiocraft-audio-generation
  env:
    COSYVOICE_MODEL_DIR: "CosyVoice 模型目录路径"
---

# CosyVoice 3.0 — 中文 TTS 与声音克隆

> "叫花子终于不用再求 Edge TTS 那口快舌了——阿里开源这把刀，九种语言、十八路方言，还能复刻人声。" — 洪七公

## 定位

北丐 TTS 武器库的**主战武器**，替换 Edge TTS：

| 维度 | Edge TTS（旧） | CosyVoice 3.0（新） |
|:--|:--|:--|
| 中文自然度 | ⚠️ 语速偏快、不可控 | ✅ SOTA 自然度 |
| 声音克隆 | ❌ 不支持 | ✅ 3-10秒零样本复刻 |
| 方言 | ❌ 不支持 | ✅ 18+ 方言 |
| 情感控制 | ❌ 不支持 | ✅ 指令控制（快/慢/喜怒） |
| 流式 | ❌ 批量 | ✅ 150ms 双向流式 |
| 许可证 | 微软服务条款 | **Apache 2.0** |
| 离线 | ❌ 需联网 | ✅ 完全本地 |

## 技术规格

| 维度 | 数值 |
|:--|:--|
| 开发者 | 阿里巴巴通义语音实验室 |
| 模型 | Fun-CosyVoice3-0.5B |
| 参数量 | 0.5B（轻量）/ 1.5B（完整） |
| 语言 | 中/英/日/韩/德/西/法/意/俄 9种 |
| 方言 | 粤/闽南/四川/东北/陕西/上海/天津等 18+ |
| 延迟 | 首包 150ms（流式） |
| 采样率 | 24kHz |
| 内容一致性 | CER 0.81%（业界最低） |
| 许可证 | Apache 2.0（完全商用） |
| GitHub | FunAudioLLM/CosyVoice |
| HuggingFace | FunAudioLLM/Fun-CosyVoice3-0.5B-2512 |

## 硬件需求

| 配置 | CPU Only | GPU (推荐) |
|:--|:--|:--|
| RAM | ≥ 8GB | ≥ 8GB |
| VRAM | — | ≥ 4GB (0.5B模型) |
| 推理速度 | ~5-10x 实时 | ~实时 |
| 适用 | 非实时批量 | 实时/流式 |

> ⚠️ WSL2 CPU 推理可行但偏慢（~10秒生成1秒音频）。建议配 NVIDIA GPU。

## 安装

### 环境要求
- Python 3.10（推荐）/ 3.11
- Git LFS（模型下载）
- CUDA 11.8+（GPU 加速，可选）

### 一键安装

```bash
# 1. 克隆仓库（含子模块）
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
cd CosyVoice

# 2. 创建虚拟环境
python3 -m venv cosyvoice_env
source cosyvoice_env/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 安装文本前端处理
cd pretrained_models/CosyVoice-ttsfrd/
unzip resource.zip -d .
pip install ttsfrd_dependency-0.1-py3-none-any.whl
pip install ttsfrd-0.4.2-cp310-cp310-linux_x86_64.whl
cd ../..

# 5. 下载模型（从 HuggingFace）
pip install huggingface_hub
huggingface-cli download FunAudioLLM/Fun-CosyVoice3-0.5B-2512 \
  --local-dir pretrained_models/Fun-CosyVoice3-0.5B

# 或从 ModelScope（国内更快）
pip install modelscope
python -c "
from modelscope import snapshot_download
snapshot_download('FunAudioLLM/Fun-CosyVoice3-0.5B-2512',
                  local_dir='pretrained_models/Fun-CosyVoice3-0.5B')
"
```

## 快速使用

### 基础 TTS（预设音色）

```python
import sys
sys.path.append('third_party/Matcha-TTS')
from cosyvoice.cli.cosyvoice import CosyVoice3
from cosyvoice.utils.file_utils import load_wav
import torchaudio

# 加载模型
model = CosyVoice3('pretrained_models/Fun-CosyVoice3-0.5B', load_jit=False, fp16=False)

# 生成语音（使用默认音色）
output = model.inference_zero_shot(
    '洪七公今天给大家演示一下什么叫降龙十八掌。',
    '',  # prompt text（空=默认音色）
    '',  # prompt audio path（空=默认音色）
    stream=False
)

# 保存
torchaudio.save('output.wav', output['tts_speech'], 24000)
print("✅ 语音生成完成: output.wav")
```

### 零样本声音克隆

```python
# 用 3-10 秒参考音频克隆声音
prompt_audio = 'reference_voice.wav'  # 你的声音样本
prompt_text = '这是参考音频对应的文字内容。'

output = model.inference_zero_shot(
    '现在我用克隆的声音说话，这招降龙十八掌果然名不虚传。',
    prompt_text,
    prompt_audio,
    stream=False
)

torchaudio.save('cloned_output.wav', output['tts_speech'], 24000)
```

### 指令控制（情感/语速）

```python
# 使用 Instruct 标签控制
texts = [
    '<fast>快快快！三招之内，必取你性命！</fast>',
    '<slow>这一掌，叫做亢龙有悔，要慢慢体会其中的奥妙。</slow>',
    '<angry>岂有此理！竟敢欺我丐帮无人！</angry>',
    '<peppa>大家好，我是小猪佩奇，这是我的弟弟乔治。</peppa>',
]

for i, text in enumerate(texts):
    output = model.inference_zero_shot(text, '', '', stream=False)
    torchaudio.save(f'instruct_{i}.wav', output['tts_speech'], 24000)
```

### 流式输出（低延迟）

```python
# 边生成边播放
output = model.inference_zero_shot(
    '这是一段很长的文字，用来测试流式输出的效果如何。',
    '', '', stream=True
)

for chunk in output:
    # 每个 chunk 包含一段音频
    print(f"收到音频块: {chunk['tts_speech'].shape}")
    # 可以实时播放或累积
```

### 命令行快速测试

```bash
# 运行官方示例
python example.py

# 启动 WebUI
python webui.py --port 50000 --model_dir pretrained_models/Fun-CosyVoice3-0.5B
# 浏览器打开 http://localhost:50000
```

## 集成到北丐流水线

### 口语化润色预处理（⭐ 来自 Candy 逐字稿方法论）

TTS 直接读文章稿会生硬。在调用 CosyVoice 之前，先用 Candy 口语化润色的 7 条原则做预处理：

| # | 原则 | 对 TTS 的意义 |
|:--|:--|:--|
| 1 | 短句有呼吸感（≤25字/句） | CosyVoice 短句停顿更自然 |
| 2 | 口语连接词（"先说""然后""说白了"） | 不像机器念稿 |
| 3 | 场景先于道理 | 场景句语调自然，道理句容易平 |
| 4 | 术语后面跟人话 | TTS 读术语不卡壳 |
| 5 | 保留人设 | 保留作者口语习惯 |
| 6 | 不改有力量的原句 | 保留金句的节奏感 |
| 7 | 结构稳定后才润色 | 框架没定不碰文字 |

**预处理 Prompt**（引用自 `30_wiki/tools/tool-candy-oral-polish`）：

```python
polish_prompt = """对以下文本执行口语化润色。严格遵循：
1. 短句——每句不超过25字。超过就拆。
2. 口语连接词——用"先说""然后""最后就是"替代"首先其次最后"
3. 场景先于道理——每个道理前，先用一个场景切入
4. 术语后人话——每个术语后面跟一句人话解释
5. 保留人设——不改动作者的口语习惯和特色表达
6. 不改有力量的原句——如果原句已经很好了，跳过
7. 不重写——这是润色，不是改写。保留原结构和逻辑链。

原文本：
{TEXT}
"""
```

**完整 TTS 流水线**：

```
文章原文
  → Candy 口语化润色 Prompt（LLM 预处理）
  → CosyVoice 3.0 TTS
  → 输出自然语音
```

### 替换边端 TTS → 文章转音频

```python
# 旧方式：Edge TTS（语速快、无克隆）
# text_to_speech("文章内容")

# 新方式：CosyVoice 3.0
from cosyvoice.cli.cosyvoice import CosyVoice3
model = CosyVoice3('pretrained_models/Fun-CosyVoice3-0.5B', load_jit=False, fp16=False)

def tts_article(text: str, output_path: str, voice_sample: str = None):
    """文章转语音"""
    prompt_text = ''
    prompt_audio = ''
    if voice_sample:
        prompt_audio = voice_sample
        prompt_text = '参考音频的文字内容'
    
    output = model.inference_zero_shot(text, prompt_text, prompt_audio, stream=False)
    torchaudio.save(output_path, output['tts_speech'], 24000)
    return output_path
```

### 与 hyperframes 配合（视频配音）

```python
# 先 CosyVoice 生成配音 → 再 HyperFrames 渲染视频
# 优势：声音可控、可复刻品牌声音
```

## 性能基准

| 硬件 | 模型 | 速度 | 内存 |
|:--|:--|:--|:--|
| CPU (i7-12700) | 0.5B | ~8x 实时 | ~4GB |
| RTX 3060 12GB | 0.5B | ~实时 | ~4GB VRAM |
| RTX 4090 24GB | 0.5B | ~2x 实时 | ~3GB VRAM |
| RTX 4090 24GB | 1.5B | ~实时 | ~8GB VRAM |

> 数据来源：insiderllm.com、官方文档、社区实测

## 常见坑点

### Pitfall 1: git clone 无 --recursive
```bash
# ❌ 错误
git clone https://github.com/FunAudioLLM/CosyVoice.git

# ✅ 正确（含 Matcha-TTS 子模块）
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
```

### Pitfall 2: PyTorch 版本不匹配
CosyVoice 3.0 需要 PyTorch ≥ 2.0。如果 GPU 推理失败：
```bash
# CPU 回退
model = CosyVoice3('pretrained_models/Fun-CosyVoice3-0.5B', load_jit=False, fp16=False)
```

### Pitfall 3: 中文前端 ttsfrd 安装失败
WSL 下可能缺 sox：
```bash
sudo apt-get install sox libsox-dev
```
如果 whl 文件与 Python 版本不匹配，跳过文本前端（部分数字/符号可能不规范但可接受）。

### Pitfall 4: 模型下载慢
- 海外：HuggingFace + `mirror=hf-mirror.com`
- 国内：ModelScope（阿里镜像，速度快 10x）

### Pitfall 5: 内存不足
0.5B 模型需要 ~4GB RAM。WSL 2 默认 8GB 内存够用，但必须确保没有其他大进程占用。

### Pitfall 6: KDO 环境 venv 错位
用 `python3 -m pip install` 而非 `pip install`（本机 `pip` → Python 3.10，`python3` → 3.11）。

## 验证清单

- [ ] `python example.py` 无报错
- [ ] 生成的中文语音自然可懂
- [ ] 零样本声音克隆相似度 ≥ 78%
- [ ] 流式输出延迟 ≤ 200ms
- [ ] WebUI 可正常访问

## 参考资料

- GitHub: https://github.com/FunAudioLLM/CosyVoice
- HuggingFace: https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512
- 论文: https://arxiv.org/abs/2505.17589
- Demo: https://funaudiollm.github.io/cosyvoice3/
