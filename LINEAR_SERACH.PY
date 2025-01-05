# Linear Search Algorithm
# This function searches for a target element in the list by checking each element.
def linear_search(arr, target):
    # Loop through each element of the array
    for i in range(len(arr)):
        # If the element is found, return its index
        if arr[i] == target:
            return i  # Return the index where the target is found
    # If the element is not found, return -1
    return -1

# Example Usage
arr = [10, 20, 30, 40, 50]  # Sample array
target = 30  # Element to search for

# Calling the linear_search function
result = linear_search(arr, target)

# Checking the result
if result != -1:
    print(f"Element found at index {result}")  # Print index if found
else:
    print("Element not found")  # Print if element is not found



"""
The linear_search function takes a list (arr) and a target value as inputs.
It loops through each element in the list using a for loop.
If it finds an element equal to the target, it returns the index of that element.
If it doesn’t find the target after checking all elements, it returns -1 to indicate that the target was not found


"""