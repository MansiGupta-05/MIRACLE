import streamlit as st


def show_dashboard(stats):
    st.subheader("Network Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Network Nodes", f"{stats['nodes']:,}")
        st.metric("Villages", f"{stats['villages']:,}")

    with col2:
        st.metric("Road Edges", f"{stats['road_edges']:,}")
        st.metric("Ambulances", f"{stats['ambulances']:,}")

    with col3:
        st.metric("Active Requests", f"{stats['active_requests']:,}")
