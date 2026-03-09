# AROGYA-MITRA Testing Guide

## Testing Overview

This guide covers testing strategies for AROGYA-MITRA at different stages of development.

---

## Local Testing (Mock Mode)

### Prerequisites
```bash
pip install -r requirements.txt
```

### Test Scenarios

#### Test 1: Basic Text Input
**Objective**: Verify text-based problem analysis

**Steps**:
1. Run `python app.py`
2. Open http://localhost:5000
3. Select city: "Mumbai"
4. Enter problem: "Experiencing chest pain and shortness of breath"
5. Click "Analyze & Get Recommendations"

**Expected Results**:
- ✅ Medical analysis displays diagnosis
- ✅ Procedures list shows: Blood Test, X-Ray, ECG
- ✅ Severity level shown
- ✅ 4 hospitals displayed
- ✅ Hospitals sorted by cost (cheapest first)
- ✅ Government hospital shows lowest price
- ✅ Scheme eligibility shows Ayushman Bharat

---

#### Test 2: Document Upload
**Objective**: Verify file upload functionality

**Steps**:
1. Select city: "Delhi"
2. Upload a PDF/image file (< 16MB)
3. Optionally add description
4. Submit form

**Expected Results**:
- ✅ File uploads successfully
- ✅ Analysis completes
- ✅ Results display correctly
- ✅ No errors in console

---

#### Test 3: City Selection
**Objective**: Verify city filtering works

**Steps**:
1. Select different cities: Mumbai, Delhi, Bangalore
2. Submit same problem for each
3. Compare results

**Expected Results**:
- ✅ Hospital names include city name
- ✅ Different hospitals for different cities
- ✅ Costs may vary by city

---

#### Test 4: Error Handling
**Objective**: Verify error messages display correctly

**Test Cases**:

a) No city selected:
- Leave city dropdown empty
- Submit form
- Expected: "City is required" error

b) No input provided:
- Select city only
- Leave problem and file empty
- Submit form
- Expected: "Please provide medical document or problem description" error

c) File too large:
- Upload file > 16MB
- Expected: Browser prevents upload or shows error

---

#### Test 5: UI Responsiveness
**Objective**: Verify responsive design

**Steps**:
1. Open app in browser
2. Resize window to different sizes:
   - Desktop (1920x1080)
   - Tablet (768x1024)
   - Mobile (375x667)

**Expected Results**:
- ✅ Layout adapts to screen size
- ✅ All elements visible and usable
- ✅ No horizontal scrolling
- ✅ Buttons and forms accessible

---

#### Test 6: Multiple Submissions
**Objective**: Verify app handles multiple requests

**Steps**:
1. Submit first analysis
2. Wait for results
3. Change city and problem
4. Submit again
5. Repeat 3-5 times

**Expected Results**:
- ✅ Each submission works independently
- ✅ Previous results cleared
- ✅ New results display correctly
- ✅ No memory leaks or slowdowns

---

## API Testing

### Using cURL

#### Test Cities Endpoint
```bash
curl http://localhost:5000/api/cities
```

**Expected Response**:
```json
{
  "cities": [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Kolkata",
    "Hyderabad",
    "Pune",
    "Ahmedabad",
    "Jaipur",
    "Lucknow"
  ]
}
```

---

#### Test Analysis Endpoint
```bash
curl -X POST http://localhost:5000/api/analyze \
  -F "city=Mumbai" \
  -F "problem_text=Chest pain and breathing difficulty"
```

**Expected Response**:
```json
{
  "medical_info": {
    "diagnosis": "General Health Checkup Required",
    "procedures": ["Blood Test", "X-Ray", "ECG"],
    "severity": "moderate",
    "urgency": "routine",
    "summary": "Routine medical examination recommended"
  },
  "recommendations": [
    {
      "name": "Mumbai Government Hospital",
      "city": "Mumbai",
      "rating": 3.8,
      "success_rate": 85,
      "total_cost": 630,
      "procedures": [...]
    }
  ],
  "scheme_eligibility": {
    "ayushman_bharat": {
      "eligible": true,
      "coverage": "Up to ₹5 lakh per family per year"
    }
  }
}
```

