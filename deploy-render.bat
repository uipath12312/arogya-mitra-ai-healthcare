@echo off
echo ========================================
echo Deploy AROGYA-MITRA to Render.com
echo ========================================
echo.

echo Step 1: Testing locally first...
echo.
pip install -r requirements.txt
echo.
echo Starting test server at http://localhost:5000
echo Press Ctrl+C after testing to continue deployment
echo.
python app_no_aws.py
echo.

echo Step 2: Push to GitHub
echo.
git add .
git commit -m "Add free hosting configs for Render.com"
git push origin main
echo.

echo ========================================
echo Next Steps:
echo ========================================
echo.
echo 1. Go to: https://render.com
echo 2. Sign up with GitHub (free)
echo 3. Click "New +" then "Web Service"
echo 4. Connect repo: uipath12312/arogya-mitra-ai-healthcare
echo 5. Root Directory: arogya-mitra
echo 6. Build Command: pip install -r requirements.txt
echo 7. Start Command: gunicorn app_no_aws:app
echo 8. Click "Create Web Service"
echo.
echo Your app will be live at: https://arogya-mitra.onrender.com
echo (or similar URL)
echo.
echo See DEPLOY-FREE.md for detailed instructions
echo.
pause
