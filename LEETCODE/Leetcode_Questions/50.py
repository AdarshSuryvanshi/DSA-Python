"""
## CHECK WHETHER THE GIVEN TREE IS "BALANCED OR NOT ""  
Optimized Approach (DFS)
We use Depth First Search (DFS) to check:

Compute height of left and right subtrees.
If the difference in heights is greater than 1, return -1 (indicating imbalance).
Otherwise, return the height of the current subtree.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Optimized DFS Approach
def isBalanced(root):
    def checkHeight(node):
        if not node:  # Base case: empty tree is balanced
            return 0
        
        left_height = checkHeight(node.left)
        if left_height == -1:  # Left subtree is unbalanced
            return -1
        
        right_height = checkHeight(node.right)
        if right_height == -1:  # Right subtree is unbalanced
            return -1
        
        if abs(left_height - right_height) > 1:  # Check balance condition
            return -1
        
        return max(left_height, right_height) + 1  # Return subtree height
    
    return checkHeight(root) != -1  # If height check returns -1, it's unbalanced

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Constructing Example 1: [3,9,20,null,null,15,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

# Constructing Example 2: [1,2,2,3,3,null,null,4,4]
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)

# Testing the function
print(isBalanced(root1))  # Output: True
print(isBalanced(root2))  # Output: False

""" 
Complexity Analysis
Time Complexity: 

O(N), since each node is visited only once.
Space Complexity: 

O(H), where H is the height of the tree (recursive stack depth).
Worst case: 

O(N) (skewed tree).
Best case: 

O(logN) (balanced tree).

"""