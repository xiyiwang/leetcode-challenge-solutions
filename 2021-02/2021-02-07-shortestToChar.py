# LeetCode Challenge: Shortest Distance to a Character (02/07/2021)

#   Given a string s and a character c that occurs in s, return an 
#   array of integers answer where answer.length == s.length and 
#   answer[i] is the shortest distance from s[i] to the character 
#   c in s. 
# 
#   Constraints: 
#   * 1 <= s.length <= 10^4 
#   * s[i] and c are lowercase English letters. 
#   * c occurs at least once in s.

#   Submission Detail:
#   * Runtime: 40 ms (better than 82.09% of python3 submissions)
#   * Memory Usage: 14.3 MB (better than 85.62% of python3 submissions)

def shortestToChar(s: str, c: str):
    n = len(s)
    ans = [None]*n
    c_idx = [i for i, char in enumerate(s) if char == c]
    prev_c = -n
    next_c = c_idx.pop(0)

    for i in range(n):
        ans[i] = min(i - prev_c, next_c - i)
        if i == next_c:
            prev_c = next_c
            if c_idx: next_c = c_idx.pop(0)
            else:     next_c = n*2

    return ans
