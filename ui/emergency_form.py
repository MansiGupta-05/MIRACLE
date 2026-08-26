import streamlit as st


def show_emergency_form(villages, priorities, resources, specialists):
    st.subheader("Emergency Request")

    with st.form("emergency_form"):
        village = st.selectbox("Patient / Village", villages)

        priority = st.selectbox("Emergency Priority", priorities)

        resource = st.selectbox("Required Resource", resources)

        specialist = st.selectbox("Specialist Required", specialists)

        submitted = st.form_submit_button(
            "DISPATCH",
            use_container_width=True,
        )

    if submitted:
        return {
            "patient_location": village,
            "priority": priority,
            "required_resource": resource,
            "specialist": specialist,
        }

    return None
