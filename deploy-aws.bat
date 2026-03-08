@echo off
echo ========================================
echo AROGYA-MITRA AWS Deployment
echo ========================================
echo.

REM Check AWS CLI
aws --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: AWS CLI not installed!
    echo Install from: https://aws.amazon.com/cli/
    pause
    exit /b 1
)

echo Checking AWS credentials...
aws sts get-caller-identity >nul 2>&1
if errorlevel 1 (
    echo ERROR: AWS credentials not configured!
    echo Run: aws configure
    pause
    exit /b 1
)

echo.
set /p BUCKET_NAME="Enter S3 bucket name (e.g., arogya-mitra-docs-123): "
set /p TABLE_NAME="Enter DynamoDB table name (default: arogya-mitra-hospitals): "
if "%TABLE_NAME%"=="" set TABLE_NAME=arogya-mitra-hospitals

echo.
echo [1/5] Creating S3 bucket: %BUCKET_NAME%
aws s3 mb s3://%BUCKET_NAME% --region ap-south-1
if errorlevel 1 (
    echo Warning: Bucket creation failed - might already exist
)

echo.
echo [2/5] Enabling S3 bucket encryption...
aws s3api put-bucket-encryption ^
    --bucket %BUCKET_NAME% ^
    --server-side-encryption-configuration "{\"Rules\":[{\"ApplyServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"AES256\"}}]}"

echo.
echo [3/5] Creating DynamoDB table: %TABLE_NAME%
aws dynamodb create-table ^
    --table-name %TABLE_NAME% ^
    --attribute-definitions AttributeName=hospital_id,AttributeType=S ^
    --key-schema AttributeName=hospital_id,KeyType=HASH ^
    --billing-mode PAY_PER_REQUEST ^
    --region ap-south-1
if errorlevel 1 (
    echo Warning: Table creation failed - might already exist
)

echo.
echo [4/5] Packaging Lambda function...
if exist package rmdir /s /q package
if exist lambda_deployment.zip del lambda_deployment.zip

mkdir package
pip install -r requirements.txt -t package --quiet
xcopy /E /I /Y services package\services >nul
copy lambda_function.py package\ >nul

cd package
powershell -command "Compress-Archive -Path * -DestinationPath ..\lambda_deployment.zip -Force"
cd ..
rmdir /s /q package

echo Lambda package created: lambda_deployment.zip

echo.
echo [5/5] Deployment package ready!
echo.
echo ========================================
echo Manual Steps Required:
echo ========================================
echo.
echo 1. Create IAM role for Lambda with these policies:
echo    - AWSLambdaBasicExecutionRole
echo    - AmazonS3FullAccess
echo    - AmazonDynamoDBFullAccess
echo    - AmazonBedrockFullAccess
echo.
echo 2. Deploy Lambda function:
echo    aws lambda create-function \
echo      --function-name arogya-mitra-analyzer \
echo      --runtime python3.9 \
echo      --role arn:aws:iam::YOUR_ACCOUNT:role/YOUR_LAMBDA_ROLE \
echo      --handler lambda_function.lambda_handler \
echo      --zip-file fileb://lambda_deployment.zip \
echo      --timeout 60 \
echo      --memory-size 512 \
echo      --region ap-south-1 \
echo      --environment Variables={S3_BUCKET_NAME=%BUCKET_NAME%,DYNAMODB_TABLE_NAME=%TABLE_NAME%}
echo.
echo 3. Create API Gateway REST API
echo 4. Connect API Gateway to Lambda function
echo 5. Deploy API and note the endpoint URL
echo.
echo For detailed instructions, see DEPLOYMENT.md
echo.
pause
