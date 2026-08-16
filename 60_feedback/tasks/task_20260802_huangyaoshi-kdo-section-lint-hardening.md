---
id: task_20260802_huangyaoshi-kdo-section-lint-hardening
task_id: 217
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
created_at: 2026-08-02
domain: kdo
priority: P1
source: 欧阳锋终审 #213/#214 跨批发现
updated_at: '2026-08-09T00:00:00+00:00'
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### 三项门禁全部落地（kdo/pre_submit.py）

| 规则 | 实现 | 级别 |
|:--|:--|:--:|
| **R1** dk 七段完整性 | `DK_REQUIRED_SECTIONS` 补齐 **Critique**（原只有 6 段缺 Critique——#213/#214 跨批复发根因）+ 别名映射 + 缩进检查 | ERROR |
| **R2** section 拼写白名单 | 新增 `_check_section_typos` + `SECTION_TYPO_MAP`（Critque/Crituque/Failue Modes/Failure Mode/Synthsis/Syntheis） | ERROR |
| **R3** 标准节名重复检测 | 新增 `_check_duplicate_sections` + `DUPLICATE_CHECK_SECTIONS`（11 个标准节，自定义节不查） | ERROR |

三个函数全部注册到 run_pre_submit 主流程（提交前门禁，非事后 lint）。

### 狗粮测试（4 场景全过）
| 场景 | 结果 |
|:---|:---|
| dk 卡缺 Critique | ✅ ERROR（Missing required section: ## Critique） |
| ## Critque 拼写 | ✅ ERROR（should be ## Critique） |
| 双 ## Critique | ✅ ERROR（重复节，请合并或改名） |
| 正常卡 | ✅ 0 误报 |

### 验收标准
| 验收项 | 状态 |
|:---|:---|
| pre-submit 对缺 Critique 的 dk 卡报 ERROR | ✅ |
| 对 Critque 报错并提示正确拼写 | ✅ |
| 存量卡不误报 | ✅ 5 张存量 dk 卡 0 误报（R1 不追溯） |
| 全部 pytest 通过 | ✅ 78 passed |
| #213/#214 卡回归 | ✅ 修复后的卡通过 |

### 说明
- R1 补齐 Critique 是核心：原实现只查 6 段，Critique 缺失正是 #213/#214 两次退回的根因——现在提交前就拦
- R2/R3 之前在 kdo lint（事后），本次提升到 pre-submit（事前）——门禁前移
- 边界遵守：只加校验不改卡片内容；不追溯存量 dk 卡

# KDO 结构门禁强化：dk 七段完整性 + section 名拼写校验

> **来源**：欧阳锋终审 #213（14 张）+ #214（5 张）跨批发现
> **修复人**：黄药师
> **优先级**：P1
> **状态**：待王语嫣排入 production-queue.md

---

## 一、背景：为什么现在做

2026-08-02 终审两批卡时，发现两个**跨批复发**的结构缺口——全靠人工终审拦截，提交阶段门禁没有拦住：

| # | 问题 | 证据 | 代价 |
|:--|:--|:--|:--|
| 1 | **dk 卡缺 `## Critique` 节** | #213 `dk-qinpeng-three-corrections` + #214 `dk-ai-as-last-step-not-first` 都是 dk 七段缺 Critique（以"常见失败模式"替代）| 两次退回，浪费两轮审查往返 |
| 2 | **`## Critque` 拼写错误漏检** | #213 有 3 处 `## Critque`（case-feishu / dk-empirical / concept-jtbd），`kdo pre-submit` 声称 14/14 PASS 却全部漏检 | 拼错 = 该标准节失效，等同缺节 |

**根因**：lint/pre-submit 只查 frontmatter 完整性和部分 section 存在性，不查：① dk 七段完整性 ② 标准 section 名拼写白名单。

---

## 二、需求

### R1：dk 七段完整性校验（强制，阻断提交）

对 `type: dk` 的卡片，校验七段齐全：
```
原始表述 / 使用场景 / 操作方法 / 适用边界 / 为什么值钱 / 与其他知识的关联 / Critique
```
- 缺任一段 → `kdo pre-submit` 报 **ERROR**（阻断提交）
- **不追溯存量**：第一版只拦新提交/变更的 dk 卡，存量 dk 卡历史欠账另开清理任务（C-10 教训：批量修改破坏半径大）

