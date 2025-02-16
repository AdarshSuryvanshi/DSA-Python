# ---------------------------------------------------
# Concept: Binary Tree Preorder Traversal (Root -> Left -> Right)
# ---------------------------------------------------
# Points to Remember:
# 1. **Preorder Traversal** means visiting nodes in this order:
#    - Visit the **root** node first.
#    - Traverse the **left** subtree.
#    - Traverse the **right** subtree.
# 2. We can implement this traversal using:
#    - **Recursive Approach** (Simpler)
#    - **Iterative Approach** (Using a stack)
# 3. **Time Complexity: O(N)**, where N is the number of nodes.
# 4. **Space Complexity:**
#    - Recursive: O(N) (because of function call stack in worst case)
#    - Iterative: O(N) (because of explicit stack)
# ---------------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# ---------------------------------------------------
# Approach 1: Recursive Solution (Simple)
# ---------------------------------------------------
def preorder_recursive(root):
    result = []  # List to store traversal result

    def dfs(node):
        if not node:  # Base condition (empty node)
            return
        result.append(node.val)  # Visit root
        dfs(node.left)  # Traverse left subtree
        dfs(node.right)  # Traverse right subtree

    dfs(root)
    return result

# ---------------------------------------------------
# Approach 2: Iterative Solution (Using Stack)
# ---------------------------------------------------
def preorder_iterative(root):
    if not root:
        return []
    
    stack = [root]  # Stack to simulate recursion
    result = []  # List to store traversal result

    while stack:
        node = stack.pop()  # Get top element
        result.append(node.val)  # Visit root

        # Push right child first, so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Constructing the example tree: [1, None, 2, 3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Testing both approaches
print(preorder_recursive(root))  # Output: [1, 2, 3]
print(preorder_iterative(root))  # Output: [1, 2, 3]


""" 
Explanation:
Recursive Approach:

Uses a helper function dfs() to traverse the tree in Root → Left → Right order.
Base case: If node is None, return.
Time Complexity: 

O(N)
Space Complexity: 

O(N) (due to recursive call stack).
Iterative Approach:

Uses a stack to manually process nodes in Root → Left → Right order.
Push right child first to ensure the left child is processed first.
Time Complexity: 

O(N)
Space Complexity: 

O(N) (due to explicit stack storage
"""