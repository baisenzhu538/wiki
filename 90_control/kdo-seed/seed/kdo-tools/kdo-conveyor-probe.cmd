@echo off
rem Conveyor probe (scheduled task kdo-conveyor-probe, every 10 min, #421)
rem #519 root cause: schtasks TR "cmd /c ""python.exe" "script" >> log 2>&1"" nested quotes
rem get stripped by cmd -> 'C:\Program' not a command -> silent noop 15h (2026-08-24 20:58
rem ~ 2026-08-25 11:1x, zero log lines, state frozen). Wrapper file removes the whole
rem nested-quote failure class (same pattern as kdo-l1-capture.cmd).
rem Failure visible: probe prints a summary line every run -> conveyor-probe.log;
rem non-zero exit also -> pending-git-commits.log (#434 caliber, no silent swallow).
rem Keep this file pure ASCII (cmd reads ANSI).
rem #532: KDO_ROOT env first, fallback to script-relative root (portable seed)
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
"C:\Program Files\Python312\python.exe" kdo-tools\conveyor_probe.py >> logs\conveyor-probe.log 2>&1
if errorlevel 1 (
  echo [%date% %time%] kdo-conveyor-probe FAILED exit=%errorlevel% >> 90_control\pending-git-commits.log
)
