# AROGYA-MITRA System Architecture

## Overview
AROGYA-MITRA is an AI-powered healthcare cost comparison system built on AWS serverless architecture for scalability and cost-efficiency.

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                    (HTML/CSS/JavaScript)                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API GATEWAY (REST)                         │
│                    HTTPS Endpoints + CORS                       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AWS LAMBDA FUNCTION                        │
│                    (Python Flask Handler)                       │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   Application Logic                       │  │
│  │  • Document Upload Handler                               │  │
│  │  • Medical Analysis Orchestrator                         │  │
│  │  • Hospital Recommendation Engine                        │  │
│  │  • Scheme Eligibility Checker                            │  │
│  └──────────────────────────────────────────────────────────┘  │
└───────┬──────────────────┬──────────────────┬──────────────────┘
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────────┐
│  Amazon S3   │  │   Amazon     │  │  Amazon Bedrock  │
│   Bucket     │  │  DynamoDB    │  │   (Claude AI)    │
│              │  │              │  │                  │
│ • Medical    │  │ • Hospital   │  │ • Document       │
│   Documents  │  │   Database   │  │   Analysis       │
│ • Reports    │  │ • Procedures │  │ • Diagnosis      │
│ • Images     │  │ • Costs      │  │   Extraction     │
│              │  │ • Ratings    │  │ • Scheme Check   │
└──────────────┘  └──────────────┘  └──────────────────┘
```

## Component Details

### 1. Frontend Layer
- **Technology**: HTML5, CSS3, Vanilla JavaScript
- **Features**:
  - Responsive design for mobile and desktop
  - File upload with drag-and-drop
  - Real-time form validation
  - Dynamic results rendering
  - No authentication required

### 2. API Gateway
- **Type**: REST API
- **Features**:
  - HTTPS endpoints
  - CORS enabled
  - Request throttling
  - API key management (optional)
- **Endpoints**:
  - `GET /api/cities` - Get available cities
  - `POST /api/analyze` - Analyze medical document

### 3. Lambda Function
- **Runtime**: Python 3.11
- **Memory**: 512 MB
- **Timeout**: 30 seconds
- **Services**:
  - `BedrockService`: AI document analysis
  - `HospitalService`: Hospital data queries
  - `S3Service`: Document storage

### 4. Amazon Bedrock (AI Engine)
- **Model**: Claude 3 Sonnet
- **Capabilities**:
  - Medical document OCR and analysis
  - Diagnosis extraction
  - Procedure recommendation
  - Government scheme eligibility detection
  - Natural language understanding

### 5. Amazon S3
- **Purpose**: Medical document storage
- **Features**:
  - Versioning enabled
  - 90-day lifecycle policy
  - Server-side encryption
  - Private access only

### 6. Amazon DynamoDB
- **Table**: hospitals
- **Schema**:
  ```
  hospital_id (PK)
  city (GSI)
  name
  type (government/private)
  rating
  success_rate
  procedures (map)
  specialties (list)
  government_schemes (boolean)
  ```

## Data Flow

### Document Analysis Flow
```
1. User uploads document/enters problem
   ↓
2. Frontend sends multipart form to API Gateway
   ↓
3. Lambda receives request
   ↓
4. Document uploaded to S3
   ↓
5. Bedrock analyzes document
   ↓
6. Extract: diagnosis, procedures, severity
   ↓
7. Query DynamoDB for hospitals in selected city
   ↓
8. Calculate costs for each hospital
   ↓
9. Check government scheme eligibility
   ↓
10. Sort hospitals by cost
   ↓
11. Return recommendations to frontend
   ↓
12. Display results with cost comparison
```

## Security Architecture

### Data Protection
- All data encrypted in transit (HTTPS/TLS)
- S3 server-side encryption at rest
- DynamoDB encryption enabled
- No PII stored permanently

### Access Control
- IAM roles with least privilege
- Lambda execution role with specific permissions
- S3 bucket policies for private access
- API Gateway throttling

### Compliance
- HIPAA-ready architecture (with BAA)
- Data retention policies
- Audit logging via CloudWatch

## Scalability

### Auto-Scaling Components
- **Lambda**: Automatic scaling (1-1000 concurrent executions)
- **DynamoDB**: On-demand capacity mode
- **API Gateway**: Handles millions of requests
- **S3**: Unlimited storage

### Performance Optimization
- DynamoDB GSI for fast city queries
- Lambda warm-up strategies
- CloudFront CDN for static assets (optional)
- Response caching

## Cost Structure

### Pay-Per-Use Model
```
Component          | Free Tier        | Cost After Free Tier
-------------------|------------------|---------------------
Lambda             | 1M requests/mo   | ₹0.0000166/request
DynamoDB           | 25GB + 25 RCU    | ₹0.25/GB + ₹0.00013/RCU
S3                 | 5GB              | ₹1.84/GB
Bedrock            | None             | ₹0.003/1K tokens
API Gateway        | 1M requests/mo   | ₹0.0035/request
```

### Estimated Monthly Costs
- **100 users**: ₹500-₹2,000
- **1,000 users**: ₹5,000-₹15,000
- **10,000 users**: ₹15,000-₹30,000

## Monitoring & Logging

### CloudWatch Integration
- Lambda execution logs
- API Gateway access logs
- DynamoDB metrics
- Custom application metrics

### Alerts
- Lambda errors
- API Gateway 5xx errors
- DynamoDB throttling
- Cost anomalies

## Disaster Recovery

### Backup Strategy
- S3 versioning enabled
- DynamoDB point-in-time recovery
- CloudFormation for infrastructure as code
- Multi-region deployment (optional)

### RTO/RPO
- Recovery Time Objective: < 1 hour
- Recovery Point Objective: < 5 minutes

## Future Enhancements

1. **Multi-language Support**: Hindi, Tamil, Telugu
2. **Real-time Chat**: AI health assistant
3. **Appointment Booking**: Direct hospital integration
4. **Price Negotiation**: AI-powered cost optimization
5. **Telemedicine**: Video consultation integration
6. **Mobile Apps**: iOS and Android native apps
7. **Analytics Dashboard**: Admin panel for insights
