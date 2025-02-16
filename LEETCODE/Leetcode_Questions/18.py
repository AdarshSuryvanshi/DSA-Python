# Question is :- https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
""" 
Optimal Approach: Sliding Window + Sorting
Time Complexity: O(n log n)
Space Complexity: O(1)
Approach:- 

Sort the array to make it easier to increment numbers from left to right.
Use a sliding window to find the largest subarray where all numbers can be made equal within k operations.
Maintain a window sum and adjust the left boundary when the cost exceeds k.
Return the maximum window size.

"""
def maxFrequency(nums, k):
    nums.sort()  # Sort the array
    left = 0
    total = 0
    max_freq = 0
    
    for right in range(len(nums)):
        total += nums[right]  # Add current number to total
        
        # While the cost exceeds k, shrink the window
        while (right - left + 1) * nums[right] - total > k:
            total -= nums[left]
            left += 1
        
        max_freq = max(max_freq, right - left + 1)
    
    return max_freq

# Example Usage:
print(maxFrequency([1,2,4], 5))  # Output: 3
print(maxFrequency([1,4,8,13], 5))  # Output: 2
print(maxFrequency([3,9,6], 2))  # Output: 1


""" 
Explanation
Example 1:
Input: nums = [1,2,4], k = 5
Sorted: [1,2,4]

Expand window to [1,2], total = 3, cost = 2-1=1 (Valid)
Expand window to [1,2,4], total = 7, cost = (3×4) - 7 = 5 (Valid)
✅ Max frequency = 3.
Example 2:
Input: nums = [1,4,8,13], k = 5
Sorted: [1,4,8,13]

Expand window to [1,4], cost = (2×4) - 5 = 3 (Valid)
Expand window to [1,4,8], cost = (3×8) - 13 = 11 (Invalid, shrink)
Expand [4,8], cost = (2×8) - 12 = 4 (Valid)
✅ Max frequency = 2.

Why is this Efficient?

Sorting takes O(n log n)

Sliding window traversal is O(n)
Overall O(n log n), which is optimal for n ≤ 10⁵.
✅ This approach efficiently finds the maximum frequency possible! 🚀

"""

## 2) Approach is :- 
""" 
def count_freq(arr):
    freq_map = {}

    # Count frequency of each element
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    max_freq = 0
    min_freq = float('inf')
    max_ele = min_ele = None

    # Find the elements with max and min frequency
    for num, freq in freq_map.items():
        if freq > max_freq:
            max_freq = freq
            max_ele = num
        if freq < min_freq:
            min_freq = freq
            min_ele = num

    print(f"The highest frequency element is: {max_ele}")
    print(f"The lowest frequency element is: {min_ele}")

# Example usage
arr = [10, 5, 10, 15, 10, 5]
count_freq(arr)

"""