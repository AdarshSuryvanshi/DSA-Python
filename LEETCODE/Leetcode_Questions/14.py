"""
Reverse an Array In-Place
We need to reverse the given array in place, meaning we cannot use extra space.

Efficient Approach (Two-Pointer Method)
Use two pointers, one at the start and one at the end of the array.
Swap the elements at these positions.
Move the pointers towards the center until they meet
"""
### TO SOLVE THIS QUESTION 1ST APPROACH THAT COMES IN OUR MIND IS 
# 1).SLICING :- Arr=[::-1] , But this not the Optimized One , Most Optimized is 
## 2) Two Pointer Approach:-
#  
def reverseArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap elements
        left += 1
        right -= 1

# Test Cases
arr1 = [1, 4, 3, 2, 6, 5]
reverseArray(arr1)
print(arr1)  # Output: [5, 6, 2, 3, 4, 1]

arr2 = [4, 5, 2]
reverseArray(arr2)
print(arr2)  # Output: [2, 5, 4]

""" 
Complexity Analysis
✅ Time Complexity: O(n) (Each element is swapped once)
✅ Space Complexity: O(1) (No extra space used)


"""