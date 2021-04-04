"""
LeetCode Challenge: Longest Valid Parentheses (2021-04-03)

Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) 
parentheses substring.

Constraints:
- 0 <= s.length <= 3 * 10^4
- s[i] is '(', or ')'.
"""

class Solution:
    # runtime - 52 ms (beats 26.61%)
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for (i, b) in enumerate(s):
            if b == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        
        return ans
