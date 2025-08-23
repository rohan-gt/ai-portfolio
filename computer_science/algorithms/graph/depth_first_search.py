from typing import Optional


def dfs(
    graph: dict[str, set[str]], start: str, visited: Optional[set[str]] = None
) -> set[str]:
    """
    Perform a depth-first search (DFS) on a graph.

    Args:
        graph: A dictionary representing the adjacency list of the graph.
        start: The starting vertex for the DFS.
        visited: A set of visited vertices.

    Returns:
        A set of visited vertices.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


if __name__ == "__main__":
    graph = {
        "A": {"B", "C"},
        "B": {"A", "D", "E"},
        "C": {"A", "F"},
        "D": {"B"},
        "E": {"B", "F"},
        "F": {"C", "E"},
    }
    print("Depth-First Search starting from vertex A:")
    dfs(graph, "A")
