import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Request a Quote | Divine's Web Dev", 
    page_icon="💻", 
    layout="centered"
)

# 2. Shared Animation, Glow, & Minimalist CSS (Matches Homepage)
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

    /* Typography */
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.5rem;
        background: linear-gradient(45deg, #ffffff, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        color: #888888;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Global Input Fields Subtle Glow & Pan on Focus */
    div.stTextInput > div > div > input, 
    div.stTextArea > div > div > textarea,
    div.stSelectbox > div > div > div {
        transition: all 0.3s ease !important;
        border: 1px solid #2e2e2e !important;
        background-color: #121214 !important;
        color: #ffffff !important;
    }
    div.stTextInput > div > div > input:focus, 
    div.stTextArea > div > div > textarea:focus {
        border-color: #a855f7 !important;
        box-shadow: 0 0 12px rgba(168, 85, 247, 0.25) !important;
        transform: translateX(3px);
    }

    /* Premium Form Button Transitions */
    div.stButton > button:first-child {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ffffff !important;
        border-radius: 6px !important;
        padding: 0.6rem 2rem !important;
        font-weight: bold !important;
        transition: all 0.25s ease-out !important;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(168, 85, 247, 0.3) !important;
        background-color: #a855f7 !important;
        color: #ffffff !important;
        border-color: #a855f7 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Setup
st.markdown('<div class="main-title">Bring Your Vision to Life 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tell me what you need, and Divine\'s Web Dev will build it.</div>', unsafe_allow_html=True)
st.divider()

# 4. Interactive Request Form
with st.form(key="project_request_form", clear_on_submit=True):
    st.subheader("1. Contact Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name *")
    with col2:
        email = st.text_input("Email Address *")
        
    st.subheader("2. Project Details")
    biz_name = st.text_input("Business / Website Name")
    
    project_desc = st.text_area(
        "Describe your ideal website *", 
        placeholder="Example: I need a clean, dark-themed 5-page website for my brand. It needs a smooth layout, a way to display my work, and a quick contact channel...",
        height=150
    )
    
    st.subheader("3. Scope & Budget")
    col3, col4 = st.columns(2)
    with col3:
        project_type = st.selectbox(
            "Project Type",
            ["Simple Landing Page", "Multi-page Business Site", "E-commerce Store", "Custom Web Application"]
        )
    with col4:
        timeline = st.selectbox(
            "Expected Timeline",
            ["As soon as possible", "1-2 Weeks", "3-4 Weeks", "Flexible"]
        )

    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button(label="Submit Project Request")

# 5. Submission Logic
if submit_button:
    if not name or not email or not project_desc:
        st.error("Please fill out all required fields (*) so I can get back to you!")
    else:
        st.success(f"Thank you, {name}! Your request has been sent to Divine's Web Dev. I will review your vision and email you at {email} within 24 hours.")