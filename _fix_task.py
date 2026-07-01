# -*- coding: utf-8 -*-
from pathlib import Path

path = Path('C:/Users/Administrator/Desktop/wiki/60_feedback/tasks/task_20260702_laowantong-yitang-scientific-sales-methodology-production.md')
text = path.read_text(encoding='utf-8')

# 1. Insert Card 11 and 12 before "## 三、已有卡 related 补链清单"
old_before3 = '''9. **Related**：≥5 条。

---

## 三、已有卡 related 补链清单'''
# Need unique context: after Card 10. Use Card 10's Synthesis line + Related line.
old_card10_tail = '''9. **Related**：≥5 条。

---

## 三、已有卡 related 补链清单'''
new_card10_tail = '''9. **Related**：≥5 条。

---

### Card 11: `case-yitang-sales-transformation-tuliaogongsi`

**类型**：case  
**主域**：sales / manufacturing-distribution / b2b / yitang  
**confidence**：0.80  
**trust_level**：medium

**必须包含的 section**：
1. **Background**：涂料公司，海量注册线索但转化率低，销售精力分散。
2. **Problem**：10 万线索分不清谁是真客户；销售平均分配精力；S 级客户被淹没；分层脱离目标。
3. **Decision**：用一堂用户分层四步法重做 SABC 分级，把资源集中到高价值客户。
4. **Process**：
   - 明确阶段目标（利润 vs 标杆）
   - 提出分层假设（公司规模、项目类型、采购周期、地域）
   - 验证假设（历史成交画像 + 抽样访谈）
   - 执行分层（10 万 → 20 S 级 + 200 A 级，其余自动培育）
5. **Result**：销售 80% 精力聚焦 Top 220 客户，S 级转化率显著提升。
6. **Lessons**：分层和目标挂钩；没有验证的分层是拍脑袋；B/C 级线索需自动培育。
7. **Failure Modes**：只看数量不看质量、分层标准不更新、B/C 级直接丢弃、销售抵制少量线索。
8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、`tool-yitang-customer-segmentation-4step`、`tool-yitang-sales-performance-management`、`master-decision-hygiene`。
9. **Related**：≥5 条。

---

### Card 12: `tool-opc-sales-dialogue-assistant`

**类型**：tool  
**主域**：personal-os / ai-sales-agent / yitang  
**confidence**：0.85  
**trust_level**：high

**定位**：OPC 销售智能体 MVP 规格卡，可直接作为 system prompt 使用。

**必须包含的 section**：
1. **When to Use**：一人公司创始人同时跟进多个客户、对话散落、容易忘记阶段、回复前需快速判断。
2. **核心功能**：读对话 → 想策略 → 给话术。
3. **输入**：客户对话记录（微信/邮件/通话转写/CRM 备注）、可选分层标签、可选当前阶段。
4. **输出**：
   - 客户意图与阶段判断（接触/购买/付款/履约 + 情绪/抗拒点）
   - 下一步建议（该做/不该做什么）
   - 2-3 个可直接选用或微调的回复选项
5. **工作逻辑**：
   - 用 `tool-yitang-customer-segmentation-4step` 判断客户等级
   - 用 `tool-yitang-sales-process-decomposition` 识别阶段与关键决策点
   - 用 `tool-yitang-value-proposition-4step` 选择匹配卖点
   - 用 `tool-yitang-sales-performance-management` 判断推进/预警
   - 生成 2-3 个不同风格回复（直接型/共情型/提问型）
6. **System Prompt 模板**：提供可直接复制到 Claude/GPT 自定义指令的精简模板。
7. **边界与风险提示**：不替代关键信任建立；不自动发送消息；隐私数据需合规处理。
8. **Checklist**：≥8 项。
9. **Anti-patterns**：照搬话术不调整、把 AI 建议当最终决策、关键谈判让 AI 代写、忽视客户情绪。
10. **Critique**：≥3 个外部反对者 + ≥2 个内部局限。
11. **Synthesis**：桥接 `opc-ai-sales-agent-architecture`、`human-ai-collaboration-double-triangle`、`framework-yitang-scientific-sales-five-step`、4 张 Step tool 卡。
12. **Related**：≥5 条。

---

## 三、已有卡 related 补链清单'''
if old_card10_tail in text:
    text = text.replace(old_card10_tail, new_card10_tail, 1)
    print('Card 11/12 inserted')
