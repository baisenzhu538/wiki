@echo off
rem KDO huangyaoshi OS-level doorbell (2026-08-28, #565 preview).
rem schtasks every 15min: resume wiki session, run one wake turn.
rem Session lock conflict (interactive alive) = fail-open: exit, next beat retries.
rem Pure ASCII + CRLF (cmd reads ANSI; LF-only batch mis-parses).
set KIMI=C:\Users\Administrator\.kimi-code\bin\kimi.exe
set ROOT=C:\Users\Administrator\Desktop\wiki
set LOG=%ROOT%\logs\kimi-doorbell.log
cd /d %ROOT%
python "%ROOT%\kdo-tools\kdo_doorbell_guard.py" huangyaoshi
if errorlevel 1 (
  echo %time% session alive, skip >> %LOG%
  exit /b 0
)
echo === %date% %time% doorbell fire === >> %LOG%
"%KIMI%" -c -p "Menling self-check: read unread segment of 90_control/todos/huangyaoshi.md + run python 90_control/scripts/queue_transition.py myqueue huangyaoshi. If myqueue shows an in-progress (claimed-huangyaoshi) task -> CONTINUE that task (read its task file, keep building, do not claim new). Else if claimable tasks exist -> claim the first in queue order and work it. New reviews/messages -> respond. Nothing -> one-line standby and end." >> %LOG% 2>&1
if errorlevel 1 (
  echo %time% resume failed, starting fresh session >> %LOG%
  "%KIMI%" -p "You are huangyaoshi (Builder): first read AGENTS.md + .agent/startup.md (incl. step-0 doorbell self-check). Then: read unread segment of 90_control/todos/huangyaoshi.md + run python 90_control/scripts/queue_transition.py myqueue huangyaoshi. If myqueue shows an in-progress task -> continue it, do not claim new. Else claim first claimable and work it. Nothing -> standby and end." >> %LOG% 2>&1
)
echo === %date% %time% doorbell done exit=%errorlevel% === >> %LOG%
