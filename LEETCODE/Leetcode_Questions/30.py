# Two Sum : Check if a pair with given sum exists in Array

# ***************************************
# Title: Two Sum Problem
# ***************************************

# 🔹 **Concept: HashMap (Dictionary in Python)**
#
# ✅ **Understanding the Problem:**
# - We are given an **array `nums`** and a **target sum**.
# - We need to find **two indices** whose values add up to the target.
# - **Each input has exactly one solution**, meaning we do not need to handle multiple cases.
#
# ✅ **Optimized Approach: Using HashMap (Dictionary)**
# - Use a dictionary to store **each number's index** as we iterate through the array.
# - For each number `num`, check if `target - num` exists in the dictionary.
# - If found, return the indices.
#
# ✅ **Time Complexity: O(n)** (Single pass through the array)
# ✅ **Space Complexity: O(n)** (For storing indices in dictionary)

def two_sum(nums, target):
    num_map = {}  # Dictionary to store {number: index}

    
    for i in range(len(nums)):  # Loop through the array
        complement = target - nums[i]  # Calculate the required complement


        # ✅ If complement exists in dictionary, return the indices
        if complement in num_map:
            return [num_map[complement], i]

        # ✅ Store the current number and its index in dictionary
        num_map[nums[i]] = i  

    return []  # This line will never be reached since a solution always exists

# 🔹 Example Test Cases
print(two_sum([2, 7, 11, 15], 9))  # Output: [0,1]
print(two_sum([3, 2, 4], 6))       # Output: [1,2]
print(two_sum([3, 3], 6))          # Output: [0,1]
