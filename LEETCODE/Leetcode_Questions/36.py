# Title: Implementing Queue using Array

# Concept of Queue:
# - A Queue follows FIFO (First In First Out) principle.
# - It has two main operations:
#   1. push(x): Adds element 'x' at the end of the queue.
#   2. pop(): Removes and returns the front element of the queue. If queue is empty, return -1.

class Queue:
    def __init__(self):
        """Initialize an empty queue"""
        self.queue = []  # Using a list as a queue

    def push(self, x):
        """Push an element 'x' to the queue"""
        self.queue.append(x)  # Enqueue at the end (O(1) time complexity)

    def pop(self):
        """Pop the front element from the queue. If empty, return -1"""
        if self.queue:
            return self.queue.pop(0)  # Dequeue from the front (O(N) time complexity)
        else:
            return -1  # Queue is empty

# Example usage:
if __name__ == "__main__":
    q = Queue()  # Creating queue instance
    queries = [1, 2, 1, 3, 2, 1, 4, 2]  # Input queries
    result = []

    i = 0
    while i < len(queries):
        if queries[i] == 1:  # Push operation
            q.push(queries[i + 1])
            i += 2  # Move to the next query after push(x)
        elif queries[i] == 2:  # Pop operation
            result.append(q.pop())  # Store the popped result
            i += 1  # Move to the next query

    print(" ".join(map(str, result)))  # Print output as required
    """ 
    Python implementation of a Queue using an Array (list in Python) with push() and pop() functions, ensuring O(1) time complexity for push and pop operations.
    """

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## OR ###
""" 
Optimized Approach using collections.deque (Recommended)
Since popping from the front of a list takes O(N) time, a better approach is to use collections.deque, which allows O(1) time complexity for both push and pop operations.
"""

from collections import deque

class Queue:
    def __init__(self):
        """Initialize an empty queue"""
        self.queue = deque()  # Using deque for efficient O(1) pop from front

    def push(self, x):
        """Push an element 'x' to the queue"""
        self.queue.append(x)  # Enqueue at the end (O(1))

    def pop(self):
        """Pop the front element from the queue. If empty, return -1"""
        if self.queue:
            return self.queue.popleft()  # Dequeue from front (O(1))
        else:
            return -1  # Queue is empty
"""
Time & Space Complexity Analysis
Using List (O(N) pop)
Push operation (push(x)) → O(1)
Pop operation (pop()) → O(N) (due to shifting all elements after removing front element)
Space Complexity → O(N)
Using collections.deque (O(1) pop) ✅ (Best)
Push operation (push(x)) → O(1)
Pop operation (pop()) → O(1) (efficient due to deque)
Space Complexity → O(N)
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------
 # OR ## 
class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 16
        self.arr = [0] * self.maxSize


    def push(self, newElement: int) -> None:
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize
        self.arr[self.end] = newElement
        print("The element pushed is", newElement)
        self.currSize += 1


    def pop(self) -> int:
        if self.start == -1:
            print("Queue Empty\nExiting...")
        popped = self.arr[self.start]
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        self.currSize -= 1
        return popped


    def top(self) -> int:
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]


    def size(self) -> int:
        return self.currSize




if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())

""" 
Time Complexity:

pop function: O(1)

push function: O(1)

top function: O(1)

size function: O(1)

Space Complexity:

Whole Queue: O(n)


"""