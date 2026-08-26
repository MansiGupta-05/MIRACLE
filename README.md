# MIRACLE

## Rural Healthcare Dispatch System
### Real-Time Emergency Resource Allocation & Routing

## Project Overview

MIRACLE is a Rural Healthcare Dispatch System designed to help manage emergency healthcare requests in rural areas.

The system receives an emergency request from a village and selects a suitable available ambulance and hospital. It considers ambulance availability, required specialist, hospital suitability, and road-network routes.

The system displays:
- Selected ambulance
- Selected hospital
- Total distance
- Estimated travel time
- Calculated route
- Emergency priority
- Decision reason

## Technologies Used

- Python
- Streamlit
- Graph-based routing
- Dijkstra's Shortest Path Algorithm
- Python Pickle for storing the road network

## Setup / Run Instructions

### Requirements

- Python 3.12 or later
- pip

### Installation

Clone the repository and open the project folder.

Install the required dependencies:

```bash
pip install -r requirements.txt

## Algorithm / Approach

The system follows these steps:

1. Receive an emergency request from the user.
2. Check available ambulances.
3. Filter hospitals according to the required specialist.
4. Calculate the route from each available ambulance to the patient.
5. Calculate the route from the patient to each suitable hospital.
6. Calculate the total travel distance.
7. Select the feasible ambulance-hospital combination with the minimum total distance.
8. Display the dispatch result, route, ETA, and decision reason.

### Routing Algorithm

Dijkstra's shortest path algorithm is used to calculate routes through the road network.

The total distance is calculated as:

Ambulance → Patient + Patient → Hospital

The combination with the shortest feasible total distance is selected.

## Testing / Test Cases

### Test Case 1: Critical Emergency
- Input: Critical priority with a required specialist.
- Expected Result: An available ambulance and suitable hospital are selected.

### Test Case 2: No Available Ambulance
- Input: All available ambulances are unavailable.
- Expected Result: The system returns "No available ambulance".

### Test Case 3: Specialist Requirement
- Input: A specific specialist such as Cardiologist.
- Expected Result: Hospitals without the required specialist are excluded.

### Test Case 4: No Feasible Route
- Input: Locations with no valid route.
- Expected Result: The system returns "No feasible route found".

## Third-Party APIs and AI Tools

### Third-Party APIs
No third-party APIs are used in the current implementation.

### AI Tools
AI tools were used during development for coding assistance, debugging, and documentation support.
