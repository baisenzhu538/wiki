---
title: "KDO 系统说明书"
type: manual
status: active
version: "1.2.0"
created_at: "2026-06-08"
updated_at: "2026-06-09"
changelog:
  - "1.2.0 (2026-06-09): 广冷电子经验工业化——硬件交叉验证检查单、电子工程目录结构标准化、弱结构素材提取骨架、产出模板体系(template+checklist+CLI)、source_refs硬门禁(空→ERROR)、标签建议模式(kdo tag suggest)"
  - "1.1.0 (2026-06-08): 标签体系升级——二级场景标签(38个)+边界标签(5个)+可靠性标签(4个)，Agent路由精度从47张/标签提升至22张/标签"
  - "1.0.0 (2026-06-08): 初始版本——完整管线/命令/四卡体系/lint规则/Skill体系/案例库/架构"
---

# KDO 系统说明书

> Knowledge Delivery OS — 知识工厂基础设施
> 版本：2026-06-08 | 测试：455 passed, 1 skipped

---

## 一、KDO 是什么

KDO 是一个**知识工厂基础设施**。它把原始素材（口述稿、文章、对话、图片）转化为结构化的知识卡片，再将卡片编译为 AI Agent 可加载的 system prompt，最后发布为可部署的 Skill 包。

核心原则：**卡片是知识原子。四卡体系描述完整方法论。Agent 做、人判断。**

---

## 二、知识管线

```
capture → ingest → enrich → produce → validate → encapsulate → publish
  捕获      编译      充实      产出        校验        编译Agent    发布
```

### 2.1 输入层

| 命令 | 用途 | 示例 |
|:---|:---|:---|
| `kdo capture <text>` | 捕获文本到 inbox | `kdo capture "一段口述稿" --title "纪浩分享"` |
| `kdo fetch-url <url>` | 抓取 URL 内容 | `kdo fetch-url https://... --title "某文章"` |
| `kdo import-chat <path>` | 导入 AI 对话 | `kdo import-chat chat.txt --format json` |
| `kdo quick "<text>"` | **Do-first 快速入口**——一句话变卡片 | `kdo quick "纪浩说信息要按场景聚合"` |

### 2.2 加工层

| 命令 | 用途 |
|:---|:---|
| `kdo ingest` | 编译 inbox → raw sources + wiki 骨架 |
| `kdo enrich [--all]` | 自动填充 wiki 卡片中的 TODO 占位 |
| `kdo query "<问题>"` | 语义+图谱检索（LightRAG + BM25） |
| `kdo clean-transcript <file>` | ASR 转录稿清理（去噪+分段+术语标注） |

### 2.3 产出层

| 命令 | 用途 |
|:---|:---|
| `kdo produce <type>/<subtype> --topic <主题>` | 创建 artifact 骨架到 40_outputs |
| `kdo validate [artifact_id]` | 按质量门校验 artifact |
| `kdo validate --v15 --card <id>` | v1.5 三信号校验（攻击者+不要用+触发器） |
| `kdo brief --topic <主题>` | 生成交接简报 |

### 2.4 Agent 编译层（知识→产品）

| 命令 | 用途 | 示例 |
|:---|:---|:---|
| `kdo encapsulate <skill-id>` | 编译 skill manifest → system prompt | `kdo encapsulate note-coach -o prompt.md` |
| `kdo skill list [--json] [--query]` | 列出所有可用 skill | `kdo skill list --query "笔记"` |
| `kdo skill validate <id>` | eval cases 结构校验 + 覆盖率报告 | `kdo skill validate note-coach --strict` |
| `kdo skill publish <id>` | 编译+打包→发布到本地目录 | `kdo skill publish note-coach -o ~/Nutstore/skills/` |
| `kdo skill install --source <dir>` | 从发布目录安装 skill | `kdo skill install -s ~/Nutstore/skills/note-coach/1.0.0` |

### 2.5 交付与反馈

| 命令 | 用途 |
|:---|:---|
| `kdo ship <artifact_id> --channel <渠道>` | 记录交付事件 |
| `kdo feedback <text> [--kind]` | 记录反馈信号 |
| `kdo improve [--apply]` | 从反馈生成改进计划 |
| `kdo case list [--query] [--json]` | 案例库检索 |

---

## 三、四卡体系（知识原子类型）

KDO 用四类卡片描述一个完整的方法论体系。欧阳锋确认：**四卡够用，关键是"一组卡协作"，不是一张卡单打独斗。**

