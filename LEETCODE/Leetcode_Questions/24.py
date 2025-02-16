##  Moves Zeros To End 

""" 
Most Optimzed Approach is "Two Pointer Approach 
"""
def moveZeroes(nums):
    n = len(nums)
    left = 0  # Pointer for placing non-zero elements
    
    # Move non-zero elements to the front
    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

# Example usage
arr1 = [0,1,0,3,12]
moveZeroes(arr1)
print(arr1)  # Output: [1,3,12,0,0]

arr2 = [0]
moveZeroes(arr2)
print(arr2)  # Output: [0]

""" 
xplanation of the Two-Pointer Approach:
Use left pointer to track where the next non-zero should go.
Use right pointer to iterate through the array.
Swap non-zero elements to the front while maintaining the relative order.
Why is this approach efficient?
✅ Time Complexity: O(n) (Single pass through the array)
✅ Space Complexity: O(1) (Modifies array in place, no extra space)
✅ Maintains Relative Order of non-zero elements

This is the most optimal way to move zeroes while keeping the relative order intact. 🚀
"""