# LeetCode Challenge: Valid Parentheses (01/20/2021)

def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.keys():
            top_element = stack.pop() if stack else '#'
            print(mapping[char])
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
    