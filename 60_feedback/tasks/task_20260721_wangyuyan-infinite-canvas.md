---
id: task_20260721_wangyuyan-infinite-canvas
task_id: 198
assignee: hermes
status: in_progress
created_at: 2026-07-21
updated_at: '2026-07-20T17:51:05.117583+00:00'
domain: content-production
priority: P1
source: 00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/
diagnosis: 60_feedback/diagnosis/diag_20260721_wangyuyan-infinite-canvas.md
---

# 无限画布Prezi · 卡片化与Skill部署任务

## 任务目标

将王欢`infinite-canvas-prezi`技能文档的核心方法论（空间即逻辑+双防线质量控制）转化为KDO wiki卡片，并把方法论解压为可运行的Skill/Agent能力。素材为已完成技能文档，聚焦**设计哲学和工程化方法论**提取，不重复技能本身的操作教程。

## 迭代记录 · #198 终审裁定（王语嫣 2026-07-21 合并）

| 对方提议 | 裁定 | 本任务单处理 |
|:---|:---|:---|
| 补 `framework` 卡 | ❌ 不采纳 | 流水线与质量机制已在 `tool-presentation-quality-gate-pipeline` 中承载，拆出重复 |
| 4 张→桥接卡 | ❌ 不采纳 | 素材为技能文档而非口述方法论，4 张够用；桥接卡待后续真实需求出现时再建 |
| 升级 `skill-duanwangye-prezi.md` | ✅ 采纳 | 纳入 S4：status draft→reviewed，与卡片层产出建立 related 双向链 |
| 脚本可用性标注 | ✅ 采纳 | S1 已标注 ⚠️：`prezi_gate.py`/`roam2prezi.py`/`prezi2roam.py` 当前不存在，需迁移或重建 |
| 与 `markdown-to-presentation` 关系 | ✅ 采纳 | 已纳入「已有资产对齐」表：markdown-to-presentation 覆盖传统幻灯，本任务补空间叙事支路 |
| 三阶段执行 | ⚠️ 部分 | P0/P1 优先级已在卡片规格中标明，不强制分 Phase；领取后按 P0→P1 顺序执行 |

## 素材

| 文件 | 路径 |
|:--|:--|
| 技能教程正文 | `00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/王欢：把一个想法，做成一张会移动的无限画布.md` |
| VLM识别报告 | `00_inbox/多模态输出/王欢：把一个想法，做成一张会移动的无限画布/_vlm_output/识别报告_无限画布教程.md` |

## 卡片规格

### P0（1张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 1 | concept-spatial-narrative-design | concept | 空间即逻辑：内容逻辑→空间结构的映射 | 四种空间结构(路径/嵌套/对比/环形) + 聚簇优先四原则 + 真嵌套的定义(scale比≥3、子坐标在父包围盒内、钻入+退回)。哲学基础：画布的位置关系=内容的逻辑关系 |

### P1（3张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 2 | tool-presentation-quality-gate-pipeline | tool | 演示产线双防线质量控制 | 四道机械闸门(plan/media/build/final, rc≠0拦截) + 七维独立终审(R1-R7, 独立子Agent执行) + 信任红线(构建者禁自审/禁改review.json) + 降级铁律(2-3次失败→立即降级) |
| 3 | dk-spatial-narrative-pitfalls | dk | 空间叙事四大失败模式 | 等距平铺(无聚簇)/伪嵌套(平铺装层级)/横图看不清(缺imgfocus)/构建者自审(违信任红线) |
| 4 | case-infinite-canvas-founders-playbook | case | 60镜头《创始人手册》：Prezi式创业旅程画布 | Claude Blog长文→60镜头单文件HTML；空间结构：中央标题锚点+7章节聚簇中心辐射+每章3嵌套子讲点；技术栈：impress.js 2.0.0，42MB单文件全内联 |

**合计：4张（1 P0 + 3 P1）** — 素材为已完成技能文档，提取方法论核心，不与技能操作教程重复

