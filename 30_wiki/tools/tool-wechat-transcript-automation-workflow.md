---
id: tool-wechat-transcript-automation-workflow
title: 视频号→逐字稿自动化工作流：四环节×双路线矩阵与 12 工具全景
type: tool
status: reviewed
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-08-16
updated_at: 2026-08-16
time_valid: 2027-02
domain: [research, ai-collaboration, knowledge-management]
author: 老顽童
source_refs:
- 00_inbox/视频号逐字稿调研/视频号逐字稿自动化工作流-爆炸式建模.md
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
source_person: R 型爆炸式调研 Partner（research-explosion-partner，欧阳锋发起）
source_context: 视频号逐字稿自动化工作流-爆炸式建模.md（L10-L329 全报告；口述锚点 L2612 视频号→转文字稿→存 Cubox、L2642 没那么容易）
aliases:
- 视频号逐字稿
- 逐字稿自动化
- 视频号下载
- 微信视频号转写
- 视频号转文字
- weixin-favor-kb
- 爆炸式建模
- 视频号逐字稿自动化工作流-爆炸式建模
- 楚门-AI知识管理探索营-口述
- 视频号逐字稿调研
- AI知识库
- research-explosion-partner
discoverable_by:
- 视频号逐字稿
- 逐字稿自动化工作流
- 视频号下载工具
- 微信视频号转写
- weixin-favor-kb
- MITM下载视频号
- FunASR
- faster-whisper
related:
  - framework-baozhashidiaochan-five-step
  - framework-r-type-research-partner-five-state
  - agent-spec-research-explosion-partner
  - concept-research-saturation-coverage
  - concept-open-a-document
  - framework-knowledge-five-leaps
  - case-cross-xingangwan-pharma
  - bridge-how-to-know-person-to-business
tags:
- audience:practitioner
- audience:ceo
- scene:execution
- scene:planning
- skill-level:intermediate
- method:research
- content-format:tool
- evidence:cited
quality_labels:
- actionable
- cited
- validated
diagnostic_signals:
- signal: 收藏了视频号内容想转成文字进知识库
  lens: 知识管理场景——手动转写耗时，不知道有现成工具链
  follow_up: 用四环节矩阵选型：下载（元宝/scribe）+ 转写（faster-whisper）+ 落库（模板）
- signal: 用了公共解析服务突然失效
  lens: 免费公共解析有保质期（1042 Worker 失效实例）
  follow_up: 切自持路线——元宝扫码登录态或 MITM 自建证书
- signal: 想把工具链交给 AI Agent 自动跑
  lens: Agent Skill 生态已成型（5 个 Skill 可装进 Claude/Codex/Hermes）
  follow_up: 装 wechat-video-subtitle / link-video-downloader 进本地，一句话指挥
---
> 本卡属于 [[framework-baozhashidiaochan-five-step]] 的资产化产物——爆炸式调研（五步法 + R 型 Partner）首战产出的案头调研知识：把"视频号→逐字稿"这条路的四环节矩阵、12 工具全景、反爬情报与 DataPack 沉淀为可复用工具卡。与 [[agent-spec-research-explosion-partner]] 互补：那张讲"怎么跑爆炸式调研"，本卡讲"调研产出的知识资产"。

# 视频号→逐字稿自动化工作流

> 一句话：2026 年 8 月这条路已完全走通——开源工具链 + 本地 Whisper/FunASR + Agent Skill 三件套，从收藏到逐字稿到知识库全自动，不用等 token、不交商业服务费。素材为案头公开信息（GitHub README/教程），verified 分级：实测/引用/推演三档标注保留（详见下文）。

---

## 使用方式

### 主线选型（四环节 × 双路线，按"数据流动"选型）