---

### Using Postman

1. **Import Collection**:
   - Create new collection "AROGYA-MITRA"
   - Add requests for each endpoint

2. **Test GET /api/cities**:
   - Method: GET
   - URL: http://localhost:5000/api/cities
   - Expected: 200 OK with cities array

3. **Test POST /api/analyze**:
   - Method: POST
   - URL: http://localhost:5000/api/analyze
   - Body: form-data
     - city: Mumbai
     - problem_text: Test problem
   - Expected: 200 OK with analysis results

---

## AWS Integration Testing

### Prerequisites
```bash
# Configure AWS credentials
aws configure

# Create .env file
cp .env.example .env
# Add your AWS credentials to .env
```

### Test S3 Integration

**Enable S3**:
```python
# In services/s3_service.py
self._use_mock = False
```

**Test Upload**:
1. Upload document through UI
2. Check S3 bucket:
```bash
aws s3 ls s3://arogya-mitra-documents/documents/
```

**Expected**: File appears in S3 bucket

---

### Test DynamoDB Integration

**Setup Database**:
```bash
python deployment/setup_dynamodb.py
```

**Enable DynamoDB**:
```python
# In services/hospital_service.py
self._use_mock = False
```

**Test Query**:
```bash
aws dynamodb scan --table-name hospitals --limit 5
```

**Expected**: Hospital records returned

---

### Test Bedrock Integration

**Enable Bedrock**:
```python
# In services/bedrock_service.py
# Remove try-except to use real Bedrock
```

**Test Analysis**:
1. Submit problem through UI
2. Check CloudWatch logs:
```bash
aws logs tail /aws/lambda/arogya-mitra-dev --follow
```

**Expected**: Bedrock API calls succeed

---

## Performance Testing

### Load Testing with Apache Bench

```bash
# Install Apache Bench
# Windows: Download from Apache website
# Linux: sudo apt-get install apache2-utils

# Test 100 requests, 10 concurrent
ab -n 100 -c 10 http://localhost:5000/
```

**Expected Metrics**:
- Requests per second: > 50
- Time per request: < 200ms
- Failed requests: 0

---

### Stress Testing

```bash
# Test 1000 requests, 50 concurrent
ab -n 1000 -c 50 -p data.json -T application/json \
  http://localhost:5000/api/analyze
```

**Monitor**:
- CPU usage
- Memory usage
- Response times
- Error rates

---

## Security Testing

### Test 1: File Upload Validation

**Test Cases**:
- Upload .exe file → Should reject
- Upload 20MB file → Should reject
- Upload malicious PDF → Should handle safely

---

### Test 2: SQL Injection

**Test Input**:
```
city: Mumbai'; DROP TABLE hospitals; --
```

**Expected**: Input sanitized, no SQL execution

---

### Test 3: XSS Prevention

**Test Input**:
```
problem_text: <script>alert('XSS')</script>
```

**Expected**: Script tags escaped, not executed

---

### Test 4: CORS Headers

```bash
curl -H "Origin: http://evil.com" \
  -H "Access-Control-Request-Method: POST" \
  -X OPTIONS http://localhost:5000/api/analyze
```

**Expected**: CORS headers present and correct

---

## Deployment Testing

### Test Lambda Deployment

```bash
# Deploy to AWS
sam build -t deployment/cloudformation.yaml
sam deploy --guided

# Test Lambda function
aws lambda invoke \
  --function-name arogya-mitra-dev \
  --payload '{"httpMethod":"GET","path":"/api/cities"}' \
  response.json

cat response.json
```

**Expected**: Lambda executes successfully

---

### Test API Gateway

```bash
# Get API URL from CloudFormation outputs
API_URL=$(aws cloudformation describe-stacks \
  --stack-name arogya-mitra \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' \
  --output text)

# Test endpoint
curl $API_URL/api/cities
```

**Expected**: API Gateway returns response

---

## Monitoring & Logging

### CloudWatch Logs

