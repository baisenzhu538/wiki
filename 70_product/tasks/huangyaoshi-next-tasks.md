# 黄药师后续任务（顺序执行）

## 任务方：黄药师（WSL tmux `claude`）

## 状态

**已完成**：Task 1-20 全部 ✅。P0+P1 整改令全部关闭。379 tests pass（+1 skipped）。
- Batch 1-5: scaffold / clean-transcript / validate / watch / task / graph / RAG / quality-gate / skill-dir / build
- 🔧 P0 整改令（`3026355` llm.py commit + 健康报告更正 + 方法学标注）✅
- 🔧 P1 整改令（`c41bcfe` orphan all-files + `ee7c1ac` llm-check + heading 结构匹配）✅
- 🔧 Batch 7 基础设施债（`2c7c04e` index.md wikilink + 源注册表垃圾清理 + auto-feedback cooldown）✅
- 🍽️ **狗粮任务**：[[70_product/tasks/task-20260524-huangyaoshi-ai-study-dogfood]]（一次性体验式，不影响主要职责）
- 欧阳锋终验：P0+P1 共 6 项整改全部通过。Batch 7 三项全部通过。
- [[60_feedback/assessments/architect-20260523-huanyyaoshi-rectification]] 关闭。

---

## 🔧 P0 整改令（欧阳锋 2026-05-23）→ ✅ 已完成

> 整改来源：[[60_feedback/assessments/architect-20260523-huanyyaoshi-rectification.md]]
> 审查结论：P0 三项全部通过。P1 三项转入下方任务队列。

### P0-1：Commit llm.py ✅

```
3026355 feat: dual-protocol LLM support (Anthropic + OpenAI) and kdo ocr command
```

Anthropic 协议适配 + `_PLACEHOLDER_PATTERNS` + `is_configured()` 修复已入库。4 files, 531 insertions.

### P0-2：更正健康报告 ✅

`wiki-health-analysis-2026-05-23.md` 已更新：
- Critique 缺失率：~~95%~~ → **100%（136/136）**
- Synthesis/wikilinks 缺失率：~~"全部"/94%~~ → **99.3%（135/136）**
- 孤岛卡片：~~111（29.2%）~~ → **196（53.6%）**（独立验证 195，差 1 张可接受）
- LLM 状态：~~401（红）~~ → **绿**（HTTP 200）

### P0-3：标注方法学 ✅

每项指标下已注明统计方法、文件过滤规则、与 v1 差异说明。

### ⚠️ 审查遗留（顺手修）

健康报告 P0 #2 仍写"136 OCR 卡 LLM 重编译：kdo enrich --all --llm"——实际不需要重做 enrich，应改为"补 Critique + Synthesis + wikilinks"。**下次编辑健康报告时顺手改。**

---

## 🔧 P1 整改项 → ✅ 全部完成（2026-05-23 终验通过）

| 整改编号 | 内容 | Commit | 验证 |
|:--:|------|------|:--:|
| P1-4 | LLM 自检 | `ee7c1ac` — `kdo llm-check` + `self-check --llm` | 实测 HTTP 200, 934ms |
| P1-5 | `kdo lint` 覆盖全文件 | `c41bcfe` — `find_orphans_vault()` 原生扫描 | 6 tests pass |
| P1-6 | heading 结构匹配 | `ee7c1ac` — `_extract_section()` 匹配 `## [Critique]` 方括号格式 | 379 tests pass |

---

## Batch 7：基础设施债清偿（P0，顺序执行）

> 以下问题自 2026-05-22 洪七公 cross-review 起已确认，至今未修。都是已有明确修复方案的工单，不需要设计。

### Task 18：index.md 反斜杠 wikilink 修复（P0，~30min）

**问题**：`30_wiki/index.md` 中 391 个链接全部使用 `[text](file)` 格式而非 `[[wikilink]]`。更深层的问题是 kdo 的 index builder（`search_index.py`）在 Windows 上调用 `os.path` 产出反斜杠路径，导致 Graph RAG 检索时链接断裂。

**改什么**：
1. `kdo/index` 或 `search_index.py` 中，路径拼接改用 `pathlib` 或手动 `replace('\\', '/')`
2. 重建 index.md：`kdo index --rebuild`，验证所有链接为正斜杠 `[[wikilink]]` 格式
3. 不产生新断链（现有 wikilink 目标页均存在）

**验收**：
- `grep '\\\\' 30_wiki/index.md` 返回空（无反斜杠）
- `grep '\[\[' 30_wiki/index.md | wc -l` ≥ 300（wikilink 格式）
- Graph RAG 重建后 `kdo graph stats` 节点/边数无明显下降

