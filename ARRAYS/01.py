# Title: Check if an Array is Sorted
# Concept:
# 1. This program checks if a given array is sorted in non-decreasing order.
# 2. The condition for being sorted is that each element should be greater than 
#    or equal to the previous element.
# 3. If we find any element that violates this condition, the array is not sorted.
# 4. The program prints "Array is not sorted" if the condition fails. 
#    Otherwise, the absence of such a message indicates the array is sorted.

# Input: Array of integers entered by the user.
# Output: A message if the array is not sorted; no message if sorted.

# Let's write the Python equivalent of the given C++ code:

# Prompt the user to enter the size of the array
n = int(input("Enter the value of n: "))  # Input the size of the array

# Initialize an empty list to store array elements
arr = []

# Input the elements of the array
print("Enter the elements of the array:")
for i in range(n):
    arr.append(int(input()))  # Append each element to the list

# Iterate through the array to check if it is sorted
for i in range(1, n):  # Start from index 1, as we compare with the previous element
    if arr[i] < arr[i - 1]:
        # If the current element is less than the previous element, the array is not sorted
        print("Array is not sorted")
        break  # Exit the loop as we've found the issue
else:
    # If no break occurred, the array is sorted
    print("Array is sorted")




"""
Explanation of Changes:
Dynamic Array Handling: Python lists are dynamic, so you don't need to specify the size beforehand.
Input Handling: Used input() to read values, as Python doesn't have cin.
Indexing: Python uses zero-based indexing, similar to C++.
Loop: The loop starts from index 1 because we compare each element with its previous element.
"""