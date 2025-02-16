# Recursive Approach to Print Numbers from 1 to n
 
def printNos(n):
    if n == 0:
        return
    printNos(n - 1)  # Recursive call to print numbers before n
    print(n, end=" ")  # Print n after recursive calls

# Test Cases
printNos(10)  # Output: 1 2 3 4 5 6 7 8 9 10
print()  # Newline for clarity
printNos(5)   # Output: 1 2 3 4 5
print()  # Newline for clarity
printNos(1)   # Output: 1

"""
Complexity Analysis
✅ Time Complexity: O(n) (One function call per number)
✅ Space Complexity: O(n) (Recursive stack for n calls)


"""