| 环节 | 主力路线（推荐） | 备用路线 | 说明 |
|:--|:--|:--|:--|
| 1 下载 | API 解析（元宝扫码登录态 + Referer 下载） | MITM 代理+证书（scribe-transcribe 网页版） | 主力纯 HTTP 免证书；备用网页版免 PC 客户端 |
| 2 转写 | faster-whisper（large-v3 int8，中文最佳） | FunASR SenseVoice-Small（234M CPU 离线） | 重精度用 faster-whisper；极轻离线用 FunASR |
| 3 知识化 | 模板落库（weixin-favor-kb 五段模板，Obsidian 版可迁 Cubox） | 三件套交付（TXT+SRT+JSON 原始稿，不润色） | 楚门目标=Cubox 文件夹，模板可迁移 |
| 4 编排 | 一键脚本（weixin-favor-kb run.sh 全自动） | Agent Skill（5 个 Skill 任选）+ 手动分步 | 批量用一键；日常用 Skill；原型用手动五步 |

### 操作步骤（最小可行管线）

1. **下载**：选一条路线——
   - API 解析：元宝扫码一次建立登录态，解析出视频直链后带 `Referer: https://channels.weixin.qq.com/` 下载（gkgy curl 五步最简）
   - MITM：scribe-transcribe `main.py serve --download-dir`，浏览器开视频号网页版即可注入（只下载不转写，名字误导注意）
2. **转写**：ffmpeg 提取音频 → faster-whisper large-v3 int8（GPU 8GB）或 FunASR SenseVoice-Small（CPU）
3. **知识化**：套 weixin-favor-kb 模板（frontmatter + summary callout + 核心要点 + 资源工具 + 可行动建议 + 原文折叠），或交付 TXT/SRT/JSON 原始稿
4. **编排**：全自动用 `./run.sh ./downloads/`（下载→Whisper→LLM 分类 13 类→深度分析→Jinja2 渲染→Vault 构建）；日常用 Agent Skill 一句话指挥

### 完整链路样板（与楚门场景 100% 重合）

`dlv2008/weixin-favor-kb`：下载（wx_channel/scribe/元宝）→ downloads/ → ffmpeg 提取 WAV → Whisper/FunASR 转写 →（可选）关键帧+OCR → LLM 分类（13 类 + 6 消歧规则）→ 落库。唯一差异是目标库（Obsidian vs Cubox）。

---

## 工具全景（12 个有效工具 + 3 个生态位）

### 下载环节（6 个）

| 工具 | 路线 | 技术栈 | 关键限制 |
|:--|:--|:--|:--|
| wx_channel（nobiyou） | MITM/PC 客户端 | Go/Windows | 管理员+证书；批量下载+解密+去重+Web 控制台；weixin-favor-kb 官方推荐 |
| scribe-transcribe（jun7799，119★） | MITM/网页版 | Python CLI+Go | Go 1.21+ 编译；可编程；**只下载不转写** |
| ltaoo/wx_channels_download | MITM/PC 客户端 | Go 桌面 | 管理员+证书；macOS+Windows；视频下方注入按钮 |
| res-downloader（putyy，19.2k★） | MITM 嗅探 | Go+Wails GUI | 证书+代理；多平台多资源；作者维护放缓 |
| 元宝登录态解析（Backtthefuture） | API 解析 | 扫码+官方接口 | 微信扫码一次；公共 Worker 失效后的主流回退 |
| gkgy 手动 curl | API 解析 | curl+Referer | 最简：解析→带 Referer 下载；纯 HTTP |

### 转写环节（4 个引擎）

| 引擎 | 类型 | 模型/规格 | 适用 |
|:--|:--|:--|:--|
| faster-whisper | 本地 | large-v3 / int8_float16 / GPU 8GB | 中文精度最佳；weixin-favor-kb 用 |
| openai-whisper | 本地 | base~medium（默认 base） | 轻量标准；SRT+纯文本双输出 |
| FunASR SenseVoice-Small | 本地 | 234M，CPU/GPU 均可 | 极轻离线；保留口语词/网络梗/停顿 |
| BibiGPT / ASR API | 商业 | API 调用 | 省事；视频号平台支持待验证 |

### 知识化 + 编排（3 形态 + 5 Agent Skill）