**估时**：~30min

---

### Task 19：源注册表垃圾清理（P0，~20min）

**问题**：`90_control/source-registry.yaml` 含 211 条垃圾条目（title ≤4 字符或 title=`---`），占总条目 38.5%。来源为 OCR 批处理中 PaddleOCR 误识的分隔线、录音碎片。

**改什么**：
1. 脚本清理：删除 title 为 `---`、纯数字、≤4 字符无意义碎片的条目
2. 增加 `kdo ingest` 前置过滤：标题最小长度 ≥8 字符，拒收 YAML 分隔符（`---`）
3. Dry-run 模式先预览，确认无误再写入

**验收**：
- 清理后注册表条目数从 548 降到 ~340
- 无 `---` 条目残留
- `kdo ingest` 对短标题/分隔符自动拒收

**估时**：~20min

---

### Task 20：auto-feedback 洪水清理（P0，~15min）

**问题**：`60_feedback/auto/` 含 1,770 个自动反馈文件，绝大多数为 `unenriched-wiki-page` 正常状态触发的噪声。淹没有效反馈信号（assessments/ 仅 19 个文件）。

**改什么**：
1. 清理 24h 内新卡片的 `unenriched-wiki-page` 自动反馈（已 enriched 的卡不应再触发）
2. 反馈逻辑增加冷却期：同一卡片 24h 内不重复触发同类型反馈
3. 或：直接关闭 `unenriched-wiki-page` 自动反馈（status 枚举已足够追踪）

**验收**：
- `60_feedback/auto/` 文件数从 1,770 降到 <500
- 无有效信号被误删（人工抽检 10 个被删文件）
- `kdo feedback` 手动反馈不受影响

**估时**：~15min

---

## Batch 8：A 类脚本化修复（P0，顺序执行）

> **背景**：老顽童在自我检讨中识别出三类 A 类基础设施债——全部可脚本化，全部是黄药师的主场。这是让工厂自己修自己的活。

### Task 21：断链批量修复（P0，~45min）

**问题**：全库约 113 个 broken wikilinks。根因：批量重命名/移动卡片时未同步更新引用。

**改什么**：
1. `kdo lint --broken-links --json` 输出全量断链清单（源文件 → 断链目标）
2. 如果目标存在但路径不对 → 自动修正
3. 如果目标不存在 → 标记为 `⚠️ 需要人工判断`（不自动删除）

**验收**：
- `kdo lint` broken wikilinks 从 ~113 降到 <10
- 不产生假修复（把断链改成错误的目标页）
- 3 个修复案例可复现

**估时**：~45min

---

### Task 22：frontmatter 批量补全（P0，~30min）

**问题**：约 271 张卡缺少 frontmatter 关键字段（id/type/status 三缺一或多缺）。

**改什么**：
1. `kdo lint --missing-frontmatter --json` 输出缺失清单
2. 自动补全规则：
   - `type`：从文件名推断（ocr- → concept，无前缀 → concept 默认）
   - `status`：有 Critique+Synthesis → enriched，缺 → draft
   - `id`：从文件名 slug 生成
3. `--dry-run` 先预览，不直接写入

**验收**：
- `kdo lint --missing-frontmatter` 缺失数从 ~271 降到 <20
- 自动推断的 type 准确率 >95%
- 不覆盖已有正确字段

**估时**：~30min

---

### Task 23：新旧格式统一（P0，~20min）

**问题**：约 166 张卡存在新旧格式并存（如同时有 `## Critique` 和 `## Constraints & Boundaries`；`## dont-use` 和 `### 不要用的场景`）。

**改什么**：
1. `kdo lint --mixed-format --json` 检测同卡并存两套标题
2. 统一规则：保留 v1.5 格式（`## Critique` / `### 不要用的场景`），删除旧格式空节
3. 如果旧节有实质内容但新节为空 → 内容迁移而不是简单删除

**验收**：
- 新旧格式并存卡从 ~166 降到 <10
- 无内容丢失（旧节有实质内容时已迁移）
- `kdo validate --v15 --all` PASS 数提升

**估时**：~20min

---

## 完成标志（更新）

