# LeetCode Challenge: Minimum Remove to Make Valid Parentheses (2021-02-19)

#   Given a string s of '(' , ')' and lowercase English characters.  
# 
#   Your task is to remove the minimum number of parentheses ( '(' or ')', 
#   in any positions ) so that the resulting parentheses string is valid and 
#   return any valid string. 
# 
#   Formally, a parentheses string is valid if and only if: 
#   * It is the empty string, contains only lowercase characters, or 
#   * It can be written as AB (A concatenated with B), where A and B are 
#     valid strings, or 
#   * It can be written as (A), where A is a valid string.

def minRemoveToMakeValid(s): # runtime - 88 ms (beats 89.13%)
    s_arr = list(s)
    stack = []
    for i, c in enumerate(s_arr):
        if c == "(": 
            # push all left brackets to the stack
            stack.append(i)
        elif c == ")":
            # remove the last left bracket from stack
            if stack: stack.pop()
            # or delete the right bracket if stack is empty
            else:     s_arr[i] = ""
    if stack:
        # delete all lone left brackets in the stack
        for idx in stack: s_arr[idx] = ""
    return "".join(s_arr)
