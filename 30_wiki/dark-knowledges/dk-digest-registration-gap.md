---
id: dk-digest-registration-gap
title: 导航卡注册缺口：SOUL 内嵌引用 ≠ 已注册进 digest/MOC
type: dk
status: draft
domain:
- human-insights
- kdo
author: coaching-leadership-assistant
reviewed_by: 待审
confidence: 0.9
trust_level: medium
aliases:
- digest注册缺口
- 卡没挂导航
- 内嵌引用未注册
- 检索链路断点
- 孤儿卡
discoverable_by:
- digest注册
- 导航卡缺口
- 孤儿卡
- 检索链路
- 卡未注册
source_refs:
- 30_wiki/domains/human-insights-domain-digest.md
- agents/coaching-leadership-assistant/SOUL.md
- 30_wiki/cases/case-morfei-semiconductor.md
- 30_wiki/tools/tool-coaching-communication-four-layers.md
diagnostic_signals:
- signal: SOUL/agent-spec 内嵌引用了一批核心卡，但主 digest 只注册了其中一部分，另一部分只挂在别的 digest 或完全没人引用
  severity: high
  implication: 检索链路断点——按"先读 digest 再取卡"的标准路径，孤儿卡永远走不到，语义检索（kdo_search）也依赖 digest/MOC 索引；卡片存在但不可达
- signal: 卡文件存在（ls 能看见）但 grep 不到任何 digest/MOC 引用
  severity: high
  implication: "存在"不等于"注册"——2026-08-23 周检实测 12 张核心卡中 7 张无人域 digest 引用（case-coaching-dialogue-three-versions / dk-y-model-communication / tool-coaching-communication-four-layers / tool-coaching-communication-segments 完全孤儿，case-morfei-semiconductor / dk-coaching-monkey-theory / dk-coaching-boundary-conditions 只挂在 management digest）
related:
- '[[dk-feature-registry-count-drift]]'
- '[[dk-agent-access-kdo-pitfalls]]'
created_at: 2026-08-23
updated_at: 2026-08-23
tags:
- audience:builder
- scene:reference
- skill-level:advanced
- agent:hermes
---

# 导航卡注册缺口：SOUL 内嵌引用 ≠ 已注册进 digest/MOC

> 一句话：写 SOUL/agent-spec 时把卡"内嵌引用"了，不等于把卡"注册进 digest/MOC"了。卡文件存在但不在任何导航表里 = 孤儿卡，检索链路走不到。2026-08-23 周检实测：教练式领导力 SOUL 内嵌 12 张核心卡，人域 digest 只注册 5 张。

## 原始表述/核心洞察

2026-08-23 每周技能内化体检（coach-session-review 流程 B），对照 SOUL.md 内嵌引用清单与 `human-insights-domain-digest.md` 实际注册表，发现系统性缺口：

- SOUL 内嵌引用 12 张核心资产卡（五阶梯/硬币模型/倾听提问反馈/21卡牌/段位/猴子理论/边界三情况/Y模型/莫非/三版本对话…）
- 人域 digest 块 2 只注册了 5 张（framework × 3 + tool 倾听/提问/反馈 + 三类下属/共识目标…）
- **7 张未注册到人域 digest**：
  - 完全孤儿（任何 digest/MOC 都 grep 不到）：`case-coaching-dialogue-three-versions` / `dk-y-model-communication` / `tool-coaching-communication-four-layers` / `tool-coaching-communication-segments` / `bridge-coaching-leadership-feature-layered` / `bridge-how-to-know-person-to-business`
  - 半孤儿（只挂在别的域 digest）：`case-morfei-semiconductor` / `dk-coaching-monkey-theory` / `dk-coaching-boundary-conditions`（挂在 management-domain-digest，人域入口走不到）

**修复动作**：把 9 张卡补注册进人域 digest（块 1 +1 bridge、块 2 +8 卡），updated_at 2026-08-23。教训：**写卡不注册 = 白写；agent-spec 内嵌引用不核对 digest = 引用了个寂寞**。

## 使用场景

1. 任何 Agent 写/改 SOUL 或 agent-spec 内嵌引用后——必须核对主 digest/MOC 是否已注册该卡
2. 每周技能内化体检——把"SOUL 引用清单 × digest 注册表对账"列为固定检查项（grep 双向验证）
3. 新建卡时——建卡即注册：写完卡立刻挂进对应 digest/MOC 的导航表，不留孤儿期

## 操作方法

```bash
cd /c/Users/Administrator/Desktop/wiki/30_wiki
# ① 列出 SOUL 内嵌引用的卡
grep -o '`30_wiki/[a-z-]*/[a-z0-9-]*\.md`' ../agents/coaching-leadership-assistant/SOUL.md | sed 's/.*\///;s/\.md//'
# ② 反向 grep：每张卡是否被任何 digest/MOC 引用
for f in case-morfei-semiconductor dk-y-model-communication tool-coaching-communication-four-layers; do
  echo "--- $f ---"; grep -rln "$f" domains/ bridges/ | head -3
done
# ③ 孤儿卡 → 补注册进对应 digest 导航表（patch），并更新 updated_at
```

## 适用边界

- 本坑针对"导航卡（digest/MOC/index）"；`30_wiki/bridges/` 下的桥接卡语义上已带"跨域"性质，容易被各域 digest 都漏掉，尤其要查
- 部分卡挂在别的域 digest 算"半可达"——语义检索可能命中，但按"先读主 digest 再取卡"的规范路径走不到，仍算缺口
- 只适用于检索可达性问题；卡片内容质量（格式/理解深度）是另一套门禁（见 dk-c8）

## 为什么值钱

- 缺口是"静默的坏"：卡建了、审了、甚至被 SOUL 引用了，但用户问题永远走不到它——知识资产在库但不可用
- 教训可泛化：**任何"内嵌/引用/提及"都不等于"注册"，检索可达性必须用 grep 双向实测，不能凭印象**

## 对既有知识的贡献

- 扩展 dk-feature-registry-count-drift：从"数量漂移"扩展到"引用≠注册"的导航完整性维度
- 给 coach-session-review 流程 B 增加固定检查项：SOUL 引用清单 × digest 注册表对账

## Critique（自我批判）

- 本卡写的是 2026-08-23 时刻的缺口快照，缺口修复后具体卡名会过时——防御：本卡保留"对账方法"作为持久价值，具体卡名只作为历史案例；定期体检以实时 grep 为准
