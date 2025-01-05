class Queue:
    def __init__(self, capacity=None):
        """
        Initialize a queue.
        :param capacity: Maximum number of elements the queue can hold (optional).
        """
        self.queue = []  # Use a list to store elements.
        self.capacity = capacity  # Maximum capacity of the queue (None for unlimited).

    def enqueue(self, item):
        """
        Add an element to the rear of the queue.
        :param item: The element to be added.
        """
        if self.capacity is not None and len(self.queue) >= self.capacity:
            print("Queue is full. Cannot enqueue.")
            return
        self.queue.append(item)  # Add the element to the end of the list.
        print(f"Enqueued {item} to the queue.")

    def dequeue(self):
        """
        Remove and return the front element of the queue.
        :return: The element removed from the front.
        """
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.pop(0)  # Remove the first element of the list.
        print(f"Dequeued {item} from the queue.")
        return item

    def peek(self):
        """
        Retrieve the front element without removing it.
        :return: The front element of the queue.
        """
        if self.is_empty():
            print("Queue is empty. No front element.")
            return None
        print(f"Front element is {self.queue[0]}.")
        return self.queue[0]

    def is_empty(self):
        """
        Check if the queue is empty.
        :return: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def is_full(self):
        """
        Check if the queue is full.
        :return: True if the queue is full, False otherwise.
        """
        if self.capacity is None:
            return False  # Unlimited capacity queues are never full.
        return len(self.queue) == self.capacity

    def size(self):
        """
        Get the number of elements in the queue.
        :return: The size of the queue.
        """
        print(f"Queue size is {len(self.queue)}.")
        return len(self.queue)

    def display(self):
        """
        Display all elements in the queue.
        """
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", " -> ".join(map(str, self.queue)))

    def reverse(self):
        """
        Reverse the elements in the queue.
        """
        if self.is_empty():
            print("Queue is empty. Cannot reverse.")
            return
        self.queue.reverse()  # Reverse the list in-place.
        print("Queue has been reversed.")

    def search(self, target):
        """
        Search for an element in the queue.
        :param target: The element to search for.
        :return: True if the element is found, otherwise False.
        """
        if self.is_empty():
            print("Queue is empty. Cannot search.")
            return False
        found = target in self.queue  # Check if the target is in the list.
        if found:
            print(f"Element {target} found in the queue.")
        else:
            print(f"Element {target} not found in the queue.")
        return found


# Example usage of the Queue class
if __name__ == "__main__":
    # Create a queue with unlimited capacity
    my_queue = Queue()

    # Enqueue elements
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    my_queue.enqueue(40)

    # Display the queue
    my_queue.display()

    # Peek at the front element
    my_queue.peek()

    # Dequeue an element
    my_queue.dequeue()
    my_queue.display()

    # Check the size of the queue
    my_queue.size()

    # Check if the queue is empty
    print("Is queue empty?", my_queue.is_empty())

    # Reverse the queue
    my_queue.reverse()
    my_queue.display()

    # Search for elements in the queue
    my_queue.search(20)
    my_queue.search(50)
"""
Explanation of the Code:
Basic Operations:

enqueue: Adds elements to the rear of the queue.
dequeue: Removes elements from the front of the queue.
peek: Retrieves the front element without removing it.
is_empty: Checks if the queue is empty.
is_full: Checks if the queue is full (for fixed-size queues).
Additional Operations:

reverse: Reverses the order of elements in the queue using the .reverse() method of lists.
search: Searches for an element in the queue using the in operator.
Error Handling:

The code handles scenarios like trying to dequeue from an empty queue or enqueue into a full queue.


"""