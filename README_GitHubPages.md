# Deploy to GitHub Pages

These steps assume you have a GitHub account and Git installed.

1. Create a new **public** repository on GitHub (e.g., `relations_project`).
2. On your computer, open a terminal and run:

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit for GitHub Pages"
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

3. In the repository **Settings → Pages**, set:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main` / `/ (root)`

4. Wait 1–3 minutes. Your site will be live at:
   `https://<your-username>.github.io/<your-repo>/`
