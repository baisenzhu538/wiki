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

echo [%DATE% %TIME%] === wiki daily bundle start === >> "%LOG%"

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
    echo [%DATE% %TIME%] ERROR: HEAD %WIKIHEAD% not found in bundle heads >> "%LOG%"
    echo FAIL > "%DEST%\wiki-bundle-daily.last-result.txt"
    exit /b 1
)

echo [%DATE% %TIME%] OK bundle=%BUNDLE% HEAD=%WIKIHEAD% >> "%LOG%"
echo OK > "%DEST%\wiki-bundle-daily.last-result.txt"

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

rem --- #592 R1: offsite copy to Nutstore dir (step 2, failure never blocks main) ---
call "C:\Users\Administrator\Desktop\wiki\90_control\scripts\wiki-bundle-offsite-2nd.bat" >> "%LOG%" 2>&1
if errorlevel 1 (
    echo [%DATE% %TIME%] WARN: offsite step2 failed, main backup unaffected >> "%LOG%"
)

rem --- rolling cleanup: keep newest 4 (by date-suffixed name sort; 7->4 per laozhu 2026-09-02, D: 130G only 9.8G left) ---
set /a COUNT=0
for /f "delims=" %%f in ('dir /b /o-n "%DEST%\wiki-bundle-2*.bundle" 2^>nul') do (
    set /a COUNT+=1
    if !COUNT! GTR 4 (
        echo [%DATE% %TIME%] cleanup: delete %%f >> "%LOG%"
        del /q "%DEST%\%%f"
    )
)
echo [%DATE% %TIME%] === wiki daily bundle done === >> "%LOG%"
endlocal
exit /b 0
