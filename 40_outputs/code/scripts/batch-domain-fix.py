"""批量补 domain 标签——基于 ID 前缀推断域。dry-run 预览，不加参数执行。"""
import re, sys
from pathlib import Path

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

PREFIX_MAP = {
    # AI 协作
    "skill-Truman": ["ai-collaboration", "yitang"],
    "skill-ban-fei-mao": ["ai-collaboration", "yitang"],
    "skill-半肥猫": ["ai-collaboration", "yitang"],
    "skill-纪浩": ["ai-collaboration", "yitang"],
    "skill-马易": ["ai-collaboration", "yitang"],
    "sk-ai": ["ai-collaboration", "yitang"],
    "skill-ai": ["ai-collaboration", "yitang"],
    "voice-input": ["ai-collaboration"],
    "framework-wanghuan": ["ai-collaboration", "yitang"],
    "tool-wanghuan": ["ai-collaboration", "yitang"],
    # 决策
    "skill-cognitive-bias": ["decision"],
    "skill-decision": ["decision"],
    "skill-三阶追问": ["decision"],
    "skill-对标借鉴": ["decision"],
    "skill-战略博弈": ["decision"],
    "skill-设定管理杠杆率": ["decision"],
    "skill-设计对抗": ["decision"],
    "skill-通过综合案例": ["decision"],
    "skill-稀缺资源": ["decision"],
    "framework-structured": ["research"],
    "skill-专家访谈": ["research"],
    # 设计
    "skill-月白": ["design"],
    "skill-马易-AIGC": ["design"],
    "yt-tool-ai-ppt": ["design"],
    # 内容生产
    "skill-李诞": ["content-production"],
    "yt-pitch": ["content-production"],
    "yt-skill-storyline": ["content-production"],
    "framework-candy": ["content-production"],
    "skill-清单式": ["content-production"],
    "skill-自我反馈": ["content-production"],
    "skill-获取他人反馈": ["content-production"],
    "skill-逐字稿": ["content-production"],
    "skill-知识库团队": ["content-production"],
    # 学习方法
    "skill-note": ["learning-methodology"],
    "skill-专题笔记": ["learning-methodology"],
    "skill-费曼": ["learning-methodology"],
    "skill-复盘推演": ["learning-methodology"],
    "skill-分享输出": ["learning-methodology"],
    "skill-立即实践": ["learning-methodology"],
    "skill-四层联系": ["learning-methodology"],
    "skill-三层目标": ["learning-methodology"],
    "skill-主动摘要": ["learning-methodology"],
    "skill-动手建模": ["learning-methodology"],
    "skill-逆向教学": ["learning-methodology"],
    "skill-反向记录": ["learning-methodology"],
    "skill-反向采访": ["learning-methodology"],
    "skill-反向提示": ["learning-methodology"],
    "skill-建立知识": ["learning-methodology"],
    "skill-提升笔记": ["learning-methodology"],
    "skill-深度分层": ["learning-methodology"],
    "skill-清单小抄": ["learning-methodology"],
    "skill-思维链": ["learning-methodology"],
    "skill-思维验证": ["learning-methodology"],
    "skill-辩证讨论": ["learning-methodology"],
    "skill-按分阶练习": ["learning-methodology"],
    "skill-从案例中学习": ["learning-methodology"],
    "skill-体系框架": ["learning-methodology"],
    "skill-知识树": ["learning-methodology"],
    "skill-用topdown": ["learning-methodology"],
    "skill-用清单体": ["learning-methodology"],
    "skill-现场建模": ["learning-methodology"],
    "skill-通过请吃饭": ["learning-methodology"],
    "skill-项目复盘": ["learning-methodology"],
    "skill-使用优先级快筛": ["learning-methodology"],
    "skill-使用概念辨析": ["learning-methodology"],
    "skill-使用一页纸速查": ["learning-methodology"],
    "skill-制作行业化": ["learning-methodology"],
    "skill-封装可复用": ["learning-methodology"],
    "skill-按图索骥": ["learning-methodology"],
    "skill-多轮确认": ["learning-methodology"],
    "skill-多模型对比": ["learning-methodology"],
    "skill-反向教学深化": ["learning-methodology"],
    "skill-数据分层": ["learning-methodology"],
    "skill-提示词结构化": ["learning-methodology"],
    "skill-增强数据": ["learning-methodology"],
    "skill-模型匹配": ["learning-methodology"],
    "skill-模型组合": ["learning-methodology"],
    "skill-渐进式披露": ["learning-methodology"],
    "skill-敏捷发布": ["learning-methodology"],
    "yt-note": ["learning-methodology"],
    # 个人修养
    "skill-水水": ["personal-growth", "decision"],
    "yt-personal": ["personal-growth"],
    "skill-人生红点": ["personal-growth"],
    "skill-创始人二当家": ["entrepreneurship"],
    "skill-城市合伙人": ["entrepreneurship"],
    "skill-快招品牌": ["entrepreneurship"],
    "skill-推行分层标准化": ["entrepreneurship"],
    "skill-采用滚动预测": ["entrepreneurship"],
    "skill-遵循规模前倾": ["entrepreneurship"],
    "skill-应用人员降级": ["entrepreneurship"],
    "skill-将未中标成本纳入": ["entrepreneurship"],
    "skill-按月份摊销": ["entrepreneurship"],
    "skill-用旗舰店替代": ["entrepreneurship"],
    "skill-任务拆解为工作流": ["entrepreneurship"],
    "skill-执行对标研究三步法": ["entrepreneurship"],
    # 产品/泛产品
    "yt-panproduct": ["product"],
    "yt-product": ["product"],
    "framework-demand": ["demand-analysis"],
    # ToB
    "yt-tob": ["yitang"],
    # 商业
    "yt-business-formula": ["yitang"],
    "yt-business-model": ["business-model"],
    "yt-composite": ["yitang"],
    "yt-entrepreneur": ["entrepreneurship"],
    "yt-lean": ["lean-startup"],
    "yt-model": ["modeling"],
    "modeling": ["modeling"],
    "model-quality": ["modeling"],
    "yt-barrier": ["barrier"],
    "yt-growth": ["growth"],
    "yt-decision": ["decision"],
    "yt-demand": ["demand-analysis"],
    "yt-market-size": ["yitang"],
    "yt-management": ["management"],
    "yt-scale-economy": ["yitang"],
    "yt-tool": ["yitang"],
    "yt-unit-model": ["yitang"],
    "yt-research": ["research"],
    "framework-ci": ["yitang"],
    "framework-course": ["yitang"],
    "framework-doris": ["research"],
    "framework-logic": ["yitang"],
    "framework-learning": ["learning-methodology"],
    "framework-multi-agent": ["ai-collaboration", "yitang"],
    "skill-react": ["ai-collaboration"],
    "master": ["master"],
    "concept-maister": ["management"],
    "concept-mckinsey": ["management"],
    "concept-minto": ["management"],
    "concept-toyota": ["management"],
    "beverage-foodservice": ["yitang"],
    "business-formula": ["yitang"],
    "ai-native": ["ai-saas"],
    "ai-complex": ["ai-saas"],
    "ai-short-drama": ["ai-saas"],
    "sales-pitch": ["yitang"],
    "shanxi-field": ["research"],
    "smart-device": ["yitang"],
    "smart-medicine": ["healthcare"],
    "xingangwan": ["healthcare"],
    "yitang-strategy-canvas": ["yitang"],
    "skill-1视角升级思考法": ["learning-methodology"],
    "skill-6维窗口期扫描法": ["decision"],
    "skill-学会提问": ["learning-methodology"],
}

