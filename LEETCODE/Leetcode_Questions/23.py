# Rotate array by K elements

def rotate(nums, k):
    n = len(nums)
    k %= n  # Handle cases where k > n
    
    # Reverse the entire array
    nums.reverse()
    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    # Reverse the remaining n-k elements
    nums[k:] = reversed(nums[k:])

# Example usage
arr1 = [1,2,3,4,5,6,7]
rotate(arr1, 3)
print(arr1)  # Output: [5,6,7,1,2,3,4]

arr2 = [-1,-100,3,99]
rotate(arr2, 2)
print(arr2)  # Output: [3,99,-1,-100]


""" 
Explanation of the Reverse Method:
Reverse the entire array → [7,6,5,4,3,2,1]
Reverse the first k elements → [5,6,7,4,3,2,1]
Reverse the remaining elements → [5,6,7,1,2,3,4]
Why is this approach efficient?
✅ Time Complexity: O(n) (Each reversal takes O(n), and we do 3 reversals)
✅ Space Complexity: O(1) (Modifies array in place, no extra space)
✅ Handles Large k Values (Uses k %= n to avoid unnecessary rotations)

This is the most optimal way to rotate an array in-place in Python. 🚀
"""