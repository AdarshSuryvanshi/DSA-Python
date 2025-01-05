# Function to count how many times a digit appears in the array
def count_occurrences(n, arr):
    count = 0  # Variable to store the count of the digit
    for num in arr:  # Loop through each number in the array
        if num == n:  # If the number matches the input number
            count += 1  # Increment the count
    return count  # Return the final count

# Taking user input for the digit to search
n = int(input("Enter the digit you want to check: "))

# Define the array (list of digits)
arr = [1, 3, 1, 2, 2, 5]

# Calling the function to count occurrences
result = count_occurrences(n, arr)

# Display the result
print(f"The digit {n} appeared {result} times in the array.")


"""
Function count_occurrences(n, arr):

This function takes two parameters: the digit n and the array arr.
It loops through each element in the array and checks if it matches the input digit.
If there’s a match, the count is incremented.
The function returns the final count after checking the whole array.
Main Part:

The user is prompted to input a digit.
A predefined array arr = [1, 3, 1, 2, 2, 5] is used for testing.
The function is called, and the result is displayed.
Example Output:


Enter the digit you want to check: 1
The digit 1 appeared 2 times in the array.
Explanation of Code Behavior:
The function efficiently counts how many times the user-provided digit appears in the array.
Time Complexity: O(n), where n is the length of the array, because we traverse the array once.
Let me know if you'd like further explanations or modifications!









"""