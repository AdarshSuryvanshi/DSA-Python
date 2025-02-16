# Here is the Python implementation for counting digits that divide n evenly:

def countDividingDigits(n):
    """
    Counts the number of digits in n that evenly divide n.

    Parameters:
    - n (int): The given positive integer

    Returns:
    - int: Count of digits that evenly divide n
    """
    count = 0
    for digit in str(n):  # Convert number to string to iterate over digits
        d = int(digit)  # Convert back to integer
        if d != 0 and n % d == 0:  # Check if it divides n evenly
            count += 1
    return count

# Example Test Cases
print(countDividingDigits(12))   # Output: 2
print(countDividingDigits(2446)) # Output: 1
print(countDividingDigits(23))   # Output: 0

""" 
📌 Explanation
Convert n to a string to iterate over each digit.
Convert each character back to an integer.
Check conditions:
Ignore 0 (as division by zero is undefined).
Check if n % d == 0, meaning 

d divides 

n evenly.
Keep a count of such digits and return the result.
⏳ Time Complexity
O(d) → Where 
d is the number of digits in 
n (at most 5 since n ≤ 10 raise to 5 ).

"""

