@echo off
title NIT Jalandhar Sem 3 - End-Term Study Portal & PDF Reader
color 0b
echo =========================================================================
echo    NIT JALANDHAR B.TECH SEMESTER 3 - STUDY PORTAL & PDF READER
echo =========================================================================
echo.
echo Starting study portal on http://localhost:8000 ...
echo.
cd /d "%~dp0"
start "" http://localhost:8000
python -m uvicorn server:app --app-dir web --host 0.0.0.0 --port 8000
pause
