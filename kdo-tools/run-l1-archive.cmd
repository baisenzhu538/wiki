@echo off
rem #508 kdo-l1-archive wrapper (pure ASCII; log inside cmd, not schtasks TR)
cd /d C:\Users\Administrator\Desktop\wiki
"C:\Program Files\Python312\python.exe" kdo-tools\l1_capture.py --archive >> D:\KDO-memory\L1-full-archive\_archive.log 2>&1
exit /b %ERRORLEVEL%
