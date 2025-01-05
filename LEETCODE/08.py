def single_number(nums):
    """
    Finds the single number in the array that appears only once.
    
    Parameters:
        nums (list): A list of integers where every element appears twice except one.
    
    Returns:
        int: The number that appears only once, or -1 if no such number exists.
    """
    # Step 1: Create an empty dictionary to store the count of each number
    count_map = {}

    # Step 2: Count how many times each number appears in the list
    for num in nums:
        if num in count_map:
            count_map[num] += 1  # If the number is already in dictionary, increase its count
        else:
            count_map[num] = 1  # If it's the first time we see this number, set its count to 1

    # Step 3: Find the number that appears only once
    for num in nums:
        if count_map[num] == 1:
            return num  # Return the number that appears only once

    return -1  # If no number appears only once, return -1 (though this shouldn't happen in this case)

# User Input
nums = list(map(int, input("Enter the list of integers (space-separated): ").split()))

# Function Call
result = single_number(nums)

# Output the result
print(f"The number that appears only once is: {result}")
"""
Explanation:
Step 1 (Initialize count_map):

We use a dictionary (count_map) to store how many times each number appears in the input list.
Step 2 (Count Occurrences):

We loop through the list nums, and for each number, we either add it to the dictionary or increment its count if it's already there.
Step 3 (Find the Unique Number):

We loop through the list again to find the first number that appears exactly once in the dictionary and return it.
Return Value:

If we find a number that appears once, we return that number. If no such number is found, we return -1, though in most cases it will not happen because the problem assumes there's exactly one number that appears only once.
Example Walkthrough:
Input:
plaintext
Copy code
Enter the list of integers (space-separated): 4 1 2 1 2
Process:
Array: [4, 1, 2, 1, 2]
Count the occurrences of each element:
4 appears 1 time.
1 appears 2 times.
2 appears 2 times.
The number that appears only once is 4.
Output:
plaintext
Copy code
The number that appears only once is: 4
Complexity:
Time Complexity: 

O(n)
We loop through the array twice: once to populate the dictionary and once to check the values.
Space Complexity: 

O(n)
We are using extra space for the dictionary that stores the count of each number.
This approach efficiently handles the problem with a simple and clear solution!








"""