@echo off
rem #607: vault git snapshot backup (30 min via schtasks kdo-vault-git-backup). Keep pure ASCII.
if "%KDO_ROOT%"=="" set "KDO_ROOT=%~dp0.."
cd /d "%KDO_ROOT%"
"C:\Program Files\Python312\python.exe" kdo-tools\vault_git_backup.py >> logs\vault-git-backup.log 2>&1
