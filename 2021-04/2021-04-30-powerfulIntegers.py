"""
LeetCode Challenge: Powerful Integers (2021-04-30)

Given three integers x, y, and bound, return a list of all the powerful 
integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some 
integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should 
occur at most once.

Constraints:
- 1 <= x, y <= 100
- 0 <= bound <= 10^6
"""
from math import log

class Solution:
    # runtime: O(N) or O(1) - 32 ms (beats 69.17%)
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list:
        if bound < 2: return []
        if x == y == 1: return [2]
        if x == 1:
            return [1 + y**i for i in range(20) if 1 + y**i <= bound]
        if y == 1:
            return [1 + x**i for i in range(20) if 1 + x**i <= bound]
        
        i, ans = 0, set()
        while x**i + 1 <= bound:
            j = 0
            while x**i + y**j <= bound:
                ans.add(x**i + y**j)
                j += 1
            i += 1
        return list(ans)
    
    # official solution: logarithmic bounds - same runtime
    def powerfulIntegers2(self, x: int, y: int, bound: int) -> list:
        a = bound if x == 1 else int(log(bound, x))
        b = bound if y == 1 else int(log(bound, y))
        
        powerful_integers = set([])
        
        for i in range(a + 1):
            for j in range(b + 1):
                value = x**i + y**j
                if value <= bound:
                    powerful_integers.add(value)
                if y == 1:
                    break
            if x == 1:
                break
        
        return list(powerful_integers)
        