@echo off
rem KDO daily health check (migrated 2026-08-19 from WSL cron: python3 -m kdo watch --health)
rem Scheduled task kdo-health-daily runs this at 02:07 daily. Keep this file pure ASCII (cmd reads ANSI).
cd /d C:\Users\Administrator\Desktop\wiki
"C:\Program Files\Python312\python.exe" -m kdo watch --health >> logs\kdo-health-cron.log 2>&1
