# AROGYA-MITRA Process Flow Diagram

## User Journey Flow

```
START
  │
  ▼
┌─────────────────────────┐
│  User Opens Website     │
│  (No Login Required)    │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Select City            │
│  (Dropdown Menu)        │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  Choose Input Method:               │
│  ┌─────────────┐  ┌──────────────┐ │
│  │ Upload      │  │ Describe     │ │
│  │ Document    │  │ Problem      │ │
│  └─────────────┘  └──────────────┘ │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────┐
│  Submit for Analysis    │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  AI Processing          │
│  (Amazon Bedrock)       │
│  • Extract diagnosis    │
│  • Identify procedures  │
│  • Assess severity      │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Query Hospital DB      │
│  (DynamoDB)             │
│  • Filter by city       │
│  • Get procedure costs  │
│  • Fetch ratings        │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Calculate Total Costs  │
│  • Sum all procedures   │
│  • Apply discounts      │
│  • Sort by price        │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Check Scheme           │
│  Eligibility            │
│  • Ayushman Bharat      │
│  • State schemes        │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Display Results        │
│  • Medical analysis     │
│  • Hospital list        │
│  • Cost comparison      │
│  • Scheme info          │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  User Reviews Options   │
│  • Compare hospitals    │
│  • Check details        │
│  • Contact hospital     │
└───────────┬─────────────┘
            │
            ▼
          END
```

## Detailed Process Flow

### Phase 1: Input Collection
```
User Input
    │
    ├─→ City Selection (Required)
    │   └─→ Validates city availability
    │
    ├─→ Medical Document Upload (Optional)
    │   ├─→ File type validation
    │   ├─→ Size check (max 16MB)
    │   └─→ Upload to S3
    │
    └─→ Problem Description (Optional)
        └─→ Text input validation
```

### Phase 2: AI Analysis
```
Document/Text Input
    │
    ▼
Amazon Bedrock (Claude AI)
    │
    ├─→ Document OCR (if image/PDF)
    │
    ├─→ Natural Language Processing
    │   ├─→ Extract medical terms
    │   ├─→ Identify symptoms
    │   └─→ Recognize conditions
    │
    ├─→ Diagnosis Extraction
    │   └─→ Primary condition identification
    │
    ├─→ Procedure Recommendation
    │   ├─→ Required tests
    │   ├─→ Treatments needed
    │   └─→ Follow-up care
    │
    └─→ Severity Assessment
        ├─→ Mild
        ├─→ Moderate
        └─→ Severe
```

### Phase 3: Hospital Matching
```
Diagnosis + City
    │
    ▼
DynamoDB Query
    │
    ├─→ Filter by city (GSI)
    │
    ├─→ Match specialties
    │
    └─→ Retrieve hospital data
        ├─→ Name & address
        ├─→ Ratings & reviews
        ├─→ Success rates
        ├─→ Procedure costs
        └─→ Scheme acceptance
```

### Phase 4: Cost Calculation
```
For Each Hospital:
    │
    ├─→ Get procedure costs
    │   ├─→ Blood Test: ₹X
    │   ├─→ X-Ray: ₹Y
    │   └─→ Consultation: ₹Z
    │
    ├─→ Calculate total
    │   └─→ Total = X + Y + Z
    │
    ├─→ Apply discounts
    │   └─→ Government hospital: -70%
    │
    └─→ Add to results array
```

### Phase 5: Scheme Eligibility
```
Medical Info + User Context
    │
    ▼
AI Eligibility Check
    │
    ├─→ Ayushman Bharat (PM-JAY)
    │   ├─→ Check condition coverage
    │   ├─→ Verify procedure inclusion
    │   └─→ Calculate coverage amount
    │
    ├─→ State Schemes
    │   └─→ Region-specific programs
    │
    └─→ Generate recommendations
        └─→ How to apply
```

### Phase 6: Results Presentation
```
Sorted Results (Cheapest First)
    │
    ├─→ Medical Analysis Card
    │   ├─→ Diagnosis
    │   ├─→ Procedures
    │   ├─→ Severity
    │   └─→ Summary
    │
    ├─→ Scheme Eligibility Card
    │   ├─→ Eligible schemes
    │   ├─→ Coverage details
    │   └─→ Application steps
    │
    └─→ Hospital Cards (Sorted)
        ├─→ Best Value Badge (1st)
        ├─→ Hospital details
        ├─→ Cost breakdown
        ├─→ Ratings & success rate
        └─→ Contact information
```

## Use Case Diagram

```
                    ┌──────────────┐
                    │    PATIENT   │
                    └──────┬───────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Upload       │  │ Describe     │  │ Select       │
│ Document     │  │ Problem      │  │ City         │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                  │
       └─────────────────┼──────────────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  AROGYA-MITRA   │
                │     SYSTEM      │
                └────────┬────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ AI Analysis  │  │ Hospital     │  │ Scheme       │
│ (Bedrock)    │  │ Comparison   │  │ Check        │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                  │
       └─────────────────┼──────────────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  RECOMMENDATIONS│
                └────────┬────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Cheapest     │  │ Best Rated   │  │ Government   │
│ Hospital     │  │ Hospital     │  │ Schemes      │
└──────────────┘  └──────────────┘  └──────────────┘
```

## Error Handling Flow

```
Error Occurs
    │
    ├─→ Invalid File Type
    │   └─→ Show error: "Please upload PDF, image, or document"
    │
    ├─→ File Too Large
    │   └─→ Show error: "File must be under 16MB"
    │
    ├─→ No City Selected
    │   └─→ Show error: "Please select a city"
    │
    ├─→ AI Analysis Failed
    │   └─→ Use fallback mock data
    │
    ├─→ No Hospitals Found
    │   └─→ Show message: "No hospitals available in this city"
    │
    └─→ Network Error
        └─→ Show error: "Connection failed. Please try again"
```
