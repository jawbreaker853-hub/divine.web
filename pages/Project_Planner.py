import streamlit as st

st.set_page_config(page_title="Project Planner | Divine's Web Dev", page_icon="📝", layout="centered")

# Shared Animation, Glow, & Input CSS
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
    
    /* Input formatting & Glows */
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
    
    /* Submit Button styling */
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

st.markdown('<div class="main-title">Design Your Website 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Fill out the planner below to outline your perfect digital workspace.</div>', unsafe_allow_html=True)
st.divider()

with st.form(key="detailed_planner_form", clear_on_submit=True):
    st.subheader("📋 Contact Details")
    c1, c2 = st.columns(2)
    with c1:
        client_name = st.text_input("Name *")
    with c2:
        client_email = st.text_input("Email *")

    st.subheader("💡 Website Vision")
    site_title = st.text_input("Desired Website / Business Name")
    
    # Custom project configurations
    site_type = st.selectbox(
        "What type of website do you need?",
        ["E-Commerce / Online Store", "Business Profile Portfolio", "Landing Page / Single Product Sales", "Custom SaaS / Web Application Platform"]
    )
    
    # Checkboxes for dynamic scope picking
    st.write("**What special features do you want included? (Select all that apply)**")
    col_feat1, col_feat2 = st.columns(2)
    with col_feat1:
        feat_contact = st.checkbox("Contact / Lead Capture Forms")
        feat_payment = st.checkbox("Payment Processing Gateway")
    with col_feat2:
        feat_blog = st.checkbox("Blog / Content Management System")
        feat_dark = st.checkbox("Dark Mode / Custom Toggle Theme Layout")

    # Detailed specifications area
    user_requirements = st.text_area(
        "Tell me exactly what you want your website to achieve *",
        placeholder="Example: I need a clean portfolio site to exhibit my photography work. I want a dark layout with high contrast, an integrated booking system, an active blog segment, and a custom animation sequence on my image grids...",
        height=180
    )

    st.subheader("💰 Scope Estimation")
    col_scope1, col_scope2 = st.columns(2)
    with col_scope1:
        budget = st.selectbox("Estimated Investment Budget", ["$500 - $1,000", "$1,000 - $2,500", "$2,500 - $5,000", "$5,000+"])
    with col_scope2:
        deadline = st.selectbox("Urgency", ["Within 1 Week", "2-3 Weeks", "1 Month", "Flexible Schedule"])

    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.form_submit_button(label="Send Specification Blueprint")

if submit:
    if not client_name or not client_email or not user_requirements:
        st.error("Please fill out all mandatory fields (*) so I can review your strategy!")
    else:
        st.success(f"Excellent, {client_name}! Your architecture preferences for '{site_title}' have been logged. Divine's Web Dev will analyze this data and reach out via {client_email} shortly.")