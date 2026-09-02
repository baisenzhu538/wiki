---
id: task_20260902_huangyaoshi-toutiao-shortlink-regex-fix
title: 头条短链 is/XXX 形态正则漏配导致采集链断（老朱 09-02 20:09 链接卡死实证）——一行修复
seq: 621
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 晚问「链接为什么没走工作流」→ 王语嫣实测定位正则漏配（采集链断点，线上在流血）
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T15:28:49.792590+00:00'
evidence: 00_inbox/wechat-collect/src_wechat_article_tt_af50baaada5fc2f2.md
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A
---

# #621 头条短链正则修复（黄药师，急单）

## 背景（全链实测证据）

老朱 20:09 转头条链接到文件传输助手，链路卡死在 gid 提取：
- `wechat_link_monitor.py` L300 短链正则 `m\.toutiao\.com/is([A-Za-z0-9]+)` 不匹配今晚新形态 `m.toutiao.com/is/Lw4BUQtFZ9E/`（is 后带斜杠）→ 短链分支没进 → 对短链原样提 gid 失败 → 「无法提取 gid，下轮重试」每小时间性死循环
- curl 实测：302 展开正常（→ /article/7667212185281528364/），info 接口正常返回 data——**链路其他环节全好，就差这一行**

## 任务

`kdo-tools/wechat_link_monitor.py` L300 正则改 `m\.toutiao\.com/is/?([A-Za-z0-9]+)`（兼容 isXXX 与 is/XXX 两形态），并用老朱这条链接（https://m.toutiao.com/is/Lw4BUQtFZ9E/）实跑验证：提取 gid → info 取正文 → 落 inbox。

## 红线

- 一行修复不扩 scope；修完监控下一轮（整点）应自动捡起来——验证时如直接手工跑一轮成功则更佳
- 失败不记 seen 的设计保留（别顺手改成记 seen）

## 交付

- diff + 该链接端到端落 inbox 的实证 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 621）

## 执行报告（2026-09-02 23:20，huangyaoshi-kimi）

**交付物**：`kdo-tools/wechat_link_monitor.py` L300 正则一行修复（已入仓，commit 1f89e2d86 随 vault backup 收口）+ 本任务单执行报告（本文件）

**完成内容**：正则 `m\.toutiao\.com/is([A-Za-z0-9]+)` → `m\.toutiao\.com/is/?([A-Za-z0-9]+)`（兼容 isXXX 与 is/XXX 两形态）；docstring 形态清单同步一行。用 main() 头条文章分支同代码路径实跑老朱链接 https://m.toutiao.com/is/Lw4BUQtFZ9E/：302 展开 → gid=7667212185281528364 → info 取正文（标题《用WorkBuddy搭建自媒体全自动流水线…》2731 字）→ 落 inbox → knowledge_ize → mark_seen。seen 写入该短链原样 URL（canonical_key 对 is 短链=原样，口径一致）。

**验证**：①正则单测三形态（is/XXX/、isXXX/、is/XXX 无尾斜杠）全匹配；②端到端实跑产出落盘并抽检内容正确——00_inbox/wechat-collect/src_wechat_article_tt_af50baaada5fc2f2.md（7264B）+ 知识化产物 00_inbox/wechat-collect/knowledge/case-wechat-article_tt_af50baaada5fc2f2.md（注：00_inbox/ 按 dba6f5376 既定口径不入仓，此处为运行产物实证非入库交付物）；③回归 pytest kdo-tools/tests -k "wechat or link" 12 passed；④「失败不记 seen」设计未动（L477-478 原样保留，本次成功才记 seen 与既有语义一致）。

**边界**：只改 L300 正则一行 + docstring 一行，未动视频管线/公众号分支/seen 语义；未跑完整 main()（避免连带处理其他链接扩 scope），手工复刻头条文章分支单链验证。监控下轮整点自动跑时该链已在 seen 不会重复采。

**需要谁动作**：欧阳锋终审（diff 见 commit 1f89e2d86；实证文件路径如上）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（2026-09-02 欧阳锋，PASS A）

- **等级**：A
- **通过维度**：版本对齐三问全过（①fix 随 commit 1f89e2d86 23:13:08 入仓，工作区该文件干净；②无长驻 wechat_link_monitor 进程跑旧码，下轮整点自动拾新版；③审查对象=HEAD 最新真相源）。验收要点成立——老朱 20:09 链接 https://m.toutiao.com/is/Lw4BUQtFZ9E/ 端到端落 inbox 实证：00_inbox/wechat-collect/src_wechat_article_tt_af50baaada5fc2f2.md（7264B 与报告一致，标题《用WorkBuddy搭建自媒体全自动流水线…》与来源 URL 抽检正确）+ 知识化产物同目录 knowledge/ 落盘；seen 已登记原样短链 URL（60_feedback/wechat-collect/seen_links.txt L34）
- **溯源要点（独立复跑，非采信报告）**：①正则三形态（is/XXX/、isXXX/、is/XXX 无尾斜杠）单测全匹配提取正确 gid 段；②pytest tests -k "wechat or link" 12 passed 与报告一致（kdo-tools 目录下复现）；③「失败不记 seen」语义原样保留（wechat_link_monitor.py L477-478）；④git show 1f89e2d86 确认 diff 确为一行正则+一行 docstring，红线零扩 scope
- **缺陷**：无
- **残余风险**：监控下轮整点为该修复首次生产自动触发（本轮系手工复刻同代码路径验证）；is 短链 canonical_key=原样 URL，同文以不同短链码再分享会重复采集——既有设计非本单范围，已落最小建议书 prop_20260902_ouyangfeng-toutiao-shortlink-canonical-key
