@echo off
echo Pushing AROGYA-MITRA to GitHub...

git config core.editor "notepad"
git merge --continue -m "Merge remote repository"
git push -u origin main

echo Done!
pause
