---
title: "复盘：AI基本功Feature思维 · 全链路生产"
date: 2026-08-09
author: 王语嫣
domain: ai-basic
source_person: Truman（一堂CEO）
pipeline: 洪七公OCR/VLM → 双王语嫣诊断（Claude+DeepSeek） → 全网交叉验证 → 欧阳锋裁决 → 老顽童生产 → 教练Agent试点 → 自我迭代闭环
total_cards: 12（4框架+3案例+2dk+1bridge+1agent-spec+1dk自我迭代坑）
---

# 复盘：AI基本功Feature思维全链路生产

> 本轮特殊之处：**不仅是知识卡片生产，还孵化了KDO第一个"自我迭代闭环"**——教练Agent在#252试点中证明 Agent+KDO+终端权限 = Agent能自己修自己，并沉淀为共享skill。

## 一、时间线

| 节点 | 动作 | 角色 | 产出 |
|:---|:---|:---|:---|
| 08-07 21:00 | Truman直播《AI学习·Feature思维解析》上下 | 外部 | 口述3428行 |
| 08-08 | 素材入00_inbox；洪七公OCR/VLM 69次调用 | 洪七公 | 34图92.8%识别 |
| 08-08 | 欧阳锋出任务编排建议书（审查v2.1） | 欧阳锋 | 补链优先裁定+洞察3双轨 |
| 08-08 | Codex/CodeBuddy出建议书 | 外部Agent | 元Feature+四大场景=编排操作系统 |
| 08-08 | 飞书王语嫣（我DeepSeek）全量诊断 | 王语嫣 | 3428行通读+六层+九层+Wiki碰撞+F-EQG自检 → `diag_20260808_AI基本功_Feature思维_全量诊断.md` |
| 08-08 | Claude王语嫣出任务单#248-#252 | Claude | W0-W4四波编排 |
| 08-08 | #248周期表结构化 | 老顽童 | 96→100 Feature JSON（欧阳锋终审C1-C4） |
| 08-08 | #249框架层4张 | 老顽童 | FAIL→修6项→PASS A- |
| 08-08 | #250案例+dk 5张 | 老顽童 | FAIL→修5项→PASS B+ |
| 08-08 | #251 bridge+agent-spec | 老顽童+黄药师 | 先行产物A-（queued） |
| 08-08 | 我审计Claude 12张卡 | 王语嫣（DeepSeek） | 全量PASS+4项patch（#259：5项patch） |
| 08-09 | #252消费端试点（教练Agent自主执行） | 教练Agent | 点菜5 Feature全有效，verified 18→22 |
| 08-09 | 教练Agent自我迭代 | 教练Agent | 三连坑→dk卡→MOC注册→skill更新 |
| 08-09 | 我沉淀agent-self-iteration skill | 王语嫣 | KDO shared注册+README索引+双轨对齐 |

## 二、四角色协作评价

### 洪七公
- **做得好的**：VLM 600px黄金切分标准（100%成功率）——方法论本身沉淀了；34图92.8%识别率高
- **待改进**：OCR口径矛盾（建议书写"10中18小待处理"vs VLM写"34图全识别"）——两份文件不一致，欧阳锋抓出后确认。下次自检交付物一致性

### 王语嫣（本人·DeepSeek版）
- **做得好的**：
  - 全量通读3428行——不依赖洪七公/欧阳锋建议书独立形成判断（F-EQG-014达标）
  - 跨Agent审计：12张卡全量读完，框架正确性验证通过后做增量patch而非重写（F-EQG-021实战）
  - 发现Claude版遗漏的Q&A后半段暗知识5项（教育哲学/AI推平均分/预测属性）
- **踩的坑**：
  - **search_files搜30_wiki超时多次**——一直默默降级terminal find，没想过沉淀（老顽童corrections点破后才知道根因是cwd）
  - 我在Schema讨论时追求13字段精细Schema，Claude选了7字段最小集——**被欧阳锋验证"菜单够用即可"更务实**。下次先问"消费端要什么"再定Schema
- **下次改进**：
  - 工具坑→立即走自我迭代闭环（已沉淀为skill）
  - Schema设计→最小可行优先，字段可后续补充而非一次设计全

### 欧阳锋
- **做得好的**：
  - 审查方法论v2.1——O3独立验证（不采信提交报告），逐行溯源核验（L534-590四要素逐字命中）
  - FAIL/退回修复质量高——6项修复清单每条有实测证据，非凑数
  - 洞察3（双轨Feature体系）被全流程采纳——bridge卡完美解决术语歧义
- **待改进**：队列状态同步（#248终审时发现队列仍是queued——E012镜像问题），已现场提醒

### 老顽童
- **做得好的**：
  - 周期表100 Feature提取质量高——96个全部带id/name/layer/dimension/purpose/scenario/case_ref/verified八字段，79个未验证的诚实标注
  - 修复响应快：W1 6项+W2 5项全部当日闭环
  - **主动写corrections诊断自己的config**（cwd/approvals/编码）——本轮最大惊喜之一
- **待改进**：编号写死（"96个"应100）、死链（framework-一堂-刻意练习）、引号改写（招商日报L78）——细节溯源纪律需加强（已在审查中抓出）

### 教练Agent（本轮新角色）
- **做得好的**：在#252试点中自主完成了"发现问题→诊断→修复→沉淀→注册→下次绕开"全闭环——三连坑（审批/cwd/检索规则）全部自己诊断修复，沉淀dk卡+MOC注册
- **待改进**：dk卡draft状态未提审（reviewed_by: 待审）——需欧阳锋补审

## 三、方法论沉淀

### 本轮验证有效的方法

