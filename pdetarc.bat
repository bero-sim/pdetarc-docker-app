@echo off
rem https://github.com/bero-sim/pdetarc-docker-app/blob/main/pdetarc.bat
setlocal enabledelayedexpansion

echo ==== PDETARC DOCKER DROPLET START ====

set INPUT=%~1

if "%INPUT%"=="" (
    echo [ERROR] No input provided
    pause
    exit /b
)

for %%I in ("%INPUT%") do (
    set "DIR=%%~dpI"
    set "NAME=%%~nxI"
)

if "!DIR:~-1!"=="\" set "DIR=!DIR:~0,-1!"

echo Input: !INPUT!
echo Dir  : !DIR!
echo Name : !NAME!

echo Running Docker...

docker run --rm ^
  -v "!DIR!":/work ^
  -w /work ^
  pdetarc ^
  "!NAME!"

echo.
echo ==== RETURN CODE: %ERRORLEVEL% ====
echo ==== PDETARC DOCKER DROPLET END ====
pause
