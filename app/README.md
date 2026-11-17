# 🎓 NIT Jalandhar B.Tech Semester 3 — AI Study Notebook (NotebookLM Edition)

> **A custom Google NotebookLM experience built exclusively for NIT Jalandhar Computer Science & Information Technology Semester 3 End-Term Preparation.**
> Grounded in 177,000+ words of official theory textbooks, 22 solved past university exam papers (2019–2024), lab guides, and 300 DPI architectural diagrams.

---

## 🌟 Key Features

### 1. 📚 Grounded "Ask Gemini" Q&A
- **Strict Ground-Truth Ingestion**: Every response is grounded directly in the active subject's official theory book and solved PYQs.
- **Academic Rigor & Citations**: Cites exact Unit numbers (e.g. `[Source: DSA Master Book § Unit 3.2 - AVL Rotations]`) and past exam papers (`[Tested in NITJ End-Sem Nov 2023, Q3(b)]`).
- **LaTeX Math & Code Support**: Full rendering of step-by-step mathematical proofs, recurrence relations, recurrence trees, and clean C++17/SQL code snippets.

### 2. 🎙️ NotebookLM Studio Artifacts
- **Deep Dive Audio Podcast Script**: 2-host conversational transcript ("Alex & Jamie") discussing complex concepts with mnemonics, examiner traps, and real-world analogies.
- **Comprehensive End-Term Study Guide**: Formatted revision briefing with Executive Blueprints, Core Definitions, Comparison Matrices, and 5-minute pre-exam checklists.
- **NIT Jalandhar Exam Simulator & Marking Scheme**: Real 50-mark exam papers structured into Section A (2 marks), Section B (5 marks), and Section C (10 marks) with complete marking rubrics.
- **Ultra-Dense Formula & Complexity Matrix**: Tabular cheatsheet of time/space complexities, recurrence relations, and key syntax.
- **15 High-Yield 2-Mark & Viva Drill**: Quick-fire practice questions with exact keywords required for full marks.

### 3. 📖 Built-In Source Document Reader
- Inspect, search, and read the complete Markdown textbooks directly in your browser.
- Instant 1-click download buttons for compiled PDFs.

### 4. 🖼️ 300 DPI Architectural Diagrams Gallery
- High-resolution visual diagrams for CPU memory hierarchy, transaction states, Big-O complexities, Euler vs Hamiltonian cycles, C++ vtable/vptr layout, and the JS event loop.

---

## 🚀 Quick Start (Local)

### Step 1: 1-Click Launch
Double-click [`launch_notebooklm.bat`](file:///C:/Users/2006s/Desktop/SEM3_ENDTERM_MASTER_KIT/launch_notebooklm.bat) in the root folder, or run:
```bash
streamlit run app/app.py
```

### Step 2: Open in Browser
Visit **`http://localhost:8501`** in any web browser.

### Step 3: Enter Your Free Gemini API Key
In the sidebar, expand **"🔑 Gemini API Key Settings"** and paste your API key from [Google AI Studio](https://aistudio.google.com/app/apikey). The key is stored only in your local browser session.

---

## 🌐 Free 24/7 Cloud Hosting Options

### Option A: Streamlit Community Cloud (Recommended - 100% Free Forever)
1. Initialize a git repository and push your project to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Sem 3 NotebookLM"
   git branch -M main
   git remote add origin https://github.com/<your-username>/nitj-sem3-notebooklm.git
   git push -u origin main
   ```
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and log in with GitHub.
3. Click **"New App"**:
   - Repository: `<your-username>/nitj-sem3-notebooklm`
   - Main file path: `app/app.py`
4. Under **Advanced Settings → Secrets**, add:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key_here"
   ```
5. Click **Deploy!** Your website is now live 24/7 at `https://nitj-sem3.streamlit.app`!

### Option B: Instant Public Link from your PC (Cloudflare Tunnel or LocalTunnel)
Double-click [`launch_public_url.bat`](file:///C:/Users/2006s/Desktop/SEM3_ENDTERM_MASTER_KIT/launch_public_url.bat), or run:
```bash
npx --yes localtunnel --port 8501
```
This generates a secure HTTPS URL (e.g. `https://happy-cat-42.loca.lt`) accessible on your mobile phone, iPad, or by classmates anywhere in the world!
