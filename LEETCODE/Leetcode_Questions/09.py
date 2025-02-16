""" 
Approach to Solve LCM and GCD
To compute the LCM (Least Common Multiple) and GCD (Greatest Common Divisor) of two numbers 

a and b, we use:

GCD Calculation using Euclidean Algorithm

The GCD of two numbers can be found using:
GCD
(𝑎 ,𝑏
)
=
GCD
(
𝑏
,
𝑎
m
o
d
 
 
𝑏
)
GCD(a,b)=GCD(b,amodb)
Base case: If 
𝑏
=
0
b=0, return 
𝑎
a.
LCM Calculation using GCD

Formula for LCM:
LCM
(
𝑎
,
𝑏
)
=
𝑎
×
𝑏
GCD
(
𝑎
,
𝑏
)
LCM(a,b)= 
GCD(a,b)
a×b
​
 
This formula avoids overflow by first dividing one number by GCD.
Dry Run
Example 1
🔹 Input: a = 5, b = 10
🔹 Expected Output: [10, 5]

Step 1: Compute GCD(5, 10)
Using Euclidean Algorithm:

GCD(5, 10) = GCD(10, 5) (swap because b > a)
GCD(10, 5) = GCD(5, 0) (since 10 % 5 = 0)
✅ GCD = 5
Step 2: Compute LCM

LCM
(
5
,
10
)
=
5
×
10
5
=
10
LCM(5,10)= 
5
5×10
​
 =10
✅ Output: [10, 5]

Example 2
🔹 Input: a = 14, b = 8
🔹 Expected Output: [56, 2]

Step 1: Compute GCD(14, 8)

GCD(14, 8) = GCD(8, 14 % 8) = GCD(8, 6)
GCD(8, 6) = GCD(6, 8 % 6) = GCD(6, 2)
GCD(6, 2) = GCD(2, 6 % 2) = GCD(2, 0)
✅ GCD = 2
Step 2: Compute LCM

LCM
(
14
,
8
)
=
14
×
8
2
=
56
LCM(14,8)= 
2
14×8
​
 =56
✅ Output: [56, 2]


"""
import math

def lcmAndGcd(a: int, b: int) -> list:
    gcd = math.gcd(a, b)  # Built-in GCD function
    lcm = (a * b) // gcd  # LCM formula
    return [lcm, gcd]

# Test Cases
print(lcmAndGcd(5, 10))  # Output: [10, 5]
print(lcmAndGcd(14, 8))  # Output: [56, 2]
print(lcmAndGcd(1, 1))   # Output: [1, 1]

"""
✅ Time Complexity: 

O(logmin(a,b)) (since Euclidean GCD runs in logarithmic time).
✅ Space Complexity: 

O(1) (only a few variables are used).


"""