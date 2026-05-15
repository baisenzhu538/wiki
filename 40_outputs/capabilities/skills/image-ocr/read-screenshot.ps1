# Read Screenshot: Auto-discover latest screenshot and OCR it
# Usage: .\read-screenshot.ps1          → latest screenshot on Desktop
#        .\read-screenshot.ps1 -Path "C:\..." → specific image
#        .\read-screenshot.ps1 -Last 3   → last 3 screenshots
param(
    [string]$Path,
    [int]$Last = 1
)

$DESKTOP = [Environment]::GetFolderPath("Desktop")
$PIPELINE_DIR = "C:\Users\Administrator\ocr-pipeline"
$NODE_SCRIPT = Join-Path $PIPELINE_DIR "ocr-paddle.cjs"
$VAULT_MEDIA = "C:\Users\Administrator\Desktop\wiki\00_inbox"

# Ensure vault media dir exists
if (-not (Test-Path $VAULT_MEDIA)) {
    New-Item -ItemType Directory -Path $VAULT_MEDIA -Force | Out-Null
}

function Invoke-Ocr {
    param([string]$ImagePath)

    $filename = Split-Path $ImagePath -Leaf
    Write-Host "`n=== OCR: $filename ===" -ForegroundColor Cyan

    Push-Location $PIPELINE_DIR
    try {
        $result = & node $NODE_SCRIPT $ImagePath 2>&1
        $exitCode = $LASTEXITCODE
    } finally {
        Pop-Location
    }

    if ($exitCode -ne 0) {
        Write-Host "ERROR: OCR failed" -ForegroundColor Red
        Write-Host ($result -join "`n")
        return $null
    }

    $text = $result -join "`n"
    return $text
}

# Mode 1: Specific path
if ($Path) {
    if (-not (Test-Path $Path)) {
        Write-Error "Image not found: $Path"
        exit 1
    }
    $text = Invoke-Ocr (Resolve-Path $Path).Path
    Write-Host $text
    exit 0
}

# Mode 2: Auto-discover latest screenshots from Desktop
$patterns = @("Snipaste_*.png", "Screenshot_*.png", "ScreenShot_*.png", "Clipboard_*.png", "image_*.png", "*.screenshot*.png")
$allImages = @()
foreach ($pattern in $patterns) {
    $found = Get-ChildItem $DESKTOP -Filter $pattern -ErrorAction SilentlyContinue
    $allImages += $found
}

# Also check vault inbox
$vaultImages = Get-ChildItem $VAULT_MEDIA -Filter "screenshot*.png" -ErrorAction SilentlyContinue
$allImages += $vaultImages

if ($allImages.Count -eq 0) {
    # Fallback: any recent PNG on Desktop
    $allImages = Get-ChildItem $DESKTOP -Filter "*.png" -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 10
}

if ($allImages.Count -eq 0) {
    Write-Error "No screenshots found on Desktop or in vault inbox"
    exit 1
}

# Sort by time, pick last N
$selected = $allImages | Sort-Object LastWriteTime -Descending | Select-Object -First $Last

Write-Host "Found $($selected.Count) screenshot(s):" -ForegroundColor Green
$selected | ForEach-Object { Write-Host "  $($_.Name) ($($_.LastWriteTime))" }

foreach ($img in $selected) {
    $text = Invoke-Ocr $img.FullName
    if ($text) {
        # Also copy to vault for persistence
        $vaultCopy = Join-Path $VAULT_MEDIA ("ocr_" + $img.Name)
        Copy-Item $img.FullName $vaultCopy -Force
        Write-Host "`nSaved to vault: $vaultCopy" -ForegroundColor Gray
    }
}
