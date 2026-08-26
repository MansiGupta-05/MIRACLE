import heapq


def dijkstra(graph, start, end, closed_roads=None):
    if closed_roads is None:
        closed_roads = set()

    distances = {start: 0}
    previous = {}
    
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)

        if current == end:
            break

        if current_distance > distances.get(current, float("inf")):
            continue

        for neighbor, weight in graph[current]:

            road = tuple(sorted((current, neighbor)))

            if road in closed_roads:
                continue

            new_distance = current_distance + weight

            if new_distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    if end not in distances:
        return None, []

    # Reconstruct route
    route = []
    current = end

    while current != start:
        route.append(current)
        current = previous[current]

    route.append(start)
    route.reverse()

    return distances[end], route