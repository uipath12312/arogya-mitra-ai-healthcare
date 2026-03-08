# AROGYA-MITRA Deployment Guide

## Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured
- Python 3.9+
- Node.js (for frontend deployment)

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file:
```bash
cp .env.example .env
# Edit .env with your AWS credentials
```

3. Run locally:
```bash
python app.py
```

Access at: http://localhost:5000

## AWS Deployment

### 1. Create S3 Bucket for Documents
```bash
aws s3 mb s3://arogya-mitra-documents --region ap-south-1
```

### 2. Create DynamoDB Table
```bash
aws dynamodb create-table \
    --table-name arogya-mitra-hospitals \
    --attribute-definitions AttributeName=hospital_id,AttributeType=S \
    --key-schema AttributeName=hospital_id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --region ap-south-1
```

### 3. Deploy Lambda Function
```bash
# Package dependencies
pip install -r requirements.txt -t package/
cp -r services package/
cp lambda_function.py package/

# Create deployment package
cd package
zip -r ../lambda_deployment.zip .
cd ..

# Deploy to Lambda
aws lambda create-function \
    --function-name arogya-mitra-analyzer \
    --runtime python3.9 \
    --role arn:aws:iam::YOUR_ACCOUNT:role/lambda-execution-role \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda_deployment.zip \
    --timeout 60 \
    --memory-size 512 \
    --region ap-south-1
```

### 4. Setup API Gateway
```bash
# Create REST API
aws apigateway create-rest-api \
    --name arogya-mitra-api \
    --region ap-south-1
```

### 5. Enable Bedrock Access
Ensure your Lambda execution role has permissions for Amazon Bedrock:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": "*"
        }
    ]
}
```

## Cost Estimation

### Prototype Phase (AWS Free Tier)
- Lambda: 1M requests/month free
- S3: 5GB storage free
- DynamoDB: 25GB storage free
- Bedrock: Pay per use (~₹0.50 per analysis)

### Production Deployment
- Lambda: ₹2,000-5,000/month
- S3: ₹500-1,000/month
- DynamoDB: ₹1,000-3,000/month
- Bedrock: ₹5,000-10,000/month
- API Gateway: ₹1,000-2,000/month

Total: ₹10,000-20,000/month for moderate usage

## Monitoring
- CloudWatch Logs for Lambda
- CloudWatch Metrics for API Gateway
- X-Ray for distributed tracing
