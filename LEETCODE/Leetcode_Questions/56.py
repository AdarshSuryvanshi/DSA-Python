""" 
Solution: Search in a Binary Search Tree (BST)
Since a Binary Search Tree (BST) follows the property:

Left subtree contains values smaller than the root.
Right subtree contains values greater than the root.
We can efficiently search for a given value val using a recursive or iterative approach.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    if not root or root.val == val:  # Base case: found or reached NULL
        return root
    if val < root.val:  # Search in the left subtree
        return searchBST(root.left, val)
    return searchBST(root.right, val)  # Search in the right subtree

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2) Iterative Approch 
def searchBST(root, val):
    while root:
        if root.val == val:
            return root
        root = root.left if val < root.val else root.right
    return None

""" 
Explanation in Simple Terms:
Loop until we find the value or reach None (end of tree).
If the value is smaller, move left.
If the value is greater, move right.
If found, return the node; otherwise, return None.

"""

""" 
# Tree structure:
#       4
#      / \
#     2   7
#    / \
#   1   3

searchBST(root, 2)  # Output: [2,1,3]

Complexity Analysis
Time Complexity: 


O(logn) (average) and 

O(n) (worst case for skewed trees).
Space Complexity:
Recursive: 
O(logn) (due to recursion stack, worst case 

O(n)).
Iterative: 

O(1) (no extra space used).

"""