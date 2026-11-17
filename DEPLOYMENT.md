# 🌐 NIT Jalandhar Semester 3 Study Portal — Deployment Guide

## 1. ⚡ Live Public Link (Active Right Now)
You can open this URL right now on your **phone, iPad, laptop**, or share it directly with classmates:

👉 **[https://jlbka-106-219-67-185.free.pinggy.net](https://jlbka-106-219-67-185.free.pinggy.net)**
*(Backup Mirror: https://iserg-106-219-67-185.run.pinggy-free.link)*

- **Zero configuration, zero passwords**: Opens the complete study kit & PDF reader immediately.
- Works on mobile Safari, Chrome, Edge, Firefox, and tablet browsers.

---

## 2. 💻 Local Access on Your PC
- Local URL: **[http://localhost:8000](http://localhost:8000)**
- Desktop 1-Click Launchers:
  - Double-click `launch_study_portal.bat` to launch locally anytime.
  - Double-click `launch_public_url.bat` to spin up a new live public HTTPS sharing link anytime.

---

## 3. ☁️ Permanent 24/7 Cloud Hosting (100% Free)
If you want the website to stay online 24/7 even when your PC is turned off:

### Option A: Render (Recommended - Free Web Service)
1. Push this folder to a GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Deploy NITJ Sem 3 Study Portal"
   git branch -M main
   git remote add origin https://github.com/<your-username>/nitj-sem3-portal.git
   git push -u origin main
   ```
2. Log into [render.com](https://render.com) and click **"New +" → "Web Service"**.
3. Connect your GitHub repository.
4. Settings:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn server:app --app-dir web --host 0.0.0.0 --port 10000`
5. Click **Deploy**. Your site will be permanently live at `https://nitj-sem3.onrender.com`.

### Option B: Hugging Face Spaces (Free Docker Hosting)
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces) and click **Create new Space**.
2. Select **Docker** as the Space SDK.
3. Push your repository. The included `Dockerfile` will automatically build and host the site.
