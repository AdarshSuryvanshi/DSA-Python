## ATOI 
# 🚀 String to Integer (atoi) Implementation
# 📌 Concept: Simulating atoi() function in C++
# ✅ Time Complexity: O(n) (Single pass)
# ✅ Space Complexity: O(1) (Constant extra space)

def myAtoi(s):
    s = s.lstrip()  # Remove leading whitespaces
    if not s:
        return 0  # If empty after removing spaces, return 0

    sign = 1  # Default sign is positive
    index = 0

    # Check if the first character is a sign
    if s[0] == '-':
        sign = -1
        index += 1
    elif s[0] == '+':
        index += 1

    result = 0
    while index < len(s) and s[index].isdigit():  # Read digits
        result = result * 10 + int(s[index])
        index += 1

    result *= sign  # Apply sign

    # Clamping result within 32-bit integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result

# Example Test Cases
print(myAtoi("42"))        # Output: 42
print(myAtoi("   -042"))   # Output: -42
print(myAtoi("1337c0d3"))  # Output: 1337
print(myAtoi("0-1"))       # Output: 0
print(myAtoi("words and 987"))  # Output: 0
