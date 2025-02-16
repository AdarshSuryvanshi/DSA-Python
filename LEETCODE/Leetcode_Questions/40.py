## Infix to Postfix 
def infixToPostfix(s: str) -> str:
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # Operator precedence
    stack = []  # Stack for operators
    output = []  # Resultant postfix expression

    for char in s:
        if char.isalnum():  # If character is an operand (A-Z, a-z, 0-9)
            output.append(char)
        elif char == '(':  # Push '(' to stack
            stack.append(char)
        elif char == ')':  # Pop until '(' is found
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator encountered
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[char]:
                output.append(stack.pop())  # Pop higher or equal precedence operators
            stack.append(char)  # Push current operator

    # Pop remaining operators from stack
    while stack:
        output.append(stack.pop())

    return "".join(output)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  2) 
def precedence(c):
    """Returns precedence of operators."""
    if c == '^':
        return 3
    elif c in ('*', '/'):
        return 2
    elif c in ('+', '-'):
        return 1
    return -1

def infix_to_postfix(expression):
    """Converts an infix expression to postfix notation."""
    stack = []  # Stack for operators
    postfix = []  # Output list for the postfix expression

    for char in expression:
        if char.isalnum():  # If operand, directly add to output
            postfix.append(char)
        elif char == '(':  # If '(', push to stack
            stack.append(char)
        elif char == ')':  # If ')', pop until '('
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator case
            while stack and precedence(char) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(char)

    # Pop all remaining operators from stack
    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)

# Example Usage
expression = "(p+q)*(m-n)"
print("Infix expression:", expression)
print("Postfix expression:", infix_to_postfix(expression))

