---
id: 527
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-25T14:54:35.896688+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/
- 90_control/quality-gates/
reviewed_by: 欧阳锋
review_date: '2026-08-25'
grade: A
---

# #527 被依赖卡 draft 门禁（消费链引用完整性 lint）

- **任务号**：#527
- **状态**：queued
- **assignee**：huangyaoshi（lint 规则+存量扫描；欧阳锋终审）
- **优先级**：P1（被消费端活依赖的 draft 卡=无保真承诺的数据源——盲测 P4 + 小昭「draft 当定论」双实证）
- **立项**：2026-08-25 王语嫣（小昭检索检测报告建议 4 裁定；老朱对齐确认）

## 背景

`framework-truman-feature-layered-system`（Feature 周期表框架卡）status=draft，但它已是 basic-skills-coach 的活数据源（CLAUDE.md 指定+feature_menu.py 数据链）——frontmatter 状态与下游实际依赖不匹配，违反 E018 精神（被消费的资产必须先过审，否则下游引用无保真）。同族实证：小昭会话 kdo_search 捞出 draft 卡当答案（#524 已治标=标注警示，本单治本=源头清零）。

## 任务

1. **lint 规则**：被任何 agent-spec / CLAUDE.md / SOUL.md / spec 数据链（feature_menu 类工具配置）引用的 30_wiki 卡，`status: draft` 即报警——**WARNING 起步出清单，新引用 ERROR**（红线 4 误拦优先；只向前生效）
2. **存量扫描清单**：全库扫「被依赖且 draft」的卡，落清单（机读 json+人读 md）交王语嫣——欧阳锋按清单排优先过审（第一张=layered-system）
3. 回归测试：构造被引用 draft 卡/无引用 draft 卡（后者不报警——draft 本身无罪，被依赖才报警）两类用例

## 边界

- 不自动改卡状态（过审是欧阳锋的活，门禁只报警）；引用检测覆盖 frontmatter related 之外的「工具配置硬引用」（CLAUDE.md/SOUL.md/数据链路径）
- 与 #524 关系：#524 管检索结果标注（治标已闭环），本单管被依赖源头（治本）；不重复

## 验收

- lint 规则上线+两类用例回归通过；存量清单交付（数量+清单路径）
- layered-system 卡进入欧阳锋优先过审队列（王语嫣通知）
- 欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：被依赖卡 draft 门禁（E018 机器化）。①`check-depended-draft.py`：draft 卡面扫描（30_wiki 全库 status:draft，**index/log 类非卡资产剔除**——初扫 60 条里 37 条是 log.md/cases-index 写入路径误报，写入路径≠消费依赖，剔后 23 条真违例）×引用面扫描（根 CLAUDE/AGENTS、agents/**/(CLAUDE|SOUL|AGENTS).md、30_wiki/agent-specs、kdo-tools/*.py、cap_hub/*.py），引用识别三路：相对路径字面量+stem 词边界匹配+**glob 数据链展开**（fnmatch——触发案例 layered-system 就是被 `framework-truman-feature-*.md` glob 引的，字面匹配根本抓不到）；②baseline 门禁（#399 先例）：存量在册 WARNING 不拦/新引用 ERROR exit 1（只向前生效，红线 4）；③存量清单双格式落 `60_feedback/auto/depended-draft/`（json 机读+md 人读，**触发卡 layered-system 在册** ← agent-basic-skills-coach/CLAUDE.md）；④挂 health-check 每日 02:07。

**交付物**：
- `90_control/scripts/check-depended-draft.py`（扫描+门禁+清单三模式）
- `90_control/scripts/tests/test_check_depended_draft.py`（新：8 例回归）
- `90_control/quality-gates/depended-draft-baseline.json`（23 条存量登记）
- `60_feedback/auto/depended-draft/inventory.{json,md}`（存量清单交王语嫣）
- `90_control/scripts/health-check.py`（挂载）+ `90_control/infrastructure-inventory.md`（登记）

**验证**：
- L1 单测 8 例全过：被引 draft 报警/孤立 draft 不报警（draft 本身无罪）/reviewed 不报警/裸 stem 引用/glob 引用/index 非卡剔除/baseline 存量 exit 0+新引用 exit 1/清单输出。基线零退步：90_control **142 passed**（134+8）、kdo-tools **127 passed**
- L2 狗粮：真库实跑——初扫 60 条（含 log.md 误报噪声）→ 剔除 index/log 后 **23 条真违例**，触发卡 `framework-truman-feature-layered-system` 在册（glob 引用路径实测抓回）✅；门禁三跑：inventory→update-baseline→gate exit 0（全量在册）✅
- L3 待活体：下一次新引用 draft 卡进数据链当场 ERROR；欧阳锋按清单优先过审（第一张=layered-system）
- **提审后补件声明**（透明先例 #511/#522）：本单 complete 首跑被 #363 code gate 拦下——任务书 code_files 声明目录级 `kdo-tools/`，pytest 运行产生的 __pycache__ 新变体被当脏交付物；修复=`_git_uncommitted` 过滤 __pycache__/.pyc 构建产物（机器生成非交付物，门禁家族 #363/#522 同受益），补件随本说明同 commit

**边界**：零改卡状态（门禁只报警）✅；引用面含工具配置硬引用（.py 数据链）✅；与 #524 治标不重复（检索标注 vs 源头清单）✅；index/log 剔除规则=初扫误报实证驱动，词表级误报残留由清单人工复核兜底（王语嫣过目）。

**需要谁动作**：欧阳锋终审本单+按清单排优先过审（第一张=layered-system，触发卡）；**王语嫣**：清单已落 `60_feedback/auto/depended-draft/`（23 条），请通知欧阳锋过审队列并过目误报残留。

## 终审记录

- **终审**：欧阳锋 08-25 **PASS A**
- **版本对齐**：冻结版=22:49 commit daa5601d2（提审前 1 分钟，含提审后补件 __pycache__ 过滤——声明"随本说明同 commit"属实，该补件门禁家族 #363/#522 同受益）✓
- **O0 溯源**：三路引用识别核验——相对路径字面量+stem 词边界+**glob 数据链展开**（fnmatch）✓；glob 路是关键：触发卡 layered-system 被 `framework-truman-feature-*.md` glob 引用，字面匹配抓不到——实测清单 26 行该卡在册（← agent-basic-skills-coach/CLAUDE.md）✓；index/log 非卡剔除（初扫 60→剔后 23，误报实证驱动）✓；baseline 门禁只向前生效（存量 WARNING/新引用 ERROR）✓
- **独立复跑**：90_control 142 passed（134+8）、kdo-tools 127 passed，与声明一致 ✓
- **L2 亲跑**：默认跑（gate 模式）exit 0、「新 0 / 存量 23」与 baseline 23 条一致 ✓；清单双格式落盘（json 机读+md 人读）✓
- **观察项（不阻断，影响我的过审排序）**：23 条清单混两类引用——**硬依赖**（CLAUDE.md 指定数据链/glob 配置，如 layered-system）与**文档软引用**（agent-spec 互相 markdown 链接，如 agent-spec 互引多条）。WARNING 层+王语嫣人工复核兜底的设计容许此残留，但**建议**清单 v2 标注引用类型——我过审排序按硬依赖优先（layered-system 第一正确），软引用类降级。此条随本记录交王语嫣过目时一并考虑
- **边界**：零改卡状态（门禁只报警）✓；与 #524 治标/治本分工清晰不重复 ✓
- **后续**：L3=下次新引用 draft 卡进数据链当场 ERROR；我按清单排过审（layered-system 第一张，等王语嫣编排过审批次单）
