# 启动agent.ps1 — KDO 一键启动（#445，冷启动三件套 A 项）
# 老朱三步入会话：右键 wiki 文件夹 → 选角色 → 自动 cd wiki + 拉起 CLI。
# 飞书类角色（洪七公/段王爷/风清扬）不进菜单——gateway 常驻，飞书直接聊。
#
# 用法：
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1             # 数字菜单选择
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -Role 黄药师  # 直接拉起
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -Register     # 注册右键菜单（HKCU，免管理员）
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -Unregister   # 移除右键菜单
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -DryRun       # 只打印将执行的命令

param(
    [string]$Role = "",
    [switch]$Register,
    [switch]$Unregister,
    [switch]$DryRun
)

$WIKI = "C:\Users\Administrator\Desktop\wiki"
$ErrorActionPreference = "Stop"
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# 角色 → 命令（CLI 类；新增角色在此登记）
$Roles = [ordered]@{
    "黄药师" = @{ cmd = "claude";   desc = "Claude Code（Builder）" }
    "欧阳锋" = @{ cmd = "kimi";     desc = "Kimi Code CLI（Architect）" }
    "王语嫣" = @{ cmd = "kimi";     desc = "Kimi Code CLI（Consultant）" }
    "老顽童" = @{ cmd = "hermes";   desc = "Hermes CLI（Producer，profile=laowantong）" }
}

function Start-AgentSession {
    param([string]$role)
    if (-not $Roles.Contains($role)) {
        Write-Host "未知角色: $role。可选: $($Roles.Keys -join ' / ')" -ForegroundColor Red
        return
    }
    $cmd = $Roles[$role].cmd
    if ($DryRun) {
        Write-Host "[DryRun] 将执行: cd $WIKI && $cmd（角色=$role）"
        return
    }
    # Windows Terminal 拉起（-d 指定工作目录 = wiki），无 wt 时回退 powershell 新窗
    $wt = Get-Command wt -ErrorAction SilentlyContinue
    if ($wt) {
        Start-Process wt -ArgumentList "-d", "`"$WIKI`"", "cmd", "/k", "chcp 65001 >nul & $cmd"
    } else {
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$WIKI'; & '$cmd'"
    }
    Write-Host "已拉起 $role（$cmd）于 $WIKI" -ForegroundColor Green
}

function Show-Menu {
    Write-Host "`n=== KDO Agent 启动 ===  (wiki: $WIKI)`n" -ForegroundColor Cyan
    $i = 0
    foreach ($k in $Roles.Keys) { $i++; Write-Host "  $i. $k — $($Roles[$k].desc)" }
    Write-Host "  0. 退出`n"
    $sel = Read-Host "选择角色"
    if ($sel -eq "0" -or [string]::IsNullOrWhiteSpace($sel)) { return }
    $idx = [int]$sel
    if ($idx -ge 1 -and $idx -le $Roles.Count) {
        Start-AgentSession $Roles.Keys[$idx - 1]
    } else {
        Write-Host "无效选择" -ForegroundColor Red
    }
}

function Register-ContextMenu {
    $base = "HKCU:\Software\Classes\Directory\shell\KDOAgent"
    $script = "C:\Users\Administrator\Desktop\wiki\kdo-tools\启动agent.ps1"
    $ps = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File `"$script`" -Role"
    New-Item -Path $base -Force | Out-Null
    Set-ItemProperty -Path $base -Name "(default)" -Value "启动 KDO Agent"
    Set-ItemProperty -Path $base -Name "Icon" -Value "shell32.dll,220"
    foreach ($role in $Roles.Keys) {
        $rp = "$base\shell\$role"
        New-Item -Path $rp -Force | Out-Null
        Set-ItemProperty -Path $rp -Name "(default)" -Value "$role — $($Roles[$role].desc)"
        New-Item -Path "$rp\command" -Force | Out-Null
        Set-ItemProperty -Path "$rp\command" -Name "(default)" -Value "$ps $role"
    }
    Write-Host "右键菜单已注册（HKCU）：右键 wiki 文件夹 → 启动 KDO Agent → 选角色" -ForegroundColor Green
}

function Unregister-ContextMenu {
    Remove-Item -Path "HKCU:\Software\Classes\Directory\shell\KDOAgent" -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "右键菜单已移除" -ForegroundColor Yellow
}

if ($Register) { Register-ContextMenu; return }
if ($Unregister) { Unregister-ContextMenu; return }
if ($Role) { Start-AgentSession $Role } else { Show-Menu }
