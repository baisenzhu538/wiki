@echo off
rem #508 kdo-l1-archive wrapper (pure ASCII; log inside cmd, not schtasks TR)
rem #532: KDO_ROOT env first, fallback to script-relative root (portable seed)
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
"C:\Program Files\Python312\python.exe" kdo-tools\l1_capture.py --archive >> D:\KDO-memory\L1-full-archive\_archive.log 2>&1
exit /b %ERRORLEVEL%
