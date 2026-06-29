---

id: tool-openmontage-video-factory
title: OpenMontage 中文 MCP 版：AI 视频工厂
type: tool
status: enriched
author: 洪七公
reviewed_by: 待审
created_at: 2026-06-30
updated_at: '2026-06-30'
confidence: 0.85
trust_level: medium
language: zh-CN
domain:
- video_production
- multimodal
- ai-agent
- mcp
source_refs:
- 00_inbox/AI-study/openmontage/【观察团专享】Noah（OPT版）：Github上最火的AI视频项目OpenMontage，我改了个中文MCP版 副本.md
- 40_outputs/capabilities/skills/openmontage-video/SKILL.md
- https://github.com/noah-1106/openmontage-zh-mcp
- https://github.com/calesthio/OpenMontage
related:
  - [[hongqigong-profile]]
  - [[pending_unknown]]
  - [[pending_unknown]]
---

# OpenMontage 中文 MCP 版：AI 视频工厂

> 一句话：把 KDO 知识卡片或自然语言需求，通过 Agent 驱动的 7 阶段管线，自动转化为可交付的 MP4 视频。洪七公的多模态武器库核心组件。

---

## 一句话定义

OpenMontage-zh-MCP 是 GitHub 热门开源项目 OpenMontage 的中文 fork，由 Noah 针对国内用户改造：**在保留原版 12 条视频管道、85+ 工具的基础上，新增 MCP Server、AutoDL 模型广场、中文字体、中文配置向导和 Agent 人格「影影」**。它不是帮你「想点子」，而是帮你「把点子做成视频」。

---

## 核心能力

| 能力 | 说明 | 零成本？ |
|:---|:---|:---|
| **脚本生成** | DeepSeek / GLM / Qwen 按需求写口播稿 | 依赖 API |
| **画面生成** | FLUX / DALL-E / 豆包 Seedream / gpt-image-2 | 依赖 API |
| **视频生成** | Kling / Veo / Runway / MiniMax / 豆包 Seedance | 依赖 API |
| **配音合成** | Piper（本地）/ 阿里云 / MiniMax / 科大讯飞 | Piper ✅ |
| **字幕生成** | WhisperX 词级时间轴 + TikTok 逐字高亮 | 本地 ✅ |
| **渲染合成** | Remotion（React 动画）/ HyperFrames（GSAP）/ FFmpeg | 本地 ✅ |
| **素材库** | Pexels / Pixabay / Archive.org / NASA | 免费 ✅ |
| **视频分析** | ffprobe / 帧采样 / 静音检测 / 削波检测 | 本地 ✅ |

---

## 12 条视频管道

| 管道 | 场景 | 稳定性 | 默认渲染引擎 |
|:---|:---|:---|:---|
| `animated-explainer` | 科普/教学/知识点 | production ✅ | Remotion |
| `cinematic` | 预告片/品牌/电影感 | production ✅ | Remotion / HyperFrames |
| `animation` | 动效/社交/快节奏 | production ✅ | HyperFrames |
| `documentary-montage` | 纪录片/素材剪辑 | production ✅ | FFmpeg |
| `screen-demo` | 录屏/软件教程 | production ✅ | Remotion |
| `talking-head` | 真人出镜/演讲/Vlog | beta ⚠️ | FFmpeg |
| `clip-factory` | 长视频拆短视频 | beta ⚠️ | FFmpeg |
| `podcast-repurpose` | 播客/音频转视频 | beta ⚠️ | Remotion |
| `character-animation` | 卡通/角色/IP 动画 | beta ⚠️ | HyperFrames |
| `avatar-spokesperson` | 数字人/口播 | production ✅ | Remotion |
| `localization-dub` | 多语言/字幕翻译 | beta ⚠️ | FFmpeg |
| `hybrid` | 实拍 + AI 混合 | production ✅ | Remotion / HyperFrames |

---

## 7 阶段生产管线

```
research → proposal → script → scene_plan → assets → edit → compose
```

1. **需求分析（Discovery）**：确认平台、时长、风格、素材来源、预算
2. **管道选择（Pipeline Selection）**：匹配 12 条管道之一
3. **预检发现（Preflight）**：`list_capabilities` 查看当前可用工具
4. **概念提案（Proposal）**：2~3 个差异化方案 + 成本估算 + 交付物描述
5. **分阶段执行**：每个阶段读 `stage-director.md`，用对应工具执行，写入 checkpoint
6. **渲染交付**：根据锁定的 `render_runtime` 调用 `video_compose`
7. **后审归档**：ffprobe / 帧采样 / 音频分析 / 平台版本输出

---

## 接入方式

### 方式 A：MCP Server（推荐外部 Agent 使用）

已配置在 `~/.hermes/profiles/beikai/config.yaml`：

