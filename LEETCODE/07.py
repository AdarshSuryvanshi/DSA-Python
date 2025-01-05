def find_max_consecutive_ones(nums):
    """
    Finds the maximum number of consecutive 1's in a binary array.
    
    Parameters:
        nums (list): A list of integers containing only 0s and 1s.
    
    Returns:
        int: The maximum count of consecutive 1's in the array.
    """
# To count in the array How many times 1 comes "consecutivly "

    max_count = 0  # Variable to track the maximum count of consecutive 1's
    count = 0      # Variable to track the current streak of consecutive 1's...i.e To count the current contunuation 

    # Iterate through the array
    for num in nums:
        if num == 1:
            count += 1  # Increment the count for consecutive 1's
        else:
            max_count = max(max_count, count)  # Update max_count if needed
            count = 0  # Reset count if a 0 is encountered

    # Final check in case the array ends with 1's
    max_count = max(max_count, count)
    
    return max_count

# User Input
nums = list(map(int, input("Enter a binary array (0s and 1s) separated by spaces: ").split()))

# Function Call
result = find_max_consecutive_ones(nums)

# Output the result
print(f"The maximum number of consecutive 1's in the array is: {result}")
"""
Explanation:
Initialization:

max_count: Tracks the overall maximum number of consecutive 1's.
count: Tracks the current streak of consecutive 1's as we traverse the array.
Iteration:

If the current number is 1, increment count.
If the current number is 0, compare count with max_count to update the maximum streak and reset count to 0.
Final Update:

Perform a final comparison between count and max_count in case the array ends with 1's.
Return:

Return max_count, which holds the maximum number of consecutive 1's.
Example Walkthrough:
Input:
plaintext
Copy code
Enter a binary array (0s and 1s) separated by spaces: 1 1 0 1 1 1 0 1
Process:
Array: [1, 1, 0, 1, 1, 1, 0, 1]
Iteration:
1 → count = 1, max_count = 0
1 → count = 2, max_count = 0
0 → max_count = 2, count = 0
1 → count = 1, max_count = 2
1 → count = 2, max_count = 2
1 → count = 3, max_count = 2
0 → max_count = 3, count = 0
1 → count = 1, max_count = 3
Output:
plaintext
Copy code
The maximum number of consecutive 1's in the array is: 3
Complexity:
Time Complexity: 

O(n):
Single pass through the array.
Space Complexity: 
O(1):
Only uses constant extra space.






"""