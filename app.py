import streamlit as st
import re

from main import dispatch_emergency, initialize_resources

from data.demo_data import (
    NETWORK_STATS,
    VILLAGES,
    PRIORITIES,
    RESOURCES,
    SPECIALISTS,
)

from ui.dashboard import show_dashboard
from ui.emergency_form import show_emergency_form
from ui.dispatch_result import show_dispatch_result
from ui.road_closure import show_road_closure
from ui.decision_log import show_decision_log


st.set_page_config(
    page_title="Rural Healthcare Dispatch System",
    page_icon="🚑",
    layout="wide",
)


st.markdown(
    """
    <style>
        .main-title {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 18px;
            color: #666666;
            margin-bottom: 25px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


if "dispatch_result" not in st.session_state:
    st.session_state.dispatch_result = None

if "decision_logs" not in st.session_state:
    st.session_state.decision_logs = []

initialize_resources()


st.markdown(
    '<div class="main-title">🚑 Rural Healthcare Dispatch System</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Real-Time Emergency Resource Allocation & Routing</div>',
    unsafe_allow_html=True,
)

st.divider()


# Network statistics
# Network statistics
dashboard_stats = NETWORK_STATS.copy()

dashboard_stats["ambulances"] = sum(
    1
    for ambulance in st.session_state.ambulances
    if ambulance["status"] == "available"
)

show_dashboard(dashboard_stats)

st.divider()


left_column, right_column = st.columns([1, 1])


# =========================
# EMERGENCY REQUEST
# =========================

with left_column:

    request = show_emergency_form(
        VILLAGES,
        PRIORITIES,
        RESOURCES,
        SPECIALISTS
    )

    if request:

        # Convert Village_101 → 101
        village_name = request["patient_location"]

        numbers = re.findall(r"\d+", str(village_name))

        if numbers:
            patient_location = int(numbers[0])
        else:
            patient_location = 5000

        # Call YOUR real backend
        result = dispatch_emergency(
            patient_location=patient_location,
            priority=request["priority"],
            required_resource=request["required_resource"],
            specialist=request["specialist"]
        )

        # Convert backend result into the format expected by UI
        if result.get("status") == "success":

            ambulance_route = result.get("ambulance_route", [])
            hospital_route = result.get("hospital_route", [])

            # Join both routes for display
            route = ambulance_route + hospital_route[1:]

            st.session_state.dispatch_result = {
                "status": "success",
                "ambulance_id": result.get("ambulance_id"),
                "hospital_id": result.get("hospital_id"),
                "distance_km": result.get("distance", 0),
                "eta_minutes": result.get("distance", 0) * 2,
                "route": [str(node) for node in route],
                "priority": result.get("priority"),
                "reason": result.get("reason")
            }

            st.session_state.decision_logs = [
                "Emergency request received",
                f"Priority classified as {request['priority']}",
                f"Checking resource: {request['required_resource']}",
                f"Checking specialist: {request['specialist']}",
                "Available ambulances checked",
                "Suitable hospital found",
                "Shortest route calculated using Dijkstra",
                "Ambulance dispatched"
            ]

        else:

            st.session_state.dispatch_result = result

            st.session_state.decision_logs = [
                "Emergency request received",
                f"Priority classified as {request['priority']}",
                "Checking available ambulances",
                "Checking suitable hospitals",
                f"Dispatch failed: {result.get('reason', 'Unknown reason')}"
            ]


# =========================
# DISPATCH RESULT
# =========================

with right_column:

    show_dispatch_result(
        st.session_state.dispatch_result
    )


st.divider()


# =========================
# ROAD CLOSURE
# =========================

left_column, right_column = st.columns([1, 1])


with left_column:

    road_update = show_road_closure()

    if road_update:

        road_id = road_update["road_id"]
        action = road_update["action"]

        if action == "Close Road":

            message = f"Road {road_id} closed. Route recalculation required."

            st.warning(message)

        else:

            message = f"Road {road_id} opened."

            st.success(message)


# =========================
# DECISION LOG
# =========================

with right_column:

    show_decision_log(
        st.session_state.decision_logs
    )


st.divider()

