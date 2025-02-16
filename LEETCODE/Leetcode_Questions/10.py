""" 
Approach to Solve the Problem
We need to compute the sum of all divisors for each number from 1 to n and return the total sum.

Brute Force Approach (O(n²))
For each number 
𝑖
i from 1 to n, find all its divisors and sum them.
This approach iterates over all numbers and checks for divisibility, leading to O(n²) complexity, which is inefficient for large values of 
𝑛
n.
Optimized Approach (O(n log n))
Instead of iterating for each 
𝑖
i, we can optimize by:

Reversing the approach: Instead of computing divisors for each number, we iterate over potential divisors and sum their contributions.
Observation: A divisor 
𝑑
d contributes to all its multiples.
Efficient Calculation: Iterate over each divisor 
𝑑
d from 1 to n, and for each 
𝑑
d, add 
𝑑
d to all its multiples.
Using this approach, we achieve O(n log n) time complexity, which is efficient for large 
𝑛
n.

Dry Run
Example 1: 
𝑛
=
4
n=4
𝐹
(
1
)
=
1
F(1)=1
𝐹
(
2
)
=
1+2=3
F(2)=1+2=3
𝐹
(
3
)
=
1
+
3
=
4
F(3)=1+3=4
𝐹
(
4
)
=
1
+
2
+
4
=
7
F(4)=1+2+4=7
Total sum = 1 + 3 + 4 + 7 = 15

Example 2: 
𝑛
=
5
n=5
𝐹
(
1
)
=
1
F(1)=1
𝐹
(
2
)
=
1
+
2
=
3
F(2)=1+2=3
𝐹
(
3
)
=
1
+
3
=
4

NOTE :- 
Example 2: 
𝑛
=
5
n=5
𝐹
(
1
)
=
1
F(1)=1
𝐹
(
2
)
=
1
+
2
=
3
F(2)=1+2=3
𝐹
(
3
)
=
1
+
3
=
4
F(3)=1+3=4
𝐹
(
4
)
=
1
+
2
+
4
=
7
F(4)=1+2+4=7
𝐹
(
5
)
=
1
+
5
=
6
F(5)=1+5=6
Total sum = 1 + 3 + 4 + 7 + 6 = 21

 


"""
def sumOfDivisors(n):
    # Array to store sum of divisors
    divisors = [0] * (n + 1)
    
    # Compute sum of divisors for each i
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):  # Adding i to all multiples of i
            divisors[j] += i
            
    return sum(divisors)  # Summing up all F(i)

# Test Cases
print(sumOfDivisors(4))  # Output: 15
print(sumOfDivisors(5))  # Output: 21
print(sumOfDivisors(1))  # Output: 1

""" 
Complexity Analysis
✅ Time Complexity: O(n log n) (Each divisor contributes to its multiples)
✅ Space Complexity: O(n) (Using an array to store divisor sums)


"""