```bash
# View Lambda logs
aws logs tail /aws/lambda/arogya-mitra-dev --follow

# Filter errors
aws logs filter-log-events \
  --log-group-name /aws/lambda/arogya-mitra-dev \
  --filter-pattern "ERROR"
```

---

### CloudWatch Metrics

```bash
# Get Lambda invocations
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Invocations \
  --dimensions Name=FunctionName,Value=arogya-mitra-dev \
  --start-time 2026-03-09T00:00:00Z \
  --end-time 2026-03-09T23:59:59Z \
  --period 3600 \
  --statistics Sum
```

---

## Automated Testing

### Unit Tests (Future)

```python
# tests/test_bedrock_service.py
import unittest
from services.bedrock_service import BedrockService

class TestBedrockService(unittest.TestCase):
    def setUp(self):
        self.service = BedrockService()
    
    def test_analyze_text(self):
        result = self.service.analyze_text("Chest pain")
        self.assertIn('diagnosis', result)
        self.assertIn('procedures', result)
    
    def test_check_scheme_eligibility(self):
        medical_info = {
            'diagnosis': 'Test',
            'procedures': ['Blood Test']
        }
        result = self.service.check_scheme_eligibility(medical_info)
        self.assertIn('ayushman_bharat', result)

if __name__ == '__main__':
    unittest.main()
```

---

### Integration Tests (Future)

```python
# tests/test_api.py
import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_get_cities(self):
        response = self.app.get('/api/cities')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('cities', data)
    
    def test_analyze_without_city(self):
        response = self.app.post('/api/analyze', data={
            'problem_text': 'Test'
        })
        self.assertEqual(response.status_code, 400)
```

---

## Test Checklist

### Pre-Deployment
- [ ] All local tests pass
- [ ] API endpoints work correctly
- [ ] Error handling works
- [ ] UI is responsive
- [ ] File uploads work
- [ ] Mock data displays correctly

### AWS Integration
- [ ] S3 uploads work
- [ ] DynamoDB queries work
- [ ] Bedrock analysis works
- [ ] Lambda deploys successfully
- [ ] API Gateway accessible
- [ ] CloudWatch logging enabled

### Production Readiness
- [ ] Load testing passed
- [ ] Security tests passed
- [ ] Monitoring configured
- [ ] Backup strategy in place
- [ ] Cost alerts set up
- [ ] Documentation complete

---

## Troubleshooting

### Issue: Tests fail locally
**Solution**: Check Python version (3.9+), reinstall dependencies

### Issue: AWS services not working
**Solution**: Verify credentials, check IAM permissions, enable services

### Issue: Slow response times
**Solution**: Check network, optimize queries, increase Lambda memory

### Issue: High costs
**Solution**: Review CloudWatch metrics, optimize Bedrock usage, use caching

---

## Test Data

### Sample Medical Problems
1. "Experiencing chest pain and shortness of breath"
2. "Severe headache and dizziness for 3 days"
3. "Persistent cough and fever"
4. "Abdominal pain and nausea"
5. "Joint pain and swelling"

### Sample Cities
- Mumbai
- Delhi
- Bangalore
- Chennai
- Kolkata

### Expected Cost Ranges
- Government Hospital: ₹500-₹1,000
- Private Hospital: ₹2,000-₹5,000
- Premium Hospital: ₹5,000-₹10,000

---

## Continuous Testing

### Daily Checks
- [ ] App loads correctly
- [ ] API endpoints respond
- [ ] No errors in logs

### Weekly Checks
- [ ] Performance metrics
- [ ] Cost analysis
- [ ] User feedback review

### Monthly Checks
- [ ] Security audit
- [ ] Dependency updates
- [ ] Feature testing

---

## Success Criteria

✅ **Functional**: All features work as expected
✅ **Performance**: Response time < 3 seconds
✅ **Reliability**: 99.9% uptime
✅ **Security**: No vulnerabilities found
✅ **Scalability**: Handles 1000+ concurrent users
✅ **Cost**: Within budget estimates

---

**Testing is crucial for a production-ready application. Follow this guide to ensure AROGYA-MITRA delivers reliable, secure, and performant healthcare recommendations!**
