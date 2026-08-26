NETWORK_STATS = {
    "nodes": 50247,
    "road_edges": 201832,
    "villages": 5184,
    "ambulances": 128,
    "active_requests": 317,
}

VILLAGES = [
    "Village_101",
    "Village_205",
    "Village_382",
    "Village_417",
    "Village_509",
]

PRIORITIES = [
    "Critical",
    "High",
    "Medium",
    "Low",
]

RESOURCES = [
    "Ambulance",
    "Doctor",
    "Medicine",
    "Ambulance + Doctor",
]

SPECIALISTS = [
    "None",
    "Cardiologist",
    "General Physician",
    "Pediatrician",
]

DEMO_DISPATCH_RESULT = {
    "status": "success",
    "ambulance_id": "A27",
    "hospital_id": "H12",
    "distance_km": 34.2,
    "eta_minutes": 41,
    "priority": "Critical",
    "route": ["V382", "N102", "N391", "H12"],
    "reason": "Nearest feasible hospital with required specialist.",
}
