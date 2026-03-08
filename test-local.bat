@echo off
echo ========================================
echo Testing AROGYA-MITRA Locally
echo ========================================
echo.

echo Installing dependencies...
pip install flask python-dotenv gunicorn

echo.
echo ========================================
echo Starting AROGYA-MITRA Demo Server
echo ========================================
echo.
echo Server will start at: http://localhost:5000
echo.
echo Features:
echo - Upload any PDF/image file to test
echo - Mock AI analysis (no AWS needed)
echo - Hospital comparison with realistic data
echo - Government scheme eligibility
echo - Cost savings recommendations
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app_no_aws.py
