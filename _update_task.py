# -*- coding: utf-8 -*-
from pathlib import Path

path = Path('C:/Users/Administrator/Desktop/wiki/60_feedback/tasks/task_20260702_laowantong-yitang-scientific-sales-methodology-production.md')
text = path.read_text(encoding='utf-8')

# 1. frontmatter title
text = text.replace(
    'title: "一堂科学销售方法论：1 framework + 5 tool + 1 framework + 2 case + 1 dk（销售域 / OPC 智能体底层）"',
    'title: "一堂科学销售方法论：1 framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool（OPC 智能体 / 销售域）"',
    1
)
print('task title updated')

# 2. expected_cards
text = text.replace('expected_cards: 10', 'expected_cards: 12', 1)
print('task expected_cards updated')

# 3. frontmatter related
old_related = '''related:
  - framework-yitang-scientific-sales-five-step
  - tool-yitang-customer-segmentation-4step
  - tool-yitang-value-proposition-4step
  - tool-yitang-sales-process-decomposition
  - tool-yitang-sales-performance-management
  - framework-yitang-sales-incentive-6d
  - tool-yitang-sales-toolkit-radar
  - dk-yitang-sales-common-pitfalls
  - case-yitang-sales-transformation-jubensha-saas
  - case-yitang-sales-transformation-meirongyuan
  - opc-ai-sales-agent-architecture
---'''
new_related = '''related:
  - framework-yitang-scientific-sales-five-step
  - tool-yitang-customer-segmentation-4step
  - tool-yitang-value-proposition-4step
  - tool-yitang-sales-process-decomposition
  - tool-yitang-sales-performance-management
  - framework-yitang-sales-incentive-6d
  - tool-yitang-sales-toolkit-radar
  - dk-yitang-sales-common-pitfalls
  - case-yitang-sales-transformation-jubensha-saas
  - case-yitang-sales-transformation-meirongyuan
  - case-yitang-sales-transformation-tuliaogongsi
  - tool-opc-sales-dialogue-assistant
  - opc-ai-sales-agent-architecture
---'''
if old_related in text:
    text = text.replace(old_related, new_related, 1)
    print('task related updated')
else:
    print('task related NOT FOUND')

# 4. main heading and version note
text = text.replace(
    '# 一堂科学销售方法论：1 framework + 5 tool + 1 framework + 2 case + 1 dk',
    '# 一堂科学销售方法论：1 framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool（OPC 智能体）',
    1
)
print('task main heading updated')

old_note = '''> OPC 适配：科学销售五步法可直接映射为 OPC 智能体军团，已有 `opc-ai-sales-agent-architecture.md` 作为承接，本次产出需反向更新其 related。
> 版本说明：初版规划 6 张卡，经用户挑战后重新判断：6 张会牺牲「未来直接拿来咨询可用」的深度，扩展为 10 张卡——用户分层与卖点提炼独立成卡，新增 2 个转型 case 和 1 张反模式 dk。'''
new_note = '''> OPC 适配：科学销售五步法可直接映射为 OPC 智能体军团，已有 `opc-ai-sales-agent-architecture.md` 作为承接，本次产出需反向更新其 related。
> 版本说明：
> - 初版规划 6 张卡，经用户挑战后扩展为 10 张卡。
> - 黄药师建议：在 10 张基础上增加操作层工具卡、案例卡与 OPC 智能体规格卡，预计 12-15 张。
> - 王语嫣独立判断：操作层细节（SABC 算法、A/B 测试、状态机等）并入现有 tool/framework 卡的 OPC 适配小节，不再单独建卡；新增 **1 个涂料公司 case** 覆盖传统工业分销场景，新增 **1 张 `tool-opc-sales-dialogue-assistant` 作为 MVP 智能体规格卡**；智能体层不一次性铺开 8-10 张，先做可直接当 system prompt 运行的对话助手。最终确定为 **12 张卡**。'''
if old_note in text:
    text = text.replace(old_note, new_note, 1)
    print('task version note updated')
