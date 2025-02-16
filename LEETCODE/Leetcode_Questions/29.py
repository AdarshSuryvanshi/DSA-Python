## Longest Subaray 

## 1) Brute-Fore Approach :- 
from typing import List

def getLongestSubarray(a, k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        for j in range(i, n): # ending index
            # add all the elements of
            # subarray = a[i...j]:
            s = 0
            for K in range(i, j+1):
                s += a[K]

            if s == k:
                length = max(length, j - i + 1)
    return length

if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")

""" 
Complexity Analysis

Time Complexity: O(N3) approx., where N = size of the array.
Reason: We are using three nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.


"""
# 2)  Better Approch_1 :-

from typing import List

def getLongestSubarray(a, k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        s = 0
        for j in range(i, n): # ending index
            # add the current element to
            # the subarray a[i...j-1]:
            s += a[j]

            if s == k:
                length = max(length, j - i + 1)
    return length

if __name__ == '__main__':
    a = [2, 3, 5, 1, 9]
    k = 10
    len = getLongestSubarray(a, k)
    print("The length of the longest subarray is:", len)
""" 
   Complexity Analysis

Time Complexity: O(N2) approx., where N = size of the array.
Reason: We are using two nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.

 
"""

# 3) Optimal  Approch _2 :- 

# ***************************************
# Title: Longest Subarray with Sum K
# ***************************************

# 🔹 **Concept: Prefix Sum with HashMap**
# 
# ✅ **Understanding Prefix Sum:**
# - A **prefix sum** is the sum of all elements from the start of the array to the current index.
# - If `prefix_sum[j] - prefix_sum[i] = k`, then the subarray from `i+1` to `j` has sum `k`.
# 
# ✅ **Key Idea:**
# - Use a **dictionary (hashmap)** to store `prefix_sum` and its **first occurrence index**.
# - If `prefix_sum - k` exists in the hashmap, update `max_length`.

# ✅ **Time Complexity: O(n)** (Single pass through the array)
# ✅ **Space Complexity: O(n)** (For storing prefix sums)

def longest_subarray_with_sum_k(arr, k):
    prefix_map = {}  # Dictionary to store first occurrence of prefix_sum
    prefix_sum = 0  # Keeps track of cumulative sum
    max_length = 0  # Stores the length of the longest subarray with sum k

    for i in range(len(arr)):  
        prefix_sum += arr[i]  # Add current element to prefix_sum

        # ✅ Case 1: If prefix_sum itself is equal to k, update max_length
        if prefix_sum == k:
            max_length = i + 1  

        # ✅ Case 2: If prefix_sum - k exists in dictionary, update max_length
        if (prefix_sum - k) in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum - k])

        # ✅ Store prefix_sum in dictionary if not already present
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i  

    return max_length  # Return the longest subarray length

# 🔹 Example Test Cases
print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, -10], 15))  # Output: 6
print(longest_subarray_with_sum_k([-5, 8, -14, 2, 4, 12], -5)) # Output: 5
print(longest_subarray_with_sum_k([10, -10, 20, 30], 5))       # Output: 0

""" 
Index:        0   1   2   3   4   5  
Array:       10   5   2   7   1  -10  
Prefix Sum:  10  15  17  24  25   15
"""

