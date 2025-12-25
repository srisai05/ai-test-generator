import streamlit as st
import logging
import sys, os
sys.path.append(os.path.abspath("."))
from logging.handlers import RotatingFileHandler
from src.generator import generate_test_cases
from src.security import validate_requirements

# ================= LOGGING SETUP =================
LOG_PATH = "logs/app.log"
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Avoid duplicate handlers

if not logger.handlers:
    handler = RotatingFileHandler(LOG_PATH, maxBytes=500000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.info("Streamlit UI Loaded")


# ================= STREAMLIT PAGE CONFIG =================
st.set_page_config(page_title="AI Test Cases Generator", layout="wide")

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.header-box {
    background: linear-gradient(135deg, #1b6cf2, #6c9dfb);
    padding: 18px;
    border-radius: 12px;
    color: white;
    font-size:20px;
    font-weight:600;
}
.info-box {
    border: 2px solid #1b6cf2;
    padding: 12px;
    border-radius:10px;
    background:#f7f9ff;
}
.footer {
    margin-top: 40px;
    text-align:center;
    color:#666;
}
</style>
""", unsafe_allow_html=True)


# ================= HEADER =================
st.markdown(
    '<div class="header-box">🧪 AI QA Test Suite Generator</div>',
    unsafe_allow_html=True
)

st.write("""
This tool converts **plain requirements** into professionally structured:
- Functional Test Cases  
- Boundary Test Cases  
- Negative Test Cases  
- Edge Cases  
- Acceptance Criteria
""")



# ================= MAIN INPUT =================
st.subheader("✍️ Enter Requirement")
requirement = st.text_area("Paste Requirement Here", height=200, placeholder="Example: User should be able to login using username and password...")

generate = st.button("Generate Test Cases")

if generate:
    try:
        logger.info("User clicked Generate Test Cases")

        if not requirement.strip():
            st.error("Requirement cannot be empty!")
            logger.warning("Empty requirement submitted")
        else:
            validate_requirements(requirement)
            logger.info("Requirement validation successful")

            with st.spinner("Generating AI Test Cases... Please wait..."):
                result = generate_test_cases(requirement)

            st.success("Test Cases Generated Successfully")
            st.subheader("📌 Generated Test Cases")
            st.code(result, language="markdown")

            # Download Button
            st.download_button(
                label="⬇️ Download Test Cases",
                data=result,
                file_name="generated_test_cases.txt",
                mime="text/plain"
            )

            logger.info("Test Cases delivered successfully to UI")

    except Exception as e:
        logger.exception("Streamlit Execution Failed")
        st.error(f"❌ Error: {str(e)}")

