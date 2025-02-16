# Title: Implementing Stack using Array

# Concept of Stack:
# - Stack follows LIFO (Last In First Out) principle.
# - It has two main operations:
#   1. push(x): Adds element 'x' to the top of the stack.
#   2. pop(): Removes and returns the top element of the stack. If stack is empty, return -1.

class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.stack = []  # Using a Python list as a stack

    def push(self, x):
        """Push an element 'x' onto the stack"""
        self.stack.append(x)  # Append at the end (O(1) time complexity)

    def pop(self):
        """Pop the top element from the stack. If empty, return -1"""
        if self.stack:
            return self.stack.pop()  # Removes last element (O(1) time complexity)
        else:
            return -1  # Stack is empty

# Example usage:
if __name__ == "__main__":
    s = Stack()  # Creating stack instance
    queries = [1, 2, 1, 3, 2, 1, 4, 2]  # Input queries
    result = []

    i = 0
    while i < len(queries):
        if queries[i] == 1:  # Push operation
            s.push(queries[i + 1])
            i += 2  # Move to the next query after push(x)
        elif queries[i] == 2:  # Pop operation
            result.append(s.pop())  # Store the popped result
            i += 1  # Move to the next query

    print(", ".join(map(str, result)))  # Print output as required

""" 
Time & Space Complexity Analysis:
Push operation (push(x)) → O(1) (Appending to the list takes constant time)
Pop operation (pop()) → O(1) (Removing the last element takes constant time)
Space Complexity → O(N) (Only storing elements in the stack, but since constraints are small, it's efficient)

"""

## It is Also present Outside this Folder , You can Also Refer that 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## OR ###
class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [0] * self.size


    def push(self, x: int) -> None:
        self.top += 1
        self.arr[self.top] = x


    def pop(self) -> int:
        x = self.arr[self.top]
        self.top -= 1
        return x


    def Top(self) -> int:
        return self.arr[self.top]


    def Size(self) -> int:
        return self.top + 1




if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.Top())
    print("Size of stack before deleting any element", s.Size())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.Size())
    print("Top of stack after deleting an element", s.Top())

"""
Time Complexity: O(N)

Space Complexity: O(N)

 
"""