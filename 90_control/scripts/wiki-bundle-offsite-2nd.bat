@echo off
rem ============================================================
rem #592 R1 offsite backup step 2 (wiki resilience trio)
rem Copies newest wiki bundle to Nutstore sync dir (= offsite copy
rem via Nutstore cloud upload). Rolling keep 3. Independent log,
rem failure NEVER blocks the main bundle backup (step 2 only).
rem Called by: 90_control/scripts/wiki-bundle-backup.bat (after OK)
rem Standalone runnable: wiki-bundle-offsite-2nd.bat
rem Iron rule (#589): wiki itself is NEVER added to Nutstore sync.
rem ============================================================
setlocal enabledelayedexpansion
set "SRC=D:\KDO-memory"
set "DEST=C:\Users\Administrator\Nutstore\1\我的坚果云\kdo-backup"
set "LOG=%SRC%\wiki-bundle-offsite.log"

rem --- ISO date stamp (locale-independent, avoid cmd for /f quote pitfall) ---
powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss" > "%TEMP%\wiki-offsite-ts.txt" 2>nul
set /p TS=<"%TEMP%\wiki-offsite-ts.txt"
del /q "%TEMP%\wiki-offsite-ts.txt" >nul 2>&1

echo [%TS%] === offsite copy start === >> "%LOG%"

rem --- find newest bundle by name (date-suffixed, dir /o-n = newest first) ---
set "NEWEST="
for /f "delims=" %%f in ('dir /b /o-n "%SRC%\wiki-bundle-2*.bundle" 2^>nul') do (
    if not defined NEWEST set "NEWEST=%%f"
)
if not defined NEWEST (
    echo [%TS%] ERROR: no wiki-bundle-2*.bundle found in %SRC% >> "%LOG%"
    echo FAIL > "%SRC%\wiki-bundle-offsite.last-result.txt"
    exit /b 1
)

rem --- copy with size check (copy then compare bytes) ---
if not exist "%DEST%" mkdir "%DEST%" >> "%LOG%" 2>&1
echo [%TS%] copying %NEWEST% ... >> "%LOG%"
copy /y "%SRC%\%NEWEST%" "%DEST%\%NEWEST%" >> "%LOG%" 2>&1
if errorlevel 1 (
    echo [%TS%] ERROR: copy failed >> "%LOG%"
    echo FAIL > "%SRC%\wiki-bundle-offsite.last-result.txt"
    exit /b 1
)

rem --- byte-size sanity check ---
for %%A in ("%SRC%\%NEWEST%") do set "SZSRC=%%~zA"
for %%A in ("%DEST%\%NEWEST%") do set "SZDST=%%~zA"
if not "%SZSRC%"=="%SZDST%" (
    echo [%TS%] ERROR: size mismatch src=%SZSRC% dst=%SZDST% >> "%LOG%"
    echo FAIL > "%SRC%\wiki-bundle-offsite.last-result.txt"
    exit /b 1
)

rem --- rolling cleanup: keep newest 3 in offsite dir ---
set /a COUNT=0
for /f "delims=" %%f in ('dir /b /o-n "%DEST%\wiki-bundle-2*.bundle" 2^>nul') do (
    set /a COUNT+=1
    if !COUNT! GTR 3 (
        echo [%TS%] cleanup: delete %%f >> "%LOG%"
        del /q "%DEST%\%%f"
    )
)

echo [%TS%] OK bundle=%NEWEST% size=%SZDST% >> "%LOG%"
echo OK > "%SRC%\wiki-bundle-offsite.last-result.txt"
echo [%TS%] === offsite copy done === >> "%LOG%"
endlocal
exit /b 0
