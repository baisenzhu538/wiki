@echo off
rem #507 kdo-daily-audit-digest wrapper (pure ASCII; log inside cmd, not schtasks TR)
cd /d C:\Users\Administrator\Desktop\wiki
"C:\Program Files\Python312\python.exe" kdo-tools\daily-audit-digest.py >> D:\KDO-memory\L2-digest\_run.log 2>&1
exit /b %ERRORLEVEL%
