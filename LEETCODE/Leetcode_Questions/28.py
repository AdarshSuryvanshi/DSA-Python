# Find the number that appears once, and the other numbers twice

## 1) Brute Force Approach :-




def getSingleElement(arr):
    # Size of the array:
    n = len(arr)

    # Run a loop for selecting elements:
    for i in range(n):
        num = arr[i]  # selected element
        cnt = 0

        # Find the occurrence using linear search:
        for j in range(n):
            if arr[j] == num:
                cnt += 1

        # If the occurrence is 1, return the number:
        if cnt == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)


if __name__ == '__main__':
    main()

""" 
Time Complexity: O(N2), where N = size of the given array.
Reason: For every element, we are performing a linear search to count its occurrence. The linear search takes O(N) time complexity. And there are N elements in the array. So, the total time complexity will be O(N2).

Space Complexity: O(1) as we are not using any extra space
"""

### 2) Better Approach 1 :- 



def getSingleElement(arr):
    # Size of the array:
    n = len(arr)

    # Find the maximum element:
    maxi = max(arr)

    # Declare hash array of size maxi+1
    # And hash the given array:
    hash = [0] * (maxi + 1)
    for num in arr:
        hash[num] += 1

    # Find the single element and return the answer:
    for num in arr:
        if hash[num] == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)


if __name__ == '__main__':
    main()



""" 
Time Complexity: O(N)+O(N)+O(N), where N = size of the array
Reason: One O(N) is for finding the maximum, the second one is to hash the elements and the third one is to search the single element in the array.

Space Complexity: O(maxElement+1) where maxElement = the maximum element of the array.


"""

### 3) Better Approach 2 :- 



def get_single_element(arr):
    # Size of the array:
    n = len(arr)

    # Declare the hashmap.
    # And hash the given array:
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1

    # Find the single element and return the answer:
    for num, count in hashmap.items():
        if count == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = get_single_element(arr)
    print("The single element is:", ans)


if __name__ == "__main__":
    main()

""" 
Time Complexity: O(N*logM) + O(M), where M = size of the map i.e. M = (N/2)+1. N = size of the array.
Reason: We are inserting N elements in the map data structure and insertion takes logM time(where M = size of the map). So this results in the first term O(N*logM). The second term is to iterate the map and search the single element. In Java, HashMap generally takes O(1) time complexity for insertion and search. In that case, the time complexity will be O(N) + O(M).

Note: The time complexity will be changed depending on which map data structure we are using. If we use unordered_map in C++, the time complexity will be O(N) for the best and average case instead of O(N*logM). But in the worst case(which rarely happens), it will be nearly O(N2).

Space Complexity: O(M) as we are using a map data structure. Here M = size of the map i.e. M = (N/2)+1.
"""


 # 4) Optimal Approach :- '
def singleNumber(nums):
    """
    This function finds the single number that appears only once in the array.
    Every other element appears twice.

    :param nums: List[int] - An array where every element appears twice except for one.
    :return: int - The single element that appears only once.
    """

    result = 0  # Initialize XOR result
    
    for num in nums:
        result ^= num  # XOR each number

    return result  # The single number remains

# Example Usage
print(singleNumber([2,2,1]))        # Output: 1
print(singleNumber([4,1,2,1,2]))    # Output: 4
print(singleNumber([1]))            # Output: 1

""" 
Explanation of XOR Approach 🔥
XOR Property: a ^ a = 0 and a ^ 0 = a
Since all numbers except one appear twice, their XOR cancels out (x ^ x = 0).
The remaining number (y) is the answer since 0 ^ y = y.
✅ Time Complexity: O(n) (Single pass)
✅ Space Complexity: O(1) (No extra space used)
"""