from routing import dijkstra


graph = {
    0: [(1, 4), (2, 2)],
    1: [(0, 4), (2, 1), (3, 5)],
    2: [(0, 2), (1, 1), (3, 8)],
    3: [(1, 5), (2, 8)]
}


closed_roads = {(1, 3)}

distance, route = dijkstra(
    graph,
    0,
    3,
    closed_roads
)

print("Shortest distance:", distance)
print("Route:", route)