#!/usr/bin/env python3
"""#229 — rebuild frontmatter for 17 historically corrupted cards (GBK damage pre-7/27)"""
import re, yaml
from pathlib import Path

root = Path(r'C:\Users\Administrator\Desktop\wiki')

cards = {
    '30_wiki/cases/case-yihang-dual-triangle-一堂双三角-IP选题智能体挑战交付上限.md': {
        'title': '双三角案例：Vikki IP 选题智能体——跳出 AI 工具回到业务视角',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-一堂双三角-图书分析AI工具.md': {
        'title': '双三角案例：刘凯图书分析 AI 工具——RAG+审美驱动畅销书分析',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-一堂双三角-教育新官网制作.md': {
        'title': '双三角案例：一堂教育新官网——审美驱动 AI 协作',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-一堂双三角-数字化营销提效十倍.md': {
        'title': '双三角案例：牟肥猫数字化营销 AI 提效十倍——100+Agent + 20+卡片',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-一堂双三角-跨行业速解工业级难题.md': {
        'title': '双三角案例：花总跨行业速解工业级难题——人和 AI 先造数据',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-一堂双三角-龙虾训练实验.md': {
        'title': '双三角案例：龙虾训练灵魂赋能实验——Agent 角色配置',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-天末的双三角模型.md': {
        'title': '双三角案例：天末室内设计——AI 辅助从调研到效果图直出',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-组织-硬件公司-AI专利落地案例.md': {
        'title': '双三角案例：硬件公司 AI 专利落地——规则显性化与一号位决心',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-组织-酒店行业-AI标签审核案例.md': {
        'title': '双三角案例：酒店 AI 标签审核——边缘切入与沙盒练兵',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-dual-triangle-阿豪的双三角模型.md': {
        'title': '双三角案例：阿豪电商选品——内网穿透与 AI 自动化',
        'domain': ['ai-collaboration', 'panproduct'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/cases/case-yihang-truman-aesthetic-library-practices.md': {
        'title': '案例：Truman 审美库建设实践——10+ 领域一年速建判断力',
        'domain': ['panproduct', 'modeling'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/tools/tool-Truman-Feature特性层训练法.md': {
        'title': 'Feature 特性层训练法：把 AI 基本功拆成可测试的最小单元',
        'domain': ['ai-collaboration'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/tools/tool-clinic-medical-shortvideo-compliance.md': {
        'title': '诊所医疗短视频/个人 IP 合规边界',
        'domain': ['healthcare'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/tools/tool-smart-medicine-cabinet-site-selection-guide.md': {
        'title': '智能药柜选址深度指南：场景、指标与验证方法',
        'domain': ['healthcare'],
        'author': '洪七公（VLM提取） 老顽童（enrich）',
    },
    '30_wiki/frameworks/framework-strategy-brm.md': {
        'title': '冉鹏版 BRM 框架（源于 IBM BLM 方法论）',
        'domain': ['strategy'],
        'author': '老顽童',
    },
    '30_wiki/frameworks/framework-yitang-project-abcd-classification.md': {
        'title': '项目ABCD复杂度分类：工具跟着复杂度走',
        'domain': ['management'],
        'author': '老顽童',
    },
    '30_wiki/frameworks/framework-yitang-project-breakdown.md': {
        'title': '项目拆计划：六维敏感度驱动的科学拆解',
        'domain': ['management'],
        'author': '老顽童',
    },
}

rebuilt = 0
for path, meta in cards.items():
    fp = root / path
    t = fp.read_text(encoding='utf-8', errors='replace')
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', t, re.DOTALL)
    body = t[m.end():] if m else t

    card_id = fp.stem
    card_type = 'case' if '/cases/' in path else ('tool' if '/tools/' in path else 'framework')
    wikilinks = list(set(re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', body)))[:15]

    fm = f'---\nid: {card_id}\ntitle: "{meta["title"]}"\ntype: {card_type}\nstatus: draft\ndomain:\n'
    for d in meta['domain']: fm += f'  - {d}\n'
    fm += f'author: {meta["author"]}\nreviewed_by: 待审\nconfidence: 0.7\ntrust_level: low\n'
    fm += 'source_refs:\n  - src_unknown\nrelated:\n'
    for w in wikilinks: fm += f'  - [[{w}]]\n'
    fm += f'created_at: 2026-06-30\nupdated_at: 2026-08-04\n'
    fm += 'tags:\n  - audience:general\n  - scene:reference\n  - skill-level:intermediate\n'
    fm += f'aliases:\n  - {meta["title"]}\n'
    fm += f'discoverable_by:\n  - {meta["title"]}\n'
    fm += '---\n'
    new_text = fm + body

    m2 = re.match(r'^---\s*\n(.*?)\n---\s*\n', new_text, re.DOTALL)
    try:
        yaml.safe_load(m2.group(1))
        fp.write_text(new_text, encoding='utf-8')
        rebuilt += 1
        print(f'OK: {fp.name}')
    except Exception as e:
        print(f'FAIL: {fp.name} — {e}')

print(f'\nRebuilt: {rebuilt}/{len(cards)}')
