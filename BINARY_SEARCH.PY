# Binary Search Algorithm
# This function searches for a target element in a sorted list using binary search.
def binary_search(arr, target):
    low = 0  # Start of the list
    high = len(arr) - 1  # End of the list

    while low <= high:
        mid = (low + high) // 2  # Find the middle index

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            low = mid + 1  # Narrow the search to the right half
        else:
            high = mid - 1  # Narrow the search to the left half

    return -1  # If the target is not found

# Example Usage
arr = [10, 20, 30, 40, 50]  # Sample sorted array
target = 30  # Element to search for

# Calling the binary_search function
result = binary_search(arr, target)

# Checking the result
if result != -1:
    print(f"Element found at index {result}")  # Print index if found
else:
    print("Element not found")  # Print if element is not found



"""
The binary_search function takes a sorted list (arr) and a target value as inputs.
It uses two variables, low and high, to keep track of the current bounds of the list being searched.
The middle element of the list is calculated, and if it matches the target, its index is returned.
If the target is smaller than the middle element, the search interval is narrowed to the left half; if it is larger, it narrows to the right half.
The search continues until the target is found or the search interval becomes invalid (low > high), in which case it returns -1..

"""