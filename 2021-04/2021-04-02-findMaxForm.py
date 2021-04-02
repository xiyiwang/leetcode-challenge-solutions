"""
LeetCode Challenge: Ones and Zeroes (2021-04-02)

You are given an array of binary strings strs and 
two integers m and n.

Return the size of the largest subset of strs such 
that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x 
are also elements of y.

Constraints:
- 1 <= strs.length <= 600
- 1 <= strs[i].length <= 100
- strs[i] consists only of digits '0' and '1'.
- 1 <= m, n <= 100
"""

from functools import lru_cache

class Solution:
    # runtime - 1964 ms (beats 91.94%)
    def findMaxForm(self, strs, m, n):
        s_cnt = [[s.count("0"), s.count("1")] for s in strs]

        @lru_cache(None)
        def dp(i, m, n):
            if m < 0 or n < 0: return -float("inf")
            if i == len(strs): return 0
            z, o = s_cnt[i]
            return max(1+dp(i+1, m-z, n-o), dp(i+1, m, n))
        
        return dp(0, m, n)
        