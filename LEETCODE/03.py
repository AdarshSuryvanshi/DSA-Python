def remove_duplicates(nums):
    """
    Function to remove duplicates from a sorted list such that each element appears at most twice.
    Returns the number of elements in the modified list.
    """
    # If the list size is less than or equal to 2, no need to process
    if len(nums) <= 2:
        return len(nums)

    # Variable to track the position of the next valid element
    k = 2  # Start from the third position, as the first two elements are always valid

    # Traverse the list starting from the third element
    for i in range(2, len(nums)):
        # Check if the current element is different from the element two positions back
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]  # Place the current element at the kth position
            k += 1  # Increment the count of valid elements

    return k  # Return the number of elements in the modified list


# Taking user input for the sorted array
print("Enter the elements of the sorted array separated by spaces:")
nums = list(map(int, input().split()))  # Convert space-separated input into a list of integers

# Call the function to remove duplicates and get the new length
new_length = remove_duplicates(nums)

# Print the result
print(f"The number of elements in the modified array is: {new_length}")
print("The array after processing is:", nums[:new_length])

"""
User Input:
Takes a sorted array as input, entered as space-separated integers.
Logic:
If the array has 2 or fewer elements, it is directly valid.
For each element starting from index 2, checks if it is different from the element two positions back.
Places valid elements in the array in place and increments the count of valid elements.
Output:
Prints the number of valid elements and the modified array up to the valid length.

"""