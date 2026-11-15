"""Task 5: iterative visualization of DFS and BFS."""

f"Libraries required: matplotlib and networkx. Install them with: pip install -r requirements.txt"

TASK_INSTRUCTIONS = (
    f"Input: hardcoded heap values [1, 3, 5, 7, 9, 8, 6].\n"
    f"Processing: traverse the tree with DFS using a stack and BFS using a queue.\n"
    f"Output: traversal order and a color-coded visualization for each method."
)

from collections import deque

import matplotlib.pyplot as plt
import networkx as nx

from task_4 import add_edges, heap_to_tree


def traversal_colors(order):
    """Create a color gradient from dark to light."""
    # Calculate the number of traversal steps.
    count = len(order)
    # Return an empty dictionary for an empty tree.
    if count == 0:
        return {}
    # Create a unique color for every step.
    return {
        node_id: f"#{int(18 + 180 * index / max(1, count - 1)):02X}"
        f"{int(60 + 150 * index / max(1, count - 1)):02X}F0"
        for index, node_id in enumerate(order)
    }


def dfs(root):
    """Perform depth-first traversal using a stack."""
    # Return an empty order for an empty tree.
    if root is None:
        return []
    # Create a stack containing the root node.
    stack = [root]
    # Create a list for the visitation order.
    order = []
    # Continue until the stack is empty.
    while stack:
        # Remove the last added node.
        node = stack.pop()
        # Add the node to the traversal order.
        order.append(node.id)
        # Add the right child first so the left child is processed earlier.
        if node.right is not None:
            stack.append(node.right)
        # Add the left child to the stack.
        if node.left is not None:
            stack.append(node.left)
    # Return the traversal order.
    return order


def bfs(root):
    """Perform breadth-first traversal using a queue."""
    # Return an empty order for an empty tree.
    if root is None:
        return []
    # Create a queue containing the root node.
    queue = deque([root])
    # Create a list for the visitation order.
    order = []
    # Continue until the queue is empty.
    while queue:
        # Remove the first node from the queue.
        node = queue.popleft()
        # Add the node to the traversal order.
        order.append(node.id)
        # Add children to the queue from left to right.
        if node.left is not None:
            queue.append(node.left)
        # Add the right child to the queue.
        if node.right is not None:
            queue.append(node.right)
    # Return the traversal order.
    return order


def draw_traversal(values, method="bfs", show=True):
    """Draw a tree colored according to traversal order."""
    # Create a tree from the heap array.
    root = heap_to_tree(values)
    # Create the graph and node coordinates.
    graph = nx.DiGraph()
    positions = {}
    # Return an empty figure for empty data.
    if root is None:
        return plt.figure(figsize=(8, 5)), []
    # Build the graph structure.
    positions[root.id] = (0, 0)
    add_edges(graph, root, positions)
    # Select a non-recursive traversal algorithm.
    order = bfs(root) if method.lower() == "bfs" else dfs(root)
    # Create colors in visitation order.
    colors_by_node = traversal_colors(order)
    # Create node labels.
    labels = nx.get_node_attributes(graph, "label")
    # Create colors for all graph nodes.
    colors = [colors_by_node[node_id] for node_id in graph.nodes]
    # Create the drawing canvas.
    figure = plt.figure(figsize=(10, 6))
    # Draw the colored tree.
    nx.draw(graph, positions, labels=labels, node_color=colors, node_size=2200, arrows=False)
    # Add a title with the algorithm name.
    plt.title(f"Tree traversal using {method.upper()} method")
    # Show the graph when requested.
    if show:
        plt.show()
    # Return the figure and order for verification.
    return figure, order


if __name__ == "__main__":
    # Print the task instructions.
    print(TASK_INSTRUCTIONS)
    # Create a demonstration heap as a binary tree.
    values = [1, 3, 5, 7, 9, 8, 6]
    # Show depth-first traversal using a stack.
    draw_traversal(values, method="dfs")
    # Show breadth-first traversal using a queue.
    draw_traversal(values, method="bfs")

