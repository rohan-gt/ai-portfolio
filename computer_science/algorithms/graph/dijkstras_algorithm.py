import heapq


def dijkstra(graph: dict[str, dict[str, int]], start: str) -> dict[str, int]:
    """
    Perform Dijkstra's algorithm to find the shortest paths from a starting vertex.

    Args:
        graph: A dictionary representing the adjacency list of the graph with edge weights.
        start: The starting vertex for Dijkstra's algorithm.

    Returns:
        A dictionary with the shortest distances from the start vertex to each vertex.
    """
    queue: list = []
    heapq.heappush(queue, (0, start))
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # Convert distances to integers
    return {vertex: int(distance) for vertex, distance in distances.items()}


if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "D": 2, "E": 5},
        "C": {"A": 4, "F": 3},
        "D": {"B": 2},
        "E": {"B": 5, "F": 1},
        "F": {"C": 3, "E": 1},
    }
    print("Dijkstra's shortest paths from vertex A:")
    distances = dijkstra(graph, "A")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")