| 类型 | 用途 | 示例 | 必含内容 |
|:---|:---|:---|:---|
| **concept** | 概念全景——"这是什么" | `concept-纪浩-ai-collaboration-methodology` | Summary / Claims / Critique / Synthesis |
| **skill** | 操作技能——"怎么做" | `skill-纪浩-four-elements-validation` | Purpose / Protocol / When to Use / When NOT to Use / Critique |
| **dk** (dark-knowledge) | 暗知识——"踩过的坑" | `dk-纪浩-pdca-starts-from-do` | 原始表述 / 使用场景 / 操作方法 / 适用边界 / 为什么值钱 |
| **case** | 案例——"有人做成过" | `case-半肥猫-course-to-skill` | 场景 / 四要素验证 / 核心洞察 / 可迁移场景 / 反例 |

**案例卡专属**：独立目录 `30_wiki/cases/`，有索引页和 `kdo case list` 检索命令。

---

## 四、质量门（lint 规则清单）

所有 lint 规则在 `kdo lint` 运行时自动执行。共 15+ 规则，覆盖结构、溯源、内容深度。

### 结构校验

| 规则 | 检查内容 |
|:---|:---|
| 目录完整性 | 必填目录是否存在（00_inbox / 10_raw / 30_wiki / 40_outputs 等） |
| 控制文件 | 必填模板文件是否存在 |
| 重复 ID | state.json 中 id 是否重复 |
| 路径存在性 | artifact / source / delivery 的路径是否指向真实文件 |
| wiki 完整性 | 30_wiki/ 下所有卡片是否在 index.md 中注册 |
| wiki 孤立页 | 无 incoming wikilink 且未入 index 的页面 |
| wikilink 死链 | `[[broken-link]]` 是否指向不存在的文件 |

### 卡片结构

| 规则 | 检查内容 |
|:---|:---|
| concept 卡 | source_refs 是否为空 / status 与必填字段一致性 |
| skill/tool 卡 | Purpose / Protocol / When NOT to Use / Critique 是否缺失 |
| dk 卡 | dark_knowledge_type / source_person / source_context 是否缺失 / 五段结构是否完整 |
| case 卡 | 四要素验证 / 可迁移场景 / 反例 / source_person / source_context 是否缺失 |

### 溯源校验

| 规则 | 检查内容 |
|:---|:---|
| source_refs 存在性 | 引用的文件是否真实存在 |
| source_refs fuzzy | 文件名相似度 >80% 但非精确匹配 → 可能的 typo（如"请单"vs"清单"） |
| OCR 强制检查 | source_refs 中的 .png/.jpg 是否有关联的 `*_paddle_ocr.txt` |
| artifact 孤儿检测 | 40_outputs/ 下的 .md 是否在 state.json 有注册 |

### 深度检测

| 规则 | 检查内容 |
|:---|:---|
| Synthesis 死链 | `## Synthesis` 段的 wikilink 是否指向存在的文件 |
| 跨卡相似度 | 不同卡片的"常见失败模式"等节段是否 copy-paste（>85% 相似） |
| 核心概念缺失 | 标题声称"N要素/N大原则"但 body 没有列出对应数量的条目 |
| L2 内容质量 | Condense 段中文 bullet ≥3 / Critique 含关键词（具体假设/边界/反例） / Synthesis 外部链接 ≥2 |

### 基线管理

| 命令 | 用途 |
|:---|:---|
| `kdo lint` | 运行全量 lint，自动对比 baseline.json，只显示新增问题 |
| `kdo lint --accept-baseline` | 将当前所有 warning 存入 baseline.json（接受历史债） |
| `kdo lint --diff` | 对比 HEAD~1，只显示本分支新增问题 |
| `kdo lint --structure-report` | 输出全库卡片结构类型分布 |

---

## 五、Skill 体系

### 5.1 三层文件结构

每个 Skill 在 `40_outputs/capabilities/skills/<id>/` 下有标准三文件：

```
note-coach/
├── SKILL.md          ← KDO 注册入口（agent 发现和调用）
├── manifest.yaml     ← 单一真相源（知识注入/能力/约束/评测/渐进式披露）
└── system-prompt.md  ← 编译产物（可直接部署）
```

### 5.2 manifest.yaml 结构

```yaml
skill:
  id / name / version / role(P|C) / description / tagline

knowledge:
  design_principles: [...]           # 所有层级共享
  progressive_disclosure:            # 渐进式披露（纪浩模式）
    triage:                          # L1 导诊台：必加载
    work_manual:                     # L2 工作手册：按能力路由
      capability_routing: [...]
    experience:                      # L3 经验库：失败信号触发
      triggers: [...]
    domain:                          # L4 领域知识：深层溯源
      cards: [...]

capabilities:                        # 能力清单（I/O + 质量标准）
constraints:                         # 硬约束（角色/边界/格式/知识/元规则）
interaction:                         # 触发模式 + 默认响应
eval:                                # 测试用例
  cases:
    - id / tests / input / expected_output_contains / expected_output_not_contain
```

