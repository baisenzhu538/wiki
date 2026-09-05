---
id: task_20260906_huangyaoshi-transcribe-timeout-and-aliases
title: "采集链两修：①wechat 转写 15min 超时死循环根治（148MB 视频每拍重下实证）②pre-submit ALIASES checker 取 basename"
seq: 649
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 王语嫣值守拍立项（老朱 09-06 链接卡转写死循环 + 老顽童 #643 friction）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T02:50:00+08:00'
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