else:
    print('Card 11/12 insertion point NOT FOUND')

# 2. Fix boundary section: replace whole section from "## 四、关键纠偏与边界" to next "---"
import re
boundary_pattern = re.compile(r'## 四、关键纠偏与边界\n\n.*?(?=\n\n---\n\n## 五、验收标准)', re.DOTALL)
new_boundary = '''## 四、关键纠偏与边界

1. **不重复建设**：用户分层、价值主张、目标管理、工具化、决策卫生等概念已有 KDO 卡覆盖，本次只做销售域实例化，通过 related 引用。
2. **用户分层与卖点独立成卡**：未来咨询「该重点跟进哪些客户」和「怎么写卖点」可分别调用，避免合并后检索困难。
3. **案例处理**：剧本杀 SaaS、美容院、涂料公司作为三个完整转型案例独立成卡，分别覆盖 To B 初创 SaaS、To C 门店零售、传统工业分销；快钱支付、儿童记忆力培训、iPhone 充电器等作为工具卡嵌入式证据。
4. **数字降级**：课程中的「2 天」「60 分」「200 个案例」「20 个记录」「85-90% 完成率」等描述为项目经验/个人做法，不当作普适真理。
5. **OPC 智能体适配内嵌**：`tool-yitang-customer-segmentation-4step`、`tool-yitang-value-proposition-4step`、`tool-yitang-sales-process-decomposition`、`tool-yitang-sales-performance-management`、`framework-yitang-sales-incentive-6d` 等卡必须包含「OPC 智能体适配」小节，说明如何映射为 system prompt；不单独为这些子模块建卡，避免碎片化。
6. **MVP 智能体优先**：智能体层只新建 `tool-opc-sales-dialogue-assistant` 一张卡，其余 10 个智能体规格待本批卡片终审后根据反馈分批扩展。
7. **法律声明**：商标/合同/提成等涉及法律判断的案例，工具卡和 framework 卡中必须明确「AI/课程只提供公共知识扫盲，最终法律结论需专业机构复核」。
8. **OPC 改编**：激励团队、周会三要点、拆目标到个人等模块不直接适用于 OPC，需在相关卡片中明确 OPC 版改编提示。
9. **跨域融合**：每张卡必须同时桥接 sales 域和对应底层方法论域（strategy / management / ai-collaboration 等），不能只讲销售技巧。'''
if boundary_pattern.search(text):
    text = boundary_pattern.sub(new_boundary, text)
    print('boundary fixed')
else:
    print('boundary pattern NOT FOUND')

# 3. Fix acceptance criteria
old_lint = '''- [ ] 10 张目标卡 `kdo lint` 0 ERROR；新增 WARNING 需在任务单中说明。'''
new_lint = '''- [ ] 12 张目标卡 `kdo lint` 0 ERROR；新增 WARNING 需在任务单中说明。'''
if old_lint in text:
    text = text.replace(old_lint, new_lint, 1)
    print('lint count fixed')
else:
    print('lint count NOT FOUND')

old_related_count1 = '''- [ ] ≥26 张已有卡的 related 已反向更新。'''
new_related_count1 = '''- [ ] ≥28 张已有卡的 related 已反向更新。'''
if old_related_count1 in text:
    text = text.replace(old_related_count1, new_related_count1, 1)
    print('related count 1 fixed')
else:
    print('related count 1 NOT FOUND')

old_opc_related = '''- [ ] `opc-ai-sales-agent-architecture.md` 的 related 已加入 10 张新卡回链。'''
new_opc_related = '''- [ ] `opc-ai-sales-agent-architecture.md` 的 related 已加入 12 张新卡回链。'''
if old_opc_related in text:
    text = text.replace(old_opc_related, new_opc_related, 1)
    print('opc related count fixed')
else:
    print('opc related count NOT FOUND')

# 4. Fix workload line
old_work = '''- **预计工时**：老顽童生产 4-5 天 + 欧阳锋终审 1 天。'''
new_work = '''- **预计工时**：老顽童生产 5-6 天 + 欧阳锋终审 1-2 天。'''
if old_work in text:
    text = text.replace(old_work, new_work, 1)
    print('workload fixed')
else:
    print('workload NOT FOUND')

path.write_text(text, encoding='utf-8', newline='')
print('task written')
