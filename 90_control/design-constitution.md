---
id: design-constitution
title: 《KDO 设计宪法》v0.1（方案 B：卡片 + 视觉资产 + Agent spec 全产出物）
type: constitution
version: v0.1
author: 黄药师
created_at: '2026-08-30'
updated_at: '2026-08-30'
status: pending_review
audience: 六角色
supersedes: null
amends: null
source_refs:
- 30_wiki/dark-knowledges/dk-aesthetic-redline-doc.md
- 30_wiki/concepts/concept-ai-style-knowledge-docs.md
- 30_wiki/concepts/concept-kdo-agent-design-principles.md
- 90_control/quality-gates/kcard.md
- 00_inbox/我用一堂做一堂/战略笃定-一堂AI转型复盘-口述.txt
---

# KDO 设计宪法 v0.1

> 域级宪法（charter §1「域级宪法（如设计宪法）在本法之下」）。把 Truman「设计宪法」暗知识落地为 KDO 的设计边界/审美红线 Data Pack。素材锚点：战略笃定篇口述（L1622-1628「设计宪法就是界定 AI，尤其设计类 AI 设计边界的东西……做了设计宪法的 Data Pack 存本地，它自己学一下」）。
> 生效链：欧阳锋终审 → 老朱拍板 → v1.0 生效。本稿 v0.1 提审中（红线清单先行，审美样例后补）。

## 1. 定位

设计宪法 = 界定 AI（尤其设计类 AI）**设计边界**的 Data Pack——「红线只讲一次，落文档 + 每次强制检查」。Truman 原话：「之前每次喷半天 AI 才知道我的基本规则，现在做了设计宪法的 Data Pack 存本地，它自己学一下就行了」。它是 `concept-ai-style-knowledge-docs` 定义的 10-11 种 AI Style 文档之一（设计方向）。

## 2. 范围（方案 B：三类产出物全覆盖）

老朱拍板设计宪法范围 = **方案 B**：覆盖 KDO 三类产出物的设计边界/审美红线——

| 产出物 | 生产者 | 落点 |
|:--|:--|:--|
| **卡片**（知识卡/工具卡/框架卡/dk） | 老顽童 / 黄药师 | `30_wiki/` |
| **视觉资产**（信息图/海报/SVG/视频） | 洪七公 | `40_outputs/content/` |
| **Agent spec**（岗位说明书/SOUL/context） | 黄药师 / 王语嫣 | `30_wiki/agent-specs/` + `.agent/` |

## 3. 核心机制（只讲一次 + 强制检查）

1. **只讲一次落文档**：红线写成「不允许出现什么」清单，一次说清，不再重复（口述 L1588「我只说你一次，我说完了你给我记到系统里」）。
2. **AI 强制检查**：红线进 AI 的 ToDo/检查清单，每次产出都查一遍（口述 L1590「新 To-Do list 以后每次都给我查一遍」）。
3. **定期刷新**：新红线追加（同文档叠加），过期红线合并/删减，保持清单可执行（`dk-aesthetic-redline-doc` Critique）。

## 4. 三类产出物红线清单（「不允许出现什么」）

### 4.1 卡片红线

| # | 红线（不允许） | 出处 |
|:--|:--|:--|
| 1 | source_refs 为空就进 enriched/reviewed | kcard gate 禁止事项 F-KDO-014 |
| 2 | author=legacy；reviewed_by=pending 但 status=reviewed（元数据造假） | kcard gate 禁止事项 |
| 3 | 一卡多事（违反卡片粒度铁律：一卡一事、案例独立、工具可执行） | 卡片粒度铁律（老朱+实战双验证） |
| 4 | 写审分离违反（author=reviewed_by，自我审查） | rules-core #4 / E018 |
| 5 | 工具名进资产文件/署名（署名只记角色名） | charter §3.4 命名铁律 |
| 6 | 三套编号混用（doc_id / #队列号 / 卡片 id） | file-flow-protocol §5 / E045 |
| 7 | 正文 src_unknown 占位不处置 | #517 门禁 |

### 4.2 视觉资产红线

| # | 红线（不允许） | 出处 |
|:--|:--|:--|
| 1 | AI 生图文字乱码/错字（生图文字不可信，须人工核） | 月白「海报文字错误修复法」卡存在即红线 |
| 2 | 色彩失真（RGB/CMYK 不校准就交付） | 月白「RGB转CMYK色彩校准法」 |
| 3 | 同项目视觉资产风格漂移（跨图不一致） | concept-ai-style-knowledge-docs 失败模式「AI 输出风格漂移→补设计宪法」 |
| 4 | VA 产物与源文件归属错位（洪七公副业：只标差异+建议，不改卡主体） | 洪七公岗位职责 |
| 5 | 无来源标注 / 无版权声明的视觉产出 | rules-core 溯源铁律 |

### 4.3 Agent spec 红线

| # | 红线（不允许） | 出处 |
|:--|:--|:--|
| 1 | 职责越界（spec 写不属于该角色的职责，或越界执行） | charter §2.6 通用行为准则 1 |
| 2 | 复制职责全文（SOUL/spec 只留最小身份+指针，真相源=charter §2.6+.agent/context，复制必漂） | #561 SOUL 对齐教训 |
| 3 | 工具名写进 spec（角色是恒量，工具是可替换耗材） | charter §3.4 命名铁律 |
| 4 | 无边界条款（spec 缺「职责外必询问」通用边界） | #455 spec 边界条款 |
| 5 | 角色名不统一（agent_id 拼音角色名未统一，或孪生 spec 漂移） | #456 / #570 |

## 5. 如何执行（Data Pack + 强制检查）

1. **落文档**：本宪法即 Data Pack，存本地（`90_control/design-constitution.md`），AI 每次工作前读。
2. **挂门禁**：机械红线（卡片红线 1/2/4/5/6/7）已由 `kdo pre-submit` / `kcard` gate / lint 机器拦截；视觉资产红线 4/5 由洪七公 VA 流程把门；Agent spec 红线 2/3/5 由 spec 审计把门。
3. **人审兜底**：审美判断（红线外的「风格要好」）留人——判断永远留人（charter §3.14 三层门控），红线管「不允许」，风格靠样例（本宪法 v0.1 先出红线，审美样例后补）。
4. **检查清单**：将 4.1/4.2/4.3 红线并入各角色产出前的检查 ToDo（一次说清，永久生效）。

## 6. 参考卡

- `dk-aesthetic-redline-doc`：红线只讲一次 + 强制检查的操作机制
- `concept-ai-style-knowledge-docs`：设计宪法=AI Style 文档之一（10-11 种）
- `concept-kdo-agent-design-principles`：Agent 设计 5 条底层原则（原则①人定审美 AI 执行=设计宪法的决策权根基）
- `90_control/cli-design-principles.md`：CLI 输出设计原则（讲香六律，接口层审美红线）

## 7. 生效规则

- 欧阳锋终审 + 老朱拍板后 v1.0 生效。
- **向前生效**：存量产出不回头改；新产出物一律过红线清单。
- 本稿 v0.1 先出红线清单；审美样例（「风格要像什么」）后补 v0.2。

---

*黄药师主笔 · 2026-08-30 · 依据 dk-aesthetic-redline-doc + concept-ai-style-knowledge-docs + kcard gate + charter 红线；无出处不写入*
