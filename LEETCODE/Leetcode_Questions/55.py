""" 
Solution: Check if Inorder Traversal is a Valid BST
A Binary Search Tree (BST) has the property that an inorder traversal of its nodes results in a strictly increasing sequence.

Approach
Iterate through the array and check whether it is strictly increasing (i.e., arr[i] < arr[i+1] for all valid i).
If all elements satisfy this condition, return True.
Otherwise, return False.

"""

def isValidBSTInorder(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:  # Check if the sequence is strictly increasing
            return False
    return True

# Example Test Cases
print(isValidBSTInorder([8, 14, 45, 64, 100]))  # Output: True
print(isValidBSTInorder([5, 6, 1, 8, 7]))      # Output: False

""" 
Complexity Analysis
Time Complexity: 

O(n) → We iterate through the list once.

Space Complexity: 

O(1) → We only use a few variables (constant space).
Edge Cases Considered
✅ Single element array (always valid).
✅ Already sorted unique elements (valid BST).
✅ Contains duplicate elements (invalid BST).
✅ Unsorted sequence (invalid BST).


"""