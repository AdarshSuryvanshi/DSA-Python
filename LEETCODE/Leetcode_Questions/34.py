def myPow(x, n):
    if n < 0:
        x, n = 1 / x, -n  # Handle negative exponent
    res = 1
    while n:
        if n % 2:
            res = res * x  # Multiply when n is odd
        x = x* x  # Square the base
        n //= 2  # Reduce exponent
    return res

# Example Test Cases
print(myPow(2.00000, 10))  # Output: 1024.0
print(myPow(2.10000, 3))   # Output: 9.261
print(myPow(2.00000, -2))  # Output: 0.25

""" 
Why is this the best approach?
✅ Time Complexity: O(log n) (Binary Exponentiation)
✅ Space Complexity: O(1) (Constant space, no recursion)
✅ Handles negative exponents efficiently
✅ Fastest possible way to compute power


"""