| 序号 | 任务 | 验证 |
|------|------|------|
| 1-14 | KDO 核心 + Batch 1-5 | ✅ |
| P0-1/2/3 | llm.py commit + 报告更正 + 方法学 | ✅ |
| P1-4/5/6 | llm-check + orphan all-files + heading 匹配 | ✅ |
| 18 | index.md wikilink 修复 | ✅ |
| 19 | 源注册表垃圾清理 | ✅ |
| 20 | auto-feedback 洪水清理 | ✅ |
| 21 | 断链批量修复 | ⏳ Sprint 4 |
| 22 | frontmatter 批量补全 | ⏳ Sprint 4 |
| 23 | 新旧格式统一 | ⏳ Sprint 4 |
| 🍽️ | AI学习域狗粮任务 | ✅ A |

---

## 🔥 Sprint 2-5：补传送带（欧阳锋 2026-05-24 批准）

> **提案来源**：[[huangyaoshi-sprint2-5-conveyor-belt-proposal]]（黄药师自提）→ 欧阳锋审查裁定。
> **核心判断**：工位齐全但工位之间没有传送带。过去一年建工位，下一阶段连工位。
> **原则**：先闭环再自动化。不建全自动流水线，先让手动路径丝滑。

---

### ⚡ Sprint 1-2：已自主完成（未 commit）

黄药师在狗粮任务中发现问题后，不等工单直接修了。以下变更在 KDO repo 工作区：

| 修复 | 文件 | 对应发现 |
|:---|:---|:---|
| `section_content` regex：`(?=^##\|\Z)` → `(?=^##\s\|\Z)` | `validation.py` L22 | 所有文章 validate word count 修复 |
| `kdo ingest --title` / `--kind` 参数 | `cli.py` + `ingestion.py` | ASR 稿可预标注，不再产垃圾标题 |
| OCR 失败 fallback 提示 | （待确认） | MinerU → PaddleOCR 提示 |
| ingest 成功确认打印 | `ingestion.py` | `✓ source_id → wiki: path — "title"` |
| `import sys` 遗漏修复 | （待确认） | 运行时 crash 修复 |

> ⚠️ **第一步：commit 以上变更。** `git status` = 3 files modified。commit message: `fix: Sprint 2 — section_content regex, ingest --title/--kind, ocr fallback`

---

### Sprint 3：传送带 — Produce 预填（P0，~6h）

> **欧阳锋裁定**：批准。这是老顽童产能瓶颈的直接解锁——produce 现在 = touch 模板，100% 手写。修完后 produce 产出的是有骨架的初稿。

| # | 任务 | 复杂度 | 估时 |
|:--:|------|:--:|:--:|
| S3-1 | **produce 读 wiki 卡片 → 预填 Body Structure** | 中 | ~2.5h |
| S3-2 | **produce 自动填 Source Lineage 表** | 低 | ~1h |
| S3-3 | **produce 后自动跑 `validate --advisory`** | 低 | ~20min |
| S3-4 | **validate 以文件 frontmatter 为唯一真相源** | 中 | ~1.5h |
| S3-5 | **artifact-registry.yaml 降级为可选导出** | 中 | ~45min |

#### S3-1：produce 读 wiki → 预填 Body Structure

**问题**：`kdo produce content/article` 只生成纯 TODO 骨架，不读 wiki、不预填结构性信息。

**改什么**：
- produce article 时，从 `--topic` 关键词查 wiki 卡片 → 提取 Reusable Knowledge 填入 Body Structure
- Draft 不自动写（那是 LLM 或人的活），但骨架信息不该让人手动复制

**验收**：`kdo produce content/article --topic "AI Native"` → Body Structure 含 RK 要点。幂等，不覆盖已有内容。≥3 tests。

#### S3-2：produce 自动填 Source Lineage

**改什么**：从 state.json 或 source registry 查 source → 自动填写 Source Lineage 表（source_id + trust_level + key claim used 占位）

**验收**：produce 完成后 Source Lineage 表已预填 source_id 和 trust_level。≥2 tests。

#### S3-3：produce → validate 快捷循环

**改什么**：`kdo produce` 完成后自动运行 `kdo validate --advisory` 预检，列出缺失字段（不 BLOCK）

**验收**：produce 完看到 advisory 结果。`--advisory` exit 0。≥2 tests。

#### S3-4：validate 以 frontmatter 为真相源

**问题**：state.json / registry / frontmatter 三源分裂。改了文件 frontmatter → validate 仍 fail。

**改什么**：
- validate 优先读文件 frontmatter 中的 source_refs/wiki_refs
- 与 state.json 不一致时 → 以文件为准，WARN + 自动同步
- 不破坏现有 validate 逻辑

**验收**：改 frontmatter → validate 读到新数据。不一致时 WARN。≥3 tests。

#### S3-5：artifact-registry.yaml 降级