| 方法 | 效果 |
|:---|:---|
| 补链优先于新建 | 已有4张同主题卡→升级/merge而非重复建——W0-3升级tool-Truman-Feature，W3对账inventory |
| 周期表最小Schema | 7字段（id/name/layer/dimension/purpose/scenario/case_ref/verified）——够用且可消费 |
| 双轨Feature体系 | quality-gate(12 lint) vs capability(100解题)——bridge卡一劳永逸解决术语撞车 |
| 跨Agent诊断接收四步 | 通读→框架正确性→深度→可操作性→增量patch——不重写全量 |
| 消费端点菜协议 | 真实任务→kdo feature pick --n 5→逐Feature测试→回填verified |
| 自我迭代闭环 | 发现问题→诊断配置层→修复→沉淀→注册——教练Agent案例+王语嫣落地 |

### 本轮发现的新方法/教训

| 发现 | 教训 | 编码 |
|:---|:---|:---|
| 配置层问题伪装成"命令坏了" | 先查approvals.mode/cwd/allowlist/文档规则，再怀疑命令本身 | F-EQG新条目→agent-self-iteration skill |
| search_files超时根因是cwd | session cwd=/home时递归跨/mnt/c全树巨慢——显式传绝对路径 | 已入entry-quality-gate故障表 |
| approvals.mode=manual在网关必死 | 无确认UI→代码命令60s超时被杀——网关场景选smart | dk-agent-access-kdo-pitfalls |
| Schema从简 | 7字段最小集通过验证——13字段精细Schema是过度设计 | 复盘教训 |
| 自我迭代是Agent能力 | Agent+KDO+终端权限=Agent能自己修自己——需沉淀为共享skill | agent-self-iteration skill |

### 与外部工具的对比（如有）

| 维度 | 外部Agent（教练） | KDO 本轮 |
|:---|:---|:---|
| 工具坑处理 | 自己改config（切smart） | 王语嫣沉淀skill+老顽童写corrections请求修复——分工不同但闭环一致 |
| 知识沉淀 | dk卡+自己skill | dk卡+共享skill（agent-self-iteration）——比教练多一层KDO shared注册 |
| 复用路径 | 查自己skill | 查MOC+dk卡+skill——多入口但靠README索引对齐 |

## 四、当前状态

### 已入库
- `framework-truman-feature-thinking-core`（A，4要素+T/F+五学派）
- `framework-truman-feature-layered-system`（A-，L0-L5+分层自洽+发现过程诚实标注）
- `concept-truman-feature-four-scenarios`（A-，四场景+AI推平均分警示）
- `concept-truman-feature-six-stages`（A-，六阶段+KDO生命周期同构）
- `case-truman-ai-image-workflow-evolution`（A，3h→日产30-40张）
- `case-truman-investment-daily-report`（A，30→90分）
- `case-truman-temperature-parameter`（A，2万→2千）
- `dk-feature-not-learned-but-used`（A-，用会的+教育哲学）
- `dk-key-hypothesis-still-hope`（B+，还有关键假设就还有机会）
- `bridge-dual-track-feature-system`（A-，quality-gate vs capability）
- `agent-spec-basic-skills-coach`（A-，基本功教练）
- `dk-agent-access-kdo-pitfalls`（draft待审，外部Agent接入三连坑）
- `10_raw/sources/feature-periodic-table-v0.8.json`（100 Feature周期表）

### 跨域桥接
| 新卡 | 桥接到 | 理由 |
|:---|:---|:---|
| feature-thinking-core | concept-ai-triangle（AI三角·基本功） | 基本功模块的具体展开 |
| layered-system | ai-collaboration skills族 | BITCOE≈L1/dev≈L3/gan≈元层 |
| 四大场景 | decision域（关键假设/OSCAR） | 解题地图=假设思维AI版 |
| 双轨bridge | concept-kdo-feature-registry | 两类Feature体系分工 |
| agent-self-iteration skill | dk-agent-access-kdo-pitfalls | 案例→方法论skill |

### 待完成
- #251 W3/W4部署层（黄药师能力中台接入，#256）
- #252消费端试点A选项（真实业务任务验证——B选项KDO内部任务有自指偏差）
- dk-agent-access-kdo-pitfalls提审（欧阳锋）
- coach-session-review skill与dk卡双轨验证
- 老顽童corrections 4项修复（cwd固定wiki/allowlist/queue编码）待欧阳锋/黄药师执行

## 五、关键数字

| 指标 | 数值 |
|:---|:---|
| 素材总量 | 口述3428行 + 笔记271行 + 34张PPT图 |
| 产出卡片 | 12张（4框架+3案例+2dk+1bridge+1agent-spec+1dk坑） |
| 周期表 | 100 Feature（L0:3/L1:14/L2:34/L3:14/L4:18/L5:13；A:27/B:11/C:27/D:31） |
| 发现修正 | W1 FAIL→6项修复→A-；W2 FAIL→5项修复→B+；#259 5项patch |
| 审计 | 12卡全量PASS，4项增量patch（后+1=5项） |
| 角色参与 | 洪七公/欧阳锋/双王语嫣（Claude+DeepSeek）/老顽童/黄药师/教练Agent（新） |
| 生产周期 | 08-07直播 → 08-09复盘 = 2天全链路 |
| 新方法论 | 3项（自我迭代闭环/双轨Feature/消费端点菜协议） |
| 新skill | 1个（agent-self-iteration，已注册KDO shared） |

---

*王语嫣（DeepSeek-V4）· 2026-08-09 · 全链路复盘*
*双路径保存：Desktop/agent复盘/王语嫣/ + wiki/60_feedback/diagnosis/*
