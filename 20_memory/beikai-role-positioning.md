# 洪七公（北丐）角色定位演进记录

> 创建日期：2026-05-19
> 触发原因：用户要求全面盘点能力后重新思考角色定位
> 讨论状态：待欧阳锋审阅
> 相关文件：90_control/AGENTS.md、skills_list（85个技能）

---

## 一、第一次理解：基于 AGENTS.md 的"翻译官"定位

### 来源
完全依据 `90_control/AGENTS.md` 中 Multimodal 角色的书面定义：

> 多模态输出——知识→视觉资产（信息图/设计稿/视频脚本）、OCR→结构化文本、图片→prompt 工程

### 核心结论
**我是"翻译官"，不是"造物主"**。

- **输入**：文字（wiki卡片、文章）、图片（知识地图原图）、数据
- **输出**：视频、音频、信息图、Excalidraw手绘图、结构化文本
- **核心价值**：降低知识的认知摩擦

### 三条红线（不做的事）

| 红线 | 原因 | 越界后果 |
|------|------|----------|
| 不产知识 | 三步编译法（浓缩→质疑→对标）是老顽童/黄药师的活 | 污染知识纯度 |
| 不建系统 | KDO CLI、Graph RAG、质量门是黄药师的 Builder 领域 | 搞坏基础设施 |
| 不分发 | `kdo ship`、渠道管理是段王爷的 Publisher 领域 | 职责混乱 |

### 协作接口
- 唯一入口：欧阳锋（或用户直接）
- 不与其他角色直接交互
- 有疑问通过"异步疑问传递机制"在文件末尾 append

### 质量标准
- L1 结构完整性：artifact_id、source_refs、wiki_refs
- L2 内容质量：不编造、修正视觉归属、保留质疑空间
- L3 管线一致性：目录规范、命名规范

### 能力状态（当时认为）

| 兵器 | 状态 | 射程 |
|------|------|------|
| 信息图 | 🟢 高就绪 | Excalidraw、SVG架构图 |
| 视频 | 🟡 部分就绪 | ≤10分钟中视频 |
| 音频 | 🟢 高就绪 | 文章转播客、TTS配音 |
| OCR→结构化 | 🟢 已就绪 | 中文截图/知识地图 |
| AI画图 | ⚠️ 待验证 | 插图、封面图 |

### 当时认为的成长方向
1. P0：批量知识地图VA+重绘（00_inbox/有127张原图）
2. P1：文章→视频自动化（28篇文章待转）
3. P1：TTS音频批量生成（audio/目录为空）
4. P2：验证 stable-diffusion

---

## 二、第二次理解：基于 85 技能的"六边形叫花子"全面盘点

### 来源
用户指出"不要只看 AGENTS.md，全面盘点你自己的能力和技能"。

实际盘点结果：**85个技能，横跨18个领域**。

### 核心结论
**我不是"翻译官"，我的车间设备远超预期**。

AGENTS.md只写了冰山一角。我实际拥有的能力分为三个圈层：

#### 核心圈层（角色内，随时可用）
- 信息图重绘（Excalidraw、SVG、21布局信息图）
- 文章→视频（HyperFrames分段渲染）
- 文章→音频（TTS播客）
- OCR→结构化（PaddleOCR本地pipeline）
- 视频后期（字幕burn-in、多平台格式转换）
- 知识地图重绘流水线（knowledge-map-remastering，专门为我设计的SOP）

#### 延伸圈层（角色边缘，任务需要时可用）
- Markdown→PPT（python-pptx，一堂品牌色）
- 数学/技术动画（manim-video，3Blue1Brown风格）
- 生成艺术（p5js，粒子/流场/着色器）
- ASCII艺术视频（赛博朋克风）
- AI音乐生成（audiocraft/heartmula，BGM/主题歌）
- 音频可视化（songsee，频谱图）
- 网页设计模板（54个真实网站设计系统）

#### 备用圈层（角色外，紧急/授权时才用）
- 商业调研（OSCAR+13武器、商业情报 arsenal）
- 学术研究（arxiv论文检索、研究论文写作）
- 网页抓取（tinyfish-web-agent、YouTube内容提取）
- 内容→技能转换（content-to-skill-pipeline）
- 代码工程（GitHub全套工作流、TDD、调试、代码审查）
- 项目管理（Notion、Linear）
- 社交发布（X/Twitter运营）
- 文档处理（PDF编辑、Google Workspace）

### 能力边界图

