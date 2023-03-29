# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type.

def question4answer(s):
   # Initialize an empty stack to keep track of opening brackets
    bracket_stack = []

    # Define a mapping of opening brackets to their corresponding closing brackets
    bracket_map = {'(': ')', '[': ']', '{': '}'}

    # Iterate over each character in the input string
    for i in range(len(s)):
        char = s[i]

        # If the character is an opening bracket, push it onto the stack
        if char in bracket_map.keys():
            bracket_stack.append(char)

        # If the character is a closing bracket, check if it matches the most recently opened bracket
        elif char in bracket_map.values():
            # If there are no opening brackets on the stack, the expression is invalid
            if len(bracket_stack) == 0:
                return False
            # Pop the most recently opened bracket from the stack
            last_opened = bracket_stack.pop()
            # Check if the closing bracket matches the most recently opened bracket
            if bracket_map[last_opened] != char:
                return False

    # If there are any remaining opening brackets on the stack, the expression is invalid
    if len(bracket_stack) > 0:
        return False

    # If we make it through the entire string without returning False, the expression is valid
    return True

s = "](){}{()[]()}["
print (question4answer(s))
