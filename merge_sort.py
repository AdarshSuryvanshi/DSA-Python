# Merge Sort Algorithm
# This function sorts an array using the merge sort method, which is a divide-and-conquer algorithm.
def merge_sort(arr):
    if len(arr) > 1:  # Base case: if the list has one or no elements, it's already sorted
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sorting the left half
        merge_sort(right_half)  # Recursively sorting the right half

        i = j = k = 0  # Initial indexes for left, right, and the merged array

        # Merging the two halves back together in sorted order
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:  # If left element is smaller, add it to the merged array
                arr[k] = left_half[i]
                i += 1
            else:  # If right element is smaller, add it to the merged array
                arr[k] = right_half[j]
                j += 1
            k += 1

        # If there are any remaining elements in the left half, add them to the merged array
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # If there are any remaining elements in the right half, add them to the merged array
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Taking user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Calling the merge_sort function
merge_sort(arr)

# Printing the sorted array
print("Sorted array is:", arr)


"""
Merge Sort is a divide-and-conquer algorithm that divides the array into two halves, recursively sorts the halves, and then merges them back together in sorted order.
Base Case: If the array has 1 or 0 elements, it is already sorted.
Divide and Conquer:
The array is split into two halves at each recursive step.
Each half is sorted recursively.
Merging: After sorting the halves, we merge them back together by comparing each element from the two halves and placing them in the correct order.
Time Complexity: O(n log n) for both the worst and average cases.


"""