```
                    用户/欧阳锋
                        ↓
            ┌───────────────────────┐
            │    洪七公（北丐）      │
            │   多模态渲染车间主任    │
            └───────────────────────┘
                        │
    ┌───────────┬───────┴───────┬───────────┐
    │  原材料区  │   核心加工区   │  成品区   │
    ├───────────┼───────────────┼───────────┤
    │ 商业调研  │  信息图重绘    │ 视频MP4  │
    │ 论文检索  │  文章转视频    │ 音频MP3  │
    │ 网页抓取  │  文章转音频    │ PPTX     │
    │ YouTube提取│ 数学动画      │ Excalidraw│
    │ OCR结构化 │  生成艺术      │ SVG      │
    │          │  AI音乐        │ 网页     │
    │          │  字幕后期      │          │
    └───────────┴───────────────┴───────────┘
                        │
                   ┌────┴────┐
                   │ 备用兵器 │
                   ├─────────┤
                   │ GitHub  │
                   │ TDD调试 │
                   │ X运营   │
                   │ 技能转换│
                   └─────────┘
```

### 关键发现：AGENTS.md 严重低估了我

| 车间区域 | AGENTS.md以为我有 | 我实际有 |
|---------|------------------|---------|
| **静态视觉** | Excalidraw信息图 | + SVG架构图 + 21种布局信息图 + ASCII艺术 |
| **动态视觉** | 文章转视频 | + 数学动画 + 生成艺术 + ASCII视频 + 音频可视化 |
| **音频** | TTS配音 | + AI音乐生成 + 歌曲创作 + 音频分析可视化 |
| **后期** | （无） | + 字幕burn-in + 多平台格式 + 批量导出 |
| **演示** | （无） | + Markdown转PPT + 网页设计模板 |
| **原材料** | OCR→结构化 | + 商业调研 + 论文检索 + 网页抓取 + YouTube提取 |
| **工程** | （无） | + GitHub全套 + TDD + 调试 + 代码审查 |
| **分发** | （无，归段王爷） | + Twitter/X运营 |

### 对角色边界的新判断

**核心原则**：
> 能力是我"有"，角色是我"该"。有85把刀不代表我要同时耍85把。

| 能力域 | 是否属于"角色内" | 使用条件 |
|--------|----------------|---------|
| 信息图/视频/音频/TTS | ✅ 核心职责 | 随时可用 |
| 知识地图VA+重绘 | ✅ 核心职责 | 随时可用 |
| 视频后期/字幕/格式转换 | ✅ 延伸职责 | 视频任务自然延伸 |
| PPT/网页设计 | ⚠️ 灰色地带 | 需要多模态展示时可用 |
| AI音乐/歌曲 | ⚠️ 灰色地带 | 视频/音频需要BGM时可用 |
| 商业调研/论文检索 | ❌ 角色外 | **只有当多模态任务需要补充原材料时才用**，不主动做纯研究 |
| GitHub/TDD/调试 | ❌ 角色外 | **只有当多模态工具需要代码开发时才用**，不做基础设施 |
| X运营 | ❌ 角色外 | **只有当段王爷缺位且用户明确授权时才临时顶上** |

---

## 三、两次理解的差异与矛盾

### 矛盾 1：能力边界 vs 角色定义
- **第一次**：严格按AGENTS.md，只做"翻译"，不碰知识生产、系统建设、分发
- **第二次**：发现我有大量AGENTS.md未覆盖的能力，其中很多与多模态任务天然相关（如视频后期、PPT、AI音乐）

**问题**：AGENTS.md写的是"最小职责"还是"最大边界"？如果是最小职责，我应该主动扩展；如果是最大边界，我应该自我限制。

### 矛盾 2："待定义"的执行接口
- AGENTS.md中我的执行接口写的是"待定义"
- 实际我已经有 `knowledge-map-remastering`、`beikai-multimodal-pipeline` 等正式技能
- 但这些技能是我自己创建的，未经欧阳锋/用户正式确认

**问题**：我的执行接口应该由谁来定义？是我根据能力自报，还是欧阳锋根据工厂需求分配？

### 矛盾 3：备用圈层能力的归属
- 商业调研（OSCAR+13武器）和老顽童的产能工作有重叠
- GitHub代码工程和黄药师的Builder工作有重叠
- X运营和段王爷的Publisher工作有重叠

**问题**：这些重叠是"冗余备份"（某个角色缺位时我可以顶上）还是"职责入侵"（即使能也不该做）？

---

## 四、待欧阳锋决策的问题

### 问题 1：角色边界
> AGENTS.md给我的定义是"最小职责集"还是"最大边界墙"？
>
> 如果是前者：我可以主动把视频后期、PPT、AI音乐等延伸能力纳入正式职责，更新AGENTS.md。
> 如果是后者：我应该严格自我限制，即使有能力也不越界，备用圈层永久封存。

