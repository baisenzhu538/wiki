---
id: task_20260714_wangyuyan-badcase-feedback-loop
title: bad case 回流机制与首条记录
type: task
status: queued
priority: P1
assignee: kimi
reviewer: 欧阳锋
created_at: 2026-07-14
updated_at: '2026-07-19T00:00:00+00:00'
expected_cards: 1
source_refs:
  - 70_product/tasks/production-queue.md #188
related:
  - framework-kdo-self-attack
  - 60_feedback/issues
  - 60_feedback/retro
---

# bad case 回流机制与首条记录

> 任务来源：生产队列 #188（原由王语嫣/老朱在队列编排中确认）
> 任务目标：建立 KDO 知识工厂 bad case 回流机制——让 Agent 输出错误、用户纠正、审查漏网之鱼能被结构化记录，并回流到知识库进化。

---

## 一、输入

1. 队列条目：`70_product/tasks/production-queue.md` #188
2. 现有相关素材（需调研后确认）：
   - `60_feedback/issues/` 下历史 issue 记录
   - `60_feedback/retro/` 下复盘记录
   - `framework-kdo-self-attack`（自攻击方法论，与 bad case 分类相关）
   - 各 Agent 的 daily-context 与审查记录

---

## 二、生产清单

### 2.1 必产：机制卡 1 张

| 卡 ID | 类型 | 优先级 | 核心内容 |
|---|---|:---:|:---|
| `framework-kdo-badcase-feedback-loop` | framework | P0 | bad case 回流机制：定义 → 发现 → 记录 → 分类 → 归因 → 修复 → 验证 → 回流 |

### 2.2 可选：首条 bad case 记录

| 卡 ID | 类型 | 说明 |
|---|---|:---|
| `case-kdo-badcase-YYYY-MM-DD-<slug>` | case | 等老朱真实使用后补充首条记录 |

---

## 三、机制卡必须包含的六要素

### 3.1 定义
- 什么是 bad case：Agent 输出错误、用户明确纠正、审查未拦截、造成实际返工或误导的案例
- 什么不是 bad case：用户偏好差异、风格争议、未采纳建议

### 3.2 发现渠道
- 用户主动反馈
- 欧阳锋终审时发现
- 老顽童生产时自攻击发现
- 王语嫣方向把关时发现
- 后续使用中发现

### 3.3 记录模板

```markdown
## bad case 记录

- **id**: badcase_YYYYMMDD_xxxxxxxx
- **日期**: YYYY-MM-DD
- **涉及 Agent**: wangyuyan|laowantong|huangyaoshi|ouyangfeng|...
- **涉及任务/卡片**: task_id / card_id
- **缺陷类型**: [事实错误|逻辑漏洞|边界遗漏|流程违反|幻觉|用户模型错误|其他]
- **现象**: 一句话描述错在哪里
- **正确做法**: 应该怎么做
- **根因**: 为什么会发生
- **修复动作**: 已做/将做什么
- **回流位置**: 更新到哪张卡 / 哪个 skill / 哪个 agent-spec
- **验证方式**: 如何确认不复发
```

### 3.4 缺陷分类

| 一级分类 | 二级分类 | 典型表现 |
|---|---|---|
| 事实错误 | 数据错误、来源误引、年份混淆 | 数字、引文、案例事实对不上 |
| 逻辑漏洞 | 推导跳跃、因果倒置、以偏概全 | 结论推不出前提 |
| 边界遗漏 | 未考虑例外、未标注适用条件 | 绝对化表述、忽视平台型企业等例外 |
| 流程违反 | 未按角色协议执行、跳过门禁 | 该检索未检索、该自检未自检 |
| 幻觉 | 编造不存在的卡片/来源/数据 | source_refs 指向不存在文件、虚构数据 |
| 用户模型错误 | 误判用户偏好、决策记录、战略方向 | 给出与用户已知结论冲突的建议 |

### 3.5 存储路径

- **机制卡**：`30_wiki/frameworks/framework-kdo-badcase-feedback-loop.md`
- **case 记录**：`60_feedback/badcases/badcase_YYYYMMDD_xxxxxxxx.md`
- **索引**：`60_feedback/badcases/index.md`（按 Agent/类型/状态汇总）
- **回流追踪**：在受影响卡片 `## 迭代日志` 节追加

### 3.6 闭环流程

```text
发现 → 记录 → 分类 → 归因 → 决策（立即修 / 排期修 / 不修）
  → 修复（更新卡 / skill / agent-spec） → 验证（抽检 / 回归测试） → 关闭
```

---

## 四、关键规则

1. **先调研再建卡**：生产前必须调研 `60_feedback/issues/`、`60_feedback/retro/`、`framework-kdo-self-attack` 等现有素材，避免与已有机制重复。
2. **机制卡不带具体案例**：机制卡只定义流程、模板、分类、路径；具体 bad case 用独立 case 卡记录。
3. **首条记录等真实案例**：不编造首条 bad case，等老朱真实使用后补充。
4. **双向链接**：机制卡必须 related 到 `framework-kdo-self-attack`、`60_feedback/issues`、`60_feedback/retro` 等现有反馈入口。
5. **不要孤岛卡**：机制卡 related ≥ 5 条，含至少 1 条跨域。

---

## 五、验收标准

- [ ] `framework-kdo-badcase-feedback-loop` 通过 `kdo pre-submit`
- [ ] `kdo lint` 0 ERROR
- [ ] 机制卡 related ≥ 5 条，含至少 1 条跨域回链
- [ ] 六要素齐全：定义、发现渠道、记录模板、缺陷分类、存储路径、闭环流程
- [ ] 已调研现有相关卡片/机制，并在卡中说明与现有机制的关系
- [ ] 欧阳锋抽检确认：模板可直接复用、分类不重叠、闭环流程可执行

---

## 六、欧阳锋抽检重点

1. 缺陷分类是否完整且互斥？是否有真实案例能对应到每个分类？
2. 记录模板字段是否过多或过少？是否便于快速填写？
3. 闭环流程是否止于"记录"？必须明确"修复 → 验证 → 关闭"的下一步责任人与触发条件。
4. 与 `framework-kdo-self-attack` 的边界是否清晰？自攻击是事前预防，bad case 回流是事后修复，二者应互补不重复。

---

## 七、队列位置

- **入队编号**：`#188`
- **状态**：`queued`
- **阻塞/依赖**：无
- **预计工期**：0.5-1 个老顽童实例周期
