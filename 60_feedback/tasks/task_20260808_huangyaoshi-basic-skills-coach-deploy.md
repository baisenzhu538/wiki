---
id: task_20260808_huangyaoshi-basic-skills-coach-deploy
task_id: 256
assignee: huangyaoshi
status: queued
updated_at: 2026-08-08
domain: ai-basic
priority: P0
---

# #256 agent-basic-skills-coach 部署（层次 2/3——黄药师独立任务）

## 背景

从 #251 拆出（一任务一执行者纪律——王语嫣编排修正 2026-08-08）。规格层（agent-spec 卡）由老顽童 #251 完成、欧阳锋审查中；**本任务=部署层+实测准备，全部黄药师**。

## 任务内容

### 层次 2：可运行部署
1. `agents/agent-basic-skills-coach/` 目录落地（CLAUDE.md + system prompt + 数据源接入）——参考 `agents/sales-dialogue-assistant/` 部署模式
2. 工具接入：`kdo feature`（#254 已 reviewed A 级——点菜/查询数据源，动态读 JSON，周期表补齐后自动生效）
3. cap_hub 注册：agent 条目（id/name/category/description/source/status——对齐 FEATURE_MENU 登记格式）

### 层次 3：实测准备
- 用 agent-spec（#251 产出）的基线用例做冒烟测试（"AI 客服跳步"示例——输出状态机 Feature 路径）
- 实测通过后：#252 消费端试点（assignee wangyuyan）可启动

## 输入（已就位）

- `30_wiki/tools/agent-spec-basic-skills-coach.md`（#251 产出——规格）
- `10_raw/sources/feature-periodic-table-v0.8.json`（#248——数据源，96/100，#255 收尾中）
- `kdo feature` 工具（#254——点菜接口）
- `30_wiki/frameworks/bridge-dual-track-feature-system.md`（#251——双轨分界，防混编）

## 补审记录（欧阳锋 2026-08-08）

**结论：PASS（条件），等级 B+**——部署主体完成（目录落地/数据源 100/测试 8/8 动态断言），但 cap_hub agent 条目注册（任务单层次 2 第 3 条）**未做** + "96"残留 ×3。

### 独立验证（O3 实测）

| 验收项 | 结果 | 证据 |
|:--|:--|:--|
| agents/ 目录落地 | ✅ | `agents/agent-basic-skills-coach/CLAUDE.md` + `system-prompt.md` 存在，内容完整（启动/核心能力/数据源/基线）|
| 数据源接入 | ✅ | `kdo feature list` 实测 **100 个**，四命令全通 |
| 冒烟测试 | ✅ | `python -m pytest kdo-tools/test_feature_menu.py` → **8 passed**（动态断言，不写死数字）|
| cap_hub 注册（层次 2 第 3 条）| ❌ | `python -m cap_hub list` → 无 agent-basic-skills-coach 条目；"可参考的说明书 (0 类)"——任务单明确要求，未做 |

### 条件项

1. **🟡 cap_hub agent 条目注册**：任务单层次 2 第 3 条验收缺口——补注册（对齐 FEATURE_MENU 格式），或黄药师裁定不需要（agent 已走 agents/ 目录启动机制，说明理由并任务单加注）
2. **🟡 "96" 残留 ×3**：`agents/.../CLAUDE.md`（"96 Feature"）、`system-prompt.md`（"96个Feature"）、`cap_hub/features.json` FEATURE_MENU description（"从 96 个...点菜"）——应随周期表 100/100 更新

### 🟡 全库 "96→100" 清扫建议（转王语嫣编排）

已知残留 6 处：agent CLAUDE.md / system-prompt / cap_hub FEATURE_MENU / framework-truman-feature-layered-system L58 / dk-key-hypothesis L46 / 40_outputs/code/scripts/README.md（feature_menu 登记）。**建议排独立清扫任务一次性清完**（逐处退回效率低），且清扫时统一改为"周期表 JSON"不带数字（根治写死）。

**#252 解锁确认**：试点用 `agents/agent-basic-skills-coach/` 启动即可（cap_hub 注册不阻塞试点功能）。

1. agents/agent-basic-skills-coach/ 可运行（启动 + system prompt 注入 + kdo feature 调用）
2. cap_hub 注册完成（agent 条目可查）
3. 基线用例冒烟测试通过（输出 Feature 路径建议）
4. 部署记录（60_feedback/ 或 agents/ 目录 README——登记纪律）

## 依赖

- #251 规格层 reviewed（agent-spec 定稿——冒烟测试的用例依据）
- #254 reviewed ✅（工具就绪）
- #248 reviewed ✅（数据源就绪，final 版等 #255）
- → **#252 消费端试点依赖本任务完成**

## 边界

- 只做部署+冒烟，不做生产环境优化（v0.1 跑通即可）
- 双轨隔离：agent 只读 capability 轨（周期表 JSON），不碰 cap_hub lint 轨

## 🆕 输入更新（2026-08-08 黄药师先行 A/B 已落盘——本任务直接使用）

- **先 A（双轨 cap_hub 侧输入）**：12 lint Feature 清单 + 边界 + bridge 卡建议（落盘位置：60_feedback/ 或任务单对应记录——bridge 卡本体已由老顽童产出 `30_wiki/bridges/bridge-dual-track-feature-system.md`）
- **先 B（Agent 注册规范）**：`cap_hub/agent-registration-norm.md`——三步机械部署（spec 落位→cap_hub 自动扫描→kdo feature --seed 接入）+ 验证命令 + 9 已有 spec 参考——**部署直接按此规范执行**
