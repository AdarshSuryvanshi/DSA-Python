# Here is the Python implementation for passing values by value and by reference:
def passedBy(a, b):
    """
    Simulates pass-by-value and pass-by-reference behavior.

    - a is passed by value (increment by 1)
    - b is passed by reference (increment by 2)

    Parameters:
    - a (int): Value passed by value
    - b (int): Value passed by reference
    
    Returns:
    - List containing updated values of a and b
    """
    a = a + 1   # Pass-by-value (local modification)
    b = b + 2   # Simulated pass-by-reference (modification in function)

    return [a, b]

# Example Test Cases
print(passedBy(1, 2))   # Output: [2, 4]
print(passedBy(10, 20)) # Output: [11, 22]

""" 
📌 Explanation
Pass-by-Value (a):

The function creates a new copy of a and increments it by 1.
Changes do not affect the original variable outside the function.

Pass-by-Reference (b):
In Python, integers are immutable, so we simulate pass-by-reference by modifying b directly inside the function.
Here, b is incremented by 2 before returning.
⏳ Time Complexity
O(1) → Constant time operations.
"""

""" 
Example 1
🔹 Input: n = 12
🔹 Expected Output: 2

Step-by-Step Dry Run
Step	Action	Value
1	Convert n to string	"12"
2	Initialize count = 0	count = 0
3	Iterate over each digit	"1", "2"
4	Convert "1" to integer	d = 1
5	Check 12 % 1 == 0	✅ Yes, so count = 1
6	Convert "2" to integer	d = 2
7	Check 12 % 2 == 0	✅ Yes, so count = 2
8	No more digits left	Final count = 2
🔹 Output: 2 ✅

Example 2
🔹 Input: n = 2446
🔹 Expected Output: 1

Step-by-Step Dry Run
Step	Action	Value
1	Convert n to string	"2446"
2	Initialize count = 0	count = 0
3	Iterate over each digit	"2", "4", "4", "6"
4	Convert "2" to integer	d = 2
5	Check 2446 % 2 == 0	✅ Yes, so count = 1
6	Convert "4" to integer	d = 4
7	Check 2446 % 4 == 0	❌ No, so count remains 1
8	Convert "4" to integer (again)	d = 4
9	Check 2446 % 4 == 0	❌ No, so count remains 1
10	Convert "6" to integer	d = 6
11	Check 2446 % 6 == 0	❌ No, so count remains 1
12	No more digits left	Final count = 1
🔹 Output: 1 ✅

Example 3
🔹 Input: n = 23
🔹 Expected Output: 0

Step-by-Step Dry Run
Step	Action	Value
1	Convert n to string	"23"
2	Initialize count = 0	count = 0
3	Iterate over each digit	"2", "3"
4	Convert "2" to integer	d = 2
5	Check 23 % 2 == 0	❌ No, so count = 0
6	Convert "3" to integer	d = 3
7	Check 23 % 3 == 0	❌ No, so count = 0
8	No more digits left	Final count = 0
🔹 Output: 0 ✅

Key Observations
✅ Convert number to string for easy iteration.
✅ Ignore 0 since division by zero is undefined.
✅ Keep a count of digits that evenly divide 
𝑛
n.
✅ The logic runs in O(d) time complexity, where 
𝑑
d is the number of digits in 
𝑛
n.


"""