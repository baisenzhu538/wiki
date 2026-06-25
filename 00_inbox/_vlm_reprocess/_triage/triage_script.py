import re
from pathlib import Path

def extract_title(text):
    m = re.search(r'"title"\s*:\s*"([^"]+)"', text)
    if m:
        t = m.group(1).strip()
        if t:
            return t
    return ''

skip_patterns = ['课程清单','进步大地图','创业地图','管理地图','个人地图','修炼地图','萃取总结','ocr_','screenshot','微信图片','清单体笔记','高阶体系探索营-三种咨询可能性','案例拆解-课程清单','创业必修','管理必修','AI学习-提问进化路线图','AI学习-truman自用的AI FeatureSet','人和AI协作','参考案例','全景图','MUSE模型','训练地图','系统故事线','十年修炼爬山地图','36计','多出牌多练习','AI助手对话','Kimi Code API']
case_patterns = ['案例','婚礼操盘','婚礼规划','ROI决策评估画布-案例']
dark_patterns = ['实操难点','小抄','武器库','段位','经验值','你的业务是一次抽样实验','解放思想','思考深度']
framework_patterns = ['模型','框架','画布','公式','方法论','分析法','决策三角形','项目方案评估三角形','关键假设','X型Y型','人机协作','稀缺机会窗口','稀缺资源清单','高水平共识曲线','TCPR','ABCD','双三角','MUSE','Y模型','五步法','产品内核','转化率','复盘','冰山图','十大单元模型','象限分析法','学练用','外部对抗地图','多模型情况','关键训练清单','发现决策','商业模式','宽度','深度','高度','动力三曲线','10大容易浪费的触点','因果模型','产品内核画布','五步法画布','十大典型指标','最佳转化率','复盘迭代','风险管理','里程碑拆解','逻辑MECE','业务建模','努力仿真','十倍速验证','攻坚会','灵感闪现','管理三段论','设计原则','酝酿式打磨','善用佳软','假设拆解','内核和边界','需求挖掘','用户分层','用户视角','行业分析画布','场景推演','多视角思考','峰终定律','惊喜公式','动力阻力','最佳实践','审美','需求工具箱','审美工具箱','落地工具箱','提问工程化','问题工程化','个人成长五步法','职业成长路线','AI FeatureSet','Truman','TCP-R皇冠模型','Y模型steps策略集','Y模型实操工作流','刻意练习','十指模型','表达力火箭','科学学习IPO','科学提问','提问刻意练习']

