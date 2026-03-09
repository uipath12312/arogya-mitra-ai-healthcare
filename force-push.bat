@echo off
echo ========================================
echo AROGYA-MITRA - Force Push to GitHub
echo ========================================
echo.
echo WARNING: This will overwrite remote repository
echo with your local version (recommended for fresh start)
echo.
pause

echo.
echo Adding all files...
git add .

echo.
echo Committing changes...
git commit -m "Complete AROGYA-MITRA: Free AI healthcare app with Groq integration"

echo.
echo Force pushing to GitHub...
git push origin main --force

echo.
echo ========================================
echo Done! Repository updated successfully!
echo ========================================
echo.
echo Check: https://github.com/uipath12312/arogya-mitra-ai-healthcare
echo.
echo Next: Deploy on Render (https://render.com)
echo.
pause
