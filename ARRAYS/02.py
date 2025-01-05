# Title: Find Intersection of Two Sorted Arrays
# Concept:
# 1. The goal is to find the intersection (common elements) of two sorted arrays.
# 2. Each common element should appear only once in the result, even if it is repeated in the original arrays.
# 3. We use two approaches:
#    - **Approach 1**: Using a Python list (similar to a vector in C++).
#    - **Approach 2**: Using a fixed-size array for results (optional in Python).

# Approach 1: Using a List to Store Results

def intersection_sorted_arrays(arr1, arr2):
    """
    Function to find the intersection of two sorted arrays.
    :param arr1: List[int] - First sorted array.
    :param arr2: List[int] - Second sorted array.
    :return: List[int] - Common elements.
    """
    visited = [0] * len(arr2)  # Track if an element in arr2 has been used
    result = []  # List to store the intersection

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and not visited[j]:
                # If elements match and arr2[j] has not been used
                result.append(arr1[i])
                visited[j] = 1  # Mark arr2[j] as visited
                break  # Break as we found a match for arr1[i]
            if arr2[j] > arr1[i]:
                # Since arr2 is sorted, no need to check further
                break

    return result


# Main Function to Demonstrate the Intersection

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

    # Find the intersection
    intersection = intersection_sorted_arrays(arr1, arr2)

    # Display the result
    print("The intersection of the two arrays is: ", intersection)

# Approach 2: Using a Fixed-Size Array (Optional in Python)
# Python lists are dynamic, so a fixed-size array isn't typically necessary.
# However, if needed, we can preallocate a list of size `min(len(arr1), len(arr2))`.
