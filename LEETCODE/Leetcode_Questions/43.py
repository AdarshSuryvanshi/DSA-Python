## Array to a Linked List
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def arrayToLinkedList(arr):
    if not arr:
        return None  # Return None if array is empty

    head = ListNode(arr[0])  # Create head node
    current = head

    for num in arr[1:]:
        current.next = ListNode(num)  # Create and link new node
        current = current.next  # Move to the new node

    return head

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end="->" if current.next else "")
        current = current.next
    print()

# Example Usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 7, 5, 1, 0]

head1 = arrayToLinkedList(arr1)
head2 = arrayToLinkedList(arr2)

printLinkedList(head1)  # Output: 1->2->3->4->5
printLinkedList(head2)  # Output: 2->4->6->7->5->1->0

""" 
Key Optimizations:
✅ O(n) Time Complexity: We iterate through the array once to construct the linked list.
✅ O(n) Space Complexity: We use only extra space for the linked list nodes.
✅ Edge Case Handling: Returns None if the array is empty.

Would you like additional modifications or explanations? 🚀
"""



# QQQ)
## IS there any Diffrence Between Pyhton List and Linked List or Both are same ??
"""
Yes, Python List and Linked List are different data structures. They serve similar purposes but work in fundamentally different ways. Let's break down the key differences:

🔹 Python List (Dynamic Array)
A Python list is an array-like structure that stores elements in contiguous memory locations.

Key Features:
✅ Indexed Access: Elements can be accessed directly using an index (O(1)).
✅ Dynamic Resizing: Python lists grow dynamically when needed.
✅ Built-in Methods: Supports append(), insert(), pop(), remove(), etc.
✅ Efficient Iteration: Faster iteration since elements are stored together in memory.
❌ Insertion/Deletion Costly: Inserting/deleting at the middle takes O(n) time due to shifting.
❌ Memory Wastage: Pre-allocated memory can be wasted if the list size shrinks.

Example (Python List)

arr = [1, 2, 3, 4]
print(arr[2])  # Access element at index 2 (O(1))
arr.append(5)  # Append element (O(1))
arr.insert(2, 10)  # Insert at index 2 (O(n) due to shifting)
print(arr)  # Output: [1, 2, 10, 3, 4, 5]

_--------------------------------------------------------------------------------------------------------------
🔹 Linked List
A linked list is a non-contiguous data structure where each element (node) contains:

Data (value)
Pointer to the next node
There are two main types:

Singly Linked List → Each node points to the next node only.
Doubly Linked List → Each node has pointers to both the next and previous nodes.
Key Features:
✅ Efficient Insertions/Deletions: Insert/Delete at the beginning/middle in O(1) or O(n) (no shifting).
✅ Dynamic Size: No need for pre-allocation, grows as needed.
❌ Slower Access: No index-based access, must traverse (O(n)).
❌ More Memory Overhead: Each node requires extra memory for storing pointers.

Example (Linked List in Python)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.printList()  # Output: 1 -> 2 -> 3 -> None
🔸 Key Differences:
Feature	Python List (Array)	Linked List
Memory Allocation	Contiguous	Non-contiguous (pointers)
Access Time	O(1) (Indexed)	O(n) (Traversal)
Insertion (Middle/Beginning)	O(n) (Shifting needed)	O(1)
Deletion (Middle/Beginning)	O(n)	O(1)
Memory Overhead	Low	High (due to pointers)
Flexibility	Fixed size (resized dynamically)	Grows dynamically
🔹 When to Use What?
✅ Use Python List (Array) when fast access and iteration are required.
✅ Use Linked List when frequent insertions/deletions at random positions are needed.
🔹 Conclusion
Python lists and linked lists are NOT the same. Python lists use arrays, while linked lists store elements non-contiguously with pointers. Each has its own advantages based on the use case.

Would you like a real-world analogy to understand better? 🚀








"""