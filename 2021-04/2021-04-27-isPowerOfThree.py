"""
LeetCode Challenge: Power of Three (2021-04-27)

Given an integer n, return true if it is a power of three. 
Otherwise, return false.

An integer n is a power of three, if there exists an integer 
x such that n == 3^x.

Constraints:
- -2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion? 
"""

# runtime: 72 ms (beats 76.88%)
class Solution:
    powerOfThree = {3**_ for _ in range(1289)}
    
    def isPowerOfThree(self, n: int) -> bool:
        return n in self.powerOfThree

class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        return 0 if n <= 0 else 1162261467 % n == 0