**改什么**：registry 不再是 validate 强制数据源，降级为可选手动导出（`kdo registry export`）。删除 validate 中对 registry 的强制读取。

**验收**：registry 不存在时 validate 不报错。≥2 tests。

---

### Sprint 4：数据卫生批修（P0，~2h）

> **欧阳锋裁定**：批准。技术债，越拖修复成本越高。**但必须在 Sprint 3 完成后做**——S3-4 的 frontmatter 逻辑变更可能影响批修脚本的写入行为。

| # | 任务 | 来源 | 复杂度 | 估时 |
|:--:|------|:---|:--:|:--:|
| S4-1 | **~113 个 broken wikilinks 修复** | Task 21 | 低 | ~45min |
| S4-2 | **~271 张卡缺失 frontmatter 补全** | Task 22 | 低 | ~30min |
| S4-3 | **~166 张卡新旧格式统一** | Task 23 | 低 | ~20min |

> ⚠️ **C-10 铁律**：单卡 dry-run → 单卡 write → validator 验证 → 人审核 → THEN 批量。不能因为"只是脚本"就跳过。

**S4-1**：`kdo lint --broken-links --json` → 目标存在但路径不对 → 自动修正。目标不存在 → 标记 ⚠️。验收：broken wikilinks <10。

**S4-2**：`kdo lint --missing-frontmatter --json` → 自动补全 type/status/id。`--dry-run` 先预览。验收：缺失数 <20。

**S4-3**：`kdo lint --mixed-format --json` → 统一为 v1.5 格式。旧节有内容 → 迁移不删除。验收：并存卡 <10。

---

### Sprint 5：Validate → Ship 闭环（暂缓 ⏸️）

> **欧阳锋裁定**：暂缓。涉及 gate.py 和 validate 两套系统的架构合并，风险高于收益。等 Sprint 3 体验沉淀后再定方案。

| # | 任务 | 暂缓原因 |
|:--:|------|:---|
| S5-1 | 统一 gate.py 和 validate | 架构重构，需先理清两套系统的检查项差异 |
| S5-2 | validate 通过后自动更新 status → "ready" | 依赖 S3-4（真相源）完成 |
| S5-3 | `kdo ship --dry-run` | 合理但非阻塞 |

---

### 暂缓（需讨论）

| 主题 | 复杂度 | 决策点 |
|:---|:--:|:---|
| **clean-transcript 会话式规则** | 高 | 纯正则够吗？需要 LLM 分段？——黄药师自判正确，先不做 |
| 多模态视觉理解管线 | 高 | 洪七公职责还是黄药师建基础设施？——另议 |
| 端到端 pipeline 编排 | 高 | Sprint 2-5 完成后再议 |

---

### 顺手修（穿插做，~10min）

| # | 任务 | 估时 |
|:--:|------|:--:|
| 🧹 | 清理 3 张狗粮垃圾 source（`90fb730a`/`dd8a0fe6`/`e290738e`）+ 对应 wiki 骨架 | 5min |
| 🎬 | `kdo video ship` 同步更新 `stages.ship` 字典（段王爷发现，见文件末尾 Task 17 附录） | 5min |

---

## 完成标志（更新）

| 序号 | 任务 | Sprint | 验证 |
|------|------|:--:|------|
| 1-20 | KDO 核心 + Batch 1-7 | — | ✅ |
| P0-1/2/3 | llm.py + 报告更正 + 方法学 | — | ✅ |
| P1-4/5/6 | llm-check + orphan + heading | — | ✅ |
| 🍽️ | AI学习域狗粮任务 | — | ✅ A |
| S1-2 | regex + --title/--kind + ocr fallback | S1-2 | ✅ |
| S3-1 | produce 读 wiki → Body Structure | S3 | ✅ |
| S3-2 | produce 自动填 Source Lineage | S3 | ✅ |
| S3-3 | produce → validate 快捷循环 | S3 | ✅ |
| S3-4 | validate 以 frontmatter 为真相源 | S3 | ✅ |
| S3-5 | artifact-registry 降级 | S3 | ✅ |
| S4-1 | 断链批量修复（~113个） | S4 | ✅ |
| S4-2 | frontmatter 批量补全（~271张） | S4 | ✅ |
| S4-3 | 新旧格式统一（~166张） | S4 | ✅ |
| 🧹 | 清理 3 张垃圾 source | 随手 | ✅ |
| 🎬 | video ship stages sync | 随手 | ✅ |
| S5 | Validate→Ship 闭环 | — | ⏸️ 暂缓 |
| S6 | query --stats/--aggregate + inbox --count/--search + prompt + label | S6 | ✅ commit 150c58b |
| S7 | produce --stats + flywheel status + 数据质量门三层 | S7 | ✅ commit d6a38dd |

