# 启动agent.ps1 — KDO 一键启动（#445，冷启动三件套 A 项）
# 老朱右键一键：直接拉起全部角色终端（用户自行输入），无需菜单选择。
#
# 用法：
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -All           # 一键拉起全部角色终端（默认行为）
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -Role 黄药师    # 拉起单个角色
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -Register       # 注册右键菜单（HKCU，免管理员）
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -Unregister     # 移除右键菜单
#   powershell -ExecutionPolicy Bypass -File 启动agent.ps1 -DryRun         # 只打印将执行的命令

param(
    [string]$Role = "",
    [switch]$All,
    [switch]$Register,
    [switch]$Unregister,
    [switch]$DryRun
)

$WIKI = "C:\Users\Administrator\Desktop\wiki"
$ErrorActionPreference = "Stop"
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# 角色表（老朱 08-23 直令顺序与配色：5 标签 5 色，只进 wiki 不拉起 agent，按需自选）
$Roles = [ordered]@{
    "黄药师" = @{ color = "#FFB74D" }   # 橙黄
    "老顽童" = @{ color = "#81C784" }   # 绿
    "王语嫣" = @{ color = "#4FC3F7" }   # 蓝
    "欧阳锋" = @{ color = "#E57373" }   # 红
    "风清扬" = @{ color = "#BA68C8" }   # 紫
}

# Windows Terminal 全路径（app execution alias 可能不在 PATH，Get-Command 检测会漏——08-23 实证）
$WT_EXE = "$env:LOCALAPPDATA\Microsoft\WindowsApps\wt.exe"

function New-WtTabArgs {
    # 生成 wt 多标签参数：首 tab 直接给 -d --tabColor，后续 " ; new-tab -d --tabColor ..." 串联。
    # 老朱 08-23 直令：标签只进 wiki 目录、不自动拉起 agent（各角色订阅额度不同，按需自选）；
    # 标题=角色名 + tab 颜色=角色专属色（5 色区分）。
    $tabs = @()
    foreach ($k in $Roles.Keys) {
        $color = $Roles[$k].color
        # shell 用 powershell（cmd 在管理员窗口会覆盖标题为"管理员: ..."，08-23 两次实证；powershell 不覆盖 wt --title）
        $seg = if ($tabs.Count -eq 0) {
            "-d `"$WIKI`" --tabColor $color --title $k powershell -NoExit -Command `"cd '$WIKI'`""
        } else {
            "new-tab -d `"$WIKI`" --tabColor $color --title $k powershell -NoExit -Command `"cd '$WIKI'`""
        }
        $tabs += $seg
    }
    return ($tabs -join " ; ")
}

function Start-AgentSession {
    param([string]$role)
    if (-not $Roles.Contains($role)) {
        Write-Host "未知角色: $role。可选: $($Roles.Keys -join ' / ')" -ForegroundColor Red
        return
    }
    if ($DryRun) {
        Write-Host "[DryRun] tab: 角色=$role（仅进 wiki，不拉起 agent）"
        return
    }
    if (Test-Path $WT_EXE) {
        # 单角色 = 单 tab（颜色+原生标题；shell=powershell 防 cmd 覆盖标题）
        Start-Process $WT_EXE -ArgumentList "-d `"$WIKI`" --tabColor $($Roles[$role].color) --title $role powershell -NoExit -Command `"cd '$WIKI'`""
    } else {
        Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$WIKI'"
    }
    Write-Host "已拉起 $role 标签（wiki 目录）" -ForegroundColor Green
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
    # 单入口：右键 wiki 文件夹 → "启动 KDO Agent" → 一键拉起全部角色终端（老朱 08-23 直令：不菜单选择，直接开窗）
    # command 值必须整串引号包裹（explorer 按值解析命令，内部引号转义成 \"）——否则"没有关联应用"（08-23 实证）
    $base = "HKCU:\Software\Classes\Directory\shell\KDOAgent"
    $script = "C:\Users\Administrator\Desktop\wiki\kdo-tools\启动agent.ps1"
    $cmd = "`"powershell.exe`" -NoProfile -ExecutionPolicy Bypass -File `"$script`" -All"
    New-Item -Path $base -Force | Out-Null
    Set-ItemProperty -Path $base -Name "(default)" -Value "启动 KDO Agent（5 终端）"
    Set-ItemProperty -Path $base -Name "Icon" -Value "shell32.dll,220"
    New-Item -Path "$base\command" -Force | Out-Null
    Set-ItemProperty -Path "$base\command" -Name "(default)" -Value $cmd
    Write-Host "右键菜单已注册（HKCU，单入口一键 5 终端）：右键 wiki 文件夹 → 启动 KDO Agent" -ForegroundColor Green
}

function Unregister-ContextMenu {
    Remove-Item -Path "HKCU:\Software\Classes\Directory\shell\KDOAgent" -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "右键菜单已移除" -ForegroundColor Yellow
}

if ($Register) { Register-ContextMenu; return }
if ($Unregister) { Unregister-ContextMenu; return }
if ($Role) { Start-AgentSession $Role; return }
# 默认/ -All：一键拉起全部角色终端（老朱直令：同一 WT 窗口多个标签页，用户自行输入）
if ($All -or -not $Role) {
    if ($DryRun) {
        foreach ($k in $Roles.Keys) { Write-Host "[DryRun] tab: 角色=$k（仅进 wiki，不拉起 agent）" }
        Write-Host "将用 wt 多标签（同一窗口 $($Roles.Count) 个 tab）"
        return
    }
    if (Test-Path $WT_EXE) {
        Start-Process $WT_EXE -ArgumentList (New-WtTabArgs)
        Write-Host "`n已拉起 Windows Terminal：$($Roles.Count) 个标签页（wiki 目录）。窗口内直接输入即可。" -ForegroundColor Cyan
    } else {
        foreach ($k in $Roles.Keys) { Start-AgentSession $k }
        Write-Host "`nwt 缺失，已按单窗口拉起（建议安装 Windows Terminal）" -ForegroundColor Yellow
    }
}
