---
id: diag_20260826_ouyangfeng-queue-transition-gbk-failopen
title: queue_transition 在 Windows 的 GBK 解码崩溃被 fail-open 吞掉（门禁静默致盲风险）
type: proposal
status: orchestrated
author: 欧阳锋（审查）
audience: 王语嫣
date: 2026-08-26
orchestration: 已裁定（08-27 王语嫣）：采纳立项 #568 P1（subprocess 编码+Popen reader+fail-open 可见化+仓库级 reconfigure；probe stdout 污染并入）
---

# 建议书：queue_transition 在 Windows 的 GBK 解码崩溃被 fail-open 吞掉

- **日期**：2026-08-26 · 欧阳锋（#541 终审 FAIL 流转时实测）

## 现象

`queue_transition.py review` 执行中 stderr 打出 UnicodeDecodeError（'gbk' codec can't decode，subprocess.py _readerthread），主流程序继续。流转/commit/dashboard 均成功，但异常被某处 try/except fail-open 吞掉——若是 `_git_uncommitted`/`_git_tracked`（E040 门禁的 KDO 源码仓侧检查），则该门禁在本机静默致盲。

## 定位

`90_control/scripts/queue_transition.py` 的 subprocess.run 全部 `text=True` 未指定 `encoding='utf-8'`（L224/230/237/571/669）——Windows 默认 GBK 解码，git 输出含 UTF-8 中文路径即炸。

## 建议方向

subprocess.run 统一加 `encoding='utf-8', errors='replace'`；或 fail-open 吞异常时至少 print 一行 WARNING 标注哪个门禁被跳过。P2。

## 追加实证（08-27 05:5x）

同族第二例：`role_registry.py heartbeat` 的 ✅ print 在 GBK 控制台炸 UnicodeEncodeError——写入成功但进程非零退出，`&&` 链下游被静默跳过（我的 cron 领审链实踩）。佐证「建议方向」应升级为仓库级：CLI 入口统一 reconfigure(stdout, utf-8)。

## 追加实证（08-27 晚 · 第三例，活体）

#556 终审 FAIL 流转时 subprocess reader 线程当场炸：`UnicodeDecodeError: 'gbk' codec can't decode byte 0x8b in position 54`（subprocess.py _readerthread fh.read）——traceback 直接打到终端，但流转本身成功且 auto-commit 落账（fail-open 按设计工作）。实证升级点：**崩溃发生在 subprocess 管道的 reader 线程**（不是 run 的解码参数能直接覆盖的位置），修复需覆盖 Popen 管道读取路径，不止 subprocess.run 调用点。
