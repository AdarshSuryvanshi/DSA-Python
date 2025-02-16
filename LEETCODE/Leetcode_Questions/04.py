# Here is the Python implementation for calculating the area based on the user's choice:

import math

def calculateArea(choice, arr):
    """
    Calculates the area of a circle or a rectangle based on the choice.
    
    Parameters:
    - choice: Integer (1 for circle, 2 for rectangle)
    - arr: List (Contains either [R] for a circle or [L, B] for a rectangle)
    
    Returns:
    - Area of the selected geometric shape.
    """
    if choice == 1:  # Area of Circle
        R = arr[0]
        return math.pi * R * R
    elif choice == 2:  # Area of Rectangle
        L, B = arr
        return L * B
    else:
        return -1  # Invalid choice

# Example Test Cases
print(calculateArea(1, [5]))     # Output: 78.53981633974483 (Area of Circle)
print(calculateArea(2, [5, 10])) # Output: 50 (Area of Rectangle)

""" 

📌 Explanation
Choice 1 → Computes area of a circle using the formula π × R² (where π = math.pi).
Choice 2 → Computes area of a rectangle using the formula L × B.
Uses list unpacking for easy extraction of L and B in case of a rectangle.
Returns -1 for invalid choices (though it's not required as per the problem).
⏳ Time Complexity
O(1) → Constant time calculations
"""