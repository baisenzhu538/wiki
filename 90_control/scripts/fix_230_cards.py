#!/usr/bin/env python3
"""#230 — fix 6 cards: add ds + positioning + related>=5 + missing sections"""
import re, yaml
from pathlib import Path

root = Path(r'C:\Users\Administrator\Desktop\wiki')

fixes = {
    '30_wiki/dark-knowledges/dk-E010-duplicate-key-detection.md': {
        'ds': "diagnostic_signals:\n  - signal: '#222/#223事故后lint仍无重复键检测——DUPLICATE_KEY门禁缺失'\n    severity: critical\n    implication: '任何老顽童提交的双aliases卡片都不会被拦截——事故会重演'\n  - signal: '存量131张卡含重复键——现在提交都不会被拦'\n    severity: high\n    implication: '王语嫣验证：lint确实无同文件重复键检测'\n  - signal: '欧阳锋洞察：一行正则即可永久封堵事故根因模式'\n    severity: low\n    implication: '实现成本极低——与F3同模式'\n",
        'related': "  - '[[concept-kdo-component-library]]'\n  - '[[framework-kdo-self-attack]]'\n  - '[[dk-c8-format-complete-mind-empty]]'\n  - '[[dk-P42-agent-fact-check-gap]]'\n  - '[[dk-delivery-path-type-bug]]'\n  - '[[dk-c5-todo-false-positive]]'\n",
        'positioning': "> **定位**：属于 KDO 事故教训库的 E 系列——E010 是 #222/#223 并行写入事故的终极防线缺口。与 #217 F3（跨文件重复 ID 检测）同模式、同文件。\n",
    },
    '30_wiki/dark-knowledges/dk-P42-agent-fact-check-gap.md': {
        'ds': "diagnostic_signals:\n  - signal: 'Agent凭记忆断言文件历史状态——无git命令附证'\n    severity: high\n    implication: '王语嫣初判dk-yi-tang为历史遗留→欧阳锋git字节验证推翻→错误处置差点被采纳'\n  - signal: '跨Agent事实争议无标准裁决流程——靠谁说的有道理'\n    severity: high\n    implication: '王语嫣vs欧阳锋各执一词→无git字节证据→争论升级'\n  - signal: '审查者收到异议后倾向辩论而非验证——1秒能终结的问题争论了30分钟'\n    severity: medium\n    implication: '浪费审查轮次，延误处置决策'\n",
        'related': "  - '[[dk-E010-duplicate-key-detection]]'\n  - '[[framework-kdo-self-attack]]'\n  - '[[workflow-cross-agent-fact-dispute]]'\n  - '[[dk-P15-false-completion-report]]'\n  - '[[framework-kdo-modeling-methodology]]'\n  - '[[dk-c5-todo-false-positive]]'\n",
        'positioning': "> **定位**：属于 KDO 事故教训库的 P 系列——P-42 是 #224 终审分歧暴露的核查方法论缺陷。与 workflow-cross-agent-fact-dispute（争议裁决协议）配套使用。\n",
        'extra_section': ('## 与其他知识的关联\n\n'
            '- dk-E010-duplicate-key-detection → 同源：都是 Agent 断言需要独立验证\n'
            '- workflow-cross-agent-fact-dispute → 配套：争议裁决的标准协议\n'
            '- P-15（声称完成但实际未做）→ 同模式：Agent 的断言需要独立验证\n'
            '- #224 终审分歧 → 直接来源\n'
            '- framework-kdo-modeling-methodology → 牌 #14（先跑脚本确认再下结论）= 同构\n\n'),
    },
    '30_wiki/dark-knowledges/dk-delivery-path-type-bug.md': {
        'ds': "diagnostic_signals:\n  - signal: 'kdo_search对所有人返回0结果——BM25+Graph双路径沉默失败'\n    severity: critical\n    implication: '小昭搜创新者的窘境永远0结果——不只是索引过期，是入口坏了'\n  - signal: '_try_bm25_query中except Exception吞TypeError——bug隐蔽数周'\n    severity: high\n    implication: '单元测试全部通过但端到端搜索失败——异常被静默吞掉'\n  - signal: 'SearchIndex.__init__未做Path类型校验'\n    severity: medium\n    implication: '防御性修复已应用——调用方做Path强转，SearchIndex自身未修'\n",
        'related': "  - '[[dk-E010-duplicate-key-detection]]'\n  - '[[framework-kdo-self-attack]]'\n  - '[[dk-c8-format-complete-mind-empty]]'\n  - '[[dk-P42-agent-fact-check-gap]]'\n  - '[[dk-c5-todo-false-positive]]'\n  - '[[dk-modeling-essence-predictive]]'\n",
        'positioning': "> **定位**：属于 KDO 事故教训库的 dk 系列——记录了 #222/#223 事故后发现的搜索管道底层 bug。与 E010（重复键）不同：这个是静默失败（不报错但永远返回空），更难发现。\n",
        'extra_section': ('## 与其他知识的关联\n\n'
            '- dk-E010-duplicate-key-detection → 同为 #222/#223 事故后发现的基础设施缺陷\n'
            '- framework-kdo-self-attack → 端到端验证 > 单元测试——此bug靠欧阳锋小昭实测发现\n'
            '- dk-c5-todo-false-positive → 同模式：脚本输出数字不等于真实结果\n'
            '- dk-P42-agent-fact-check-gap → 同模式：需要独立验证\n\n'),
    },
    '30_wiki/workflows/workflow-cross-agent-fact-dispute.md': {
        'ds': "diagnostic_signals:\n  - signal: '跨Agent事实争议靠谁说的有道理裁决——无git字节验证'\n    severity: high\n    implication: '#224王语嫣vs欧阳锋争论30分钟→git show 1秒终结'\n  - signal: 'Agent凭记忆/错误核查挑战审查结论——无标准流程'\n    severity: high\n    implication: '王语嫣初判错误→差点误导处置方向→欧阳锋git验证才纠正'\n  - signal: '争议本身有价值——暴露了核查方法论的缺口'\n    severity: low\n    implication: '不是因为有人错了才需要协议——是因为正确的人也会错'\n",
        'related': "  - '[[dk-P42-agent-fact-check-gap]]'\n  - '[[framework-kdo-self-attack]]'\n  - '[[dk-E010-duplicate-key-detection]]'\n  - '[[dk-P15-false-completion-report]]'\n  - '[[framework-kdo-modeling-methodology]]'\n  - '[[dk-c5-todo-false-positive]]'\n",
        'positioning': "> **定位**：属于 KDO 工厂流程——跨 Agent 协作的质量保障协议。当两个 Agent 对同一事实产生分歧时，以 git 字节验证为最终裁决。已写入 operating-principles.md。\n",
    },
    '30_wiki/tools/tool-mcp-reachability-check.md': {
        'ds': "diagnostic_signals:\n  - signal: '老顽童提交新卡前不自检搜索可达性——外部Agent搜不到但pre-submit不报错'\n    severity: high\n    implication: '创新者的窘境案例：卡已入库但小昭搜不到——空title+缺aliases'\n  - signal: 'pre-submit只查结构不查搜索——#219补了title/aliases但未验证搜索生效'\n    severity: medium\n    implication: '门禁和实际搜索之间有gap——此工具补上'\n  - signal: 'import被site-packages MCP SDK劫持——脚本无法运行'\n    severity: medium\n    implication: '已用importlib.util绝对路径加载修复'\n",
        'related': "  - '[[tool-kdo-help]]'\n  - '[[dk-delivery-path-type-bug]]'\n  - '[[dk-E010-duplicate-key-detection]]'\n  - '[[framework-kdo-self-attack]]'\n  - '[[dk-P42-agent-fact-check-gap]]'\n  - '[[dk-c8-format-complete-mind-empty]]'\n",
        'positioning': "> **定位**：属于 KDO 生产工具——老顽童提卡前自检。pre-submit 查结构（YAML/字段/段名），此工具查搜索可达性（外部 Agent 能否搜到）。两者互补。\n",
        'extra_section': '## 失败模式\n\n| 失败模式 | 症状 | 修复 |\n|:--|:--|:--|\n| import 劫持 | `from mcp.tools import search` 被 site-packages MCP SDK 拦截 | 脚本已用 importlib.util 绝对路径加载 |\n| 关键字选择不当 | 自查全绿但用户实际搜索词不同 | 加用户反馈的搜索词——不只测自己能想到的词 |\n| 只测 BM25 不测 Graph | BM25 命中但语义搜索失败 | 脚本内 search() 走完整 RRF 融合——已覆盖双路径 |\n',
    },
    '30_wiki/tools/tool-kdo-help.md': {
        'ds': "diagnostic_signals:\n  - signal: '外部Agent首次接入KDO不知如何检索——工具描述是技术参数非操作手册'\n    severity: high\n    implication: '小昭接到任务后反复尝试才找到正确检索路径——kdo_help一次调用即可消除摸索成本'\n  - signal: 'MCP tool description无路由信息——Agent不知道搜不到时换什么工具'\n    severity: medium\n    implication: 'kdo_help补上了搜索模式+评分指引+工具路由网'\n  - signal: '新Agent接入无标准化onboarding——每次都是重新摸索'\n    severity: medium\n    implication: 'kdo_help=可复用的新人引导——一次调用理解KDO完整检索模型'\n",
        'related': "  - '[[tool-mcp-reachability-check]]'\n  - '[[framework-kdo-self-attack]]'\n  - '[[dk-delivery-path-type-bug]]'\n  - '[[dk-E010-duplicate-key-detection]]'\n  - '[[dk-P42-agent-fact-check-gap]]'\n  - '[[dk-c8-format-complete-mind-empty]]'\n",
        'positioning': "> **定位**：属于 KDO MCP 工具集——外部 Agent 的首次接入引导。与 tool-mcp-reachability-check 互补：一个是新人引导（怎么用），一个是提交前自检（能否被搜到）。\n",
        'extra_section': '## 失败模式\n\n| 失败模式 | 症状 | 修复 |\n|:--|:--|:--|\n| 引导内容过时 | 新增工具/搜索模式未更新到 kdo_help | 每次 MCP 工具变更时同步更新 help_guide() |\n| Agent 不调用 | 外部 Agent 不知道 kdo_help 存在 | tool description 中增加"首次接入请先调 kdo_help" |\n| 引导太啰嗦 | Agent 上下文被长引导占满 | help_guide 返回值已做结构化分层——Agent 可按需跳读 |\n',
    },
}

