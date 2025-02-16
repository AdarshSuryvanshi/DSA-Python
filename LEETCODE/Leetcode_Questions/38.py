## Implement Queues Using Stacks
## Most Optimzed IS using 2 Stacks we can Create a Queues 
class MyQueue:
    def __init__(self):
        """Initialize two stacks."""
        self.stack1 = []  # For push operations
        self.stack2 = []  # For pop and peek operations

    def push(self, x: int) -> None:
        """Push element x to the back of queue (O(1))."""
        self.stack1.append(x)

    def pop(self) -> int:
        """Remove and return the front element (Amortized O(1))."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Reverse elements
        return self.stack2.pop() if self.stack2 else -1  # Return -1 if empty

    def peek(self) -> int:
        """Get the front element without removing it (Amortized O(1))."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else -1  # Return -1 if empty

    def empty(self) -> bool:
        """Return True if the queue is empty, False otherwise (O(1))."""
        return not self.stack1 and not self.stack2
    
     ## EXAMPLE RUN 
"""
myQueue = MyQueue()
myQueue.push(1)   # Queue: [1]
myQueue.push(2)   # Queue: [1, 2]
print(myQueue.peek())  # Output: 1
print(myQueue.pop())   # Output: 1, Queue: [2]
print(myQueue.empty()) # Output: False

"""

""" 
Time Complexity Analysis
Operation	Time Complexity
Push:- 	O(1)
Pop :- 	Amortized O(1)
Peek:-	Amortized O(1)
Empty:- 	O(1)

Why Amortized O(1) for Pop and Peek?
Worst case (O(N)): When stack2 is empty, we move N elements from stack1 to stack2.
Best case (O(1)): If stack2 already has elements, we pop in constant time.
Since each element is moved at most once, the average cost per operation remains O(1).

"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2) 
from queue import LifoQueue
# using LifoQueue which is a stack in python




class MyQueue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()


    # Push element x to the back of queue.
    def push(self, x: int) -> None:
        print("The element pushed is ", x)
        self.input.put(x)


    # Removes the element from in front of queue and returns that element.
    def pop(self) -> int:
        # shift input to output
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        x = self.output.get()
        return x


    # Get the front element.
    def top(self) -> int:
        # shift input to output
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        return self.output.queue[-1]


    def size(self) -> int:
        return self.input.qsize() + self.output.qsize()




if __name__ == "__main__":
    q = MyQueue()
    q.push(3)
    q.push(4)
    print("The element poped is ", q.pop())
    q.push(5)
    print("The top of the queue is ", q.top())
    print("The size of the queue is ", q.size())

""" 
Time Complexity: O(1 )

Space Complexity: O(2N)


"""