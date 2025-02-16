
### Implement Stacks Using Queues 
# 1) Striver Approach
from queue import Queue
class Stack:
    def __init__(self):
        self.q = Queue()


    def push(self, x):
        s = self.q.qsize()
        self.q.put(x)
        for i in range(s):
            self.q.put(self.q.get())


    def pop(self):
        n = self.q.get()
        return n


    def top(self):
        return self.q.queue[0]


    def size(self):
        return self.q.qsize()




if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(4)
    s.push(1)
    print("Top of the stack: ", s.top())
    print("Size of the stack before removing element: ", s.size())
    print("The deleted element is: ", s.pop())
    print("Top of the stack after removing element: ", s.top())
    print("Size of the stack after removing element: ", s.size())

    """ Time Complexity: O(N)
Space Complexity: O(N)
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import deque

class MyStack:
    def __init__(self):
        """Initialize a single queue"""
        self.q = deque()

    def push(self, x: int) -> None:
        """Push element onto stack in O(N) by rotating queue"""
        self.q.append(x)  # Insert element
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())  # Rotate queue to keep LIFO order

    def pop(self) -> int:
        """Remove the top element and return it (O(1))"""
        return self.q.popleft() if self.q else -1

    def top(self) -> int:
        """Return the top element without removing it (O(1))"""
        return self.q[0] if self.q else -1

    def empty(self) -> bool:
        """Return True if stack is empty, else False (O(1))"""
        return not self.q

""" 
Single Queue Approach
Push :- O(n)
Pop:- O(1)
top:- O(1)
"""