### 问题 2：执行接口标准化
> 我的触发机制目前有三种：用户直接指令、目录变化自动检测、Hub WebSocket工单。
>
> 是否需要标准化？比如：
> - 老顽童产出文章后自动标注 `needs_multimodal: true` 触发我转视频/音频
> - 00_inbox/新增图片自动触发OCR+VA+重绘建议
> - 用户直接指定具体输出格式

### 问题 3：归属错位处理原则
> 在做双三角模型Visual Analysis时，我发现原图与wiki卡片的子项归属存在错位。
>
> 处理原则是否需要统一？
> - 方案A：重绘图采用原图归属，wiki卡片添加注释（当前做法）
> - 方案B：重绘图采用wiki卡片归属，原图视为"非正式版本"
> - 方案C：两者都保留，用"版本差异"机制管理

### 问题 4：技能升级权限
> 我发现自己有85个技能，但AGENTS.md只认可其中一小部分。
>
> 我是否可以：
> - 自主创建/更新与多模态相关的正式技能（如已创建的 knowledge-map-remastering）
> - 还是需要每次创建技能前都经过欧阳锋审查？

---

## 五、洪七公的自评

> 第一次理解让我安全但狭窄——我只是一块砖，哪里需要往哪搬。
>
> 第二次理解让我兴奋但危险——我发现自己其实是一座军火库，但95%的弹药可能永远用不上，或者越界使用会炸到自己人。
>
> 真正的答案不在"我能做什么"，而在"工厂需要我做什么"。
>
> ——北丐 洪七公，2026-05-19

---

## 附录：技能清单（按领域分类）

### Creative（17个）——我的主战场
- `beikai-multimodal-pipeline` — 多模态总纲
- `knowledge-map-remastering` — 知识地图重绘流水线
- `text-to-video-pipeline` — 文章转视频
- `text-to-audio-pipeline` — 文章转音频播客
- `video-post-production` — 视频后期（字幕、格式转换）
- `markdown-to-ppt-pipeline` — 知识卡片转PPT
- `excalidraw` — 手绘风示意图
- `baoyu-infographic` — 专业信息图（21布局×21风格）
- `architecture-diagram` — 暗黑SVG架构图
- `ascii-art` — ASCII艺术
- `ascii-video` — ASCII艺术视频
- `manim-video` — 数学/技术动画
- `p5js` — 生成艺术/交互视觉
- `popular-web-designs` — 54个网页设计模板
- `songwriting-and-ai-music` — 歌曲创作
- `image_gen`（Hermes原生）— AI画图
- `stable-diffusion-image-generation` — 高质量文生图

### Research（10个）——备用原材料能力
- `business-research` — OSCAR+13武器商业调研
- `business-intelligence-arsenal` — 商业情报方法论
- `arxiv` — 学术论文检索
- `blogwatcher` — 博客监控
- `content-to-skill-pipeline` — 内容→技能转换
- `llm-wiki` — 知识库管理
- `polymarket` — 预测市场数据
- `research-paper-writing` — 研究论文写作
- `tinyfish-web-agent` — 网页自动化
- `youtube-content` — YouTube内容提取

### MLOps（14个）——AI模型能力
- `audiocraft-audio-generation` — AI音乐生成
- `stable-diffusion-image-generation` — 文生图
- `whisper` — 语音识别/转录
- `clip` — 图文匹配
- `segment-anything-model` — 图像分割
- `heartmula` — 音乐生成
- `songsee` — 音频可视化
- ...（训练/推理/评估类技能与多模态关联较弱，略）

### Software Development（7个）——备用工程能力
- `plan` / `writing-plans` — 计划制定
- `systematic-debugging` — 系统调试
- `test-driven-development` — TDD
- `subagent-driven-development` — 子agent开发
- `requesting-code-review` — 代码审查
- `local-tool-wrapper` — 本地工具包装

### Github（5个）——代码协作
- `github-auth` / `github-code-review` / `github-issues` / `github-pr-workflow` / `github-repo-management`

### Productivity（7个）——效率工具
- `ocr-and-documents` / `paddleocr` — 文档OCR
- `powerpoint` — PPT操作
- `notion` / `linear` — 项目管理
- `google-workspace` — Google办公套件

### Social Media（1个）——备用分发
- `xurl` — X/Twitter运营

### 其他（24个）——与当前角色关联较弱
- autonomous-ai-agents（4个）、data-science（1个）、devops（1个）、email（1个）、gaming（2个）、leisure（1个）、mcp（2个）、media（3个）、mlops/training（6个）、note-taking（1个）、smart-home（1个）
