import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.rag_pipeline import generate_answer
from src.config import SAFETY_DISCLAIMER


st.set_page_config(page_title="Clinical RAG Assistant", layout="wide")

st.title("🩺 Clinical Diagnosis Support Assistant")

st.warning(SAFETY_DISCLAIMER)

query = st.text_area("Enter patient symptoms:", height=150)

if st.button("Analyze"):
    if query.strip() == "":
        st.error("Please enter symptoms.")
    else:
        with st.spinner("Analyzing..."):
            escalation, response = generate_answer(query)

        if escalation:
            st.error(escalation)

        st.markdown("## Results")
        st.write(response)
