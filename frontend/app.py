# frontend/app.py

import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Government Scheme Assistant",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    .main-title { color: #1B3A6B; font-size: 2.5rem; font-weight: 700; }
    .answer-box {
        background: #f0f8ff;
        border-left: 4px solid #2980B9;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-size: 1rem;
        line-height: 1.8;
    }
    .source-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    .scheme-tag {
        background: #1B3A6B;
        color: white;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        margin-right: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏛️ Government Scheme Assistant")
    st.markdown("---")

    try:
        health = requests.get(f"{API_URL}/health", timeout=3).json()
        st.success("✅ System Online")
        st.metric("Schemes Indexed", health.get("total_schemes", 0))
    except:
        st.error("❌ API Offline")
        st.info("Run: python -m uvicorn api.main:app --reload --port 8000")

    st.markdown("---")
    st.markdown("### 💡 Sample Questions")

    sample_questions = [
        "Who is eligible for PM-KISAN?",
        "How to apply for Ayushman Bharat?",
        "Schemes for women entrepreneurs",
        "PM Awas Yojana benefits",
        "Scholarship for SC/ST students",
        "What is Kisan Credit Card?",
        "How to get MUDRA loan?",
        "Schemes for unemployed youth",
    ]

    for q in sample_questions:
        if st.button(q, use_container_width=True):
            st.session_state.question = q
            st.rerun()

    st.markdown("---")
    st.markdown("**Powered by:**")
    st.markdown("- 🤖 Groq LLaMA 3.1")
    st.markdown("- 🔍 ChromaDB")
    st.markdown("- ⚡ LangChain")
    st.markdown("- 🚀 FastAPI")

# ── MAIN PAGE ─────────────────────────────────────────────────────────
st.markdown('<p class="main-title">🇮🇳 Government Scheme Assistant</p>',
            unsafe_allow_html=True)
st.markdown("#### Ask any question about Indian Government Schemes in plain English")
st.markdown("---")

tab1, tab2 = st.tabs(["💬 Ask a Question", "📋 Browse Schemes"])

with tab1:
    if "question" not in st.session_state:
        st.session_state.question = ""

    question = st.text_area(
        "Your Question",
        value=st.session_state.question,
        placeholder="e.g., What schemes are available for farmers?",
        height=100,
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        ask_btn = st.button("🔍 Ask", type="primary", use_container_width=True)
    with col2:
        max_sources = st.slider("Max sources", 1, 5, 3)

    if ask_btn and question.strip():
        with st.spinner("🔍 Searching government scheme database..."):
            try:
                response = requests.post(
                    f"{API_URL}/query",
                    json={"question": question, "max_sources": max_sources},
                    timeout=30
                )

                if response.status_code == 200:
                    data = response.json()

                    st.markdown("### 📝 Answer")
                    st.markdown(
                        f'<div class="answer-box">{data["answer"]}</div>',
                        unsafe_allow_html=True
                    )

                    if data["sources"]:
                        st.markdown(f"### 📚 Sources ({data['num_sources']} schemes referenced)")
                        cols = st.columns(min(len(data["sources"]), 3))
                        for i, source in enumerate(data["sources"]):
                            with cols[i % 3]:
                                st.markdown(f"""
                                <div class="source-card">
                                    <b>📋 {source['scheme_name']}</b><br><br>
                                    <p style="font-size:0.8rem;color:#666;margin-top:8px">
                                        {source['preview'][:150]}...
                                    </p>
                                </div>
                                """, unsafe_allow_html=True)

                    st.markdown("---")
                    st.markdown("**Was this helpful?**")
                    c1, c2, c3 = st.columns([1, 1, 8])
                    with c1:
                        st.button("👍 Yes")
                    with c2:
                        st.button("👎 No")

                else:
                    st.error(f"API Error: {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to API. Make sure FastAPI is running!")
            except Exception as e:
                st.error(f"Error: {e}")

    elif ask_btn:
        st.warning("Please enter a question first!")

with tab2:
    st.markdown("### All Indexed Government Schemes")
    try:
        schemes_resp = requests.get(f"{API_URL}/schemes", timeout=5).json()
        schemes = schemes_resp.get("schemes", [])

        search = st.text_input("🔍 Search schemes", placeholder="e.g., farmer, health, housing")
        if search:
            schemes = [s for s in schemes if search.lower() in s.lower()]

        st.markdown(f"Showing **{len(schemes)}** schemes")
        st.markdown("---")

        cols = st.columns(2)
        for i, scheme in enumerate(schemes):
            with cols[i % 2]:
                st.markdown(f"• **{scheme}**")

    except:
        st.warning("Start the FastAPI server to browse schemes")