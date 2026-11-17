"""
app.py
NIT Jalandhar B.Tech Semester 3 — AI Study Notebook (NotebookLM Edition)
Powered by Google Gemini 2.5 & Streamlit
"""

import os
import sys
import time
import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="NotebookLM — NITJ B.Tech Sem 3 Master Kit",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom NotebookLM Material Theme CSS
st.markdown("""
<style>
    /* Google NotebookLM Inspired Aesthetic */
    @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Roboto+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Google Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Top App Banner */
    .notebook-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 20px 28px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    .notebook-title {
        font-size: 26px;
        font-weight: 700;
        color: #F8FAFC;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .notebook-subtitle {
        color: #94A3B8;
        font-size: 14px;
        margin-top: 4px;
    }

    .badge-chip {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        background: rgba(66, 133, 244, 0.15);
        color: #60A5FA;
        border: 1px solid rgba(96, 165, 250, 0.3);
    }

    /* Source Cards in Sidebar */
    .source-box {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 10px;
        transition: all 0.2s ease;
    }

    .source-box:hover {
        border-color: #60A5FA;
        transform: translateY(-1px);
    }

    /* Prompt Chips */
    .prompt-chip {
        display: inline-block;
        background: #1E293B;
        border: 1px solid #475569;
        color: #E2E8F0;
        padding: 8px 14px;
        border-radius: 20px;
        font-size: 13px;
        margin-right: 8px;
        margin-bottom: 8px;
        cursor: pointer;
        transition: all 0.15s ease-in-out;
    }

    .prompt-chip:hover {
        background: #334155;
        border-color: #93C5FD;
        color: #FFFFFF;
    }

    /* Studio Card */
    .studio-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 20px;
    }

    /* Code & Output styling */
    pre, code {
        font-family: 'Roboto Mono', monospace !important;
    }
</style>
""", unsafe_allow_html=True)

# Import backend modules
import document_manager as dm
import gemini_engine
import studio_generators

# Initialize session states
if "messages" not in st.session_state:
    st.session_state.messages = []

if "active_subject" not in st.session_state:
    st.session_state.active_subject = "01_CSA"

if "api_key" not in st.session_state:
    st.session_state.api_key = os.environ.get("GEMINI_API_KEY", "")

if "generated_studio_doc" not in st.session_state:
    st.session_state.generated_studio_doc = None


