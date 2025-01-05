# Rotate an array to the right by 'k' steps
def rotate_array(nums, k):
    """
    Rotates the array to the right by k steps.
    
    Parameters:
        nums (list): The input array to be rotated.
        k (int): The number of steps to rotate the array.
    
    Returns:
        list: The rotated array.
    """
    n = len(nums)
    
    # Handle cases where k is greater than the array size
    k %= n  # Only rotate the necessary number of times
    
    # Steps:
    # 1. Reverse the entire array
    nums.reverse()
    # 2. Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    # 3. Reverse the remaining elements
    nums[k:] = reversed(nums[k:])
    
    return nums

# User Input
nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
k = int(input("Enter the number of steps to rotate the array: "))

# Function Call
rotated_array = rotate_array(nums, k)

# Output the result
print("Rotated Array:", rotated_array)
"""
Reverse the Entire Array:

When the array is reversed, the last element comes to the front.
Reverse the First k Elements:

This step ensures that the first part (rotated portion) is in the correct order.
Reverse the Remaining Elements:

The rest of the array is reversed back to its original order.
Example Walkthrough:
Input:
plaintext
Copy code
Array: [1, 2, 3, 4, 5, 6, 7]
Steps to rotate (k): 3
Process:
Reverse the entire array:
[7, 6, 5, 4, 3, 2, 1]
Reverse the first k=3 elements:
[5, 6, 7, 4, 3, 2, 1]
Reverse the remaining elements:
[5, 6, 7, 1, 2, 3, 4]
Output:
plaintext
Copy code
Rotated Array: [5, 6, 7, 1, 2, 3, 4]
This method is efficient, with a time complexity of 
O(n) and a space complexity of 
O(1)








"""