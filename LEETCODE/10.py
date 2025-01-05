def isPalindrome(x):
    """
    Checks if the integer x is a palindrome.
    A palindrome is a number that reads the same backward as forward.
    Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes.

    Parameters:
        x (int): The integer to check.

    Returns:
        bool: True if x is a palindrome, False otherwise.
    """
    # Step 1: Handle edge cases
    if x < 0 or (x % 10 == 0 and x != 0):  # Negative numbers and multiples of 10 (except 0) are not palindromes
        return False
    
    revnum = 0  # Initialize reversed number to 0
    
    # Step 2: Reverse half of the number
    while x > revnum:
        last_digit = x % 10  # Get the last digit
        revnum = revnum * 10 + last_digit  # Append the last digit to revnum
        x //= 10  # Remove the last digit from x
    
    # Step 3: Check if the number is a palindrome
    return x == revnum or x == revnum // 10  # Handle odd-length numbers

# User Input
num = int(input("Enter an integer to check if it's a palindrome: "))

# Function Call
result = isPalindrome(num)

# Output the result
if result:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
"""
Explanation:
Edge Case Handling:

If the number is negative or ends with a zero (except for zero itself), it can't be a palindrome, so we return False immediately.
Reversing Half of the Number:

We reverse only half of the digits of the number. The reason is that, for numbers with even digits, the reversed half should match the original first half. For numbers with odd digits, the middle digit doesn't affect the palindrome property.
We keep extracting the last digit of x and build the reversed number revnum.
Check Palindrome:

If x equals revnum, the number is a palindrome.
If the number has an odd length, we compare x with revnum // 10 (to discard the middle digit).
Example Walkthrough:
Input:
plaintext
Copy code
Enter an integer to check if it's a palindrome: 121
Process:
Start with x = 121 and revnum = 0.
Extract last digits: 1, update revnum = 1, then x = 12.
Extract last digits: 2, update revnum = 12, then x = 1.
Now x = 1 and revnum = 12. The loop ends.
Check if x == revnum // 10, which is true (x == 121).
Output:
plaintext
Copy code
121 is a palindrome.
Complexity:
Time Complexity: 
𝑂
(
log
⁡
10
𝑛
)
O(log to the base 10 n), where 

n is the number of digits in the integer x. We process each digit once.
Space Complexity: 

O(1), as we only use a few variables (constant space).

"""