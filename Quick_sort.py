# Quick Sort Algorithm
# This function sorts an array using the quick sort method, which is a divide-and-conquer algorithm.
def quick_sort(arr):
    if len(arr) <= 1:  # Base case: if the list has one or no elements, it's already sorted
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Selecting the middle element as the pivot
        # Partitioning the array into three parts: less than pivot, equal to pivot, and greater than pivot
        left = [x for x in arr if x < pivot]  # Elements smaller than pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x > pivot]  # Elements greater than pivot
        # Recursively sorting the left and right parts, and combining them with the middle part
        return quick_sort(left) + middle + quick_sort(right)

# Taking user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Calling the quick_sort function
sorted_arr = quick_sort(arr)

# Printing the sorted array
print("Sorted array is:", sorted_arr)

"""
Quick Sort is a divide-and-conquer algorithm that divides the array into smaller sub-arrays based on a pivot element, recursively sorts them, and then combines them back together.
Base Case: If the array has 1 or 0 elements, it's already sorted.
Pivot Selection: We select the middle element as the pivot.
Partitioning: The array is divided into three parts:
Elements smaller than the pivot
Elements equal to the pivot
Elements greater than the pivot
Recursive Sorting: The quick_sort function is called recursively on the left and right parts of the array.
Time Complexity: O(n log n) on average, but can degrade to O(n^2) in the worst case if the pivot is not chosen well.
"""