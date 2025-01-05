class Node:
    def __init__(self, data):
        """
        Initialize a new node with data and a reference to the next node.
        :param data: The value to store in the node.
        """
        self.data = data  # Store the data.
        self.next = None  # Initially, the next reference is None.

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None  # The head of the linked list starts as None (empty list).

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the linked list.
        :param data: The value to insert.
        """
        new_node = Node(data)  # Create a new node with the given data.
        new_node.next = self.head  # Point the new node to the current head.
        self.head = new_node  # Update the head to the new node.
        print(f"Inserted {data} at the beginning of the linked list.")

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the linked list.
        :param data: The value to insert.
        """
        new_node = Node(data)  # Create a new node with the given data.
        if self.head is None:  # If the list is empty, make the new node the head.
            self.head = new_node
            print(f"Inserted {data} as the first node in the linked list.")
            return
        current = self.head  # Start at the head.
        while current.next:  # Traverse to the last node.
            current = current.next
        current.next = new_node  # Point the last node to the new node.
        print(f"Inserted {data} at the end of the linked list.")

    def insert_at_position(self, position, data):
        """
        Insert a new node at a specific position in the linked list.
        :param position: The 1-based position to insert the node.
        :param data: The value to insert.
        """
        if position < 1:
            print("Invalid position. Position must be 1 or greater.")
            return
        new_node = Node(data)  # Create the new node with the given data.
        if position == 1:
            new_node.next = self.head  # Point the new node to the current head.
            self.head = new_node  # Update the head to the new node.
            print(f"Inserted {data} at position {position} in the linked list.")
            return
        current = self.head  # Start at the head.
        for _ in range(position - 2):  # Traverse to one node before the target position.
            if current is None:
                print("Position out of range.")
                return
            current = current.next
        if current is None:
            print("Position out of range.")
            return
        new_node.next = current.next  # Link the new node to the next node.
        current.next = new_node  # Update the current node's next to the new node.
        print(f"Inserted {data} at position {position} in the linked list.")

    def delete_from_beginning(self):
        """
        Delete the node at the beginning of the linked list.
        """
        if self.head is None:  # Check if the list is empty.
            print("Linked list is empty. Nothing to delete.")
            return
        deleted_data = self.head.data  # Get the data of the node being deleted.
        self.head = self.head.next  # Update the head to the next node.
        print(f"Deleted {deleted_data} from the beginning of the linked list.")

    def delete_from_end(self):
        """
        Delete the node at the end of the linked list.
        """
        if self.head is None:  # Check if the list is empty.
            print("Linked list is empty. Nothing to delete.")
            return
        if self.head.next is None:  # If there's only one node.
            deleted_data = self.head.data
            self.head = None  # Set the head to None (empty list).
            print(f"Deleted {deleted_data} from the linked list. The list is now empty.")
            return
        current = self.head  # Start at the head.
        while current.next.next:  # Traverse to the second-to-last node.
            current = current.next
        deleted_data = current.next.data  # Get the data of the last node.
        current.next = None  # Remove the reference to the last node.
        print(f"Deleted {deleted_data} from the end of the linked list.")

    def delete_by_position(self, position):
        """
        Delete the node at a specific position (1-based index).
        :param position: The 1-based position to delete the node.
        """
        if position < 1:  # Ensure the position is valid.
            print("Invalid position. Position must be 1 or greater.")
            return
        if self.head is None:  # Check if the list is empty.
            print("Linked list is empty. Nothing to delete.")
            return
        if position == 1:  # If the node to delete is the first node.
            deleted_data = self.head.data
            self.head = self.head.next  # Update the head to the next node.
            print(f"Deleted node at position {position} with value {deleted_data}.")
            return
        current = self.head  # Start at the head.
        for _ in range(position - 2):  # Traverse to one node before the target position.
            if current is None:
                print("Position out of range.")
                return
            current = current.next
        if current is None or current.next is None:  # Check if the position is out of range.
            print("Position out of range.")
            return
        deleted_data = current.next.data  # Get the data of the node to delete.
        current.next = current.next.next  # Remove the reference to the node.
        print(f"Deleted node at position {position} with value {deleted_data}.")

    def display(self):
        """
        Display all the elements in the linked list.
        """
        if self.head is None:  # Check if the list is empty.
            print("Linked list is empty.")
            return
        current = self.head  # Start at the head.
        print("Linked list elements:", end=" ")
        while current:  # Traverse the list and print each node's data.
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list.

    def reverse(self):
        """
        Reverse the linked list.
        """
        previous = None  # Initialize the previous node as None.
        current = self.head  # Start at the head.
        while current:  # Traverse the list and reverse the pointers.
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous  # Update the head to the last node (now the first).
        print("Linked list has been reversed.")

# Example usage of the LinkedList
if __name__ == "__main__":
    my_linked_list = LinkedList()  # Create a new linked list instance.

    # Insert elements at the beginning.
    my_linked_list.insert_at_beginning(10)
    my_linked_list.insert_at_end(20)
    my_linked_list.insert_at_position(2, 15)

    # Display the linked list.
    my_linked_list.display()

    # Delete elements from a specific position.
    my_linked_list.delete_by_position(2)  # Delete node at position 2.
    my_linked_list.delete_by_position(1)  # Delete node at position 1.

    # Display after deletions.
    my_linked_list.display()

    # Reverse the linked list.
    my_linked_list.reverse()
    my_linked_list.display()
