---
id: task_20260906_huangyaoshi-transcribe-timeout-and-aliases
title: "采集链两修：①wechat 转写 15min 超时死循环根治（148MB 视频每拍重下实证）②pre-submit ALIASES checker 取 basename"
seq: 649
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 王语嫣值守拍立项（老朱 09-06 链接卡转写死循环 + 老顽童 #643 friction）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T19:47:42.102342+00:00'
evidence: 60_feedback/tasks/task_20260906_huangyaoshi-transcribe-timeout-and-aliases.md
---

# #649 采集链两修（黄药师）

## 修一：wechat 转写超时死循环（P1，正在烧资源）

**实证**（03:07 值守拍定位）：
- `wechat_link_monitor.py` 转写步 `subprocess.run(..., timeout=900)`——15 分钟超时（L416/L512 两处）
- 老朱 09-06 深夜投放的启动会回放链接：视频 148MB（`60_feedback/wechat-collect/4b6327b374540e2e.mp4`），转写需时 >15min → 超时进程被杀 → 无产出未标 seen → 下一拍（10min）重新走全流程
- 循环实证：mp4 mtime 01:51 与 02:11 两次（重下）、transcribe 进程 01:51/02:11 两轮后消亡、`src_wechat_*.md` 无产出
- **每拍代价=148MB 下载+15min CPU，永不成功**

**修法**（三选一，取实现稳者）：
1. timeout 与视频体量挂钩（如 ≥60min 或按 MB 系数）
2. 转写异步任务化：落 pending 转写队列 + 完成回查，节拍只做提交与收割
3. 长视频自动降 tiny 模型（现 tiny 为默认？确认 DEFAULT_MODEL）+ 保底 timeout

**验收**：①该 148MB 视频完整转写产出 `src_wechat_4b6327b374540e2e.md` 且 seen 标注②模拟超时场景有明确失败留痕不再静默循环。
**注意**：修一施工前可先 `schtasks /change /tn wechat-link-monitor /disable` 止血（每拍 148MB 重下），**修完必须 /enable 恢复**——停用期间其他链接积压在微信 DB 不丢失。此步涉及停用常驻监控，执行时在执行报告显式声明起止时间。

## 修二：pre-submit ALIASES checker 取 basename（P2）

**实证**：老顽童 #643 收尾 friction（09-06 02:20 登记 PROPOSAL 段）——`kdo pre-submit` 的 ALIASES 检查对 `source_refs` 全路径多行段失效（checker 按 source name 比对，全路径取 basename 失败），误报要求补 aliases；老顽童已把有效 aliases 常驻表落 #643 执行报告。
**修法**：checker 从 source_refs 行提取时先取 basename 再比对 aliases。
**验收**：#643 执行报告中实证过的场景复跑不再误报；现有回归不红。

---

## 执行报告（#649，黄药师 2026-09-06）

**交付物**
- `kdo-tools/wechat_link_monitor.py`：转写步动态 timeout + 失败留痕 + 3 败熔断（`run_transcribe` 收敛两处 900s 调用点）+ 新增 `media_duration_seconds`/`transcribe_timeout`/`transcribe_fail_count`/`record_transcribe_fail`，`scan_downloaded_videos` 顺带统一走 `knowledge_ize`
- `kdo-tools/tests/test_wechat_link_monitor.py`：+6 回归用例（时长挂钩/体量兜底/超时留痕/失败留痕/3 败熔断/成功路径）
- KDO CLI 仓 `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/pre_submit.py` + `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/tests/test_source_refs_gate_567.py`：commit `4b0e45f`（ALIASES basename+剥扩展名，+5 回归）
- 补转写产出：`00_inbox/wechat-collect/src_wechat_4b6327b374540e2e.md`（116KB / 3218 行 / 3214 段）+ 知识化 `00_inbox/wechat-collect/knowledge/case-wechat-4b6327b374540e2e.md`；施工日志 `_tmp/transcribe-backfill-4b6327b374540e2e.log`
- seen 标注：`60_feedback/wechat-collect/seen_links.txt` 追加 `https://weixin.qq.com/sph/A86PKGRQTu` + 规范化键（管线自带 `mark_seen` 写入）

