## Binary Search 
def sortedArraySearch(arr, k):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return True  # Element found
        elif arr[mid] < k:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return False  # Element not found

# Example Usage
print(sortedArraySearch([1, 2, 3, 4, 6], 6))  # Output: True
print(sortedArraySearch([1, 2, 4, 5, 6], 3))  # Output: False
print(sortedArraySearch([2, 3, 5, 6], 1))     # Output: False
