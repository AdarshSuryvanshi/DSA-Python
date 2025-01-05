
# WE CAN DO LOTS OF THINGS USING THIS CONCEPTS 

def find_occurrence(nums):
    """
    Finds the first element in the array that occurs only once.
    
    Parameters:
        nums (list): The input array of integers.
    
    Returns:
        int: The first unique number in the array, or -1 if none exist.
    """
    # Step 1: Find the maximum element to define hash array size
    max_element = max(nums) if nums else 0  # Handle empty array edge case

    # Step 2: Create a hash array with size `max_element + 1`
    hash_array = [0] * (max_element + 1)

    # Step 3: Populate the hash array with counts of each number in `nums`
    for num in nums:
        hash_array[num] += 1

    # Step 4: Find and return the number that occurs only once
    for num in nums:
        if hash_array[num] == 1:
            return num
    """
    K= K is the number which i have to find out how many that number appears in the Array 
    for num in nums:
        if num == k:
            return hash_array[num]
    
    """
        
    

    # If no unique element is found, return -1
    return -1

# User Input
nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Function Call
result = find_occurrence(nums)

# Output the result
if result != -1:
    print(f"The first unique number in the array is: {result}")
else:
    print("No unique number found in the array.")
    
"""
Explanation:
Step 1: Find Maximum Element:

This determines the size of the hash array (to handle all possible values in the input array).
Step 2: Create Hash Array:

A list (hash_array) of size max_element + 1 is initialized with 0. Each index in this list represents a number in the input, and the value at the index represents the count of occurrences.
Step 3: Populate Hash Array:

For each number in nums, increment the corresponding index in hash_array to record its frequency.
Step 4: Check for Unique Occurrence:

Iterate through nums again, and find the first number that has a frequency of 1 in hash_array.
Edge Cases:

If no unique number exists, return -1.
Handle an empty array by returning -1.
Example Walkthrough:
Input:
plaintext
Copy code
Enter the elements of the array separated by spaces: 4 3 3 2 4 5 2
Process:
Maximum element = 5.
Initialize hash_array = [0, 0, 0, 0, 0, 0].
Populate counts:
Array: [4, 3, 3, 2, 4, 5, 2]
hash_array: [0, 0, 2, 2, 2, 1]
Traverse nums:
Check: 4 → Count = 2
Check: 3 → Count = 2
Check: 2 → Count = 2
Check: 5 → Count = 1 → Return 5.
Output:
plaintext
Copy code
The first unique number in the array is: 5
Complexity:
Time Complexity: 

O(n):
Finding max_element takes 

O(n).
Populating the hash array takes 

O(n).
Checking for unique elements takes 

O(n).
Space Complexity: 

O(k), where 
𝑘
k is max_element + 1 (size of the hash array).






"""