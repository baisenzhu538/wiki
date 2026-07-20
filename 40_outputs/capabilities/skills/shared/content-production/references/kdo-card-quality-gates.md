# KDO Card Quality Gates — By Card Type

> 附录于 `content-production` skill。记录欧阳锋审查中反复出现的按卡片类型的 pre-submit 门禁要求。
> 本文件是对 `kdo pre-submit` 机械检查的补充——机械检查覆盖 YAML 语法/必填字段/结构完整性，本文件覆盖**内容质量**层面的类型专属要求。

## 一、通用要求（所有类型）

### 必填 frontmatter 字段
- `reviewed_by: pending` — draft 卡必须保留此占位，否则 pre-submit FAIL
- `diagnostic_signals` — 至少 1 条信号，新卡可用占位 `"卡片新建，待欧阳锋终审后补充信号"`

### 提交前检查
- `kdo pre-submit -f <file>` 必须 PASS
- 检查是否有同 ID 的重复文件残留在错误目录（如 `dark-knowledges/` 中的 ai-collaboration 域卡）

## 二、dk 卡专属要求

| 检查项 | 标准 | 信号 |
|:--|:--|:--|
| `## Critique` section | 必须存在，含 ≥1 外部挑战 + ≥1 内部局限 | 缺失 = 🔴 退回 |
| 标准 6 section | `原始表述` / `使用场景` / `操作方法` / `适用边界` / `为什么值钱` / `与其他知识的关联` | pre-submit 机械检查已覆盖 |

## 三、tool 卡专属要求

| 检查项 | 标准 | 信号 |
|:--|:--|:--|
| `related` 数量 | ≥5 个互链 | <5 = 🔴 退回（欧阳锋裁定） |
| 四节结构 | `原始表述` / `使用场景` / `操作方法` / `适用边界` 齐全 | pre-submit 机械检查已覆盖 |

### tool 卡 related 补链策略
当 tool 卡 related < 5 时，优先从以下方向补充：
1. 同域 framework/concept 卡（方法论基础）
2. 同域 case 卡（应用实例）
3. 同域 dk 卡（暗知识/失败模式）
4. 跨域 framework 卡（方法论来源）
5. 相邻域桥接卡

## 四、case 卡专属要求

| 检查项 | 标准 | 信号 |
|:--|:--|:--|
| 关键数字 | 正文含至少 3 个可量化数字 | 无数字 = 🔴 退回 |
| 证据表 | `## 证据` section 含来源+强度标注 | pre-submit 检查 |
| 案例 section | `背景` / `决策链` / `关键数字` / `证据` / `复盘反思` | pre-submit 机械检查已覆盖 |
| 数字标注 | 讲师自述数字必须加 `> 数字为讲师自述，待独立核实` | 缺失 = 🟡 |

## 五、framework 卡专属要求

| 检查项 | 标准 | 信号 |
|:--|:--|:--|
| `related` 数量 | ≥5 个互链 | 建议性 |
| 外部批判 | `## Critique` section 含 ≥2 外部学者/框架引用 | 缺失 = 🟡 |
| 操作步骤 | `## 操作方法` 含可执行步骤（非纯理论） | pre-submit 检查 |
| 失败模式 | ≥3 个具体失败模式，每条含信号+修复 | <3 或模板话 = 🔴 |

## 六、concept 卡专属要求

| 检查项 | 标准 | 信号 |
|:--|:--|:--|
| `related` 数量 | ≥5 个互链 | 建议性 |
| 外部批判 | `## Critique` section 建议含外部引用 | 缺失 = 🟡 |

## 七、常见退回模式（本文件来源）

| 退回编号 | 问题 | 复现频率 |
|:--|:--|:--|
| R-001 | `diagnostic_signals` 全局缺失 | 高（新批次常见） |
| R-002 | dk 卡缺 `## Critique` section | 高（老顽童习惯性遗漏） |
| R-003 | tool 卡 `related` < 5 | 中 |
| R-004 | 同 ID 卡残留于错误目录（如 dark-knowledges/） | 中（scaffold 时路径错误导致） |
| R-005 | `reviewed_by` 缺失导致 pre-submit FAIL | 中（新卡常见） |

## 八、修复优先级

1. `reviewed_by` 缺失 → pre-submit 直接 FAIL，最高优先
2. `diagnostic_signals` + dk Critique + tool related → 欧阳锋审查退回，次高优先
3. 残留文件清理 → 影响索引准确性，次高优先
