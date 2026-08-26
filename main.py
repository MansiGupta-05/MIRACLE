import pickle
import streamlit as st

from allocation import find_best_dispatch


# Load road network
with open("graph_data.pkl", "rb") as file:
    graph = pickle.load(file)


# -----------------------------
# Initialize demo resources
# -----------------------------

def initialize_resources():

    if "ambulances" not in st.session_state:

        st.session_state.ambulances = [
            {
                "id": "A01",
                "location": 100,
                "status": "available"
            },
            {
                "id": "A02",
                "location": 500,
                "status": "available"
            },
            {
                "id": "A03",
                "location": 1500,
                "status": "available"
            }
        ]

    if "hospitals" not in st.session_state:

        st.session_state.hospitals = [
            {
                "id": "H01",
                "location": 1000,
                "specialists": [
                    "Cardiologist",
                    "General Physician"
                ],
                "medicines": [
                    "Emergency",
                    "Heart"
                ]
            },
            {
                "id": "H02",
                "location": 2000,
                "specialists": [
                    "General Physician",
                    "Pediatrician"
                ],
                "medicines": [
                    "Emergency",
                    "Pediatric"
                ]
            },
            {
                "id": "H03",
                "location": 3000,
                "specialists": [
                    "Cardiologist",
                    "Pediatrician"
                ],
                "medicines": [
                    "Emergency",
                    "Heart",
                    "Pediatric"
                ]
            }
        ]


# -----------------------------
# Dispatch emergency
# -----------------------------

def dispatch_emergency(
    patient_location,
    priority,
    required_resource,
    specialist
):

    initialize_resources()

    result = find_best_dispatch(
        graph=graph,
        patient_location=patient_location,
        ambulances=st.session_state.ambulances,
        hospitals=st.session_state.hospitals,
        priority=priority,
        specialist=specialist
    )

    # If dispatch succeeded
    if result.get("status") == "success":

        ambulance_id = result["ambulance_id"]

        # Change ambulance status
        for ambulance in st.session_state.ambulances:

            if ambulance["id"] == ambulance_id:
                ambulance["status"] = "dispatched"

    return result