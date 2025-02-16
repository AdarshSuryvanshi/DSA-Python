""" 
Approach to Delete a Node in BST
To delete a node in a Binary Search Tree (BST):

Search for the Node:
If key < root.val, move left.
If key > root.val, move right.
If key == root.val, we found the node to delete.
Delete the Node (Three Cases):
Case 1: The node is a leaf (has no children) → Delete it directly.
Case 2: The node has one child (left or right) → Replace the node with its child.
Case 3: The node has two children → Find the inorder successor (smallest node in the right subtree), replace the node’s value with it, and delete the successor.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root, key):
    if not root:
        return None  # If tree is empty or key not found

    if key < root.val:
        root.left = deleteNode(root.left, key)  # Move left
    elif key > root.val:
        root.right = deleteNode(root.right, key)  # Move right
    else:
        # Case 1 & 2: Node has 0 or 1 child
        if not root.left:
            return root.right  # Replace with right child (or None)
        elif not root.right:
            return root.left  # Replace with left child (or None)
        
        # Case 3: Node has two children
        successor = findMin(root.right)  # Find inorder successor
        root.val = successor.val  # Replace with successor value
        root.right = deleteNode(root.right, successor.val)  # Delete successor

    return root  # Return updated root

def findMin(node):
    while node.left:
        node = node.left  # Find leftmost (smallest) node
    return node

""" 
Time & Space Complexity
Time Complexity: 

h is the height of the BST (

O(logn) for balanced BST, 

O(n) in worst case).
Space Complexity: 

O(h) due to recursion stack (or 
O(1) if using an iterative approach).

Example Walkthrough
Example 1
Input:

python
Copy
Edit
root = [5,3,6,2,4,null,7]
key = 3
Tree Before Deletion (key = 3):

markdown
Copy
Edit
      5
     / \
    3   6
   / \    \
  2   4    7
After Deletion (key = 3):

markdown
Copy
Edit
      5
     / \
    4   6
   /     \
  2       7
Output: [5,4,6,2,null,null,7]

Example 2
Input:

python
Copy
Edit
root = [5,3,6,2,4,null,7]
key = 0
0 is not in the BST, so the tree remains unchanged.
Output: [5,3,6,2,4,null,7]
Example 3
Input:

python
Copy
Edit
root = []
key = 0
Tree is empty, so output remains [].

"""
