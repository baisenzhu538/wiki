@echo off
rem #553: role_clock scheduler beat (5 min via schtasks kdo-role-clock). Keep pure ASCII.
rem #532: KDO_ROOT env first, fallback to script-relative root (portable seed)
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
"C:\Program Files\Python312\python.exe" kdo-tools\role_clock.py run >> logs\role-clock.log 2>&1
