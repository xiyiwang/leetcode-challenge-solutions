"""
LeetCode Challenge: Beautiful Arrangement II (2021-04-12)

Given two integers n and k, you need to construct a list which 
contains n different positive integers ranging from 1 to n and 
obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list 
[|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k 
distinct integers.

If there are multiple answers, print any of them.

Note:
- The n and k are in the range 1 <= k < n <= 10^4.
"""

class Solution:
    # runtime - O(n) - 44 ms (beats 86%)
    def constructArray(self, n: int, k: int) -> list:
        ans = [0] * n
        i = j = 0
        while j < k // 2:
            if k % 2 == 0:
                ans[i], ans[i+1] = n-j, j+1
            else:
                ans[i], ans[i+1] = j+1, n-j
            j += 1
            i += 2
        j += 1
        while i < n:
            ans[i] = j
            j += 1
            i += 1
        return ans
    
    # Official solution - construction
    def constructArray2(self, n: int, k: int) -> list:
        ans = list(range(1, n-k))
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n-k + i//2)
            else:
                ans.append(n - i//2)
        return ans
