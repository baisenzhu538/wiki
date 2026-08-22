---
id: 408
assignee: hermes
status: reviewed
updated_at: '2026-08-22T03:29:54.710175+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-22'
grade: A-
---
# #408 两张空壳 skill 案例卡补强修复（src_unknown 清零 + 8-15 口述新细节回填）

- **任务号**：#408
- **状态**：queued
- **assignee**：laowantong
- **优先级**：P2
- **立项**：2026-08-22 王语嫣（老朱 08-21 深夜拍板"补强修复入列"）
- **来源**：老朱探针"两个 agent 分工做写 skills 的 agent 流程能不能做案例卡"——核查发现库内已有两张同主题卡但 src_unknown 空洞遍地（6-14 建卡至今未回填），"知而不行"活化石

## 目标卡（2 张，均 cases/）

1. `30_wiki/cases/case-truman-ai-skill-engineering-guide.md`（3 小时高阶 Skill 工程指南）——Background/What Happened 六阶段细节/关键成功因子/关键证据/Checklist 细节/教训 全部 src_unknown
2. `30_wiki/cases/case-truman-ai-skill-self-packaging.md`（AI 自复盘自封装 design case）——Step 3 合并同类项/落地模板/互链/关键证据/教训 全部 src_unknown

## 一等素材（两份口述，逐字读相关段落，W1）

- `10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md`（两卡原 source_refs，回填骨架细节的主依据）
- `00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt` **L994-1066**（8-15 新细节，本次补强增量）：
  - 双窗口流水线：左 Claude 右 Obsidian，"一个负责下载，一个负责翻译，一个负责解读"，官方标杆 skill 交叉比对（L1014-1022）
  - 自评起点"真实评分 74"+ 读标杆 21-29 号（L1028）
  - "换最好的那个模型，用了最贵的模型，因为这工作最重要"（L1024-1026）
  - 十几轮纠偏原话："优先级不对给我改/没有 SBC 给我改/不完备给我改"（L1036-1038）
  - 独立打分 agent：官方教程+拆推评算基本功贴入知识库，新窗口 agent 交叉打分 → 体检报告 → "虽然分没咱高但也有优点，再吸收一轮"（L1044-1054）
  - 封装成 YI partner"skill 创业专家"→ 复用产"调研专家"skill（吸收知识库调研方法论）（L1056-1066）
  - 保存链路：YAI 笔记 → Cubox → Obsidian，"全程盯着目录做"（L1068-1070）

## 动作清单

1. 逐字读两份口述相关段落，把两张卡所有 `src_unknown` 占位回填为真实内容（每个空洞至少一条有行号的口述证据）
2. 8-15 新细节补强进 `case-truman-ai-skill-engineering-guide`（双窗口流水线/74 分起点/最贵模型/打分 agent 体检报告/再吸收一轮）；YI partner 复用链补强进 `case-truman-ai-skill-self-packaging`（自封装→复用的闭环证据）
3. frontmatter 修复：`domain: src-unknown` → 正确域（ai-collaboration 等）；tags 清 src_unknown；`source_refs` 加 8-15 口述；trust/confidence 按一等证据补足情况重评并注明理由
4. 两张卡正文开头补定位声明（#199 门禁规则）
5. related 双向回链检查（只增不改，#384/E017 模式）：两卡之间互链 + `dk-three-context-formula`/`tool-skill-packaging-eight-steps` 已有关联核实
6. `kdo pre-submit` 两卡 0 ERROR 附输出；完成后走 queue_transition 提审 + commit 入档

## 验收标准

- 两张卡 `src_unknown` 清零（可用 #399 全库复扫工具验证）
- 每个回填段带口述行号；8-15 增量细节全部入卡
- 两卡分工不动（engineering-guide=指南生产过程 / self-packaging=自封装流程），不合并不新建
- 欧阳锋终审：重点抽"回填内容是否真的出自口述原文"（防脑补，E039）

## 边界

- 只回填+补强，不改两卡的框架结构和既有结论
- 不动其他 src_unknown 卡（全库空壳卡治理是另一个议题，已随洞察挂停车场，明天并案）

## 终审记录（2026-08-22 欧阳锋 · PASS A-）

**O0 溯源核验**（防脑补 E039，逐条对源）：
- **8-15 增量（楚门口述 L1016-1072）全部逐字吻合**：双窗口流水线（L1016-1022）/ 真实评分 74+读 21-29（L1028）/ 换最贵模型（L1024-1026）/ 十几轮纠偏原话"优先级不对给我改、没有 SBC 给我改、不完备给我改"（L1038）/ 打分 agent 体检报告+再吸收一轮（L1044-1054）/ YI partner"skill 创业专家"复用产调研专家（L1056-1066）/ 保存链路 YAI→Cubox→Obsidian（L1068-1072）——引文与源逐字一致，无脑补
- **原口述核心数字实锤**：官方 B+/花总 A/自评 S（L2546-2550）/ 3 小时显著超过（L2552）/ 七条改十条（L2504）/ "我也拿不准"（L2536）/ 出现一次喷一次（L1218）
- src_unknown 两卡清零（grep 0）+ pre-submit PASS 0 issues（两卡 80/100）+ 定位声明 ✅ + 双向回链（两卡互链 + tool-skill-packaging-eight-steps + dk-three-context-formula 均回链）✅ + domain/tags/source_refs 修复 ✅ + reviewed_by: pending 合规 ✅

**遗留 TODO（小瑕疵，不阻断）**：
1. 卡 1 阶段 4 引用"让他 MECE"（L2482-2484）——源口述中 MECE 被 ASR 转写为"MISS/MIC/MC1"，卡还原为 MECE 未标注 ASR 还原（#379 加分纪律）；建议下批顺手补"（ASR 还原）"标注
2. 卡 2 触发条件"高频重复任务"（L1204-1206）为对源"两周前做好多的图"的合理抽象，可接受；如需严格可改"两周密集协作"
