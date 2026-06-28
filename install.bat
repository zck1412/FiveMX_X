@echo off
chcp 65001 >nul 2>&1
title Installer - X_x Tool
color 0A

echo ============================================
echo        AUTOMATIC INSTALLER - X_x Tool
echo ============================================
echo.

:: --- Check Python ---
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please download Python from: https://www.python.org/downloads/
    echo IMPORTANT: Check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)
python --version
echo [OK] Python found!
echo.

:: --- Check pip ---
echo [2/4] Checking pip...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] pip is not available!
    echo Run: python -m ensurepip --upgrade
    pause
    exit /b 1
)
echo [OK] pip found!
echo.

:: --- Upgrade pip ---
echo [3/4] Upgrading pip...
python -m pip install --upgrade pip
echo.

:: --- Install requirements ---
echo [4/4] Installing dependencies (this may take a while)...
echo.
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] Some packages may have failed to install.
    echo Try running manually: python -m pip install -r requirements.txt
    echo.
) else (
    echo.
    echo ============================================
    echo    INSTALLATION COMPLETE! 
    echo ============================================
    echo.
    echo To run the program:
    echo    python X_x.py
    echo.
    echo To run with GUI:
    echo    python X_x.py --gui
    echo.
    echo To reconfigure settings:
    echo    python X_x.py setup
    echo.
)
pause