---



---

### 🔍 欧阳锋终验（2026-05-24 Batch 7）

**提交**：`2c7c04e` — 单 commits 覆盖三任务，64 行增 / 4 行删。

| 任务 | 验收 | 评级 | 备注 |
|:---|:--:|:--:|:---|
| 18: index.md wikilink | ✅ | A | 391 `[[wikilink]]`，0 反斜杠。`as_posix()` + `--rebuild` |
| 19: 源注册表垃圾 | ✅ | A- | 337 条目（-211）。preventive filter `<8` chars 已加。dry-run 未实现但可接受 |
| 20: auto-feedback | ✅ | A | 112 文件（-1,658）。24h cooldown 逻辑正确 |
| pytest | ✅ | 379 passed，1 skipped，0 回归 | |

**总评**：A。增量修复，未过度工程。三个任务都在一个方向上：从源头阻止垃圾进入系统，而非事后清理。

**审计发现**：剩余 112 个 auto-feedback 文件大部分是 `near-duplicate-wiki-pages`（非 `unenriched-wiki-page`），与 5 张卡相关（`深度调研集群方法论` 35次、`结构化面试打分卡` 12次等）。是类似洪水问题的相邻类型，但不在此批次范围内。建议后续工单追踪。

---



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

---

## 🔧 Batch 6：kdo video CLI（P1，~2h）

> **触发**：洪七公独自扛视频生产 7 步，session 爆了后降级为"HTML 幻灯片→录屏"，产出不可用。
> **根因**：没有工具强制执行阶段门禁，没有中间产物持久化机制。
> **设计文档**：[[40_outputs/capabilities/workflows/video-production-flow.md]]
> **角色分工**：老顽童→脚本 / 洪七公→分镜+画面 / 工具链→音频+组装 / 欧阳锋→阶段审查

### Task 15：`kdo video` 四个子命令（P1，~2h）

`kdo video` 是一个轻量编排器——它自己不渲染、不生成音频。它负责：建项目骨架、验证阶段产物、调外部工具组装。

#### 子命令 1：`kdo video init <article_path> [--title] [--slug]`

```
入参：一篇已存在的文章 .md 路径
出参：视频项目目录 + _spec.md + 阶段模板文件
```

**行为**：
1. 读取文章 frontmatter（artifact_id, title, source_refs, wiki_refs）
2. 在 `40_outputs/content/videos/<slug>/` 下创建目录结构：
   ```
   <slug>/
   ├── _spec.md                 # 项目 manifest
   ├── 01-script.md             # Stage 1 模板（预填文章摘要+5段占位）
   ├── 02-storyboard.md         # Stage 2 模板（预填分镜表头+style guide 占位）
   ├── frames/                  # Stage 3 输出目录（空）
   ├── audio/                   # Stage 4 输出目录（空）
   └── draft/                   # Stage 5 输出目录（空）
   ```
3. `_spec.md` 内容：
   ```yaml
   ---
   video_id: "<slug>_<timestamp>"
   title: "<article title>"
   source_article: "<article relative path>"
   source_refs: [<from article frontmatter>]
   wiki_refs: [<from article frontmatter>]
   status: init
   created_at: <timestamp>
   stages:
     script: pending
     storyboard: pending
     frames: pending
     audio: pending
     compose: pending
   ---
   ```
4. `01-script.md` 预填：文章标题 + 5 段占位符（## Segment 1-5）+ 文章 Key Takeaways 作为参考
5. `02-storyboard.md` 预填：Style Guide 占位（colors/font/animation/brand 四项）+ 空分镜表

**验收**：
- 目录结构完整（6 entries）
- `_spec.md` 可解析 YAML，source_article 路径正确
- `01-script.md` 包含 5 个 `## Segment N` 占位符
- `02-storyboard.md` 包含 Style Guide 和分镜表头
- 幂等：对同一 article 重复 init 不覆盖已有内容（检查 `_spec.md` 存在则提示 "already initialized"）

#### 子命令 2：`kdo video validate <video_dir> [--stage script|storyboard|frames|audio|compose|all]`

```
入参：视频项目目录路径
出参：终端报告 + 退出码（0=pass, 1=fail, 2=warn）
```

**三层门禁**（与 workflow 对齐）：

