def reverse(x):
    """
    Reverses the digits of the integer x. 
    If the reversed number overflows, it returns 0.

    Parameters:
        x (int): The integer to be reversed.

    Returns:
        int: The reversed integer, or 0 if overflow occurs.
    """
    revnum = 0  # Initialize the reversed number as 0

    while x != 0:
        last_digit = x % 10  # Extract the last digit of x
        revnum = revnum * 10 + last_digit  # Append the last digit to revnum
        
        # Check for overflow before returning the result
        if revnum > 2**31 - 1 or revnum < -2**31:
            return 0  # Return 0 if the result overflows the 32-bit integer range
        
        x //= 10  # Remove the last digit from x (integer division)

    return revnum  # Return the reversed number

# User Input
num = int(input("Enter an integer to reverse: "))

# Function Call
result = reverse(num)

# Output the result
print(f"The reversed number is: {result}")

"""
Explanation:
revnum Initialization: We initialize revnum to 0, which will hold the reversed number.

Loop Through Digits:

We extract the last digit of x using the modulus operator (x % 10).
We update revnum by multiplying it by 10 (shifting the digits left) and adding the last digit.
Overflow Check:

Before updating revnum, we check if it exceeds the 32-bit integer limits (-2^31 to 2^31 - 1).
If it does, we return 0 to indicate an overflow.
Remove Last Digit: We reduce x by performing integer division (x //= 10), which removes the last digit.

Return: Finally, after the loop finishes, we return revnum, which contains the reversed number.

Example Walkthrough:
Input:
plaintext
Copy code
Enter an integer to reverse: -123
Process:
Start with x = -123 and revnum = 0.
Extract the last digit: last_digit = -123 % 10 = -3, update revnum = 0 * 10 + (-3) = -3.
Update x = -123 // 10 = -12.
Repeat for -12 and -1, until x == 0.
Output:
plaintext
Copy code
The reversed number is: -321
Complexity:
Time Complexity: 
O(log to the base 10 n), where 

n is the number of digits in the integer 

x. This is because we process each digit once.
Space Complexity: 
O(1), as we only use a few variables (constant space).

"""