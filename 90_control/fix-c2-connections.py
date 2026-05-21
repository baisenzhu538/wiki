import os

BASE = r'E:\wiki\30_wiki\concepts'

APPENDS = {
    'yt-decision-consensus-iceberg.md': {
        'marker': '| 冲突概念 | [[yt-decision-height-toolkit]] | 高度工具中的"共识曲线"与本卡有重叠，但本卡聚焦"如何操作"而非"什么是对齐内容" |',
        'additions': [
            '| 跨域连接 | [[psychological-safety-edmondson]] | L4信息层对齐的前提是团队心理安全——Edmondson研究证明心理安全是团队学习的先决条件 |',
            '| 跨域连接 | [[nonviolent-communication-rosenberg]] | 教练式提问中的"观察→感受→需要→请求"与NVC四要素在沟通结构上同源 |',
            '| 跨域连接 | [[facilitation-technology]] | 共识冰山的"教练式提问"与引导技术的"中立主持人"角色互补——前者由领导者执行，后者由第三方执行 |',
            '| 跨模块连接 | [[yt-management-meeting-design]] | 管理模块的会议设计为共识冰山提供结构化会议流程（如六顶思考帽、世界咖啡） |',
        ]
    },
    'yt-decision-full-process.md': {
        'marker': '| 关联框架 | [[yt-decision-abcd-model]] | 假设思维体系的四套操作系统之一，与Y模型同源 |',
        'additions': [
            '| 跨域连接 | [[pdca-deming]] | 五阶段流程与PDCA在"计划→执行→检查→改进"闭环逻辑上同源，但Y模型增加了"有意识"前置和"共识"中间层 |',
            '| 跨域连接 | [[ooda-loop-boyd]] | 危机决策场景下，五阶段流程可压缩为OODA的快速循环变体——观察→判断→决策→行动 |',
            '| 跨域连接 | [[design-thinking-ideo]] | 阶段一"有意识"与阶段五"复盘"与设计思维的"同理心→定义→构思→原型→测试"在迭代节奏上互补 |',
            '| 跨模块连接 | [[yt-lean-startup-mvp]] | 起盘模块的精益创业MVP与阶段三"细打磨"在假设验证上同源——先黑板推演，再小规模验证 |',
            '| 跨模块连接 | [[yt-growth-hacking-loop]] | 增长模块的增长黑客循环与阶段五"复盘"在数据驱动迭代上互补 |',
        ]
    },
    'yt-decision-canvas.md': {
        'marker': '| 关联工具 | [[yt-entrepreneur-key-hypotheses]] | 关键假设验证方法论，可与画布配合使用 |',
        'additions': [
            '| 跨域连接 | [[business-model-canvas-osterwalder]] | Y模型决策画布与商业模式画布在"结构化一页纸"设计上同源，但Y模型聚焦决策评估而非商业模式设计 |',
            '| 跨域连接 | [[lean-canvas-maurya]] | 精益画布的问题-解决方案匹配与Y模型宽度区的收益-成本识别在逻辑上互补 |',
            '| 跨域连接 | [[empathy-map-design-thinking]] | 画布宽度区的"列推查"与设计思维同理心地图在"穷尽用户视角"上同源 |',
            '| 跨模块连接 | [[yt-startup-business-plan]] | 起盘模块的商业计划书使用画布作为决策前的快速评估工具 |',
            '| 跨模块连接 | [[yt-growth-channel-canvas]] | 增长模块的渠道评估画布与Y模型画布在"收益-成本结构化"上同源 |',
        ]
    },
    'yt-decision-review.md': {
        'marker': '| 关联概念 | [[yt-management-scientific-decision]] | 复盘是科学管理的核心闭环，与一堂管理课的复盘模型互补 |',
        'additions': [
            '| 跨域连接 | [[after-action-review-aar]] | L1-L4四层复盘与美军AAR在"结构化事后分析"上同源，但Y模型增加了迁移层和能力层 |',
            '| 跨域连接 | [[double-loop-learning-argyris]] | L3迁移层=单环学习（改进策略），L4能力层=双环学习（改变假设）——Argyris学习理论是复盘的分层基础 |',
            '| 跨域连接 | [[seci-model-nonaka]] | 复盘产生的"迁移规则"与SECI模型在"隐性知识显性化"上同源——个人经验→团队知识→组织资产 |',
            '| 跨模块连接 | [[yt-growth-data-analysis]] | 增长模块的数据分析为复盘提供L2过程层的偏差量化（实际vs预判） |',
            '| 跨模块连接 | [[yt-management-performance-review]] | 管理模块的绩效复盘与决策复盘在"能力缺失识别"上互补 |',
        ]
    },
    'yt-decision-ai-partner.md': {
        'marker': '| 关联工具 | [[yt-entrepreneur-key-hypotheses]] | 关键假设验证，可与AI Partner结合使用 |',
        'additions': [
            '| 跨域连接 | [[human-in-the-loop-dss]] | AI Partner的"人主导AI辅助"与决策支持系统（DSS）的人在回路（HITL）设计原则同源 |',
            '| 跨域连接 | [[explainable-ai-xai]] | AI Partner的"六步对话流程"本质是XAI的"可解释交互"——让AI的推理过程对人透明 |',
            '| 跨域连接 | [[distributed-cognition-hutchins]] | 双三角模型（人+AI）与Hutchins分布式认知理论同源——认知过程分布在人与工具之间 |',
            '| 跨模块连接 | [[yt-growth-data-driven]] | 增长模块的数据驱动决策使用AI Partner进行L3/L4定量分析的快速原型 |',
            '| 跨模块连接 | [[yt-management-intelligent-ops]] | 管理模块的智能化运营与AI Partner在"人机协作工作流"上互补 |',
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
    
    first_addition = config['additions'][0]
    if first_addition in text:
        print(f'SKIP: {fname} - already patched')
        return
    
    additions_text = '\n'.join(config['additions'])
    text = text.replace(marker, marker + '\n' + additions_text)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'FIXED: {fname} - added {len(config["additions"])} connections')

def main():
    for fname, config in APPENDS.items():
        fix_file(fname, config)
    print('\nC2 Done.')

if __name__ == '__main__':
    main()
