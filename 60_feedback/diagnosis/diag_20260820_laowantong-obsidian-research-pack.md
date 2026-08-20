---
id: diag_20260820_laowantong-obsidian-research-pack
title: Obsidian×AI 知识管理调研包（4 子题）——老顽童 2026-08-20
type: diagnosis
author: 老顽童
created_at: 2026-08-20
status: pending_wangyuyan_gate
source: 楚门-AI知识管理探索营（口述 3510 行 + 逐字稿）
---

# Obsidian×AI 知识管理调研包（4 子题）

> 老朱 08-20 课程收官拍板立项；本报告产调研结论（非卡片），①②③补强/新卡清单分开陈述，④为长程研判。
> 溯源分级：**实测**（网络一手/库内已证）/ **引用**（口述锚点原文）/ **推演**（我的分析推断，非实测）。
> 网络受限说明：reddit / modelcontextprotocol.io / docs.anthropic.com 本环境不可达，相关结论标注"推演"或"未获取"（O0 零编造）。

## 子题① Obsidian 高质量图

### 锚点校准（一等证据）
- 口述 L1186-1214：16 项目调研最佳实践图（产品/工程调研+客户案例）——"全程 15 秒，就是一句口说出来的，靠的就是这套东西，所有上下文 AI 是自己学的"；"我说我想做一个插画，叫做大量调研最佳实践……去森林里找一找我的各种项目……做一个拼接的图吧"
- 口述 L2220-2266：做图带宽=五设计师并行——"我直接五个设计师同时上班……A 做这张图，B 做这个图，按照系列拆开分工"；"每一个 session 打开，我只需要跟他说一句话，叫我给你看一下设计规范，熟悉一下项目就可以干活"；"做完了我让他写一个设计规范……然后他其他的人就可以接着干活了"；"我不只是把我的设计师的能力，我还可以用一份设计规范把设计师几乎一秒钟变成另外一个人的设计师能力"