# ==========================================
# SIDEBAR: Sources & Configuration
# ==========================================
with st.sidebar:
    st.markdown("### 📚 **NotebookLM Sources**")
    st.caption("Official NIT Jalandhar Semester 3 Study Kit")

    # API Key Configuration
    with st.expander("🔑 **Gemini API Key Settings**", expanded=(not bool(st.session_state.api_key))):
        key_input = st.text_input(
            "Google Gemini API Key",
            value=st.session_state.api_key,
            type="password",
            placeholder="AIzaSy...",
            help="Get your free Gemini API key with 1M context from Google AI Studio (aistudio.google.com)"
        )
        if key_input:
            st.session_state.api_key = key_input.strip()
            st.success("API Key saved for this session!")
        st.markdown("[Get a free Gemini API Key →](https://aistudio.google.com/app/apikey)")

    # Model Selector
    model_choice = st.selectbox(
        "🧠 AI Model",
        options=[m["id"] for m in gemini_engine.AVAILABLE_MODELS],
        format_func=lambda x: next(m["name"] for m in gemini_engine.AVAILABLE_MODELS if m["id"] == x),
        index=0
    )

    st.divider()

    # Subject Scope Selector
    st.markdown("#### 🎯 **Active Subject**")
    subject_keys = list(dm.SUBJECT_METADATA.keys())
    
    selected_subject_idx = subject_keys.index(st.session_state.active_subject) if st.session_state.active_subject in subject_keys else 0
    active_subject = st.selectbox(
        "Select Course Subject:",
        options=subject_keys,
        format_func=lambda k: f"{dm.SUBJECT_METADATA[k]['icon']} {dm.SUBJECT_METADATA[k]['short']} — {dm.SUBJECT_METADATA[k]['name']}",
        index=selected_subject_idx
    )
    st.session_state.active_subject = active_subject

    # Load active subject data
    active_sources = dm.get_subject_sources(active_subject)
    active_meta = active_sources["meta"]

    st.markdown(f"**Course Code**: `{active_meta.get('code')}`")
    st.caption(active_meta.get("description", ""))

    # Sources checklist
    st.markdown("#### 📑 **Included Sources**")
    inc_theory = st.checkbox("📖 Exhaustive Theory Book (Units 1–5)", value=True)
    inc_pyq = st.checkbox("📝 Solved PYQs (2019–2024 Audit)", value=True)
    inc_earlier = st.checkbox("💡 User Notes & Lab Solutions", value=True)

    # Calculate token count
    loaded_sources_for_prompt = []
    token_est = 0

    single_src = {
        "meta": active_meta,
        "theory_text": active_sources["theory_text"] if inc_theory else "",
        "pyq_text": active_sources["pyq_text"] if inc_pyq else "",
        "earlier_notes": active_sources["earlier_notes"] if inc_earlier else {},
        "official_pyqs": active_sources["official_pyqs"],
        "diagrams": active_sources["diagrams"]
    }
    loaded_sources_for_prompt.append(single_src)

    raw_text_len = len(single_src["theory_text"]) + len(single_src["pyq_text"])
    for c in single_src["earlier_notes"].values():
        raw_text_len += len(c)
    token_est = int(raw_text_len / 4)

    st.markdown(f"""
    <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10B981; border-radius: 8px; padding: 10px; margin-top: 12px;">
        <span style="color: #34D399; font-weight: 600; font-size: 13px;">⚡ Active Context: ~{token_est:,} tokens</span><br/>
        <span style="color: #94A3B8; font-size: 11px;">Consumes ~{round(token_est/10000, 1)}% of Gemini's 1,000,000 token limit</span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Corpus Quick Stats
    all_stats = dm.get_full_corpus_stats()
    st.markdown("#### 📊 **Master Corpus Stats**")
    st.caption(f"• Total Words: **{all_stats['total_words']:,}** across 6 subjects")
    st.caption(f"• Total Lines: **{all_stats['total_lines']:,}** lines of verified notes")
    st.caption("• 22 Official NITJ Exam Papers Solved")

    # Clear Chat Button
    if st.button("🗑️ Reset Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ==========================================
# MAIN INTERFACE: NotebookLM Experience
# ==========================================

# Top Banner
st.markdown(f"""
<div class="notebook-header">
    <div>
        <div class="notebook-title">
            <span>{active_meta.get('icon', '🎓')}</span>
            <span>{active_meta.get('name', 'Semester 3 Notebook')}</span>
            <span class="badge-chip">{active_meta.get('code', 'NIT JALANDHAR')}</span>
        </div>
        <div class="notebook-subtitle">
            Ground-truth exam preparation workspace • Powered by Google Gemini 2.5 Flash
        </div>
    </div>
    <div style="text-align: right;">
        <span class="badge-chip" style="background: rgba(16, 185, 129, 0.15); color: #34D399; border-color: rgba(16, 185, 129, 0.3);">
            ● Grounded & Verified
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Build Grounded Context String
context_block = gemini_engine.format_context_prompt(loaded_sources_for_prompt)

# Main Navigation Tabs
tab_chat, tab_studio, tab_reader, tab_diagrams, tab_deploy = st.tabs([
    "💬 Ask Gemini (Grounded Chat)",
    "🎙️ Studio & Revision Tools",
    "📖 Source Document Reader",
    "🖼️ Technical Diagrams Gallery",
    "🌐 Cloud Hosting & Sharing"
])


# ==========================================
# TAB 1: Grounded Chat ("Ask Gemini")
# ==========================================
with tab_chat:
    # Suggested Prompt Chips
    st.markdown("##### 💡 **Suggested Inquiries for this Subject:**")
    prompt_cols = st.columns(len(active_meta.get("sample_prompts", [])))
    
    clicked_prompt = None
    for i, p_text in enumerate(active_meta.get("sample_prompts", [])):
        with prompt_cols[i]:
            if st.button(f"🔍 {p_text}", key=f"chip_{active_subject}_{i}", use_container_width=True):
                clicked_prompt = p_text

    st.write("")

    # Display chat message history
    for msg in st.session_state.messages:
        avatar = "🧑‍💻" if msg["role"] == "user" else "✨"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    # Chat Input handler
    chat_prompt = st.chat_input("Ask any question regarding syllabus, theorems, PYQs, derivations, or code...")

    # Determine prompt to run (either clicked chip or typed prompt)
    prompt_to_run = clicked_prompt or chat_prompt

    if prompt_to_run:
        # Check API key
        if not st.session_state.api_key:
            with st.chat_message("assistant", avatar="✨"):
                st.warning("⚠️ **Gemini API Key Required**\nPlease enter your Google Gemini API Key in the left sidebar to activate live Q&A. You can get one for free at [Google AI Studio](https://aistudio.google.com/app/apikey).")
        else:
            # Append user message
            st.session_state.messages.append({"role": "user", "content": prompt_to_run})
            with st.chat_message("user", avatar="🧑‍💻"):
                st.markdown(prompt_to_run)

            # Generate and stream Gemini response
            with st.chat_message("assistant", avatar="✨"):
                client = gemini_engine.get_gemini_client(st.session_state.api_key)
                if client:
                    stream = gemini_engine.stream_gemini_response(
                        client=client,
                        model=model_choice,
                        messages=st.session_state.messages,
                        context_text=context_block
                    )
                    full_response = st.write_stream(stream)
                    st.session_state.messages.append({"role": "model", "content": full_response})
                else:
                    st.error("Failed to connect to Gemini API. Please check your API key.")


# ==========================================
# TAB 2: Studio & Revision Tools
# ==========================================
with tab_studio:
    st.markdown("### 🎙️ **NotebookLM Studio & Exam Artifacts**")
    st.caption("Generate multi-modal exam materials grounded on your course notes.")

    s_col1, s_col2 = st.columns([1, 2])

    with s_col1:
        st.markdown("#### 🛠️ **Choose Tool**")
        tool_choice = st.radio(
            "Select Artifact to Generate:",
            options=[
                "🎙️ Deep Dive Audio Podcast Script",
                "📑 Comprehensive End-Term Study Guide",
                "🎯 NIT Jalandhar Exam Simulator & Marking Scheme",
                "⚡ Ultra-Dense Formula & Complexity Cheat Sheet",
                "❓ 15 High-Yield 2-Mark & Viva Drill"
            ]
        )

        st.markdown("#### 🎯 **Focus Target**")
        focus_target = st.selectbox(
            "Select Unit or Scope:",
            options=["All Units (Entire Subject)"] + active_meta.get("units", [])
        )

        gen_button = st.button("✨ Generate Artifact", type="primary", use_container_width=True)

    with s_col2:
        if gen_button:
            if not st.session_state.api_key:
                st.warning("⚠️ Please provide your Gemini API Key in the left sidebar to generate Studio artifacts.")
            else:
                client = gemini_engine.get_gemini_client(st.session_state.api_key)
                with st.spinner(f"Generating {tool_choice} with {model_choice}..."):
                    if "Audio Podcast" in tool_choice:
                        result = studio_generators.generate_podcast_script(
                            client, model_choice, active_meta["name"], focus_target, context_block
                        )
                    elif "Study Guide" in tool_choice:
                        result = studio_generators.generate_study_guide(
                            client, model_choice, active_meta["name"], focus_target, context_block
                        )
                    elif "Exam Simulator" in tool_choice:
                        result = studio_generators.generate_exam_simulator(
                            client, model_choice, active_meta["name"], "Standard End-Sem Pattern (50 Marks)", context_block
                        )
                    elif "Cheat Sheet" in tool_choice:
                        result = studio_generators.generate_cheat_sheet(
                            client, model_choice, active_meta["name"], context_block
                        )
                    else:
                        result = studio_generators.generate_faq_drill(
                            client, model_choice, active_meta["name"], context_block
                        )

                    st.session_state.generated_studio_doc = {
                        "title": f"{tool_choice} — {active_meta['short']}",
                        "content": result
                    }

        # Render generated artifact
        if st.session_state.generated_studio_doc:
            doc = st.session_state.generated_studio_doc
            st.markdown(f"### 📄 {doc['title']}")
            st.download_button(
                label="📥 Download as Markdown (.md)",
                data=doc["content"],
                file_name=f"{doc['title'].replace(' ', '_')}.md",
                mime="text/markdown"
            )
            st.markdown("---")
            st.markdown(doc["content"])
        else:
            st.info("👈 Select an artifact type on the left and click **'Generate Artifact'** to create personalized exam guides, podcast scripts, and mock tests.")


# ==========================================
# TAB 3: Source Document Reader
# ==========================================
with tab_reader:
    st.markdown("### 📖 **Source Document Reader**")
    st.caption("Inspect the exact source textbooks and solved PYQs used for grounding.")

    r_col1, r_col2 = st.columns([1, 3])

    with r_col1:
        doc_choice = st.radio(
            "Select Document to Read:",
            options=["Exhaustive Theory Book", "Solved PYQs Compendium", "Supplementary Guides"]
        )

    with r_col2:
        if doc_choice == "Exhaustive Theory Book":
            text_to_show = active_sources["theory_text"]
            pdf_path = active_sources["theory_pdf"]
            title = f"{active_meta['name']} — Theory Master Book"
        elif doc_choice == "Solved PYQs Compendium":
            text_to_show = active_sources["pyq_text"]
            pdf_path = active_sources["pyq_pdf"]
            title = f"{active_meta['name']} — Solved PYQs"
        else:
            earlier_keys = list(active_sources["earlier_notes"].keys())
            if earlier_keys:
                selected_guide = st.selectbox("Select Guide:", options=earlier_keys)
                text_to_show = active_sources["earlier_notes"][selected_guide]
                pdf_path = None
                title = selected_guide
            else:
                text_to_show = "No supplementary guides in this folder."
                pdf_path = None
                title = "None"

        st.markdown(f"#### 📄 **{title}**")
        if pdf_path and os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pf:
                st.download_button(
                    label="📥 Download Compiled PDF Version",
                    data=pf.read(),
                    file_name=os.path.basename(pdf_path),
                    mime="application/pdf"
                )

        # Search inside document
        search_kw = st.text_input("🔍 Search keyword in this document:", placeholder="e.g. Tomasulo, BCNF, AVL, Dijkstra...")
        if search_kw:
            matching_lines = [line for line in text_to_show.split("\n") if search_kw.lower() in line.lower()]
            st.caption(f"Found {len(matching_lines)} matching lines:")
            with st.expander("Matching excerpts", expanded=True):
                st.markdown("\n".join([f"- {line}" for line in matching_lines[:15]]))

        with st.expander("👁️ View Full Document Text", expanded=True):
            st.markdown(text_to_show[:30000] + ("\n\n*(Truncated in preview... download full text or ask Gemini)*" if len(text_to_show) > 30000 else ""))


# ==========================================
# TAB 4: Technical Diagrams Gallery
# ==========================================
with tab_diagrams:
    st.markdown("### 🖼️ **300 DPI High-Resolution Technical Diagrams**")
    st.caption("Custom-rendered architectural illustrations and state machines.")

    if active_sources["diagrams"]:
        for dpath in active_sources["diagrams"]:
            st.image(dpath, caption=f"Technical Diagram: {os.path.basename(dpath)}", use_container_width=True)
            with open(dpath, "rb") as img_f:
                st.download_button(
                    label=f"📥 Download High-Res {os.path.basename(dpath)}",
                    data=img_f.read(),
                    file_name=os.path.basename(dpath),
                    mime="image/png",
                    key=f"dl_diag_{os.path.basename(dpath)}"
                )
    else:
        st.info("No standalone diagram files in this folder.")


# ==========================================
# TAB 5: Deployment & Sharing
# ==========================================
with tab_deploy:
    st.markdown("### 🌐 **How to Host & Share this NotebookLM Website**")
    st.markdown("""
    You have **3 simple, 100% free ways** to host this website so you can access it anywhere (phone, iPad, laptop) or share it with classmates!

    ---

    #### 🚀 **Method 1: 1-Click Instant Public URL (Via Cloudflare Tunnel or ngrok)**
    *Best for running from your current laptop and sharing a live HTTPS link instantly without uploading code anywhere.*
    1. Open your terminal in this directory.
    2. Run Streamlit: `streamlit run app/app.py`
    3. Run Cloudflare Tunnel:
       ```bash
       npx cloudflared tunnel --url http://localhost:8501
       ```
       or with ngrok:
       ```bash
       ngrok http 8501
       ```
    4. You will get a live public HTTPS URL (e.g. `https://random-subdomain.trycloudflare.com`) that you can open on any phone or send to friends!

    ---

    #### ☁️ **Method 2: Streamlit Community Cloud (100% Free 24/7 Cloud Hosting)**
    *Best for permanent 24/7 cloud hosting with your own custom URL.*
    1. Initialize a git repository in `SEM3_ENDTERM_MASTER_KIT`:
       ```bash
       git init
       git add .
       git commit -m "NITJ Sem 3 NotebookLM Kit"
       ```
    2. Push to your GitHub repository (e.g. `github.com/your-username/nitj-sem3-notebooklm`).
    3. Go to [share.streamlit.io](https://share.streamlit.io) and log in with GitHub.
    4. Click **'New App'**, choose your repo, set the main file path to `app/app.py`.
    5. In **Advanced Settings -> Secrets**, add:
       ```toml
       GEMINI_API_KEY = "your_actual_gemini_api_key"
       ```
    6. Click **Deploy!** In ~60 seconds, your app will be live at `https://nitj-sem3.streamlit.app`!

    ---

    #### 🐳 **Method 3: Docker / Render / Hugging Face Spaces**
    We have included a production `Dockerfile` and `requirements.txt` inside the `app/` directory ready for 1-click container deployment.
    """);
