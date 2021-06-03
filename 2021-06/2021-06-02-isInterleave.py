"""
LeetCode Challenge: Interleaving String (2021-06-02)

Given strings s1, s2, and s3, find whether s3 is formed by an 
interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where 
they are divided into non-empty substrings such that:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or 
  t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Constraints:
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional 
memory space?
"""

class Solution:
    # DP
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        
        dp = [False for _ in range(len(s2) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == j == 0: dp[j] = True
                elif i == 0: dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0: dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                else: dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[-1]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
# True

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
# False

s1 = ""
s2 = ""
s3 = ""
# True
