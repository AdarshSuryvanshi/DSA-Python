# Bubble Sort in Python
# This program sorts an array using Bubble Sort and finds the largest element.

def bubble_sort(arr):
    """
    Function to sort an array using the Bubble Sort algorithm.
    Args:
    arr (list): List of integers to be sorted.

    Returns:
    None: The array is sorted in place.
    """
    n = len(arr)  # Length of the array
    # Outer loop runs from the end of the array to the beginning
    for i in range(n - 1, 0, -1):  
        for j in range(i):  # Compare elements up to the sorted portion
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Main function to take input and display output
if __name__ == "__main__":
    # Input the size of the array
    n = int(input("Enter the value of n: "))
    
    # Initialize an empty list to hold the array elements
    arr = []
    print("Enter the elements of the array:")
    # Input the array elements
    for i in range(n):
        arr.append(int(input()))  # Append each input integer to the list
    
    # Call the bubble_sort function to sort the array
    bubble_sort(arr)
    
    # Display the sorted array
    print("Sorted Array:")
    for num in arr:
        print(num, end=" ")
    print()  # Newline after printing the array
    
    # Display the largest element in the array
    print("Largest element in the array is:", arr[-1])

"""
Python-Specific Features:

The list data type is used for the array.
Swapping elements is done using tuple unpacking for simplicity: arr[j], arr[j + 1] = arr[j + 1], arr[j].




"""