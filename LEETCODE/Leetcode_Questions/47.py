# ---------------------------------------------------
# Concept: Binary Tree Inorder Traversal (Left -> Root -> Right)
# ---------------------------------------------------
# Points to Remember:
# 1. **Inorder Traversal** follows the order:
#    - Traverse the **left** subtree.
#    - Visit the **root** node.
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
def inorder_recursive(root):
    result = []  # List to store traversal result

    def dfs(node):
        if not node:  # Base condition (empty node)
            return
        dfs(node.left)  # Traverse left subtree
        result.append(node.val)  # Visit root
        dfs(node.right)  # Traverse right subtree

    dfs(root)
    return result

# ---------------------------------------------------
# Approach 2: Iterative Solution (Using Stack)
# ---------------------------------------------------
def inorder_iterative(root):
    result = []  # List to store traversal result
    stack = []  # Stack to simulate recursion
    current = root  # Start from root node

    while stack or current:
        while current:  # Reach the leftmost node
            stack.append(current)
            current = current.left
        
        current = stack.pop()  # Process node
        result.append(current.val)  # Visit root
        current = current.right  # Move to right subtree

    return result

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Constructing the example tree: [1, None, 2, 3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Testing both approaches
print(inorder_recursive(root))  # Output: [1, 3, 2]
print(inorder_iterative(root))  # Output: [1, 3, 2]

""" 
Explanation:
Recursive Approach:

Uses a helper function dfs() to traverse the tree in Left → Root → Right order.
Base case: If node is None, return.
Time Complexity: 

O(N)
Space Complexity: 

O(N) (due to recursive call stack).
Iterative Approach:

Uses a stack to manually process nodes in Left → Root → Right order.
First, reach the leftmost node, then process the root, and finally move to the right subtree.
Time Complexity: 
O(N)
Space Complexity: 

O(N) (due to explicit stack storage).

"""