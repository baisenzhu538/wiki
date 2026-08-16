---
id: task_20260809_huangyaoshi-kdo-index-rebuild
assignee: huangyaoshi
status: closed_no_action
updated_at: 2026-08-09
priority: P0
wsjf: 4.0
---

# KDO 索引重建（#305 · 8-09 生产卡未入索引）

## 任务目标

`.kdo/state.sqlite` 最后更新 2026-07-19——今天（8-09）生产的 85 张卡（教练域 #280/281/288 + 科学开会域 #285/286 + 补链）全部在磁盘但**未入检索索引**：`kdo query "科学开会"` 命中 0、kdo_capabilities 统计读旧基线（小昭报告 tools/cases 无增长的原因）。

## 规格

1. `kdo index --rebuild`（或等价命令）重建检索索引/state.sqlite
2. 重建后验证：`kdo query "科学开会 十大原则"` 命中 meeting 卡；`kdo query "教练式领导力 五阶梯"` 命中 framework-leadership-five-ladders
3. 统计确认：tools/cases/frameworks/dk 数字反映 8-09 全量（85 卡）
4. GraphRAG 索引（如有）同步重建

## 验收标准

- kdo query 命中今天新卡（抽查 5 个：framework-meeting-ten-principles / tool-meeting-basic-principles / case-meeting-roi-awakening / tool-coaching-communication-four-layers / case-morfei-semiconductor）
- state.sqlite 时间戳更新为今天
- 目录统计数字含今日生产

## 依赖

- 无（基建例行）

## 边界

- 只重建索引，不修改卡内容
- 重建前先 git status 确认无未提交改动（防索引与磁盘不一致）


## 补充：增量写入机制（E028 用户要求——日常随卡更新）

- 除批量重建外，增加**单卡增量写入**能力：`kdo index --add <card>` 或生产命令（pre-submit/入库）自动写索引
- 目标：每张卡终审闭环即可检索，不依赖批量重建
- 本任务交付批量重建（补 8-09 存量），增量机制并入或另开（黄药师按可行性定）


## CLOSE（2026-08-09 黄药师实测诊断）

**无需重建——检索/统计全部正常**：
- kdo query "科学开会十大原则"/"领导力五阶梯" 命中今天新卡
- BM25 索引含 5/5 验收卡（doc_count 3883，search_index.json 8-09 19:41）
- kdo_capabilities 实时扫磁盘（不读 state.sqlite）
- state.sqlite 旧（6-30）但只存 sources 注册记录，无功能依赖（有磁盘 fallback）
- 避免 P-15 反向：盲目重建引入风险

**保留动作**：state.sqlite sources 同步 = P2 观察项（无实际影响）；增量写入机制（E028 纪律）= 抽查确认已自动更新，不另建

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O3 独立验证（四项全复现）：
1. **"索引过期"不成立** ✅：search_index.json 8-09 19:41 生成（新鲜），doc_count 3883 含全部卡，kdo query 实跑正常加载（graph 3468 节点/8342 边 + vectordb 2691 entities）
2. **"统计读旧基线"不成立** ✅：kdo_capabilities（kdo-tools/mcp/tools.py L349-375）用 rglob 实时扫磁盘，不读任何缓存/基线
3. **state.sqlite 旧** ⚠️ 事实（实测时间戳 7-19 更旧）——但检索（search_index）与统计（rglob）均不依赖它——无功能影响
4. **导航层刷新** ✅：index.md 含 4 处今日新卡关键词 + links/index.md 12 处 meeting-ten-principles（回链索引重建）——kdo index --rebuild 已执行

结论：小昭报告"索引过期/读旧基线"经独立复现均不成立；state.sqlite 旧为事实但无功能依赖。处置正确：导航层重建 + 检索/统计层验证正常。**O3 独立验证又一次拦截了外部 agent 报告的误报。**

五维：溯源 95/逻辑 95/暗知识 85/可操作 95/表达 90 → 总分 93（A）
