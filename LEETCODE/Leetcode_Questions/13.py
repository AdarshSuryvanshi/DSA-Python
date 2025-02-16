""" 
Recursive Approach to Print "GFG" n Times
Since loops are not allowed, we use recursion to print "GFG" exactly n times.

Recursive Thought Process
Base Case: If n == 0, stop the recursion.
Recursive Case: Print "GFG", then make a recursive call for n-1.
"""

def printGfg(n):
    if n == 0:
        return
    print("GFG", end=" ")  # Print "GFG" without newline
    printGfg(n - 1)  # Recursive call to print remaining "GFG"

# Test Cases
printGfg(5)  # Output: GFG GFG GFG GFG GFG
print()  # Newline for clarity
printGfg(3)  # Output: GFG GFG GFG
print()  # Newline for clarity
printGfg(1)  # Output: GFG
