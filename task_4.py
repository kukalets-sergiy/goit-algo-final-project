"""Task 4: visualizing a binary heap as a tree."""

f"Libraries required: matplotlib and networkx. Install them with: pip install -r requirements.txt"

TASK_INSTRUCTIONS = (
    f"Input: hardcoded min-heap values [1, 3, 5, 7, 9, 8, 6].\n"
    f"Processing: convert the list into a binary tree using heap indexes.\n"
    f"Output: a NetworkX and matplotlib visualization of the heap."
)

import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    """A tree node used for heap visualization."""

    def __init__(self, value):
        # Store the node value.
        self.value = value
        # Create a reference to the left child.
        self.left = None
        # Create a reference to the right child.
        self.right = None
        # Create a unique node identifier.
        self.id = str(uuid.uuid4())


def heap_to_tree(values):
    """Convert a heap array into a linked binary tree."""
    # Return None for an empty heap.
    if not values:
        return None
    # Create nodes for all array elements.
    nodes = [Node(value) for value in values]
    # Attach children using binary heap indexes.
    for index, node in enumerate(nodes):
        # Calculate the left child index.
        left_index = 2 * index + 1
        # Calculate the right child index.
        right_index = 2 * index + 2
        # Attach the left child if it exists.
        if left_index < len(nodes):
            node.left = nodes[left_index]
        # Attach the right child if it exists.
        if right_index < len(nodes):
            node.right = nodes[right_index]
    # Return the root node.
    return nodes[0]


def add_edges(graph, node, positions, x=0, y=0, layer=1):
    """Add nodes, edges, and coordinates to a NetworkX graph."""
    # Stop recursion for a missing node.
    if node is None:
        return
    # Add a node labeled with its value.
    graph.add_node(node.id, label=str(node.value), color="#87CEEB")
    # Process the left child.
    if node.left is not None:
        # Add an edge to the left child.
        graph.add_edge(node.id, node.left.id)
        # Place the left child lower and to the left.
        positions[node.left.id] = (x - 1 / 2**layer, y - 1)
        # Recursively add the subtree.
        add_edges(graph, node.left, positions, positions[node.left.id][0], y - 1, layer + 1)
    # Process the right child.
    if node.right is not None:
        # Add an edge to the right child.
        graph.add_edge(node.id, node.right.id)
        # Place the right child lower and to the right.
        positions[node.right.id] = (x + 1 / 2**layer, y - 1)
        # Recursively add the subtree.
        add_edges(graph, node.right, positions, positions[node.right.id][0], y - 1, layer + 1)


def visualize_heap(values, show=True):
    """Build a tree from a heap array and return a matplotlib figure."""
    # Create the tree root from the heap array.
    root = heap_to_tree(values)
    # Create a directed graph.
    graph = nx.DiGraph()
    # Return an empty figure for an empty heap.
    if root is None:
        return plt.figure(figsize=(8, 5))
    # Set the root node coordinates.
    positions = {root.id: (0, 0)}
    # Populate the graph with nodes and edges.
    add_edges(graph, root, positions)
    # Get the node labels.
    labels = nx.get_node_attributes(graph, "label")
    # Get the node colors.
    colors = list(nx.get_node_attributes(graph, "color").values())
    # Create the visualization canvas.
    figure = plt.figure(figsize=(10, 6))
    # Draw the tree without arrows.
    nx.draw(graph, positions, labels=labels, node_color=colors, node_size=2200, arrows=False)
    # Add a title using an f-string.
    plt.title(f"Binary heap: {values}")
    # Show the graph only when requested.
    if show:
        plt.show()
    # Return the figure for tests or later saving.
    return figure


if __name__ == "__main__":
    # Print the task instructions.
    print(TASK_INSTRUCTIONS)
    # Create an example min-heap.
    heap = [1, 3, 5, 7, 9, 8, 6]
    # Visualize the heap.
    visualize_heap(heap)

