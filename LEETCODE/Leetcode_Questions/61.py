""" 
Approach to Insert into a BST
To insert a new value into a Binary Search Tree (BST):

Start at the root.
Compare the value:
If the value is less than the current node’s value, move left.
If the value is greater, move right.
If an empty (None) spot is found, insert the new node there.
Ensure the tree remains a valid BST.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    if not root:  
        return TreeNode(val)  # If tree is empty, create new node

    if val < root.val:
        root.left = insertIntoBST(root.left, val)  # Insert into left subtree
    else:
        root.right = insertIntoBST(root.right, val)  # Insert into right subtree

    return root  # Return modified root

""" 
Time & Space Complexity
Time Complexity: 

O(h), where 

h is the height of the BST (

O(logn) for balanced BST, 

O(n) in worst case).
Space Complexity: 

O(h) due to recursion (or 

O(1) if using an iterative approach).

"""