""" 
Optimal Approach (Using a Frequency Array)
Time Complexity: O(n)
Space Complexity: O(n)
Approach:
Create a frequency array freq of size n, initialized with zeros.
Iterate through arr[] and increment the corresponding index in freq[] (using 1-based indexing).
Return the frequency array.
"""
def frequencyCount(arr, n):
    freq = [0] * n  # Initialize frequency array with zeros
    
    for num in arr:
        freq[num - 1] += 1  # Increment frequency at correct index (1-based indexing)
    
    return freq

# Example Usage:
arr1 = [2, 3, 2, 3, 5]
print(frequencyCount(arr1, len(arr1)))  # Output: [0, 2, 2, 0, 1]

arr2 = [3, 3, 3, 3]
print(frequencyCount(arr2, len(arr2)))  # Output: [0, 0, 4, 0]

arr3 = [1]
print(frequencyCount(arr3, len(arr3)))  # Output: [1]

"""
Explanation
For arr = [2, 3, 2, 3, 5]:

Initialize freq = [0, 0, 0, 0, 0]
Process the elements:
2 → freq[1] += 1 → [0, 1, 0, 0, 0]
3 → freq[2] += 1 → [0, 1, 1, 0, 0]
2 → freq[1] += 1 → [0, 2, 1, 0, 0]
3 → freq[2] += 1 → [0, 2, 2, 0, 0]
5 → freq[4] += 1 → [0, 2, 2, 0, 1]
Final Output: [0, 2, 2, 0, 1]


"""