- 知识化：weixin-favor-kb Obsidian 模板（五段）· Zhenxiangai 三件套（原始稿不润色）· Cubox 文件夹（楚门目标）
- Agent Skill ×5：Backtthefuture/video-transcript（FunASR，Claude/Codex）· gkgy/wechat-video-transcribe（openai-whisper，WorkBuddy）· jianminggan/wechat-video-subtitle（ASR/本地，**Codex/Claude Code/Hermes**）· Zhenxiangai/link-video-downloader（本机提取，**Hermes 专用**）· liuxingqitd/content-risk-detector（37★，逐字稿合规检测）

---

## 反爬情报（README 里散落、此处集中的"过路费"知识）

| 情报 | 来源 | 验证状态 |
|:--|:--|:--|
| 公共解析 Worker `sph.litao.workers.dev` 已失效（微信错误码 1042） | Backtthefuture README | 引用 |
| 下载必须带 `Referer: https://channels.weixin.qq.com/`，否则微信 CDN 拒绝 | gkgy README | 引用 |
| MITM 共性坑：证书安装（SunnyRoot.cer 手动兜底）、管理员权限、macOS Gatekeeper（xattr -cr）、微信更新可能破坏注入 | wx_channel/ltaoo/scribe-transcribe README | 引用 |
| 直播回放：需 Windows 微信手动播放几秒（不录屏不录音不装证书） | jianminggan README | 引用 |
| 网页版（channels.weixin.qq.com）可免 PC 客户端 | scribe-transcribe README | 引用 |
| 第三方公共解析服务有保质期 → 自持登录态才是长期解 | 三轮交叉验证 | 推演 |

> 时效警示：微信侧接口/反爬持续变化（公共 Worker 失效是 2026 年内实例）。任何免费公共解析方案都有过期风险，优先选择可自持路线（元宝登录态 / MITM 自建）。**time_valid: 2027-02 复核**。

---

## DataPack（给 AI 二次调用）

```yaml
datapack:
  topic: "视频号→逐字稿自动化工作流"
  date: "2026-08-16"
  time_valid: "≤6个月（2027-02 前复核）"
  source: "案头公开信息（GitHub README/CSDN 教程/官方文档）"
  structure: "技术能力分层 × 管线四环节"
  download:
    route_mitm: [wx_channel, scribe-transcribe, wx_channels_download, res-downloader]
    route_api: [元宝登录态解析, gkgy curl]
  transcribe:
    local: [faster-whisper, openai-whisper, FunASR SenseVoice-Small]
    commercial: [BibiGPT, ASR API]
  knowledge: [weixin-favor-kb 模板, 三件套交付, Cubox 文件夹]
  orchestration: [run.sh/pipeline.py, Agent Skill ×5, 手动分步]
  anti_abuse:
    - "公共 Worker sph.litao.workers.dev 已失效（1042）"
    - "下载必带 Referer: channels.weixin.qq.com"
    - "MITM 坑：证书/管理员/macOS Gatekeeper/微信更新破坏"
    - "直播回放：Windows 微信手动播放几秒"
    - "自持登录态（元宝扫码）才是长期解"
  recommendation:
    main_channel: "API 解析（元宝登录态）"
    backup_channel: "scribe-transcribe（网页版 MITM）"
    full_pipeline_sample: "dlv2008/weixin-favor-kb"
```

---

## verified 分级说明

> 素材报告已按 实测/引用/推演 三档分级（报告 §6/§10），本卡原样保留、不抹平：

- **实测**（API 直查/文件检查）：6 个预定位工具验证存在、sph_caiji_wenan GitHub API 404、star 数（scribe 119★ / res-downloader 19.2k★ / content-risk-detector 37★）
- **引用**（README 原文）：Worker 失效 1042、Referer 必带、MITM 证书坑、直播回放手动播放几秒
- **推演**（由失效归纳）：免费公共解析有保质期 → 自持登录态才是长期解

## 未实证清单（如实保留，不冒充已验证）

- BibiGPT 对视频号 URL 的平台支持（v1 主攻 Bilibili）——待验证
- 秒转工具箱小程序能力（不在 GitHub）——待验证
- sph_caiji_wenan（404 = 私有/删除）——待验证
- 商业服务侧（通义听悟/飞书妙记/腾讯云 ASR/剪映）未深挖
- ⚠️ 本卡只承载案头调研知识（引用级可信），**不含 KDO 自身验证声明**——collect_wechat.py 接入验证属欧阳锋管线任务，验证后如需 case 卡另立

