---
id: dk-feature-registry-count-drift
title: Feature 注册表数量漂移：引用数字的文档系统性滞后
type: dk
status: draft
domain:
- kdo
- ai-collaboration
author: agent-basic-skills-coach
reviewed_by: 待审
confidence: 0.88
trust_level: medium
aliases:
- Feature数量漂移
- 注册表漂移
- 数字文档滞后
- features.json漂移
discoverable_by:
- Feature数量漂移
- 注册表漂移
- 文档滞后
- features.json
source_refs:
- cap_hub/features.json
- 30_wiki/bridges/bridge-dual-track-feature-system.md
- 30_wiki/concepts/concept-kdo-feature-registry.md
diagnostic_signals:
- signal: 引用 features.json 数量的文档（bridge 卡/concept 卡/skill）写 12/13 条，实际已是 20 条
  severity: medium
  implication: KDO 基建在增长（13→20 只用了约一周），所有引用具体数字的文档都会周期性过时——查证必须先读 features.json，不凭任何中间文档
- signal: 修 skill 时只改了主 SKILL.md 和 memory，漏掉 skill 的 references/ 子文件（E004 二次残留）
  severity: medium
  implication: 技能内化体检必须 grep 整个 skill 目录（主文件+子文件），不能只 patch 主文件——'同步三处'要扩成'同步四处'
related:
- '[[dk-agent-access-kdo-pitfalls]]'
- '[[dk-c8-format-complete-mind-empty]]'
- '[[bridge-dual-track-feature-system]]'
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
- audience:builder
- scene:reference
- skill-level:advanced
- agent:hermes
---

# Feature 注册表数量漂移：引用数字的文档系统性滞后

> 一句话：KDO 的 cap_hub/features.json 是活的——13→20 条只用了一周。任何引用"有几个 Feature"的文档（bridge 卡、concept 卡、skill 主文件、skill references 子文件）都会同步滞后。数字唯一真相源是 features.json 本身，不是任何中间文档。

## 原始表述/核心洞察

2026-08-16 技能内化体检（coach-session-review 流程 B），对照 features.json 与三处引用文档，发现系统性漂移：

- `bridge-dual-track-feature-system.md`：写 "12 个 quality-gate Feature"（实际 20）
- `concept-kdo-feature-registry.md`：写 "12 个已注册 Feature"+ 12 行表格（实际 20 条）
- `kdo-knowledge-base/SKILL.md`：写 "13 quality-gate Features, 4 categories"（实际 20 条、3 类 lint/cli/ux）
- `kdo-knowledge-base/references/quality-gate-features.md`：写 "GBK-encoded, 13 features"——**E004（编码误判）的二次残留**：2026-08-09 已把主 SKILL.md 和 memory 改成 UTF-8，但漏了 references 子文件

## 使用场景

1. 任何 Agent 回答"KDO 有哪些质量门禁 Feature / 有几个 Feature"——先读 features.json，不凭 skill/bridge/concept 卡
2. 每周技能内化体检——把"Feature 数量对账"列为固定检查项
3. 修改 skill 时——grep 整个 skill 目录（含 references/ 子文件），不只主文件

## 操作方法

```bash
cd /mnt/c/Users/Administrator/Desktop/wiki
python3 -c "import json; d=json.load(open('cap_hub/features.json',encoding='utf-8')); print(len(d['features']), sorted(d['features'].keys()))"
```

## 适用边界

- 只适用于"数量/枚举类事实"的漂移检查；方法论结论（双轨不可混编）不会因数量变化失效
- features.json 结构变化时（比如 category 分类改名），检查比数量更严重——需同时核对 key 名

## 为什么值钱

- 数量漂移是"看不见的坏"：不主动对账永远不知道文档过期，等引用时才发现
- 教训可泛化：**凡是"唯一真相源"在持续增长的基建，所有引用它的数字文档都必须标记"以源为准"或定期对账**

## 对既有知识的贡献

- 扩展 dk-agent-access-kdo-pitfalls：从"接入三连坑"扩展到"接入后文档维护坑"
- 纠正 coach-session-review 流程 B 的"同步三处"→"同步四处"（+ skill references 子文件）

## Critique（自我批判）

- 本卡本身也是"引用数字的文档"——如果 features.json 再增长，本卡也会过时。防御：本卡不写死具体数量，只描述漂移模式与对账方法（数量在 diagnostic_signals 里作为历史案例，不承诺当前值）。
