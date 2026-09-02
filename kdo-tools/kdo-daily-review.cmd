@echo off
rem #623: daily Truman review scheduler (23:37 via schtasks kdo-daily-review). Keep pure ASCII.
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
"C:\Program Files\Python312\python.exe" kdo-tools\daily_review.py >> logs\daily-review.log 2>&1
