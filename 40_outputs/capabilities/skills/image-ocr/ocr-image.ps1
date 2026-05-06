# OCR Pipeline: Chinese text extraction from images
# Engine: PaddleOCR v5 (local, no API key needed)
# Usage: .\ocr-image.ps1 <image-path> [-Batch]
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$ImagePath,
    [switch]$Batch
)

$PIPELINE_DIR = "C:\Users\Administrator\ocr-pipeline"
$NODE_SCRIPT = Join-Path $PIPELINE_DIR "ocr-paddle.cjs"

if (-not (Test-Path $NODE_SCRIPT)) {
    Write-Error "OCR pipeline not found at: $PIPELINE_DIR"
    Write-Error "Expected: ocr-paddle.cjs, models/, node_modules/"
    exit 1
}

function Invoke-Ocr {
    param([string]$Path)

    Write-Host "`n=== OCR: $(Split-Path $Path -Leaf) ===" -ForegroundColor Cyan
    Push-Location $PIPELINE_DIR
    try {
        $result = & node $NODE_SCRIPT $Path 2>&1
        $exitCode = $LASTEXITCODE
    } finally {
        Pop-Location
    }

    if ($exitCode -ne 0) {
        Write-Host "ERROR processing $Path" -ForegroundColor Red
        Write-Host ($result -join "`n")
        return $false
    }

    Write-Host ($result -join "`n")
    return $true
}

if ($Batch) {
    $images = Get-ChildItem $ImagePath -Include @('*.png','*.jpg','*.jpeg') -ErrorAction SilentlyContinue
    if (-not $images) {
        Write-Error "No images found matching: $ImagePath"
        exit 1
    }

    $total = $images.Count
    $ok = 0
    foreach ($img in $images) {
        if (Invoke-Ocr $img.FullName) { $ok++ }
    }
    Write-Host "`n=== Done: $ok/$total succeeded ===" -ForegroundColor Green
} else {
    if (-not (Test-Path $ImagePath)) {
        Write-Error "Image not found: $ImagePath"
        exit 1
    }
    Invoke-Ocr (Resolve-Path $ImagePath).Path
}