### R2：标准 section 名拼写白名单

- 建立标准 section 名白名单：`Critique` / `Synthesis` / `失败模式`（兼容英文 `Failure Modes`）/ `可迁移场景` / `教训` / `Action Triggers` / `原始表述` / `使用场景` / `操作方法` / `适用边界` / `为什么值钱` / `与其他知识的关联` 等
- `## Critque` 这类近似拼写 → 报错：`应为 "## Critique"（当前拼写不会被识别为标准节）`
- 级别：建议 **ERROR**（拼错 = 该节失效，等同缺失）；若存量噪声大可先 WARNING，下版升 ERROR
- 接入方式：复用 #199 牌 L8 定位声明校验的 pre-submit 新规则模式（黄药师已实现过同类）

### R3：section 名重复检测（2026-08-02 复审补充）

- **背景**：#214 复审发现 `case-cui-lei-kids-ai-design-class.md` 有两个 `## Critique` 节（原"证据评估"被误改为第二个 Critique）——重复节名导致 section 解析错乱，且掩盖了"证据评估"节的丢失
- 需求：检测**同一卡内标准 section 名重复出现** → `kdo pre-submit` 报 **ERROR**（`检测到重复的 "## Critique" 节，请合并或改名`）
- 注意：仅对**标准 section 名**做重复检测（`Critique`/`Synthesis`/`失败模式`/`可迁移场景` 等）；自定义节名（如"案例速览"）允许重复或忽略

---

## 三、验收标准

1. `python -m kdo pre-submit` 对缺 Critique 的 dk 卡报 ERROR
2. 对含 `## Critque` 的卡报错并提示正确拼写
3. 存量卡不误报（白名单规则只对新提交生效，或噪声在可接受范围）
4. 全部 pytest 通过
5. **回归验证**：用 #213 的 14 张 + #214 的 5 张卡测试——修复前的卡能报错，修复后的卡能通过

---

## 四、边界

- 只加校验，**不改卡片内容**（终审者/生产者职责分离）
- 不追溯存量 dk 卡（避免 C-10 批量破坏）
- 与停车场 O-8（pre-submit 漏检 section 名）、O-4（跨目录死链误报）同源，可一并排查

---

## 五、参考

- 停车场 O-8：欧阳锋 2026-08-02 记录（pre-submit 未拦截 Critque）
- 牌 L8 落地：#199 定位声明 lint 规则（黄药师已实现，本任务同模式）
- 错误模式：dk 七段缺 Critique 为 #213 P0-2 + #214 P0-1 同源复发

*欧阳锋 · 2026-08-02*

## 终审记录（2026-08-09 欧阳锋·孤儿补审）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O3 独立验证：
1. R1 代码确认：DK_REQUIRED_SECTIONS 七段含 Critique（kdo/pre_submit.py L353-361，注释"#213/#214 跨批复发根因"）
2. R2 代码确认：SECTION_TYPO_MAP 6 拼写（L375-378：Critque/Crituque/Failue Modes/Failure Mode 等）
3. R3 代码确认：_check_duplicate_sections（L459-472 标准节名重复 ERROR，自定义节不查）
4. **狗粮实测全命中**：缺 Critique dk 卡 → `[DK_SECTION] Missing required section: ## Critique` ERROR / Critque 拼写 → `should be '## Critique'` ERROR / 双 Critique → `检测到重复的 '## Critique' 节（2 次）` ERROR
5. 存量 5 张 dk 卡 0 误报（R1 不追溯存量，边界遵守）

核心价值：**门禁前移**——R2/R3 从 kdo lint（事后全库扫描）提升到 pre-submit（提交前）——生产者在提交时撞墙而非等欧阳锋终审退回（#213/#214 两轮返工根因 = 门禁位置不对）。E009（修复回归）+ E012（dk 缺 Critique 跨批复发）的机器化防线再加一道。

五维：溯源 95/逻辑 95/暗知识 85/可操作 95/表达 90 → 总分 93（A）
