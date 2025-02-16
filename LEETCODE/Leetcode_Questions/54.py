""" 
# Same Tree :-
Approach 1: Recursion (DFS)
We define a helper function isMirror(left, right), which checks:

If both nodes are None → ✅ True.
If one node is None and the other isn’t → ❌ False.
If values of both nodes are different → ❌ False.
Recursively check:
left.left with right.right
left.right with right.left

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)

    return isMirror(root.left, root.right) if root else True

# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
# Example 1: root = [1,2,2,3,4,4,3] (Expected: True)
root1 = TreeNode(1, 
                 TreeNode(2, TreeNode(3), TreeNode(4)), 
                 TreeNode(2, TreeNode(4), TreeNode(3)))

# Example 2: root = [1,2,2,null,3,null,3] (Expected: False)
root2 = TreeNode(1, 
                 TreeNode(2, None, TreeNode(3)), 
                 TreeNode(2, None, TreeNode(3)))

# Testing the function
print(isSymmetric(root1))  # Output: True
print(isSymmetric(root2))  # Output: False

""" 
Complexity Analysis
Time Complexity: 
𝑂
(
𝑁
)
O(N) → Every node is visited once.
Space Complexity: 
𝑂
(
𝑁
)
O(N) → Worst case, all nodes in the queue at once.
Key Takeaways
✅ Recursive (DFS) approach is simple and intuitive.
✅ Iterative (BFS) approach avoids recursion depth issues.
✅ Edge Cases Covered:

Empty tree → True
Single node → True
Tree with asymmetry → False
Perfectly symmetric tree → True
"""