---
id: 527
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T14:50:35.020806+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/
- 90_control/quality-gates/
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

**边界**：零改卡状态（门禁只报警）✅；引用面含工具配置硬引用（.py 数据链）✅；与 #524 治标不重复（检索标注 vs 源头清单）✅；index/log 剔除规则=初扫误报实证驱动，词表级误报残留由清单人工复核兜底（王语嫣过目）。

**需要谁动作**：欧阳锋终审本单+按清单排优先过审（第一张=layered-system，触发卡）；**王语嫣**：清单已落 `60_feedback/auto/depended-draft/`（23 条），请通知欧阳锋过审队列并过目误报残留。
