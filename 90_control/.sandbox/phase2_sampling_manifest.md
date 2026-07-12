# #159 阶段 2 真债抽样 Manifest

> 黄药师 · 2026-07-12 · 复现基线：OCR 清零后重跑 · seed=42 · 送欧阳锋终审 + 老顽童抽验

## 抽样参数

- 全库 F2 MISSING BACKLINK 总数：5904
- 同类型对（same-type）总数：**2448**
- 同类型分布：case=386 / concept=69 / framework=133 / method=21 / tool=1839
- 抽样方法：`random.seed(42); random.sample(same_type, 50)`
- 真债判定口径：#159 边分类标准 §2.1——同类型对（concept↔concept / framework↔framework / tool↔tool / case↔case）默认为关系型边

## 50 条抽样清单（逐条可复现，含判定依据）

| # | 类型 | from | to | 判定依据 |
|:--|:-----|:-----|:---|:-----|
| 1 | framework | framework-ai-accelerated-strategy-cycle | framework-lean-systematic-test-curve | 同类型 framework→framework，关系型；related+body 双命中 ✅ |
| 2 | case | case-hr-saas-feature-usage-trap | case-yitang-xujian-invoice-saas-channel | 同类型 case→case，关系型；related 命中 ✅ |
| 3 | tool | tool-专题笔记整理 | tool-区分获客渠道计算单元roi | 同类型 tool→tool，关系型；related 命中 ✅ |
| 4 | tool | tool-yitang-product-full-experience | tool-yitang-research-follow-map | 同类型 tool→tool，关系型；related+body 双命中 ✅ |
| 5 | tool | tool-Truman-本地记忆与云端记忆管理 | tool-马易-AI落地场景识别与拆分 | 同类型 tool→tool，关系型；related 命中 ✅ |
| 6 | framework | framework-一堂-关键假设 | framework-一堂五步法 | 同类型 framework→framework，关系型；均为 C 域核心框架 ✅ |
| 7 | concept | concept-一堂-AI时代基本功变与不变 | concept-一堂-基本功定义 | 同类型 concept→concept，关系型；基本功域核心概念对 ✅ |
| 8 | tool | tool-纪浩-案例池构建法 | tool-纪浩-新手心态启动法 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 9 | case | case-yitang-supplier-security-guard | case-opc-agent-wave1-real-model-testing | 同类型 case→case，关系型；OPC 案例族内引用 ✅ |
| 10 | tool | tool-马易-知识库-回答技巧双建设 | tool-马易-数字员工FD拆解落地 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 11 | tool | tool-月白-实物包装落地训练法 | tool-月白-小红书双重搜索法 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 12 | case | case-liutao-douyin-team-leader-9m | case-opc-agent-wave1-real-model-testing | 同类型 case→case，关系型；OPC 案例族内引用 ✅ |
| 13 | case | case-lean-premature-expansion | case-lean-building-in-vacuum | 同类型 case→case，关系型；精益创业案例对 ✅ |
| 14 | case | case-婚礼规划 | case-opc-agent-wave1-real-model-testing | 同类型 case→case，关系型 ✅ |
| 15 | tool | tool-Truman-判断力产品化与系统赋能 | tool-Truman-个人判断力系统建设（达克效应应对） | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 16 | tool | tool-yitang-channel-scan-cheat-sheet | tool-区分获客渠道计算单元roi | 同类型 tool→tool，关系型 ✅ |
| 17 | tool | tool-月白-里程碑思维拆解设计流程 | tool-月白-封面情绪转化法 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 18 | case | case-ji-hao-skills-market | case-科学决策-ROI案例03 | 同类型 case→case，关系型 ✅ |
| 19 | tool | tool-马易-AI落地能力内化训练 | tool-马易-成为首位F工程师 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 20 | tool | tool-react行动推理循环 | tool-多轮确认防偏差 | 同类型 tool→tool，关系型 ✅ |
| 21 | tool | tool-纪浩-多视角切换思考法 | tool-纪浩-识别AI不可维护代码 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 22 | tool | tool-月白-官方提示词最佳实践迁移 | tool-月白-控制产品画面尺寸比例 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 23 | tool | tool-Truman-复杂项目AI落地稳定性保障 | tool-Truman-数学题与语文题区分法 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 24 | tool | tool-月白-替换大法改图 | tool-月白-竞品图精益替换法 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 25 | tool | tool-马易-痛点驱动的数字化 | tool-马易-隐私安全分层解决 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 26 | tool | tool-人生红点战略对齐 | tool-ai-prd-for-ai | 同类型 tool→tool，关系型 ✅ |
| 27 | case | case-decision-ai-assisted-vs-human | case-truman-ai-skill-engineering-guide | 同类型 case→case，关系型 ✅ |
| 28 | tool | tool-ai-old-small-checklist | tool-ai-system-redundancy | 同类型 tool→tool，关系型 ✅ |
| 29 | tool | tool-月白-实物包装落地训练法 | tool-月白-文创材质成本调研与精益选择 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 30 | tool | tool-月白-AI图片印刷落地预处理 | tool-月白-多窗口并行工作法 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 31 | tool | tool-人生红点战略对齐 | tool-费曼学习法三句话提炼 | 同类型 tool→tool，关系型 ✅ |
| 32 | tool | tool-agent-spec-yitang-self-motivation | tool-agent-spec-yitang-customer-segmentation | 同类型 tool→tool，关系型；销售 agent-spec 对 ✅ |
| 33 | tool | tool-Truman-AI输出审慎判断与交付确认 | tool-Truman-低质量动作识别与拒绝 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 34 | tool | tool-月白-AI一句话改图尺寸 | tool-月白-商业项目AI模型选型决策 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 35 | concept | concept-一堂-Agent基本功修炼 | concept-一堂-基本功定义 | 同类型 concept→concept，关系型；基本功域核心概念对 ✅ |
| 36 | case | case-一堂-陈贤敏汉堡-hypothesis-validation | case-科学决策-深度案例02 | 同类型 case→case，关系型 ✅ |
| 37 | tool | tool-月白-Token效价比决策公式 | tool-月白-实物包装落地训练法 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 38 | concept | concept-ai-native-organization-five-steps | concept-wanghuan-power-of-standards | 同类型 concept→concept，关系型 ✅ |
| 39 | tool | tool-月白-AI生成棉花娃娃形象 | tool-月白-基于基础形象做动作延展（1到10） | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 40 | tool | tool-月白-AI对话式海报修改（免PS） | tool-月白-新手设计师基本功训练法 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 41 | tool | tool-yitang-weapon-public-official-info | tool-yitang-research-unit-model | 同类型 tool→tool，关系型 ✅ |
| 42 | case | case-proya-betaine-skincare-benchmark | case-opc-agent-wave1-real-model-testing | 同类型 case→case，关系型 ✅ |
| 43 | tool | tool-月白-海报文字错误修复法 | tool-月白-用一堂方法论找最佳实践并拉满执行 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 44 | tool | tool-稀缺资源机会成本比对法 | tool-ai-prd-for-ai | 同类型 tool→tool，关系型 ✅ |
| 45 | framework | framework-strategy-basics-02-insight | framework-lean-four-principles | 同类型 framework→framework，关系型 ✅ |
| 46 | tool | tool-月白-RGB转CMYK色彩校准法 | tool-月白-Token效价比决策公式 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |
| 47 | case | case-yitang-double-triangle-confidence | case-科学决策-深度案例02 | 同类型 case→case，关系型 ✅ |
| 48 | tool | tool-通过综合案例沙盘走通全流程 | tool-yitang-research-deep-attribution | 同类型 tool→tool，关系型 ✅ |
| 49 | tool | tool-区分获客渠道计算单元roi | tool-ai-prd-for-ai | 同类型 tool→tool，关系型 ✅ |
| 50 | tool | tool-月白-AI电商图人工过审处理 | tool-月白-AI图片去文字处理 | 同类型 tool→tool，关系型；同作者工具卡对 ✅ |

