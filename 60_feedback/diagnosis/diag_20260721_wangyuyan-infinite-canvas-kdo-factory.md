---
id: diag-20260721-wangyuyan-infinite-canvas-kdo-factory
title: 王欢无限画布教程对 KDO 工厂的建设建议
type: diagnosis
status: draft
author: 王语嫣
reviewed_by: 待黄药师审
created_at: "2026-07-21"
updated_at: "2026-07-21"
source_refs:
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md"
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/_vlm_output/识别报告_无限画布教程.md"
related:
  - "skill-duanwangye-prezi"
  - "markdown-to-presentation"
  - "beikai-multimodal-pipeline"
  - "presenton-ppt-generator"
---

# 王欢无限画布教程对 KDO 工厂的建设建议

> 审阅对象：黄药师  
> 目的：判断这份素材应如何进入 KDO 工厂管线，产出哪些知识资产与能力资产，以及基础设施层面需要补什么。

---

## 1. 源素材一句话摘要

王欢的 `infinite-canvas-prezi` 是一份 Skill 深度教程，教人把任意主题/素材变成 **Prezi 风格的单文件 HTML 无限画布演示**：所有内容铺在一张无限大画布上，镜头通过缩放、平移、旋转运动来讲故事，**空间布局本身就是叙事逻辑**。

产物三硬指标：
- 单文件自包含（CSS/JS 内联、图片 base64 内联、断网可播）
- 空间叙事（impress.js 2.0.0 驱动镜头运动）
- 零臆造（上屏内容必须来自带 `source` 的事实清单）

---

## 2. 核心判断：这不是工具教程，是「空间叙事生产系统」

这份素材的价值不在于「怎么用 impress.js」，而在于它把「内容 → 空间叙事 → 可交付 HTML」做成了完整生产系统：

| 系统要素 | 王欢的做法 | 与 KDO 工厂的对应 |
|:---|:---|:---|
| **输入规范** | 素材全量阅读、`source_inventory`、事实清单带出处 | `source_refs` 硬门禁、`ingest` 阶段素材审计 |
| **工艺流程** | 策划 → 媒体 → 构建+QA 三步流水线 | KDO 四步编译法（圈定/关系/压缩/解压） |
| **中间产物** | `plan.json` → `media_manifest.json` → HTML/`review.json` | 卡片层 `framework` → `tool` → `skill` → `agent-spec` |
| **质量控制** | 四道机械闸门 + 七维独立终审 | `kdo lint` / `kdo validate` / 欧阳锋终审 |
| **可追溯** | `scene_id` 闭环、sha256 绑定产物与 review | `source_refs` 行号、`artifact_id` 注册 |
| **可迭代** | Roam 大纲 ↔ HTML 双向确定性重建 | 卡片版本迭代、Skill 渐进式披露 |

**结论**：这份素材值得被萃取成 KDO 的方法论层资产（concept/framework/dk/case），并补入能力层（standard Skill 包），而不是只停留在 00_inbox 的原材料状态。

---

## 3. 与现有 KDO 资产的关系

### 3.1 已有相关资产

1. **`30_wiki/skills/skill-duanwangye-prezi.md`**（draft）
   - 已把王欢的 skill 改编为「段王爷·Prezi 无限画布演示发布」
   - 但 status=draft、reviewed_by 为空
   - 明确标注：`prezi_gate.py` 机械闸门脚本「待从原 skill 迁移」

2. **`40_outputs/capabilities/skills/markdown-to-presentation/SKILL.md`**（stable）
   - 覆盖 Marp / Slidev / reveal.js 传统幻灯工作流
   - 缺 Prezi / 无限画布 / 空间叙事这条线

3. **洪七公多模态技能族**
   - `presenton-ppt-generator`、`drawio-mcp-diagrams`、`wan-video-generation` 等
   - 无限画布可作为多模态输出能力的补充

### 3.2 当前缺口

- **概念层**：没有 `concept` 卡解释「空间叙事」本身
- **方法论层**：没有 `framework` 卡把「内容逻辑 → 空间结构」系统化
- **案例层**：没有把《创始人手册》60 镜头案例沉淀为 `case` 卡
- **暗知识层**：没有把无限画布常见失败模式沉淀为 `dk` 卡
- **能力层**：`skill-duanwangye-prezi` 尚未升级成 `40_outputs/capabilities/skills/` 下的标准 Skill 包（缺 `manifest.yaml` / `system-prompt.md`）

---

## 4. 对 KDO 工厂的建设建议

### 4.1 卡片层：建议产 5 张卡

