# Bubble Sort Algorithm
# This function sorts a list in ascending order using the bubble sort technique.
def bubble_sort(arr):
    # Traverse through all array elements
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted, so no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements if out of order

# Taking user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Calling the bubble_sort function
bubble_sort(arr)

# Printing the sorted array
print("Sorted array is:", arr)


"""
Explanation of Code:
Bubble Sort repeatedly compares adjacent elements in the list and swaps them if they are in the wrong order. This "bubbles" the largest unsorted element to the end of the list with each pass.
Outer loop: It runs through the entire list, reducing the range each time since the largest elements are placed at the end in each pass.
Inner loop: Compares each element with the next one and swaps them if they are in the wrong order.
Time Complexity: O(n^2) in both the best and worst cases, making it inefficient for larger datasets.


"""