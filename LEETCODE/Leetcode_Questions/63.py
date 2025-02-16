""" 
Approach to Validate a BST
A Binary Search Tree (BST) must satisfy the following conditions:

Left subtree contains only nodes with values less than the current node.
Right subtree contains only nodes with values greater than the current node.
Both the left and right subtrees must also be valid BSTs.
Optimal Approach: Using Min-Max Range (Recursive)
We recursively check whether the node's value lies within the valid range (min, max):

Initially, the range is (-∞, ∞).
If we move left, update the range as (min, node.val).
If we move right, update the range as (node.val, max).
If a node violates the BST property, return False.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True  # An empty tree is a valid BST

    if not (min_val < root.val < max_val):
        return False  # Node violates BST property

    # Recursively check left and right subtrees with updated ranges
    return isValidBST(root.left, min_val, root.val) and isValidBST(root.right, root.val, max_val)

""" 
Time & Space Complexity
Time Complexity: 

O(n), where 

n is the number of nodes (each node is visited once).
Space Complexity: 

h is the height of the BST (recursion stack space, 

O(logn) for balanced BST, 

O(n) for skewed tree).
Example Walkthrough
Example 1
Input:

python
Copy
Edit
root = [2,1,3]
Tree Structure:

Copy
Edit
   2
  / \
 1   3
1 < 2 (Valid Left Subtree)
3 > 2 (Valid Right Subtree)
Output: True
Example 2
Input:

python
Copy
Edit
root = [5,1,4,null,null,3,6]
Tree Structure:

markdown
Copy
Edit
      5
     / \
    1   4
       / \
      3   6
4 should be in range (5, ∞), but 4 < 5 ❌ (violates BST property).
Output: False
"""