## 验收标准

1. source_refs引用技能教程行号
2. concept卡必须含：四种空间结构图示、聚簇四原则、真嵌套vs伪嵌套对照
3. tool卡必须含：四闸对应的确定性规则清单、七维各自的检查问题、信任红线声明
4. related ≥5且≥2跨域（必须链接四字诀和欧阳锋审查方法论）
5. 提交前跑`kdo pre-submit`

## 已有卡关联（必须建立 related）

### 关系型（双向，必须）

| 已有卡 | 同构关系 | 回链内容 |
|:--|:--|:--|
| framework-一堂-基本功-四字诀拆建推练 | 三步流水线(Plan→Media→Build)与四字诀同构 | 四字诀卡新增"演示产线"场景实例 |
| framework-ouyangfeng-review-methodology | 七维独立终审与欧阳锋五轴审查+魔鬼代言人+分层阻断**完全同构**——都是独立审查、多维检查、禁止自审 | 欧阳锋方法论卡新增"演示产线审查"作为跨域应用 |

### 引用型（单向，必须）

| 已有卡 | 关系 |
|:--|:--|
| framework-yitang-case-crafting-four-step (#196) | 空间叙事=案例表达四步法"打磨表达"的可视化版本 |
| framework-一堂-表达力火箭模型 | 空间设计服务于表达递进 |
| infinite-canvas-prezi skill | 本任务是技能的**方法论提取**，不是重复技能教程 |

## 边界说明

- **不覆盖**：技能本身的操作教程（已有王欢原文和index.html）
- **不覆盖**：impress.js技术文档
- **不重复**：四字诀/欧阳锋审查方法的完整内容（只建引用和同构声明）
- **域归属**：归入content-production域（演示内容生产），与欧阳锋审查方法论跨域桥接

## 🔴 附加任务：Skill部署层（2026-07-21 迭代追加）

> 基于KDO建模方法论§解压展开（tool→skill→workflow→agent-spec编译链）。卡片层提取方法论，Skill层让工具可被KDO调用。

| # | 任务 | 执行者 | 验收标准 |
|:--|:--|:--|:--|
| S1 | 将`infinite-canvas-prezi`部署为KDO skill | 老顽童 | skill可被`/infinite-canvas-prezi`触发。⚠️ `~/.claude/skills/infinite-canvas-prezi/scripts/`当前不存在——王欢教程引用的`prezi_gate.py`/`roam2prezi.py`/`prezi2roam.py`需创建或从原仓库迁移，非直接可用 |
| S2 | 七维终审适配KDO上下文 | 黄药师 | 终审清单中引用KDO卡片路径替代原路径；与欧阳锋审查方法论卡建立related双向链 |
| S3 | 编译agent-spec：Prezi构建Agent | 黄药师 | 角色定位+对话模式+工具映射写入agent-spec卡；含Feature清单（诊断报告§八·Feature分解） |
| S4 | 升级`skill-duanwangye-prezi.md`状态 | 段王爷/欧阳锋 | status: draft→reviewed；能力表中⚠️项清零或标注阻塞原因；与#198的卡片层产出建立related双向链 |

**卡片层（4张）+ Skill层（4项）= 完整成果**

## 已有资产对齐

| 资产 | 位置 | 状态 | 与#198关系 |
|:--|:--|:--|:--|
| skill-duanwangye-prezi.md | `30_wiki/skills/` | draft (2026-07-20) | 段王爷已做领域适配；#198卡片层提取通用方法论，skill卡保留发布域适配。产出后双向related |
| markdown-to-presentation | `40_outputs/capabilities/skills/` | stable | 覆盖Marp/Slidev/reveal.js，缺Prezi线；#198补上空间叙事这一支 |

## 特殊说明

- 洪七公已完成VLM预处理（22张图逐图识别），老顽童可直接引用
- ⚠️ 脚本未部署：王欢教程中的机械闸门脚本当前不存在于本环境，S1需从原仓库迁移或按教程重建
