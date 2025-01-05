# Title: Optimized Intersection of Two Sorted Arrays
# Concept:
# 1. This approach uses two pointers (i and j) to traverse both arrays simultaneously.
# 2. The goal is to find common elements efficiently without using extra space for tracking visited elements.
# 3. Time Complexity: O(n + m), where n and m are the lengths of the two arrays.
# 4. Space Complexity: O(1) for the algorithm itself (excluding the result storage).

def intersection_sorted_arrays(arr1, arr2):
    """
    Finds the intersection of two sorted arrays using a two-pointer approach.
    :param arr1: List[int] - First sorted array.
    :param arr2: List[int] - Second sorted array.
    :return: List[int] - List containing the intersection of arr1 and arr2.
    """
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    result = []  # List to store intersection elements

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1  # Move the pointer for arr1 forward
        elif arr2[j] < arr1[i]:
            j += 1  # Move the pointer for arr2 forward
        else:  # arr1[i] == arr2[j]
            result.append(arr1[i])  # Add the common element to the result
            i += 1  # Move both pointers forward
            j += 1

    return result


# Main Function to Test the Intersection
if __name__ == "__main__":
    # Input for the first array
    n = int(input("Enter the number of elements in the first array: "))
    arr1 = []
    print("Enter elements of the first array (sorted): ")
    for _ in range(n):
        arr1.append(int(input()))

    # Input for the second array
    m = int(input("Enter the number of elements in the second array: "))
    arr2 = []
    print("Enter elements of the second array (sorted): ")
    for _ in range(m):
        arr2.append(int(input()))

    # Find the intersection of the two arrays
    intersection = intersection_sorted_arrays(arr1, arr2)

    # Display the result
    print("Intersection of the two arrays: ", " ".join(map(str, intersection)))



"""

Key Features:
Two-Pointer Technique:
Efficiently compares elements of both arrays.
Avoids unnecessary comparisons once one pointer exceeds its array's length.
No Additional Space for Visited:
Tracks unique elements directly by advancing pointers.
Reduces space complexity to 
𝑂(1)
O(1), apart from storing results.
Dynamic Lists:
Python lists handle dynamic memory management seamlessly, eliminating the need for predefining sizes.


Enter the number of elements in the first array: 5
Enter elements of the first array (sorted): 
1
2
3
4
5
Enter the number of elements in the second array: 4
Enter elements of the second array (sorted): 
2
4
6
8
Intersection of the two arrays:  2 4

"""