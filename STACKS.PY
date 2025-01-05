# Let's define a Stack class to implement stack operations
class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        An empty list will be used to store the stack elements.
        """
        self.stack = []  # This list will hold the stack elements.

    def push(self, element):
        """
        Add an element to the top of the stack.
        :param element: The value to be added to the stack.
        """
        self.stack.append(element)  # Append the element to the list.
        print(f"Pushed {element} to the stack.")  # Inform the user.

    def pop(self):
        """
        Remove and return the top element of the stack.
        :return: The top element if the stack is not empty, otherwise None.
        """
        if not self.is_empty():  # Check if the stack is not empty.
            removed_element = self.stack.pop()  # Remove the last element.
            print(f"Popped {removed_element} from the stack.")  # Inform the user.
            return removed_element
        else:
            print("Stack is empty. Nothing to pop.")  # Inform the user if the stack is empty.
            return None

    def peek(self):
        """
        Return the top element of the stack without removing it.
        :return: The top element if the stack is not empty, otherwise None.
        """
        if not self.is_empty():  # Check if the stack is not empty.
            top_element = self.stack[-1]  # Get the last element.
            print(f"Top element is {top_element}.")  # Inform the user.
            return top_element
        else:
            print("Stack is empty. No top element.")  # Inform the user if the stack is empty.
            return None

    def is_empty(self):
        """
        Check if the stack is empty.
        :return: True if the stack is empty, otherwise False.
        """
        return len(self.stack) == 0  # Return True if the list is empty.

    def size(self):
        """
        Return the number of elements in the stack.
        :return: The size of the stack.
        """
        return len(self.stack)  # Return the length of the list.

    def display(self):
        """
        Display the entire stack.
        """
        print("Stack elements (from bottom to top):", self.stack)

    def reverse(self):
        """
        Reverse the stack.
        This changes the order of the elements such that the bottom becomes the top.
        """
        if not self.is_empty():  # Check if the stack is not empty.
            self.stack.reverse()  # Reverse the list in place.
            print("Stack reversed.")  # Inform the user.
        else:
            print("Stack is empty. Cannot reverse.")  # Inform the user if the stack is empty.

    def search(self, element):
        """
        Search for an element in the stack and return its position from the top.
        :param element: The value to search for in the stack.
        :return: Position from the top (1-based index) if found, otherwise -1.
        """
        if element in self.stack:  # Check if the element exists in the stack.
            # Calculate the position from the top.
            position_from_top = len(self.stack) - self.stack.index(element)
            print(f"Element {element} found at position {position_from_top} from the top.")
            return position_from_top
        else:
            print(f"Element {element} not found in the stack.")  # Inform the user if the element is not found.
            return -1

# Example usage of the Stack
if __name__ == "__main__":
    # Create a new stack instance.
    my_stack = Stack()

    # Push elements onto the stack.
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)

    # Display the stack.
    my_stack.display()

    # Reverse the stack.
    my_stack.reverse()
    my_stack.display()

    # Search for an element in the stack.
    my_stack.search(20)  # Element exists.
    my_stack.search(50)  # Element does not exist.

    # Peek at the top element.
    my_stack.peek()

    # Get the size of the stack.
    print(f"Size of stack: {my_stack.size()}")

    # Pop elements from the stack.
    my_stack.pop()
    my_stack.display()

    # Check if the stack is empty.
    print(f"Is stack empty? {my_stack.is_empty()}")
