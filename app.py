import streamlit as st
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CyberSec Check",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# LOAD CSS
# =========================================================

def load_css():
    css_file = Path(__file__).parent / "style.css"

    with open(css_file, encoding="utf-8") as f:
        css = f.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )


load_css()


# =========================================================
# HOME PAGE
# =========================================================

st.html("""
<div class="hero">


    <div class="hero-title">
        CyberSec Check
    </div>

    <div class="hero-subtitle">
        CyberSec Check is an interactive cybersecurity awareness
                tool designed to help small businesses understand their
                current security practices and identify practical areas
                for improvement.
    </div>

</div>
""")



# =========================================================
# FEAUTRES
# =========================================================




col1, col2, col3 = st.columns(3)


with col1:
    st.html("""
    <div class="feature-card">


        <h3>📝 1. Answer</h3>

        <p>
            Work through a series of simple questions about
            your business's current cybersecurity practices.
        </p>

    </div>
    """)


with col2:
    st.html("""
    <div class="feature-card">

    

        <h3>🔍 2. Understand</h3>

        <p>
            Learn why each area matters and understand where
            your business could be vulnerable.
        </p>

    </div>
    """)


with col3:
    st.html("""
    <div class="feature-card">


        <h3>💡 3. Improve</h3>

        <p>
            Receive practical, prioritised recommendations
            to help improve your cybersecurity.
        </p>

    </div>
    """)


# =========================================================
# START ASSESSMENT
# =========================================================




if st.button("START ASSESSMENT  →"):
    st.switch_page("pages/intro.py")