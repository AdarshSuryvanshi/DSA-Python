# Let's define the Node class first. A node will represent each element in the tree.
class Node:
    def __init__(self, data):
        """
        Initialize a node with the given data.
        :param data: The value to store in the node.
        """
        self.data = data  # Store the value in the node.
        self.left = None  # Initially, no left child.
        self.right = None  # Initially, no right child.

# Now, let's define the Binary Search Tree (BST) class
class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty Binary Search Tree (BST).
        """
        self.root = None  # Initially, the tree has no root.

    def insert(self, data):
        """
        Insert a node with the given data into the BST.
        :param data: The value to insert into the tree.
        """
        if self.root is None:
            # If the tree is empty, create the root node
            self.root = Node(data)
            print(f"Inserted {data} as the root of the tree.")
        else:
            # Otherwise, insert the node in the correct position
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """
        Helper function to insert data recursively.
        :param node: The current node in the tree where we want to insert the data.
        :param data: The value to insert into the tree.
        """
        if data < node.data:  # If data is smaller than current node, go to the left
            if node.left is None:  # If no left child, insert here
                node.left = Node(data)
                print(f"Inserted {data} as the left child of {node.data}.")
            else:
                self._insert_recursive(node.left, data)  # Recursively insert into the left subtree
        else:  # If data is greater than current node, go to the right
            if node.right is None:  # If no right child, insert here
                node.right = Node(data)
                print(f"Inserted {data} as the right child of {node.data}.")
            else:
                self._insert_recursive(node.right, data)  # Recursively insert into the right subtree

    def search(self, data):
        """
        Search for a node with the given data in the BST.
        :param data: The value to search in the tree.
        :return: True if found, False otherwise.
        """
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        """
        Helper function to search for data recursively.
        :param node: The current node in the tree where we search for the data.
        :param data: The value to search for.
        :return: True if found, False otherwise.
        """
        if node is None:
            return False  # If node is None, data is not found.
        
        if data == node.data:
            return True  # If data matches the node's value, found it.
        
        elif data < node.data:
            return self._search_recursive(node.left, data)  # Search in left subtree if data is smaller.
        
        else:
            return self._search_recursive(node.right, data)  # Search in right subtree if data is larger.

    def delete(self, data):
        """
        Delete a node with the given data from the BST.
        :param data: The value to delete from the tree.
        """
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        """
        Helper function to delete a node recursively.
        :param node: The current node in the tree where we will delete the data.
        :param data: The value to delete.
        :return: The updated node after deletion.
        """
        if node is None:
            print(f"{data} not found in the tree!")
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)  # Search in the left subtree.
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)  # Search in the right subtree.
        else:  # We found the node to delete.
            if node.left is None:
                temp = node.right  # Node has only right child or no child.
                node = None  # Node is deleted.
                return temp  # Return the right child.
            elif node.right is None:
                temp = node.left  # Node has only left child.
                node = None  # Node is deleted.
                return temp  # Return the left child.
            
            # Node has two children, get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.data = temp.data  # Copy the inorder successor's value to this node.
            node.right = self._delete_recursive(node.right, temp.data)  # Delete the inorder successor.
        
        return node

    def _min_value_node(self, node):
        """
        Get the node with the smallest value (leftmost node).
        :param node: The starting node to find the minimum.
        :return: The node with the minimum value.
        """
        current = node
        while current.left is not None:
            current = current.left  # Traverse to the leftmost node.
        return current  # Return the leftmost node.

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the BST.
        This will print values in ascending order.
        """
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        """
        Helper function to traverse the tree in-order recursively.
        :param node: The current node in the tree to traverse.
        """
        if node:
            self._inorder_recursive(node.left)  # Traverse the left subtree.
            print(node.data, end=" -> ")  # Visit the node.
            self._inorder_recursive(node.right)  # Traverse the right subtree.

    def preorder_traversal(self):
        """
        Perform a preorder traversal of the BST.
        """
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        """
        Helper function to traverse the tree in preorder recursively.
        :param node: The current node in the tree to traverse.
        """
        if node:
            print(node.data, end=" -> ")  # Visit the node.
            self._preorder_recursive(node.left)  # Traverse the left subtree.
            self._preorder_recursive(node.right)  # Traverse the right subtree.

    def postorder_traversal(self):
        """
        Perform a postorder traversal of the BST.
        """
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        """
        Helper function to traverse the tree in postorder recursively.
        :param node: The current node in the tree to traverse.
        """
        if node:
            self._postorder_recursive(node.left)  # Traverse the left subtree.
            self._postorder_recursive(node.right)  # Traverse the right subtree.
            print(node.data, end=" -> ")  # Visit the node.

# Example of using the BinarySearchTree
if __name__ == "__main__":
    bst = BinarySearchTree()  # Create an empty BST.
    
    # Inserting nodes
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # Display tree in-order
    print("Inorder Traversal:")
    bst.inorder_traversal()
    print("\n")

    # Searching for a node
    print("Search for 40:", bst.search(40))  # Should return True
    print("Search for 25:", bst.search(25))  # Should return False

    # Deleting a node
    bst.delete(20)
    print("\nInorder Traversal after deletion:")
    bst.inorder_traversal()
    print("\n")

    # Preorder Traversal
    print("Preorder Traversal:")
    bst.preorder_traversal()
    print("\n")

    # Postorder Traversal
    print("Postorder Traversal:")
    bst.postorder_traversal()
