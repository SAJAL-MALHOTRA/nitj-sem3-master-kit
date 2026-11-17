@echo off
title NIT Jalandhar Sem 3 - NotebookLM Study Workspace
color 0b
echo =========================================================================
echo    NIT JALANDHAR B.TECH SEMESTER 3 - AI STUDY NOTEBOOK (NOTEBOOKLM)
echo =========================================================================
echo.
echo Starting clean NotebookLM web server on http://localhost:8000 ...
echo.
cd /d "%~dp0"
start "" http://localhost:8000
python -m uvicorn server:app --app-dir web --host 0.0.0.0 --port 8000
pause
