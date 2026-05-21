import os

fpath = r'E:\wiki\30_wiki\concepts\yt-decision-habit-shift.md'
with open(fpath, 'r', encoding='utf-8') as f:
    text = f.read()

marker = '| 关联工具 | [[yt-decision-ai-partner]] | AI辅助诊断自己是X型还是Y型的对话流程 |'
additions = [
    '| 理论同源 | [[thinking-fast-slow-kahneman]] | X型=System 1（快思考/直觉），Y型=System 2（慢思考/分析）——Kahneman双系统理论是习惯转换的认知科学基础 |',
    '| 跨域连接 | [[immunity-to-change-kegan]] | 从X型到Y型的转换阻力与Kegan"变革免疫"同源——既有承诺阻碍新行为adoption |',
    '| 跨域连接 | [[status-quo-bias-samuelson]] | X型拍脑袋的惯性部分源于行为经济学的"现状偏见"——默认维持当前行为模式 |',
    '| 跨模块连接 | [[yt-management-team-building]] | 管理模块的团队建设需要Y型决策习惯作为协作基础——共识建立在结构化分析之上 |',
]

if marker in text and additions[0] not in text:
    text = text.replace(marker, marker + '\n' + '\n'.join(additions))
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)
    print('FIXED: habit-shift')
else:
    print('SKIP: habit-shift (already patched or marker not found)')
