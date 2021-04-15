from functools import lru_cache


"""
LeetCode Challenge: Fibonacci Number (2021-04-15)

The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the 
sum of the two preceding ones, starting from 0 and 1. 

Given n, calculate F(n).

Constraints:
- 0 <= n <= 30
"""
class Solution:
    # dynamic programming: O(n) - beats 83.28%
    def fib(self, n: int) -> int:
        if n <= 1: return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
    
    # 2-line solution with memoization: O(n)
    from functools import lru_cache
    @lru_cache
    def fib2(self, n: int) -> int:
        return n if n <= 1 else self.fib2(n-2) + self.fib2(n-1)
