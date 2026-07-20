---
id: diag-20260721-wangyuyan-infinite-canvas-kdo-factory
title: 王欢无限画布教程对 KDO 工厂的建设建议（#198 终审版）
type: diagnosis
status: complete
author: 王语嫣
reviewed_by: 欧阳锋
review_date: "2026-07-21"
created_at: "2026-07-21"
updated_at: "2026-07-21"
source_refs:
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md"
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/_vlm_output/识别报告_无限画布教程.md"
related:
  - "task_20260721_wangyuyan-infinite-canvas"
  - "case-infinite-canvas-founders-playbook"
  - "skill-duanwangye-prezi"
  - "markdown-to-presentation"
---

# 王欢无限画布教程对 KDO 工厂的建设建议（#198 终审版）

> 审阅对象：黄药师  
> 目的：判断这份素材应如何进入 KDO 工厂管线，产出哪些知识资产与能力资产，以及基础设施层面需要补什么。  
> **注意**：本文件为建议性诊断，最终执行任务单见 `60_feedback/tasks/task_20260721_wangyuyan-infinite-canvas.md`。

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

**结论**：这份素材值得被萃取成 KDO 的方法论层资产（concept/tool/dk/case），并补入能力层（standard Skill 包），而不是只停留在 00_inbox 的原材料状态。

---

## 3. #198 终审裁定（欧阳锋）

| 提议 | 裁定 | 本建议处理 |
|:---|:---|:---|
| 补 `framework` 卡 | ❌ 不采纳 | 流水线与质量机制已在 `tool-presentation-quality-gate-pipeline` 中承载，拆出重复 |
| 4 张→桥接卡 | ❌ 不采纳 | 素材为已完成技能文档，非口述方法论，4 张够用；桥接卡待真实需求出现时再建 |
| 升级 `skill-duanwangye-prezi.md` | ✅ 采纳 | 纳入 Skill 部署层 S4：status draft→reviewed，与卡片层产出建 related 双向链 |
| 脚本可用性标注 | ✅ 采纳 | S1 标注 ⚠️：`prezi_gate.py`/`roam2prezi.py`/`prezi2roam.py` 当前不存在，需迁移或重建 |
| 与 `markdown-to-presentation` 关系 | ✅ 采纳 | markdown-to-presentation 覆盖传统幻灯（Marp/Slidev/reveal.js），本任务补空间叙事支路 |
| 三阶段执行 | ⚠️ 部分 | P0/P1 优先级已在任务单卡片规格中标明，不强制分 Phase |

---

## 4. 建议产出的卡片与能力资产

### 4.1 卡片层：4 张（任务单已锁定）

| 优先级 | 卡片 ID | 类型 | 核心内容 |
|:---|:---|:---|:---|
| P0 | `concept-spatial-narrative-design` | concept | 空间即逻辑：四种空间结构（路径/嵌套/对比/环形）+ 聚簇优先四原则 + 真嵌套定义 |
| P1 | `tool-presentation-quality-gate-pipeline` | tool | 双防线质量控制：四道机械闸门 + 七维独立终审 + 信任红线 + 降级铁律 |
| P1 | `dk-spatial-narrative-pitfalls` | dk | 空间叙事四大失败模式：等距平铺 / 伪嵌套 / 缺 imgfocus / 构建者自审 |
| P1 | `case-infinite-canvas-founders-playbook` | case | 60 镜头《创始人手册》：中心辐射 + 7 聚簇 + 真嵌套 + 42MB 单文件 HTML |

**说明**：其中 `case-infinite-canvas-founders-playbook` 已存在（老顽童 2026-07-21 初稿，status=draft），任务执行时只需按验收标准补齐，无需从零新建。

### 4.2 能力层：Skill 部署（S1-S4）

| # | 任务 | 执行者 | 验收标准 |
|:---|:---|:---|:---|
| S1 | 部署 `infinite-canvas-prezi` 为 KDO Skill | 老顽童 | skill 可被 `/infinite-canvas-prezi` 触发；⚠️ scripts 当前不存在，需迁移或重建 |
| S2 | 七维终审适配 KDO 上下文 | 黄药师 | 终审清单引用 KDO 卡片路径；与欧阳锋审查方法论卡建立 related 双向链 |
| S3 | 编译 Prezi 构建 Agent 的 agent-spec | 黄药师 | 角色定位 + 对话模式 + 工具映射 + Feature 清单 |
| S4 | 升级 `skill-duanwangye-prezi.md` | 段王爷/欧阳锋 | status draft→reviewed；⚠️ 项清零或标注阻塞原因；与 #198 卡片层产出建 related |

### 4.3 与已有资产的关系

| 已有资产 | 位置 | 状态 | 关系 |
|:---|:---|:---|:---|
| `skill-duanwangye-prezi.md` | `30_wiki/skills/` | draft | 段王爷已做发布域适配；#198 提取通用方法论，产出后双向 related |
| `markdown-to-presentation` | `40_outputs/capabilities/skills/` | stable | 覆盖 Marp/Slidev/reveal.js，缺 Prezi 线；#198 补空间叙事支路 |
| `case-infinite-canvas-founders-playbook` | `30_wiki/cases/` | draft | 已存在，需按验收标准补齐 |

---

## 5. 基础设施层：待黄药师判断的三件事

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

## 6. 对老朱/OPC 的即时价值

这份能力建设不只是为了 KDO 工厂本身，对老朱当前业务也有直接用途：

1. **商业方法论可视化**：利润为王、五步法、Y 模型等都可做成空间叙事演示。
2. **出海/代理商推介**：单文件 HTML、断网可播、浏览器即开，适合海外客户。
3. **知识库视觉层**：KDO 卡片是文字层，无限画布可以成为「知识地图」的可视化层。
4. **融资/BP 演示**：巨米教训、鑫港湾商业模式用空间叙事呈现更有说服力。

---

## 7. 建议执行顺序

已按 P0/P1 在任务单中标注优先级。领取后建议按以下顺序执行：

1. `concept-spatial-narrative-design`（P0，方法论基础）
2. `tool-presentation-quality-gate-pipeline`（P1，承接 concept 的操作法）
3. `dk-spatial-narrative-pitfalls`（P1，与 tool 卡配套）
4. `case-infinite-canvas-founders-playbook`（P1，补齐已有草稿）
5. S1-S4 Skill 部署层（卡片层完成后启动）

---

## 8. 待黄药师确认的问题

1. `prezi_gate.py`、`roam2prezi.py`、`prezi2roam.py` 是否已有可执行脚本？还是仅停留在教程描述阶段？
2. 是否值得为无限画布新增一个独立的 artifact subtype，还是先复用 `content/presentation`？
3. `skill-duanwangye-prezi.md` 当前 draft 中提到的「机械闸门待迁移」是否已有开发计划？
4. 这份素材应归入哪个 domain？任务单已选 `content-production`，是否合适？

---

*王语嫣 · 2026-07-21 · #198 终审版 · 执行任务单：`60_feedback/tasks/task_20260721_wangyuyan-infinite-canvas.md`*
