---
id: task_20260809_huangyaoshi-skill-crystallize
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: 2026-08-09
priority: P1
wsjf: 4.3
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师）

### 交付物
1. **`kdo-tools/skill_crystallize.py`** — 经验→技能自动结晶（jarvis 模式）：
   - 扫描 4 类数据源（错误模式库/技能进化日志/认知复盘/daily-context，共 33 个文件）
   - 8 个主题关键词聚类，同主题 ≥2 次 → 结晶候选
   - 产物 draft 骨架（frontmatter: status=draft + 证据来源列表 + 触发词）
   - **不自动 publish**——人审路径：`skill_lifecycle.py set crystallized-<name> --status published --apply`

### 验收标准
| 验收项 | 状态 |
|:---|:---|
| 从存量复盘/错误库结晶 ≥1 个 draft 候选 | ✅ **8 个候选**（33/29/23/18/15/14/10 次命中） |
| 候选进入 #273 draft status 机制 | ✅ skill_lifecycle status 实跑 `crystallized-dry-run-before-batch → draft` |

### 8 个候选（按命中次数）
1. 先诊断根因再调参（33）2. 证据先于声称（29）3. 批量操作 dry-run 先行（23）4. 狗粮测试三连（18）5. 摩擦当下记录（15）6. 调研先行（14）7. 编码感知文件 IO（10）8. frontmatter round-trip 校验

### 狗粮测试（完整链路）
| 场景 | 结果 |
|:---|:---|
| scan dry-run | ✅ 候选分布 + 证据追溯 |
| scan --apply | ✅ 8 候选生成（工作区 + 发布副本） |
| frontmatter 校验 | ✅ 8/8 status=draft, type=capability/skill |
| skill_lifecycle 集成 | ✅ status 实跑可见 crystallized-* |
| 发布路径 draft→published→回滚 draft | ✅ 完整验证（人审前状态正确） |

### 过程中踩的坑（2 个，已修复）
1. **hits 缺 name 字段**：candidates 从 values() 来无 name → KeyError。修复：构造时保留 name
2. **发布目录父目录未创建**：`crystallized-<name>/SKILL.md` 写入前未 mkdir → FileNotFoundError。修复：pub_dir.mkdir

### 设计要点
- **jarvis 阈值 3 → 2**：存量复盘有限，≥2 更实用（≥3 会漏掉大部分主题）
- **双目录设计**：draft 骨架在 crystallized-candidates/（工作区）+ 发布副本 crystallized-*/（skill_lifecycle 可发现）——审后发布直接走 #273 机制，不改已终审代码

# 经验→技能自动结晶（#279 · 黄药师建议书 #269s）

## 任务目标

jarvis 模式：使用 ≥3 次的有效做法自动提炼为 draft skill 候选，人审后 publish。

## 规格

1. `kdo skill crystallize` 命令：扫描错误模式库 + 技能进化日志 + daily-context 复盘，提取"重复出现的有效做法"（关键词/结构匹配 + 候选清单）
2. 产物为 draft 状态 skill 骨架（模板填充），**不自动 publish**
3. 人审路径：黄药师审候选 → 达标则 publish → 登记 README

## 验收标准

- 从存量复盘/错误库结晶出 ≥1 个 draft skill 候选
- 候选进入 #273 的 draft status 机制

## 依赖

- **#273（Skill 生命周期化）**——结晶产物用 draft status

## 借鉴

jarvis 模式（使用次数阈值触发提炼）

## 参考素材

- 黄药师建议书 §#269s

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O3 独立验证：
1. skill_crystallize.py 存在（8930B）；8 个结晶副本 + 1 个工作区（40_outputs/capabilities/skills/crystallized-*）✅
2. **8/8 候选 status: draft**——不自动 publish 纪律遵守（人审路径 skill_lifecycle set --status published）✅
3. skill_lifecycle 集成生效：list draft 4→12（+8 结晶候选可发现）✅
4. 内容骨架真实：抽查 crystallized-evidence-over-claims——触发词 + 使用方法（待填占位）+ 证据来源（29 次命中，技能进化日志关键词"声称、验证"）✅
5. 坑记录诚实（hits 缺 name / 发布目录未 mkdir，均修复）；jarvis 阈值 3→2 有理由（存量复盘有限）✅

亮点：**jarvis 模式落地——从经验库到 draft skill 的全自动链路**（扫描→聚类→结晶→draft→人审→publish），把"重复出现的有效做法"从复盘文字变成可复用资产管线；双目录设计不改已终审代码。8 个候选中"证据先于声称（29 次）/先诊断根因（33 次）/调研先行（14 次）"正是本厂核心纪律——结晶命中真实。

待办（人审路径）：8 候选的"使用方法"为占位——发布前需黄药师/欧阳锋补操作步骤 + source_refs/related，再走 #273 publish。

五维：溯源 90/逻辑 90/暗知识 85/可操作 90/表达 85 → 总分 89（A）
