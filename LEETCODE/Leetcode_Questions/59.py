#Finding Ceil in a BST
""" 
Approach:
Start from the root of the BST.
If root's value is equal to X, return X (direct match).
If root's value is greater than X, store it as a potential ceil and move left (as a smaller valid ceil may exist).
If root's value is less than X, move right (since all left-side values are smaller and invalid as ceil).
If no valid ceil is found, return -1.

"""
def findCeil(root, X):
    ceil = -1
    while root:
        if root.val == X:  # If X matches a node value, return it immediately
            return X
        elif root.val > X:  # Possible ceil, but try to find a smaller one
            ceil = root.val
            root = root.left
        else:  # Move right to find a larger value
            root = root.right
    return ceil  # Return the smallest valid ceil or -1 if not found

""" 
Example Walkthrough
Example 1:
🔹 Input:

mathematica
Copy
Edit
BST: [5, 1, 7, N, 2, N, N, N, 3], X = 3
🔹 BST Structure:

markdown
Copy
Edit
      5
    /   \
   1     7
    \
     2 
      \
       3
🔹 Steps:

Start at 5 → Move left (5 > 3, so store 5 as a potential ceil).
At 1 → Move right (1 < 3).
At 2 → Move right (2 < 3).
At 3 → Exact match found ✅ Return 3.
🔹 Output: 3

Example 2:
🔹 Input:

mathematica
Copy
Edit
BST: [10, 5, 11, 4, 7, N, N, N, N, N, 8], X = 6
🔹 BST Structure:

markdown
Copy
Edit
     10
    /  \
   5    11
  / \ 
 4   7
      \
       8
🔹 Steps:

Start at 10 → Move left (10 > 6, store 10 as potential ceil).
At 5 → Move right (5 < 6).
At 7 → Move left (7 > 6, store 7 as potential ceil).
No exact match, return smallest valid ceil → 7 ✅.
🔹 Output: 7

Time Complexity:
Best case: O(1) (if X is found immediately)
Worst case: O(h) (where h is tree height, O(log n) for balanced BST, O(n) for skewed BST)

"""