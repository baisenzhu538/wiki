@echo off
rem #508 kdo-l1-archive wrapper (pure ASCII; log inside cmd, not schtasks TR)
rem #532: KDO_ROOT env first, fallback to script-relative root (portable seed)
rem #690: KDO-memory root via kdo_memory_root marker scan (guard: no hardcoded drive letter)
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
for /f "delims=" %%i in ('"C:\Program Files\Python312\python.exe" kdo-tools\kdo_memory_root.py') do set "KDO_MEM=%%i"
if not defined KDO_MEM (
    echo kdo_memory_root resolve failed, gate-blocked alarm written by resolver, skip this run 1>&2
    exit /b 1
)
"C:\Program Files\Python312\python.exe" kdo-tools\l1_capture.py --archive >> "%KDO_MEM%\L1-full-archive\_archive.log" 2>&1
exit /b %ERRORLEVEL%
