""" 
 # SAME TREE 
 Approach: Recursive DFS
We will use Depth-First Search (DFS) with recursion:

If both p and q are None, return True.
If only one of them is None, return False (since one tree is missing a node).
If the values at p and q are different, return False.
Recursively check:
Left subtrees of p and q
Right subtrees of p and q
If both subtrees match, return True.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive DFS solution
def isSameTree(p, q):
    # Base cases
    if not p and not q:
        return True  # Both are None, so trees are identical
    if not p or not q:
        return False  # One is None, the other is not

    # Check values and recursively check left and right subtrees
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Example 1: p = [1,2,3], q = [1,2,3] (Expected: True)
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))

# Example 2: p = [1,2], q = [1,null,2] (Expected: False)
p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))

# Example 3: p = [1,2,1], q = [1,1,2] (Expected: False)
p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))

# Testing the function
print(isSameTree(p1, q1))  # Output: True
print(isSameTree(p2, q2))  # Output: False
print(isSameTree(p3, q3))  # Output: False

""" 
Complexity Analysis
Time Complexity: 

O(N), where 
N is the number of nodes. Each node is visited once.
Space Complexity: 
O(H)
H is the height of the tree (recursive stack depth).
Best case: 
O(logN) for a balanced tree.
Worst case: 

O(N) for a skewed tree.
"""