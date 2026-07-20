---
id: skill-infinite-canvas-prezi
title: "无限画布Prezi演示生成器"
type: skill
status: draft
author: 老顽童
confidence: 0.85
trust_level: medium
domain: [content-production]
source_refs:
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md"
  - "00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/_vlm_output/识别报告_无限画布教程.md"
related:
  - concept-spatial-narrative-design
  - tool-presentation-quality-gate-pipeline
  - dk-spatial-narrative-pitfalls
  - case-infinite-canvas-founders-playbook
  - framework-一堂-基本功-四字诀拆建推练
  - framework-ouyangfeng-review-methodology
created_at: 2026-07-21
updated_at: 2026-07-21
reviewed_by: pending
diagnostic_signals:
  - "⚠️ prezi_gate.py 等机械闸门脚本当前不存在，Skill 层可被触发但闸门需从原仓库迁移"
---

# infinite-canvas-prezi

> **一句话**：把任意主题或素材变成 Prezi 风格的单文件 HTML 演示——所有内容铺在一张无限画布上，镜头用缩放/平移/旋转运动讲故事，空间布局本身就是叙事逻辑。

**引擎**: impress.js 2.0.0 · **产物**: 零构建单文件 `.html` · **流程**: 三步流水线 + 四道机械闸门 + 七维独立终审

---

## 触发方式

```
/infinite-canvas-prezi
```

或自然语言描述需求，例如：
- "做一个关于黑洞的 Prezi 风格无限画布演示"
- "把 @这篇文章 做成一张镜头会缩放平移的无限画布演示"

触发后自动按 1→2→3 跑完整条流水线，只在原则性疑惑时暂停（素材严重残缺 / 多种完全不同的理解 / 受众目的无法判断）。

---

## 三步流水线

### 步骤 1 · 素材理解与画布策划（Plan）

**角色**：叙事设计师 + 信息架构师

**输入**：用户提供的主题/长文/转写稿

**动作**：
1. 完整读完素材（长文档必须分页读完，禁止只读开头就规划）
2. 建立**事实清单**：所有上屏文字/数据/术语只能来自这份清单，每条带 `source` 出处
3. 建立 `source_inventory`：登记每个重要内容点 → covered / skipped + 理由
4. 拆成 6-20 个场景，每个场景只讲一个讲点（10-30 秒可消化）
5. **由内容逻辑推导空间结构**（四种结构：路径/嵌套/对比/环形）
6. 规划每个场景坐标，落盘 `plan.json`

**产出**：`plan.json`（场景序列 + 坐标 + 事实清单）

**闸门**：`prezi_gate.py plan plan.json` — 检查场景数/坐标合法性/事实完备性

### 步骤 2 · 媒体准备（Media）

**角色**：素材采购员

**输入**：`plan.json`

**动作**：
1. 按优先级链获取素材：AI生成 → 免费图库 → 原文素材截图
2. 默认产出 60%-80% 内容场景配图（每 1-2 页一图）

**降级铁律**：每个素材最多验证 2-3 个候选 URL，全失败立即降级。按时交付完整演示 > 单个素材完美。

**产出**：`media_manifest.json`（素材URL + 许可 + 降级标记）

**闸门**：`prezi_gate.py media media_manifest.json` — 检查覆盖率/URL可达性

### 步骤 3 · 构建 HTML 演示与 QA（Build）

**角色**：资深前端工程师 + 演示设计师

**输入**：`plan.json` + `media_manifest.json`

**动作**：
1. 渲染为单文件 HTML（CSS/JS/图片全内联，base64）
2. 坐标严格照搬步骤 1 规划
3. QA 分三段：
   - **构建闸（机械）**：`prezi_gate.py build output.html`
   - **实机截图（必做）**：至少截 3 帧验证
   - **独立终审（柔，七维）**：七维独立子Agent审查

**闸门**：`prezi_gate.py build output.html` — 检查HTML有效性/impress.js加载/镜头数

---

## 四道机械闸门