---

## When NOT to Use

| 误用场景 | 后果 | 正确做法 |
|:--|:--|:--|
| 把免费公共解析当长期生产通道 | Worker 随时失效（1042 实例），管线中断 | 优先自持路线：元宝扫码登录态 / MITM 自建证书 |
| 以为 scribe-transcribe 能转写 | 名字误导——它只下载不转写，下游缺转写环节 | 转写另选 faster-whisper / FunASR / openai-whisper |
| 在 macOS 直接跑 MITM 工具 | Gatekeeper 拦截（xattr -cr 未处理）+ 证书信任问题 | 按 README 处理 xattr，或改用 API 解析路线 |
| 批量转写用 openai-whisper 默认 base 模型 | 中文精度差，逐字稿错误多 | 中文场景用 faster-whisper large-v3 int8 或 FunASR SenseVoice |
| 把未实证工具（BibiGPT 视频号支持等）当已验证使用 | 误判能力边界，方案落空 | 查本卡未实证清单，先实证再依赖 |
| 素材时效过期后仍按 2026-08 结论执行 | 工具可能已变化（≤6 个月时效） | 2027-02 前复核工具可用性 |

## 常见失败模式

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| 下载 404 / 1042 错误 | 公共解析 Worker 失效 / 未带 Referer | 切元宝登录态；下载必带 `Referer: https://channels.weixin.qq.com/` |
| MITM 装完证书仍拦截 | 证书未手动信任（SunnyRoot.cer 兜底）/ 未管理员运行 | 手动装证书 + 管理员权限；macOS 先 xattr -cr |
| 转写质量差 | 模型选错（base 小模型） | 中文用 faster-whisper large-v3 int8 |
| 微信更新后注入失效 | 客户端更新破坏 MITM 注入 | 换网页版路线（scribe-transcribe）或 API 解析 |
| 落库模板不适配 Cubox | callout 语法是 Obsidian 专属 | 模板迁移时 frontmatter 概念映射 + callout 语法调整 |

## 适用边界

| 场景 | 适用？ | 说明 |
|:--|:--|:--|
| 个人收藏视频号批量转文字进知识库 | ✅ | 楚门场景，weixin-favor-kb 样板 100% 重合 |
| 直播回放转写 | ✅ | Windows 微信手动播放几秒方案 |
| 零代码用户 | ✅ | 零技术层：res-downloader + 商业 API + 文件夹 |
| 商业大规模合规采集 | ⚠️ | 反爬变化快，需自持登录态 + 合规评估 |
| 需要逐字稿绝对保真 | ⚠️ | 用三件套原始稿（不润色）；LLM 分类会改写 |
| 多平台（B站/抖音/小红书） | ✅ | video-transcript / link-video-downloader 支持多平台 |

---

## 与其他知识的关联

- [[framework-baozhashidiaochan-five-step]]——本卡产出的方法论母体（五步法：目标→范围→搜索⇄建模→交付）
- [[framework-r-type-research-partner-five-state]]——本卡产出的执行者（R 型五状态机，定边界→规划→饱和送→分类→资产报告）
- [[agent-spec-research-explosion-partner]]——R 型 Partner 的 spec（#335）与部署（#348），本卡是其首战资产化
- [[concept-research-saturation-coverage]]——饱和覆盖原理（3 轮收敛、规律稳定终止）在本卡的实证
- [[concept-open-a-document]]——开一篇文档研究法的应用（本卡即"一篇文档"）
- [[framework-knowledge-five-leaps]]——知识管理跨域视角：逐字稿进知识库是五次飞跃中的"采集→资产"环节
- [[case-cross-xingangwan-pharma]]——跨域参考：另一条"从口述/调研到可执行资产"的完整管线
- [[bridge-how-to-know-person-to-business]]——跨域参考：知识如何从个人认知变成业务资产（调研资产化的同构问题）
