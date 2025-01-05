# Function to check if the array can be sorted by a single rotation
def check_rotation(nums):
    # Get the size of the array
    n = len(nums)
    
    # If the array has 0 or 1 element, it is sorted by default
    if n <= 1:
        return True

    # Variable to count the number of order violations
    count = 0

    # Traverse the array to check for order violations
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            count += 1
            # If more than one violation, the array cannot be sorted by rotation
            if count > 1:
                return False

    # If there is exactly one violation, check the rotation condition
    if count == 1:
        # If the first element is smaller than the last, rotation is not possible
        if nums[0] < nums[n - 1]:
            return False

    # If no violations or the array satisfies the rotation condition, return True
    return True


# Taking user input for the array
print("Enter the elements of the array separated by spaces:")
nums = list(map(int, input().split()))  # Convert space-separated input into a list of integers

# Call the function and print the result
if check_rotation(nums):
    print("The array can be sorted by a single rotation.")
else:
    print("The array cannot be sorted by a single rotation.")
