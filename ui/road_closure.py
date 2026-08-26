import streamlit as st


def show_road_closure():
    st.subheader("Road Closure Simulation")

    with st.form("road_closure_form"):
        road_id = st.text_input(
            "Road ID",
            placeholder="Example: R102",
        )

        action = st.selectbox(
            "Action",
            ["Close Road", "Open Road"],
        )

        submitted = st.form_submit_button(
            "UPDATE ROAD",
            use_container_width=True,
        )

    if submitted:
        road_id = road_id.strip()

        if not road_id:
            st.warning("Please enter a Road ID.")
            return None

        return {
            "road_id": road_id,
            "action": action,
        }

    return None
