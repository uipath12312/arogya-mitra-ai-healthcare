# AROGYA-MITRA Deployment Guide

## 🚀 Free Deployment Options

This application uses **FREE AI services** and can be deployed for **FREE** on multiple platforms.

---

## Option 1: Render (Recommended - 100% Free)

### Steps:

1. **Fork/Clone Repository**
   ```bash
   git clone https://github.com/uipath12312/arogya-mitra-ai-healthcare.git
   cd arogya-mitra-ai-healthcare
   ```

2. **Push to Your GitHub**
   ```bash
   git remote set-url origin https://github.com/uipath12312/arogya-mitra-ai-healthcare.git
   git push -u origin main
   ```

3. **Deploy on Render**
   - Go to https://render.com
   - Sign up with GitHub (Free)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: arogya-mitra
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free
   - Click "Create Web Service"

4. **Add Environment Variables (Optional)**
   - Go to Environment tab
   - Add `GROQ_API_KEY` if you have one (get free from https://console.groq.com/)
   - App works without it using mock data

5. **Access Your App**
   - URL: `https://arogya-mitra.onrender.com`
   - First load may take 30-60 seconds (free tier)

---

## Option 2: Railway (Free Tier)

### Steps:

1. **Deploy on Railway**
   - Go to https://railway.app
   - Sign up with GitHub (Free)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway auto-detects Python and deploys

2. **Configure**
   - Add environment variables if needed
   - Railway provides free $5 credit monthly

3. **Access**
   - Railway provides a public URL

---

## Option 3: Heroku (Free Dyno)

### Steps:

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login and Create App**
   ```bash
   heroku login
   heroku create arogya-mitra
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Open App**
   ```bash
   heroku open
   ```

---

## Option 4: PythonAnywhere (Free)

### Steps:

1. **Sign Up**
   - Go to https://www.pythonanywhere.com
   - Create free account

2. **Upload Code**
   - Use "Files" tab to upload your code
   - Or clone from GitHub:
     ```bash
     git clone https://github.com/uipath12312/arogya-mitra-ai-healthcare.git
     ```

3. **Create Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose Flask
   - Point to your `app.py`

4. **Install Dependencies**
   - Open Bash console
   - Run:
     ```bash
     pip install -r requirements.txt
     ```

5. **Reload and Access**
   - Click "Reload" button
   - Access at `yourusername.pythonanywhere.com`

---

## Option 5: Vercel (Serverless)

### Steps:

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Create vercel.json**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Deploy**
   ```bash
   vercel
   ```

---

## 🆓 Free AI API Setup

### Groq (Recommended - Fast & Free)

1. **Sign Up**
   - Go to https://console.groq.com/
   - Create free account

2. **Get API Key**
   - Go to API Keys section
   - Create new key
   - Copy the key

3. **Add to Environment**
   - In your deployment platform, add:
     ```
     GROQ_API_KEY=your_key_here
     ```

4. **Benefits**
   - Free tier: 14,400 requests/day
   - Fast inference (Llama 3)
   - No credit card required

### Alternative: Hugging Face (Free)

1. **Sign Up**
   - Go to https://huggingface.co/
   - Create account

2. **Get Token**
   - Go to Settings → Access Tokens
   - Create new token

3. **Use in App**
   - Add `HUGGINGFACE_API_KEY` to environment

---

## 📝 Post-Deployment Checklist

- [ ] App loads successfully
- [ ] Can select city
- [ ] Can enter medical problem
- [ ] Results display correctly
- [ ] Hospital recommendations show
- [ ] Costs are calculated
- [ ] No errors in logs

---

## 🔧 Troubleshooting

### Issue: App won't start
**Solution**: Check logs for missing dependencies
```bash
# Render: View logs in dashboard
# Heroku: heroku logs --tail
```

### Issue: Slow first load
**Solution**: Normal for free tiers (cold start)
- First request: 30-60 seconds
- Subsequent requests: Fast

### Issue: AI not working
**Solution**: App works without AI API key using mock data
- Add GROQ_API_KEY for real AI analysis
- Or continue with mock data for demo

---

## 💰 Cost Comparison

| Platform | Free Tier | Limitations |
|----------|-----------|-------------|
| Render | ✅ Free forever | 750 hours/month, sleeps after 15min |
| Railway | ✅ $5 credit/month | ~500 hours |
| Heroku | ✅ Free dyno | Sleeps after 30min |
| PythonAnywhere | ✅ Free forever | Limited CPU |
| Vercel | ✅ Free forever | Serverless limits |

**Recommendation**: Start with Render for best free experience.

---

## 🌐 Custom Domain (Optional)

### Free Domain Options:
1. **Freenom**: Free .tk, .ml, .ga domains
2. **GitHub Pages**: Use with custom subdomain
3. **Cloudflare**: Free DNS management

### Setup:
1. Get free domain
2. Add CNAME record pointing to your deployment
3. Configure in deployment platform

---

## 📊 Monitoring (Free)

### UptimeRobot
- Free monitoring
- Keeps app awake (prevents sleep)
- Email alerts

### Setup:
1. Go to https://uptimerobot.com
2. Add your app URL
3. Set check interval: 5 minutes

---

## 🔐 Security

### Environment Variables
- Never commit `.env` file
- Use platform's environment variable settings
- Rotate API keys regularly

### HTTPS
- All platforms provide free SSL
- Automatic HTTPS redirect

---

## 📈 Scaling

### When to Upgrade:
- More than 1000 users/day
- Need faster response times
- Want custom domain
- Need more storage

### Paid Options:
- Render: $7/month (no sleep)
- Railway: Pay as you go
- Heroku: $7/month (hobby dyno)

---

## 🎉 Success!

Your AROGYA-MITRA app is now live and helping patients find affordable healthcare!

**Share your deployment:**
- URL: https://your-app.onrender.com
- GitHub: https://github.com/uipath12312/arogya-mitra-ai-healthcare

---

## 🆘 Need Help?

- Check platform documentation
- Review app logs
- Test locally first: `python app.py`
- Ensure all files committed to GitHub

**Happy Deploying! 🚀**
