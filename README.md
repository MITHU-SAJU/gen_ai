# Project

This repository contains a `frontend/` (Vite/React) and `backend/` (Python) folder.

Quick setup to initialize git and push to GitHub (replace `<repo-url>`):

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

If you prefer to create the GitHub repo from this folder using GitHub CLI:

```powershell
gh auth login
gh repo create my-repo --public --source=. --remote=origin --push
```

Notes:

- Update `<repo-url>` with your repository URL (HTTPS or SSH).
- Ensure `frontend/package.json` and `backend/requirements.txt` are correct before CI.
