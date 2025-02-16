## Next Greater Element 2 :-
def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n  # Initialize result with -1
    stack = []  # Monotonic decreasing stack to store indices

    # Traverse the array twice to handle circular nature
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:  # Circular indexing
            result[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)  # Push only in the first pass

    return result

# Example Usage
nums1 = [1, 2, 1]
nums2 = [1, 2, 3, 4, 3]
print(nextGreaterElements(nums1))  # Output: [2, -1, 2]
print(nextGreaterElements(nums2))  # Output: [2, 3, 4, -1, 4]

""" 
Key Optimizations:
✅ Monotonic Stack: Stores indices, ensuring efficient O(n) complexity.
✅ Circular Handling: We iterate twice (2 * n) using nums[i % n] to simulate a circular array.
✅ Single Pass Stack Update: We only push indices in the first traversal to avoid redundancy.

Time Complexity:
O(n) because each element is pushed and popped at most once.
Space Complexity:
O(n) for storing the results and stack in the worst case.
"""