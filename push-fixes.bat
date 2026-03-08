@echo off
echo ========================================
echo Pushing Deployment Fixes to GitHub
echo ========================================
echo.

echo Cleaning up any stuck processes...
taskkill /F /IM vim.exe 2>nul
taskkill /F /IM vi.exe 2>nul

echo.
echo Adding fixes...
git add requirements.txt runtime.txt app_no_aws.py

echo.
echo Committing...
git commit -m "Fix deployment: Remove Pillow dependency, use Python 3.11"

echo.
echo Pushing to GitHub...
git push origin main

echo.
echo ========================================
echo Done! Render will auto-redeploy.
echo Check your Render dashboard in 2-3 minutes.
echo ========================================
pause
