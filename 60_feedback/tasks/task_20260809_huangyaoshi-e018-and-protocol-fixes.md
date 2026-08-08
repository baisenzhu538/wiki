---
id: task_20260809_huangyaoshi-e018-and-protocol-fixes
task_id: 264
assignee: huangyaoshi
status: queued
updated_at: 2026-08-09
domain: system
priority: P0
---

# #264 E018 铁律升级 + 协议 v0.1 三修正 + cap_hub 注册（Feature 域收官三件）

## 背景

#252 试点终审 PASS（条件）B+。欧阳锋建议三项排入下批（E018 四提四证刻不容缓）；#258 裁定触发条件已满足（试点通过）。

## 任务内容（三项，全部黄药师）

### 1. E018 升级为全角色铁律（欧阳锋条件项③，四提四证）
- 写入所有 agent 的 context + system prompt：`wangyuyan/laowantong/hongqigong/ouyangfeng/duanwangye` + coach 的 CLAUDE.md/system-prompt.md
- 铁律内容（E018 三条款）：
  - ① 自建经验卡允许（author=自己）
  - ② reviewed_by 必须真实审查者
  - ③ status 默认 draft，不得自行标 reviewed
- 并入 #261（全局认知标准化）的生产纪律部分或独立落盘——黄药师裁定

### 2. 协议 v0.1 三修正（欧阳锋条件项①②）
- **verified 语义声明**：原语义"口述中至少一次有效"扩展为"已被真实任务测试（含边界无效）"——协议 v0.1 声明新语义 + 写入周期表 JSON schema 说明
- **消费端读 verify_note**：`feature_menu.py` fmt() 输出 verify_note（F039 类"无效但 true"不被误当有效点菜）
- 更新 `10_raw/sources/feature-periodic-table-v0.8.json` 的 schema 说明字段

### 3. cap_hub 注册触发（#258 裁定条件满足）
- 试点通过 → 按 agent-registration-norm.md 三步规范注册 agent-basic-skills-coach 到 cap_hub

## 验收标准

1. 5 角色 + coach 的 context/system prompt 含 E018 铁律（grep 可查）
2. feature_menu fmt() 显示 verify_note；JSON schema 含 verified 语义说明
3. cap_hub 注册 agent 条目完成（cap_hub list 可查）
4. 冒烟复测（feature_menu 输出无回归）

## 依赖

- #252 reviewed ✅（试点通过，触发条件满足）
- #261（E018 并入其生产纪律部分——黄药师协调）
