""" 
Solution for "Binary Tree Zigzag Level Order Traversal" (Leetcode 103)
We need to traverse a binary tree level by level, but:

Odd levels (1st, 3rd, etc.) should be traversed left to right.
Even levels (2nd, 4th, etc.) should be traversed right to left.
Approach: BFS (Queue)
We will use Breadth-First Search (BFS) with a queue:

Use a queue (deque) to store nodes at each level.
Use a flag (left_to_right) to determine traversal order.
At each level:
Read all nodes in the queue.
If left_to_right == True, append values normally.
If left_to_right == False, insert values at the beginning (reverses the order).
Flip left_to_right for the next level.

"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_nodes = deque()

        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level_nodes.append(node.val)  # Normal order
            else:
                level_nodes.appendleft(node.val)  # Reverse order

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level_nodes))
        left_to_right = not left_to_right  # Flip direction

    return result

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Example 1: root = [3,9,20,null,null,15,7] (Expected: [[3],[20,9],[15,7]])
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

# Example 2: root = [1] (Expected: [[1]])
root2 = TreeNode(1)

# Example 3: root = [] (Expected: [])
root3 = None

# Testing the function
print(zigzagLevelOrder(root1))  # Output: [[3], [20,9], [15,7]]
print(zigzagLevelOrder(root2))  # Output: [[1]]
print(zigzagLevelOrder(root3))  # Output: []

""" 
Complexity Analysis
Time Complexity: 

O(N), where 

N is the number of nodes. Every node is processed once.
Space Complexity: 

O(N), worst case for storing all nodes in the queue at one time.
Key Takeaways
✅ BFS is ideal for level-order traversal.
✅ Deque helps with efficient insertion for zigzag traversal.
✅ Edge Cases Covered:

Empty tree → []
Single node → [[1]]
Tree with multiple levels → Alternating order traversal
"""