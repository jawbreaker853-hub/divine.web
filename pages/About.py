import streamlit as st

st.set_page_config(page_title="About | Divine's Web Dev", page_icon="💻", layout="centered")

# Shared Animation & Minimalist CSS
st.markdown("""
    <style>
    .stApp {
        animation: fadeInPage 0.7s cubic-bezier(0.16, 1, 0.3, 1) ease-out;
        background-color: #0b0b0c;
    }
    @keyframes fadeInPage {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(45deg, #ffffff, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle { color: #888888; font-size: 1.1rem; margin-bottom: 2rem; }
    .skill-badge {
        display: inline-block;
        background-color: #121214;
        border: 1px solid #2e2e2e;
        color: #ffffff;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.85rem;
        transition: all 0.3s ease;
    }
    .skill-badge:hover {
        border-color: #a855f7;
        box-shadow: 0 0 10px rgba(168, 85, 247, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">About Divine\'s Web Dev</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">The engineer behind high-performance digital interfaces.</div>', unsafe_allow_html=True)
st.divider()

st.subheader("My Philosophy")
st.write(
    "I believe a website shouldn't just look incredible—it needs to run fast, remain ultra-secure, "
    "and seamlessly convert visitors into loyal customers. At Divine's Web Dev, I build scalable "
    "web solutions utilizing modern code structures, tailored specifically around individual business goals."
)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Expertise & Core Stack")
st.caption("Hover over my toolkit to see them interact:")

# Interactive skill badges
skills = ["Python / Streamlit", "HTML5 & Custom CSS3", "UI/UX Design", "API Integrations", "Database Architecture", "Performance Optimization"]
badges_html = "".join([f'<div class="skill-badge">{skill}</div>' for skill in skills])
st.markdown(f'<div>{badges_html}</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("My Workflow")
st.markdown("""
1. **The Blueprint:** We plan out your layout, target audience, and site architecture.
2. **The Build:** I engineer a fast, clean environment with premium styling.
3. **The Launch:** Your web system is deployed live onto rapid servers, ready for business.
""")