| 闸门 | 检查点 | 命令 | 拦截条件 |
|:--|:--|:--|:--|
| Plan Gate | 场景数/坐标/事实清单完整 | `prezi_gate.py plan` | rc≠0 |
| Media Gate | 覆盖率/URL可达性 | `prezi_gate.py media` | rc≠0 |
| Build Gate | HTML有效性/impress.js/镜头数 | `prezi_gate.py build` | rc≠0 |
| Final Gate | 全量文件完备性 | `prezi_gate.py final` | rc≠0 |

> ⚠️ **脚本可用性声明**：`prezi_gate.py`、`roam2prezi.py`、`prezi2roam.py` 当前不存在于 KDO 环境。教程中引用的这些脚本需从王欢原仓库迁移或按教程重建。Skill 层可被触发，但闸门脚本未就绪时无法执行机械检查——此时应诚实告知用户阻塞状态，不得跳过闸门直接交付。

---

## 七维独立终审

| 维度 | 检查问题 | 执行者 |
|:--|:--|:--|
| R1 完整性 | 原素材的重要点都覆盖了吗？ | 独立子Agent A |
| R2 准确性 | 数字/事实与原素材一致吗？ | 独立子Agent B |
| R3 空间 | 只看全景图能读出内容结构吗？（路径/嵌套/聚簇） | 独立子Agent C |
| R4 视觉 | 配图风格统一吗？信息可读吗？ | 独立子Agent D |
| R5 节奏 | 镜头运动流畅吗？有晕眩感吗？ | 独立子Agent E |
| R6 体验 | 浏览器直接打开正常吗？断网可播吗？ | 独立子Agent F |
| R7 合规 | 图片许可/敏感信息合规吗？ | 独立子Agent G |

**信任红线**：
- 构建者禁自审——七维审查全部由独立子Agent执行
- 禁改 `review.json`——审查结论不可被构建者覆盖
- 3/7 项不通过 → 退回构建者返修
- 2-3 次连续不通过 → 降级为人工接管

---

## 双防线质量控制

```
机械闸门（确定性规则）         独立终审（柔，七维）
─────────────────────       ─────────────────────
rc≠0 = 绝对拦截             各维独立评估
无主观判断                   不通过→返修→重审
四道串行                     七维并行（子Agent）
```

两道防线完全独立——机械闸门通过 ≠ 终审通过；终审通过的前提是机械闸门先全过。

---

## 与欧阳锋审查方法论完全同构

| 无限画布Prezi | 欧阳锋审查方法论 | 同构点 |
|:--|:--|:--|
| 四道机械闸门 | L1 机械门禁（kdo lint） | 确定性规则，rc≠0 拦截 |
| 七维独立终审 | L3 审查终审（五轴+魔鬼代言人+分层阻断） | 独立审查、多维检查 |
| 构建者禁自审 | 写审分离（"牲口而非宠物"） | 禁止自审 |
| 降级铁律 | 分层阻断 | 连续失败→降级 |

---

## 工具映射

| 工具 | 用途 |
|:--|:--|
| AI 生图 | `Evan-gpt-image` → `gen_via_codex.py`（codex CLI 订阅额度） |
| impress.js CDN | `cdn.jsdelivr.net/gh/impress/impress.js@2.0.0`（唯一实测可用） |
| 公开预览 | `wrangler` CLI（需先确认才部署，不自动推公网） |

---

## 何时触发

- 用户明确说：**Prezi / Prezi 风格 / 无限画布 / 空间叙事 / impress.js / 镜头在一张画布上缩放平移旋转**
- 内容有天然空间结构：总分/层级、时间线/流程、对比、循环
- 想要**单文件、零构建、浏览器直接打开**的可分享演示

## 何时别触发

- 用户要的是"一页页翻的幻灯"→ 走 `markdown-to-presentation`（Marp/Slidev/reveal.js）
- 内容简单（<3 层次）→ 传统 PPT 更高效
- 被泛化的"会动的网页/缩放动画"描述 → 确认用户是否真的需要空间叙事

---

## 已知限制

1. **闸门脚本未部署**：`prezi_gate.py`/`roam2prezi.py`/`prezi2roam.py` 需从原仓库迁移
2. **impress.js 2.0.0**：社区活跃度有限（GitHub 最后一次 release 为 2017 年），技术选型有长期风险
3. **单文件大小**：42MB 全内联在移动端/弱网体验差，按需加载需后续迭代
