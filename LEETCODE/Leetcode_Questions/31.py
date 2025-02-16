# Sort an array of 0's 1's and 2's


# 🚀 Sort Colors (Dutch National Flag Algorithm)
# 📌 Concept: Three-way partitioning (0s, 1s, and 2s)
# ✅ Time Complexity: O(n) (Single Pass)
# ✅ Space Complexity: O(1) (In-place Sorting)
# 📌 This approach efficiently sorts the array in one pass.

def sortColors(nums):
    left, mid, right = 0, 0, len(nums) - 1  # Three pointers

    while mid <= right:
        if nums[mid] == 0:  # If the current element is 0
            nums[left], nums[mid] = nums[mid], nums[left]  # Swap with left
            left += 1
            mid += 1
        elif nums[mid] == 1:  # If the current element is 1
            mid += 1  # Move mid forward
        else:  # If the current element is 2
            nums[mid], nums[right] = nums[right], nums[mid]  # Swap with right
            right -= 1  # Move right pointer left

# Example Test Cases
nums1 = [2, 0, 2, 1, 1, 0]
sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]
