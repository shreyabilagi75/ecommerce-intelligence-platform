"""Streamlit entry point / page router.  Run with: streamlit run app.py"""
import streamlit as st

st.set_page_config(page_title="E-Commerce Intelligence Platform", layout="wide")

pages = [
    st.Page("pages/overview.py", title="Overview", icon="📊", default=True),
    st.Page("pages/customer_analytics.py", title="Customer Analytics", icon="👥"),
    st.Page("pages/recommendations.py", title="Product Recommendations", icon="🛍️"),
    st.Page("pages/churn.py", title="Churn Intelligence", icon="⚠️"),
    st.Page("pages/scenario.py", title="Business Impact (Simulator)", icon="💷"),
    st.Page("pages/evaluation.py", title="Model Evaluation", icon="🧪"),
    st.Page("pages/methodology.py", title="Data & Methodology", icon="📚"),
]
st.navigation(pages).run()
