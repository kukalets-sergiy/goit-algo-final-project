"""Task 3: Dijkstra's algorithm with a binary min-heap."""

TASK_INSTRUCTIONS = (
    f"Input: a hardcoded weighted graph with vertices A, B, C, D, and E; start vertex A.\n"
    f"Processing: Dijkstra's algorithm uses a binary min-heap.\n"
    f"Output: shortest distances from A to every vertex."
)

import heapq


def dijkstra(graph, start):
    """Return the shortest distances from start to all vertices."""
    # Check that the start vertex exists in the graph.
    if start not in graph:
        raise ValueError(f"Start vertex {start!r} is missing from the graph.")
    # Initialize all distances to infinity.
    distances = {vertex: float("inf") for vertex in graph}
    # Set the distance to the start vertex to zero.
    distances[start] = 0
    # Create a min-heap with the start vertex.
    queue = [(0, start)]
    # Process vertices in order of increasing distance.
    while queue:
        # Remove the vertex with the smallest known distance.
        current_distance, current = heapq.heappop(queue)
        # Skip an outdated heap entry.
        if current_distance > distances[current]:
            continue
        # Check all neighbors of the current vertex.
        for neighbor, weight in graph[current]:
            # Dijkstra's algorithm does not allow negative edge weights.
            if weight < 0:
                raise ValueError("Вага ребра не може бути від'ємною.")
            # Calculate the distance through the current vertex.
            new_distance = current_distance + weight
            # Update the best distance if a shorter path was found.
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # Add the improved candidate to the min-heap.
                heapq.heappush(queue, (new_distance, neighbor))
    # Return the distances to all vertices.
    return distances


if __name__ == "__main__":
    # Print the task instructions.
    print(TASK_INSTRUCTIONS)
    # Create a weighted graph using adjacency lists.
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)],
    }
    # Calculate the shortest distances from vertex A.
    distances = dijkstra(graph, "A")
    # Print the result in a stable order.
    for vertex, distance in distances.items():
        # Display the vertex and its shortest distance.
        print(f"Shortest distance from A to {vertex}: {distance}")

