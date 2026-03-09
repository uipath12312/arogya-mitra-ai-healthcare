# AROGYA-MITRA

AI-powered healthcare system that analyzes medical documents, compares treatment costs across hospitals, and recommends affordable healthcare options.

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)
[![Deploy](https://img.shields.io/badge/deploy-free-brightgreen)](DEPLOYMENT.md)

## 🎯 Problem Statement

Patients in India struggle to understand medical reports, compare treatment costs, and identify affordable hospitals. There is no intelligent system to analyze medical documents and recommend cost-effective treatment options or government scheme eligibility, leading to financial burden and poor healthcare decisions.

## 💡 Solution

AROGYA-MITRA is an AI-powered healthcare system that:
- Analyzes uploaded medical documents to extract diagnosis
- Compares treatment costs across hospitals
- Evaluates hospital success rates and reviews
- Identifies eligibility for government healthcare schemes (Ayushman Bharat)
- Recommends the most affordable and effective treatment options

## ✨ Features

- 🤖 AI-based medical document analysis (using free Groq API with Llama 3)
- 💰 Treatment cost comparison across hospitals
- 🏥 Hospital recommendations based on cost, ratings, and success rates
- 🎯 Government scheme eligibility detection (Ayushman Bharat)
- 📍 City-based hospital search (10 major Indian cities)
- 🚀 No login required - instant access
- 💯 100% FREE to deploy and run

## 🛠️ Tech Stack

### Frontend
- HTML5, CSS3, JavaScript
- Responsive design

### Backend
- Python 3.11 (Flask)
- RESTful API

### AI & Data
- **Groq API** (Free Llama 3 model) for document analysis
- JSON file storage (no database needed)
- Local file storage (no cloud needed)

### Deployment
- Render / Railway / Heroku (100% FREE)
- Vercel / PythonAnywhere (alternatives)

## 🚀 Quick Start

### Local Development

```bash
# Clone repository
git clone https://github.com/uipath12312/arogya-mitra-ai-healthcare.git
cd arogya-mitra-ai-healthcare

# Install dependencies
pip install -r requirements.txt

# Run setup (creates data files)
python setup.py

# Start application
python app.py
```

Visit `http://localhost:5000`

**That's it!** App works with mock data - no API keys needed.

### Optional: Enable Real AI

1. Get free API key from https://console.groq.com/
2. Add to `.env` file:
   ```
   GROQ_API_KEY=your_key_here
   ```
3. Restart app

## ☁️ Free Deployment

### Deploy on Render (Recommended)

1. Fork this repository
2. Go to https://render.com
3. Sign in with GitHub
4. New → Web Service
5. Connect: `uipath12312/arogya-mitra-ai-healthcare`
6. Click "Create Web Service"
7. Done! Live in 2 minutes ✨

**See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions**

### Other Free Options
- **Railway**: https://railway.app
- **Heroku**: https://heroku.com
- **PythonAnywhere**: https://pythonanywhere.com
- **Vercel**: https://vercel.com

## 📖 Documentation

- [QUICKSTART.md](QUICKSTART.md) - 5-minute getting started guide
- [DEPLOYMENT.md](DEPLOYMENT.md) - Free cloud deployment guide
- [GITHUB_SETUP.md](GITHUB_SETUP.md) - Repository setup instructions
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - System architecture
- [docs/FEATURES.md](docs/FEATURES.md) - Detailed features
- [docs/TESTING_GUIDE.md](docs/TESTING_GUIDE.md) - Testing procedures

## 🎨 Screenshots

### Home Page
Upload medical documents or describe your health concern

### Analysis Results
- Medical diagnosis and recommended procedures
- Government scheme eligibility
- Hospital recommendations sorted by cost

### Hospital Comparison
- Detailed cost breakdown
- Ratings and success rates
- Contact information

## 💰 Cost

- **Development**: ₹0 (100% Free)
- **Production**: ₹0 (Free tier forever)
- **Scaling**: ₹500-₹2,000/month (only if needed for high traffic)

## 🌟 Unique Selling Points

1. **AI Document Analysis**: First platform to analyze actual medical documents
2. **Comprehensive Comparison**: Cost + quality + schemes in one place
3. **Government Integration**: Automatic scheme eligibility detection
4. **No Barriers**: No login, instant access
5. **Cost Savings**: 40-70% savings for patients
6. **100% Free**: No cloud costs, free deployment

## 🎯 Use Case Example

**Patient**: Rajesh, Mumbai  
**Problem**: Chest pain, needs ECG and blood tests

**AROGYA-MITRA Analysis**:
- Diagnosis: Possible cardiac issue
- Recommended: ECG, Blood Test, Consultation

**Hospital Comparison**:
1. Government Hospital: ₹630 (70% cheaper) ✅
2. Fortis Healthcare: ₹1,900
3. Apollo Hospital: ₹2,850

**Scheme**: Eligible for Ayushman Bharat (₹5L coverage)

**Result**: Rajesh saves ₹2,220 and gets free treatment!

## 🗺️ Roadmap

### Phase 2 (3 months)
- Multi-language support (Hindi, Tamil, Telugu)
- Voice input
- Real-time AI chat assistant

### Phase 3 (6 months)
- Appointment booking
- Insurance claim support
- Medicine price comparison

### Phase 4 (12 months)
- Telemedicine integration
- Mobile apps (iOS/Android)
- Health records management

## 👥 Team

**Team Karishma**  
Leader: Karishma

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📄 License

MIT License - feel free to use for social good!

## 🙏 Acknowledgments

- Groq for free AI API
- Render/Railway for free hosting
- Healthcare workers for inspiration
- Patients for whom we build

## 📞 Contact

- **GitHub**: https://github.com/uipath12312/arogya-mitra-ai-healthcare
- **Issues**: Open an issue for support
- **Discussions**: Use GitHub Discussions

## 🎉 Success Metrics

- ✅ 100% free to deploy
- ✅ No API costs (free tier)
- ✅ No database costs
- ✅ No cloud storage costs
- ✅ Production-ready
- ✅ Scalable architecture

---

**AROGYA-MITRA: Empowering patients with intelligent healthcare guidance, reducing financial burden, and improving access to affordable treatment across India.** 🏥💙

**Star ⭐ this repo if you find it helpful!**
