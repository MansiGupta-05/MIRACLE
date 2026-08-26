import streamlit as st


def show_dispatch_result(result):
    st.subheader("Dispatch Result")

    if not result:
        st.info("Submit an emergency request to view the dispatch result.")
        return

    if result.get("status") != "success":
        st.error("Dispatch could not be completed.")
        return

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Ambulance", result.get("ambulance_id", "N/A"))
        st.metric("Hospital", result.get("hospital_id", "N/A"))
        st.metric("Priority", result.get("priority", "N/A"))

    with col2:
        st.metric("Distance", f"{result.get('distance_km', 0)} km")
        st.metric("ETA", f"{result.get('eta_minutes', 0)} min")

    st.markdown("### Route")

    route = result.get("route", [])

    if route:
        st.code(" → ".join(route))
    else:
        st.write("Route unavailable.")

    st.markdown("### Decision Reason")
    st.success(result.get("reason", "No reason provided."))
