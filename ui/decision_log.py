import streamlit as st


def show_decision_log(logs):
    st.subheader("Decision Log")

    if not logs:
        st.info("No decisions recorded yet.")
        return

    for message in logs:
        st.write(f"✓ {message}")