else:
    print('task version note NOT FOUND')

# 5. Section 二 heading
text = text.replace('## 二、10 张目标卡', '## 二、12 张目标卡', 1)
print('task sec2 heading updated')

# 6. Insert Card 11 and 12 after Card 10
old_after10 = '''8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、`tool-yitang-customer-segmentation-4step`、`tool-yitang-sales-process-decomposition`、`tool-yitang-sales-performance-management`、`framework-yitang-sales-incentive-6d`、`tool-yitang-sales-toolkit-radar`、`framework-yitang-channel-exploration-4step`。
9. **Related**：≥5 条。

---

## 三、已有卡 related 补链清单'''
new_after10 = '''8. **Synthesis**：桥接 `framework-yitang-scientific-sales-five-step`、`tool-yitang-customer-segmentation-4step`、`tool-yitang-sales-process-decomposition`、`tool-yitang-sales-performance-management`、`framework-yitang-sales-incentive-6d`、`tool-yitang-sales-toolkit-radar`、`framework-yitang-channel-exploration-4step`。
9. **Related**：≥5 条。

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
if old_after10 in text:
    text = text.replace(old_after10, new_after10, 1)
    print('task Card 11/12 inserted')
else:
    print('task Card 11/12 insertion point NOT FOUND')

# 7. Add entries to 已有卡补链清单
old_list = '''21. `case-yitang-sales-routine-deconstruction`
22. `case-yitang-ai-painting-commercialization`
23. `opc-ai-sales-agent-architecture`
24. `human-ai-collaboration-double-triangle`
25. `framework-lean-pivot-decision`
26. `dk-yitang-channel-exploration-traps`'''
new_list = '''21. `case-yitang-sales-routine-deconstruction`
22. `case-yitang-ai-painting-commercialization`
23. `opc-ai-sales-agent-architecture`
24. `human-ai-collaboration-double-triangle`
25. `framework-lean-pivot-decision`
26. `dk-yitang-channel-exploration-traps`
27. `case-yitang-sales-transformation-tuliaogongsi`
28. `tool-opc-sales-dialogue-assistant`'''
if old_list in text:
    text = text.replace(old_list, new_list, 1)
    print('task related list updated')
else:
    print('task related list NOT FOUND')

# 8. Update 关键纠偏与边界 to mention OPC adaptation subsections
old_boundary = '''1. **不重复建设**：用户分层、价值主张、目标管理、工具化、决策卫生等概念已有 KDO 卡覆盖，本次只做销售域实例化，通过 related 引用。
2. **用户分层与卖点独立成卡**：未来咨询「该重点跟进哪些客户」和「怎么写卖点」可分别调用，避免合并后检索困难。
3. **案例处理**：剧本杀 SaaS 和美容院作为两个完整转型案例独立成卡，覆盖 To B 与 To C 场景；快钱支付、涂料公司、儿童记忆力培训、iPhone 充电器等作为工具卡嵌入式证据。
4. **数字降级**：课程中的「2 天」「60 分」「200 个案例」「20 个记录」「85-90% 完成率」等描述为项目经验/个人做法，不当作普适真理。'''
new_boundary = '''1. **不重复建设**：用户分层、价值主张、目标管理、工具化、决策卫生等概念已有 KDO 卡覆盖，本次只做销售域实例化，通过 related 引用。
2. **用户分层与卖点独立成卡**：未来咨询「该重点跟进哪些客户」和「怎么写卖点」可分别调用，避免合并后检索困难。
3. **案例处理**：剧本杀 SaaS、美容院、涂料公司作为三个完整转型案例独立成卡，分别覆盖 To B 初创 SaaS、To C 门店零售、传统工业分销；快钱支付、儿童记忆力培训、iPhone 充电器等作为工具卡嵌入式证据。
4. **数字降级**：课程中的「2 天」「60 分」「200 个案例」「20 个记录」「85-90% 完成率」等描述为项目经验/个人做法，不当作普适真理。
5. **OPC 智能体适配内嵌**：`tool-yitang-customer-segmentation-4step`、`tool-yitang-value-proposition-4step`、`tool-yitang-sales-process-decomposition`、`tool-yitang-sales-performance-management`、`framework-yitang-sales-incentive-6d` 等卡必须包含「OPC 智能体适配」小节，说明如何映射为 system prompt；不单独为这些子模块建卡，避免碎片化。
6. **MVP 智能体优先**：智能体层只新建 `tool-opc-sales-dialogue-assistant` 一张卡，其余 10 个智能体规格待本批卡片终审后根据反馈分批扩展。'''
if old_boundary in text:
    text = text.replace(old_boundary, new_boundary, 1)
    print('task boundary updated')
else:
    print('task boundary NOT FOUND')

# 9. Update acceptance criteria count
old_accept = '''- [ ] 10 张目标卡 `kdo pre-submit` PASS，无新增 ERROR。'''
new_accept = '''- [ ] 12 张目标卡 `kdo pre-submit` PASS，无新增 ERROR。'''
if old_accept in text:
    text = text.replace(old_accept, new_accept, 1)
    print('task accept count updated')
else:
    print('task accept count NOT FOUND')

# Update specific card checks
old_checks = '''- [ ] `dk-yitang-sales-common-pitfalls` 包含 6 个反模式、≥6 条预警信号、每个陷阱的修复动作。
- [ ] `case-yitang-sales-transformation-jubensha-saas` 包含 Background/Problem/Decision/Process/Result/Lessons/Failure Modes。
- [ ] `case-yitang-sales-transformation-meirongyuan` 包含 Background/Problem/Decision/Process/Result/Lessons/Failure Modes。'''
new_checks = '''- [ ] `dk-yitang-sales-common-pitfalls` 包含 6 个反模式、≥6 条预警信号、每个陷阱的修复动作。
- [ ] `case-yitang-sales-transformation-jubensha-saas` 包含 Background/Problem/Decision/Process/Result/Lessons/Failure Modes。
- [ ] `case-yitang-sales-transformation-meirongyuan` 包含 Background/Problem/Decision/Process/Result/Lessons/Failure Modes。
- [ ] `case-yitang-sales-transformation-tuliaogongsi` 包含 Background/Problem/Decision/Process/Result/Lessons/Failure Modes。
- [ ] `tool-opc-sales-dialogue-assistant` 包含 When to Use/输入/输出/工作逻辑/System Prompt 模板/边界与风险/Checklist/Anti-patterns/Critique/Synthesis/Related。'''
if old_checks in text:
    text = text.replace(old_checks, new_checks, 1)
    print('task card checks updated')
else:
    print('task card checks NOT FOUND')

# 10. Update production order table
old_order = '''| 第六批 | `dk-yitang-sales-common-pitfalls` + `case-yitang-sales-transformation-jubensha-saas` + `case-yitang-sales-transformation-meirongyuan` | 反模式 + 两个转型案例 |

---'''
new_order = '''| 第六批 | `dk-yitang-sales-common-pitfalls` + `case-yitang-sales-transformation-jubensha-saas` + `case-yitang-sales-transformation-meirongyuan` + `case-yitang-sales-transformation-tuliaogongsi` | 反模式 + 三个转型案例 |
| 第七批 | `tool-opc-sales-dialogue-assistant` | OPC 智能体 MVP 规格卡，放在最后以便聚合前五步工具逻辑 |

---'''
if old_order in text:
    text = text.replace(old_order, new_order, 1)
    print('task order updated')
else:
    print('task order NOT FOUND')

# 11. Update estimated workload
text = text.replace('预计工时：老顽童生产 4-5 天 + 欧阳锋终审 1 天。', '预计工时：老顽童生产 5-6 天 + 欧阳锋终审 1-2 天。', 1)
print('task workload updated')

path.write_text(text, encoding='utf-8', newline='')
print('task written')
