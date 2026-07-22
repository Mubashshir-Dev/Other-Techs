@echo off

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    pause
    exit /b 1
)

:: Install dependencies
if exist "requirements.txt" (
    python -m pip install -r requirements.txt
)

:: Run the application
python main.py

pause