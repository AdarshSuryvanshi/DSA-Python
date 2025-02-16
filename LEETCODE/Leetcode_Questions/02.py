# Here is the Python implementation for determining the size of a given data type in bytes:
def dataTypeSize(data_type):
    """
    Returns the size of the given data type in bytes.
    If the data type is invalid, returns -1.
    """
    size_map = {
        "Character": 1,  # In Python, it's 1 byte (Java uses 2 bytes)
        "Integer": 4,
        "Long": 8,
        "Float": 4,
        "Double": 8
    }
    
    return size_map.get(data_type, -1)  # Return size if valid, else -1

# Example Test Cases
print(dataTypeSize("Character"))  # Output: 1
print(dataTypeSize("Integer"))    # Output: 4
print(dataTypeSize("Long"))       # Output: 8
print(dataTypeSize("Float"))      # Output: 4
print(dataTypeSize("Double"))     # Output: 8
print(dataTypeSize("String"))     # Output: -1 (Invalid data type)

""" 
📌 Explanation
Using a Dictionary (size_map) to store the byte sizes of different data types.
get(data_type, -1) fetches the value if the key exists, else returns -1 for invalid input
"""
""" 
⏳ Time Complexity
O(1) → Constant time lookup using a dictionary.

"""

#🚀 Alternative Approach (Using if-elif conditions) 
def dataTypeSize(data_type):
    if data_type == "Character":
        return 1
    elif data_type == "Integer":
        return 4
    elif data_type == "Long":
        return 8
    elif data_type == "Float":
        return 4
    elif data_type == "Double":
        return 8
    else:
        return -1

# This method works but is less efficient than using a dictionary (O(1) lookup)