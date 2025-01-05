# Selection Sort Algorithm
# This function sorts a list in ascending order using the selection sort algorithm.
def selection_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i  
        # Find the smallest element in the remaining unsorted part of the list
        for j in range(i+1, n):  
            if arr[j] < arr[min_index]:
                min_index = j  # Update the minimum index
        # Swap the smallest found element with the element at the current index
        arr[i], arr[min_index] = arr[min_index], arr[i]  

# Taking user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Calling the selection_sort function
selection_sort(arr)

# Printing the sorted array
print("Sorted array is:", arr)


"""
The code now takes user input for the size of the array (n).
The user is asked to input each element of the array.
After the input is collected, the selection_sort function is called to sort the array.
Finally, the sorted array is printed.
"""