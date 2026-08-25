@echo off
rem #507 kdo-daily-audit-digest wrapper (pure ASCII; log inside cmd, not schtasks TR)
rem #532: KDO_ROOT env first, fallback to script-relative root (portable seed)
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
"C:\Program Files\Python312\python.exe" kdo-tools\daily-audit-digest.py >> D:\KDO-memory\L2-digest\_run.log 2>&1
exit /b %ERRORLEVEL%
