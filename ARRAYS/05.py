# Program to find the largest element in an array in Python

# Main function
if __name__ == "__main__":
    # Input the size of the array
    n = int(input("Enter the value of n: "))
    
    # Initialize an empty list to store the array elements
    arr = []
    
    print("Enter the elements of the array:")
    # Take array elements as input
    for i in range(n):
        arr.append(int(input()))  # Append each input integer to the list
    
    # Initialize the largest variable to the first element of the array
    largest = arr[0]
    
    # Iterate through the array to find the largest element
    for i in range(n):
        if largest < arr[i]:  # Compare current element with the largest so far
            largest = arr[i]  # Update largest if current element is greater
    
    # Print the largest element
    print("Largest element in the array is:", largest)

"""
Explanation:
Input Handling:

The size of the array n is taken as input using int(input()).
An empty list arr is initialized to hold the array elements.
The elements are appended to the list using a loop.
Finding the Largest Element:

A variable largest is initialized with the first element of the array (arr[0]).
The loop iterates through the array, comparing each element with largest.
If an element is larger than largest, the variable is updated.
Output:

The largest element is printed after the loop completes.
Example Run:
Input:


Enter the value of n: 5
Enter the elements of the array:
10
20
5
30
15
Output:
plaintext
Copy code
Largest element in the array is: 30


"""