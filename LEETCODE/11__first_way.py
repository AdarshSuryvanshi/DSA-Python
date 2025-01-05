def isPalindrome(s):
    """
    Checks if a given string s is a palindrome, ignoring non-alphanumeric characters
    and case differences. A palindrome reads the same forward and backward.

    Parameters:
        s (str): The input string to check.

    Returns:
        bool: True if s is a palindrome, False otherwise.
    """
    left = 0  # Initialize left pointer to the start of the string
    right = len(s) - 1  # Initialize right pointer to the end of the string

    while left < right:
        # Move left pointer to the next valid character (alphanumeric)
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to the previous valid character (alphanumeric)
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case insensitive)
        if s[left].lower() != s[right].lower():
            return False  # If characters don't match, return False
        
        # Move the pointers inward after the comparison
        left += 1
        right -= 1
    
    return True  # If no mismatches are found, return True

# User Input
input_string = input("Enter a string to check if it's a palindrome: ")

# Function Call
result = isPalindrome(input_string)

# Output the result
if result:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

"""
Explanation:
Pointers:

Two pointers, left and right, are used to traverse the string from both ends.
Skipping Non-Alphanumeric Characters:

The isalnum() function is used to skip over characters that are not letters or digits, ensuring that only alphanumeric characters are compared.
Case Insensitivity:

The lower() function ensures that the comparison is case-insensitive, so 'A' and 'a' are considered the same.
Pointers Move Towards Each Other:

After comparing the characters at the left and right pointers, both pointers are moved inward and the process repeats until the middle of the string is reached.
Final Check:

If the characters at the left and right pointers match throughout the string, the function returns True, indicating the string is a palindrome. If any mismatch is found, it returns False.
Example Walkthrough:
Input:
plaintext
Copy code
Enter a string to check if it's a palindrome: A man, a plan, a canal, Panama
Process:
The left pointer starts at 'A', and the right pointer starts at 'a'.
Non-alphanumeric characters (like spaces, commas) are skipped.
The characters 'A' and 'a' are compared and match (ignoring case).
This continues until the middle of the string is reached, with no mismatches found.
Output:
plaintext
Copy code
'A man, a plan, a canal, Panama' is a palindrome.
Complexity:
Time Complexity: 
𝑂
(
𝑛
)
O(n), where 
𝑛
n is the length of the string. The algorithm goes through the string once, comparing characters.
Space Complexity: 
𝑂
(
1
)
O(1), as only a few variables (pointers and counters) are used.

"""