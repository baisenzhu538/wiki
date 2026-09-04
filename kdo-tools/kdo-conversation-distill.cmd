@echo off
rem #645: conversation distill scheduler (23:50 via schtasks kdo-conversation-distill). Keep pure ASCII.
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
"C:\Program Files\Python312\python.exe" kdo-tools\conversation_distill.py >> logs\conversation-distill.log 2>&1
