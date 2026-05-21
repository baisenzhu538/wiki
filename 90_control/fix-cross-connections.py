#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C阶段修复脚本：批量追加跨域/跨模块连接到关联表
"""

import os

BASE = r'E:\wiki\30_wiki\concepts'

# 定义每张卡片需要追加的连接（在关联表最后一条后追加）
APPENDS = {
    'yt-decision-depth-ladder.md': {
        'marker': '| [[yt-decision-ai-partner]] | 加速辅助 | 用AI辅助拆公式漏斗、生成benchmark范围、做敏感性分析，但经验值必须人工校准 |',
        'additions': [
            '| [[pirate-metrics-aarrr]] | 跨域连接 | L3转化率漏斗与AARRR海盗指标在获客分析上同源——获取→激活→留存→收入→推荐 |',
            '| [[npv-irr-finance]] | 跨域连接 | L4严格财务ROI与NPV/IRR在资本预算决策中互补，尤其融资/并购场景 |',
            '| [[confidence-interval-statistics]] | 跨域连接 | 三点预测法的乐观/合理/悲观版与统计学置信区间在"不确定性量化"上同源 |',
            '| [[yt-growth-unit-economics]] | 跨模块连接 | 增长模块的单元模型计算直接调用深度工具的L4完整财务ROI方法 |',
            '| [[yt-forecast-market-size]] | 跨模块连接 | 预判模块的市场规模估算使用L3交叉类比法进行多参照物调整 |',
        ]
    },
    'yt-decision-height-toolkit.md': {
        'marker': '| [[yt-decision-ai-partner]] | 加速辅助 | 用AI模拟"老板视角""长期推演""窗口期预测"，但需人工校校假设合理性 |',
        'additions': [
            '| [[second-curve-handy]] | 跨域连接 | 长期视角与Handy第二曲线在"何时启动新业务"决策上互补——当前业务成熟期即新曲线起点 |',
            '| [[blue-ocean-strategy]] | 跨域连接 | 机会成本分析中的"价值创新"与蓝海战略的重构市场边界同源——不做选择而创造新选项 |',
            '| [[porter-five-forces]] | 跨域连接 | 公司视角的"加一思考"与波特五力在竞争格局分析上互补——从内部视角扩展到行业结构 |',
            '| [[yt-forecast-timing-window]] | 跨模块连接 | 预判模块的时机窗口分析为高度工具的时间窗口维度提供前置信号 |',
            '| [[yt-startup-strategic-choice]] | 跨模块连接 | 起盘模块的战略选择使用高度工具的长期视角评估不同路径的3年/10年ROI |',
        ]
    },
    'yt-decision-habit-shift.md': {
        'marker': '| [[yt-decision-ai-partner]] | 关联工具 | AI辅助诊断自己是X型还是Y型的对话流程 |',
        'additions': [
            '| [[thinking-fast-slow-kahneman]] | 理论同源 | X型=System 1（快思考/直觉），Y型=System 2（慢思考/分析）——Kahneman双系统理论是习惯转换的认知科学基础 |',
            '| [[immunity-to-change-kegan]] | 跨域连接 | 从X型到Y型的转换阻力与Kegan"变革免疫"同源——既有承诺阻碍新行为adoption |',
            '| [[status-quo-bias-samuelson]] | 跨域连接 | X型拍脑袋的惯性部分源于行为经济学的"现状偏见"——默认维持当前行为模式 |',
            '| [[yt-management-team-building]] | 跨模块连接 | 管理模块的团队建设需要Y型决策习惯作为协作基础——共识建立在结构化分析之上 |',
        ]
    },
}

def fix_file(fname, config):
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    marker = config['marker']
    if marker not in text:
        print(f'SKIP: {fname} - marker not found')
        return
    
    # 检查是否已修复
    first_addition = config['additions'][0]
    if first_addition in text:
        print(f'SKIP: {fname} - already patched')
        return
    
    # 在 marker 行后追加
    additions_text = '\n'.join(config['additions'])
    text = text.replace(marker, marker + '\n' + additions_text)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'FIXED: {fname} - added {len(config["additions"])} connections')

def main():
    for fname, config in APPENDS.items():
        fix_file(fname, config)
    print('\nDone.')

if __name__ == '__main__':
    main()
