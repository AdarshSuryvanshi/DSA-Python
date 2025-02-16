""" 
Approach to Solve the Problem
We need to reverse a given integer 

x, ensuring that the reversed value stays within the 32-bit signed integer range 
. If it overflows, return 0.

Step-by-Step Plan
Handle Negative Numbers:

If 
x is negative, extract the absolute value, reverse it, and then add back the negative sign.
Reverse Digits Using Modulo and Division:

Extract the last digit using x % 10.
Append this digit to the reversed number.
Remove the last digit using integer division x // 10.
Check for Overflow:

If the reversed number exceeds 2^{31}-1 (2147483647), return 0.
If it goes below -2^{31} (-2147483648), return 0.
Dry Run
Example 1
🔹 Input: x = 123
🔹 Expected Output: 321

Step	x	last_digit = x % 10	reversed_num
1	123	3	3
2	12	2	32
3	1	1	321
4	0 (done)	-	321 ✅
🔹 Output: 321

Example 2
🔹 Input: x = -123
🔹 Expected Output: -321

Step	x	last_digit	reversed_num
1	-123	3	3
2	-12	2	32
3	-1	1	321
4	0 (done)	-	-321 ✅
🔹 Output: -321

Example 3
🔹 Input: x = 120
🔹 Expected Output: 21

Step	x	last_digit	reversed_num
1	120	0	0
2	12	2	2
3	1	1	21
4	0 (done)	-	21 ✅
🔹 Output: 21
"""

def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    rev = 0
    sign = -1 if x < 0 else 1  # Handle negative numbers
    x = abs(x)
    
    while x != 0:
        last_digit = x % 10
        x //= 10
        
        # Check for overflow before updating rev
        if rev > (INT_MAX - last_digit) // 10:
            return 0
        
        rev = rev * 10 + last_digit
    
    return sign * rev
""" 
Edge Cases
x = 0 → Output: 0
x = 1000000003 (Overflow) → Output: 0
x = -2147483412 (Valid within range) → Output: -2143847412
x = 1534236469 (Overflows after reversal) → Output: 0

"""