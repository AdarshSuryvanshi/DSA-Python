# Function to count the occurrences of lowercase characters in a string
def count_occurrences(s, ch):
    # Create a list to store the frequency of each lowercase letter ('a' to 'z')
    hash = [0] * 26  # Initialize a list with 26 zeros (one for each letter)
    
    # Count the frequency of each letter in the string
    for char in s:
        hash[ord(char) - ord('a')] += 1  # Increment the count for the character
        
    # Return the count of the queried character
    return hash[ord(ch) - ord('a')]

# Input the string
s = input("Enter the string you wanted: ")

# Input the number of queries
Q = int(input("Enter how many queries you want: "))

# Process each query
for _ in range(Q):
    ch = input("Enter the character: ").lower()  # Read the character and convert to lowercase
    # Output the result for the current query
    print(f"The alphabet '{ch}' appeared {count_occurrences(s, ch)} times.")


"""
Function count_occurrences(s, ch):

This function takes two parameters:
s: The input string to search in.
ch: The character whose frequency we want to count.
A list hash of length 26 is used to store the frequency of each lowercase letter ('a' to 'z').
The list is populated by iterating through the string and updating the count for each character.
The frequency of the queried character is returned by using the ASCII value of ch to find its corresponding index in the hash list.
Main Logic:

The user is prompted to input a string s.
The user is asked how many queries they want to make (Q).
For each query, the user is asked to enter a character, and the program outputs how many times that character appears in the string.
Example Output:


Enter the string you wanted: abacadaba
Enter how many queries you want: 2
Enter the character: a
The alphabet 'a' appeared 4 times.
Enter the character: b
The alphabet 'b' appeared 2 times.
Explanation of Code Behavior:
Time Complexity:
Precomputing Frequencies: O(n), where n is the length of the string.
Query Processing: O(1) for each query, since accessing the frequency list is a constant-time operation.
Space Complexity: O(1) for the hash array since its size is fixed at 26, representing the lowercase English alphabet.



"""