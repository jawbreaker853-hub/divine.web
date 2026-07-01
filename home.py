import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Divine's Web Dev | Premium Websites", 
    page_icon="💻", 
    layout="centered"
)

# 2. Complete Animation, Glow, & Minimalist CSS
st.markdown("""
    <style>
    /* Smooth Page Entrance Transition */
    .stApp {
        animation: fadeInPage 0.7s cubic-bezier(0.16, 1, 0.3, 1) ease-out;
        background-color: #0b0b0c;
    }
    @keyframes fadeInPage {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* Typography & Custom Headers */
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.5rem;
        background: linear-gradient(45deg, #ffffff, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        color: #888888;
        font-size: 1.25rem;
        margin-bottom: 2rem;
    }
    
    /* Interactive Cards with Subtle Hover Lift & Glow */
    .feature-card {
        border: 1px solid #1e1e20;
        border-radius: 8px;
        padding: 1.5rem;
        background-color: #121214;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .feature-card:hover {
        transform: translateY(-4px);
        border-color: #a855f7;
        box-shadow: 0 10px 25px rgba(168, 85, 247, 0.15);
    }

    /* Global Input Fields Subtle Glow & Pan on Focus */
    div.stTextInput > div > div > input, 
    div.stTextArea > div > div > textarea {
        transition: all 0.3s ease !important;
        border: 1px solid #2e2e2e !important;
        background-color: #121214 !important;
        color: #ffffff !important;
    }
    div.stTextInput > div > div > input:focus, 
    div.stTextArea > div > div > textarea:focus {
        border-color: #a855f7 !important;
        box-shadow: 0 0 12px rgba(168, 85, 247, 0.25) !important;
        transform: translateX(3px); /* Subtle horizontal pan */
    }

    /* Premium Button Transitions */
    div.stButton > button:first-child {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ffffff !important;
        border-radius: 6px !important;
        padding: 0.6rem 2rem !important;
        font-weight: bold !important;
        transition: all 0.25s ease-out !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 24px rgba(168, 85, 247, 0.3) !important;
        background-color: #a855f7 !important;
        color: #ffffff !important;
        border-color: #a855f7 !important;
    }
    div.stButton > button:first-child:active {
        transform: translateY(1px) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Section Content
st.markdown('<div class="hero-title">Divine\'s Web Dev</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">High-performance, ultra-clean websites built to scale your business online.</div>', unsafe_allow_html=True)

# Interactive Call to Action Button
if st.button("Get a Custom Website ⚡"):
    st.switch_page("Request_a_Quote.py")

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# 4. Interactive Services Grid (Hover to test layout animations)
st.subheader("What I Deliver")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="feature-card">
            <h4>⚡ Blazing Fast Speed</h4>
            <p style="color: #888888; font-size: 0.9rem; margin-bottom: 0;">
                Clean backend structures and highly optimized assets to maximize your conversion rates.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <h4>🎨 Premium UI/UX</h4>
            <p style="color: #888888; font-size: 0.9rem; margin-bottom: 0;">
                Minimalist, high-contrast digital interfaces tailored intentionally around your branding.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. Live Micro-Interaction Preview Block
st.subheader("Interactive Playground")
st.caption("Click into the input text area below to witness the purple neon halo and subtle 3px shifting pan effect.")
test_input = st.text_input("Drop a quick idea...", placeholder="Type an innovative concept here...")
