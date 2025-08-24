from collections import deque


def breadth_first_search(graph: dict[str, set[str]], start: str) -> None:
    """
    Perform a breadth-first search (BFS) on a graph.

    Args:
        graph: A dictionary representing the adjacency list of the graph.
        start: The starting vertex for the BFS.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    graph = {
        "A": {"B", "C"},
        "B": {"A", "D", "E"},
        "C": {"A", "F"},
        "D": {"B"},
        "E": {"B", "F"},
        "F": {"C", "E"},
    }
    print("Breadth-First Search starting from vertex A:")
    breadth_first_search(graph, "A")
