# AROGYA-MITRA Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Option 1: Local Development (No AWS Required)

The app works with mock data for immediate testing!

1. **Install Python 3.9+**
   ```bash
   python --version
   ```

2. **Clone and Setup**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Open Browser**
   ```
   http://localhost:5000
   ```

That's it! The app runs with mock data - no AWS credentials needed for testing.

---

## 🧪 Test the Application

### Test Case 1: Text Input
1. Select city: "Mumbai"
2. Enter problem: "Experiencing chest pain and shortness of breath"
3. Click "Analyze & Get Recommendations"
4. View results with hospital recommendations

### Test Case 2: Document Upload
1. Select city: "Delhi"
2. Upload a medical document (PDF/image)
3. Optionally add description
4. Get AI-powered analysis

### Expected Results
- Medical analysis with diagnosis
- 4 hospitals sorted by cost
- Government scheme eligibility
- Detailed cost breakdown

---

## ☁️ Deploy to AWS (Production)

### Prerequisites
- AWS Account
- AWS CLI configured
- Bedrock access enabled

### Quick Deploy
```bash
# Install SAM CLI
pip install aws-sam-cli

# Configure AWS
aws configure

# Deploy
cd deployment
sam build -t cloudformation.yaml
sam deploy --guided
```

Follow the prompts and your app will be live in ~10 minutes!

### Post-Deployment
```bash
# Populate hospital data
python deployment/setup_dynamodb.py

# Get your API URL
aws cloudformation describe-stacks --stack-name arogya-mitra
```

---

## 🔧 Configuration (Optional)

### Enable Free AI Analysis

1. **Get Free Groq API Key**
   - Go to https://console.groq.com/
   - Sign up (free, no credit card)
   - Create API key
   - Copy the key

2. **Add to Environment**
   ```bash
   # Create .env file
   echo "GROQ_API_KEY=your_key_here" > .env
   ```

3. **Restart App**
   ```bash
   python app.py
   ```

**Note**: App works perfectly without API key using intelligent mock data!

---

## 📱 Usage Guide

### For Patients

1. **Select Your City**
   - Choose from dropdown menu
   - More cities coming soon

2. **Provide Medical Information**
   - Option A: Upload medical document
   - Option B: Describe your problem
   - Option C: Both for better analysis

3. **Review Results**
   - Medical analysis summary
   - Government scheme eligibility
   - Hospital recommendations (sorted by cost)

4. **Choose Hospital**
   - Compare costs, ratings, success rates
   - Check government scheme acceptance
   - Contact hospital directly

### For Developers

1. **Customize Hospital Data**
   - Edit `services/hospital_service.py`
   - Modify `_get_mock_hospitals()` method
   - Add more cities and hospitals

2. **Adjust AI Prompts**
   - Edit `services/bedrock_service.py`
   - Customize analysis prompts
   - Fine-tune responses

3. **Modify UI**
   - Edit `templates/index.html`
   - Update `static/style.css`
   - Enhance `static/script.js`

---

## 🐛 Troubleshooting

### Issue: Port 5000 already in use
```bash
# Use different port
python app.py
# Then manually change port in app.py to 8080
```

### Issue: Module not found
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Issue: Want real AI analysis
```bash
# Get free Groq API key
# Visit: https://console.groq.com/
# Add to .env file: GROQ_API_KEY=your_key
```

### Issue: Data folder not created
```bash
# Create manually
mkdir data
# App will auto-populate on first run
```

---

## 📊 Project Structure

```
arogya-mitra/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── services/             # Business logic
│   ├── bedrock_service.py   # AI analysis
│   ├── hospital_service.py  # Hospital data
│   └── s3_service.py        # Document storage
├── templates/            # HTML templates
│   └── index.html
├── static/               # Frontend assets
│   ├── style.css
│   └── script.js
├── deployment/           # AWS deployment
│   ├── cloudformation.yaml
│   ├── lambda_handler.py
│   └── setup_dynamodb.py
└── docs/                 # Documentation
    ├── ARCHITECTURE.md
    ├── FLOW_DIAGRAM.md
    └── FEATURES.md
```

---

## 🎯 Next Steps

1. **Test Locally**: Run with mock data ✅
2. **Get Free AI**: Sign up for Groq API (optional)
3. **Deploy Free**: Push to Render/Railway
4. **Share**: Help patients find affordable care
5. **Contribute**: Add more cities and features

---

## 💡 Tips

- App works great without any API keys
- Free deployment on Render/Railway
- No database setup needed
- No cloud costs
- Perfect for hackathons and demos

---

## 🆘 Need Help?

- Check `DEPLOYMENT.md` for cloud deployment
- See `GITHUB_SETUP.md` for repository setup
- Review `docs/` folder for detailed docs
- Open issue on GitHub

---

## 🎉 Success Checklist

- [ ] App runs locally
- [ ] Can select city
- [ ] Can enter medical problem
- [ ] Results display correctly
- [ ] Hospital costs shown
- [ ] Scheme eligibility works
- [ ] Ready for free deployment

**Congratulations! You're ready to help patients find affordable healthcare!** 🏥

**Deploy for FREE**: See `DEPLOYMENT.md`  
**GitHub Repo**: https://github.com/uipath12312/arogya-mitra-ai-healthcare
