# -*- coding: utf-8 -*-
from pathlib import Path

qpath = Path('C:/Users/Administrator/Desktop/wiki/70_product/tasks/production-queue.md')
with qpath.open('r', encoding='utf-8', newline='') as f:
    lines = f.read().splitlines()

new_row = "| 52 | `task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure` | Y模型根节点化：Schema + GraphRAG + 旧卡 deprecation 基础设施 | queued | 黄药师 | schema + GraphRAG + 文档 | 依赖 #51 新卡产出；schema 设计可并行 | `60_feedback/tasks/task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure.md` | 黄药师提出 Y模型应成为 KDO 知识图谱根节点；本任务在基础设施层实现：新增 is_root_node / replaces / deprecated_by schema 字段；kdo lint 新增校验；kdo index --rebuild 支持根节点权重和 theory/fact/practice 边类型；3 张旧卡正式 deprecated；创建 system-kdo-factory-as-Y-model.md 文档 |"

lines.append(new_row)
print('appended #52')

with qpath.open('w', encoding='utf-8', newline='') as f:
    f.write('\n'.join(lines))
print('queue written')

# Dashboard
dpath = Path('C:/Users/Administrator/Desktop/wiki/70_product/tasks/dashboard.md')
with dpath.open('r', encoding='utf-8', newline='') as f:
    text = f.read()

old51 = '| task_20260703_laowantong-yitang-Y-model-foundation-production | 一堂底层逻辑域：Y模型 + 实事求是 + 解放思想（3 framework + 1 tool + 1 dk + 2 case） | queued | 老顽童(Kimi) | P1 | task_20260703_laowantong-yitang-Y-model-foundation-production.md | 王语嫣判断：Y模型是一堂最底层元框架，科学理念 = Y模型，实事求是和解放思想是从 Y模型生长出的两层能力；产出 7 张卡填补 KDO 底层逻辑域空白；重写升级 3 张旧 concept 卡并标记 deprecated；反向更新 >=17 张已有卡 related |'
new51 = old51 + '\n| task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure | Y模型根节点化：Schema + GraphRAG + 旧卡 deprecation 基础设施 | queued | 黄药师 | P1 | task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure.md | 黄药师提出 Y模型应成为 KDO 知识图谱根节点；基础设施层实现：is_root_node / replaces / deprecated_by schema 字段；kdo lint 校验；kdo index --rebuild 根节点权重和 theory/fact/practice 边类型；3 张旧卡 deprecated；创建 system-kdo-factory-as-Y-model.md |'

if old51 in text:
    text = text.replace(old51, new51, 1)
    print('dashboard #52 row added')
else:
    print('dashboard #51 row NOT FOUND')

text = text.replace('Queued: 12', 'Queued: 13', 1)
text = text.replace('Total Active: 20', 'Total Active: 21', 1)
print('summary updated')

old_note = '> **🆕 新增 #51**：一堂底层逻辑域建设：Y模型 + 实事求是 + 解放思想；王语嫣判断 Y模型是一堂最底层元框架，科学理念 = Y模型，实事求是和解放思想是从 Y模型生长出的两层能力；产出 3 framework + 1 tool + 1 dk + 2 case 共 7 张卡；重写升级 3 张旧 concept 卡；为后续 Y模型教练 Agent 奠定方法论底座。'
new_note = old_note + '\n>\n> **🆕 新增 #52**：Y模型根节点化基础设施，由黄药师负责；在 schema / GraphRAG / deprecation / 文档四个层面把 Y模型推到 KDO 知识图谱根节点位置；让 KDO 工厂的运行方式本身成为 Y模型实例；为后续 Agent 实测回流管线（#53）奠定图索引基础。'

if old_note in text:
    text = text.replace(old_note, new_note, 1)
    print('dashboard note added')
else:
    print('dashboard note NOT FOUND')

dpath.write_text(text, encoding='utf-8', newline='')
print('dashboard written')
