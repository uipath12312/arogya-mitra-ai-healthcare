# Deploy AROGYA-MITRA to GitHub

There's currently a vim editor blocking git operations. Here are your options:

## Option 1: Close the Vim Editor (Quickest)

Look for a terminal window showing the merge message. In that window:
1. Press `ESC` key
2. Type `:q!` (colon, q, exclamation mark)
3. Press `Enter`

Then run:
```bash
cd arogya-mitra
force-push.bat
```

## Option 2: Use the Batch Files

I've created batch files to handle this:

### A. Force Push (Recommended - Clean slate)
```bash
cd arogya-mitra
force-push.bat
```

### B. Normal Push
```bash
cd arogya-mitra
quick-push.bat
```

## Option 3: Manual Commands

Open a NEW PowerShell/CMD window and run:

```bash
cd arogya-mitra

# Kill vim processes
taskkill /F /IM vim.exe
taskkill /F /IM vi.exe

# Clean merge state
del /F /Q .git\MERGE_HEAD
del /F /Q .git\MERGE_MODE  
del /F /Q .git\MERGE_MSG

# Reset and push
git reset --hard HEAD
git add .
git commit -m "Complete AROGYA-MITRA system"
git push -u origin main --force
```

## Option 4: Fresh Clone (Nuclear option)

```bash
cd ..
git clone https://github.com/uipath12312/arogya-mitra-ai-healthcare.git temp-repo
xcopy /E /I /Y arogya-mitra\* temp-repo\
cd temp-repo
git add .
git commit -m "Complete AROGYA-MITRA system"
git push origin main
```

## Verify Deployment

After successful push, verify at:
https://github.com/uipath12312/arogya-mitra-ai-healthcare

Your repository should contain:
- ✅ app.py
- ✅ lambda_function.py  
- ✅ services/ folder
- ✅ templates/ folder
- ✅ static/ folder
- ✅ data/ folder
- ✅ deploy.bat, deploy-aws.bat, deploy-local.bat
- ✅ README.md, DEPLOYMENT.md, ARCHITECTURE.md
