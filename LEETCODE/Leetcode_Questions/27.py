# Count Maximum Consecutive One's in the array
from typing import List




class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi, cnt)
        return maxi




if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    obj = Solution()
    ans = obj.findMaxConsecutiveOnes(nums)
    print("The maximum  consecutive 1's are", ans)


    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ## OR ## 
def findMaxConsecutiveOnes(nums):
    """
    This function returns the maximum number of consecutive 1's in a binary array.

    :param nums: List[int] - A binary array containing 0s and 1s
    :return: int - Maximum count of consecutive 1's
    """
    
    max_count = 0  # To store the maximum count of consecutive 1s
    current_count = 0  # To track the ongoing sequence of 1s

    for num in nums:
        if num == 1:
            current_count += 1  # Increment count if 1 is found
            max_count = max(max_count, current_count)  # Update max count
        else:
            current_count = 0  # Reset count when a 0 is encountered

    return max_count

# Example Usage
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))  # Output: 2

