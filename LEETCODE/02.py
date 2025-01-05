def remove_duplicates(nums):
    """
    Function to remove duplicates from a sorted list in-place.
    Returns the number of unique elements.
    """
    # Edge case: If the list is empty, return 0
    if len(nums) == 0:
        return 0

    # Variable to track the position of the next unique element
    k = 1 # TO count the total number of Unique elements .... and K=1 becoz , we assume that 1st element is alredy "Unique " check from next one  
    # Start from the second element

    # Traverse the array starting from the second element
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # Check if the current element is unique
            nums[k] = nums[i]      # Update the position of the next unique element
            k += 1                 # Increment the count of unique elements

    return k  # Return the count of unique elements


# Taking user input for the sorted array
print("Enter the elements of the sorted array separated by spaces:")
nums = list(map(int, input().split()))  # Convert space-separated input into a list of integers

# Call the function and get the count of unique elements
unique_count = remove_duplicates(nums)

# Print the result
print(f"The number of unique elements is: {unique_count}")
print("The array after removing duplicates is:", nums[:unique_count])

"""
Key Points:
User Input: The code accepts a space-separated input list of integers, assuming the input is already sorted.
Logic:
Starts with the second element (k = 1) and checks for duplicates by comparing the current element with the previous one.
Updates the list in place to retain only unique elements.
Output:
Displays the number of unique elements.
Prints the modified array containing only the unique elements up to the returned count
"""