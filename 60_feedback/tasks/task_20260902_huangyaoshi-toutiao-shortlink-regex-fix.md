---
id: task_20260902_huangyaoshi-toutiao-shortlink-regex-fix
title: 头条短链 is/XXX 形态正则漏配导致采集链断（老朱 09-02 20:09 链接卡死实证）——一行修复
seq: 621
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 晚问「链接为什么没走工作流」→ 王语嫣实测定位正则漏配（采集链断点，线上在流血）
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T15:12:36.361500+00:00'
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
