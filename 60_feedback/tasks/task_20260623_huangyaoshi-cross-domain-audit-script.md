# 黄药师任务指令：跨域 related 自动审计脚本（王语嫣）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。黄药师负责基础设施/脚本开发。
> 来源：已批准的跨域融合计划（策略 A）——`plans/jade-batgirl-kate-bishop.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务来源 | 跨域融合计划（战略 · 精益 · 决策 · AI 协作桥接体系） |
| 计划文件 | `plans/jade-batgirl-kate-bishop.md` |
| 反馈日期 | 2026-06-23 |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | 黄药师 |

---

## 1. 任务目标

扩展现有死链/图谱清理脚本，新增**跨域 related 审计能力**：

- 自动识别哪些 framework/tool/digest 卡的 `related` 未跨越 ≥2 个域；
- 自动识别 bridge framework 卡是否链接到 ≥2 个目标域的核心卡；
- 输出月度审计报告到 `60_feedback/audit/cross-domain-link-report.md`；
- 脚本可集成到每日 9:03 自动巡检或独立运行。

---

## 2. 输入与输出

### 2.1 输入

- `30_wiki/` 下所有 `.md` 卡片；
- 每张卡的 frontmatter（id, type, domain, related）；
- 域映射表：根据卡 id 前缀或 domain 字段判断所属域。

### 2.2 输出

- 报告文件：`60_feedback/audit/cross-domain-link-report.md`
- 报告结构：
  - 执行时间
  - 总检查卡数
  - 未满足跨域要求的卡清单（按类型分组）
  - bridge 卡目标域覆盖情况
  - 修复建议
  - 白名单说明

---

## 3. 审计规则

### 规则 1：framework/tool 卡必须跨域

```python
if card.type in ['framework', 'tool']:
    related_domains = {domain_of(r) for r in card.related}
    if len(related_domains) < 2:
        flag(f"{card.id}: related 未跨越 ≥2 个域")
```

- `domain_of(related_id)` 的判定逻辑：
  - 优先读取被引用卡的 frontmatter `domain` 字段；
  - 若无法读取，按 id 前缀启发式判断（如 `framework-strategy-*` → strategy，`framework-lean-*` → lean-startup，`yt-five-step-*` → five-step，`tool-agent-*` → ai-collaboration）。

### 规则 2：bridge framework 卡必须链接到 ≥2 个目标域的核心卡

```python
if card.id.startswith('framework-') and is_bridge_card(card):
    target_domains = detect_bridge_target_domains(card.id, card.title)
    covered_domains = {domain_of(r) for r in card.related if domain_of(r) in target_domains}
    if len(covered_domains) < 2:
        flag(f"{card.id}: bridge 卡未覆盖 ≥2 个目标域")
```

当前 bridge 卡清单（由王语嫣指定）：
- `framework-strategy-lean-validation` → 目标域：strategy, lean-startup
- `framework-five-step-lean-interface` → 目标域：five-step, lean-startup
- `framework-lean-pivot-decision` → 目标域：lean-startup, decision
- `framework-ai-accelerated-strategy-cycle` → 目标域：strategy, lean-startup, ai-collaboration
- `framework-demand-lean-bridge` → 目标域：demand-analysis, lean-startup

### 规则 3：domain digest 必须链接到 ≥2 个相关 domain digest

```python
if card.type == 'index' and card.id.endswith('-domain-digest'):
    related_digests = [r for r in card.related if r.endswith('-domain-digest')]
    if len(related_digests) < 2:
        flag(f"{card.id}: domain digest 未链接到 ≥2 个其他 digest")
```

### 规则 4：白名单机制

某些纯技术/单域工具卡可以豁免跨域要求。白名单文件：`90_control/cross-domain-audit-whitelist.json`

初始白名单示例：
```json
[
  "tool-agent-crawl4ai",
  "tool-agent-firecrawl",
  "tool-strategy-gap-analysis"
]
```

白名单由王语嫣审核，黄药师维护。

---

## 4. 脚本要求

### 4.1 功能

1. 解析 `30_wiki/` 所有 `.md` 文件 frontmatter；
2. 建立 id → 卡片元数据索引；
3. 实现 `domain_of(id)` 函数，支持 frontmatter 读取 + 前缀启发式；
4. 实现三条审计规则 + 白名单；
5. 生成 Markdown 报告；
6. 支持命令行参数：`--vault`、`--report`、`--whitelist`。

### 4.2 建议位置

`90_control/scripts/cross_domain_audit.py`

### 4.3 建议调用方式

```bash
# 独立运行
python 90_control/scripts/cross_domain_audit.py

# 集成到每日巡检
python 90_control/scripts/daily_inspection.py --cross-domain-check
```

### 4.4 与现有脚本的关系

- 可复用 `repair-obsidian-links.py` 或 `vault_linter.py` 中的 frontmatter 解析函数；
- 不要重复造轮子，优先封装为通用 `vault_utils.py`；
- 输出格式参考现有 `vault-status.md` 或死链清理报告。

---

## 5. 报告模板

```markdown
# 跨域链接审计报告

**执行时间**：2026-06-23
**总检查卡数**：X
**异常卡数**：Y

## 1. framework/tool 卡未跨域

| 卡 id | 类型 | 当前 related 域 | 建议补充 |
|:---|:---|:---|:---|
| ... | ... | ... | ... |

## 2. bridge 卡目标域覆盖不足

| 卡 id | 目标域 | 已覆盖域 | 缺失域 |
|:---|:---|:---|:---|
| ... | ... | ... | ... |

## 3. domain digest 链接不足

| digest id | 当前 linked digests | 建议补充 |
|:---|:---|:---|
| ... | ... | ... |

## 4. 白名单

（列出被豁免的卡）
```

---

## 6. 验收标准

1. 脚本能在 `C:/Users/Administrator/Desktop/wiki/` 正常运行；
2. 能正确识别当前 5 张 bridge 卡的目标域覆盖情况；
3. 能正确标记未跨域的 framework/tool 卡；
4. 白名单机制可用；
5. 报告输出到 `60_feedback/audit/cross-domain-link-report.md`；
6. 脚本通过 `kdo lint` 或项目代码风格检查；
7. 不修改任何 `30_wiki/` 卡片内容（脚本只读）。

---

## 7. 特别注意

1. **脚本只读**：除非用户明确批准，否则脚本不得自动修改卡片。
2. **优先复用**：与现有死链清理/图谱修复脚本共享 frontmatter 解析逻辑。
3. **异常处理**：遇到 YAML 解析失败的卡，记录到报告但继续执行。
4. **性能**：当前全库约 1100 张卡，脚本应在 10 秒内完成。

---

*质量负责人：王语嫣 | 生成时间：2026-06-23*
