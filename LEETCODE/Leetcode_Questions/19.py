""" 
Optimal Approach: Single Pass Iteration
Time Complexity: O(n) (Single traversal)
Space Complexity: O(1) (No extra space used)

"""
def largestElement(arr):
    return max(arr)  # Using built-in max function

# Example Usage:
print(largestElement([1, 8, 7, 56, 90]))  # Output: 90
print(largestElement([5, 5, 5, 5]))  # Output: 5
print(largestElement([10]))  # Output: 10
# ---------------------------------------------------------------------------------------------------------------------------

""" 
Manual Approach (Without max() Function)
If you want to find the largest element manually, iterate through the array:

"""
def largestElement(arr):
    largest = arr[0]  # Initialize with the first element
    for num in arr:
        if num > largest:
            largest = num  # Update if a larger element is found
    return largest

# Example Usage:
print(largestElement([1, 8, 7, 56, 90]))  # Output: 90
print(largestElement([5, 5, 5, 5]))  # Output: 5
print(largestElement([10]))  # Output: 10

""" Why is this Efficient?
We traverse the array once, so the time complexity is O(n).
No extra space is used apart from a single variable.
"""