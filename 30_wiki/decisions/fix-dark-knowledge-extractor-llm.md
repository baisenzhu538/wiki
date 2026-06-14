---

id: "fix-dark-knowledge-extractor-llm"
title: "萃取器升级：regex → LLM-based 暗知识提取"
type: "improvement-plan"
status: "pending"
domain:
  - "master"
created_at: 2026-05-31
updated_at: 2026-05-31
target_roles:
  - "黄药师（Builder）"
reviewer: "欧阳锋（Architect）"
related:
  - "task-20260531-huangyaoshi-extractor-run-all"
  - "plan_20260531_data-curator-v1.3"
author: "legacy"
source_context: "60_feedback/data-quality/dk-candidates/"
source_refs: []
reviewed_by: "pending"
confidence: 0.75
trust_level: "medium"
---

# 萃取器升级：regex → LLM-based 暗知识提取

> **问题**：`extract_dark_knowledge.py` 纯 regex 方案提取的 118 条候选质量不可接受。
>   - title 全部为空
>   - use_case 模板化（"在使用 X 的场景中"）
>   - operation 几乎全缺
>   - score 压缩在 0.50-0.60 区间
>
> **方案**：保持 regex 预筛（定位候选区间），增加 LLM 精提取阶段（填充 6 字段 + 评分）。
>
> **配置**：走 `~/.kdo/config.yaml` 里配的 LLM（当前是 Kimi，可随时切 DeepSeek）。

---

## 升级方案

### 核心改动

在 `extract_dark_knowledge.py` 中新增 `llm_extract_candidate()` 函数，对每个 regex 筛出的 segment 做 LLM 精提取：

```
regex 预筛（已有的） → 对每个 segment 调 LLM 精提取（新增） → 写 JSON（已有的）
    定位候选区间          填充6字段 + 评分              结构不变
```

**不打乱现有代码结构**。原来的 regex 路径保留为 fallback（`--no-llm` 或 LLM 未配置时）。

---

### Step 1：新增 import + fallback 逻辑

```python
# 文件顶部加
from pathlib import Path

KDO_CLI = Path(r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo")
sys.path.insert(0, str(KDO_CLI.parent))

from kdo.llm import LLMConfig, chat

# 新增命令行参数
parser.add_argument("--llm", action="store_true", default=True,
    help="Use LLM for candidate refinement (default: True)")
parser.add_argument("--no-llm", action="store_true",
    help="Use regex-only extraction (fallback)")
```

---

### Step 2：新增 prompt

```python
LLM_EXTRACT_PROMPT = """你是一个暗知识萃取专家。分析以下从口述稿中提取的原始片段，判断它是否包含值得入库的暗知识。

一条好的暗知识应该是：
1. 具体的、可执行的（不是泛泛的道理）
2. AI 训练语料中不存在的（不是公开常识）
3. 独立可读的（不需要看上下文就明白在说什么）

原始片段：
---
{segment}
---

请判断这条片段所属的类型（在下面 4 类中选择最匹配的一类）：
- tool_usage：具体工具配置技巧、集成方式、使用窍门
- failure：错误、踩坑、教训、"不要做"类经验
- insight：个人专业判断、金句、反常识洞察
- workflow：具体操作流程、步骤序列

返回严格的 JSON 格式（不要 markdown 标记）：
{{
  "is_valid": true/false,
  "title": "简短标题（10字以内，用'：'分隔主题和内容）",
  "dark_knowledge_type": "tool_usage|failure|insight|workflow",
  "original_quote": "保留原文中最有价值的那段引文",
  "use_case": "具体到'谁、在什么情况下'需要用到这条知识",
  "operation": "具体的操作步骤",
  "boundary": "什么情况下不适用，或与哪种易混淆模式的区别",
  "why_valuable": "为什么 AI 训练语料里没有这条知识",
  "cross_reference": "可能关联的概念或工具名",
  "score": 0.0-1.0,
  "score_reason": "一句话说明评分理由"
}}

如果 is_valid 为 false，除 score 和 score_reason 外其他字段可以为空。
"""
```

