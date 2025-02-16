""" 
## DIAMETER OF THE TREE 
Understanding the Problem
The diameter of a binary tree is the longest path between any two nodes, measured in number of edges.

Example 1

        1
       / \
      2   3
     / \
    4   5
The longest path is [4 → 2 → 1 → 3] or [5 → 2 → 1 → 3].
Diameter = 3 (number of edges).
Output: 3

Example 2
    1
   /
  2
The longest path is [2 → 1].
Diameter = 1.
Output: 1

Optimized Approach (DFS)
We use Depth-First Search (DFS) to:

Compute the height of each subtree.
Track the longest diameter seen so far.
Update the diameter when left height + right height is greater.


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Optimized DFS Approach
def diameterOfBinaryTree(root):
    diameter = [0]  # Using a list to store max diameter globally

    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)   # Compute left subtree height
        right_height = height(node.right) # Compute right subtree height
        
        # Update the diameter (max path length found so far)
        diameter[0] = max(diameter[0], left_height + right_height)

        return max(left_height, right_height) + 1  # Return height to parent
    
    height(root)
    return diameter[0]  # Return final diameter

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Constructing Example 1: [1,2,3,4,5]
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

# Constructing Example 2: [1,2]
root2 = TreeNode(1)
root2.left = TreeNode(2)

# Testing the function
print(diameterOfBinaryTree(root1))  # Output: 3
print(diameterOfBinaryTree(root2))  # Output: 1

""" 
Complexity Analysis
Time Complexity: 

O(N), since we visit each node only once.
Space Complexity: 

O(H), where H is the height of the tree (recursive stack depth).
Worst case: 

O(N) for a skewed tree.
Best case: 

O(logN) for a balanced tree.
Key Takeaways
✔ Efficient DFS Approach: Uses recursion to compute heights and update diameter in one pass.
✔ Global Variable Usage: We store the maximum diameter found during traversal.
✔ Handles Edge Cases: Works for single-node and empty trees
"""
#-----------------------------------------