| Layer | Checks | When | Exit Code on Fail |
|:-----:|--------|------|:--:|
| L1 | `_spec.md` 存在且可解析；`01-script.md` 非空非 TODO；`02-storyboard.md` 非空非 TODO；`frames/` 目录存在；`audio/` 目录存在 | --stage all | 1 |
| L2 | script 含 5 个 `## Segment`；storyboard 含 Style Guide 四个字段；frames 数量 ≥ script 中 speaking points 数；frame 文件名匹配 `segment_N_frame_FFF` | --stage storyboard / frames | 1 |
| L3 | source_article 路径可解析；storyboard 中颜色值为合法 hex；帧文件均为 ≥ 1920×1080 | --stage all | 2 (warn only) |

**注意**：L1/L2 = BLOCK（exit 1），L3 = WARN（exit 2）。--stage 参数限定检查范围。

**验收**：
- L1 通过刚 init 的项目（空模板不算 fail——只检查文件存在，不检查内容质量）
- L2 在 storyboard 缺 Style Guide 时 fail
- L3 在 source_article 路径断裂时 warn
- ≥3 tests

#### 子命令 3：`kdo video render --audio <video_dir>`

```
入参：已完成 script + storyboard 的项目目录
出参：audio/segment_N.mp3 × 5
```

**行为**：
1. 读取 `01-script.md` → 提取每个 segment 的 speaking text
2. 读取 `02-storyboard.md` → 提取每个 segment 的目标时长
3. 调用外部 TTS 工具（设计为可配置插件，默认调用 edge-tts 或系统 TTS）
4. 每段生成一个 mp3，时长控制在 storyboard 标注的 ±5%
5. 生成低音量 BGM（可选，--bgm 开关）

**外部依赖**：
- TTS：edge-tts（pip install edge-tts）或系统内置 TTS
- BGM：无版权素材库路径或静音（--no-bgm）

**验收**：
- 5 个 segment_*.mp3 生成，每个非空（>10KB）
- 每段时长在 storyboard 标注 ±10% 内
- ≥1 test（mock TTS 输出）

#### 子命令 4：`kdo video render --compose <video_dir>`

```
入参：frames/* + audio/* + storyboard.md
出参：draft/draft.mp4
```

**行为**：
1. 读取 `02-storyboard.md` → 提取 frame→duration 映射
2. 用 ffmpeg 将每个 segment 的画面帧 + 音频合成为 segment clip
3. 拼接 5 个 segment clips → 输出 `draft/draft.mp4`
4. 格式：H.264 1080p 30fps，AAC 192kbps

**外部依赖**：ffmpeg（系统已安装）

**验收**：
- `draft/draft.mp4` 生成，1920×1080，时长 8-10 min
- ffmpeg 未安装时打印清晰错误信息（非 traceback）
- ≥1 test（mock ffmpeg 或检查命令拼接正确性）

#### 子命令 5：`kdo video ship <video_dir> [--channel]`

```
入参：validate 通过的项目目录
出参：final/final.mp4 + delivery record
```

**行为**：
1. 验证 `kdo video validate` 通过
2. Copy `draft/draft.mp4` → `final/final.mp4`
3. 更新 `_spec.md` status → shipped
4. 写入 `50_delivery/published/<video_id>.yaml`

**验收**：
- `final/final.mp4` 存在
- `_spec.md` status = shipped
- delivery record 写入

### 不做什么

- **不做** GUI 或 Web 界面
- **不做** 实时预览或播放器
- **不做** 视频托管或 CDN 分发
- **不做** TTS 引擎本身（调用外部工具）
- **不做** 画面渲染本身（洪七公负责）
- **不做** 分镜表 GUI 编辑器

### 总体验收

- `kdo video --help` 输出清晰
- 5 个子命令各自 --help 输出清晰
- `kdo video init <article> && kdo video validate <dir>` 跑通完整 init→validate 链路
- ≥5 new tests（init×2 + validate×2 + render mock×1）
- 不破坏现有 286 tests
- 错误信息始终打印到 stderr，正常输出到 stdout
- 所有路径操作使用 pathlib，兼容 Windows 反斜杠路径

### 完成标志

- [x] 5 个子命令全部可用
- [x] 286 + 24 new tests = 310 tests，全部 pass（1 skipped 系已有）
- [x] `e8b9265` feat: kdo video CLI — init/validate/render/ship
- [x] 用洪七公产出的 KDO quickstart 文章做首次 init 实测：创建成功，validate 返回 WARN（正确——空模板）
- [x] 欧阳锋审查：待审查

---

## 🔧 Task 16：`kdo video render` 修两个缺口（P0，~1h）

> **触发**：视频试点 Gate 3 通过，洪七公准备执行 `kdo video render --audio` 时实测报错：`No speaking points found.` 根因两个缺口。

