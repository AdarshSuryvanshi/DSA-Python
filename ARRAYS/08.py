# Function to count how many times a character appears in a string
def count_occurrences(c, s):
    count = 0  # Variable to store the count of the character
    for char in s:  # Loop through each character in the string
        if char == c:  # If the character matches the input character
            count += 1  # Increment the count
    return count  # Return the final count

# Taking user input for the character to search
c = input("Enter the character you want to check: ")

# Define the string (array of characters)
s = "ababacd"

# Calling the function to count occurrences
result = count_occurrences(c, s)

# Display the result
print(f"The character '{c}' appeared {result} times in the string.")


"""
Explanation:
Function count_occurrences(c, s):

This function takes two parameters: the character c and the string s.
It loops through each character in the string and checks if it matches the input character.
If there's a match, the count is incremented.
The function returns the final count after checking the whole string.
Main Part:

The user is prompted to input a character.
A predefined string s = "ababacd" is used for testing.
The function is called, and the result is displayed.
Example Output:

Enter the character you want to check: a
The character 'a' appeared 3 times in the string.
Explanation of Code Behavior:

The function efficiently counts how many times the user-provided character appears in the string.
Time Complexity: O(n), where n is the length of the string, because we traverse the string once.
Let me know if you'd like further modifications!








"""