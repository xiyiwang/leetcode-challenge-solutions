"""
LeetCode Challenge: Palindromic Substrings (2021-03-27)

Given a string, your task is to count how many palindromic 
substrings in this string.

The substrings with different start indexes or end indexes 
are counted as different substrings even they consist of 
same characters.

Note:
- The input string length won't exceed 1000.
"""
# Runtime: 380 ms (N^3) - this isn't optimal
def countSubstrings(s):
    ans = len(s)
    for (i, char) in enumerate(s):
        next_char = s.find(char, i+1)
        while next_char != -1:
            sub_string = s[i:next_char+1]
            if sub_string == sub_string[::-1]: ans += 1
            next_char = s.find(char, next_char+1)
    return ans


# Expand around center: runtime - 116 ms (N^2)
def countSubstrings2(s):
    def helper(i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i, j = i - 1, j + 1
        return (j-i)//2
    return sum(helper(k,k) + helper(k,k+1) for k in range(len(s)))
