## Find Minimum In BST
def findMin(root):
    while root and root.left:
        root = root.left  # Keep moving left
    return root.val if root else None  # Return value if root exists

#------------------------------------------------------------------------------------------------------------------
#Finding the Maximum in a BST

def findMax(root):
    while root and root.right:
        root = root.right  # Keep moving right
    return root.val if root else None  # Return value if root exists

""" 
Explanation in Simple Terms:
For Minimum → Keep moving left until there's no left child.
For Maximum → Keep moving right until there's no right child.
Return the last visited node's value (if tree is not empty).
This solution runs in O(h) time (where h is tree height), which is O(log n) for balanced BSTs and O(n) in the worst case (skewed tree). 🚀
"""
