# -----------------------------------------------
# Concept: Maximum Nodes at Level i in a Binary Tree
# -----------------------------------------------
# Points to Remember:
# 1. A Binary Tree follows a hierarchical structure.
# 2. At each level, the number of nodes follows a pattern:
#    - Level 0 → 2^0 = 1 node
#    - Level 1 → 2^1 = 2 nodes
#    - Level 2 → 2^2 = 4 nodes
#    - Level 3 → 2^3 = 8 nodes
#    - General Formula: At level 'i', max nodes = 2^i
# 3. The time complexity is O(1) because we are using a direct formula.
# 4. The space complexity is O(1) as no extra space is used.
# -----------------------------------------------

def countNode(i):
    # Using the formula 2^i to get the max nodes at level 'i'
    print(2 ** i)  # ** operator is used for exponentiation in Python

# Example cases
countNode(5)  # Output: 16
countNode(1)  # Output: 2