**完成内容**
- 修一：根因升级为双层——①固定 `timeout=900`（L416/L512）对 65min（3905s）视频必然超时杀进程；②超时抛 `TimeoutExpired` 未捕获→整拍崩溃，无产出未标 seen→10min 下一拍重下 148MB 重转写死循环（实证：mp4 mtime 01:51→02:11→…→02:51）。修法取任务三选一的选 1（timeout 挂媒体时长，ffprobe 精确取时长×1.0+300s，下限 900s 上限 4h；ffprobe 缺席按体量兜底 60s/MB）——选 2 异步任务化对本死循环过重，选 3 降 tiny 违反 #634 质量裁定（政策/课程类 tiny 乱码）不可选。另加失败留痕 ledger（`transcribe_fails.txt`：key|epoch|原因尾段）+同素材 3 败熔断，静默循环封死
- 修二：真根因两个——①全路径切段把目录段（`capabilities`/`shared`）当素材名；②扩展名未剥，`xxx.md` basename 永远匹配不上 alias 里的 `xxx`（#643 卡 alias 实存仍误报的直接证据）。修法=只取 basename+比对与报告统一剥扩展名（王语嫣裁定口径）；既有 #569 日期工件豁免保留
- 止血与恢复（显式声明）：`schtasks /change /tn wechat-link-monitor /disable` **02:54:17** 执行；02:51 在途拍（PID 167548/167804，注定 03:06 被超时杀）一并终止 **02:59:11**；修复+补转写完成后 `/enable` 恢复 **03:43:51**（State=Ready，NextRun 03:51:51）。停用期间链接积压在微信 DB 未丢，恢复后首拍按 seen 跳过
- 补转写：受控后台直跑 `transcribe_win.py`（默认 small 与管线口径一致），02:59:11 起 03:41 收工，实测耗时 2475s（RTF 0.63）——旧 900s 超时仅为实际所需 36%，死循环量级坐实；新动态 timeout=4205s（1.7x 余量）

**验证**
- `python -m pytest kdo-tools/tests/ -q`：**272 passed**（含新增 6 例）；KDO CLI 仓 `python -m pytest tests/ -q` 全绿（含新增 5 例）；`py_compile` 过
- 修二验收复跑：`kdo pre-submit --files 老顽童-20260905-qingdanti-skill-stress-test-report.md` → **ALIASES 0 issues / PASS**（修前同文件 1 warning：private-board-majingjing-qingdanti-note, capabilities, shared, SKILL, rubric）；同单笔记件复跑仍 PASS 无回归
- 模拟超时场景：回归用例 `test_run_transcribe_timeout_leaves_trace`（TimeoutExpired→ledger 落 `timeout <N>s killed` 行）/`test_run_transcribe_circuit_breaker_after_three_fails`（3 败后不再起子进程）——失败不再静默
- 转写产物抽验：首段 `[00:00] 妮妮妮 别吵架…`/尾段 `[65:02] 我们在一堂的课堂上不见不散`，头尾完整覆盖 65:05 全长；知识化 LLM 三层次成功产出
- seen 拦截验证：`A86PKGRQTu` 与 canonical 键均命中 seen 集合，03:51 首拍不会重下

**边界**
- 修一不含：转写质量模型升级（small→medium 属 #634 待办，本单沿用管线默认 small）；微信 DB 解密/下载链未动；`transcribe_fails.txt` 熔断后需人工核验清 ledger 才重试（有意设计，防无限烧）
- 修二已知取舍（用例钉死防无声回退）：目录段携带的素材名（如 `10_raw/sources/handle-the-business/`）不再入 aliases 比对（王语嫣裁定 basename 口径的直接后果，vault 内此类 ref 约 939 条）；basename 素材名照查（`test_aliases_check_directory_carried_names_out_of_scope` 双向钉死）
- 调度器 `MultipleInstances=IgnoreNew` 已核实（调度器不杀在途实例，900s 是唯一杀手）；若未来改 StopExisting，长转写仍会被下一拍截杀——本修不覆盖该场景（现配置下不触发）
- 计划任务停用窗内 02:51 拍的 promote 步（PID 168424）为活孤儿，未干预（避免打断库内写入），自行消亡
- 00_inbox 产物不进 git（gitignore 铁律），E040 走 _git_ignored 豁免分支

**需要谁动作**
- 欧阳锋：终审本单（代码 diff 2 仓 + 回归 + 复跑证据）
- 王语嫣：知会老朱——死循环已根治+148MB 视频完整稿已入库（启动会回放逐字稿可作素材消费）；`transcribe_fails.txt` 熔断语义（3 败停试、人工清账）如需改口径请立项

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/transcribe-backfill-4b6327b374540e2e.log`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `00_inbox/wechat-collect/knowledge/case-wechat-4b6327b374540e2e.md`
- 🔴 声称但未入仓（untracked）: `00_inbox/wechat-collect/src_wechat_4b6327b374540e2e.md`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（乱码）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
