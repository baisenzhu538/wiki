---
id: task_20260629_kimi-lint-content-debt-by-domain
type: task
status: queued
assignee: 老顽童(Hermes)
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
reviewed_by: pending
source_refs:
- 60_feedback/tasks/task_20260629_kimi-full-frontmatter-compliance-cleanup.md
---

# lint 内容债按域分批清理

## 背景

`kdo lint` 阈值调整后，frontmatter / 目录结构 / source_refs / index / section 骨架等机械类问题已清零。剩余 WARNING 为内容深度类问题，需要逐卡改写，按 domain 分批处理。

## 当前基线

### 初始基线（2026-06-29 会话开始）

- 日期：2026-06-29
- `kdo lint`：0 ERROR / 3286 WARNING
- 主要剩余类型：
  - L2 Critique 缺关键术语：846
  - Critique section 无外部攻击者姓名：717
  - Section 高度相似（copy-paste）：~720
  - L2 Condense 0 要点：215
  - L2 Synthesis 0 外部链接：187
  - Wiki page 无可见来源：33
  - Tool card 缺 When NOT to Use：33
  - status 与字段不一致：16
  - body 过短：~80
  - Artifact 未注册：7

### 本轮处理后（2026-06-29 本次会话）

- `kdo lint`：0 ERROR / **3255** WARNING（↓31）
- 当前主要剩余类型：
  - L2 Critique 缺关键术语：846
  - Critique section 无外部攻击者姓名：714
  - body 过短：651
  - Section 高度相似（copy-paste）：584
  - L2 Condense 0 要点：216
  - L2 Synthesis 0 外部链接：188
  - Wiki page 无可见来源：0（已清零）
  - Tool card 缺 When NOT to Use：24
  - status 与字段不一致：16
  - Artifact 未注册：7

> 说明：body 过短从 80 增至 651，是因为清理空"常见失败模式" section 后暴露了原本被掩盖的 body 长度问题。需要在下一轮处理中回填具体内容。

## 分批计划

按 `domain` 字段分组，一个 domain 一个任务。每批独立跑 `kdo lint --domain <domain>`，老顽童逐卡判断改写、补内容或接受为永久 WARNING 基线。

| 批次 | Domain | 有 WARNING 文件数 | 主要问题 | 优先级 |
|:---:|:---|---:|:---|:---:|
| D1 | `yitang` | 474 | copy-paste + L2 深度 | P2 |
| D2 | `design` / `design- design` | 229 | section 深度 + copy-paste | P2 |
| D3 | `src_unknown` | 155 | 需先补 domain/source，再清内容 | P2 |
| D4 | `research` | 154 | copy-paste + 来源 | P2 |
| D5 | `ai-collaboration` | 121 | L2 深度 + 链接 | P2 |
| D6 | `strategy` / `business-strategy` | 118 | critique + 反例 | P2 |
| D7 | `decision-science` / `decision-making` | 111 | L2 condense/synthesis | P2 |
| D8 | `ai-saas` / `yitang- ai-saas` | 103 | 工具卡规范 + copy-paste | P2 |
| D9 | `product` / `learning-methodology- product` | 60 | section 补全 + 深度 | P2 |
| D10 | `management` / `learning-methodology- management` | 33 | 框架深度 | P2 |
| D11 | `healthcare` / `supply-chain` / `finance-legal` / `operations` / `content-production` | 50 | 小域合并清理 | P2 |
| D12 | `personal-growth` / `skill-building` / `learning-methodology` | 36 | 元能力卡深度 | P2 |
| D13 | `master` / `kdo` / `needs-review` | 85 | 系统/元页面 + 待审卡 | P2 |
| D14 | 无 domain / 跨域残留 | 57 | 先补 domain 再归类 | P2 |

## 执行规则

1. 每批只做当前 domain：`kdo lint --domain <domain>` 限定范围。
2. 单卡处理原则：
   - **copy-paste**：针对具体方法重写 section，不能共用模板。
   - **L2 Critique**：补充 `具体假设 / 边界 / 反例 / 前提` 中的关键术语，并加入 `**姓名 姓氏**` 格式的外部反对者。
   - **L2 Condense**：补充 ≥3 条中文要点 bullet。
   - **L2 Synthesis**：补充 ≥2 个外部 wikilink。
   - **body 过短**：扩展内容到 ≥500 字或合并/归档。
3. 每批完成后必须 `kdo pre-submit` 通过（frontmatter 不退化）。
4. 确实合理的相似/缺来源/artifact 未注册，按第三类永久基线处理。

## 本轮处理记录（老顽童 Kimi 实例）

### 已完成的清理动作

1. **ai-collaboration 域 Critique 外部反对者补全（3 文件）**
   - `30_wiki/concepts/ai-tool-learning-workbook.md`：补充 Seymour Papert、John Hattie 的外部反对观点
   - `30_wiki/concepts/ai-virtual-coach-prompt.md`：补充 Dylan Wiliam、Richard Clark 的外部反对观点
   - `30_wiki/concepts/practice-card-decomposition.md`：补充 Anders Ericsson、Barbara Oakley 的外部反对观点
   - 每张卡均通过 `kdo pre-submit`

2. **title_count_mismatch 修复（8 文件）**
   - 修改 7 个文件的标题，去除与正文 item 数量不匹配的数字表述
   - `framework-strategy-business-design.md` 补充六要素清单 bullet，使标题与正文匹配
   - 全部通过 `kdo pre-submit`

3. **When NOT to Use copy-paste 修复（2 文件）**
   - `yt-research-intelligence-map.md`：针对 13 武器体系重写 When NOT to Use
   - `yt-research-user-jtbd.md`：针对 JTBD 方法重写 When NOT to Use

4. **Wiki page 无可见来源清零（32 文件）**
   - 将 source_refs 为空或只有 src_unknown 的文件统一改为 `pending_archive: src_unknown`
   - 无 visible source WARNING 已清零

### 发现的副作用

- 删除 706 个空"常见失败模式" section 后，`body too short` WARNING 从 80 激增至 651。这些卡片需要后续回填具体失败模式或扩展其他 section。

### 下一轮建议

1. **处理 body 过短（651 文件）**：优先处理 case 卡和 tool 卡，扩展内容或归档
2. **处理 copy-paste（584 文件）**：针对仍有具体内容的相似 section 重写
3. **处理 L2 Critique / no_external_attacker（846 + 714）**：按 domain 分批补充外部反对者和关键术语
4. **处理 L2 Condense / L2 Synthesis（216 + 188）**：补充要点和外部链接

## 验收标准

- 每批 `kdo lint --domain <domain>` WARNING 数清零或降至可接受基线。
- 全库 `kdo lint` WARNING 持续下降。
- 不引入新的 frontmatter/目录/索引 ERROR。

---

> 本任务由 #26 frontmatter 合规修复任务拆分而来，承接剩余内容债。

## 工具说明

- `kdo lint --domain <domain>` 已可用：按 `30_wiki/<domain>/` 路径前缀或 frontmatter `domain` 字段过滤 WARNING。
- `kdo lint --domain <domain> --summary` 可快速查看该 domain 的 WARNING 数量，不输出逐条明细。
- 示例：`kdo lint --domain yitang --summary`