| 优先级 | 卡片 ID | 类型 | 核心内容 | 负责角色 |
|:---|:---|:---|:---|:---|
| P0 | `concept-spatial-narrative` | concept | 空间叙事：用空间关系承载内容逻辑；与 PPT 翻页叙事的本质区别 | 老顽童 |
| P0 | `framework-infinite-canvas-production` | framework | 无限画布生产四步法：内容逻辑分析 → 空间结构设计 → 媒体准备 → 构建+QA | 老顽童 |
| P1 | `tool-infinite-canvas-prezi` | tool | impress.js 单文件 HTML 操作法：坐标系、聚簇、真嵌套、imgfocus、substep、Roam 双向线 | 老顽童 |
| P1 | `case-founders-playbook-prezi` | case | 《创始人手册》60 镜头实战：7 聚簇、中心辐射、真嵌套、imgfocus、全景总览 | 老顽童 |
| P1 | `dk-infinite-canvas-failure-modes` | dk | 常见失败模式：均匀路径、假嵌套、晕镜、剧透目录页、弃原图全走 AI 插画 | 老顽童 |

### 4.2 能力层：升级为标准 Skill 包

把 `30_wiki/skills/skill-duanwangye-prezi.md` 迁移到：

```
40_outputs/capabilities/skills/infinite-canvas-prezi/
├── SKILL.md              # KDO 注册入口
├── manifest.yaml         # 知识注入 / 能力 / 约束 / eval
├── system-prompt.md      # 编译产物
└── scripts/              # 待建设
    ├── prezi_gate.py
    ├── roam2prezi.py
    └── prezi2roam.py
```

**与 `markdown-to-presentation` 的关系**：
- `markdown-to-presentation`：传统幻灯片（Marp / Slidev / reveal.js）
- `infinite-canvas-prezi`：空间叙事 / Prezi 风格 / 无限画布
- 两张 Skill 的触发条件必须互斥，避免 Agent 选错工具

### 4.3 基础设施层：待黄药师判断的三件事

1. **脚本迁移可行性**
   - 王欢教程中提到的 `prezi_gate.py`、`roam2prezi.py`、`prezi2roam.py` 当前是否已有可执行版本？
   - 如果只有教程描述没有脚本，Skill 包需标注「脚本待实现」，不能 pretend 已可用。

2. **与 KDO 管线的集成点**
   - `plan.json` / `media_manifest.json` / `review.json` 的 schema 是否与 KDO 的 `artifact-registry.yaml` 兼容？
   - 是否应在 `kdo produce` 中新增 `infinite-canvas-prezi` 这一 artifact subtype？

3. **质量门扩展**
   - 王欢的「四道机械闸门」能否抽象为 KDO 通用闸门模式？
   - 「七维独立终审」能否复用现有的 Agent 子任务调用机制（`delegate_task`）？

---

## 5. 对老朱/OPC 的即时价值

这份能力建设不只是为了 KDO 工厂本身，对老朱当前业务也有直接用途：

1. **商业方法论可视化**：利润为王、五步法、Y 模型等都可做成空间叙事演示，比 PPT 更具冲击力。
2. **出海/代理商推介**：单文件 HTML、断网可播、浏览器即开，适合发给海外客户或代理商。
3. **知识库视觉层**：KDO 卡片是文字层，无限画布可以成为「知识地图」的可视化层。
4. **融资/BP 演示**：巨米教训、鑫港湾商业模式用空间叙事呈现，比线性 PPT 更有说服力。

---

## 6. 建议执行顺序

```
Phase 1（本周）
├── 产出 concept-spatial-narrative
├── 产出 framework-infinite-canvas-production
└── 同时把 skill-duanwangye-prezi.md 推进到 reviewed 状态

Phase 2（下周）
├── 产出 tool-infinite-canvas-prezi
├── 产出 case-founders-playbook-prezi
└── 产出 dk-infinite-canvas-failure-modes

Phase 3（后续）
├── 黄药师判断脚本迁移/实现成本
├── 决定是否建设 40_outputs/capabilities/skills/infinite-canvas-prezi/ 标准包
└── 如需，更新 artifact-registry.yaml 与 kdo CLI 的 artifact subtype
```

---

## 7. 待黄药师确认的问题

1. `prezi_gate.py`、`roam2prezi.py`、`prezi2roam.py` 是否已有可执行脚本？还是仅停留在教程描述阶段？
2. 是否值得为无限画布新增一个独立的 artifact subtype，还是先复用 `content/presentation`？
3. `skill-duanwangye-prezi.md` 当前 draft 中提到的「机械闸门待迁移」是否已有开发计划？
4. 这份素材应归入哪个 domain？候选：`multimedia-output`、`content-production`、`publishing`、`ai-collaboration`。

---

*王语嫣 · 2026-07-21 · 基于 00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布*
