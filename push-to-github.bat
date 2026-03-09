@echo off
echo ========================================
echo AROGYA-MITRA - Push to GitHub
echo ========================================
echo.

echo Adding all files...
git add .

echo.
echo Committing changes...
git commit -m "Update: Free AI integration with Groq, no AWS dependencies"

echo.
echo Pushing to GitHub repository...
git push origin main

echo.
echo ========================================
echo Done! Check: https://github.com/uipath12312/arogya-mitra-ai-healthcare
echo ========================================
echo.
echo Next steps:
echo 1. Visit the GitHub repository
echo 2. Deploy on Render: https://render.com
echo 3. See DEPLOYMENT.md for instructions
echo.
pause
