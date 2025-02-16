""" 
Approach to Solve the Problem
A palindrome number reads the same forwards and backwards. To check if an integer x is a palindrome, we have two methods:

Convert to String & Compare
Reverse Half of the Number (Mathematical Approach)
Method 1: Convert to String
Convert the integer x to a string.
Compare the original string with its reversed version.
If they are equal, return True; otherwise, return False.

"""
def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

""" 
✅ Time Complexity: 

O(logx) → converting and reversing a number takes 

O(logx) operations.
✅ Space Complexity: 
O(logx) → storing the string representation of x.

Method 2: Reverse Half the Number (Mathematical Approach)
Instead of converting x into a string, we reverse only half of the number and check if it matches the first half.

Steps:
Negative numbers are not palindromes, so return False if x < 0.
If the last digit is 0 but x ≠ 0 (e.g., 10, 100), return False (because leading zeros are not allowed).
Reverse half of x:
Extract the last digit using x % 10.
Build the reversed half by rev = rev * 10 + last_digit.
Reduce x by x //= 10 until x ≤ rev.
If x == rev (for even-length numbers) or x == rev // 10 (for odd-length numbers), return True.

"""