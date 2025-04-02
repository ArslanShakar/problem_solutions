def is_valid(s: str) -> bool:
    stack = []
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'  # Get last open bracket
            if bracket_map[char] != top_element:
                return False  # Mismatched bracket
        else:
            stack.append(char)  # Push open bracket onto stack
            a = 0

    return not stack  # Valid if stack is empty


def is_valid_alt(s: str) -> bool:
    stack = []
    bracket_map = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for char in s:
        if char in bracket_map:
            stack.append(char)  # Push open bracket onto stack
            a = 0
        else:
            top_element = stack.pop() if stack else '#'  # Get last open bracket
            if bracket_map[top_element] != char:
                return False  # Mismatched bracket

    return not stack  # Valid if stack is empty


# Example usage:
# print(is_valid("()"))  # True
# print(is_valid("()[]{}"))  # True
# print(is_valid("(]"))  # False
# print(is_valid("([)]"))  # False
# print(is_valid("{[]}"))  # True
# print(is_valid("({)}"))  # False
# print(is_valid("[(()[]){}]"))  # True
print(is_valid_alt("[(()[]){}]"))  # True
print(is_valid_alt("[(()[]){})(]"))  # False
