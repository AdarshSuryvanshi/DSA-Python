# Here is the Python implementation for comparing two integers n and m and returning the appropriate relation:

def compareNM(n, m):
    """
    Compares two integers n and m.
    Returns:
    - "lesser" if n < m
    - "equal" if n == m
    - "greater" if n > m
    """
    if n < m:
        return "lesser"
    elif n == m:
        return "equal"
    else:
        return "greater"

# Example Test Cases
print(compareNM(4, 8))  # Output: lesser
print(compareNM(8, 8))  # Output: equal
print(compareNM(8, 4))  # Output: greater

"""
⏳ Time Complexity
O(1) → Constant time comparison.
"""