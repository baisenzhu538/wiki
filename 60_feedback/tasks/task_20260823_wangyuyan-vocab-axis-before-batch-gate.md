---
id: 485
assignee: wangyuyan
status: queued
updated_at: '2026-08-24T01:00:00+08:00'
version: v0.1
---
# #485 轴文件先行·剩余域轴批量出 + gate 化（#426 放量前提机制化）

- **任务号**：#485
- **状态**：queued
- **assignee**：wangyuyan（编排；规范改；黄药师 gate 工具支撑挂子任务/老朱拍板后拆）
- **优先级**：P1（#426 放量堵点根治——轴文件缺位=放量堵点反复，content 域卡数小时实证）
- **立项**：2026-08-24 王语嫣（老顽童建议书 `diag_20260823_laowantong-vocab-axis-before-batch` 裁定采纳）
- **执行前提**：**需老朱拍板规范改**（tags-vocab-design 补「轴文件先行」条目）+ 剩余域清单确认

## 背景（老顽童 #426 治理实证）

#426 治理 7 批 260 张（决策域 44/ai-collaboration 200/human-insights 2/content 14），每批放量都依赖王语嫣临时补轴。**content 域 23:08 才补，12 张空缺卡数小时**——轴文件缺位=放量堵点反复。

**根因**（老顽童定位）：词表 v0.3 写"每域轴文件王语嫣按域起草"但**无强制闭环**——"无词表不动手"只约束生产者（老顽童），不约束编排侧出轴节奏（王语嫣）；轴文件是隐式依赖，无"轴文件先行"显式 gate。与 E054（建轴义务漏）同根——E054 是个人主动化，本任务是机制 gate 化。

## 任务

### 任务 1·剩余域轴批量出（王语嫣自办）
- 剩余待治理域轴文件批量出齐落 `90_control/tags-vocab/`：business / ai-native / leadership / operations / ...（按 #426 全库 tags 空缺域清单，不全出——按放量节奏）
- 每域轴按半肥猫五维+来源轴（专业/对象/性质/认知警示/使用者/经验+来源），格式照 content.yaml/human-insights.yaml/decision-making.yaml v0.1
- 老顽童试点反馈新词→王语嫣审词入轴→版本+0.1（双原则）

### 任务 2·「轴文件先行」gate 化（规范改，需老朱拍板）
- `90_control/tags-vocab-design.md` §三分域实施规则补一条硬纪律：**「轴文件先行」：任何域未出轴文件前，该域不得进入 #426 治理队列**（gate 化）
- 黄药师工具支撑（挂子任务/老朱拍板后拆 #487）：full-library-rescan / pre-submit 侧加"域空缺治理前置检查"——该域轴文件存在才允许批次提审

## 验证
- L1：剩余域轴文件落 90_control/tags-vocab/（yaml 合法，半肥猫五维+来源轴）
- L2 狗粮：tags-vocab-design 补「轴文件先行」条目（grep 校验）
- L3 待活体：#426 下一域治理前查"轴文件是否存在"，不存在先建轴（gate 生效）

## 边界
- **执行前需老朱拍板规范改**（tags-vocab-design 补条目）
- 剩余域不全出——按 #426 放量节奏（避免过度建设，每域出轴随治理批次）
- 黄药师 gate 工具是子任务/拆单（E026 不跨角色，王语嫣规范+出轴，黄药师工具另单）
- 不动已治理域（decision-making/ai-collaboration/human-insights/content 已有轴）

## 关联
- 老顽童建议书 `diag_20260823_laowantong-vocab-axis-before-batch`（裁定采纳）
- E054（建轴义务漏——个人主动化）/ 本任务（机制 gate 化）同根补全
- tags-vocab-design §三（分域实施规则）/ #426（tags 治理）/ #449（file-flow-protocol 规范）
- content.yaml/human-insights.yaml/decision-making.yaml（已出 3 轴 v0.1 范本）

## 需要谁动作
- **王语嫣**：剩余域轴批量出 + tags-vocab-design 补「轴文件先行」条目（执行前老朱拍板）
- **黄药师**：gate 工具支撑（pre-submit 检查域轴，挂子任务/老朱拍板后拆 #487）
- **老顽童**：轴到位即按轴放量（本批 content 已验证流程跑通）
- **老朱**：拍板规范改（tags-vocab-design 补条目）
