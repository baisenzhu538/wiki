---
title: "黄药师：全量跑萃取器 LLM 模式 + 候选质量验证"
assigned_to: "黄药师（Builder）"
priority: "P0"
created_at: "2026-06-01"
reviewer: "欧阳锋"
status: "pending"
depends_on: ["extract_dark_knowledge.py LLM 升级 ✅"]
blocks: ["老顽童 Phase 3 — 口述稿暗知识生产"]
---

# 黄药师：全量跑萃取器 LLM 模式 + 候选质量验证

萃取器代码已升级（+60 行，`--llm` 模式），但**还没全量跑**。当前 `60_feedback/data-quality/dk-candidates/` 下的 3 个 JSON 还是旧 regex 产出（5/31 17:58-18:56），title 全空、use_case 模板化。

需要重新跑一遍，用 LLM 精提取替换旧候选。

---

## Step 1：重新跑 3 篇口述稿

```powershell
cd C:\Users\Administrator\Desktop\wiki

python "40_outputs/capabilities/skills/data-curator/scripts/extract_dark_knowledge.py" ^
  --input "00_inbox/design/AI设计-AI设计基础01.txt" ^
  --output "60_feedback/data-quality/dk-candidates/" ^
  --llm

python "40_outputs/capabilities/skills/data-curator/scripts/extract_dark_knowledge.py" ^
  --input "00_inbox/design/AI设计-AI设计师实操培训01.txt" ^
  --output "60_feedback/data-quality/dk-candidates/" ^
  --llm

python "40_outputs/capabilities/skills/data-curator/scripts/extract_dark_knowledge.py" ^
  --input "00_inbox/design/AI设计-文创案例设计课口述.txt" ^
  --output "60_feedback/data-quality/dk-candidates/" ^
  --llm
```

> 注意：LLM 模式约 3-5 秒/条候选，3 篇约 118 条 ≈ **400-600 秒**（含 LLM 调用耗时）。建议跑 `--dry-run` 先确认 1 篇质量，再全量。

## Step 2：验证产出质量

跑完后检查：

```powershell
python -c "
import json, os, sys
root = 'C:/Users/Administrator/Desktop/wiki/60_feedback/data-quality/dk-candidates'
for f in os.listdir(root):
    if not f.endswith('.json'): continue
    with open(f'{root}/{f}', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    with_title = sum(1 for d in data if d.get('title', '').strip())
    with_ops = sum(1 for d in data if 'OPERATION_NEEDS_HUMAN' not in str(d.get('operation', '')))
    top_scores = sorted([d.get('score', 0) for d in data], reverse=True)[:3]
    print(f'{f}: {len(data)} cand, {with_title} with title, {with_ops} with ops, top_scores={top_scores}')
"
```

### 验收标准

| # | 检查项 | 合格条件 |
|:-:|:-------|:---------|
| 1 | 3 篇全部跑完 | `dk-candidates/` 下 3 个 JSON 文件更新时间在本次执行之后 |
| 2 | title 有值 | 不是 `""`，比例 > 80% |
| 3 | operation 有值 | `[OPERATION_NEEDS_HUMAN]` 比例 < 30%（相比旧版 ~95%） |
| 4 | score 拉开差距 | 分布在 0.2-0.9，不是全部 0.5-0.6 |
| 5 | 不满足验收标准 → 调 `LLM_EXTRACT_PROMPT` 重跑 |

## Step 3：通知老顽童

通过 `70_product/tasks/task-20260601-laowantong-three-tasks.md` 末尾追加一行：

```
📦 AI设计口述稿暗知识候选已就绪（LLM 模式）→ 60_feedback/data-quality/dk-candidates/
  共 3 篇，约 N 条候选。按 score 从高到低取，预计产出 ~15 张暗知识卡。
```
