"""Task 1: operations with a singly linked list."""

TASK_INSTRUCTIONS = (
    f"Input: hardcoded lists [7, 3, 9, 1, 5] and [2, 4, 8].\n"
    f"Processing: sort, reverse, and merge singly linked lists.\n"
    f"Output: the resulting lists are printed below."
)


class Node:
    """A node of a singly linked list."""

    def __init__(self, value):
        # Store the node value.
        self.value = value
        # Initially, the next node is absent.
        self.next = None


class LinkedList:
    """A singly linked list with basic algorithms."""

    def __init__(self):
        # Store a reference to the first node.
        self.head = None

    def append(self, value):
        # Create a new node with the given value.
        new_node = Node(value)
        # If the list is empty, make the new node the head.
        if self.head is None:
            self.head = new_node
            return
        # Start at the first node.
        current = self.head
        # Move to the last node.
        while current.next is not None:
            current = current.next
        # Append the new node at the end.
        current.next = new_node

    def to_list(self):
        # Create a regular list for convenient output.
        values = []
        # Start traversing from the head.
        current = self.head
        # Add every value during traversal.
        while current is not None:
            values.append(current.value)
            current = current.next
        # Return the values as a Python list.
        return values

    def reverse(self):
        # Store the previous node for changing links.
        previous = None
        # Start traversing from the head.
        current = self.head
        # Reverse every link in the list.
        while current is not None:
            # Save the next node before changing the link.
            next_node = current.next
            # Point the current node to the previous node.
            current.next = previous
            # Move the previous node forward.
            previous = current
            # Move to the next node.
            current = next_node
        # Make the former last node the new head.
        self.head = previous
        # Return the current list for method chaining.
        return self

    def sort(self):
        # Create an empty sorted list.
        sorted_list = LinkedList()
        # Insert nodes into the correct position one by one.
        current = self.head
        # Process every node of the original list.
        while current is not None:
            # Save the next node before changing links.
            next_node = current.next
            # Insert the node at the beginning if it is the smallest.
            if sorted_list.head is None or current.value <= sorted_list.head.value:
                current.next = sorted_list.head
                sorted_list.head = current
            else:
                # Start searching for the insertion position.
                position = sorted_list.head
                # Find the last node before the insertion position.
                while (
                    position.next is not None
                    and position.next.value < current.value
                ):
                    position = position.next
                # Insert the current node after the found position.
                current.next = position.next
                position.next = current
            # Move to the next node of the original list.
            current = next_node
        # Replace the current head with the sorted head.
        self.head = sorted_list.head
        # Return the current list.
        return self


def merge_sorted_lists(first, second):
    """Merge two sorted lists by changing links between nodes."""
    # Create a dummy node before the result.
    dummy = Node(0)
    # Store the current position in the result list.
    tail = dummy
    # Compare both list heads until one list is exhausted.
    while first.head is not None and second.head is not None:
        # Add the smaller node to the result.
        if first.head.value <= second.head.value:
            tail.next = first.head
            first.head = first.head.next
        else:
            tail.next = second.head
            second.head = second.head.next
        # Move the result tail forward.
        tail = tail.next
    # Append the remaining part of either list.
    tail.next = first.head if first.head is not None else second.head
    # Create a list starting after the dummy node.
    result = LinkedList()
    result.head = dummy.next
    # Return the merged list.
    return result


if __name__ == "__main__":
    # Print the task instructions.
    print(TASK_INSTRUCTIONS)
    # Create the first unsorted list.
    first_list = LinkedList()
    # Add demonstration values.
    for value in [7, 3, 9, 1, 5]:
        first_list.append(value)
    # Print the original list using an f-string.
    print(f"Original list: {first_list.to_list()}")
    # Sort the list using insertion sort.
    first_list.sort()
    # Print the sorted list.
    print(f"Sorted list: {first_list.to_list()}")
    # Reverse the links between nodes.
    first_list.reverse()
    # Print the reversed list.
    print(f"Reversed list: {first_list.to_list()}")
    # Create the second sorted list.
    second_list = LinkedList()
    # Fill the second list.
    for value in [2, 4, 8]:
        second_list.append(value)
    # Restore the first list to sorted order.
    first_list.reverse()
    # Merge the two sorted lists.
    merged = merge_sorted_lists(first_list, second_list)
    # Print the merge result.
    print(f"Merged list: {merged.to_list()}")

