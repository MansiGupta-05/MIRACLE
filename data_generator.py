import random

NUM_NODES = 50000
NUM_EDGES = 200000


def generate_graph():
    graph = {i: [] for i in range(NUM_NODES)}

    # First make sure every node is connected to the next one
    for i in range(NUM_NODES - 1):
        weight = random.randint(1, 20)

        graph[i].append((i + 1, weight))
        graph[i + 1].append((i, weight))

    # Add extra random roads
    edges_added = NUM_NODES - 1

    while edges_added < NUM_EDGES:
        a = random.randint(0, NUM_NODES - 1)
        b = random.randint(0, NUM_NODES - 1)

        if a == b:
            continue

        weight = random.randint(1, 20)

        graph[a].append((b, weight))
        graph[b].append((a, weight))

        edges_added += 1

    return graph

def save_graph(graph):
    import pickle

    with open("graph_data.pkl", "wb") as file:
        pickle.dump(graph, file)

    print("Graph saved to graph_data.pkl")


if __name__ == "__main__":
    graph = generate_graph()

    print("Graph generated successfully!")
    print("Nodes:", len(graph))

    total_edges = sum(len(edges) for edges in graph.values()) // 2
    print("Edges:", total_edges)

    save_graph(graph)