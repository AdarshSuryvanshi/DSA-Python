from collections import defaultdict

def majorityElement(nums):
    """
    Finds the majority element in the list `nums`, which is the element
    that appears more than n // 2 times, where n is the size of the list.

    Parameters:
        nums (list): A list of integers.

    Returns:
        int: The majority element if it exists, else -1.
    """
    n = len(nums)  # Get the size of the list
    mpp = defaultdict(int)  # Dictionary to store the frequency of each element
    
    # Count the frequency of each element
    for num in nums:
        mpp[num] += 1

    # Check for the element that appears more than n // 2 times
    for key, value in mpp.items():
        if value > n // 2:
            return key  # Return the majority element
    
    return -1  # Return -1 if no majority element exists

# User Input
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Function call
result = majorityElement(nums)

# Output the result
print(f"The majority element is: {result}")
"""
Explanation:
Using a Dictionary (defaultdict):

A defaultdict is used to keep track of the frequency of each element in the input list nums. By default, it initializes the count of each element to zero.
Counting Occurrences:

We iterate through each element in the list and increase its count in the dictionary.
Finding the Majority Element:

After counting the occurrences, we check for an element that appears more than n // 2 times, where n is the total number of elements in the list.
Returning the Result:

If such an element is found, it is returned as the majority element.
If no such element exists, we return -1.
Example Walkthrough:
Input:
plaintext
Copy code
Enter numbers separated by space: 3 3 4 2 4 4 2 4 4
Process:
The list of numbers is [3, 3, 4, 2, 4, 4, 2, 4, 4].
The frequency of each element is counted:
3 appears 2 times
4 appears 5 times
2 appears 2 times
The majority element is 4, as it appears more than n // 2 (which is 4 in this case).
Output:
plaintext
Copy code
The majority element is: 4
Complexity Analysis:
Time Complexity: 
𝑂
(
𝑛
)
O(n), where n is the number of elements in the list. We iterate through the list once to count the frequencies and once more to check the frequencies.
Space Complexity: 
𝑂
(
𝑛
)
O(n), for storing the frequencies of each element in the dictionary.

"""