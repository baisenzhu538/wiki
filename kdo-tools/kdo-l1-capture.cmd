@echo off
rem L1 full-context capture (scheduled task kdo-l1-capture, every 30 min, #471)
rem Incremental capture + trace + mirror + verify + size log.
rem Failure visible: stderr -> l1-capture.log + pending-git-commits.log (#434 caliber, no silent swallow).
rem Keep this file pure ASCII (cmd reads ANSI).
cd /d C:\Users\Administrator\Desktop\wiki
"C:\Program Files\Python312\python.exe" kdo-tools\l1_capture.py >> logs\l1-capture.log 2>&1
if errorlevel 1 (
  echo [%date% %time%] kdo-l1-capture FAILED exit=%errorlevel% >> 90_control\pending-git-commits.log
)
"C:\Program Files\Python312\python.exe" kdo-tools\l1_capture.py --verify >> logs\l1-capture.log 2>&1
if errorlevel 1 (
  echo [%date% %time%] kdo-l1-capture VERIFY-FAILED exit=%errorlevel% >> 90_control\pending-git-commits.log
)
