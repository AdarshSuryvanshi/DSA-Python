# ---------------------------------------------------
# Concept: Binary Tree Postorder Traversal (Left -> Right -> Root)
# ---------------------------------------------------
# Points to Remember:
# 1. **Postorder Traversal** follows the order:
#    - Traverse the **left** subtree.
#    - Traverse the **right** subtree.
#    - Visit the **root** node.
# 2. We can implement this traversal using:
#    - **Recursive Approach** (Simpler)
#    - **Iterative Approach** (Using two stacks or one stack with reverse order)
# 3. **Time Complexity: O(N)**, where N is the number of nodes.
# 4. **Space Complexity:**
#    - Recursive: O(N) (function call stack in worst case)
#    - Iterative: O(N) (explicit stack storage)
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
def postorder_recursive(root):
    result = []  # List to store traversal result

    def dfs(node):
        if not node:  # Base condition (empty node)
            return
        dfs(node.left)  # Traverse left subtree
        dfs(node.right)  # Traverse right subtree
        result.append(node.val)  # Visit root

    dfs(root)
    return result

# ---------------------------------------------------
# Approach 2: Iterative Solution (Using Two Stacks)
# ---------------------------------------------------
def postorder_iterative(root):
    if not root:
        return []
    
    stack1, stack2 = [root], []  # Two stacks
    result = []  # List to store traversal result

    while stack1:
        node = stack1.pop()  # Pop from stack1
        stack2.append(node)  # Push to stack2
        if node.left:  # Push left child
            stack1.append(node.left)
        if node.right:  # Push right child
            stack1.append(node.right)

    while stack2:  # Process stack2 in reverse order
        result.append(stack2.pop().val)

    return result

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Constructing the example tree: [1, None, 2, 3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Testing both approaches
print(postorder_recursive(root))  # Output: [3, 2, 1]
print(postorder_iterative(root))  # Output: [3, 2, 1]


""" 
Explanation:
Recursive Approach:

Uses a helper function dfs() to traverse the tree in Left → Right → Root order.
Base case: If node is None, return.
Time Complexity: 

O(N)
Space Complexity: 

O(N) (due to recursive call stack).
Iterative Approach (Using Two Stacks):

Stack1 is used to traverse the tree, pushing nodes in Root → Right → Left order.
Stack2 is used to reverse the order so that we process Left → Right → Root.
Time Complexity: 

O(N)
Space Complexity: 

O(N)

"""