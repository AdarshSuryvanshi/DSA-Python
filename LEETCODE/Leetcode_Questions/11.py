"""
Approach to Solve the Problem
We need to determine the minimum number of jumps required to reach the last index from the first index. Each element in the array represents the maximum jump length that can be taken from that position.

Optimal Approach: Greedy Algorithm (O(n) Time)
We use a greedy approach with three key variables:

maxReach → The farthest index we can currently reach.
steps → The number of steps we can still take before needing a jump.
jumps → The total number of jumps taken.
Steps to solve:

Start from the first index.
Update maxReach as the farthest index that can be reached from the current index.
Reduce steps by 1 after moving to the next index.
If steps becomes 0, we must jump (increment jumps and update steps to maxReach - currentIndex).
If at any point maxReach is less than the current index, return -1 (indicating that we are stuck).
Stop if we reach the last index.

"""
def minJumps(arr):
    n = len(arr)
    
    # If the first element is 0, we can't move anywhere
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1
    
    maxReach = arr[0]  # Max index we can reach
    steps = arr[0]      # Steps remaining in the current jump
    jumps = 1           # Number of jumps
    
    for i in range(1, n):
        # If we reached the last index
        if i == n - 1:
            return jumps
        
        # Update maxReach
        maxReach = max(maxReach, i + arr[i])
        
        # Use a step to get to the next index
        steps -= 1
        
        # If no more steps left
        if steps == 0:
            jumps += 1  # Must jump
            
            # If the current position is beyond maxReach, return -1
            if i >= maxReach:
                return -1
            
            # Reset steps for the next jump
            steps = maxReach - i
    
    return -1

# Test Cases
print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))  # Output: 3
print(minJumps([1, 4, 3, 2, 6, 7]))  # Output: 2
print(minJumps([0, 10, 20]))  # Output: -1

"""
Complexity Analysis
✅ Time Complexity: O(n) (Single pass through the array)
✅ Space Complexity: O(1) (Only a few variables used)

This is an efficient approach suitable for large constraints (up to 
10 raise to 6 
"""