@echo off
echo ========================================
echo Pushing AROGYA-MITRA to GitHub
echo ========================================
echo.

REM Kill any stuck git processes
taskkill /F /IM vim.exe 2>nul
taskkill /F /IM vi.exe 2>nul
taskkill /F /IM notepad.exe 2>nul

echo Cleaning up stuck merge...
git merge --abort 2>nul

echo.
echo Adding all files...
git add .

echo.
echo Committing changes...
git commit -m "Complete AROGYA-MITRA AI Healthcare System with deployment scripts"

echo.
echo Pulling from remote...
git pull origin main --rebase --no-edit

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo View your repository at:
echo https://github.com/uipath12312/arogya-mitra-ai-healthcare
echo.
pause
