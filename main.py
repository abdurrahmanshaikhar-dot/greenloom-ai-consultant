import streamlit as st
from main import run_analysis

st.set_page_config(
    page_title="AI Business Consultant",
    page_icon="📊",
    layout="wide"
)

with st.sidebar:
    st.header("About")

    st.write("""
    Multi-Agent Business Consultant

    Agents:
    - Research Analyst
    - Strategy Consultant
    - Report Writer

    Powered by:
    - CrewAI
    - OpenRouter
    - Streamlit
    """)
    
st.title("📊 AI Business Consultant")

st.markdown("""
Generate executive-level business analysis and strategic recommendations using a multi-agent AI system built with CrewAI.
""")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input(
        "Company Name",
        placeholder="Tesla"
    )

with col2:
    industry = st.text_input(
        "Industry",
        placeholder="Automotive"
    )

problem = st.text_area(
    "Business Problem",
    placeholder="Sales have declined by 20% over the last year..."
)

if st.button("🚀 Generate Strategic Report"):

    if company and problem:

        with st.spinner("AI Agents are working..."):

            report = run_analysis(
                company,
                problem
            )

        st.success("Analysis Complete")

        st.download_button(
            "📥 Download Report",
            report,
            file_name=f"{company}_report.md"
        )

        st.markdown(report)

    else:
        st.warning(
            "Please complete all required fields."
        )