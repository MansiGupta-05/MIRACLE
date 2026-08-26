
import pickle
from allocation import find_best_dispatch

print("Loading graph...")

with open("graph_data.pkl", "rb") as file:
    graph = pickle.load(file)




ambulances = [
    {
        "id": "A01",
        "location": 100,
        "status": "available"
    },
    {
        "id": "A02",
        "location": 500,
        "status": "available"
    }
]


hospitals = [
    {
        "id": "H01",
        "location": 1000,
        "specialists": ["Cardiologist", "General Physician"],
        "medicines": ["Emergency", "Heart"]
    },
    {
        "id": "H02",
        "location": 2000,
        "specialists": ["General Physician"],
        "medicines": ["Emergency"]
    }
]


result = find_best_dispatch(
    graph=graph,
    patient_location=5000,
    ambulances=ambulances,
    hospitals=hospitals,
    priority="Critical",
    specialist="Cardiologist"
)


print("\nRESULT")
print(result)