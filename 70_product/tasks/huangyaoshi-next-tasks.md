# 黄药师后续任务（顺序执行）

## 任务方：黄药师（WSL tmux `claude`）

## 状态

**已完成**：Task 1-12 全部 ✅。282 tests pass（+16 since Task 10）。
- Batch 1: scaffold + clean-transcript + validate --watch
- Batch 2: watch 解耦 + scaffold 修正 + task 自动化 + graph rebuild + graph stats
- Batch 3: Graph RAG 深化 + Quality Gate v2
- Batch 4: Skill 审查流水线 + KDO Build 系统

**🔥 紧急**：Task 13-14 — scaffold 攻击者检测盲区 + 空 H4 校验。71 张卡受损。见 [[#🔥 Batch 5：scaffold 紧急修复]]。

**⚠️ 欧阳锋审查（2026-05-19）**：代码质量 A，但全部未 commit。详见 [[#🔍 欧阳锋审查（2026-05-19）]]

---

## Batch 2：修 bonus 问题 + 增量索引 + 统计面板

### Task 4：`kdo watch` 依赖解耦（P1，~30min）

**问题**：`watch.py` 硬 import `watchdog`，`pyproject.toml` 加了 `watchdog>=4.0`。违反 KDO 零运行时依赖原则。且 `kdo watch` 零测试。

**改什么**：

1. `watch.py` 顶部改为可选 import：
```python
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    _HAS_WATCHDOG = True
except ImportError:
    _HAS_WATCHDOG = False
```

2. `cmd_watch` 启动时检查 `_HAS_WATCHDOG`，未安装时打印 "kdo watch requires watchdog. Install: pip install watchdog" 并 return 1

3. `pyproject.toml` 移除 `watchdog` 依赖

4. `test_watch.py` 新增 ≥3 tests：
   - `test_watch_missing_watchdog_returns_1`（mock ImportError）
   - `test_watch_inbox_not_found`
   - `test_health_check_runs`

**验收**：pytest 全绿。未装 watchdog 时 `kdo watch` 不崩溃。

---

### Task 5：scaffold 插入位置修正（P2，~20min）

**问题**：scaffold 目前追加到文件末尾。Critique 应在 `## Constraints & Boundaries` 和 `## Synthesis` 之间，不是文末。

**改什么**：`_scaffold_card` 写入逻辑改为智能插入：
- 缺 Critique → 在 `## Constraints & Boundaries` 节后、`## Synthesis` 节前插入
- 缺 不要用场景 → 在 `## Synthesis` 节内、`### 关联卡片` 后插入  
- 缺 Action Triggers → 追加到 `## Synthesis` 节后（本节之后，已有的 AT 或文末之前）
- 如果找不到锚点 → fallback 到文末追加（当前行为）

**验收**：对一张已有 Critique+Synthesis 但缺不要用的卡 scaffold，验证不要用场景插在了正确位置。对已有全部节的卡 scaffold 返回 None 不变。

---

### Task 6：`kdo task` 自动化 + dashboard（P0，~1.5h）

**问题**：当前手工编辑 Markdown 任务文件交接——欧阳锋手动改状态表、Agent 手动读文件找任务、完成/审查后无人更新。已导致设计域文件明明是存在的却被误报缺失。用户要求立即自动化。

**改什么**：

1. 任务文件加 YAML frontmatter（结构化状态层，不改 Markdown brief 内容）：
```yaml
---
tasks:
  - id: hys-5
    title: scaffold 插入位置修正
    status: done
    assigned_to: 黄药师
    priority: P2
---
```

2. `kdo task` 新增子命令：
   - `kdo task dashboard` → 扫描所有任务文件 frontmatter，生成 `70_product/tasks/dashboard.md`
   - `kdo task mine [--assignee <name>]` → 列出当前 agent 的待办（按优先级+依赖排序）
   - `kdo task done <id>` → 标记任务完成，更新 frontmatter
   - `kdo task review <id> --verdict A [--notes "..."]` → 欧阳锋记录审查结论
   - `kdo task verify` → 扫描所有任务引用的文件/工具是否存在，报告缺失

3. 现有 `cmd_task()` 扩展：支持 YAML frontmatter 读写（读任务文件 → 解析 frontmatter → 更新字段 → 写回）

**验收**：
- `kdo task dashboard` 生成 dashboard.md，内容与两个任务文件状态一致
- `kdo task done hys-5` 后，对应任务文件的 frontmatter 状态变为 done
- `kdo task verify` 对缺失文件报 warning
- pytest ≥5 新 test cases
- 不破坏现有 `kdo task` CRUD 功能（state.json 模式保持兼容）

---

### Task 7：Graph RAG 增量更新（P2，~1-2h）

**问题**：当前 `kdo graph rebuild` 全量重建。老顽童每天新增/修改 3-5 张卡，全量重建浪费 30s+。改为增量：只处理变更的卡。

**改什么**：`kdo graph rebuild --incremental`

1. 记录上次 rebuild 的时间戳到 `.kdo/graph_state.json`
2. 增量模式：只扫描 `mtime > last_rebuild` 的 `.md` 文件
3. 对新增/修改的卡：更新 LightRAG 索引中对应 entity + chunks + relations
4. 对删除的卡：从索引中移除
5. `--incremental` 为默认行为，`--full` 强制全量

**技术方案**：利用 LightRAG 的 `ainsert` / `adelete_by_doc_id` API。如果 LightRAG 版本不支持增量 → 改为增量检测 + 全量重建（至少省了"哪些卡要重建"的判断）。

**验收**：
- 修改 1 张卡后 `kdo graph rebuild --incremental` 耗时 <5s（全量重建 ~30s）
- 索引中该卡的内容已更新（冒烟：`kdo graph query "新加的内容关键词"` 能命中）
- `--full` 行为不变

---

### Task 8：`kdo graph stats`（P3，~30min）

**问题**：Graph RAG 索引建完后没有健康检查手段。不知道 entity 数、chunk 数、relation 数、最后一次 rebuild 时间。

**改什么**：`kdo graph stats [--json]`

输出：
```
Graph RAG Index
  Entities:   226
  Chunks:     721
  Relations:  1252
  Nodes:      406
  Edges:      1252
  Last build: 2026-05-19 15:30
  Status:     OK
```

数据来源：LightRAG 内部存储（`kg_db` / `vector_db`）。如果索引不存在 → `Status: NOT BUILT`。

**验收**：`kdo graph stats` 输出合法。`--json` 输出可管道。

---

## 完成标志

| 序号 | 任务 | 验证 |
|------|------|------|
| 1 | scaffold | ✅ A，17 tests |
| 2 | clean-transcript | ✅ A，7 tests |
| 3 | validate --watch | ✅ A，纯标准库 |
| 4 | `kdo watch` 依赖解耦 | ✅ 4 tests, watchdog 可选, pyproject.toml 已清理 |
| 5 | scaffold 插入位置修正 | ✅ Critique→CB/Synthesis间, 不要用→关联卡片后, AT→Synthesis后 |
| 6 | `kdo task` 自动化 + dashboard | ✅ 6 tests, dashboard/mine/done/review/verify, 向后兼容 |
| 7 | graph rebuild --incremental | ✅ 5 tests, --full + incremental, graph_state.json 追踪 |
| 8 | `kdo graph stats` | ✅ 4 tests, --json, NOT BUILT 处理 |
| 9 | Graph RAG 深化（查询+推理+监控） | ✅ 图遍历查询 + 跨域路径发现 + 索引自动健康检查, 9 tests |
| 10 | Quality Gate v2（文章+skill 校验） | ✅ validate 扩展到 article/skill 类型, 9 tests |
| 11 | Skill 审查流水线 | ✅ `kdo validate --skill-dir` + batch 扫描 + L1 5节检查, 9 tests |
| 12 | KDO Build 系统 | ✅ `kdo build` + CHANGELOG + build_state.json, 11 tests |
| 13 | 🔥 scaffold 检测盲区 | `_count_external_attacks` 识别旧格式，dry-run 不误伤 |
| 14 | 空 H4 校验 | H4 下 <100 字不计入，pytest ≥3 new tests |

---

## 🔍 欧阳锋审查（2026-05-19）


---

## Batch 3：Graph RAG 深化 + 质量门扩展

### Task 9：Graph RAG 深化（P1，~2h）

**问题**：当前 Graph RAG 能检索但缺少图遍历能力。查询"A 和 B 之间有什么关联路径"时只能靠 chunk 相似度，无法沿图边遍历发现间接关系。索引健康监控只有 `kdo graph stats` 的静态快照。

**改什么**：

1. **图遍历查询**：`kdo graph path <entity_a> <entity_b>` — 沿关系边 BFS 发现最短路径，输出实体→关系→实体的路径链
2. **跨域推理增强**：在 `kdo query` 结果中标注跨域桥接卡（如 `yt-concept-weapon-arsenal`），高亮不同 domain 之间的间接关联
3. **索引自动健康检查**：`kdo graph stats` 加 `--health` 模式——检查 entity 数是否下降 >20%、孤立节点占比、chunk 覆盖率，异常时报警

**验收**：
- `kdo graph path Kahneman Mintzberg` 输出至少一条通过共享卡片的关系路径
- `kdo query "..."` 结果中跨域关联被标注
- `kdo graph stats --health` 输出健康评分 + 异常项
- pytest ≥6 新 tests

---

### Task 10：Quality Gate v2 — 扩展到 article + skill（P1，~1.5h）

**问题**：`kdo validate --v15` 只校验 concept/tool/framework 卡片。洪七公产出 skill、段王爷产出 article，没有自动化质量检查。这直接阻碍他们进入工作流。

**改什么**：

1. `kdo validate --article <path>` — 文章质量门：
   - 目标读者明确（`## 目标读者` 节）
   - 核心论点 ≤3 句可提取
   - 来源可追溯（每段关键声明有 `source_ref` 或脚注）
   - 结构完整（摘要→正文→结论→反馈入口）

2. `kdo validate --skill <path>` — Skill 质量门：
   - Purpose / When to Use / When NOT to Use 三节齐全
   - Protocol 可执行（≥3 个可照做的步骤）
   - 至少一个真实 Example
   - 边界清晰（When NOT to Use 非空）

3. `kdo validate --all` 自动检测类型并路由到对应门禁

**验收**：
- `kdo validate --skill 40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md` 返回 PASS
- `kdo validate --article <一篇老顽童产出的文章>` 返回结构化检查结果
- `--all` 覆盖三种类型
- pytest ≥5 新 tests
- 不破坏现有 `--v15` 卡片校验

---

---

## Batch 4：审查支撑 + Build 系统

### Task 11：`kdo validate` skill 审查流水线（P1，~1h）

**背景**：Task 10 建好了 `kdo validate --skill`，但老顽童产出的设计域 S1+S2 skill 需要入库到 `40_outputs/capabilities/skills/` 后欧阳锋才能审查。当前流程：老顽童产出 → 放错路径 → 欧阳锋发现 → 让老顽童搬。应该在入库环节就自动校验。

**改什么**：

1. `kdo validate --skill <path>` 增加 batch 模式：`kdo validate --skill-dir <dir>` 扫描整个目录下所有 SKILL.md
2. 输出统一格式（PASS/FAIL/WARN + 缺失节清单），和 `--v15` 输出风格一致
3. 集成到 `kdo validate --all`（当前已支持 concept/article/skill 三种类型，确认 skill 路由正常）
4. 增加 L1 结构检查：SKILL.md 必须有 Purpose / When to Use / When NOT to Use / Protocol / Examples 五节

**验收**：
- `kdo validate --skill-dir 40_outputs/capabilities/skills/` 扫描全部 skill 输出汇总
- 对老顽童即将入库的 3 个设计域 skill 能跑通
- pytest ≥3 新 tests

**估时**：~1h

---

### Task 12：KDO Build 系统（P2，~2h）

**背景**：当前 `kdo backup` 只做源码 zip 快照，没有版本号管理、没有 CHANGELOG 生成、没有跨会话的 build 记录。KDO CLI 已经迭代了 scaffold/validate/watch/clean-transcript/graph/task 等多个模块，需要正式的 build 管线。

**改什么**：

1. `kdo build` 命令：
   - `kdo build --version <semver>` — 打版本标签，生成 CHANGELOG（从 commit 历史自动提取）
   - `kdo build --check` — dry-run，检查工作空间完整性（所有产出文件路径有效、引用不悬空）
   - `kdo build --release` — 完整发布：check → backup → tag → changelog

2. CHANGELOG 生成规则：
   - 从 `git log` 提取 feat/fix/refactor 前缀的 commit
   - 按模块分组（scaffold, validate, graph, task, clean-transcript）
   - 输出到 `70_product/releases/CHANGELOG.md`

3. `.kdo/build_state.json` 记录：当前版本号、上次 build 时间、pytest 结果、模块清单

**验收**：
- `kdo build --check` 通过
- `kdo build --version 0.2.0` 生成 CHANGELOG
- `.kdo/build_state.json` 记录完整
- pytest ≥5 新 tests
- 不破坏现有 `kdo backup`

**估时**：~2h

---

## 原则

1. **顺序执行**，不做完上一个不开下一个
2. **每完成一个 → 跑 pytest 全量**，确认无回归
3. **每完成一个 → 更新本文件的完成标志**
4. **完工后通知欧阳锋审查**

---

## Task 1：`kdo scaffold`（P0，现在就开工）

### 工单

[[70_product/tasks/kdo-scaffold-v15.md]]

### 为什么先做

`kdo validate --v15 --upgrade-plan` 诊断了 89 张 FAILED 卡每张缺什么，但老顽童修卡时每张都要从空白页开始搭 Critique/不要用/AT 的框架——定格式、查学者、写占位是重复劳动。scaffold 自动化这一步，老顽童拿到的是"框架已搭好、学者方向已建议"的卡，只填内容。

### 核心做什么

`kdo scaffold --card <id>` 读卡→诊断缺失→追加 TODO 骨架。不覆盖已有内容。

```
kdo scaffold --batch A --write    # 全信号缺失高引卡，第一批开工
kdo scaffold --card yt-pitch-metaphor  # 单卡 dry-run
```

智能部分：攻击者建议——扫描同 domain 下已有 Critique 的卡，提取攻击者名→去重→按频次排序→推荐 top 3。

### 验收

- [ ] 对缺 Critique / 缺不要用 / 缺 AT 的卡分别正确生成骨架
- [ ] `--batch A/B/C/D/E` 分组正确
- [ ] 攻击者建议不推荐该卡已有的攻击者
- [ ] `--write` 写入后原卡已有内容完整保留
- [ ] 对 205 张真实卡运行无崩溃
- [ ] pytest ≥8 新 test cases，全绿

### 估时

~200-250 行代码，~2-3 小时。

---

## Task 2：设计域转录稿清理工具（P1）

### 背景

`00_inbox/design/` 有两份 AI 设计培训的语音转文字稿（月白老师分享），是 ASR 实时输出——口语化严重、有填充词、分段破碎、有回音/网络问题导致的乱码。老顽童做设计域编译前，需要先清理。

手动清理两份长文太慢。黄药师做一个自动化预处理工具。

### 要做什么

`kdo clean-transcript <file>` 或集成到 `kdo ingest --clean`：

1. **去噪**：删除口头禅（"呃"、"就是"、"那个"、"有没有回音"、"现在还有回音吗"）、重复的互动询问（"有回音吗"在文中出现多次）、网络中断提示
2. **分段**：识别主题转换信号（"第二个..."、"下一个..."、"我们来说..."、"总结一下"），按主题切为段落
3. **标点修复**：ASR 输出无标点或标点错误，基于语义停顿插入句号/逗号
4. **术语标注**：识别 AI 设计术语（GAN、VAE、Diffusion、GPT-2o、Nano Banana、巨米4.0），用 backtick 包裹或斜体
5. **输出**：清理后的 `.md` 文件到 `10_raw/sources/` 或原地 `00_inbox/design/cleaned/`

### 技术方案（三种，从轻到重）

| 方案 | 实现 | 优点 | 缺点 |
|------|------|------|------|
| **A. 规则引擎** | Python 正则 + 关键词词典。去噪=正则删除匹配行。分段=检测主题转换词。术语=术语表匹配 | 轻量、无依赖、可控 | 规则覆盖不全，边缘 case 多 |
| **B. LLM 批处理** | 调 DeepSeek API，分块送入 LLM，用 system prompt 指定清理规则。每块 ~2000 tokens | 质量最高，处理口语化/ASR 错误效果好 | 需 API key，有成本（~$0.1-0.3/全文），速度慢 |
| **C. 混合** | 规则引擎做粗清理（去噪+分段），LLM 做精修（标点修复+术语标注+语义纠错） | 兼顾速度和质量 | 架构复杂度最高 |

**建议方案 A（规则引擎）MVP 先跑通**。两份转录稿的噪音模式相对固定（同一平台、同一 speaker），规则覆盖率高。如果效果不够再加 LLM 精修。

### CLI

```bash
kdo clean-transcript 00_inbox/design/AI设计-AI设计基础01.txt --output 10_raw/sources/
kdo clean-transcript 00_inbox/design/ --output 10_raw/sources/  # 批量
kdo clean-transcript ... --method llm   # LLM 精修模式（如果实现）
```

### 验收

- [ ] 去噪：口头禅删除率 >80%（人工抽检 50 行）
- [ ] 分段：主题边界准确，不把同一主题切成两段
- [ ] 术语：GAN/VAE/Diffusion/GPT-2o/Nano Banana 正确标注
- [ ] 输出是合法 Markdown
- [ ] 清理后文件行数 < 原文 70%（去除了噪音行）
- [ ] 不丢失案例细节（Leo 案例必须完整保留）
- [ ] pytest ≥3 新 test cases

### 估时

~100-150 行（规则引擎方案），~1-2 小时。

---

## Task 3：`kdo validate --v15 --watch`（P2）

### 背景

老顽童修 89 张卡时，每修完一张需要手动跑 `kdo validate --v15 --card <id>` 看是否通过。更高效的方式：启动 watch 模式，文件保存时自动重检目标卡片，实时反馈。

### 要做什么

`kdo validate --v15 --watch [--domain <d>]`：

1. 用 `watchdog`（或纯 Python `os.stat` 轮询）监听 `30_wiki/concepts/` 目录
2. 检测到 `.md` 文件变更（防抖 2 秒）→ 自动对该文件运行 `validate --v15 --card`
3. 输出结果到终端（pass/fail/warn + 缺失信号详情）
4. `Ctrl+C` 退出

### 技术方案

**纯 Python 标准库方案**（零依赖，与 KDO 原则一致）：
- `os.stat` 轮询 + `time.sleep(1)`，不需要 watchdog 第三方库
- 防抖：2 秒内同一文件的多次变更合并为一次验证
- 输出用简单的 PASS/FAIL/WARN 前缀，可加 `--json` 输出

### CLI

```bash
kdo validate --v15 --watch                     # 监听全库
kdo validate --v15 --watch --domain yitang     # 只监听指定域
kdo validate --v15 --watch --json              # JSON 输出（给 CI/tmux status）
```

### 验收

- [ ] 修改一张卡并保存 → 2 秒内自动验证该卡
- [ ] 防抖正常：连续保存 3 次只触发 1 次验证
- [ ] `Ctrl+C` 正常退出
- [ ] 不监听非 `.md` 文件和 `.obsidian/` 目录
- [ ] `--domain` 过滤正常
- [ ] 全量 pytest 无回归（不阻塞 CI——watch 测试用 subprocess 超时）

### 估时

~80-100 行，~1 小时。

---

## 完成标志

| 序号 | 任务 | 工单 | 验证 |
|------|------|------|------|
| 1 | `kdo scaffold` | [[70_product/tasks/kdo-scaffold-v15.md]] | pytest ≥8 新 tests 全绿 + 对 205 张卡无崩溃 + 欧阳锋审查 |
| 2 | 转录稿清理工具 | 本文件 Task 2 | pytest ≥3 新 tests 全绿 + 清理两份设计转录稿验收通过 + 欧阳锋审查 |
| 3 | `kdo validate --v15 --watch` | 本文件 Task 3 | 修改卡自动重检 + 防抖正常 + 无回归 + 欧阳锋审查 |

---

## 相关

- [[70_product/tasks/validate-v15-upgrade-plan.md]] — scaffold 的前置工单
- [[70_product/tasks/quality-gate-automation-v15.md]] — validate v15 本身
- [[70_product/tasks/laowantong-next-tasks.md]] — 老顽童队列（scaffold 的消费者、设计域编译器）
- [[70_product/tasks/kdo-infrastructure-backlog-proposal.md]] — 原始 backlog

---

## 🔍 欧阳锋审查（2026-05-19）

### Task 11：`kdo validate --skill-dir` — A

- `cmd_validate_skill_dir` 递归扫描 SKILL.md → batch 检查 → PASS/FAIL/WARN 汇总
- L1 结构检查：Purpose / When to Use / When NOT to Use / Protocol / Example 五段全覆盖
- 实测：`ai-design-fundamentals` → PASS（Protocol 12 steps, all sections present）
- 测试：TestSkillQualityGate(4) + TestValidateSkillDir(4) + TestSkillL1Structure(1) + TestValidateAllAutoDetect(2) = 11 tests

### Task 12：KDO Build 系统 — A

- `build --check` 检查 9 目录 + state.json + graph + backups
- `build --version <semver>` 生成 CHANGELOG（git log feat/fix/refactor 按模块分组）+ build_state.json
- `build --release` 顺序：check → backup → tag → changelog
- 实测：`kdo build --check` → PASS
- 测试：11 tests (check/changelog/module guess/version state)

### ⚠️ 全部未 commit

```
未暂存修改: cli.py, quality.py, validation.py, workspace.py, etc. (12 files)
未跟踪新增: commands/build.py, commands/cards.py, commands/transcript.py,
              tests/test_build.py, tests/test_graph.py, tests/test_transcript.py,
              tests/test_validate_v15.py, tests/test_watch.py (8 files)
```

**行动**：黄药师在 KDO repo 目录执行：
```bash
cd "C:\Users\Administrator\Knowledge Delivery OS 0.0.1"
git add -A
git commit -m "feat: Task 11+12 — skill-dir validation + KDO build system"
```

---

## 🔥 Batch 5：scaffold 紧急修复（P0，~45min）

> **事故**：老顽童 2026-05-20 跑 `kdo scaffold --batch B --write`，71 张卡攻击者内容被清空。老顽童自检确认 scaffold 共三个缺陷叠加。详见 [[70_product/tasks/dashboard#🔧 黄药师 Task 13-14：scaffold 紧急修复]]。

### Task 13：修复 scaffold 三个缺陷（P0，~45min）

**缺陷 1：检测盲区**（`_count_external_attacks`）

`_count_external_attacks` (quality.py L152) 只查 `## Critique` H2 节。旧格式卡把攻击者放在 `## Framework Gallery` 下：

```markdown
## Framework Gallery

### 外部攻击：Taleb的"随机性" + Snowden的"复杂域"

**Nassim Nicholas Taleb**……（完整论证）
**Dave Snowden**……（完整论证）
```

`_find_section(sections, "critique")` 返回 None → `atk_count = 0` → scaffold 以为缺攻击者。

**缺陷 2：重复插入**

当卡片已有 `## Critique` 但 scaffold 判定 `atk_count < atk_needed` 时，`_insert_critique` 会在 `## Synthesis` 前插入**第二个** `## Critique` 块，导致一张卡出现双 Critique 节。老顽童发现 6 张卡有此问题。

**缺陷 3：内容丢弃**

`_insert_critique` 插入新块时，旧攻击者正文未被保留——插入操作实际上覆盖/替换了相邻的旧内容，而非纯粹追加。这是 71 张卡内容丢失的直接根因。

**改什么**：

1. `_count_external_attacks` 增加 fallback：
   - 先走现有逻辑（找 `## Critique`）
   - 若未找到，检查 `## Framework Gallery` 下的 `### 外部攻击*` H3 子节
   - 在子节内容中匹配 `**学者名**` 粗体格式，提取学者名
2. `_insert_critique` 增加**幂等检查**：若卡片已有 `## Critique` H2 节，只追加缺失的 H4 攻击者（不重复创建整个 Critique 块）
3. `_insert_critique` 改为**纯追加模式**：绝不对已有内容做替换/覆盖，只在 `## Synthesis` 前或文末插入新块

### Task 14：空 H4 校验（P1，~15min）

**问题**：validator 只检查 H4 标题存在，不检查标题下是否有实质内容。空 `#### Scholar：批判` + 空行 = 通过。

**改什么**：H4 计数逻辑增加内容检查——从 H4 标题行到下一个 H4/H3/H2 之间，提取非空纯文本（跳过 `> [!TODO]` 和 `[TODO]` 等占位符），要求 ≥100 字符才算有效攻击者。

### 验收

- [ ] `_count_external_attacks` 能识别 `## Framework Gallery` 下 `### 外部攻击*` 中的 `**学者名**` 格式
- [ ] 卡片已有 `## Critique` 时，`_insert_critique` 不重复创建第二个 Critique 块
- [ ] `_insert_critique` 纯追加，不覆盖/替换已有内容
- [ ] 在 `yt-entrepreneur-key-hypotheses` 原始版本（commit `99787ad`）上 dry-run scaffold 返回 `None`（无需 scaffold）
- [ ] 空 H4（下面 <100 字正文）不计入攻击者计数
- [ ] pytest 新增 ≥5 tests：旧格式识别 / 双 Critique 幂等 / 内容保留 / 空 H4 拒绝 / dry-run 不误伤
- [ ] 不破坏现有 282 tests
