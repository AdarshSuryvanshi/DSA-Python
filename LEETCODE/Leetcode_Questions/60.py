""" 
Finding Floor in a BST
The Floor of X in a BST is the greatest node value that is smaller than or equal to X.

Approach:
Start from the root of the BST.
If root's value is equal to X, return X (direct match).
If root's value is less than X, store it as a potential floor and move right (as a larger valid floor may exist).
If root's value is greater than X, move left (since all right-side values are greater and invalid
"""

def findFloor(root, x):
    floor = -1  # Default case when no floor is found

    while root:
        if root.val == x:  # Exact match found
            return x
        elif root.val < x:  # Potential floor, move right
            floor = root.val
            root = root.right
        else:  # Move left to find a smaller valid floor
            root = root.left

    return floor  # Return the stored floor value

""" 
Example Walkthrough
Example 1
Input:

python
Copy
Edit
root = [2, None, 81, 42, 87, None, None, 66, None, None, 90, 45]
x = 87
Tree Structure:

markdown
Copy
Edit
       2
        \
         81
        /   \
      42     87
        \       \
         66      90
        /
      45
Output: 87 (as 87 is present in BST)

Example 2
Input:

python
Copy
Edit
root = [6, None, 8, 7, 9]
x = 11
Tree Structure:

markdown
Copy
Edit
      6
       \
        8
       /  \
      7    9
Output: 9 (largest value ≤ 11)

Example 3
Input:

python
Copy
Edit
root = [6, None, 8, 7, 9]
x = 5
Output: -1 (no value ≤ 5 in BST)

Example Walkthrough
Example 1
Input:

python
Copy
Edit
root = [4,2,7,1,3]
val = 5
Tree Before Insertion:

markdown
Copy
Edit
      4
     / \
    2   7
   / \    
  1   3  
After Insertion (val = 5):

markdown
Copy
Edit
      4
     / \
    2   7
   / \  /
  1   3 5
Output: [4,2,7,1,3,5]

Example 2
Input:

python
Copy
Edit
root = [40,20,60,10,30,50,70]
val = 25
Tree Before Insertion:

markdown
Copy
Edit
       40
      /   \
    20     60
   /  \   /  \
 10   30 50   70
After Insertion (val = 25):

markdown
Copy
Edit
       40
      /   \
    20     60
   /  \   /  \
 10   30 50   70
      /
     25
Output: [40,20,60,10,30,50,70,null,null,25]


"""