override = {
    '一堂-单元模型-单sku模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-单元模型-单商圈模型': ('new-tool', 'tool-单元模型-单商圈'),
    '一堂-单元模型-单城市模型': ('new-tool', 'tool-单元模型-单城市'),
    '一堂-单元模型-单客户模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-单元模型-单履约模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-单元模型-单柜子模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-单元模型-单用户模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-单元模型-单订单模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-单元模型-单销售模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-单元模型-单门店模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-单元模型-基准值': ('enrich', 'yt-tool-unit-model-benchmark'),
    '一堂-单元模型-壁垒预判': ('new-tool', 'tool-单元模型-壁垒预判'),
    '一堂-单元模型-外部对抗地图': ('new-framework', 'framework-单元模型-外部对抗地图'),
    '一堂-单元模型-多模型情况': ('enrich', 'yt-tool-unit-model-selection'),
    '一堂-单元模型-学练用': ('new-concept', 'concept-单元模型-学练用'),
    '一堂-单元模型-对抗小抄01': ('dk', 'dk-单元模型-对抗小抄'),
    '一堂-单元模型-对抗小抄02': ('dk', 'dk-单元模型-对抗小抄'),
    '一堂-单元模型-对抗小抄': ('dk', 'dk-单元模型-对抗小抄'),
    '一堂-单元模型-扭蛋机案例': ('enrich-case', 'case-unit-model-gashapon'),
    '一堂-单元模型-找全成本实操难点': ('dk', 'dk-单元模型-找全成本实操难点'),
    '一堂-单元模型-找单元模型实操难点': ('dk', 'dk-单元模型-找单元模型实操难点'),
    '一堂-单元模型-找基准值实操难点': ('dk', 'dk-单元模型-找基准值实操难点'),
    '一堂-单元模型-斧子、尺子、梯子': ('enrich', 'yt-unit-model-three-tools'),
    '一堂-单元模型-斧子尺子梯子详解': ('enrich', 'yt-unit-model-three-tools'),
    '一堂-单元模型-最简单元模型': ('new-concept', 'concept-最简单元模型'),
    '一堂-单元模型-段位专家': ('enrich', 'yt-unit-model-ladder'),
    '一堂-单元模型-示例01': ('case', 'case-单元模型-示例01'),
    '一堂-单元模型-示例': ('case', 'case-单元模型-示例'),
    '一堂-单元模型-规模对抗实操难点': ('dk', 'dk-单元模型-规模对抗实操难点'),
    '一堂-单元模型-规模经济对抗武器库': ('enrich', 'yt-scale-economy-weapon-library'),
    '一堂-单元模型-象限分析法': ('new-tool', 'tool-单元模型-象限分析法'),
    '一堂-单元模型-动态预测': ('enrich', 'yt-tool-unit-model-dynamic'),
    '一堂-单元模型-TCPR底层网络协议': ('new-framework', 'framework-TCPR底层网络协议'),
    '一堂-单元模型-ABCD策略模型': ('enrich', 'yt-assumption-abcd-model（如存在）'),
    '一堂-单元模型-修炼地图': ('skip', '目录/索引型'),
    '一堂DOC-单元模型-十大单元模型': ('enrich', 'yt-unit-model-overview'),
    '一堂-科学决策-ROI决策评估画布': ('new-tool', 'tool-ROI决策评估画布'),
    '一堂-科学决策-ROI高阶训练全景图': ('skip', '全景地图/目录'),
    '一堂-科学决策-X型Y型决策习惯对比': ('new-concept', 'concept-X型Y型决策习惯'),
    '一堂-科学决策-一堂双三角磨合追求-从入门到无限进步': ('skip', '全景地图/目录'),
    '一堂-科学决策-人机协作决策': ('new-concept', 'concept-AI时代双三角竞争力'),
    '一堂-科学决策-关键假设ABCD模型': ('enrich', 'yt-assumption-abcd-model'),
    '一堂-科学决策-关键训练清单（重要））': ('new-tool', 'tool-科学决策关键训练清单'),
    '一堂-科学决策-决策三角形': ('new-framework', 'framework-科学决策三角形'),
    '一堂-科学决策-发现决策': ('new-concept', 'concept-发现决策'),
    '一堂-科学决策-商业模式-完整财务公式决策': ('new-tool', 'tool-完整财务公式决策'),
    '一堂-科学决策-宽度-个人': ('new-concept', 'concept-科学决策宽度-个人'),
    '一堂-科学决策-宽度-企业': ('new-concept', 'concept-科学决策宽度-企业'),
    '一堂-科学决策-宽度-团队': ('new-concept', 'concept-科学决策宽度-团队'),
    '一堂-科学决策-深度-L1优先级定性': ('new-tool', 'tool-决策深度-L1优先级定性'),
    '一堂-科学决策-深度-L2部分定量': ('new-tool', 'tool-决策深度-L2部分定量'),
    '一堂-科学决策-深度-L3定量公式': ('new-tool', 'tool-决策深度-L3定量公式'),
    '一堂-科学决策-深度-L4-案例01': ('case', 'case-决策深度-L4-案例01'),
    '一堂-科学决策-深度-L4严格财务公式': ('new-tool', 'tool-决策深度-L4严格财务公式'),
    '一堂-科学决策-深度-你的业务是一次抽样实验': ('dk', 'dk-你的业务是一次抽样实验'),
    '一堂-科学决策-深度-决策经验值': ('dk', 'dk-决策经验值'),
    '一堂-科学决策-深度-案例01': ('case', 'case-科学决策-全员涨薪20%'),
    '一堂-科学决策-深度-案例02': ('case', 'case-科学决策-上班开车还是打车'),
    '一堂-科学决策-深度-案例03': ('case', 'case-科学决策-自研IM_CRM'),
    '一堂-科学决策-深度-案例04': ('case', 'case-科学决策-管员工中午饭'),
    '一堂-科学决策-深度-案例05': ('case', 'case-科学决策-租办公室ROI'),
    '一堂-科学决策-深度-案例06': ('case', 'case-科学决策-电话外呼ROI'),
    '一堂-科学决策-稀缺机会窗口': ('new-concept', 'concept-稀缺机会窗口'),
    '一堂-科学决策-稀缺资源清单': ('new-tool', 'tool-稀缺资源清单'),
    '一堂-科学决策-项目方案评估三角形': ('new-tool', 'tool-项目方案评估三角形'),
    '一堂-科学决策-高度-两种典型的思考习惯': ('new-concept', 'concept-两种典型思考习惯'),
    '一堂-科学决策-高水平共识曲线（重要）': ('new-framework', 'framework-高水平共识曲线'),
    '泛产品设计-审美卡片-最佳实践建模': ('new-tool', 'tool-审美-最佳实践建模'),
    '泛产品设计-审美卡片-最佳实践收集': ('new-tool', 'tool-审美-最佳实践收集'),
    '泛产品设计-审美卡片-最佳实践池子': ('new-tool', 'tool-审美-最佳实践池子'),
    '泛产品设计-审美卡片-美好作品想象': ('new-concept', 'concept-美好作品想象'),
    '泛产品设计-审美工具箱指南': ('new-tool', 'tool-审美工具箱指南'),
    '泛产品设计-用户卡片-一堂五步法': ('enrich', 'yt-five-step-method'),
    '泛产品设计-用户卡片-动力阻力': ('new-concept', 'concept-动力阻力'),
    '泛产品设计-用户卡片-场景推演': ('new-tool', 'tool-场景推演'),
    '泛产品设计-用户卡片-多视角思考': ('new-tool', 'tool-多视角思考'),
    '泛产品设计-用户卡片-峰终定律': ('new-concept', 'concept-峰终定律'),
    '泛产品设计-用户卡片-惊喜公式': ('new-concept', 'concept-惊喜公式'),
    '泛产品设计-用户卡片-用户分层': ('new-tool', 'tool-用户分层'),
    '泛产品设计-用户卡片-用户视角': ('new-concept', 'concept-用户视角'),
    '泛产品设计-用户卡片-行业分析画布': ('new-tool', 'tool-行业分析画布'),
    '泛产品设计-用户卡片-需求挖掘': ('new-tool', 'tool-需求挖掘'),
    '泛产品设计-用户卡片-项目背景分析': ('new-tool', 'tool-项目背景分析'),
    '泛产品设计-落地卡片-ROI分析': ('new-tool', 'tool-泛产品-ROI分析'),
    '泛产品设计-落地卡片-业务建模': ('new-tool', 'tool-泛产品-业务建模'),
    '泛产品设计-落地卡片-低成本测试MVP': ('enrich', 'yt-panproduct-execution-low-cost-mvp'),
    '泛产品设计-落地卡片-假设拆解': ('new-tool', 'tool-假设拆解'),
    '泛产品设计-落地卡片-内核和边界': ('new-concept', 'concept-内核和边界'),
    '泛产品设计-落地卡片-努力仿真': ('new-tool', 'tool-努力仿真'),
    '泛产品设计-落地卡片-十倍速验证': ('new-tool', 'tool-十倍速验证'),
    '泛产品设计-落地卡片-善用佳软': ('new-tool', 'tool-善用佳软'),
    '泛产品设计-落地卡片-复盘迭代': ('new-tool', 'tool-复盘迭代'),
    '泛产品设计-落地卡片-攻坚会': ('new-tool', 'tool-攻坚会'),
    '泛产品设计-落地卡片-灵感闪现': ('dk', 'dk-灵感闪现'),
    '泛产品设计-落地卡片-管理三段论': ('new-framework', 'framework-管理三段论'),
    '泛产品设计-落地卡片-解放思想': ('enrich', 'yt-liberate-thinking（如存在）'),
    '泛产品设计-落地卡片-设计原则': ('new-concept', 'concept-设计原则'),
    '泛产品设计-落地卡片-逻辑MECE': ('new-tool', 'tool-逻辑MECE'),
    '泛产品设计-落地卡片-酝酿式打磨': ('new-tool', 'tool-酝酿式打磨'),
    '泛产品设计-落地卡片-里程碑拆解': ('new-tool', 'tool-里程碑拆解'),
    '泛产品设计-落地卡片-风险管理': ('new-tool', 'tool-风险管理'),
    '泛产品设计-需求工具箱指南': ('new-tool', 'tool-需求工具箱指南'),
    '一堂-个人修炼-Y模型': ('enrich', 'yt-decision-y-model'),
    '一堂-个人修炼-全景图MUSE模型': ('skip', '全景地图/目录'),
    '一堂-个人修炼-双三角模型': ('new-concept', 'concept-AI时代双三角竞争力'),
    '一堂-个人修炼-提问刻意练习画布': ('new-tool', 'tool-提问刻意练习画布'),
    '一堂-个人修炼-科学学习IPO-全景策略': ('enrich', 'yt-scientific-learning-ipo（如存在）'),
    '一堂-个人修炼-科学学习IPO完整清单': ('new-tool', 'tool-科学学习IPO完整清单'),
    '一堂-个人修炼-科学学习IPO模型': ('enrich', 'yt-scientific-learning-ipo（如存在）'),
    '一堂-个人修炼-科学提问刻意练习': ('new-tool', 'tool-科学提问刻意练习'),
    '一堂-个人修炼-表达力火箭模型-执行武器库': ('enrich', 'yt-expressive-rocket-model（如存在）'),
    '一堂-个人修炼-表达力火箭模型': ('enrich', 'yt-expressive-rocket-model（如存在）'),
    '一堂-个人修炼-解放思想': ('new-concept', 'concept-思考深度分级'),
    '一堂-个人修炼-讲香十指模型-超级武器库': ('new-tool', 'tool-讲香十指模型-超级武器库'),
    '一堂-个人修炼-讲香基本功-十指模型修炼地图': ('skip', '地图/目录'),
    '一堂-个人修炼-讲香基本功': ('new-tool', 'tool-讲香基本功-十指模型'),
    '一堂-个人修炼-课程清单': ('skip', '课程清单'),
    'AI俱乐部-人和AI协作-纪浩-五层结构-图片01': ('new-framework', 'framework-问题边界与Problem澄清五层结构'),
    'AI俱乐部-人和AI协作-纪浩-参考案例-图片02': ('skip', '参考案例/未明'),
    'ocr_screenshot2': ('skip', '截图/无独立价值'),
    'ocr_Snipaste_2026-05-15_21-39-40': ('skip', '截图/无独立价值'),
    'screenshot1': ('skip', '截图/无独立价值'),
    'screenshot2': ('skip', '截图/无独立价值'),
    'Truman的个人成长五步法': ('new-framework', 'framework-个人成长五步法'),
    'truman的选择：两条职业成长路线': ('new-concept', 'concept-两条职业成长路线'),
    '一堂-AI学习-truman自用的AI FeatureSet': ('new-tool', 'tool-Truman自用AI FeatureSet'),
    '一堂-AI学习-提问工程化': ('new-tool', 'tool-提问工程化'),
    '一堂-AI学习-提问进化路线图': ('skip', '路线图/目录'),
    '一堂-AI清单体笔记（系统故事线）-truman-图片01': ('skip', '笔记方法/目录'),
    '一堂-AI清单体笔记（训练段位图）-truman-图片02': ('skip', '笔记方法/目录'),
    '一堂-TCPR模型-皇冠模型': ('new-framework', 'framework-TCPR皇冠模型'),
    '一堂-人机协作-双三角模型': ('new-concept', 'concept-AI时代双三角竞争力'),
    '一堂-创业必修-课程清单': ('skip', '课程清单'),
    '一堂-地图-个人地图': ('skip', '地图/目录'),
    '一堂-地图-创业地图_conv': ('skip', '地图/目录'),
    '一堂-地图-创业地图': ('skip', '地图/目录'),
    '一堂-地图-管理地图_conv': ('skip', '地图/目录'),
    '一堂-地图-管理地图': ('skip', '地图/目录'),
    '一堂-案例拆解-课程清单': ('skip', '课程清单'),
    '一堂-管理必修-课程清单': ('skip', '课程清单'),
    '一堂-高阶体系探索营-三种咨询可能性': ('skip', '单页/未明'),
    '一堂DOC-单元模型-十大单元模型': ('enrich', 'yt-unit-model-overview'),
    '一堂Y模型-科学成事道理': ('enrich', 'yt-decision-y-model'),
    '一堂Y模型steps策略集': ('new-tool', 'tool-Y模型STEPS策略集'),
    '一堂Y模型实操工作流': ('new-tool', 'tool-Y模型实操工作流'),
    '一堂个人地图：高潜力成长者修炼全景图': ('skip', '地图/目录'),
    '一堂五步法-产品内核画布': ('enrich', 'yt-product-kernel-canvas'),
    '一堂五步法画布': ('enrich', 'yt-five-step-method'),
    '一堂产品内核-十大典型指标': ('enrich', 'yt-product-ten-metrics'),
    '一堂刻意练习十年成长指数': ('new-tool', 'tool-刻意练习十年成长指数'),
    '一堂提炼过的因果模型': ('new-framework', 'framework-一堂因果模型'),
    '一堂最佳转化率动力曲线图': ('new-framework', 'framework-最佳转化率动力三曲线'),
    '一堂泛产品设计-十年修炼爬山地图': ('skip', '地图/目录'),
    '一堂泛产品设计-多出牌多练习': ('dk', 'dk-多出牌多练习'),
    '一堂泛产品设计36计-全套地图': ('skip', '地图/目录'),
    '一堂深度复盘冰山图': ('new-tool', 'tool-深度复盘冰山图'),
    '一堂转化率-10大容易浪费的触点': ('new-tool', 'tool-转化率10大浪费触点'),
    '一堂进步大地图_compressed': ('skip', '地图/目录'),
    '一堂进步大地图': ('skip', '地图/目录'),
    '优秀泛产品设计者的自我修养': ('new-concept', 'concept-优秀泛产品设计者的自我修养'),
    '婚礼操盘-用户和场景': ('case', 'case-婚礼操盘-用户和场景'),
    '婚礼规划': ('case', 'case-婚礼规划'),
    '审美提升的层级': ('new-concept', 'concept-审美提升的层级'),
}