### 缺口 1：只认 bullet point 格式，不认散文体脚本

**位置**：`commands/video.py` `_render_audio()` L426

**现状**：
```python
points = re.findall(r'^- (.+)', seg, re.MULTILINE)
speaking_text = ' '.join(points)
```

这只匹配 `- 说话内容` 格式。老顽童的十指讲香脚本是散文体（段落+`--` 停顿标记），不含任何 bullet point。结果是 `points = []` → `speaking_text = ''` → 所有 segment 都被跳过。

**改法**：提取逻辑改为双路径 fallback：

```python
# Path A: 尝试提取 bullet points
points = re.findall(r'^- (.+)', seg, re.MULTILINE)
if points:
    speaking_text = ' '.join(points)
else:
    # Path B: 从散文体中提取——跳过 frontmatter、标题、Visual hint、空行、分隔线
    # 保留以中文/英文开头的内容行（去掉 `--` 停顿标记）
    prose_lines = []
    for line in seg.split('\n'):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('[') or line.startswith('>') or line.startswith('---') or line == '`':
            continue
        # 去停顿标记但保留停顿节奏（-- → 逗号停顿）
        line = re.sub(r'\s*--\s*', '，', line)
        prose_lines.append(line)
    speaking_text = ' '.join(prose_lines)
```

或者更简单的方式：如果存在 `## Full Text` 段，直接按 segment 边界拆分 Full Text 段的内容。

**验收**：对散文体脚本运行 `render --audio`，5 个 segment 各自提取到 >100 字的 speaking text。

### 缺口 2：TTS 未集成

**位置**：`commands/video.py` `_render_audio()` L431-435

**现状**：提取文本后写入 `.txt` 文件，打印 `TTS not yet integrated`。不生成任何 mp3。

**改法**：
1. 装依赖：`pip install edge-tts`（纯 Python，零系统依赖，支持中文）
2. 在 `_render_audio()` 中调用 `edge-tts`：

```python
import asyncio
import subprocess

async def _tts_segment(text, out_path, voice='zh-CN-XiaoxiaoNeural'):
    """Generate MP3 from Chinese text using edge-tts."""
    cmd = ['edge-tts', '--voice', voice, '--text', text, '--write-media', str(out_path)]
    proc = await asyncio.create_subprocess_exec(*cmd)
    await proc.wait()
    return proc.returncode == 0

def _generate_audio(segments, audio_dir):
    """同步封装：为每个 segment 调 edge-tts 生成 mp3。"""
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        for seg_title, text, out_path in segments:
            ok = loop.run_until_complete(_tts_segment(text, out_path))
            if not ok:
                print(f"  ⚠ TTS failed for {seg_title}")
            else:
                print(f"  {out_path.name} ← {len(text)} chars")
    finally:
        loop.close()
```

3. edge-tts 未安装时的处理：try import / 检查命令是否存在，不存在则打印清晰错误信息 + 安装指令，不扔 traceback。

**验收**：
- 对试点项目运行 `render --audio`，`audio/` 下生成 5 个 .mp3（每个 >10KB）
- edge-tts 未安装时打印 `edge-tts not found. Install: pip install edge-tts` 并 exit 1
- 不破坏现有 310 tests

### 总体验收

| # | 验收项 | 判定方式 |
|:--:|------|------|
| 1 | 散文体脚本提取到 speaking text（≥100 字/段） | 对试点项目 dry-run，5 段均有非空输出 |
| 2 | `audio/` 下生成 5 个 .mp3 | 文件存在 + >10KB |
| 3 | edge-tts 缺失时清晰报错不崩溃 | 临时 uninstall edge-tts 后运行 |
| 4 | `kdo video validate --stage audio` 通过 | exit 0 |
| 5 | ≥3 new tests（散文体提取 + mock TTS + edge-tts 缺失） | pytest 全绿，不破 310 |
| 6 | 对视频试点项目实测：`render --audio` → `render --compose` → `draft/draft.mp4` 可播放 | 最终产物存在 + ffprobe 可读 |

### 🛑 门禁（通过标准，缺一不可）

| # | 门禁项 | 判定方式 |
|:--:|------|------|
| 1 | 散文体脚本不报 `No speaking points found` | 实测试点项目 |
| 2 | 5 个 segment 各生成 >10KB mp3 | 文件大小检查 |
| 3 | pytest ≥3 new tests 全绿，不破 310 | 终端 |
| 4 | `kdo video validate --stage audio` PASS | exit 0 |

### 🛑 审批

