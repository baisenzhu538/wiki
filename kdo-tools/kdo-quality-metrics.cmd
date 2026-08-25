@echo off
rem Quality metrics weekly baseline report (scheduled task kdo-quality-metrics, Monday 06:35, #514)
rem Read-only stats: queue history + gate-blocked.log + force-exceptions.log -> 60_feedback/auto/quality-metrics/
rem Wrapper-file pattern per #519 lesson (no nested quotes in schtasks TR).
rem Keep this file pure ASCII (cmd reads ANSI).
cd /d C:\Users\Administrator\Desktop\wiki
"C:\Program Files\Python312\python.exe" kdo-tools\quality_metrics.py >> logs\quality-metrics.log 2>&1
if errorlevel 1 (
  echo [%date% %time%] kdo-quality-metrics FAILED exit=%errorlevel% >> 90_control\pending-git-commits.log
)
