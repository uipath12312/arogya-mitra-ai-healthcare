@echo off
echo ========================================
echo AROGYA-MITRA Local Development Setup
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Install Python 3.9+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/3] Setting up environment...
if not exist .env (
    copy .env.example .env
    echo Created .env file - please configure your AWS credentials
)

echo.
echo [3/3] Starting development server...
echo.
echo ========================================
echo Server starting at http://localhost:5000
echo Press Ctrl+C to stop
echo ========================================
echo.

python app.py
