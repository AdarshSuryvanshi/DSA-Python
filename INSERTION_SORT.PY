# Insertion Sort Algorithm
# This function sorts a list in ascending order using the insertion sort technique.
def insertion_sort(arr):
    # Start with the second element (index 1) because the first element is already "sorted" by itself
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted into the sorted portion of the list
        j = i - 1  # Index for comparing the elements before the current element
        
        # Move elements of arr[0..i-1] that are greater than the key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift the larger element to the right
            j -= 1  # Move to the next element to the left
        
        arr[j + 1] = key  # Place the key in its correct position

# Taking user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Calling the insertion_sort function
insertion_sort(arr)

# Printing the sorted array
print("Sorted array is:", arr)


"""
Insertion Sort works by dividing the list into a sorted portion and an unsorted portion. It picks the elements from the unsorted portion one by one and places them in the correct position in the sorted portion.
Key is the element from the unsorted portion that we're trying to insert into the sorted portion.
Inner loop shifts all elements larger than the key one position to the right, making space for the key.
Time Complexity: The worst-case and average-case time complexity is O(n^2), but it performs well on smaller lists or nearly sorted lists.



"""