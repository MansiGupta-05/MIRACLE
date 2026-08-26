
from routing import dijkstra


def find_best_dispatch(
    graph,
    patient_location,
    ambulances,
    hospitals,
    priority,
    specialist=None,
    required_medicine=None
):
    available_ambulances = [
        a for a in ambulances
        if a["status"] == "available"
    ]

    if not available_ambulances:
        return {
            "status": "failed",
            "reason": "No available ambulance"
        }

    suitable_hospitals = []

    for hospital in hospitals:

        if specialist and specialist != "None":
            if specialist not in hospital["specialists"]:
                continue

        if required_medicine:
            if required_medicine not in hospital["medicines"]:
                continue

        suitable_hospitals.append(hospital)

    if not suitable_hospitals:
        return {
            "status": "failed",
            "reason": "No suitable hospital available"
        }

    best_option = None

    for ambulance in available_ambulances:

        ambulance_distance, ambulance_route = dijkstra(
            graph,
            ambulance["location"],
            patient_location
        )

        if ambulance_distance is None:
            continue

        for hospital in suitable_hospitals:

            hospital_distance, hospital_route = dijkstra(
                graph,
                patient_location,
                hospital["location"]
            )

            if hospital_distance is None:
                continue

            total_distance = (
                ambulance_distance +
                hospital_distance
            )

            option = (
                total_distance,
                ambulance,
                hospital,
                ambulance_route,
                hospital_route
            )

            if best_option is None or total_distance < best_option[0]:
                best_option = option

    if best_option is None:
        return {
            "status": "failed",
            "reason": "No feasible route found"
        }

    distance, ambulance, hospital, ambulance_route, hospital_route = best_option

    return {
        "status": "success",
        "ambulance_id": ambulance["id"],
        "hospital_id": hospital["id"],
        "distance": distance,
        "ambulance_route": ambulance_route,
        "hospital_route": hospital_route,
        "priority": priority,
        "reason": (
    f"{ambulance['id']} selected because it is the nearest "
    f"available ambulance with a feasible route. "
    f"{hospital['id']} selected because it has the required "
    f"specialist ({specialist})."
)
    }