### 全网发现
| 来源 | 分级 | 要点 |
|:--|:--|:--|
| [JSON Canvas 官网](https://jsoncanvas.org/)（Obsidian 官方 2024-03 开源） | 实测 | Canvas 文件格式开放化（spec/1.0）：nodes/edges 的 JSON 结构——**程序/AI 可直接读写**，这是"Agent 做图"的基础设施前提 |
| [Obsidian blog: JSON Canvas](https://obsidian.md/blog)（kepano 2024-03-11） | 实测 | 开放文件格式 + 规范 + 开源资源；无限画布工具用于空间化组织信息 |
| [Mermaid 官方](https://mermaid.js.org/intro/) | 实测 | "用文本和代码创建图表可视化……渲染 Markdown 启发的文本定义动态生成/修改图表"——**text→diagram，与楚门派'口喷→图'同构**，Agent 可直接写 Mermaid 源码成图 |
| Excalidraw（官网） | 实测 | 无限画布白板工具（JS 应用，细节本环境未深取） |
| [Obsidian 论坛 Canvas 实践帖](https://forum.obsidian.md/t/canvas-tips/59294) | 实测 | Canvas 插件日常使用问题社区生态活跃 |
| [Obsidian 论坛 research canvas](https://forum.obsidian.md/t/organizing-research-by-creating-traceable-links-in-the-canvas/79711) | 实测 | Canvas 做**可追溯研究链接**：页面入 canvas→链接→Metadata Menu 转 frontmatter links→脚本溯源；插件栈 Dataview/DB Folder/Metadata Menu/Simple CanvaSearch/Templater |

### 路线对比（楚门派 vs Obsidian 生态）
| 维度 | 楚门派（口述锚点） | Obsidian 生态路线 |
|:--|:--|:--|
| 图源 | 口喷一段话→Agent 从知识库学→拼接生成 | Canvas 手工/半自动排版；Mermaid 代码生成 |
| 规模化 | 五 Agent 并行 + 设计规范复制（L2220-2266） | 模板复用 + 插件自动化（Dataview/Metadata Menu） |
| 一致性 | 设计规范文档=能力复制介质（L2246-2258） | 主题/模板（CSS/模板变量） |
| 可追溯 | 上下文自动学（L1206） | JSON Canvas 开放格式 → 可脚本化溯源（forum 79711） |

**融合判断（推演）**：楚门派把"做图"当作 Agent 能力（口喷+规范复制），Obsidian 生态把"图"当作开放数据（JSON Canvas+Mermaid 文本）；二者不冲突——**Agent 口喷生成 JSON Canvas/Mermaid 文件**即是融合点（楚门做事方式 × Obsidian 开放格式）。

### 补强已有卡清单（L7 已查，不重复造卡）
| 已有卡 | 补强点 |
|:--|:--|
| `case-truman-ai-image-workflow-evolution` | 补五设计师并行+设计规范复制机制（L2220-2266） |
| `dk-three-context-formula` | 补做图场景的上下文补全实证（L2236-2238"补两个上下文秒变专业"） |

### 新卡候选清单
| 候选卡名（提案） | 类型 | 依据 |
|:--|:--|:--|
| dk-agent-parallel-design-system（Agent 并行做图+设计规范复制） | dk | L2220-2266：五设计师并行+规范=能力复制介质 |
| tool-json-canvas-agent-write（Agent 写 JSON Canvas 开放格式图） | tool | JSON Canvas 官方 spec + 楚门派口喷生成图（推演融合） |

## 子题② Obsidian 最佳实践调研

### 锚点校准
- 口述 L984-992：调研想法→"随便喷口拍一段，他就用非常专业的一堂科学体系方法，交叉验证的、全面搜集的调研方法帮我去"；"市场很多调研能力/工具都不够好，太通用了，商业表演上有点弱，而且很随机"
- 口述 L1550-1554：最佳实践指南文档=资产包（"类似于我刚才的报告，那就是一个最佳实践的最佳文档是个资产包，有点像包研究"）
- 口述 L3254：楚门自追全球最佳实践——"目前全球范围内的知识管理的最佳实践……LLM 类自动化的知识管理的工作流"
- 逐字稿 L343：idea→Agent 聊目标边界→启动调研→报告放 Obsidian（"调研国内一人公司 APP 最佳实践清单"）

### 全网发现
| 来源 | 分级 | 要点 |
|:--|:--|:--|
| [Obsidian 论坛 #79711](https://forum.obsidian.md/t/organizing-research-by-creating-traceable-links-in-the-canvas/79711) | 实测 | 研究组织最佳实践：Canvas 页面链接全链路（证据源→逻辑步骤→结论）可追溯；Metadata Menu 转 frontmatter links |
| [fortelabs PARA](https://fortelabs.com/blog/para/) | 实测 | 四个顶层文件夹：Projects/Areas/Resources/Archives——行动导向分类法 |
| 口述 L984-992（楚门） | 引用 | "口喷→Agent 专业调研"是 AI 原生调研流，市场工具"太通用、商业表现弱" |

### 融合判断（推演）
楚门"口喷→Agent 科学调研→Obsidian 资产"与海外"Canvas 可追溯研究链接"互补：前者解决**调研发起与执行自动化**，后者解决**结论溯源**。一堂科学体系（交叉验证）是楚门流的核心差异化——海外工具（太通用）缺的正是这套方法论内核。

### 补强已有卡清单
| 已有卡 | 补强点 |
|:--|:--|
| `tool-yitang-research-best-practice`（一堂老卡） | 补"口喷→Agent 科学调研→Obsidian 资产"的 AI 原生调研流融合点 |
| `framework-multi-agent-research-architecture` | 补 Canvas 可追溯研究链接作为调研产出去向（forum 79711） |
| `tool-agent-research-pipeline` | 补最佳实践文档=资产包（L1550-1554）落库机制 |

### 新卡候选清单
| 候选卡名（提案） | 类型 | 依据 |
|:--|:--|:--|
| case-truman-ai-native-research-flow（口喷→Agent 科学调研→Obsidian 资产） | case | L984-992 + L1550-1554 + 逐字稿 L343 |

## 子题③ 知识库编码顺序

### 锚点校准
- 口述 L1114-1120：真实项目目录——"一开头的文档都是关于拆解的基本思路；二开头是市场的最佳实践；三开头是建模和来回测评；四开头是记报告来回打磨；五开头是封装成 Y 模型支持的数据包；最后还有一个复盘文档；技能在另外一个目录封装到技能池里"——**数字前缀=工作流顺序**（1 拆解→2 最佳实践→3 建模测评→4 报告打磨→5 封装数据包→复盘+技能池）

### 全网发现
| 来源 | 分级 | 要点 |
|:--|:--|:--|
| [fortelabs PARA](https://fortelabs.com/blog/para/) | 实测 | Projects/Areas/Resources/Archives——按**行动状态**分类（P=有目标有期限，A=长期责任，R=兴趣参考，A=归档） |
| [Johnny Decimal 官网](https://www.johnnydecimal.com/) | 实测 | 十进位编号（area 10-19/20-29…）+ 名称——每项有唯一 ID；Life Admin / Small Business 模板系统 |
| Zettelkasten（卢曼卡片盒） | 推演 | 编号=位置（卡片 ID）+ 链接网络；与 PARA/JD 不同源（本环境未取一手源，标推演） |
| LATCH（信息组织五法） | 推演 | Location/Alpha/Time/Category/Hierarchy——按信息属性分类（未取一手源，标推演） |

### 路线对比
| 体系 | 分类轴 | 适用场景 | 与楚门流关系 |
|:--|:--|:--|:--|
| 楚门数字前缀（L1114-1120） | **业务流顺序** | 单项目全生命周期（拆解→调研→建模→报告→封装） | 本体 |
| PARA | 行动状态 | 个人知识库全局（多项目并行） | 互补（楚门流=项目内，PARA=库顶层） |
| Johnny Decimal | 领域+唯一 ID | 强结构归档（企业/档案） | 互补（楚门流=流水线编号，JD=静态归档） |
| Zettelkasten | 位置+链接 | 学术/创作思考 | 异源（楚门流偏产出导向） |

### 补强已有卡清单
| 已有卡 | 补强点 |
|:--|:--|
| `dk-doc-numbering-business-logic` | 补"数字前缀=工作流顺序"的完整实证（L1114-1120 1-5 段） |
| `concept-structured-naming-as-infrastructure` | 补 PARA/JD 对标（适用边界） |

### 新卡候选清单
| 候选卡名（提案） | 类型 | 依据 |
|:--|:--|:--|
| framework-knowledge-naming-systems-comparison（知识编码体系对比：业务流/PARA/JD/Zettelkasten） | framework | L1114-1120 + PARA/JD 实测 + 推演 |

## 子题④ 上下文+全场景打通（长程研判，2-3 年）

### 锚点校准
- 逐字稿 L419-421：上下文模式——"Obsidian 极其简单，本质上就是本地一堆 markdown 文档，各 Agent 可随时编辑交叉使用……我切换到'上下文模式'：和一堆 Agent 共享一套高质量上下文文档，无需传纸条"
- 逐字稿 L523："AI 和 Agent 工具不太重要，这个文档库才是决定性因素"
- 逐字稿 L679-705：外围数据中心打通——Feishu CLI（飞书搜索/阅读/录音豆）/ YAI CLI（一堂知识库/数据包/Partner）/ Flomo MCP（碎片灵感）；"主线：我不愿意只做一次，我想追求无限复利"
- 逐字稿 L697 + L699 + L703：**WriteLess 假设**——"基于 Openclaw 能不能做一个更加原生的 Obsidian，更适配多 Agent 角色的复杂项目协作，人类尽量减少复制粘贴当胶水，而是由 AI 自动分配、自动路由、自动整理，最终实现完全摆脱人类的自托管"；"Context is Everywhere——日常主动记录，全天候记录，分析，安全脱敏后存入数据库，然后各个场景全部打通"

### 全网发现
| 来源 | 分级 | 要点 |
|:--|:--|:--|
| JSON Canvas 开放格式（jsoncanvas.org） | 实测 | 知识载体开放化（Canvas 文件可被程序读写）——**全场景打通的数据层前提之一** |
| MCP（Model Context Protocol）生态 | 推演/未获取 | modelcontextprotocol.io 本环境不可达；基于已有认知（hermes MCP 集成）：MCP 是 Agent↔外部数据/工具的标准协议——与楚门"CLI/MCP 打通外围"方向一致；具体生态演进无法本环境实证 |
| 楚门锚点（逐字稿 L679-705） | 引用 | 已实践打通 Feishu/YAI/Flomo + 探索智能设备/3D 打印机/数据库接入 |

### 2-3 年演化研判（雷达）
**判断 1：知识管理基础设施将向"Agent 原生"演进，Obsidian（本地 Markdown）是当下最优解但非终局。**
- 证据：楚门 WriteLess 假设（L697）直指"更适配多 Agent 角色复杂项目协作"的原生工具；JSON Canvas 开放格式证明"知识载体可程序化"方向已启动；MCP 生态（推演）提供 Agent 连接外部数据标准协议。
- 中间态（1-2 年）：Obsidian+CLI/MCP 打通 + Agent 直接读写本地 Markdown/JSON Canvas——楚门当前架构就是中间态范本。
- 终局态（2-3 年，推演）：AI 自动分配/路由/整理的自托管知识系统（WriteLess 方向），人类脱离"复制粘贴胶水"角色；Context is Everywhere 成为默认架构（全天候记录+场景全打通）。

**判断 2：KDO 的位置分析。**
- 优势：KDO 已经是"本地 Markdown 优先 + 流程自动化（queue_transition/ingest/pre-submit）+ 多 Agent 协作"的中间态实践者——与楚门架构同构（本地文档库为决定性因素，L523 印证）。
- 缺口（推演）：①Agent 读写外围数据（飞书/Flomo/数据库）的 CLI/MCP 打通尚未系统化（楚门已做 Feishu CLI/YAI CLI/Flomo MCP）；②"人类胶水"环节仍多（跨系统搬运/人工编排）；③Context is Everywhere 的全场景记录层未建。
- 该押什么注（建议，推演）：押"本地文档开放格式（Markdown/JSON Canvas）+ Agent 直连标准协议（MCP/CLI）+ 流程自动化"三件套——这是从中间态到终局态的低风险路径；WriteLess 类原生工具值得跟踪但不必自建（等生态成熟）。

### 产出规格说明
- 本子题为长程雷达项：**产出研判报告（本文）**，不进入卡片生产线，直呈老朱决策参考。

## 6 层交叉验证留痕
| 层 | 验证 |
|:--|:--|
| 来源 | 每子题≥2 来源：锚点（口述/逐字稿）+ 官网（jsoncanvas/fortelabs/johnnydecimal/mermaid）+ 论坛实测（#79711） |
| 时间 | 楚门实践 2026-08（当前）+ JSON Canvas 2024-03（官方公告）+ 论坛帖（社区持续） |
| 逻辑 | 楚门派"口喷→Agent 做图/调研"与 Obsidian 生态"开放格式/插件化"互补不冲突（融合判断） |
| 数据 | 数字锚点全部标行号（L1186-1214/L2220-2266/L984-992/L1550-1554/L3254/L1114-1120/逐字稿 L419-523/L679-705） |
| 反例 | 楚门自己指出"市场调研工具太通用、商业表现弱"（L990）——网络工具非银弹 |
| 行动 | ①②③给补强/新卡清单（王语嫣门禁），④给研判+押注建议（老朱） |

## 待王语嫣门禁
- ①②③补强清单 8 项 + 新卡候选 4 项
- ④研判报告直呈老朱（本报告 §子题④）
