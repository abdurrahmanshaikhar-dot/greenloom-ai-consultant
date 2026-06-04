import streamlit as st

from main import run_analysis

st.set_page_config(
    page_title="AI Business Consultant",
    page_icon="📊"
)

st.title("📊 AI Business Consultant")

st.write(
    "Analyze a company and generate strategic recommendations."
)

company = st.text_input("Company Name")

problem = st.text_area(
    "Business Problem",
    placeholder="Subscriber growth has slowed..."
)

if st.button("Generate Report"):

    if company and problem:

        with st.spinner("Generating report..."):

            report = run_analysis(
                company,
                problem
            )

        st.success("Report Generated")

        st.markdown(report)

    else:
        st.warning(
            "Please enter company name and business problem."
        )