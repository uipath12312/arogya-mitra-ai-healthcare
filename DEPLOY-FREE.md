# Deploy AROGYA-MITRA for FREE (No AWS Required)

## Option 1: Render.com (Recommended - Easiest)

### Steps:
1. **Push code to GitHub first** (fix vim issue with `force-push.bat`)

2. **Go to Render.com**
   - Visit: https://render.com
   - Sign up with GitHub account (free)

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo: `uipath12312/arogya-mitra-ai-healthcare`
   - Select the `arogya-mitra` folder

4. **Configure Service**
   - Name: `arogya-mitra`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app_no_aws:app`
   - Instance Type: `Free`

5. **Deploy**
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment
   - Your link: `https://arogya-mitra.onrender.com`

### Note:
- Free tier sleeps after 15 min of inactivity
- First request after sleep takes 30-60 seconds
- Perfect for demos and testing!

---

## Option 2: Railway.app (Alternative)

### Steps:
1. Visit: https://railway.app
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select: `uipath12312/arogya-mitra-ai-healthcare`
5. Railway auto-detects Python and deploys
6. Your link: `https://arogya-mitra.up.railway.app`

**Free tier:** $5 credit/month (enough for demos)

---

## Option 3: Vercel (Static + Serverless)

### Steps:
1. Visit: https://vercel.com
2. Import GitHub repo
3. Framework: Other
4. Build settings will auto-detect
5. Deploy!

Your link: `https://arogya-mitra.vercel.app`

---

## Option 4: PythonAnywhere (Simple)

### Steps:
1. Visit: https://www.pythonanywhere.com
2. Sign up (free tier)
3. Upload your code or clone from GitHub
4. Configure web app with Flask
5. Your link: `https://yourusername.pythonanywhere.com`

---

## Option 5: Local Network Access

To share on your local network:

```bash
cd arogya-mitra
python app_no_aws.py
```

Then share: `http://YOUR_LOCAL_IP:5000`

Find your IP:
```bash
ipconfig
```
Look for "IPv4 Address"

---

## Quick Test Locally

```bash
cd arogya-mitra
pip install -r requirements.txt
python app_no_aws.py
```

Access at: http://localhost:5000

---

## Files Added for Free Deployment:
- ✅ `render.yaml` - Render.com config
- ✅ `Procfile` - Process file for hosting
- ✅ `runtime.txt` - Python version
- ✅ `app_no_aws.py` - Demo version without AWS
- ✅ `requirements.txt` - Updated with gunicorn

## Next Steps:
1. Fix git push (close vim or run `force-push.bat`)
2. Choose a platform above
3. Deploy and get your live link!

**Recommended:** Start with Render.com - it's the easiest and most reliable free option.
