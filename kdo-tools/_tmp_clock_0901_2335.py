# -*- coding: utf-8 -*-
# 王语嫣时钟值守 2026-09-01 23:35 拍：编排动作批量落盘（保持原换行符）
import re

# ---------- 1. production-queue.md ----------
qp = '70_product/tasks/production-queue.md'
qraw = open(qp, 'rb').read()
q_eol = '\r\n' if b'\r\n' in qraw else '\n'
lines = qraw.decode('utf-8').split(q_eol)

NOW = '2026-09-01 23:35'
done = []

def strike(idx, ruling):
    l = lines[idx]
    assert not l.lstrip().startswith('- ~~'), 'already struck: ' + l[:80]
    assert l.lstrip().startswith('- '), 'not a list item: ' + l[:80]
    lines[idx] = '- ~~' + l.lstrip()[2:] + '~~ → ' + ruling

for i, l in enumerate(lines):
    if l.startswith('- [gate-blocked] role-liveness｜09-01 23:07') and 'huangyaoshi 全实例疑似死亡' in l and '23:02:00' in l:
        strike(i, '已知问题划销（%s 王语嫣）：role-liveness 冷却重报——check-liveness 实测全死角色 0（cli 心跳 30.9min 在岗），queued 0 无施工实例=收工空窗架构常态' % NOW); done.append('liveness')
    elif l.startswith('- [gate-blocked] task_20260902_skills-assistant-research-core-integration') and 'F-035' in l:
        strike(i, '已化解划销（%s 王语嫣）：#594 已欧阳锋双审 PASS A 闭环（首审+独立复核会签留档），F-035 时序残留——意见书负向断言（无主43）已被终审「无主总数亲数=31」实证消化' % NOW); done.append('f035')
    elif l.startswith('- [gate-blocked] 建议书_20260901_skill健康度勘察与检测方法论.md'):
        strike(i, '编排决策（%s 王语嫣）：**部分采纳立项 #596**（动作1 manifest 72个补建+动作2 name修复，skills-assistant，待#595收口开工）；动作3/9 并黄药师欠账候选（BOM/缺title 与 #595 未做项①同源）；动作4/5/6 缓议一拍（挂载面刚经 #594/#595 两连改）；动作7/8 随 #596 二期；frontmatter 已对齐 orchestrated+decision' % NOW); done.append('proposal')
    elif l.startswith('- 00_inbox/泡泡玛特的拆解/拆书会第218期'):
        strike(i, '已诊断+立项 #597（%s 王语嫣）：域归属=strategy/商业案例（泡泡玛特王宁长期主义经营哲学，李翔《因为独特》精华提炼 10.7KB）；初判=拆书会系列 90+ 卡先例、结构完整金句密度高，与库内 case-popmart-prospectus-pricing（招股书定价）/tool-blind-box-mechanism（盲盒机制）互补不撞车；按 0831/0901 inbox 自动化流水线立项产卡 2-3 张（老顽童 #597），终审归欧阳锋；素材原文不动' % NOW); done.append('inbox218')
print('struck:', done)
assert len(done) == 4, 'expected 4 strikes, got %d' % len(done)

row596 = '| 596 | `task_20260901_skills-assistant-skill-manifest-batch` | 全厂skill manifest补建批（健康度建议书动作1+2，王语嫣部分采纳）：72/76缺manifest.yaml按deep-debug/anti-ai-bs样板补建（trigger.natural_language+adapted_from+适用agent）+2处name与目录名不一致修复 | queued | skills-assistant | 76/76 manifest齐+name清零+INDEX/MOUNT-MATRIX重扫fresh | 建议书_20260901_skill健康度勘察（部分采纳裁定节在档）；待#595收口开工 | `60_feedback/tasks/task_20260901_skills-assistant-skill-manifest-batch.md` | 防扫描器并发写（#595收口前置）；不动挂载面（动作4/5/6缓议）；欧阳锋终审 |'
row597 = '| 597 | `task_20260901_laowantong-chaishu218-unique-cards` | 拆书会218期《因为独特》（泡泡玛特王宁）产卡2-3张：case长期主义经营+消费两件事（满足感/存在感）+品牌感官包裹感/减法护城河 | queued | laowantong | 2-3卡+source_refs+pre-submit+执行报告 | inbox自动化流水线（0831/0901老朱直令）；拆书会90+卡先例 | `60_feedback/tasks/task_20260901_laowantong-chaishu218-unique-cards.md` | 与库内popmart定价卡/盲盒机制卡互补不撞车；素材原文不动；欧阳锋终审 |'
ins = None
for i, l in enumerate(lines):
    if l.startswith('| 595 | `task_20260902_skills-assistant-frontmatter-backfill`'):
        ins = i + 1
        break
assert ins, 'row595 not found'
assert all('| 596 |' not in x and '| 597 |' not in x for x in lines), 'rows already exist'
lines[ins:ins] = [row596, row597]
print('rows inserted after line', ins)

open(qp, 'wb').write(q_eol.join(lines).encode('utf-8'))
print('queue written, eol=%r' % q_eol)