def classify(stem):
    if stem in override:
        return override[stem]
    s = stem.lower()
    if any(p in s for p in skip_patterns):
        return ('skip', '目录/清单/地图/截图/缺失原图')
    if any(p in s for p in case_patterns):
        return ('case', '待命名')
    if any(p in s for p in dark_patterns):
        return ('dk', '待命名')
    if any(p in s for p in framework_patterns):
        return ('new_or_enrich', '需二轮提取后判断')
    return ('review', '需人工判断')

lines = []
lines.append('# VLM 描述独立框架价值标注（王语嫣）\n')
lines.append('> 基于 `00_inbox/_vlm_reprocess/` 172 份 VLM 描述文件，按文件名 + VLM 标题做价值标注。\n')
lines.append('> 动作说明：\n> - `new-*`：建议新建成品卡\n> - `enrich`：建议 enrich 已有 wiki 卡片\n> - `case`：建议新建案例卡\n> - `dk`：建议新建暗知识卡\n> - `skip`：暂不建议入库（课程清单/大地图/截图/原图缺失）\n> - `new_or_enrich`：需二轮 case-mining 后再判断是新建还是 enrich\n> - `review`：需人工判断\n')
for domain in ['单元模型','科学决策','泛产品设计','个人修炼','其他']:
    files = sorted(Path(domain).glob('*_vlm_desc.md'))
    lines.append(f'\n## {domain}（{len(files)} 张）\n')
    lines.append('| 文件名 | VLM 标题 | 建议动作 | 目标卡片 / 备注 |')
    lines.append('|:---|:---|:---:|:---|')
    for f in files:
        text = f.read_text(encoding='utf-8')
        title = extract_title(text) or ''
        stem = f.stem.replace('_vlm_desc','')
        action, note = classify(stem)
        lines.append(f'| {stem} | {title} | {action} | {note} |')

out = Path('_triage/vlm_framework_value_triage.md')
out.write_text('\n'.join(lines), encoding='utf-8')
print('wrote', out)