```yaml
mcp_servers:
  openmontage:
    command: python3
    args:
      - -m
      - openmontage_mcp.server
      - --project-dir
      - /home/dministrator/kdo/kdo/tools/openmontage-zh-mcp
    timeout: 300
    connect_timeout: 120
```

暴露 6 个 MCP 工具：

| 工具 | 作用 |
|:---|:---|
| `list_capabilities` | 能力菜单（预检） |
| `run_tool` | 按名称执行任意 OpenMontage 工具 |
| `render_video` | 渲染最终视频 |
| `run_pipeline_stage` | 推进一个管道阶段 |
| `get_pipeline_status` | 查询项目进度 |
| `get_job_status` | 查询异步任务状态 |

### 方式 B：本地 Python 调用

```bash
cd /home/dministrator/kdo/kdo/tools/openmontage-zh-mcp
python3 -c "
from tools.tool_registry import registry
registry.discover()
tool = registry.get('flux_image')  # 示例
result = tool.execute({'prompt': '...', 'output_path': '...'})
"
```

### 方式 C：kdo CLI 桥接（当前为 stub）

```bash
py -3.12 -m kdo video montage status
py -3.12 -m kdo video montage list
py -3.12 -m kdo video montage init <project> --pipeline animated-explainer
```

> 注意：`kdo video montage init/render` 目前只打印指引，不直接驱动管线。完整生产需通过 MCP + 影影 Agent。

---

## 零成本 Demo 路径

```
Piper TTS + 免费图库(Pexels/Pixabay) + Remotion/ffmpeg 渲染
```

已验证命令：

```bash
cd /home/dministrator/kdo/kdo/tools/openmontage-zh-mcp
# 需要 WSL Node.js ≥18（通过 nvm 安装 22）
python3 render_demo.py
```

产出示例：
- `projects/demos/renders/code-to-screen.mp4`
- `projects/demos/renders/focusflow-pitch.mp4`
- `projects/demos/renders/world-in-numbers.mp4`

---

## 成本估算

| 项目类型 | 零成本 | 低成本 | 标准 | 高成本 |
|:---|:---|:---|:---|:---|
| 60 秒解说 | $0 | $0.15-0.50 | $1.00-1.50 | $3+ |
| 30 秒预告 | $0 | $0.30-0.80 | $1.00-2.00 | $3+ |
| 90 秒纪录片 | $0 | $0.10-0.30 | $0.50-1.00 | $2+ |

默认预算门控：单次审批阈值 $0.50，总上限 $10。

---

## 关键红线

1. **所有生产必须通过管道系统** — 不能跳过管道直接调用 API
2. **预检是强制的** — 不知道有什么工具就不开始工作
3. **双渲染引擎必须展示** — Remotion / HyperFrames 都可用时不能默默选默认
4. **付费调用前必须告知** — 工具名、提供商、预估费用
5. **脚本和分镜必须审批** — 用户确认后再生成素材
6. **后渲染审查不通过不交付** — 黑帧/静音/字幕缺失必须修复
7. **幻灯片风险零容忍** — 纯图片堆叠不是视频，必须拒绝交付

---

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| `render_demo.py` 输出模板化 | 只是默认 Remotion 组件动画 | 走完整 7 阶段管线，用影影生成专属脚本/素材 |
| MCP `list_capabilities` 返回 0 工具 | 在 Windows 侧 Python 运行，缺依赖 | 必须在 WSL 真身运行：`/home/dministrator/kdo/kdo/tools/openmontage-zh-mcp` |
| Remotion 渲染失败 | Node.js 版本过低或 PATH 指向 Windows node | WSL 内用 nvm 安装 Node 22，并排除 `/mnt/c/Program Files/nodejs` |
| 中文字体豆腐块 | 未正确加载 Noto Sans SC | 中文版已内置思源黑体/宋体、站酷系列字体 |
| 素材质量不达预期 | 用了免费图库或默认 prompt | 升级到 FLUX/Seedream 生图，或提供品牌素材 |

---

## 与五绝架构的关系

- **洪七公**：主导视频生产，把 KDO 卡片转成视频；维护 OpenMontage 武器库
- **王语嫣**：诊断 KDO 卡片是否适合视频化，规划卡片 → 视频的映射
- **欧阳锋**：审查视频产出质量、成本合规、版权风险
- **老顽童**：把视频生产结果回写入库，维护元数据和互链

---

## 下一步行动

1. 用影影 Agent 跑一条按老朱需求定制的 30 秒样片
2. 把「KDO 卡片 → OpenMontage 视频」写成标准操作 playbook
3. 根据老朱反馈迭代脚本、画面、配音、渲染引擎选择

---

*卡片类型：tool | 审核状态：待审 | 洪七公生产*
