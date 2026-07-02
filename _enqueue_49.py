# -*- coding: utf-8 -*-
from pathlib import Path

qpath = Path('C:/Users/Administrator/Desktop/wiki/70_product/tasks/production-queue.md')
with qpath.open('r', encoding='utf-8', newline='') as f:
    lines = f.read().splitlines()

new_row = "| 49 | `task_20260702_laowantong-opc-sales-agent-incremental-specs` | OPC 销售智能体军团增量：开场/异议/自我驱动 3 张 agent-spec | queued | - | 3 张 | 依赖 #44 终审通过；建议 #47 完成至少 2 张后再启动 | `60_feedback/tasks/task_20260702_laowantong-opc-sales-agent-incremental-specs.md` | 用户提出「边做边玩」补充销售智能体军团缺口：开场 3 分钟助手 / 异议处理助手 / 自我驱动助手；优先级 P2；Agent 做带宽、人做判断；反向更新 OPC 架构与对话助手 related |"

insert_idx = None
for i, line in enumerate(lines):
    if line.startswith('| 47 |'):
        insert_idx = i + 1
        break

if insert_idx is None:
    lines.append(new_row)
    print('appended at end')
else:
    lines.insert(insert_idx, new_row)
    print('inserted after #47 at line', insert_idx+1)

with qpath.open('w', encoding='utf-8', newline='') as f:
    f.write('\n'.join(lines))
print('queue written')

# Dashboard
dpath = Path('C:/Users/Administrator/Desktop/wiki/70_product/tasks/dashboard.md')
with dpath.open('r', encoding='utf-8', newline='') as f:
    text = f.read()

# Add #49 row after #47 row
old47 = '| task_20260702_laowantong-opc-sales-agent-specs-production | OPC 销售智能体军团首批规格卡：从 #44 方法论卡片编译 4 张 agent-spec | in_progress | 老顽童(Kimi) | P1 | task_20260702_laowantong-opc-sales-agent-specs-production.md | KDO Agent 化审计结论：把 #44 中 4 张核心 tool 卡编译成可直接当 system prompt 使用的 agent-spec：客户分级助手 / 卖点生成助手 / 销售阶段追踪助手 / 业绩监控助手；#44 已终审通过，本任务立即启动；Agent 做带宽、人做判断；反向更新 OPC 架构与对话助手 related |'
new47 = old47 + '\n| task_20260702_laowantong-opc-sales-agent-incremental-specs | OPC 销售智能体军团增量：开场/异议/自我驱动 3 张 agent-spec | queued | - | P2 | task_20260702_laowantong-opc-sales-agent-incremental-specs.md | 用户提出「边做边玩」补充智能体军团缺口：开场 3 分钟助手 / 异议处理助手 / OPC 自我驱动助手；优先级 P2；依赖 #44 和 #47 部分进度；反向更新 OPC 架构与对话助手 related |'

if old47 in text:
    text = text.replace(old47, new47, 1)
    print('dashboard #49 row added')
else:
    print('dashboard #47 row NOT FOUND')

# Update summary counts
text = text.replace('Queued: 10', 'Queued: 11', 1)
text = text.replace('Total Active: 17', 'Total Active: 18', 1)
print('summary counts updated')

# Add note after #47 note
old_note = '> **🆕 新增 #47**：KDO Agent 化审计结论：一堂科学销售方法论已完成九层深挖诊断；王语嫣评级 A；经用户挑战深度后从 6 张扩展为 10 张，再按黄药师建议+王语嫣独立判断扩展为 12 张：1 framework（五步法总览） + 5 tool（用户分层 / 卖点提炼 / 过程拆解 / 业绩管理 / 工具箱） + 1 framework（六维激励） + 3 case（剧本杀 SaaS / 美容院 / 涂料公司） + 1 dk（销售反模式） + 1 tool（`tool-opc-sales-dialogue-assistant` MVP 对话助手）；MVP 对话助手解决 OPC 同时聊多客户跟丢/跟乱/跟错节奏的痛点，不改变销售动作，只输出「小抄」；反向更新 >=28 张已有卡 related；`opc-ai-sales-agent-architecture.md` 需回链并补充 MVP 启动路径。\n>\n> **🆕 新增 #47**：KDO Agent 化审计结论：把 #44 中 4 张核心 tool 卡编译成可直接当 system prompt 使用的 agent-spec：客户分级助手 / 卖点生成助手 / 销售阶段追踪助手 / 业绩监控助手；#44 已终审通过，本任务立即启动；Agent 做带宽、人做判断；反向更新 OPC 架构与对话助手 related。'
new_note = old_note + '\n>\n> **🆕 新增 #49**：用户提出「边做边玩」补充智能体军团缺口，新增 3 张 agent-spec：开场 3 分钟助手 / 异议处理助手 / OPC 自我驱动助手；优先级 P2；依赖 #44 和 #47 部分进度；反向更新 OPC 架构与对话助手 related。'

if old_note in text:
    text = text.replace(old_note, new_note, 1)
    print('dashboard note added')
else:
    print('dashboard note NOT FOUND')

dpath.write_text(text, encoding='utf-8', newline='')
print('dashboard written')
