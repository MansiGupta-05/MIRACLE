import pickle
import time
from routing import dijkstra


print("Loading graph...")

with open("graph_data.pkl", "rb") as file:
    graph = pickle.load(file)

print("Graph loaded!")
print("Nodes:", len(graph))

start_node = 0
end_node = 49999

print("\nFinding shortest route...")
start_time = time.time()

distance, route = dijkstra(graph, start_node, end_node)

end_time = time.time()

if distance is not None:
    print("Shortest distance:", distance)
    print("Number of nodes in route:", len(route))
    print("Execution time:", round(end_time - start_time, 4), "seconds")
else:
    print("No route found.")