def parse_fm(text):
    if not text.startswith("---"): return None, 0
    end = text.find("---", 3)
    if end == -1: return None, 0
    fm = {}
    for line in text[3:end].split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if v.startswith("[") and v.endswith("]"):
                fm[k] = [it.strip().strip('"').strip("'") for it in v[1:-1].split(",") if it.strip()]
            elif v == "":
                fm[k] = []
            else:
                fm[k] = v
    return fm, end

def should_fix(fm):
    dom = fm.get("domain", [])
    if isinstance(dom, str): dom = [dom]
    if not dom or dom == [] or dom == [""] or dom == ["[]"]:
        return True
    # Also fix if unknown or empty
    if "unknown" in dom or "" in dom:
        return True
    return False

def infer_domain(card_id):
    for prefix, domains in sorted(PREFIX_MAP.items(), key=lambda x: -len(x[0])):
        if card_id.startswith(prefix):
            return domains
    # Fallback: check if it's a skill-* or yt-* without prefix match
    if card_id.startswith("skill-") or card_id.startswith("sk-"):
        return ["learning-methodology"]
    if card_id.startswith("yt-"):
        return ["yitang"]
    return None

def fix_file(fpath, dry_run=False):
    text = fpath.read_text(encoding="utf-8")
    fm, end = parse_fm(text)
    if fm is None or "id" not in fm:
        return None
    if not should_fix(fm):
        return None
    cid = fm["id"]
    domains = infer_domain(cid)
    if domains is None:
        return None
    new_dom = domains
    # Format: domain:\n  - d1\n  - d2
    dom_lines = "domain:\n"
    for d in new_dom:
        dom_lines += f"  - {d}\n"
    # Insert or replace domain in frontmatter
    fm_text = text[3:end]
    rest = text[end+3:]
    if "\ndomain:" in fm_text or fm_text.startswith("domain:"):
        new_fm = re.sub(r'^domain:.*$(\n(?:  -.*\n?)*)?', dom_lines.rstrip(), fm_text, flags=re.MULTILINE)
    else:
        new_fm = fm_text.rstrip() + "\n" + dom_lines.rstrip()
    new_text = "---\n" + new_fm + "\n---" + rest
    if not dry_run:
        fpath.write_text(new_text, encoding="utf-8")
    return new_dom

if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    fixed = 0
    skipped = 0
    for f in WIKI.rglob("*.md"):
        if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
            continue
        try:
            result = fix_file(f, dry_run=dry_run)
            if result is not None:
                cid = None
                try:
                    t = f.read_text(encoding="utf-8")[:500]
                    m = re.search(r'^id:\s*(.+)$', t, re.MULTILINE)
                    if m: cid = m.group(1).strip()
                except: pass
                print(f"  {'[DRY-RUN]' if dry_run else '[FIX]'} {cid or f.stem} -> {result}")
                fixed += 1
        except Exception as e:
            skipped += 1
    print(f"\n{'[DRY-RUN]' if dry_run else ''} 修复: {fixed} | 跳过: {skipped}")
