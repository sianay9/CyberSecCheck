import streamlit as st
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CyberSec Check – Assessment",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# LOAD GLOBAL CSS
# =========================================================

def load_css():
    css_file = Path(__file__).parent.parent / "style.css"

    with open(css_file, encoding="utf-8") as f:
        css = f.read()

    st.html(f"<style>{css}</style>")


load_css()


# =========================================================
# TEST PAGE
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-title">
        Assessment
    </div>

    <div class="hero-subtitle">
        Hello World 👋
        <br><br>
        If you're seeing this, the assessment page is working!
    </div>

</div>
""")