# AWS Deployment Guide

## Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured
- SAM CLI installed
- Python 3.11+

## Deployment Steps

### 1. Install AWS SAM CLI
```bash
pip install aws-sam-cli
```

### 2. Configure AWS Credentials
```bash
aws configure
```

### 3. Enable Amazon Bedrock
- Go to AWS Console → Amazon Bedrock
- Request access to Claude models
- Enable model access in your region

### 4. Deploy Infrastructure
```bash
# Build the application
sam build -t deployment/cloudformation.yaml

# Deploy to AWS
sam deploy --guided
```

Follow the prompts:
- Stack Name: arogya-mitra
- AWS Region: us-east-1 (or your preferred region)
- Environment: dev
- Confirm changes: Y
- Allow SAM CLI IAM role creation: Y

### 5. Populate Hospital Data
```bash
python deployment/setup_dynamodb.py
```

### 6. Get API Endpoint
```bash
aws cloudformation describe-stacks --stack-name arogya-mitra --query 'Stacks[0].Outputs'
```

## Local Testing with AWS Services

### 1. Create .env file
```bash
cp .env.example .env
```

### 2. Update .env with AWS credentials
```
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
S3_BUCKET_NAME=arogya-mitra-documents-dev
DYNAMODB_TABLE_NAME=hospitals-dev
```

### 3. Run locally
```bash
python app.py
```

## Cost Optimization

### Free Tier Usage
- Lambda: 1M requests/month free
- DynamoDB: 25GB storage + 25 RCU/WCU free
- S3: 5GB storage free
- Bedrock: Pay per token (no free tier)

### Estimated Monthly Costs
- Prototype (100 users): ₹500-₹2,000
- Small Scale (1000 users): ₹5,000-₹15,000
- Medium Scale (10000 users): ₹15,000-₹30,000

## Monitoring
```bash
# View Lambda logs
aws logs tail /aws/lambda/arogya-mitra-dev --follow

# Check API Gateway metrics
aws cloudwatch get-metric-statistics --namespace AWS/ApiGateway --metric-name Count --dimensions Name=ApiName,Value=arogya-mitra
```

## Cleanup
```bash
# Delete stack
aws cloudformation delete-stack --stack-name arogya-mitra

# Empty and delete S3 bucket
aws s3 rm s3://arogya-mitra-documents-dev --recursive
aws s3 rb s3://arogya-mitra-documents-dev
```
