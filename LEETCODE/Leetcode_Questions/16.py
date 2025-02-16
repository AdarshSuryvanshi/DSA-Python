""" 
Here are three approaches to solving the Fibonacci number problem:

1. st Approch is "Recursive Approach "
Time Complexity: O(2ⁿ) (Exponential)
Space Complexity: O(n) (Recursion stack)

Worst Approach :- Issue: This method is inefficient for large n due to redundant calculations.
"""
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Example
print(fib(4))  # Output: 3

"""
 2. Dynamic Programming (Memoization)
Time Complexity: O(n)
Space Complexity: O(n) (for memoization storage)

✅ Improves performance by storing previously computed values.
"""
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# Example
print(fib(4))  # Output: 3

## The Optimized Code/Approach is :- 
"""
3. Iterative Approach (Optimized)
Time Complexity: O(n)
Space Complexity: O(1) (Only two variables used)

"""
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example
print(fib(4))  # Output: 3
