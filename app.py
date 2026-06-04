import streamlit as st
from main import generate_report

st.set_page_config(
    page_title="AI Business Consultant",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("About")

    st.write("""
AI Business Consultant

Built with:
- CrewAI
- OpenRouter
- Multi-Agent Architecture
- DuckDuckGo Search

Agents:
- Research Analyst
- Strategy Consultant
- Report Writer
""")

# ==================================================
# MAIN PAGE
# ==================================================

st.title("📊 AI Business Consultant")

st.write("Analyze a company and generate strategic recommendations.")

company = st.text_input(
    "Company Name",
    placeholder="Tesla"
)

problem = st.text_area(
    "Business Problem",
    placeholder="Vehicle sales are declining..."
)

if st.button("Generate Report"):

    if company and problem:

        with st.spinner("Running AI Agents..."):

            report = generate_report(company, problem)

        st.success("Report Generated Successfully")

        st.markdown(report)

    else:
        st.warning("Please enter company name and business problem.")