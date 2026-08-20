#!/usr/bin/env python3
"""Batch skill extraction for remaining OCR sources."""
import sys, json, re
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, "/mnt/c/Users/Administrator/Knowledge Delivery OS 0.0.1")

from kdo.workspace import safe_read, ensure_dir, write_markdown, now_iso
from kdo.llm import LLMConfig, chat

root = Path("/mnt/c/Users/Administrator/Desktop/wiki")
marker_path = root / ".kdo/skill_scan_progress.json"

llm_config = LLMConfig.from_yaml()
if not llm_config.is_configured():
    llm_config = LLMConfig.from_env()

with open(marker_path, 'r') as f:
    scanned = set(json.load(f))
with open(root / ".kdo/state.json", 'r') as f:
    state = json.load(f)

today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
new_sources = [s for s in state.get("sources", []) if today_str in s.get("registered_at", "")]
remaining = [s for s in new_sources if s.get("id") not in scanned]

print(f"Remaining sources: {len(remaining)}")

SYSTEM_PROMPT = (
    "你是技能提取器。从以下口述稿/课程文本中提取所有可操作的技能。\n\n"
    "技能的定义：程序性知识——\"怎么做、什么时候做、用什么工具做\"。\n"
    "不是概念（\"什么是XX\"），不是理论，不是观点。\n\n"
    "语言模式提示：寻找以下模式——\n"
    "- 操作链：\"先...然后...接着...\"\n"
    "- 技巧声明：\"技巧就是...\" / \"我的方法是...\" / \"一个小窍门\"\n"
    "- 工具+动作：\"用XX工具...\" / \"在XX里输入...\"\n"
    "- 对比经验：\"以前我...后来发现...\"\n"
    "- 效果断言：\"...之后效果好了很多\"\n\n"
    "对每条技能，输出一个 JSON 块，格式如下：\n"
    "```json\n{\n"
    '  "name": "简短名称（动词开头）",\n'
    '  "quote": "原文引用",\n'
    '  "steps": ["步骤1", "步骤2"],\n'
    '  "when_to_use": ["✅ 场景", "❌ 不适用"],\n'
    '  "why_works": "原理说明",\n'
    '  "tools": ["需要的工具"],\n'
    '  "person": "谁说的"\n'
    "}\n```\n\n"
    "不要提取纯观点/理论。如无技能输出空数组 []。"
)

skills_found = 0
concepts_dir = root / "30_wiki" / "concepts"
ensure_dir(concepts_dir)

for i, source in enumerate(remaining):
    loc = source.get("location", "")
    if not loc:
        continue
    src_path = root / loc
    if not src_path.exists():
        continue
    source_text = safe_read(src_path, limit=80_000)
    if len(source_text) < 500:
        scanned.add(source.get("id"))
        continue
    source_id = source.get("id", "unknown")
    person = source.get("author", source.get("title", "unknown"))
    print(f"[{i+1}/{len(remaining)}] Scanning: {source_id}...")
    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"原文（{person}）：\n\n{source_text[:60_000]}"},
        ]
        raw = chat(messages, llm_config, temperature=0.3, timeout=120)
    except Exception as e:
        print(f"    LLM error: {e}")
        scanned.add(source_id)
        continue
    
    blocks = re.findall(r'```json\s*\n(.*?)\n```', raw, re.DOTALL)
    if not blocks:
        try:
            parsed = json.loads(raw)
            blocks = [json.dumps(item) for item in (parsed if isinstance(parsed, list) else [parsed])]
        except (json.JSONDecodeError, ValueError):
            scanned.add(source_id)
            continue
    
    batch_skills = 0
    for block in blocks:
        try:
            skill = json.loads(block)
        except (json.JSONDecodeError, ValueError):
            continue
        if not isinstance(skill, dict):
            continue
        name = skill.get("name", "")
        if not name:
            continue
        slug = "skill-" + re.sub(r'[^\w-]', '', name.lower().replace(' ', '-'))[:40]
        skill_path = concepts_dir / f"{slug}.md"
        if skill_path.exists():
            continue
        steps = skill.get("steps", [])
        when = skill.get("when_to_use", [])
        use_yes = [w[2:] for w in when if w.startswith("✅")]
        use_no = [w[2:] for w in when if w.startswith("❌")]
        body = (
            f"# 技能：{name}\n\n"
            f"## 原始表述\n> {skill.get('quote', '（待补充）')}\n\n"
            f"## 操作步骤\n" +
            "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps) if s) +
            "\n\n## 适用场景\n" +
            "\n".join(f"- ✅ {s}" for s in use_yes) + "\n" +
            "\n".join(f"- ❌ {s}" for s in use_no) +
            f"\n\n## 为什么有效\n{skill.get('why_works', '（待补充）')}\n\n"
            f"## 工具/环境\n" +
            "\n".join(f"- {t}" for t in skill.get("tools", ["（待补充）"])) +
            f"\n\n## 常见失败模式\n- （待补充）\n\n"
            f"## 关联技能\n- （待补充）\n\n"
            f"## 来源\n- {skill.get('person', person)}，{source_id}，{now_iso()[:10]}\n\n"
            f"## Feedback Path\n- 60_feedback/comments/ — 反馈\n"
        )
        fm = {
            "id": slug, "title": f"技能：{name}", "type": "skill",
            "status": "draft", "domain": [],
            "source_person": skill.get("person", person),
            "source_context": source_id,
            "source_refs": [source_id],
            "wiki_refs": [],
            "definition_of_done": ["操作步骤清晰可执行", "适用场景有正反例", "工具要求明确"],
            "tools_required": skill.get("tools", []),
            "prerequisite_skills": [], "related": [],
            "tags": ["#skill"],
            "created_at": now_iso(), "updated_at": now_iso(),
        }
        write_markdown(skill_path, fm, body)
        batch_skills += 1
        skills_found += 1
    
    if batch_skills > 0:
        print(f"    Created {batch_skills} skills")
    scanned.add(source_id)
    
    if (i + 1) % 5 == 0:
        with open(marker_path, 'w') as f:
            json.dump(list(scanned), f)
        print(f"  Progress saved: {len(scanned)}/{len(new_sources)}")

with open(marker_path, 'w') as f:
    json.dump(list(scanned), f)

print(f"\n=== COMPLETE ===")
print(f"Total skills created: {skills_found}")
print(f"Total scanned: {len(scanned)}/{len(new_sources)}")
