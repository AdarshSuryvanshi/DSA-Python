# ---------------------------------------------------
# Concept: Maximum Depth of a Binary Tree , ""DEPTH == HEIGHT ""... Depth=Height 
# ---------------------------------------------------
# Points to Remember:
# 1. **Definition of Depth**:
#    - The depth of a binary tree is the **number of nodes** along the **longest path** from the root to a leaf.
# 2. We can solve this problem using:
#    - **Recursive Approach** (DFS - Depth First Search)
#    - **Iterative Approach** (BFS - Level Order Traversal)
# 3. **Time Complexity: O(N)**, where N is the number of nodes.
# 4. **Space Complexity:**
#    - Recursive: O(N) (function call stack in worst case)
#    - Iterative: O(N) (queue storage for BFS)
# ---------------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# ---------------------------------------------------
# Approach 1: Recursive Solution (DFS - Depth First Search)
# ---------------------------------------------------
def maxDepth_recursive(root):
    if not root:  # Base case: empty tree
        return 0
    # Recursively find depth of left and right subtree, then add 1 for root
    return 1 + max(maxDepth_recursive(root.left), maxDepth_recursive(root.right))

# ---------------------------------------------------
# Approach 2: Iterative Solution (BFS - Level Order Traversal)
# ---------------------------------------------------
from collections import deque

def maxDepth_iterative(root):
    if not root:
        return 0
    
    queue = deque([root])  # Queue for level order traversal
    depth = 0  # Initialize depth

    while queue:
        depth += 1  # Increase depth at each level
        for _ in range(len(queue)):  # Process all nodes at the current level
            node = queue.popleft()  # Remove node from queue
            if node.left:  # Add left child to queue
                queue.append(node.left)
            if node.right:  # Add right child to queue
                queue.append(node.right)

    return depth

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Constructing the example tree: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Testing both approaches
print(maxDepth_recursive(root))  # Output: 3
print(maxDepth_iterative(root))  # Output: 3

""" 
Explanation:
Recursive Approach (DFS):

Uses postorder traversal: calculates depth of left and right subtrees, then returns the maximum depth.
Base case: If root is None, return 0.
Time Complexity: 

O(N)
Space Complexity: 

O(N) (due to recursive call stack).
Iterative Approach (BFS - Level Order Traversal):

Uses a queue to traverse the tree level by level.
Increases depth count whenever we finish a level.
Time Complexity: 

O(N)
Space Complexity: 

O(N) (queue storage for level order traversal).
"""