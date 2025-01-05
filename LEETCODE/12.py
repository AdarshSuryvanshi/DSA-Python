def fib(n):
    """
    Computes the nth Fibonacci number using recursion.

    Parameters:
        n (int): The position of the desired Fibonacci number.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:  # Base case: return n if n is 0 or 1
        return n
    return fib(n - 1) + fib(n - 2)  # Recursively sum the previous two Fibonacci numbers

# User Input
n = int(input("Enter a number to calculate the Fibonacci number: "))

# Function Call
result = fib(n)

# Output the result
print(f"The {n}th Fibonacci number is: {result}")

"""
Explanation:
Base Case:

If n is 0 or 1, the function simply returns n because the Fibonacci sequence starts with 0 and 1.
Recursive Case:

For values of n greater than 1, the function returns the sum of the two preceding Fibonacci numbers, recursively calling fib(n-1) and fib(n-2).
Input and Output:

The program prompts the user to input a number and then calls the fib() function to calculate the Fibonacci number for that input.
The result is printed to the screen.
Example Walkthrough:
Input:
plaintext
Copy code
Enter a number to calculate the Fibonacci number: 5
Process:
The function calculates the Fibonacci number for 5 using recursion.
fib(5) = fib(4) + fib(3)
fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib(1)
fib(2) = fib(1) + fib(0)
As the recursion reaches the base case (fib(1) and fib(0)), it starts returning values and adds them up.
Output:
plaintext
Copy code
The 5th Fibonacci number is: 5
Complexity:
Time Complexity: 
𝑂
(
2
𝑛
)
O(2 
n
 ) due to the exponential growth of recursive calls. Each call to fib(n) results in two more calls, leading to a tree of calls.
Space Complexity: 
𝑂
(
𝑛
)
O(n) because the maximum depth of the recursion stack is n.

"""