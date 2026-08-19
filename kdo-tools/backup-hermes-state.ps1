# 老顽童 Hermes state.db 定时备份（2026-08-19 从 WSL backup-laowantong-state.sh 迁移到 Windows）
# 原 WSL 版备份的是 WSL 侧 profile；全量 Windows 迁移后背 Windows 侧 profile
# 计划任务 hermes-laowantong-backup 每小时调用；保留最近 10 份
$ProfileDir = "$env:LOCALAPPDATA\hermes\profiles\laowantong"
$BackupDir  = "$ProfileDir\backups"
$Src        = "$ProfileDir\state.db"

New-Item -ItemType Directory -Force -Path $BackupDir | Out-Null
if (Test-Path $Src) {
    $Dst = Join-Path $BackupDir ("state.db." + (Get-Date -Format "yyyyMMdd_HHmmss"))
    Copy-Item $Src $Dst
    Get-ChildItem "$BackupDir\state.db.*" |
        Sort-Object LastWriteTime -Descending |
        Select-Object -Skip 10 |
        Remove-Item -Force
    Write-Output "backup ok: $Dst"
} else {
    Write-Output "skip: $Src not found"
}