### 5.3 渐进式披露

知识不是一次性全部注入——是按需四层递进：

```
L1 导诊台（必加载）    → Agent 身份认知 + 任务路由
L2 工作手册（按能力）   → 只在对应能力触发时加载
L3 经验库（信号触发）   → 检测到失败模式时加载
L4 领域知识（溯源时）   → 需要深层方法论时加载
```

### 5.4 Skill 质量门

```
kdo skill validate <id>     → eval cases 结构校验 + 覆盖率报告
kdo lint                     → 卡片溯源 + 结构完整性
kdo encapsulate <id>         → 编译 system prompt
kdo skill publish <id>       → 发布
```

---

## 六、案例库

### 6.1 位置

`30_wiki/cases/` ——独立于概念卡/skill 卡的专属目录。

### 6.2 检索

```
kdo case list                 → 全部案例
kdo case list --query "Agent" → 按关键词搜索
kdo case list --json          → JSON 输出
```

### 6.3 当前案例

| # | 案例 | 教什么 |
|:--:|:---|:---|
| 1 | 纪浩 Skills 市场 | Agent 分发平台怎么做 |
| 2 | Truman AI Partner | 领域 Agent 怎么设计（哲学层） |
| 3 | 纪浩 /focus 设计 | 结构化 prompt 怎么做产品设计 |
| 4 | 半肥猫 课程转 Skill | 端到端：课程→Skill 的完整工程流程 |
| 5 | 以太在线获客 | 商业案例 |

---

## 七、Graph RAG

纯本地知识图谱检索。零外部 API 依赖。

| 命令 | 用途 |
|:---|:---|
| `kdo graph rebuild` | 重建索引（内容变更后运行） |
| `kdo graph query "<问题>"` | 语义+图检索 |
| `kdo graph stats` | 索引统计 |

---

## 八、其他命令速查

| 命令 | 用途 |
|:---|:---|
| `kdo status` | 工作空间库存盘点 |
| `kdo cards [--type] [--domain] [--count]` | 按条件列出概念卡 |
| `kdo review --sample 5 --domain <域>` | 随机抽检卡片 |
| `kdo scaffold --card <id>` | 为缺 v1.5 信号的卡生成升级骨架 |
| `kdo stale` | 检测过期卡片（按域/类型的 review 间隔） |
| `kdo project / task / connector` | 产品项目管理 |
| `kdo dashboard [--serve]` | 生成静态 HTML dashboard |
| `kdo video init/validate/render/compose/ship` | 视频管线 |
| `kdo backup [--output <dir>]` | 备份 KDO 源码 |
| `kdo llm-check` | LLM 连通性自检 |
| `kdo label` | Auto-label chunks（pre-screen → LLM → route） |

---

## 九、系统架构

```
KDO CLI (Python, ~14,000 行, 47 .py 文件)
├── kdo/commands/          ← 命令实现（ingestion / delivery / quality / graph / system / encapsulate）
├── kdo/workspace.py       ← lint 规则（15+ 规则）+ 状态管理 + 前端解析
├── kdo/cli.py             ← CLI 注册（40+ 子命令）
├── kdo/validation.py      ← v1.5 三信号校验
├── kdo/links.py           ← wikilink 解析 + 死链检测
├── kdo/artifacts.py       ← artifact 生命周期管理
└── kdo/search_index.py    ← CJK 语义搜索
```

测试：455 passed, 1 skipped（pre-existing CSRF）, 0 new failures。

---

## 十、角色分工

KDO 知识工厂五角色（详见 `90_control/AGENTS.md`）：

| 角色 | 代号 | 职责 |
|:---|:---|:---|
| Architect | 欧阳锋 | 审查全部产出、任务分配、架构决策、质量标准 |
| Builder | 黄药师 | KDO CLI 开发、质量门、Graph RAG、基础设施 |
| Producer | 老顽童 | 卡片量产、文章/内容、跨域合成 |
| Multimodal | 洪七公 | 知识→视觉资产、OCR→结构化、图片→prompt |
| Publisher | 段王爷 | `kdo ship`→渠道分发、反馈收集、版本发布 |

---

*本文档自动生成于 2026-06-08。最新命令列表请运行 `kdo --help`。*
