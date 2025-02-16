# ---------------------------------------------------
# Concept: Binary Tree Representation from Level Order Traversal
# ---------------------------------------------------
# Points to Remember:
# 1. A Binary Tree consists of nodes where each node has at most two children.
# 2. Level-order traversal inserts nodes from left to right, level by level.
# 3. Given a list of 7 values, we construct a complete binary tree:
#    - Root → nodes[0]
#    - Left child of root → nodes[1], Right child → nodes[2]
#    - Left child of nodes[1] → nodes[3], Right child → nodes[4]
#    - Left child of nodes[2] → nodes[5], Right child → nodes[6]
# 4. Time Complexity: O(1), as we insert a fixed number of 7 nodes.
# 5. Space Complexity: O(1), as we use a fixed number of pointers.
# ---------------------------------------------------

# Define a class for the tree node
class TreeNode:
    def __init__(self, val):
        self.val = val  # Node value
        self.left = None  # Left child
        self.right = None  # Right child

# Function to create a binary tree from the given level order list
def create_tree(root, vec):
    if len(vec) != 7:  # Ensuring there are exactly 7 nodes
        return
    
    # Creating nodes for the tree
    root.left = TreeNode(vec[1])  # Left child of root
    root.right = TreeNode(vec[2])  # Right child of root

    root.left.left = TreeNode(vec[3])  # Left child of node[1]
    root.left.right = TreeNode(vec[4])  # Right child of node[1]

    root.right.left = TreeNode(vec[5])  # Left child of node[2]
    root.right.right = TreeNode(vec[6])  # Right child of node[2]

# Function to print the tree in level order
def print_tree(root):
    if not root:
        return
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")  # Print node value
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()

# Example usage:
nodes = [1, 2, 3, 4, 5, 6, 7]
root = TreeNode(nodes[0])  # Root of the tree
create_tree(root, nodes)
print_tree(root)  # Output: 1 2 3 4 5 6 7


""" 
Explanation:
We first define a TreeNode class for representing each node.
The create_tree function manually assigns left and right children based on level-order indexing.
The print_tree function performs a level-order traversal to verify the tree structure.
The time complexity is O(1) because we are inserting only 7 nodes.
The space complexity is O(1) because we use a fixed number of pointers.
"""