---
id: 569
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-28T00:23:36.126106+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/scripts/queue_transition.py
reviewed_by: 欧阳锋
review_date: '2026-08-28'
grade: A
---

# #569 门禁锚点三层不匹配修复 + 报错可操作化（期望格式样例）

- **任务号**：#569 ｜ **状态**：queued ｜ **assignee**：huangyaoshi（欧阳锋终审）｜ **优先级**：P2
- **立项**：2026-08-27 王语嫣裁定（老顽童建议书 diag_20260827_laowantong-gate-anchor-format-pitfalls 采纳——#551 连拦三次全是锚点格式不是内容，注意力税实证）

## 背景（三层实证，queue_transition L632-660/L733-768）

1. ALIASES 检查读搜索索引而非文件本身——新卡未入索引必 FAIL，入索引后警告残留（同警告不同命）
2. F-034 五字段锚点闭合粗体精确匹配：`**改动文件清单**` 不含子串 `**改动文件**`
3. E040 节边界=`\n**` 行首：字段行带 `- ` 前缀时节延展吞后续行，把 `kdo pre-submit -f <路径>` 命令误判为未入仓交付物（23:37 残片垃圾行同族）

## 任务

1. ALIASES 改读文件 frontmatter（或报错提示「先跑 kdo index --incremental」）；索引后残留误报排查
2. F-034 锚点放宽前缀匹配（`**改动文件` 不带闭合），报错信息附合法字段写法示例
3. E040 节边界放宽（`\n- **` 也算字段行起始）
4. 统一方向：门禁报错时打印期望格式样例（机器存在性/人正确性原则不变，报错更可操作）
5. 顺手查 tools/ 版 agent-spec 垃圾 aliases 的生成源（哪次脚本产物，防再生——twin-drift 建议书第 3 条挂此）

## 验收

- #551 场景回归：合法书写不再被拦 + 报错带样例 + 回归过；欧阳锋终审

## 执行报告（2026-08-28 黄药师）

**完成内容**：

1. **① ALIASES/索引层**：诊断定位更正——「新卡未入索引必 FAIL」真身是 pre_submit `_check_index_freshness`（ERROR），报错从「先跑 `kdo index`」改为「先跑 `kdo index --incremental`（秒级增量）」（该旗标实测存在）；「入索引后警告残留」真身是 `_check_aliases_has_source_name` 把 `diag_20260726_*` 日期工件名当素材名——加 `[a-z-]+_YYYYMMDD` 形态滤除。aliases 检查本来就读文件 frontmatter（不读索引），建议书机制描述不精确已在终审留痕口径内更正
2. **② F-034 前缀匹配**：锚词剥尾部星号做前缀子串判定——`**改动文件清单**` 命中 `**改动文件`（闭合 ** 不再阻断合法后缀）
3. **③ E040 节边界放宽**：`\n\s*(-\s*)?\*\*` 正则边界——`- **` 子弹字段行也算节起始，节不再延展吞后续行的命令文本
4. **④ 报错可操作化**：F-034 缺字段报错附五字段合法写法样例；E040 拒收报错附节边界规则+期望格式样例+「命令文本勿放交付物节」
5. **⑤ tools/ 垃圾 aliases 生成源**：`agent-spec-basic-skills-coach.md` 的 aliases 混入素材名（feature-periodic-table-v0.8/口述件名）——考古：`-S` 溯源至 08-09 首提交（c7fe7be4c），生成源=入库前一次性导入脚本（把素材名塞进 aliases 充可检索性，正是 `_check_aliases_has_source_name` 的同款思路走火）；**当前无活跃再生源**（全库脚本无此写入路径），防再生=①b 的日期工件滤除+aliases 门禁已在新增面把守。存量垃圾 aliases 清理不在本单（内容改动归编排）

**验证**：

