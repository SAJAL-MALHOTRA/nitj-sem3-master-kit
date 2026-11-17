@echo off
title NIT Jalandhar Sem 3 - Live Public Sharing Link
color 0a
echo =========================================================================
echo    NIT JALANDHAR B.TECH SEMESTER 3 - LIVE PUBLIC SHARING LINK
echo =========================================================================
echo.
echo Starting study portal and creating live public HTTPS link...
echo (You can open this link on your phone, tablet, or share with classmates)
echo.
cd /d "%~dp0"
start "" cmd /c "python -m uvicorn server:app --app-dir web --host 0.0.0.0 --port 8000"
echo Waiting 3 seconds for local server to initialize...
timeout /t 3 >nul
echo Generating secure public HTTPS link...
echo.
ssh -o StrictHostKeyChecking=no -p 443 -R0:127.0.0.1:8000 a.pinggy.io
pause
