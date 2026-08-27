@echo off
rem KDO huangyaoshi OS-level doorbell (2026-08-28, #565 preview).
rem Fired by schtasks every 15min: resume the wiki session and run one wake turn.
rem Session lock conflict (interactive session alive) = harmless fail-open: exit, next beat retries.
rem Keep this file pure ASCII (cmd reads ANSI).
set KIMI=C:\Users\Administrator\.kimi-code\bin\kimi.exe
set ROOT=C:\Users\Administrator\Desktop\wiki
set LOG=%ROOT%\logs\kimi-doorbell.log
cd /d %ROOT%
echo === %date% %time% doorbell fire === >> %LOG%
"%KIMI%" -c --auto -p "门铃自检：读 90_control/todos/huangyaoshi.md 未读段 + 跑 python 90_control/scripts/queue_transition.py myqueue huangyaoshi。有新终审/新任务/新消息→按队列序施工或响应；无事→一句话待命并立即结束。" >> %LOG% 2>&1
if errorlevel 1 (
  echo %time% resume failed, starting fresh session >> %LOG%
  "%KIMI%" --auto -p "你是黄药师（Builder）：先读 AGENTS.md + .agent/startup.md 开机（含第0步门铃自查）。然后门铃自检：读 90_control/todos/huangyaoshi.md 未读段 + 跑 python 90_control/scripts/queue_transition.py myqueue huangyaoshi，有事施工无事待命即结束。" >> %LOG% 2>&1
)
echo === %date% %time% doorbell done (exit %errorlevel%) === >> %LOG%