---

### Step 3：新增 LLM 提取函数

```python
import json
import re

def llm_extract_candidate(segment: str, cfg: LLMConfig) -> dict | None:
    """Use LLM to extract and refine a dark knowledge candidate."""
    prompt = LLM_EXTRACT_PROMPT.format(segment=segment[:2000])
    try:
        response = chat(
            [{"role": "user", "content": prompt}],
            config=cfg,
            temperature=0.1,
        )
        json_match = re.search(r"\{.*\}", response, re.DOTALL)
        if not json_match:
            return None
        result = json.loads(json_match.group(0))
        if not result.get("is_valid", False):
            return None
        return result
    except Exception as exc:
        print(f"  LLM extraction failed: {exc}", file=sys.stderr)
        return None
```

---

### Step 4：修改 main 中的处理流程

当前主循环：

```python
for segment in candidate_segments:
    dk_type = classify_segment(segment)
    score = score_candidate(segment, dk_type)
    candidates.append({
        "title": "",
        "dark_knowledge_type": dk_type,
        "score": score,
        ...
    })
```

改为：

```python
cfg = _load_llm_config() if use_llm else None

for segment in candidate_segments:
    if cfg and cfg.is_configured():
        refined = llm_extract_candidate(segment, cfg)
        if refined:
            candidates.append({
                "title": refined.get("title", ""),
                "dark_knowledge_type": refined.get("dark_knowledge_type", classify_segment(segment)),
                "source_person": source_person,
                "source_context": source_context,
                "score": refined.get("score", 0.0),
                "original_quote": refined.get("original_quote", segment),
                "use_case": refined.get("use_case", ""),
                "operation": refined.get("operation", "[OPERATION_NEEDS_HUMAN]"),
                "boundary": refined.get("boundary", ""),
                "why_valuable": refined.get("why_valuable", ""),
                "cross_reference": refined.get("cross_reference", ""),
            })
    else:
        # Fallback: regex-only (existing path)
        ...
```

---

### Step 5：LLM 配置加载函数

```python
def _load_llm_config() -> LLMConfig | None:
    try:
        cfg = LLMConfig.from_yaml()
        if cfg.is_configured():
            return cfg
    except Exception:
        pass
    return None
```

---

## 验收标准

| # | 验收项 | 判定 |
|:-:|:------|:----:|
| 1 | 不加 `--no-llm` 时走 LLM 路径 | title 有值，不是 `""` |
| 2 | title 有意义 | 不是模板文本，能概括该条候选的核心 |
| 3 | use_case 具体 | 不是"在使用 X 的场景中"这种模板 |
| 4 | score 拉开差距 | 分布在 0.2-0.9 区间，不是全部 0.5-0.6 |
| 5 | is_valid=false 的候选被过滤 | 输出条数比 regex-only 少（118 → 预估 ~50） |
| 6 | `--no-llm` 时行为不变 | 和当前输出一致 |
| 7 | 不改输出 JSON 格式 | 老顽童可以直接取用 |

---

## 文件改动

| 文件 | 改动量 | 说明 |
|------|:-----:|------|
| `extract_dark_knowledge.py` | +~80 行 | 新增 prompt + llm_extract_candidate + config加载 + 流程修改 |
| `~/.kdo/config.yaml` | 不变 | 沿用已有 Kimi/DeepSeek 配置 |

**不改已有 regex 路径**，`--no-llm` 和 LLM 未配置时行为完全不变。

---

## 执行

```powershell
python extract_dark_knowledge.py --input "00_inbox/design/AI设计-AI设计基础01.txt" --dry-run --llm
# 确认产出质量
python extract_dark_knowledge.py --input "00_inbox/design/AI设计-AI设计基础01.txt" --output "60_feedback/data-quality/dk-candidates/" --llm
```

3 篇口述稿跑完预计 5-10 分钟（LLM 调用约 3-5 秒/条，118 条候选约 400-600 秒）。

---

*欧阳锋 · 2026-05-31*