提报格式：
```
黄药师 [Task 16 kdo video render 修复] 已完成
路径：C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\commands\video.py
测试：pytest tests/test_video.py -v
```

审批人：欧阳锋。审批结果：
- **通过** → 通知洪七公执行 7h 渲染合成
- **修改** → 标注具体缺口 + 期望，黄药师修改后重新提报

### 🛑 节点

```
视频试点流水线
    │
🛑 GATE 3 ⏳ 等待用户终检 40 帧画面
    │
洪七公 7h 渲染合成 ← 阻塞在此。等你修完 render 模块才能执行
    │
洪七公 7g timing → GATE 4
```

你在 Gate 3 和 7h 之间。上游 = Gate 3（等待用户终检），下游 = 洪七公 7h（等你工具就绪）。**这是视频管线唯一的工具链阻塞点。**

---

## Task 17：kdo video render 两个遗留缺陷（~1h，P1）

**触发**：洪七公 7g 音画对位实测发现两个工具问题。Gate 4 审查（欧阳锋，2026-05-20）要求写入 backlog 修复。

### Bug 1：Seg 5 TTS 生成异常时长

**症状**：`kdo video render --audio` 生成的 `Segment_5` 音频 558.5s（9.3min），远超脚本标注 ~1min。洪七公已备份异常音频至 `audio/segments_backup/`。全文 TTS（`full_audio.mp3` 487.9s）正常。

**待排查方向**：
- `_extract_speaking_text()` 对 Seg 5 的 prose 提取结果是否正确——Seg 5 脚本全文（含 `## Full Text` 节）是否被整段当成了 segment 正文
- 分段正则 `re.split(r'\n(?=## Segment \d)', script_text)` 是否正确切割 Seg 5 边界
- `## Full Text` 节是否被误识别为 `## Segment 5` 的一部分

**复现步骤**：
```bash
kdo video render --audio "40_outputs/content/videos/knowledge-delivery-os-快速上手指南把散落知识变成可交付资产"
```
检查 `audio/Segment_5_*.mp3` 的 ffprobe duration。

### Bug 2：compose 缺少动态帧时长分配

**症状**：`kdo video render --compose` 均匀分配帧时长（500.1s / 40 帧 = 12.2s/帧），不考虑每段口播实际时长。导致帧切换与口播内容不对位。

**期望行为**：按 segment 口播音频时长比例分配帧时长。例：Seg 1 口播 ~45s，占全文 9%，则 Seg 1 的 10 帧应分配 ~4.5s/帧。

**改什么**：
1. `_render_compose()` 增加 `--segment-durations` 可选参数
2. 未指定 `--segment-durations` 时，自动解析 `audio/` 下各段 mp3 的 ffprobe duration，按比例分配
3. 如果 audio 不存在，fallback 到均匀分配（当前行为）+ 打印 warning

### 🛑 门禁（通过标准）

| # | 门禁项 | 判定方式 |
|:--:|------|------|
| 1 | Seg 5 音频时长 = 脚本标注（~60s，非 558.5s） | 对试点项目 dry-run |
| 2 | compose 帧时长按 audio 比例分配（非均匀 12.2s） | 检查 ffmpeg concat 文件中每帧 duration 不相等 |
| 3 | `--segment-durations` 未指定 + audio 不存在时 fallback 均匀分配 + warning | 测试覆盖 |
| 4 | pytest ≥3 new tests，不破 317 | 终端 |

### 🛑 审批

提报格式：
```
黄药师 [Task 17 kdo video render 遗留缺陷] 已完成
路径：C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\commands\video.py
测试：pytest tests/test_video.py -v
```

审批人：欧阳锋。审批结果：
- **通过** → 关闭。试点视频用当前 draft.mp4 先 ship，本修复用于后续视频项目
- **修改** → 标注具体缺口 + 期望，修改后重新提报

### 🛑 节点

```
视频试点管线
    │
🛑 GATE 4 ⚠️ 条件通过（洪七公补 timing.md）
    │
洪七公 timing.md 修正 → ship
    │
黄药师 Task 17 ← 你在 backlog。不阻塞当前试点 ship，修完后用于后续视频项目
```

**优先级 P1（非阻塞）**。当前试点 draft.mp4 已可用（500.1s, H.264/AAC），先 ship 跑通流程。本 Task 的修复用于下一个视频项目的自动化管线。

---

## 顺手修：`kdo video ship` 同步更新 stages 字典（~5min，P3）

> ⚠️ 已并入 Sprint 2-5"顺手修"清单。详见上方 [[#顺手修-穿插做-10min]]。
