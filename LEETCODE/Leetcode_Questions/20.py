## Q) Find Second Smallest and Second Largest Element in an array

## 1) st Approach :- Slicing/ Array Method 
def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    arr.sort()
    small = arr[1]
    large = arr[n-2]
    print("Second smallest is", small)
    print("Second largest is", large)


if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    getElements(arr, n)

""" 
Time Complexity: O(NlogN), For sorting the array

Space Complexity: O(1)
"""

## 2)  Better Approach :- 

def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)




if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    getElements(arr, n)

""" 
Time Complexity: O(N), We do two linear traversals in our array

Space Complexity: O(1)
"""
 ## 3) Optimal Approach :- 

 


def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small




def secondLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large




if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]
    n = len(arr)
    sS = secondSmallest(arr, n)
    sL = secondLargest(arr, n)
    print("Second smallest is", sS)
    print("Second largest is", sL)


