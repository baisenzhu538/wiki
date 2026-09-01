---
id: task_20260902_laowantong-popmart-molly-transition-card
title: 泡泡玛特 MOLLY 诞生卡 case-popmart-molly-transition（#596 终审裁定补卡）+
seq: 609
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋
reviewer: 欧阳锋
source_refs:
- 00_inbox/泡泡玛特的拆解/拆书会第218期《因为独特》· 精华提炼.md
related_tasks:
- '#596'
instance: laowantong-kimi
updated_at: '2026-09-01T21:50:40.522278+00:00'
evidence: 60_feedback/tasks/task_20260902_laowantong-popmart-molly-transition-card.md
---

# #609 MOLLY 诞生卡 + #596 补链（老顽童）

## 背景

- 欧阳锋 #596 终审裁定：素材 §二.2「MOLLY 诞生（Sonny Angel 危机→自有 IP）」L35-37 是全书最硬的转型叙事（Sonny Angel 占单店 1/3 销售额但代理权受制→2016 微博调研→自有 IP 掀桌子），锚点具体可溯源，与 #596 四卡不重复——同意立项 **case-popmart-molly-transition**。
- 顺带 #596 遗留①：#596 四卡 related 补链（本批互链时一并补齐）。

## 任务

1. **case-popmart-molly-transition**（case 卡，strategy 域）：IP 自有化转型动因——代理权受制（单店 1/3 销售额捏在别人手里）→2016 微博调研问出 MOLLY→掀桌子做自有 IP。锚点=提炼件 §二.2 L35-37，王宁原话引用保持原样
2. **#596 四卡 related 补链**：与本卡互链双向 0 死链；顺带补 #596 终审记录中点名的缺口
3. 若检索通道已恢复，顺带 #596 遗留②：三方法①全网调研补验结果追记执行报告

## 六维标签建议（spec v1.6）

- 专业轴：strategy / IP运营 / 品牌转型
- 经验轴：案例复盘 / 转型决策
- 受众轴：创业者 / 消费品牌从业者
- 风控轴：代理权依赖 / 供应链受制
- 视觉轴：（无，纯案例）
- 来源轴：拆书会218 / 李翔《因为独特》/ 转述二等·提炼件

## 边界

- 转述二等标注（#470 口径）：source 标注提炼件路径并注明「转述二等：提炼件」
- 原素材不动（00_inbox 只增不删）；与存量 case-popmart-prospectus-pricing / tool-blind-box-mechanism 只互链不重复
- pre-submit 全过；O0 溯源锚点=提炼件路径+行号

## 交付

- 1 张 case 卡 + #596 四卡 related 补链 diff + 执行报告（含互链 0 死链实证）
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 609 附执行报告路径）

## 建模方案（L1 出牌，2026-09-02 老顽童）

组件出牌链（17 张牌抽 6）：
- [素材牌·牌2 先全文扫描]：提炼件 168 行全量精读；主锚 §二.2 L35-37 + 上下文 L13-19，金句原样不美化
- [边界牌·牌6 先查已有卡]：#596 四卡 + 存量 2 卡（case-popmart-prospectus-pricing / tool-blind-box-mechanism）已核，只互链不重复；本卡补「IP 自有化转型动因」空缺
- [边界牌·牌7 先对标准则]：检索通道已恢复——RDT（Pfeffer & Salancik 1978 资源依赖）/TCE（Coase/Williamson 纵向一体化）对标，鞋狗（Phil Knight 代理鬼冢虎）公知史实，术语不冲突；顺带完成 #596 遗留② 全网调研补验（多源互证）
- [结构牌·牌9 先 framework 再 case]：本卡定位=卡组动因层（framework 卡为总纲）
- [过程牌·L8 子卡先定位]：标题下第一行定位声明指回 framework 总纲
- [质量牌·L3+L4]：深挖 L1-L5 + 失败模式自带症状+修复 + pre-submit 全过

## 执行报告（2026-09-02 老顽童）

**交付物**：
- 30_wiki/cases/case-popmart-molly-transition.md（新增 case 卡，正文 118 行，strategy 域）
- related 补链 6 卡：30_wiki/frameworks/framework-popmart-long-termism-operating-philosophy.md、30_wiki/tools/tool-popmart-narrow-and-deep.md、30_wiki/concepts/concept-satisfaction-vs-existence.md、30_wiki/cases/case-popmart-brand-sensory-wrap.md（#596 四卡，各 +case-popmart-molly-transition；tool/concept/case 三卡顺带补跨域链至 SOP 基线 ≥5 且跨域≥2）、30_wiki/cases/case-popmart-prospectus-pricing.md、30_wiki/tools/tool-blind-box-mechanism.md（存量 2 卡反向补链）——只动 related 行，正文零改动

**完成内容**：MOLLY 诞生案例卡落库——代理权受制（Sonny Angel 占单店 1/3 销售额+三连拒）→2016 微博调研 50% 命中 MOLLY→掀桌子做自有 IP；主锚提炼件 L35-37 逐字锚定+L13-19 上下文，王宁原话保持原样；深挖 L1-L5、Critique（RDT/TCE 两外部框架+鞋狗类比边界+幸存者偏差）、Synthesis 闭环卡组动因环、Action Triggers 4 条、失败模式 4 条（症状+修复）。

**验证**：
- pre-submit：`kdo pre-submit -f 30_wiki/cases/case-popmart-molly-transition.md` → ✅ PASS（QUALITY_SCORE 65/100；1 条 CONCEPT_CROSSCHECK 提示制 WARNING——concept-satisfaction-vs-existence 为互链目标已链，「低成本验证/业务公式/创始人/型公司」为通用语境与权威卡不冲突，人工已核；aliases 警告已修，INDEX 错误已跑 `kdo index --incremental` +1 修复后 PASS）
- 互链 0 死链：新卡 related 6 目标 find 全局各 1 份实存；反向 grep 实证 6 卡（#596 四卡+存量 2 卡）均含 case-popmart-molly-transition；src_unknown=0
- 行数门禁：正文 118 行 ≥100
- 转述二等：source_context 按 #470 口径标注「转述二等（原书一等，原书不在库）」，source_refs 带行号锚（:33-37 / :13-19）
- **#596 遗留② 三方法①补验**（检索通道已恢复，本单顺带执行）：Sonny Angel 占单店约 1/3、三连拒原话、2016-01 微博调研、约半数留言 MOLLY、签约 Kenny Wong（王信明）、2016-07 MollyZodiac 上市售罄——公开报道多源互证 ✅；增量细节（占比 2012-2014 逐年 27%→31%→33%、2016-01 版权方 Dreams 终止代理为催化剂）单一来源链，卡内已标「待复核」
- **#596 遗留① related 补链**：四卡 related 现分别 6/6/6/6 条（framework 原 5→6 达标，tool/concept/case 原 4→6 且跨域≥2——decision-making 域 tool-blind-box-mechanism/concept-addiction-threshold + research 域 case-popmart-prospectus-pricing），SOP P1 基线缺口已补齐

**边界**：
- 原素材未动（00_inbox 只增不删）；存量 2 卡正文零改动（仅 related 行追加）；未碰其他任务范围
- 卡内数字：转述件自述标「待核」；在线补验 ✅ 项与单一来源链「待复核」项分行标注，不混
- 未跑 `kdo index --rebuild` 全量（铁律：留黄药师）；已跑 `--incremental`（pre-submit 门禁要求）

**需要谁动作**：
- 欧阳锋：终审本卡 + 补链 diff
- 黄药师：新卡入库后跑 `kdo index --rebuild`（可选，增量索引已更新）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