for path, meta in fixes.items():
    fp = root / path
    t = fp.read_text(encoding='utf-8', errors='replace')
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', t, re.DOTALL)
    fm, body = m.group(1), t[m.end():]

    # 1. Add diagnostic_signals before related:
    fm = fm.replace('\nrelated:', '\n' + meta['ds'] + 'related:')

    # 2. Replace related list
    fm = re.sub(r"^related:\n((?:  - .+\n)+)", 'related:\n' + meta['related'], fm, flags=re.MULTILINE)
    fm = re.sub(r"^related:\n((?:  - '\[\[.+\]\]'\n)+)", 'related:\n' + meta['related'], fm, flags=re.MULTILINE)

    # 3. Add positioning after h1
    body = re.sub(r'(^# .+\n)', r'\1\n' + meta['positioning'] + '\n', body, count=1, flags=re.MULTILINE)

    # 4. Add extra section before Critique (for dk) or at end (for tool)
    if 'extra_section' in meta:
        es = meta['extra_section']
        if '## Critique' in body:
            body = body.replace('## Critique', es + '## Critique')
        elif '## 失败模式' not in body:
            body += '\n' + es + '\n'

    new_text = '---\n' + fm + '\n---\n' + body
    m2 = re.match(r'^---\s*\n(.*?)\n---\s*\n', new_text, re.DOTALL)
    try:
        yaml.safe_load(m2.group(1))
        fp.write_text(new_text, encoding='utf-8')
        print(f'OK: {fp.name}')
    except Exception as e:
        print(f'YAML FAIL: {fp.name} — {e}')

print('\nDone')
