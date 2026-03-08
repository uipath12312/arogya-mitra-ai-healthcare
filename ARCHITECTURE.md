# AROGYA-MITRA System Architecture

## Overview
AROGYA-MITRA uses a serverless, multi-agent AI architecture on AWS to provide intelligent healthcare analysis and recommendations.

## Architecture Components

### Frontend Layer
- HTML/CSS/JavaScript web interface
- Responsive design for mobile and desktop
- File upload with drag-and-drop support
- Real-time results display

### API Layer
- AWS API Gateway (REST API)
- Request validation and throttling
- CORS enabled for web access
- Authentication via API keys

### Processing Layer
- AWS Lambda (Serverless compute)
- Python 3.9 runtime
- Auto-scaling based on demand
- 60-second timeout for analysis

### AI/ML Layer
- Amazon Bedrock (Claude AI)
- Medical document analysis
- Diagnosis extraction
- Treatment recommendation

### Data Layer
- Amazon S3 (Document storage)
- Amazon DynamoDB (Hospital database)
- Encrypted at rest
- Versioning enabled

### Multi-Agent System

#### Agent 1: Document Analyzer
- Extracts text from PDFs/images
- Uses Bedrock AI for medical entity recognition
- Identifies diagnosis, treatment, severity

#### Agent 2: Hospital Comparator
- Queries hospital database
- Compares costs across facilities
- Ranks by affordability and quality
- Considers success rates and reviews

#### Agent 3: Scheme Detector
- Checks government scheme eligibility
- Matches patient profile with criteria
- Calculates potential savings
- Provides application guidance

#### Agent 4: Recommendation Engine
- Synthesizes insights from all agents
- Generates personalized recommendations
- Prioritizes affordable options
- Suggests alternative treatments

## Data Flow

1. User uploads medical document
2. Document stored in S3
3. Lambda triggered via API Gateway
4. Document Analyzer extracts diagnosis
5. Hospital Comparator finds treatment options
6. Scheme Detector checks eligibility
7. Recommendation Engine synthesizes results
8. Results returned to user interface

## Security
- IAM roles for service access
- S3 bucket encryption
- API Gateway authentication
- HIPAA-compliant data handling
- No PII stored permanently

## Scalability
- Serverless auto-scaling
- DynamoDB on-demand capacity
- CloudFront CDN for frontend
- Multi-region deployment ready

## Cost Optimization
- Lambda pay-per-use pricing
- S3 lifecycle policies
- DynamoDB auto-scaling
- Bedrock usage optimization
