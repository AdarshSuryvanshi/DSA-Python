""" 
Valid Palindrome - LeetCode 125
We need to check if a given string is a palindrome after:

Converting all uppercase letters to lowercase.
Removing all non-alphanumeric characters.
A palindrome reads the same forward and backward.

Approach: Two-Pointer Method
Step 1: Use two pointers, one starting from the beginning and the other from the end.
Step 2: Move the pointers until they both point to alphanumeric characters.
Step 3: Compare characters at both positions.
Step 4: If they mismatch, return False; otherwise, continue.
Step 5: If pointers meet, return True
"""

## 1st Approch By using  ""Slicing"" 
import re

def isPalindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test Cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
print(isPalindrome(" "))  # Output: True

"""
Complexity Analysis
✅ Time Complexity: O(n) (String slicing takes linear time)
✅ Space Complexity: O(n) (A new reversed string is created)

This approach is simple and elegant, but it requires extra space to store the reversed string. If you want an in-place solution, the two-pointer method is better. 🚀

"""
## 2nd Approch By using  ""Regular Expression"" By Two Pointer Approach 
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1  # Skip non-alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1  # Skip non-alphanumeric
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True

# Test Cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
print(isPalindrome(" "))  # Output: True

""" 
Complexity Analysis
✅ Time Complexity: O(n) (We iterate the string once)
✅ Space Complexity: O(1) (No extra storage is used)... THIS IS THE MOST OPTIMZED APPROACH 
"""

### WHAT IS THE MEANING OF ALPHA-NUMERIC AND NON-ALPHANUMERIC

""" 
Alphanumeric & Non-Alphanumeric Meaning
✔ Alphanumeric Characters:
These include letters (A-Z, a-z) and numbers (0-9).
✅ Examples:

"Hello123" → Contains only letters and numbers (Alphanumeric).
"Python3.9" → The letters Python and numbers 3 & 9 are alphanumeric, but . is not.

✖ Non-Alphanumeric Characters:
These include special characters, symbols, punctuation, and spaces that are not letters or numbers.
✅ Examples:

@, #, $, %, &, *, (, ), !, ? , space " " are non-alphanumeric.
"Hello@123!" → Contains @ and !, which are non-alphanumeric.


Practical Example in Python
import re

s = "A man, a plan, a canal: Panama"
cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s)  # Removes non-alphanumeric characters
print(cleaned_s)  # Output: AmanaplanacanalPanama


This removes spaces, punctuation, and special characters, leaving only letters and numbers.


"""