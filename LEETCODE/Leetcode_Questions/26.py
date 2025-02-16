"""
Since the input arrays a[] and b[] are already sorted, we can use the two-pointer technique to efficiently find the union of both arrays while ensuring uniqueness.
"""
## 1st Approach is "Set"

def find_union(arr1, arr2):
    s = set()
    union = []
    
    for num in arr1:
        s.add(num)
    
    for num in arr2:
        s.add(num)
    
    for num in s:
        union.append(num)
    
    return union

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)

""" 
Time Compleixty : O( (m+n)log(m+n) ) . Inserting an element in a set takes logN time, where N is no of elements in the set. At max set can store m+n elements {when there are no common elements and elements in arr,arr2 are distntict}. So Inserting m+n th element takes log(m+n) time. Upon approximation across inserting all elements in worst, it would take O((m+n)log(m+n) time.

Using HashSet also takes the same time, On average insertion in unordered_set takes O(1) time but sorting the union vector takes O((m+n)log(m+n))  time. Because at max union vector can have m+n elements.

Space Complexity : O(m+n) {If Space of Union ArrayList is considered} 

O(1) {If Space of union ArrayList is not considered
"""





### 2). Using Array method 

def unionUnsortedArrays(a, b):
    """
    This function takes two unsorted arrays as input, sorts them, 
    and then finds their union while ensuring distinct elements in sorted order.

    :param a: List[int] - First array (unsorted)
    :param b: List[int] - Second array (unsorted)
    :return: List[int] - Sorted union of both arrays with unique elements
    """
    
    # Step 1: Sort both arrays
    a.sort()
    b.sort()
    
    # Step 2: Initialize two pointers for both arrays
    i, j = 0, 0
    result = []  # This will store the final union of both arrays

    # Step 3: Use two-pointer technique to find the union
    while i < len(a) and j < len(b):
        # If current element of 'a' is smaller, add it to result (if unique)
        if a[i] < b[j]: 
            if not result or result[-1] != a[i]:  # Ensure no duplicates
                result.append(a[i])  
            i += 1  # Move pointer in 'a'
        
        # If current element of 'b' is smaller, add it to result (if unique)
        elif a[i] > b[j]: 
            if not result or result[-1] != b[j]:  # Ensure no duplicates
                result.append(b[j])  
            j += 1  # Move pointer in 'b'
        
        # If both elements are equal, add only one of them to result (if unique)
        else:  # a[i] == b[j]
            if not result or result[-1] != a[i]:  # Ensure no duplicates
                result.append(a[i])  
            i += 1  # Move both pointers since the element is processed
            j += 1  

    # Step 4: Add any remaining elements from 'a' (to ensure all elements are included)
    while i < len(a):
        if not result or result[-1] != a[i]:  # Ensure no duplicates
            result.append(a[i])
        i += 1  # Move pointer in 'a'

    # Step 5: Add any remaining elements from 'b' (to ensure all elements are included)
    while j < len(b):
        if not result or result[-1] != b[j]:  # Ensure no duplicates
            result.append(b[j])
        j += 1  # Move pointer in 'b'

    return result  # Return the final sorted union array

# Example Usage
print(unionUnsortedArrays([5, 3, 1, 4, 2], [6, 3, 2, 7, 1]))  # Output: [1, 2, 3, 4, 5, 6, 7]
print(unionUnsortedArrays([5, 4, 3, 2, 2], [4, 3, 1, 1, 2]))  # Output: [1, 2, 3, 4, 5]
print(unionUnsortedArrays([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]))  # Output: [1, 2]

""" 
Why Use the Two-Pointer Technique?
✅ Time Complexity: O(n + m) (Much faster than merging and sorting)
✅ Space Complexity: O(n + m) (Stores unique elements in the result)
✅ Efficient for large input sizes (up to 10^5 elements in each array)

This approach avoids extra sorting and removes duplicates efficiently while keeping the union sorted
"""

# ---------------------------------------------------------------------------------------------------------------------------------------------------
 ## OR ### 
 
# Striver Ka code 

def find_union(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)