# ---------- 2. proposal frontmatter + ruling section ----------
pp = '60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md'
praw = open(pp, 'rb').read()
p_eol = '\r\n' if b'\r\n' in praw else '\n'
p = praw.decode('utf-8')
if 'status: pending-review' in p:
    p = p.replace('status: pending-review', 'status: orchestrated' + p_eol + 'decision: 部分采纳（2026-09-01 王语嫣）：动作1+2→#596；动作3/9→黄药师欠账候选（同源#595未做项①）；动作4/5/6缓议一拍；动作7/8随#596二期', 1)
    print('proposal status patched')
ruling = p_eol + '## 编排裁定（王语嫣 2026-09-01 23:35，职权内四选一：**部分采纳**）' + p_eol + p_eol
ruling += '- **采纳立项 #596（skills-assistant，P1）**：动作1（72 个 manifest.yaml 按 deep-debug / anti-ai-bs-three-moves / research-core 样板补建：trigger.natural_language ≥3 触发词组 + adapted_from 来源卡 + 适用agent）+ 动作2（content-production-polish / knowledge-collision 两处 name 与目录名不一致修复）。开工前置：#595 终审收口（防 INDEX/MOUNT-MATRIX 扫描器并发写）。' + p_eol
ruling += '- **并入既有欠账候选（不重复立项）**：动作3（37 BOM 清理）、动作9（8 维检测纳入扫描脚本）——与 #595 执行报告未做项① BOM/缺 title 欠账同源，归口黄药师基建批量出。' + p_eol
ruling += '- **缓议（观察一拍）**：动作4（22 个已挂载🔴降级/下架判定）、动作5（nine-character / skill-architecture-design 双🟢优先挂载）、动作6（research 武器库挂载瘦身）——挂载面刚经 #594（research-core 21 单元）+#595（frontmatter 全量）两连改，稳定一拍再动，防路由面连续抖动。' + p_eol
ruling += '- **随 #596 二期**：动作7（53 个 legacy skill 归档裁定）、动作8（test-prompts.json 先补 🟢/🟡 14 个）。' + p_eol + p_eol
ruling += '> 报告本体留档本区；探针三元组口径已按 status=orchestrated+decision 对齐（#506 中文终态枚举扩展仍挂观察项）。' + p_eol
if '## 编排裁定（王语嫣' not in p:
    p = p.rstrip() + ruling
    print('ruling section appended')
open(pp, 'wb').write(p.encode('utf-8'))

# ---------- 3. task files ----------
def wf(path, fm_fields, body):
    eol = '\r\n'
    fm = '---' + eol
    for k, v in fm_fields:
        fm += '%s: %s' % (k, v) + eol
    fm += '---' + eol
    open(path, 'wb').write((fm + body.replace('\n', eol)).encode('utf-8'))
    print('wrote', path)

wf('60_feedback/tasks/task_20260901_skills-assistant-skill-manifest-batch.md',
   [("id", "'596'"), ("title", "全厂 skill manifest.yaml 补建批 + 2 处 name 不一致修复（Skills助理第三单）"), ("type", "skill-production"), ("status", "queued"), ("priority", "P1"), ("assignee", "skills-assistant"), ("created_by", "王语嫣"), ("created_at", "2026-09-01"), ("source_refs", "\n- 60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md\n- 40_outputs/capabilities/skills/INDEX.md\n- 40_outputs/capabilities/skills/MOUNT-MATRIX.md"), ("instance", "skills-assistant"), ("updated_at", "'2026-09-01T23:35:00+08:00'")],
"""# #596 全厂 skill manifest 补建批（健康度建议书动作1+2，王语嫣部分采纳立项）

## 背景

Skills助理健康度勘察（建议书_20260901，文末裁定节在档）实测：72/76 缺 manifest.yaml（仅 deep-debug / nine-character-ai-collaboration / research-core / skill-architecture-design 有），渐进式披露第一层与三写一致真相源系统性缺位；另 2 处 frontmatter name 与目录名不一致（content-production-polish=Vikki-human-speech、knowledge-collision=knowledge-collision-workflow）。王语嫣 2026-09-01 23:35 裁定部分采纳，动作1+2 立项本单。

## 任务

1. 为 72 个缺 manifest 的 shared skill 按样板（deep-debug / anti-ai-bs-three-moves / research-core）补建 manifest.yaml：必含 trigger.natural_language（≥3 触发词组）+ adapted_from（来源卡路径；确无来源卡的写 none 并注明）+ 适用agent
2. 内容依据各 skill SKILL.md 正文提炼，不虚构触发场景；53 个 description<80 字符的扩写不在本单（frontmatter 归 #595 已收口口径，避免二次触碰）
3. 修复 2 处 name 与目录名不一致（name 对齐目录名）
4. 重跑 scan_skills_registry.py 刷新 INDEX/MOUNT-MATRIX，`--check` 🟢 fresh
5. pre-submit 抽验 5 个 + 执行报告五字段 + complete 提审（完整 task_id）

## 验收标准

1. 76/76 skill manifest.yaml 在案（72 新建+4 既有），三件套字段齐、零虚构
2. 2 处 name 不一致清零
3. `--check` fresh + pre-submit 抽验 5/5 PASS + git diff 仅 manifest/name 相关变更

## 边界

- 只新建 manifest.yaml + 修 2 处 name；不碰 SKILL.md 正文与 frontmatter
- 不动挂载面（建议书动作4/5/6 缓议，等编排层解冻）
- 开工前置：#595 终审收口（防扫描器并发写）

## 关联

- 来源：60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md（文末编排裁定节）
- 前序：#588（扫描器）/#594（research-core 整合）/#595（frontmatter 补齐）
- 终审：欧阳锋
""")

