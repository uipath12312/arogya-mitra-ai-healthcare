@echo off
echo ========================================
echo Force Push to GitHub (Clean Slate)
echo ========================================
echo.

echo WARNING: This will overwrite remote repository!
echo Press Ctrl+C to cancel, or
pause

echo.
echo Cleaning up...
taskkill /F /IM vim.exe 2>nul
taskkill /F /IM vi.exe 2>nul

REM Remove merge state
del /F /Q .git\MERGE_HEAD 2>nul
del /F /Q .git\MERGE_MODE 2>nul
del /F /Q .git\MERGE_MSG 2>nul

echo.
echo Resetting to clean state...
git reset --hard HEAD

echo.
echo Adding all files...
git add .

echo.
echo Committing...
git commit -m "Complete AROGYA-MITRA AI Healthcare System"

echo.
echo Force pushing to GitHub...
git push -u origin main --force

echo.
echo ========================================
echo Done! Check your repository:
echo https://github.com/uipath12312/arogya-mitra-ai-healthcare
echo ========================================
pause
