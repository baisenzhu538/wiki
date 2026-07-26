---
id: tool-three-ring-capability-filter
title: cap_hub 三环过滤器——能力注册准入 checklist
type: tool
status: draft
author: 黄药师
reviewed_by: pending
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-07-11
updated_at: 2026-07-11
domain:
- infrastructure
- ai-collaboration
source_refs:
- 00_inbox/Manage the team/Fundamentals Seminar/一堂-基本功拆解-笔记.txt
- 00_inbox/Manage the team/Fundamentals Seminar/_vlm_output/整合笔记_苦练基本功完整版.md
- 70_product/tasks/task_20260711_wangyuyan-fundamentals-dual-triangle-factory-buildout.md
related:
- '[[tool-一堂-基本功-三环六维自检]]'
- '[[concept-一堂-基本功定义]]'
- '[[task_20260708_huangyaoshi-capability-hub-phase1]]'
- '[[concept-yihang-dual-triangle-core]]'
aliases:
- 三环过滤器
- capability filter
- 能力准入
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---

# cap_hub 三环过滤器

> **一句话定义**：本过滤器是 `[[tool-一堂-基本功-三环六维自检]]` 在 cap_hub 能力注册场景的工程化应用——任何能力要进入 cap_hub 注册表，必须先通过三环 checklist。不是所有功能都值得注册为能力。
>
> **位置**：cap_hub Phase 2 Skill 注册标准的准入层。当前 Phase 1 的 `register()` 无门禁，本卡定义了门禁标准。Phase 2 实现时，`registry.register()` 应调用本卡的判定逻辑。

---

## 一、三环准入标准

### 环 1：务实性（具体 + 场景）

**判定问题**：这个能力有明确的 input/output spec 吗？在什么场景下被调用？

| 检查项 | 通过标准 | 不通过示例 |
|--------|---------|-----------|
| **输入规格** | 输入类型、必填字段、数据格式有文档 | "传一个图片"——没说格式/大小/来源 |
| **输出规格** | 输出类型、成功/失败返回格式有文档 | "返回分析结果"——没说结构/字段/错误码 |
| **场景锚定** | 至少 1 个明确的调用场景（谁、在什么环节、为什么调这个而不是别的） | "通用图片分析"——没有具体场景 |

**判定**：三项全部通过才算务实性达标。缺一项 = 能力定义不够具体，先补文档再注册。

> 为什么务实性重要 → 见 `[[tool-一堂-基本功-三环六维自检]]`"务实"维度的三环判定逻辑。

---

### 环 2：可练性（独立 + 可检验）

**判定问题**：这个能力能独立验证吗？有没有自动化的验证脚本？

| 检查项 | 通过标准 | 不通过示例 |
|--------|---------|-----------|
| **独立可调用** | 不依赖其他未注册的能力；`from cap_hub.xxx import process` 后单行可调 | 需要手动先跑 A、再跑 B、再调 C —— 且 A/B 未注册 |
| **验证脚本存在** | 存在 `test_<capability>.py` 或 `__main__.py` 中的 `--test` 模式，给定标准输入可自动判定 pass/fail | "我手动测过了，能用"——没有可重复的验证脚本 |
| **错误可定位** | 失败时输出明确的错误信息（哪个检查项、期望值 vs 实际值） | 只输出 "FAIL"，不知道哪里坏了 |

**判定**：三项全部通过才算可练性达标。验证脚本优先于手动测试。

> 为什么可练性重要 → 见 `[[tool-一堂-基本功-三环六维自检]]`"可练"维度的三环判定逻辑。

---

### 环 3：价值性（重复 + 复利）

**判定问题**：这个能力会被高频调用吗？越用越值钱吗？

| 检查项 | 通过标准 | 不通过示例 |
|--------|---------|-----------|
| **高频重复** | 预估月调用次数 ≥ 10，或 ≥ 2 个 Agent 会调用 | "这个能力只有某个特定任务需要"——一次性任务 |
| **复利效应** | 每多用一次，系统的能力在增强（数据积累/模型改善/覆盖面扩大） | 每次调用都是独立消费，不产生可积累资产 |
| **非重复造轮子** | 已有能力库里没有功能等价的替代品；若有近似能力，必须写明差异 | 新建一个"图片分析 v2"但与 vlm 功能重叠且差异不清晰 |

