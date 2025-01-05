def move_zeroes(nums):
    """
    Moves all zeroes in the array to the end while maintaining the relative order of non-zero elements.
    
    Parameters:
        nums (list): The input array containing integers.
    
    Returns:
        None: The input array is modified in-place.
    """
    j = 0  # Pointer to track the position of the next non-zero element

    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the current non-zero element with the element at index j
            nums[i], nums[j] = nums[j], nums[i]
            j += 1  # Move the pointer forward for the next non-zero element

# User Input
nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Function Call
move_zeroes(nums)

# Output the result
print("Array after moving zeroes:", nums)
"""
Explanation:
Initialize a Pointer (j):

This pointer tracks the position where the next non-zero element should be placed.
Iterate Through the Array:

If the current element is not zero, swap it with the element at index j and increment j.
Zeroes Automatically Move to the End:

Non-zero elements are shifted forward while zeroes remain at the back.
Example Walkthrough:
Input:
plaintext
Copy code
Array: [0, 1, 0, 3, 12]
Process:
Initialize j = 0.
Traverse the array:
At i = 0: nums[i] is 0, do nothing.
At i = 1: nums[i] is 1, swap nums[1] and nums[0]. Array becomes [1, 0, 0, 3, 12], increment j = 1.
At i = 2: nums[i] is 0, do nothing.
At i = 3: nums[i] is 3, swap nums[3] and nums[1]. Array becomes [1, 3, 0, 0, 12], increment j = 2.
At i = 4: nums[i] is 12, swap nums[4] and nums[2]. Array becomes [1, 3, 12, 0, 0], increment j = 3.
Output:
plaintext
Copy code
Array after moving zeroes: [1, 3, 12, 0, 0]
Complexity:
Time Complexity: 
O(n) — Single pass through the array.
Space Complexity: 
O(1) — In-place modification of the array.






"""