@echo off
echo ========================================
echo AROGYA-MITRA Deployment Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/6] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/6] Checking AWS CLI...
aws --version >nul 2>&1
if errorlevel 1 (
    echo WARNING: AWS CLI not found. Install from https://aws.amazon.com/cli/
    echo Skipping AWS deployment steps...
    goto :local_deploy
)

echo.
echo [3/6] Creating S3 bucket for documents...
set BUCKET_NAME=arogya-mitra-documents-%RANDOM%
aws s3 mb s3://%BUCKET_NAME% --region ap-south-1 2>nul
if errorlevel 1 (
    echo Note: Bucket might already exist or AWS not configured
)

echo.
echo [4/6] Creating DynamoDB table...
aws dynamodb create-table ^
    --table-name arogya-mitra-hospitals ^
    --attribute-definitions AttributeName=hospital_id,AttributeType=S ^
    --key-schema AttributeName=hospital_id,KeyType=HASH ^
    --billing-mode PAY_PER_REQUEST ^
    --region ap-south-1 2>nul
if errorlevel 1 (
    echo Note: Table might already exist
)

echo.
echo [5/6] Packaging Lambda function...
if exist package rmdir /s /q package
mkdir package
pip install -r requirements.txt -t package
xcopy /E /I /Y services package\services
copy lambda_function.py package\
cd package
powershell -command "Compress-Archive -Path * -DestinationPath ..\lambda_deployment.zip -Force"
cd ..

echo.
echo [6/6] Lambda deployment package created: lambda_deployment.zip
echo.
echo To deploy Lambda function, run:
echo aws lambda create-function --function-name arogya-mitra-analyzer --runtime python3.9 --role YOUR_ROLE_ARN --handler lambda_function.lambda_handler --zip-file fileb://lambda_deployment.zip --timeout 60 --memory-size 512 --region ap-south-1
echo.
goto :end

:local_deploy
echo.
echo ========================================
echo Starting Local Development Server
echo ========================================
echo.
echo Creating .env file if not exists...
if not exist .env (
    copy .env.example .env
    echo Please edit .env file with your AWS credentials
)

echo.
echo Starting Flask application...
echo Access the application at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py

:end
echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Configure AWS credentials in .env file
echo 2. Deploy Lambda function using AWS CLI
echo 3. Setup API Gateway
echo 4. Update frontend with API endpoint
echo.
echo For detailed instructions, see DEPLOYMENT.md
echo.
pause
