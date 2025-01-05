## LEFT ROTATE BY 1 


# Step 1: Take the size of the array as input
n = int(input("Enter the value of n: "))  # The number of elements in the array

# Step 2: Initialize the array and take input for each element
arr = []  # Original array
print("Enter the elements of the array:")
for i in range(n):
    arr.append(int(input()))  # Take each element as input

# Step 3: Create a new array to store the rotated elements
arr2 = [0] * n  # New array to store rotated result

# Step 4: Store the first element of arr[] in a temporary variable
temp = arr[0]  # Temporary variable to store the 0th index element

# Step 5: Shift all elements of arr[] to the left by one position
for i in range(1, n):
    arr2[i - 1] = arr[i]  # Store the element at position i to position i-1 in arr2

# Step 6: Place the first element of arr[] at the last position in arr2
arr2[n - 1] = temp  # Move the first element to the last position (n-1) in arr2

# Step 7: Print the rotated array
print("Elements after rotating the array to the left by 1 place:")
for element in arr2:
    print(element, end=" ")  # Print the elements of the rotated array