wf('60_feedback/tasks/task_20260901_laowantong-chaishu218-unique-cards.md',
   [("id", "'597'"), ("title", "拆书会218期《因为独特》泡泡玛特产卡（老顽童）"), ("type", "card-production"), ("status", "queued"), ("priority", "P2"), ("assignee", "laowantong"), ("created_by", "王语嫣"), ("created_at", "2026-09-01"), ("source_refs", "\n- 00_inbox/泡泡玛特的拆解/拆书会第218期《因为独特》· 精华提炼.md"), ("instance", "laowantong"), ("updated_at", "'2026-09-01T23:35:00+08:00'")],
"""# #597 拆书会218《因为独特》产卡（inbox 自动化流水线，0831/0901 老朱直令）

## 背景

00_inbox 新素材（watch_inbox 09-01 15:11 登记）：拆书会第218期精华提炼（10.7KB）——李翔《因为独特》泡泡玛特创始人王宁访谈，主线=「尊重时间、尊重经营」的长期主义样本。王语嫣 2026-09-01 23:35 入口诊断：拆书会系列 90+ 卡先例、结构与金句密度高，与库内 case-popmart-prospectus-pricing（招股书定价视角）/ tool-blind-box-mechanism（盲盒机制视角）互补不撞车 → 按自动化流水线立项产卡。

## 任务

产 2-3 卡（候选方向，生产者按素材判准增删）：
1. **case 卡**：泡泡玛特王宁长期主义经营案例（被投资圈忽视→Sonny Angel 代理困局转型→砍品类聚焦潮玩→千亿市值；「尊重时间尊重经营」主线）
2. **概念/方法卡候选**：「消费=满足感+存在感」两件事框架（含「就算消费降级，审美与情感需求也不降级」之辩）
3. **概念/方法卡候选**：「品牌=感官包裹感」（盖住 logo 也认得/门店如教堂/唱片公司模式）或「减法护城河」（拒绝诱惑+七分饱+减宽加深）

## 验证

- 卡内关键数字（融资额/营收/上市时点）标 source 指向素材原文；外部可证数据（上市日期/市值）建议补外部锚
- 域归属建议 strategy（主）；与既有 popmart 两卡互链
- pre-submit + 执行报告五字段 + queue_transition 提审

## 边界

- 素材原文不动（00_inbox 只增不删铁律）
- 不搬运「本周作业」教学层内容
- 终审：欧阳锋
""")

# ---------- 4. todos append ----------
tp = '90_control/todos/wangyuyan.md'
traw = open(tp, 'rb').read()
t_eol = '\r\n' if b'\r\n' in traw else '\n'
entries = [
 '[' + NOW + '] ⚖️ 裁定 建议书_20260901_skill健康度勘察与检测方法论：部分采纳——动作1+2 立项 #596（72 manifest 补建+2 name 修复，skills-assistant，待 #595 收口开工）；动作4/5/6 缓议一拍（挂载面刚经 #594/#595 两连改）；动作3/9 并黄药师欠账候选；动作7/8 随 #596 二期；建议书 frontmatter 已对齐 orchestrated+裁定节落档',
 '[' + NOW + '] 📥 inbox 素材入口诊断+立项：泡泡玛特的拆解/拆书会第218期《因为独特》精华提炼——strategy/商业案例（王宁长期主义经营哲学），与库内 popmart 定价卡/盲盒机制卡互补不撞车，按 0831/0901 流水线立项 #597 产卡 2-3 张（老顽童），终审归欧阳锋',
 '[' + NOW + '] 🕐 时钟值守拍（23:35）：①PROPOSAL-PENDING 划销 3 行（role-liveness 冷却重报实测全死0/#594 F-035 已化解双审闭环/健康度建议书部分采纳立项 #596）；②INBOX-PENDING 消费 1 行（拆书会218→#597 立项）；③产线：#595 pending_review 已拉欧阳锋终审、#597 queued 已拉老顽童施工、#596 queued 待 #595 收口下拍拉 skills-assistant（防扫描器并发写）；④结构地图例行 grep 8 命中=历史残留（新增命中 #594 已终审闭环不涉裁定）；⑤心跳已写',
 '[' + NOW + '] 🚀 已拉起 ouyangfeng：#595 终审（pending_review>0 v4.2 直令）；🚀 已拉起 laowantong：#597 施工（headless 后台）',
]
with open(tp, 'ab') as f:
    f.write((t_eol + t_eol.join(entries) + t_eol).encode('utf-8'))
print('todos appended, eol=%r' % t_eol)
print('ALL DONE')
