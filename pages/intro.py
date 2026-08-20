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
# LOAD GLOBAL CSS
# =========================================================

css_file = Path(__file__).parent.parent / "style.css"

with open(css_file, encoding="utf-8") as f:
    css = f.read()

st.html(f"<style>{css}</style>")


# =========================================================
# INTRODUCTION
# =========================================================

st.html("""
<div class="intro-hero">

    <h1>Before We Get Started...</h1>

</div>
""")


# =========================================================
# STATISTICS
# =========================================================

st.html("""
<div class="stats-container">

    <div class="stat-card">

        <div class="stat-number">5.5m</div>

        <div class="stat-title">
            Small organisations in the UK
        </div>

        <div class="stat-description">
            The UK has approximately 5.5 million small organisations
            with between 0 and 49 employees.
        </div>

        <div class="stat-source">
            SOURCE: NCSC
        </div>

    </div>


    <div class="stat-card">

        <div class="stat-number">50%</div>

        <div class="stat-title">
            Experience a cyber incident
        </div>

        <div class="stat-description">
            Around 1 in 2 small businesses experience a cyber incident
            every year.
        </div>

        <div class="stat-source">
            SOURCE: NCSC
        </div>

    </div>


    <div class="stat-card">

        <div class="stat-number">1 in 2</div>

        <div class="stat-title">
            Small businesses are affected
        </div>

        <div class="stat-description">
            Being a small organisation does not mean being too small
            to become a target.
        </div>

        <div class="stat-source">
            SOURCE: NCSC
        </div>

    </div>

</div>
""")


# =========================================================
# WHY CYBERSEC CHECK?
# =========================================================

st.html("""
<div class="intro-info">

    <h2>Why CyberSec Check?</h2>

    <p>
        Cybersecurity guidance can often be difficult for
        non-technical users to understand. CyberSec Check aims
        to translate cybersecurity concepts into simple,
        practical questions and recommendations that small
        businesses can understand and act upon.
    </p>

    <p>
        The assessment will guide you through a series of
        questions about your current cybersecurity practices.
        Your answers will then be used to identify areas where
        improvements could be beneficial.
    </p>

</div>
""")


# =========================================================
# DISCLAIMER
# =========================================================

st.html("""
<div class="intro-disclaimer">

    <h3>⚠ Important Disclaimer</h3>

    <p>
        CyberSec Check is an educational and awareness tool.
        It is designed to provide general guidance based on
        the information provided by the user and should not
        be considered a professional cybersecurity assessment,
        audit, penetration test, or guarantee of security.
    </p>

    <p>
        The recommendations provided are intended to help
        identify potential areas for improvement and should
        not be treated as a substitute for professional
        cybersecurity advice where this is required.
    </p>

</div>
""")


# =========================================================
# START ASSESSMENT
# =========================================================




if st.button("START ASSESSMENT  →"):
    st.switch_page("pages/assessment.py")