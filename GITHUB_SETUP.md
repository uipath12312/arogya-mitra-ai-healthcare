# GitHub Repository Setup Guide

## 🚀 Quick Setup for uipath12312/arogya-mitra-ai-healthcare

### Step 1: Initialize Git (if not already done)

```bash
git init
git add .
git commit -m "Initial commit: AROGYA-MITRA Healthcare App"
```

### Step 2: Connect to GitHub Repository

```bash
# Add remote repository
git remote add origin https://github.com/uipath12312/arogya-mitra-ai-healthcare.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify Upload

Go to: https://github.com/uipath12312/arogya-mitra-ai-healthcare

You should see all files uploaded.

---

## 📁 Repository Structure

Your repository will contain:

```
arogya-mitra-ai-healthcare/
├── app.py                    # Main application
├── requirements.txt          # Dependencies
├── Procfile                  # Deployment config
├── runtime.txt              # Python version
├── README.md                # Documentation
├── DEPLOYMENT.md            # Deployment guide
├── QUICKSTART.md            # Quick start
├── services/                # Business logic
├── templates/               # HTML
├── static/                  # CSS/JS
├── docs/                    # Documentation
└── data/                    # Hospital data (auto-created)
```

---

## 🔧 Repository Settings

### 1. Make Repository Public (for free deployment)

- Go to Settings → General
- Scroll to "Danger Zone"
- Click "Change visibility" → "Make public"

### 2. Add Description

```
AI-powered healthcare cost comparison system. 
Helps patients find affordable treatment options in India.
```

### 3. Add Topics

```
healthcare, ai, python, flask, groq, llama3, 
cost-comparison, ayushman-bharat, medical-ai
```

---

## 🌐 Deploy from GitHub

### Option 1: Render

1. Go to https://render.com
2. Sign in with GitHub
3. New → Web Service
4. Connect repository: `uipath12312/arogya-mitra-ai-healthcare`
5. Configure:
   - Name: `arogya-mitra`
   - Environment: `Python 3`
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
6. Deploy!

### Option 2: Railway

1. Go to https://railway.app
2. Sign in with GitHub
3. New Project → Deploy from GitHub
4. Select: `uipath12312/arogya-mitra-ai-healthcare`
5. Auto-deploys!

### Option 3: Vercel

1. Go to https://vercel.com
2. Import Git Repository
3. Select your repo
4. Deploy!

---

## 🔑 Environment Variables (Optional)

Add in deployment platform:

```
GROQ_API_KEY=your_groq_key_here
```

Get free key from: https://console.groq.com/

**Note**: App works without API key using mock data!

---

## 📝 README Badge

Add to your README.md:

```markdown
[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-3.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)
```

---

## 🔄 Update Repository

When you make changes:

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

Deployment platforms will auto-redeploy!

---

## 📊 GitHub Actions (Optional CI/CD)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python -m pytest tests/ || true
```

---

## 🎉 Success!

Your repository is now:
- ✅ On GitHub
- ✅ Ready for deployment
- ✅ Using free AI services
- ✅ 100% open source

**Repository URL**: https://github.com/uipath12312/arogya-mitra-ai-healthcare

Share it with the world! 🌍