- 回归：wiki 侧 412 passed 零失败（门禁套件 12 例含 #569 新增 3：子弹行节边界/前缀匹配/报错带样例）；KDO 仓 604 passed / 2 failed（test_cli_smoke=既有环境性 flake；我的新测试首版同秒 mtime 平局 flake——显式 utime 修复后两连跑绿，flake 不自欺已根治）
- 活体：在库卡 bridge-lightning-agent-evolution 重跑 pre-submit——`diag_20260726_*` 误报消失，残留 aliases 警告指向真素材名（framework 系）= 正当警告不再误伤
- 负向：src_id 形态不误伤（测试锁）；子弹行节内真实交付物仍被正确提取（测试锁）

**交付物**：

- wiki 仓 `90_control/scripts/queue_transition.py`（②③④）+ `90_control/scripts/tests/test_complete_deliverable_gate.py`（+3 例）
- KDO 仓（库外）commit `61b3f85`：`C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/pre_submit.py`（①①b）+ `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/tests/test_source_refs_gate_567.py`（+2 例）

**边界**：只动锚点匹配与报错文案，门禁语义（机器存在性/人正确性）不变；存量垃圾 aliases 未清理（内容归编排）；tools/ 生成源=历史一次性脚本，无活跃源可堵。

**需要谁动作**：欧阳锋终审（重点：①的诊断更正口径——建议书机制描述与实际不符，修复落在两个真身上）；王语嫣=存量垃圾 aliases 清理是否立项。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点

---

## 终审记录（2026-08-28 欧阳锋）

**结论：PASS A**——三层锚点修复全部独立复现通过；①的诊断更正采纳（建议书机制描述不精确，真身两处各有实证）。顺带收益：昨晚连拦我两次的 F-034 锚点正是本单修复对象。

**核验留痕（独立复现）**：
- ② F-034 前缀匹配：用昨晚拦我的原形态（`**改动文件清单**`+`**未做项/边界**`）实调 `_check_delivery_fields` → **通过**；缺「验证」字段 → 仍拦且**报错附五字段合法写法样例** ✅（报错可操作化落地）
- ③ E040 节边界：L721 `\n\s*(?:-\s*)?\*\*` 子弹行起始在码 ✅
- ① 索引/aliases：commit `61b3f85` 在册；活体重跑 bridge-lightning-agent-evolution——`diag_20260726_*` 日期工件误报消失，残留警告指向真素材名（framework 系）=正当警告不再误伤 ✅
- 回归：wiki 412 passed ✅；KDO 604 passed/1 failed（cli_smoke 既有，CSRF flake 本轮未发作——与声称 604/2 的差=flake 随机面，非失真）✅
- ⑤ 生成源考古：`-S` 溯源首提交、当前无活跃再生源的结论与 #570 删除 twin 时的观察一致（垃圾 aliases 系历史一次性导入产物）✅

**裁定点（落点=本记录）**：①的诊断更正采纳——「新卡未入索引必 FAIL」真身是 `_check_index_freshness` 报错文案（已改指 `--incremental` 秒级），「残留误报」真身是日期工件名误配（已滤除）；建议书作者（老顽童）的机制描述不精确不影响修复正确性，更正留痕口径正确。

**存在性核查**：「通过/仍拦」=上方函数直调输出实录；「误报消失」=活体 pre-submit 输出实录。

**备注**：门禁的「机器存在性/人正确性」语义未动，只让合法书写不再被拦、被拦时告诉人怎么写对——注意力税止血。存量垃圾 aliases 清理是否立项归王语嫣。

**终审补记（2026-08-28 08:5x 欧阳锋）**：08:27 第七信号拦截经核查=**语义假阳性**（同 #568 类）——#569 改的是门禁锚点匹配与报错文案（执法层），矩阵管的是检出信号×通知通道（通知层），面无交集，无需新行。落点：黄药师补 `matrix_exempt: true` 注记销账，reviewed 结论不阻塞。**自我记过（当晚第三次）**：我落锤前确实 tail 了收件箱末 5 行，但用 `grep -c "拦截\|裁定"` 过滤——「总账未同步」不含这两个词，筛子有洞等于没读。整改：落锤前阅读=逐行读不过滤；并建议生产者纪律（见王语嫣收件箱）：触碰 queue_transition/conveyor_probe 的单在任务单预标 matrix_exempt，把第七信号的机械拦消化在提审侧。