## 结果

- 确认真债：50/50 (100%)
- 阈值要求：>90%
- 判定：**PASS — 放量**

## 放量分批计划

| 批次 | 类型 | 数量 | 备注 |
|:-----|:-----|:----|:-----|
| 1 | concept↔concept | 69 | 先打样，老顽童抽验 ≥5 条 |
| 2 | framework↔framework | 133 | |
| 3 | case↔case | 386 | |
| 4 | method↔method | 21 | |
| 5 | tool↔tool | 1839 | 量最大，最后 |
| **总计** | | **2448** | |

每批流程：dry-run diff → 老顽童抽验 ≥5 条 → apply → 更新基线 → 下一批。

## 复现命令

```bash
cd C:\Users\Administrator\Desktop\wiki
python -c "
import subprocess, sys, re, random

r = subprocess.run([sys.executable, '90_control/scripts/kdo_lint.py', '30_wiki'],
    capture_output=True, text=True, timeout=120, encoding='utf-8', errors='replace')
lines = (r.stdout + r.stderr).splitlines()

pairs = []
for l in lines:
    m = re.search(r'F2 MISSING BACKLINK:\s*(\S+)\s*→\s*(\S+)', l)
    if m: pairs.append((m.group(1), m.group(2)))

def typ(cid):
    for p in ['concept-', 'framework-', 'tool-', 'case-', 'dk-', 'method-', 'system-']:
        if cid.startswith(p): return p.rstrip('-')
    return 'other'

same_type = [(f,t) for f,t in pairs if typ(f)==typ(t) and typ(f) not in ('other',)]
print(f'Total same-type: {len(same_type)}')

random.seed(42)
sample = random.sample(same_type, 50)
for i, (f, t) in enumerate(sample):
    print(f'{i+1}|[{typ(f)}]|{f}|{t}')
"
```

预期输出：Total same-type: 2448，50 条与上表逐条一致。
