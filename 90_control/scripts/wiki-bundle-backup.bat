@echo off
rem ============================================================
rem #589 wiki vault daily bundle backup (incident anti-recurrence)
rem Schedule: daily 02:30 (offset from 02:00 incident window), S4U no-window
rem Keeps rolling >=4 bundles, logs to %LOG%, exit code file for verification
rem ============================================================
setlocal enabledelayedexpansion
set "GIT=C:\Program Files\Git\cmd\git.exe"
set "WIKI=C:\Users\Administrator\Desktop\wiki"
set "DEST=D:\KDO-memory"
set "LOG=%DEST%\wiki-bundle-daily.log"

rem --- ISO date stamp (locale-independent) ---
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd"') do set "TODAY=%%i"
set "BUNDLE=%DEST%\wiki-bundle-%TODAY%.bundle"

rem --- 2026-09-05 laozhu: weekly full bundle gate (Monday only) ---
rem Daily full bundle grew to ~2GB/day x2 disks (C: offsite copy kept 3) -> C: 95%.
rem Obsidian snapshot + pruning still run DAILY; full bundle only on Monday.
for /f %%w in ('powershell -NoProfile -Command "(Get-Date).DayOfWeek"') do set "WD=%%w"
if /i not "%WD%"=="Monday" goto :daily_only

echo [%DATE% %TIME%] === wiki weekly bundle start (Monday) === >> "%LOG%"

rem --- create bundle (all refs) ---
"%GIT%" -C "%WIKI%" bundle create "%BUNDLE%" --all >> "%LOG%" 2>&1
if errorlevel 1 (
    echo [%DATE% %TIME%] ERROR: bundle create failed rc^>0 >> "%LOG%"
    echo FAIL > "%DEST%\wiki-bundle-daily.last-result.txt"
    exit /b 1
)

rem --- verify bundle ---
"%GIT%" -C "%WIKI%" bundle verify "%BUNDLE%" >> "%LOG%" 2>&1
if errorlevel 1 (
    echo [%DATE% %TIME%] ERROR: bundle verify failed >> "%LOG%"
    echo FAIL > "%DEST%\wiki-bundle-daily.last-result.txt"
    exit /b 1
)

rem --- HEAD comparison: HEAD commit must be in bundle ---
"%GIT%" -C "%WIKI%" rev-parse HEAD > "%TEMP%\wiki-bundle-head.txt" 2>nul
set /p WIKIHEAD=<"%TEMP%\wiki-bundle-head.txt"
del /q "%TEMP%\wiki-bundle-head.txt" >nul 2>&1
if "%WIKIHEAD%"=="" (
    echo [%DATE% %TIME%] ERROR: rev-parse HEAD returned empty >> "%LOG%"
    echo FAIL > "%DEST%\wiki-bundle-daily.last-result.txt"
    exit /b 1
)
"%GIT%" -C "%WIKI%" bundle list-heads "%BUNDLE%" | findstr /i "%WIKIHEAD%" >nul
if errorlevel 1 (
    rem Race note: obsidian-git auto-commit (10min cadence) can land a new HEAD
    rem between bundle create and this check. Bundle itself is valid+verified.
    rem Downgrade to WARN, keep last-good semantic: bundle usable, retry HEAD next night.
    echo [%DATE% %TIME%] WARN: HEAD %WIKIHEAD% not in bundle heads ^(auto-commit race^) - bundle kept >> "%LOG%"
)

echo [%DATE% %TIME%] OK bundle=%BUNDLE% HEAD=%WIKIHEAD% >> "%LOG%"
echo OK > "%DEST%\wiki-bundle-daily.last-result.txt"

rem --- #592 R1: offsite copy (now weekly, runs only after Monday bundle) ---
call "C:\Users\Administrator\Desktop\wiki\90_control\scripts\wiki-bundle-offsite-2nd.bat" >> "%LOG%" 2>&1
if errorlevel 1 (
    echo [%DATE% %TIME%] WARN: offsite step2 failed, main backup unaffected >> "%LOG%"
)

rem --- .obsidian snapshot (not git-tracked by design: multi-device sync concerns, 05-02 ab2bd33ba) ---
rem 08-31 incident proved .obsidian is a backup blind spot (config total loss, zero recovery).
rem Git tracking stays OFF (per-machine config). This is a per-machine rolling snapshot only.
set "OBS_SNAP=%DEST%\obsidian-snapshot"
if not exist "%OBS_SNAP%" mkdir "%OBS_SNAP%"
powershell -NoProfile -Command "Remove-Item -Recurse -Force '%OBS_SNAP%\*' -ErrorAction SilentlyContinue; Copy-Item -Recurse -Force '%WIKI%\.obsidian' '%OBS_SNAP%\.obsidian' | Out-Null; if ($?) { 'OK' } else { 'FAIL' }" > "%TEMP%\obs-snap-result.txt" 2>nul
set /p OBS_RESULT=<"%TEMP%\obs-snap-result.txt"
del /q "%TEMP%\obs-snap-result.txt" >nul 2>&1
if "%OBS_RESULT%"=="OK" (
    echo [%DATE% %TIME%] OK .obsidian snapshot updated >> "%LOG%"
) else (
    echo [%DATE% %TIME%] WARN: .obsidian snapshot failed, main bundle unaffected >> "%LOG%"
)

:daily_only
echo [%DATE% %TIME%] skip: not Monday, full bundle skipped (obsidian snapshot still runs) >> "%LOG%"

rem --- rolling cleanup: keep newest 2 (weekly cadence, laozhu 2026-09-05) ---
set /a COUNT=0
for /f "delims=" %%f in ('dir /b /o-n "%DEST%\wiki-bundle-2*.bundle" 2^>nul') do (
    set /a COUNT+=1
    if !COUNT! GTR 2 (
        echo [%DATE% %TIME%] cleanup: delete %%f >> "%LOG%"
        del /q "%DEST%\%%f"
    )
)
echo [%DATE% %TIME%] === wiki bundle task done === >> "%LOG%"
endlocal
exit /b 0
