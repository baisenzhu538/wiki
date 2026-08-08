---
id: task_20260808_huangyaoshi-agent-knowledge-access
task_id: 260
assignee: huangyaoshi
status: queued
updated_at: 2026-08-08
domain: system
priority: P0
---

# #260 KDO Agent 知识接入规范（agent 用知识库的基建缺口）

## 背景（用户实测触发）

用户实测 agent-basic-skills-coach 发现：**agent 不知道 KDO、不知道如何调用 KDO 知识库**。根因：agent 部署只接了"Feature 菜单子集"（kdo feature + 周期表 JSON），未接入"KDO 知识库本体"（认知层缺失 + 检索层缺失）。这是"agent 用知识库"的系统性缺口——我们修过"人用知识库"（MOC/#236），但从没建"agent 用知识库"。

对照 Truman 原则（口述下 L1494-1500）："你去一堂学一下双三角模型，帮我做一个复盘"——**知识库资产应被 agent 按需调用**。coach 恰好缺此能力。

## 任务目标

建立 KDO Agent 知识接入规范（所有 agent-spec 适用）+ coach 试点接入。

## 规范内容

### 1. Agent 系统提示的"KDO 知识地图"段（认知层）
所有 KDO agent-spec 的系统提示必含：
- KDO 是什么（知识库定位：AI for Business 商业判断力 + 方法论）
- 域结构导航（MOC 清单：复盘/design/master/product/kdo + 各域 digest）
- "不知道的先去查，不凭记忆答"（W8 规则的 agent 版）

### 2. Agent 检索工具接入（检索层）
- agent 可调用 `kdo query`（语义+BM25 检索）——以工具形式暴露
- agent 可调用 MOC 导航（域入口→子卡定位）
- 工具清单写入 cap_hub agent 注册（对齐 FEATURE_MENU 格式）

### 3. coach 试点接入（本任务直接落）
- agents/agent-basic-skills-coach/ 的 CLAUDE.md + system-prompt.md 追加：
  - "KDO 知识地图"段（域导航 + 检索指引）
  - 检索工具调用示例（"去 KDO 查一下 XX 方法论"）
- 冒烟测试新增：问"你知道 KDO 吗？怎么查复盘方法论？"→ 应答命中 KDO 定位 + MOC 导航

## 验收标准

1. 规范文档落盘（90_control/ 或 cap_hub 规范——黄药师裁定位置）
2. coach 系统提示含知识地图段；冒烟测试新增用例通过（知道 KDO + 会导航）
3. 规范可复用（#246 复盘教练/#150 教练等 agent-spec 后续按规范补）

## 依赖 / 边界

- 无硬依赖（coach 已部署可改）
- 不阻塞 #252 试点（试点用 Feature 菜单，知识接入补完后试点可顺带验证"知识调用"能力）
- 与 #258（cap_hub 注册裁定）衔接——知识接入规范随 agent 注册一起定

---

## 状态流转提醒（2026-08-09 王语嫣编排——完成未闭环优先）

三件套（认知/检索/实测）已完成且实测通过，但任务单/队列状态仍 queued——**请黄药师补走提交（complete）→ 欧阳锋终审 → reviewed**。完成未闭环的任务优先于排队任务（执行序①）。
