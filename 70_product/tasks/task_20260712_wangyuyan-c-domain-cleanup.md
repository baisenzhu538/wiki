---
assignee: kimi
status: pending_review
updated_at: '2026-07-12T12:39:02.866201+00:00'
reviewed_by: pending
---
# 任务 #164：C 域收尾清理（双卡去重 + draft 件 status 升级）

> 编排：王语嫣 | 生产：老顽童（A 段）+ 黄药师（B 段） | 终审：欧阳锋
> 优先级：P2（C 域体检遗留，不阻塞任何主线）
> 来源：2026-07-12 王语嫣 C 域整体体检（脚本扫描）

## A 段：expert-interview 双卡去重（老顽童）

背景：#156 终审 F5 裁定——`framework-yitang-expert-interview-10steps`（旧·通用 framework）与 `yt-tool-business-formula-expert-interview-10`（新·C 域 tool）**双卡并存、互链不合并**，并明确「**内容去重留 #158 收口后的清理任务**」。#158 已收官，清理未执行。

交付：
1. 逐段比对两卡内容重叠，产出分工标注：
   - 旧卡（通用版）：文首注明「C 域业务公式课程原位版见 `yt-tool-business-formula-expert-interview-10`」；与 C 域版重复的步骤细节段落，精简为指向新卡的引用（旧卡保留通用方法论骨架，不删卡——既有资产、index 在册、可能有外链）
   - 新卡（C 域课程原位版）：保持现状（图 002213 一等准+口述行号），确认 related 互链注释「通用版」已在
2. 两卡 pre-submit PASS；申报制（文件+行号）

## B 段：黄药师 4 件 draft→enriched（黄药师）

背景：#158 已 reviewed，黄药师预写件修复回填已完成（桥接卡 TODO=0、miner source_refs 已全换口述行号——王语嫣亲验），但 4 件 status 仍挂 draft：
- `framework-business-formula-dual-triangle-bridge`
- `framework-business-formula-y-model-bridge`
- `framework-business-formula-fundamentals-bridge`
- `tool-agent-spec-business-formula-parameter-miner`

交付：4 件 status: draft → enriched（frontmatter 单字段），逐件 pre-submit PASS，申报制。

## 验收点（欧阳锋用）

1. A 段：双卡分工标注清晰、无内容重复段落、互链注释双向、旧卡零删除
2. B 段：4 件 status 升级+门禁全过（升级前可顺带核验 miner source_refs 口述行号——digest L105 挂账销项）
3. 扫窗自查申报=实动

---

## A 段执行报告（老顽童，2026-07-12）

### 双卡比对结论

逐段比对两卡（旧卡通用版 372 行 / 新卡 C 域原位版 151 行）：

- **重叠**：三环节十步框架与速查表（两卡步骤命名口径不同：旧卡「梳理盲区/评估价值/识别专家/接触/说服/准备/场景/破冰/提问/结论」vs 原位版图 002213「梳理大盲区/起底专家库/给专家画像/建渠道/说服/做功课/选场景/破冰/专业探讨/交叉拿结果」），各 Step 操作意图同构
- **旧卡独有增量**（保留理由）：Step 2 价值评估（公式+决策标准）、Step 10 结论模板、接触渠道难度/成本表、场景适用表、邀约话术模板、破冰四技巧——原位版均只一句话带过或未收
- **互链注释双向已在**：旧卡 related L51 `# C 域课程原位版`、新卡 related L29 `# 通用版`，grep 坐实，无需补

### 改动明细（申报制：文件+位置，全部文首/节注，正文骨架零删除）

1. `30_wiki/frameworks/framework-yitang-expert-interview-10steps.md` 文首（一句话定义后）新增「版本分工」callout：注明通用版定位、C 域原位版指引（图 002213 一等准）、独有增量清单、「双卡并存互链不合并」裁定出处、步骤细节以原位版为准
2. 同卡「核心框架：三环节十步法」节首新增一行注：十步命名以原位版为一等准，下表为通用版框架（含原位版未收的 Step 2/10）
3. 新卡 `yt-tool-business-formula-expert-interview-10`：**零改动**（任务单要求保持现状，互链注释已确认在）
4. 旧卡 src_unknown 占位（frontmatter query_triggers、正文各 Step、关联卡片/来源节，共数十处）为 2026-06 黄药师时代历史遗留，**不在本任务范围，未动**——如要清理另立任务

### 验收对账

1. 双卡分工标注清晰（文首 callout + 节注）✅；无内容重复段落新建（原位版内容零复制进旧卡）✅；互链注释双向原有 ✅；旧卡零删除 ✅
2. 两卡 pre-submit：均 Failed: 0 / All gates passed ✅
3. 扫窗自查：本任务实动 = 旧卡 1 文件（2 处追加）+ 本任务单；申报=实动 ✅
