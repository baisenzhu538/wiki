@echo off
rem KDO daily health check (migrated 2026-08-19 from WSL cron: python3 -m kdo watch --health)
rem Scheduled task kdo-health-daily runs this at 02:07 daily. Keep this file pure ASCII (cmd reads ANSI).
rem #532: KDO_ROOT env first, fallback to script-relative root (portable seed)
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
"C:\Program Files\Python312\python.exe" -m kdo watch --health >> logs\kdo-health-cron.log 2>&1
rem #549: daily token metering (delta cursor, no history backfill)
"C:\Program Files\Python312\python.exe" kdo-tools\token_meter.py >> logs\kdo-health-cron.log 2>&1
rem #592 R3: vault integrity check (worktree/bundle/offsite copy, anomalies to gate-blocked)
"C:\Program Files\Python312\python.exe" 90_control\scripts\vault-integrity-check.py >> logs\kdo-health-cron.log 2>&1
rem #671: graph index coverage probe (30_wiki dirs vs graph_state path_map, gaps to gate-blocked)
"C:\Program Files\Python312\python.exe" 90_control\scripts\graph-index-coverage-probe.py >> logs\kdo-health-cron.log 2>&1
