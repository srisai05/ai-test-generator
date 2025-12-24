import streamlit as st
from security import validate_requirements
from generator import generate_test_cases

st.set_page_config(page_title="AI Test Case Generator", layout="wide")

# ======= CUSTOM CSS UI =========
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
.button-style {
    background:#1b6cf2;
    color:white;
    padding:10px 20px;
    border-radius:10px;
    font-weight:600;
}
</style>
""", unsafe_allow_html=True)

# ======= HEADER =========
st.markdown('<div class="header-box">🧪 AI TEST CASE GENERATOR – Using Local OLLAMA</div>', unsafe_allow_html=True)

st.write("")
st.write("""
This tool converts **plain requirements** into:
- Functional Test Cases  
- Boundary Test Cases  
- Negative Test Cases  
- Edge Cases  
- Acceptance Criteria
""")

# ======= API KEY & SECURITY NOTE =========
st.markdown("""
<div class="info-box">
<b>🔐 Security & API Key Information</b><br>
✔ This project does NOT require API Key<br>
✔ Uses Secure Local OLLAMA Gen-AI Engine<br>
✔ No cloud dependency – Completely Offline<br>
✔ Data Never Leaves System<br>
</div>
""", unsafe_allow_html=True)

# ======= MAIN INPUT =========
st.subheader("✍️ Enter Requirement")
requirement = st.text_area("Paste Requirement Here", height=200)

if st.button("Generate Test Cases"):
    try:
        validate_requirements(requirement)
        result = generate_test_cases(requirement)
        
        st.success("Test Cases Generated Successfully")
        st.subheader("📌 Generated Test Cases")
        st.code(result, language="markdown")

    except Exception as e:
        st.error(str(e))

# ======= CONFIG & LOG INFO =========
st.markdown("""
<div class="info-box">
<b>⚙️ Configuration & Engineering Practices Followed</b><br>
✔ Configuration Managed via settings.yaml<br>
✔ Centralized Logging Enabled<br>
✔ Secure Input Validation Implemented<br>
✔ Structured Modular Code<br>
✔ Professional Engineering Standards Followed
</div>
""", unsafe_allow_html=True)

