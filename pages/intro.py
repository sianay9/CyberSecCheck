import streamlit as st
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CyberSec Check - Introduction",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# LOAD CSS
# =========================================================

def load_css():
    css_file = Path(__file__).parent.parent / "style.css"

    with open(css_file, encoding="utf-8") as f:
        css = f.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )


load_css()


# =========================================================
# INTRODUCTION PAGE
# =========================================================

st.title("HELLO WORLD 👋")

st.write("Welcome to CyberSec Check.")