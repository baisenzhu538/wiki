---
id: task_20260808_huangyaoshi-feature-menu-tool
task_id: 254
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-08
updated_at: 2026-08-08
domain: system
priority: P0
---

# #254 周期表"点菜"查询工具（消费端协议技术底座）

## 背景

消费端协议（#252 试点）需要"点菜式查询"——从周期表 100 Feature 中按 layer/dimension/scenario 过滤点菜。没有工具，点菜靠人肉翻 JSON（消费端协议无法跑通）。本任务 = 消费端的技术底座。

## 任务目标

实现 `kdo feature` 命令（或 cap_hub 扩展——黄药师定）：

```
kdo feature list                      # 全量 100 Feature 列表
kdo feature query --layer L2          # 按层级过滤（L0-L5）
kdo feature query --dimension A       # 按四维坐标过滤（A角色/B上下文/C能力/D任务）
kdo feature query --scenario 作图     # 按场景过滤
kdo feature pick --n 5                # 点菜：随机/推荐 5 个候选（关键假设起点）
kdo feature info F001                 # 单 Feature 详情（含 verified/case_ref）
```

## 规格（对齐 #248 JSON Schema）

- 数据源：`#248` 周期表 JSON（id/name/layer/dimension/purpose/scenario/case_ref/verified 八字段）
- 输出：表格/JSON 两模式（人看用表格，消费端协议用 JSON）
- **双轨防混编（欧阳锋洞察 3 技术侧）**：`kdo feature` 只查 capability Feature（课程周期表）；cap_hub/features.json 的 lint 类 Feature 不混入——cap_hub 侧可加类型标记（lint/capability）作为工程保障
- 与 cap_hub 的关系：黄药师裁定（独立命令 or cap_hub 子模块），但**查询语义必须区分两轨**

## 验收标准

1. `kdo feature` 可用（list/query/pick/info 四命令）
2. 用 #248 真实 JSON 数据狗粮验证（点菜 5 个 → 消费端协议 #252 试点可用）
3. pytest 通过；`kdo --help` 登记
4. 工具登记（40_outputs/code/scripts/README.md 或 cap_hub 规范——登记纪律）

## 依赖

- #248 reviewed（周期表 JSON 就绪——数据源）
- #253（域注册，命令挂靠域入口）

## 边界

- 不做推荐算法（v0.1 只做过滤+随机；智能推荐是 v0.2+）
- 不碰 lint 类 Feature（双轨隔离）

---

## 补审记录（欧阳锋 2026-08-08）

**结论：PASS**，等级 A-。四个命令真实运行验证通过，非采信报告。

### 独立验证（O3，实测输出）

| 命令 | 实测 | 与 #248 JSON 一致性 |
|:--|:--|:--|
| `list` | 96 个全量 | ✅ 一致 |
| `query --layer L2` | 34 results | ✅ L2=34 一致 |
| `query --dimension A` | 27 results | ✅ A=27 一致 |
| `pick --n 5` | 5 个随机点菜，已验证项带 case_ref | ✅ 随机逻辑正确 |
| `info F031` | 完整详情 + verified + 溯源"口述上 L676-750" | ✅ 逐字命中口述上 L674/748 |

### 验收逐项

| 验收项 | 结果 | 说明 |
|:--|:--|:--|
| 1. 四命令可用 | ✅ | 实测全通 |
| 2. #248 真实 JSON 狗粮验证 | ✅ | 数字与 JSON 分布完全一致；动态读 JSON——#248 C1/C2 补完 100 个后自动生效，无需改码 |
| 3. pytest 通过 / kdo --help 登记 | 🟡 | **无测试文件**（未找到 feature_menu 对应 test）；工具为 kdo-tools 独立脚本非 KDO CLI 扩展，"kdo --help 登记"不适用——cap_hub 登记已满足"不登记=不存在"纪律 |
| 4. 工具登记 | ✅ | cap_hub/features.json 13/13（12 lint + **FEATURE_MENU** cli 条目完整：id/name/category/description/test/source/status）|
| 附：双轨防混编 | ✅ | 数据源物理隔离——feature_menu.py 只读 `10_raw/sources/feature-periodic-table-v0.8.json`（capability 轨），cap_hub lint 轨在 features.json，无交叉路径 |

### 条件项（不阻塞 #249/#252 试点）

- 🟡 T1：补 smoke test（query 边界/pick n 上限/info 未找到 ID 分支）——建议 #252 试点后随复盘补
- 🟢 T2：pick 增加 `--seed` 支持可复现点菜（试点复盘需要复现性）——P2
- 🟢 T3：code 质量观察——`fmt()` 用 `f['purpose'][:50]` 对短 purpose 正常，无溢出风险；纯标准库符合零运行时依赖 ✅

### 关联：#248 条件项进展

- **C4 已从 7 项缩减至 1 项**：17 个 verified 中 16 个 case_ref 已带行号；剩余 F044（新开窗分支测试）仍为"口述：分支测试法"无行号——转 #248 修复清单

**#249 启动确认**：`kdo feature pick --n 5` 点菜能力就绪，老顽童 W1 可直接使用。

---

## 条件项复核（欧阳锋 2026-08-08，T1/T2/T3）

| 条件 | 状态 | 独立验证证据 |
|:--|:--|:--|
| T1 补 smoke test | ✅ 完成 | `kdo-tools/test_feature_menu.py` 存在，`python -m pytest` → **9 passed in 0.07s** |
| T2 pick --seed 可复现 | ✅ 完成 | feature_menu.py L54-55/L90 实现；实测 `pick --n 3 --seed 42` 两次输出逐字一致（F082/F015/F004 同序）|
| T3 工具登记 | ✅ 完成 | `40_outputs/code/scripts/README.md` L115-126 已登记：功能描述 + 命令 + 使用场景 + 5 个用法示例（含 `--seed 42` 可复现）。"不登记=不存在"纪律满足 |

**T1/T2/T3 三条件全齐，等级升级：A- → A**（2026-08-08 复核）。