**判定**：三项全部通过才算价值性达标。月调用次数可以通过搜索 Agent context 文件中的 `from cap_hub` 引用来估算。

> 为什么价值性重要 → 见 `[[tool-一堂-基本功-三环六维自检]]`"价值"维度的三环判定逻辑。

---

## 二、使用方式

### 2.1 新能力注册前自检

能力开发者提交 PR 前，自己跑一遍：

```
1. 读本卡的三个环
2. 逐项勾选
3. 任一环不通过 → 先补再提交
4. 全部通过 → 在能力目录下放一个 REGISTRATION_CHECKLIST.md（本卡的实例化）
```

### 2.2 注册表定期巡检

```bash
python -m cap_hub audit --three-ring
```

遍历已注册能力，检查：
- input/output spec 是否存在且可读
- 验证脚本是否存在且可运行
- 月调用频率是否达标（从 Agent 日志统计）

不达标能力打 `status: deprecated` 标记，保留 30 天后移除。

### 2.3 与 cap_hub Phase 2 的对接点

> ⚠️ **挂起**：以下设计依赖 cap_hub Phase 2 的 Skill 注册标准到位。当前 Phase 1 的 `register()` 无门禁，本卡的判定逻辑暂时以**人工 checklist**形式运行。Phase 2 时将此 checklist 编码为 `registry.validate(cap)` → `(bool, str)`。

```python
# cap_hub/registry.py Phase 2 预期接口
def validate(cap: Capability) -> tuple[bool, str]:
    """三环过滤器。返回 (通过, 原因)。"""
    checks = [
        _check_concreteness(cap),   # 环1 务实性
        _check_testability(cap),    # 环2 可练性
        _check_valuability(cap),    # 环3 价值性
    ]
    for ok, reason in checks:
        if not ok:
            return False, reason
    return True, "三环通过"

def register(cap: Capability):
    ok, reason = validate(cap)
    if not ok:
        raise ValueError(f"能力 {cap.name} 未通过三环过滤器: {reason}")
    _registry[cap.name] = cap
```

---

## 三、常见失败模式

| 失败模式 | 卡在哪个环 | 修复 |
|---------|-----------|------|
| "通用工具"思维——想做一个万能的分析器 | 环 1 务实性 | 拆成 2-3 个场景明确的小能力 |
| 手动测过但没写验证脚本 | 环 2 可练性 | 最小验证脚本只需 5 行：给定固定输入，检查输出含预期字段 |
| 建了一个和已有能力 90% 重叠的新能力 | 环 3 价值性 | 扩展已有能力而非新建；写明与近似能力的差异 |
| 为某个一次性任务建了能力 | 环 3 价值性 | 一次性任务用临时脚本，不过早抽象为能力 |
| spec 写了但放在脑子里——只有作者知道怎么调 | 环 1 + 环 2 | 补文档 + 补验证脚本；另一个人能跑通才算通过 |

---

## 四、Critique

### 内部局限

1. **三环不是银弹**：满足三环是最低准入标准，不保证能力质量高。三环之上还需要设计评审。
2. **"高频"判定的主观性**：新能力可能调用频率低但战略价值高（如灾备恢复能力）。本卡的三环偏"高频刚需"导向，低频率高价值能力需人工 override。
3. **Phase 1 手动阶段依赖自律**：在 Phase 2 自动化之前，三环检查靠人执行，有被跳过的风险。

### 外部攻击

**过早抽象警告**：三环过滤器可能鼓励"先想清楚再写代码"——但某些能力的最优 spec 是在实际使用中浮现的。建议允许"实验性注册"（不通过三环但打 `status: experimental` 标签，30 天试用期后复审）。

---

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 有人提 PR 加新能力到 cap_hub | 跑三环 checklist | 三项全部通过或明确标记 experimental |
| `python -m cap_hub list` 输出中有 ≥5 个能力 | 启动首次 `cap_hub audit --three-ring` | 不达标能力标记 deprecated |
| 发现两个能力功能重叠 | 用环 3 的"非重复造轮子"标准判定 | 合并或明确差异后保留一个 |
| Phase 2 Skill 注册标准到位 | 把本卡的判定逻辑编码为 `registry.validate()` | 自动化拒绝不通过三环的注册 |
